# Athletic Shoe Shopping Agent

A demonstration of an agentic AI application that helps users find the perfect athletic shoes based on their needs, preferences, and activities.

## Overview

This application showcases a conversational AI agent that assists users in shopping for athletic shoes. The agent uses natural language understanding and specialized tools to provide personalized shoe recommendations.

## What Makes This App Agentic?

This application demonstrates key principles of agentic AI:

1. **Goal-directed behavior**: The agent has a specific goal—helping users find the right athletic shoes—and it takes autonomous actions to achieve this goal.

2. **Tool usage**: The agent leverages specialized tools for searching, filtering, and recommending products rather than just generating text responses.

3. **Memory and context awareness**: The agent maintains conversation history and builds a user preference model throughout the interaction.

4. **Adaptive decision-making**: Based on user inputs, the agent decides which tools to use and when, making contextual decisions rather than following a rigid script.

5. **Personalization**: The agent learns from user inputs and refines recommendations based on stated preferences and feedback.

## Project Structure

```
athletic_shoe_agent/
├── agents/
│   ├── __init__.py
│   └── shopping_agent.py    # Core agent implementation
├── tools/
│   ├── __init__.py
│   ├── search_tool.py       # Tool for searching shoes
│   ├── filter_tool.py       # Tool for filtering shoes
│   └── recommendation_tool.py # Tool for personalized recommendations
├── utils/
│   ├── __init__.py
│   ├── memory.py            # Memory management utilities
│   └── prompts.py           # Prompt templates
├── data/
│   └── shoes_database.py    # Mock database of athletic shoes
├── app.py                   # Streamlit web interface
├── config.py                # Configuration settings
├── requirements.txt         # Project dependencies
└── README.md                # This file
```

## Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd athletic_shoe_agent
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the Streamlit application:
```
streamlit run app.py
```

This will launch a web interface where you can interact with the shopping agent.

## Agent Components

### 1. Shopping Agent

The central controller that coordinates all components. It:
- Manages conversation flow
- Routes user queries to appropriate tools
- Maintains context and user preferences
- Generates natural language responses

### 2. Tools

The agent has access to specialized tools:

- **Search Tool**: Finds shoes that match keywords or descriptions
- **Filter Tool**: Narrows down results based on specific criteria
- **Recommendation Tool**: Suggests shoes based on user preferences and activities

### 3. Memory System

The agent uses a specialized memory system to:
- Store conversation history
- Track and update user preferences over time
- Remember previously recommended shoes

### 4. Mock Database

For demonstration purposes, the agent uses a mock database of athletic shoes with details like:
- Brand, type, and price
- Available sizes and colors
- Features and descriptions

## Learning Purpose

This project demonstrates:
- How to structure an agentic application
- Tool-based architecture for LLM applications
- Managing conversation context and user preferences
- Creating natural, helpful AI shopping assistants

## Future Enhancements

Potential improvements for a production version:
- Integration with real e-commerce inventory
- User accounts and preference saving
- Image recognition for shoe identification
- Price comparison across retailers
- More sophisticated recommendation algorithms

## License

This project is for educational purposes only.