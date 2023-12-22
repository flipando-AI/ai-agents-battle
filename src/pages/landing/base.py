import streamlit as st

from src.utils.utils import navigate_to


def landing_page():
    st.markdown("# 🛡️🏹 AI Agents Battle ⚔️🗡️")
    st.write("Welcome to the Autonomous Agent Discussions app. Here you can simulate discussions between AI agents with specific goals, upload supporting documents, and configure agent roles for a goal-orientated discussion simulation.")
    st.divider()
    st.button(
        "Continue to Setup Page", 
        on_click=navigate_to, 
        args=("setup",), 
        type="secondary", 
        use_container_width=True,
        help="Start configuring your agent's discussion"
    )
