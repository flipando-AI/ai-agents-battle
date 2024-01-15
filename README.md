![Flipando.ai Logo](https://assets-global.website-files.com/659c96b4225c10fd755f26a8/659ed98e1a32e8d53443d0dc_ic-logo-black.svg)

# 🛡️🏹 AI Agents Battle ⚔️🗡️

## Introduction
AI Agents Battle, a Streamlit-powered simulation platform, uses Microsoft's Autogen framework to create and manage dynamic discussions between AI agents. Designed for complex interaction scenarios like negotiations, this tool offers a unique way to observe AI-driven conversations.

## Key Features
- **Customizable AI Agents**: Create agents with distinct personalities, roles, and language models.
- **Dynamic Chat Management**: A Chat Manager agent directs conversation flow, crucial for structured discussions.
- **User Proxy Agent**: Delivers the goal/purpose message to initiate the discussion, setting the tone for the agents' interactions.
- **Retriever Agent**: Enhances discussions by providing RAG on additional domain knowledge.
- **Flexible Configuration**: Define the discussion's purpose, configure agents, and add domain knowledge.
- **Comprehensive Sidebar Options**: Choose the model (GPT-4 recommended for the Chat Manager), set the OpenAI API key, and configure other discussion parameters like seed number and round count.

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/flipando-AI/punta-tech
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

### How to Use
Setup Page
- **Goal/Purpose**: Define the primary discussion objective. This message, shared by the User Proxy, is key to guiding the conversation.
- **Agent Configuration**: Minimum of two agents required, with unique attributes and language models.
- **Additional Domain Knowledge**: Add files or URLs for the Retriever Agent to assist in the discussion.

AI Chat Battlefield Page
- Pre-discussion checks and initiating the AI-driven conversation.
- The Chat Manager and agents engage based on the user-defined setup.

Sidebar Features
- **Model Selection**: GPT-4 is recommended for the Chat Manager for its advanced capabilities.
- **API Key**: Essential for model requests.
- **Seed Number and Rounds**: Customize the discussion's dynamics.

Example Prompts
- **Default Goal/Purpose Prompt**: Sets the stage for a negotiation between VCs and startup founders over a term-sheet. (Include `default_battle_prompt` here)
- **Agent Definition Example**: An example of configuring a Shark Partner agent for the negotiation. (Include `system_message_shark_partner` here)

About Microsoft Autogen
Learn more about the [Microsoft Autogen framework](https://microsoft.github.io/autogen/).

Copyright and Logo
©Flipando.ai - All rights reserved.
![Flipando.ai Logo](https://assets-global.website-files.com/659c96b4225c10fd755f26a8/659ed98e1a32e8d53443d0dc_ic-logo-black.svg)
