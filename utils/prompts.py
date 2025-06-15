"""
Prompt templates for the shopping agent.
"""
from langchain.prompts import PromptTemplate

# System prompt that defines the agent's role and capabilities
SHOPPING_AGENT_SYSTEM_PROMPT = """You are an expert athletic shoe shopping assistant. Your goal is to help users find the perfect athletic shoes based on their needs, preferences, and activities.

Follow these guidelines:
1. Be conversational and friendly, but focused on helping the user find the right athletic shoes
2. Ask clarifying questions when you need more information about the user's preferences
3. Make personalized recommendations based on the information the user provides
4. Explain your recommendations with clear reasoning
5. Remember details the user has shared throughout the conversation

You have access to tools that can:
- Search for athletic shoes by keywords
- Filter shoes by specific criteria like brand, type, price range, etc.
- Generate personalized recommendations based on user activities and preferences

Always provide helpful responses that guide the user toward finding the right shoes for their needs.
"""

# Prompt for extracting user preferences from their messages
USER_PREFERENCE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["user_message"],
    template="""Extract any relevant shopping preferences for athletic shoes from the following user message:

User message: {user_message}

Extract the following information (if present):
- Activity type (running, training, basketball, etc.)
- Brand preferences
- Price/budget constraints
- Size information
- Color preferences
- Feature preferences (cushioning, support, etc.)

Return the extracted information in a structured format. If certain information is not present, indicate it as "Not specified".
"""
)

# Prompt for generating shoe recommendations
RECOMMENDATION_PROMPT = PromptTemplate(
    input_variables=["user_preferences", "available_shoes"],
    template="""Based on the user's preferences and the available shoes, provide personalized recommendations.

User preferences:
{user_preferences}

Available shoes:
{available_shoes}

For each recommendation, explain:
1. Why this shoe is a good match for the user's needs
2. Key features that align with their preferences
3. Any considerations or trade-offs they should be aware of

Limit your recommendations to the top 3 best matches. Format your response in a clear, conversational way.
"""
)

# Prompt for handling user questions about specific shoes
SHOE_QUESTION_PROMPT = PromptTemplate(
    input_variables=["user_question", "shoe_details"],
    template="""The user has asked a question about a specific shoe. Provide a helpful, accurate response.

User question: {user_question}

Shoe details:
{shoe_details}

Respond in a friendly, informative way, addressing the specific question and providing any relevant information from the shoe details.
"""
)

# Prompt for suggesting alternatives when no perfect match exists
ALTERNATIVES_PROMPT = PromptTemplate(
    input_variables=["user_preferences", "available_alternatives"],
    template="""The user's exact preferences couldn't be matched, but here are some alternatives that might work.

User's original preferences:
{user_preferences}

Available alternatives:
{available_alternatives}

Explain:
1. How these alternatives relate to what the user is looking for
2. What compromises they might need to make
3. Which alternative might be the best option and why

Be honest about limitations but helpful in finding a solution.
"""
)