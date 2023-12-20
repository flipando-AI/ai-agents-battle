import streamlit as st

from src.pages import discussion_page, landing_page, setup_page
from src.styles import styles
from src.utils import navigate_to


def page_switcher():
    st.markdown("---")
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
            st.button("Discussion Page", on_click=navigate_to, args=("discussion",), type="secondary", help="Go to the discussion chat page")
    st.markdown("---")


# Main Application
if __name__ == "__main__":
    st.set_page_config(layout="wide")

    with open("src/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown(styles, unsafe_allow_html=True)

    if 'current_page' not in st.session_state:
        st.session_state.current_page = "landing"

    page_switcher()

    with st.sidebar:
        st.session_state.selected_model = st.selectbox(
            "Select Model", ["gpt-3.5-turbo-1106", "gpt-4-1106-preview"], index=0
        )

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
