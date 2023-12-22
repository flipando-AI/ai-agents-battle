import os

import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


def save_file_to_disk(file: UploadedFile):
    """Function to save a file to disk."""
    save_path = "temp_files"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    with open(os.path.join(save_path, file.name), "wb") as f:
        f.write(file.getbuffer())    

    return os.path.join(save_path, file.name)


def knowledge_setup():
    knowledge_expander = st.expander("Configure extra domain knowledge of your agents", expanded=False)
    with knowledge_expander:
        additional_files = st.file_uploader("Upload any additional documents to expand the domain knowledge of your agents", type=['txt', 'docx', 'pdf'], help="Your agents will be able to access the data in these documents whenever they need to during the discussion.", accept_multiple_files=True)
        additional_document_resources = st.text_area(
            "Provide a link to any additional documents to expand the domain knowledge of your agents", 
            help="Provide a link to a document to expand the domain knowledge of your agents. Note: If multiple links are provided, separate them with a new line."
        )


    additional_file_paths = [save_file_to_disk(file) for file in additional_files]
    st.session_state.knowledge = additional_file_paths + additional_document_resources.split("\n") if additional_document_resources else additional_file_paths
