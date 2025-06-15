"""
Streamlit web application for Athletic Shoe Shopping Agent.
"""
import streamlit as st
import os
from dotenv import load_dotenv

from agents.shopping_agent import ShoppingAgent
from config import APP_TITLE, APP_DESCRIPTION

# Load environment variables
load_dotenv()

# Check for any supported API key
if not os.getenv("OPENAI_API_KEY") and not os.getenv("GOOGLE_API_KEY") and not os.getenv("ANTHROPIC_API_KEY"):
    st.warning("⚠️ No API key found. Please add either an OpenAI API key, Google API key, or Anthropic API key to your .env file.")
    st.stop()

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="👟",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session state for the agent
if "agent" not in st.session_state:
    st.session_state.agent = ShoppingAgent()

# App header
st.title(f"👟 {APP_TITLE}")
st.markdown(APP_DESCRIPTION)

# Sidebar with user preferences
st.sidebar.title("Shopping Preferences")

# Display current preferences from agent memory
preferences = st.session_state.agent.get_preferences()
if preferences:
    st.sidebar.subheader("Your Current Preferences")
    
    # Activity type
    if preferences["activity_type"]:
        st.sidebar.write(f"**Activity:** {preferences['activity_type']}")
    
    # Preferred brands
    if preferences["preferred_brands"]:
        st.sidebar.write(f"**Preferred Brands:** {', '.join(preferences['preferred_brands'])}")
    
    # Budget
    if preferences["budget"]:
        st.sidebar.write(f"**Budget:** ${preferences['budget']}")
    
    # Size
    if preferences["size"]:
        st.sidebar.write(f"**Size:** {preferences['size']}")
    
    # Color preference
    if preferences["color_preference"]:
        st.sidebar.write(f"**Color:** {preferences['color_preference']}")
    
    # Feature preferences
    if preferences["feature_preferences"]:
        st.sidebar.write(f"**Features:** {', '.join(preferences['feature_preferences'])}")

# Reset button
if st.sidebar.button("Reset Conversation"):
    st.session_state.messages = []
    st.session_state.agent.reset()
    st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("How can I help you find athletic shoes today?")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Display thinking spinner while getting response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.handle_message(user_input)
            st.write(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Help section at the bottom
with st.expander("How to use this shopping assistant"):
    st.markdown("""
    ### How to get the most out of your athletic shoe shopping assistant:
    
    1. **Tell the assistant about your needs**: Mention the type of activities you'll be doing, any specific preferences, and your budget.
    
    2. **Ask specific questions**: You can ask about specific brands, shoe types, or features you're looking for.
    
    3. **Refine your search**: If the recommendations don't match what you're looking for, tell the assistant what you'd like to change.
    
    4. **Get detailed information**: Ask for more details about specific shoes that interest you.
    
    5. **Reset the conversation**: Use the "Reset Conversation" button in the sidebar to start fresh.
    
    Example queries:
    - "I need running shoes for marathon training"
    - "I'm looking for basketball shoes under $150"
    - "What's the difference between the Nike ZoomX Invincible and the Adidas Ultraboost?"
    - "Show me training shoes with good ankle support"
    """)

# Footer
st.markdown("---")
st.markdown("This is a demo application for educational purposes only.")