import streamlit as st
from utils import header,footer
from styles import page_config,homepage_tile_styles
from navigation import go_to_code_generation, go_to_code_chat, go_back_to_codeassistant,get_history
from codegeneration import code_Generation
from Chatbot import chatbot
from history import get_history_session


def codeassistant():
    """
    Method to render the code assistant application
    with header foother and the entire page reqirements
    """

    try:
        page_config()
        header()
        if "history" not in st.session_state:
            st.session_state.history = {} 
        with st.sidebar:
            col0,col1 = st.columns([0.8,2])
            with col1:
                st.button("chat", on_click=go_to_code_chat)
                st.button("Generate_code", on_click=go_to_code_generation)
                st.button("Get History", on_click=get_history)
                if "code_generation" in st.session_state:
                    st.session_state["session_id"]=st.text_input("Session ID",value="default_session")
                    st.subheader("Upload docx's to genrate code")
                    uploaded_files = st.file_uploader("Choose a file", type=['docx'], accept_multiple_files=False)
                    if uploaded_files is None:
                        st.stop()
                    else:
                        temdocx=f"./temp.docx"
                        with open(temdocx,"wb") as file:
                            file.write(uploaded_files.read())
                            file_name=uploaded_files.name
                        st.session_state["generate"] = st.button("Generate Code")
        if "code_chat" in st.session_state:
            chatbot()  
        if "get_history" in st.session_state:
            get_history_session()
        if 'generate' in st.session_state:
            code_Generation(temdocx)
            del st.session_state["generate"]
        footer()
    except Exception as e:
        error = "Error from codeassistant method: {}".format(e)
        st.error(error)

if __name__ == "__main__":
    codeassistant()

