"""
Configuration settings for the Athletic Shoe Agent
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys - Support OpenAI, Gemini and Anthropic
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Agent Configuration
DEFAULT_MODEL = "claude-3-opus-20240229"  # Updated to use Claude as default
TEMPERATURE = 0.7
MAX_TOKENS = 500

# Streamlit Configuration
APP_TITLE = "Athletic Shoe Shopping Agent"
APP_DESCRIPTION = "An AI agent that helps you find the perfect athletic shoes based on your preferences and needs."