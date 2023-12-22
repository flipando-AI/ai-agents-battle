from io import BytesIO

import streamlit as st

from src.utils.utils import load_document


def purpose_setup():
    st.subheader("Goal/Purpose of the Discussion", help="This message will be displayed to the agents at the beginning of the discussion, think of it as the 'prompt' to kick off the battle.")
    st.session_state.default_prompt = st.text_area(
        "State the goal/purpose of the discussion", 
        st.session_state.default_prompt, 
        height=100
    )
    
    st.divider()
    # Additional Documents Sub-Section
    st.subheader("Additional Documents to discuss upon", help="Any document uploaded here will be incorporated right after the goal/purpose of the discussion that is displayed to the agents.")
    doc_upload = st.file_uploader("Upload Document (i.e.: term sheet)", type=['txt', 'pdf', 'doc','docx'], accept_multiple_files=False)
    if doc_upload is not None:
        st.session_state.DOCUMENT = load_document(BytesIO(doc_upload.read()))
        additional_docs_expander = st.expander("Document Preview", expanded=True)
        with additional_docs_expander:
            st.text_area("Document Content", st.session_state.DOCUMENT, height=300, disabled=True, label_visibility="hidden")
