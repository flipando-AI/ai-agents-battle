import streamlit as st

from src.discussion import GroupDiscussion, fetch_model_config
from src.prompts import (system_message_analytics_assistant,
                         system_message_confident_founder,
                         system_message_shark_partner,
                         system_message_shy_founder)
from src.styles import styles
from src.term_sheet import TERM_SHEET



if __name__ == "__main__":
    st.set_page_config(layout="wide")


    with open("src/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


    st.markdown(styles, unsafe_allow_html=True)
    st.title("Term-Sheet Negotiation Simulation")


    with st.sidebar:
        st.header("Agent Configuration")
        selected_model = st.selectbox("Select Model", ["gpt-3.5-turbo-1106", "gpt-4-1106-preview"], index=1)
        st.header("Agent Roles")

        with st.expander("Laurie - Shark Partner"):
            st.write(system_message_shark_partner)
        with st.expander("Monica - Analytics Assistant"):
            st.write(system_message_analytics_assistant)
        with st.expander("Flipper - Confident CoFounder"):
            st.write(system_message_confident_founder)
        with st.expander("Dwight - Shy CoFounder"):
            st.write(system_message_shy_founder)

    with st.container():
        if st.button("Kick Off Negotiation", key="start_conversation"):
            if not selected_model:
                st.warning(
                    "You must choose a preferred model", icon="⚠️")
                st.stop()

            llm_config = fetch_model_config(selected_model)
            discussion = GroupDiscussion(llm_config=llm_config)
            manager = discussion.assemble_groupchat(num_rounds=2)
            manager.initiate_chat(
                manager, 
                message=f"""
                    Welcome to the Term Sheet Negotiation!

                    The term-sheet upon which the negotiation will be based is as follows:

                    ```
                    {TERM_SHEET}
                    ```

                    Begin!
                """
            )
