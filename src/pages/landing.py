import streamlit as st

from src.utils import navigate_to


def landing_page():
    st.markdown("# Autonomous Agent Discussions")
    st.write("Welcome to the Autonomous Agent Discussions app. Here you can simulate discussions between AI agents with specific goals, upload supporting documents, and configure agent roles for a goal-orientated discussion simulation.")
    st.button("Continue to Setup Page", on_click=navigate_to, args=("setup",), type="secondary", help="Start configuring your agent's discussion")
