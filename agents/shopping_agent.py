"""
Athletic Shoe Shopping Agent implementation.
"""
import os
import sys
import traceback
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import BaseTool
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from typing import Dict, Any, List, Optional

# Import Anthropic modules
from anthropic import Anthropic

from utils.memory import ShoppingMemory
from utils.prompts import SHOPPING_AGENT_SYSTEM_PROMPT
from tools.search_tool import SearchTool
from tools.filter_tool import FilterTool 
from tools.recommendation_tool import RecommendationTool
from config import DEFAULT_MODEL, TEMPERATURE, ANTHROPIC_API_KEY, MAX_TOKENS

class ShoppingAgent:
    """Athletic Shoe Shopping Agent that helps users find the right athletic shoes."""
    
    def __init__(self):
        """Initialize the shopping agent with tools and memory."""
        # Initialize memory
        self.memory = ShoppingMemory()
        
        # Initialize tools
        self.tools = {
            "search": SearchTool(),
            "filter": FilterTool(),
            "recommend": RecommendationTool()
        }
        
        # Configure Anthropic API
        try:
            # Initialize the Anthropic client with the provided API key
            self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
            print(f"✅ Successfully configured Anthropic API with key: {ANTHROPIC_API_KEY[:4]}...{ANTHROPIC_API_KEY[-4:]}")
            
            # Use the configured model
            self.model = DEFAULT_MODEL
            print(f"✅ Using Anthropic model: {self.model}")
            
            # Test the API with a simple message
            test_response = self.client.messages.create(
                model=self.model,
                max_tokens=10,
                temperature=TEMPERATURE,
                messages=[
                    {"role": "user", "content": "Hello, are you working?"}
                ]
            )
            print(f"✅ Anthropic API test successful: {test_response.content[0].text[:50]}...")
        except Exception as e:
            print(f"❌ Error configuring Anthropic API: {e}")
            print(traceback.format_exc())
            raise RuntimeError(f"Failed to initialize Anthropic API: {e}")
    
    def handle_message(self, message: str) -> str:
        """
        Process a user message and generate a response.
        
        Args:
            message: The user's input message
            
        Returns:
            str: The agent's response
        """
        # Add the user message to memory
        self.memory.add_user_message(message)
        
        try:
            # Prepare chat history for context
            history_text = ""
            if self.memory.get_chat_history():
                history_text = "Previous conversation:\n"
                for msg in self.memory.get_chat_history():
                    # Access LangChain message objects correctly
                    if msg.type == "human":
                        history_text += f"User: {msg.content}\n"
                    else:
                        history_text += f"Assistant: {msg.content}\n"
            
            # Prepare user preferences for context
            preferences = self.memory.user_preferences
            preferences_text = "User preferences:\n"
            for key, value in preferences.items():
                if value:
                    if isinstance(value, list):
                        preferences_text += f"- {key}: {', '.join(value)}\n"
                    else:
                        preferences_text += f"- {key}: {value}\n"
            
            # Prepare tools information
            tools_text = "Available tools:\n"
            tools_text += "1. search - Search for athletic shoes by criteria\n"
            tools_text += "2. filter - Filter shoes by specific attributes\n"
            tools_text += "3. recommend - Get personalized shoe recommendations\n"
            
            # Build the prompt
            prompt = f"""
            {SHOPPING_AGENT_SYSTEM_PROMPT}
            
            {preferences_text}
            
            {history_text}
            
            {tools_text}
            
            Current user question: {message}
            
            Please provide a helpful response. If you need to use a tool, clearly indicate which tool you are using and what parameters you are providing.
            """
            
            print("\n--- SENDING TO CLAUDE ---")
            print(prompt[:200] + "..." if len(prompt) > 200 else prompt)
            
            # Generate response using Claude
            response = self.client.messages.create(
                model=self.model,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            ai_response = response.content[0].text
            
            print("\n--- CLAUDE RESPONSE ---")
            print(ai_response[:200] + "..." if len(ai_response) > 200 else ai_response)
            
            # Add the AI response to memory
            self.memory.add_ai_message(ai_response)
            
            return ai_response
        
        except Exception as e:
            error_traceback = traceback.format_exc()
            print(f"❌ Error generating response: {e}")
            print(error_traceback)
            
            error_response = "I apologize, but I encountered a technical issue. Let me try to help you with general information instead. What kind of athletic shoes are you looking for?"
            self.memory.add_ai_message(error_response)
            return error_response
    
    def reset(self) -> None:
        """Reset the agent's memory."""
        self.memory.clear()
        
    def get_preferences(self) -> Dict[str, Any]:
        """Get the current user preferences."""
        return self.memory.user_preferences
        
    def get_recommendations(self) -> List[Dict[str, Any]]:
        """Get all shoe recommendations made during the session."""
        return self.memory.get_recommendations()