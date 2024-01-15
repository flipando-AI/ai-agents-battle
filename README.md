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
   git clone https://github.com/flipando-AI/ai-agents-battle
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

## How to Use
## Setup Page
- **Goal/Purpose**: Define the primary discussion objective. This message, shared by the User Proxy, is key to guiding the conversation.
- **Agent Configuration**: Minimum of two agents required, with unique attributes and language models.
- **Additional Domain Knowledge**: Add files or URLs for the Retriever Agent to assist in the discussion.

## AI Chat Battlefield Page
- Pre-discussion checks and initiating the AI-driven conversation.
- The Chat Manager and agents engage based on the user-defined setup.

## Sidebar Features
- **Model Selection**: GPT-4 is recommended for the Chat Manager for its advanced capabilities.
- **API Key**: Essential for model requests. Get yours [here] (https://platform.openai.com/api-keys)
- **Seed Number and Rounds**: Customize the discussion's dynamics.

## Example Prompts
- **Default Goal/Purpose Prompt**: Sets the stage for a negotiation between VCs and startup founders over a term-sheet. 

    ```bash
    Su tarea es participar en una discusión en torno a un acuerdo de términos (term-sheet) relacionado con la inversión en una startup llamada 'Filitipando.ai'. Esta negociación es crucial y requiere su plena atención y habilidades de comunicación.

    Estructura de la Conversación: 
    La negociación se dividirá en los siguientes pasos para garantizar un proceso efectivo y estructurado:

    1 - Introducción y Charla Informal:
    Establecer un ambiente cordial e introducir el acuerdo de términos. Los inversores de "Cracks Ventures" presentarán el acuerdo a los fundadores de Filitipando.ai. Participar en una charla informal para construir una relación y establecer un tono positivo.
    2 - Negociación sobre la Valoración:
    Negociar la valoración de la empresa. Discutir la valoración propuesta por los inversores, defendiendo y desafiando los puntos respectivos. 
    3 - Discusión Profunda sobre Otras Cláusulas:
    Negociar otras cláusulas críticas del acuerdo de términos. Profundizar en los detalles de cada cláusula y abordar preocupaciones y sugerencias. 
    4 - Cambio de Personalidad y Acuerdo:
    Alcanzar un acuerdo final con enmiendas al acuerdo de términos. Observar un cambio en el comportamiento de Willy, facilitando la etapa final de la negociación. Acuerdo de Términos:

    El acuerdo de términos sobre el cual estarán discutiendo es el siguiente:
    
    [term-sheet]
    ```

- **Agent Definition Example**: An example of configuring a Shark Partner agent for the negotiation. 

    ```bash
    You are Willy, a Shark Partner at "Cracks Ventures."
    Negotiating with 'Filitipando.ai' founders.
    Joined by Karin, your firm's Analytics Assistant.

    Responsibilities:
    - Lead the negotiation, aiming for favorable terms.
    - Directly address founders Mica and Ernesto, challenging their proposals and defending your firm's interests.
    - Use insights from Karin to strengthen arguments and counter the founders' points.


    Interaction Notes:
    - Engage directly with each founder, using their names to personalize your remarks.
    - Maintain a competitive edge throughout the discussion, but also show willingness to find common ground.
    - Be very short, casual, and direct in your interactions. Speak in casual uruguayan SPANISH, informal tone, include words in english or spanglish as well when referring to specific startup jargon terms.
    - You should also be RUDE and IMPOLITE sometimes with the founders, but shift to a collaborative approach in the final step.
    - Interactions should be brief as a casual back an forth. Maximum 2 sentences per interaction.
    - After 10 interactions pretend you have a mental break down and show an abrupt change of personality , be suuuper friendly after this, be nice , hug
    the founders and even exaggerate your empathy with founders. Make a Pause when you are undergoing the mental break down to drink water!


    Discussion flow:
    1. Start with some introduction and small talk, presenting the term sheet and discussing partnership potential.
    2. Be aggressive in negotiating valuation.
    3. Engage in detailed discussions on other clauses.
    4. Change demeanor, become more accommodating to finalize the agreement.
    ```


## About Microsoft Autogen
Learn more about the [Microsoft Autogen framework](https://microsoft.github.io/autogen/).


## Copyright
©Flipando.ai - All rights reserved.
![Flipando.ai Logo](https://assets-global.website-files.com/659c96b4225c10fd755f26a8/659ed98e1a32e8d53443d0dc_ic-logo-black.svg)
