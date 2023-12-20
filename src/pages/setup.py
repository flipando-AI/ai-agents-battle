from io import BytesIO

import streamlit as st

from src.prompts import (system_message_analytics_assistant,
                         system_message_confident_founder,
                         system_message_shark_partner,
                         system_message_shy_founder)
from src.utils import load_document, navigate_to


def add_agent():
    """Function to add a new agent to the session state."""
    st.session_state.agents.append(("", "", "Right"))    


def remove_agent(agent_index):
    """Function to remove an agent from the session state by index."""
    del st.session_state.agents[agent_index]


def setup_page():
    st.markdown("# Discussion Setup")
    st.write("On this page, you'll define the objective of the discussion, provide any necessary documents, and configure the agents that will participate in the discussion. Customize the agents' names, roles, and initial prompts to tailor the simulation to your needs.")

    # Goal/Purpose Sub-Section
    st.subheader("Goal/Purpose of the Discussion")
    st.session_state.default_prompt = st.text_area(
        "State the goal that the agents must pursue during this discussion", 
        st.session_state.default_prompt, 
        height=100
    )

    # Additional Documents Sub-Section
    st.subheader("Additional Documents")
    doc_upload = st.file_uploader("Upload Document (i.e.: term sheet)", type=['txt', 'pdf', 'docx'])
    if doc_upload is not None:
        st.session_state.DOCUMENT = load_document(BytesIO(doc_upload.read()))
        additional_docs_expander = st.expander("Document Preview", expanded=True)
        with additional_docs_expander:
            st.text_area("Document Content", st.session_state.DOCUMENT, height=300, disabled=True, label_visibility="hidden")

    # Agents Sub-Section
    st.subheader("Agents")
    agents_expander = st.expander("Configure the agents to participate in your discussion", expanded=False)
    with agents_expander:
        default_agents = [
            ("Laurie", system_message_shark_partner, "Right"),
            ("Monica", system_message_analytics_assistant, "Right"),
            ("Flipper", system_message_confident_founder, "Left"),
            ("Dwight", system_message_shy_founder, "Left")
        ]

        if 'agents' not in st.session_state:
            st.session_state.agents = default_agents

        agents_to_remove = []
        for i, agent in enumerate(st.session_state.agents[:]):
            col1, col2 = st.columns([1, 4])
            with col1:
                agent_name = st.text_input("Agent Name", agent[0], key=f"name_{i}")
                agent_chat_side = st.selectbox(
                    "Chat-Side", ["Left", "Right"], 
                    index=0 if agent[2] == "Left" else 1, 
                    key=f"side_{i}", 
                    help="Select the side of the chat where this agent will appear"
                )
                if st.button(f"Remove Agent", key=f"remove_{i}", type="primary", help="Remove this agent from the discussion"):
                    agents_to_remove.append(i)

            with col2:
                agent_prompt = st.text_area("Agent Prompt", agent[1], key=f"prompt_{i}", height=300)
            st.session_state.agents[i] = (agent_name, agent_prompt, agent_chat_side)

        if agents_to_remove:
            for index in sorted(agents_to_remove, reverse=True):
                remove_agent(index)
            st.rerun()
        st.button("Add Agent", type="secondary", on_click=add_agent, help="Add a new agent to the discussion")
    st.button("Continue to Discussion Chat Page", on_click=navigate_to, args=("discussion",), type="secondary", help="Go ahead a kickoff your discussion")

