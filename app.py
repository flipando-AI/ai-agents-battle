import streamlit as st

from src.pages import discussion_page, landing_page, setup_page
from src.styles.styles import styles
from src.utils.utils import navigate_to


def page_switcher():
    page = st.session_state.current_page
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if page != "landing":
            st.button("Home", on_click=navigate_to, args=("landing",), type="secondary", help="Return to the home page")
    with col2:
        if page != "setup":
            st.button("Setup Page", on_click=navigate_to, args=("setup",), type="secondary", help="Go to the discussion setup page")
    with col3:
        if page != "discussion":
            st.button("Chat Battlefield Page", on_click=navigate_to, args=("discussion",), type="secondary", help="Go to the discussion chat page")

    st.divider()

# Main Application
if __name__ == "__main__":
    st.set_page_config(layout="wide")

    with open("src/styles/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown(styles, unsafe_allow_html=True)

    if 'current_page' not in st.session_state:
        st.session_state.current_page = "landing"

    page_switcher()

    with st.sidebar:
        st.session_state.manager_model = st.selectbox(
            "Select Model", ["gpt-35-turbo-16k", "gpt-3.5-turbo-1106", "gpt-4-1106-preview"], index=0, help="Select the AI model to use for the Chat Manager"
        )
        st.session_state.num_rounds = st.number_input("Number of Rounds", min_value=1, max_value=100, value=10, step=1, help="Number of rounds for the discussion")
        st.session_state.human_feedback = st.toggle("Human Intervention", value=False, help="Whether to ask for human feedback during the conversation to steer the discussion in the right direction", disabled=True)

    if 'current_page' not in st.session_state:
        st.session_state.current_page = "setup"
    if 'default_prompt' not in st.session_state:
        st.session_state.default_prompt = "Bienvenidos a la negociación del term-sheet! El term-sheet sobre el cual se basará la negociación es el siguiente: "
    if 'DOCUMENT' not in st.session_state:
        st.session_state.DOCUMENT = None

    if st.session_state.current_page == "landing":
        landing_page()
    elif st.session_state.current_page == "setup":
        setup_page()
    elif st.session_state.current_page == "discussion":
        discussion_page()
