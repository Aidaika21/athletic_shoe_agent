#!/usr/bin/env python3
"""
Simple utility script to clear the conversation history for the athletic_shoe_agent.
"""
from utils.memory import ShoppingMemory

if __name__ == "__main__":
    # Initialize memory
    memory = ShoppingMemory()
    
    # Clear the memory
    memory.clear()
    
    print("✅ Conversation history has been cleared successfully.")
    print("You can now restart the application with a fresh conversation.")
    print("To restart: streamlit run app.py")