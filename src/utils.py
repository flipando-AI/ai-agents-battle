from io import BytesIO

import streamlit as st
from langchain.document_loaders import UnstructuredFileIOLoader


def load_document(document_data: BytesIO):
    loader = UnstructuredFileIOLoader(document_data)
    docs = loader.load()
    return docs[0].page_content


def navigate_to(page):
    st.session_state.current_page = page
