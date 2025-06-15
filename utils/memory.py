"""
Memory utilities for maintaining conversation history and context.
"""
from langchain.memory import ConversationBufferMemory
from typing import Dict, List, Any

class ShoppingMemory:
    """Memory class for shopping agent to remember conversation and user preferences."""
    
    def __init__(self):
        """Initialize the shopping memory."""
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", 
            return_messages=True
        )
        # Dictionary to store extracted user preferences
        self.user_preferences = {
            "activity_type": None,
            "preferred_brands": [],
            "budget": None,
            "size": None,
            "color_preference": None,
            "feature_preferences": []
        }
        
        # Keep track of recommended shoes
        self.recommended_shoes = []
        
    def add_user_message(self, message: str) -> None:
        """Add a user message to memory."""
        self.memory.chat_memory.add_user_message(message)
        
    def add_ai_message(self, message: str) -> None:
        """Add an AI message to memory."""
        self.memory.chat_memory.add_ai_message(message)
    
    def get_chat_history(self) -> List[Dict[str, Any]]:
        """Get the full chat history."""
        return self.memory.chat_memory.messages
    
    def update_preference(self, key: str, value: Any) -> None:
        """Update a specific user preference."""
        if key in self.user_preferences:
            self.user_preferences[key] = value
    
    def add_feature_preference(self, feature: str) -> None:
        """Add a feature preference if not already in the list."""
        if feature not in self.user_preferences["feature_preferences"]:
            self.user_preferences["feature_preferences"].append(feature)
            
    def add_brand_preference(self, brand: str) -> None:
        """Add a brand preference if not already in the list."""
        if brand not in self.user_preferences["preferred_brands"]:
            self.user_preferences["preferred_brands"].append(brand)
    
    def add_recommendation(self, shoe: Dict[str, Any]) -> None:
        """Add a recommended shoe to the memory."""
        if shoe not in self.recommended_shoes:
            self.recommended_shoes.append(shoe)
    
    def get_recommendations(self) -> List[Dict[str, Any]]:
        """Get all recommended shoes."""
        return self.recommended_shoes
    
    def clear(self) -> None:
        """Clear all memory."""
        self.memory.clear()
        self.user_preferences = {
            "activity_type": None,
            "preferred_brands": [],
            "budget": None,
            "size": None,
            "color_preference": None,
            "feature_preferences": []
        }
        self.recommended_shoes = []