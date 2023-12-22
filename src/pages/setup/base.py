import streamlit as st

from src.pages.setup.agents import agents_setup
from src.pages.setup.knowledge import knowledge_setup
from src.pages.setup.purpose import purpose_setup
from src.utils.utils import navigate_to


def setup_page():
    st.markdown("# Battle Setup")
    st.write("On this page, you'll define the objective of the discussion, provide any necessary documents, and configure the agents that will participate in the discussion. Customize the agents' names, roles, and initial prompts to tailor the simulation to your needs.")
    st.divider()

    # Goal/Purpose Sub-Section
    purpose_setup()
    st.divider()
    
    # Agents Sub-Section
    st.subheader("Agents")
    agents_expander = st.expander("Configure the agents to participate in your discussion", expanded=False)
    with agents_expander:
        agents_setup()

    # Knowledge Sub-Section
    knowledge_setup()
    st.divider()
    
    # Continue Button
    st.button(
        "Continue to Chat Battlefield Page", 
        on_click=navigate_to, 
        args=("discussion",), 
        type="secondary", 
        use_container_width=True,
        help="Go ahead a kickoff your battle!"
    )
