import streamlit as st

from src.discussion import GroupDiscussion, fetch_model_config
from src.utils import navigate_to


def discussion_page():
    st.markdown("# Discussion Chat")
    st.write("This is the stage where your configured agents will engage in the negotiation based on the setup parameters you've provided. Initiate the discussion and observe how the agents interact with each other to achieve the set goals.")

    if st.button("Kick Off Negotiation", key="start_conversation", type="primary", help="Start the discussion"):
        if not st.session_state.selected_model:
            st.warning("Please select a preferred AI model.", icon="⚠️")
            st.stop()

        agent_data = [(name, prompt) for name, prompt, _ in st.session_state.agents]

        llm_config = fetch_model_config(st.session_state.selected_model)
        discussion = GroupDiscussion(agents=agent_data, llm_config=llm_config)
        manager = discussion.assemble_groupchat(num_rounds=8)

        message = f"{st.session_state.default_prompt}\n\n\n<Document context>\n\n{st.session_state.DOCUMENT}\n\nBegin!" if st.session_state.DOCUMENT else f"{st.session_state.default_prompt}\n\nBegin!"
        
        manager.initiate_chat(manager, message=message)      

        st.button("Back to Setup Page", on_click=navigate_to, args=("setup",), type="secondary", help="Return to the setup page")
