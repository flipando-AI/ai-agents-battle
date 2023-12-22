import streamlit as st

from src.battle.prompts import (system_message_analytics_assistant,
                         system_message_confident_founder,
                         system_message_shark_partner,
                         system_message_shy_founder)


def init_default_agents():
    return [
        ("Willy", system_message_shark_partner, "gpt-35-turbo-16k", False, "Right"),
        ("Monica", system_message_analytics_assistant, "gpt-35-turbo-16k", False, "Right"),
        ("Flipper", system_message_confident_founder, "gpt-35-turbo-16k", False, "Left"),
        ("Dwight", system_message_shy_founder, "gpt-35-turbo-16k", False, "Left")
    ]


def add_agent():
    """Function to add a new agent to the session state."""
    st.session_state.agents.append(("", "", "gpt-35-turbo-16k", False, "Right"))    


def remove_agent(agent_index):
    """Function to remove an agent from the session state by index."""
    del st.session_state.agents[agent_index]


def agents_setup():
    default_agents = init_default_agents()
    if 'agents' not in st.session_state:
        st.session_state.agents = default_agents

    agents_to_remove = []
    for i, agent in enumerate(st.session_state.agents[:]):
        st.markdown("<div class='agent-config'>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 3])
        with col1:
            agent_name = st.text_input("Agent Name", agent[0], key=f"name_{i}")
            agent_model = st.selectbox(
                "Model", ["gpt-35-turbo-16k", "gpt-3.5-turbo-1106", "gpt-4-1106-preview"], index=0, key=f"model_{i}", help="Select the AI model to use for this agent"
            )
            code_execution = st.checkbox("Enable Code Execution", key=f"code_{i}", help="Enable code execution for this agent")
            agent_chat_side = st.selectbox(
                "Chat-Side", ["Left", "Right"], 
                index=0 if agent[4] == "Left" else 1, 
                key=f"side_{i}", 
                help="Select the side of the chat where this agent will appear"
            )

        with col2:
            agent_prompt = st.text_area("Agent Prompt", agent[1], key=f"prompt_{i}", height=300)

        if st.button(f"Remove Agent",key=f"remove_{i}", type="primary", help="Remove this agent from the discussion", use_container_width=True):
            agents_to_remove.append(i)

        st.session_state.agents[i] = (agent_name, agent_prompt, agent_model, code_execution, agent_chat_side)
        st.markdown("-"* 50)
        st.markdown("</div>", unsafe_allow_html=True)

    if agents_to_remove:
        for index in sorted(agents_to_remove, reverse=True):
            remove_agent(index)
        st.rerun()

    st.button("Add New Agent", type="secondary", on_click=add_agent, help="Add a new agent to the discussion", use_container_width=True)
