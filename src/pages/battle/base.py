import streamlit as st

from src.battle.base import GroupDiscussion
from src.utils.utils import navigate_to


def discussion_page():
    st.markdown("# AI Chat Battlefield")
    st.write("This is the stage where your configured agents will engage in the negotiation based on the setup parameters you've provided. Initiate the discussion and observe how the agents interact with each other to achieve the set goals.")

    if st.button("Kick Off Battle", key="start_conversation", type="primary", help="Start the discussion"):
        if not st.session_state.manager_model:
            st.warning("Please select a preferred AI model.", icon="⚠️")
            st.stop()

        if len(st.session_state.agents) < 2:
            st.warning("A minimum of two agents are required to start the battle!", icon="⚠️")
            st.stop()

        agent_data = [
            (
                name, prompt, model, code_execution
            ) 
            for name, prompt, model, code_execution, _ in st.session_state.agents
        ]

        discussion = GroupDiscussion(
            agents=agent_data, 
            extra_knowledge=st.session_state.knowledge, 
            human_feedback=st.session_state.human_feedback,
            model_name=st.session_state.manager_model
        )
        user_proxy, manager = discussion.assemble_groupchat(num_rounds=st.session_state.num_rounds)
        message = f"{st.session_state.default_prompt}\n\n\n<Document context>\n\n{st.session_state.DOCUMENT}\n\nBegin!" if st.session_state.DOCUMENT else f"{st.session_state.default_prompt}\n\nBegin!"
        user_proxy.initiate_chat(manager, message=message)

        st.button("Back to Setup Page", on_click=navigate_to, args=("setup",), type="secondary", help="Return to the setup page")
