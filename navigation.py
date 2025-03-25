import streamlit as st

def go_back_to_codeassistant():
    """
    Method to which enables navigation to codeAssistant home Page
    input: None
    ouput: Sets a session state variable to navigate from other pages to home page
    return: None
    """
    try:
        if "code_generation" in st.session_state:
            del st.session_state["code_generation"]
        if "code_chat" in st.session_state:
            del st.session_state["code_chat"]
        if "history" in st.session_state:
            del st.session_state["history"] 
    except Exception as e:
        error = "Error from go_back_to_codeassistant method: {}".format(e)
        st.error(error)
        raise  

def go_to_code_generation():
    """
    Method to which enables navigation to code generation page
    input: None
    ouput: Sets a session state variable to navigate from home page to Code generation Page
    return: sets code generation in session state
    """
    try:
        if "code_chat" in st.session_state:
            del st.session_state["code_chat"]
        if "get_history" in st.session_state:
            del st.session_state["get_history"]
        if "code_generation" not in st.session_state:
            st.session_state["code_generation"] = True
    except Exception as e:
        error = "Error from go_to_code_generation method: {}".format(e)
        st.error(error)
        raise

def go_to_code_chat():
    """
    Method to which enables navigation to code chat page
    input: None
    ouput: Sets a session state variable to navigate from home page to Code chat Page
    return: sets code chat in session state
    """
    try:
        if "code_generation" in st.session_state:
            del st.session_state["code_generation"]
        if "get_history" in st.session_state:
            del st.session_state["get_history"]
        if "code_chat" not in st.session_state:
            st.session_state["code_chat"] = True
    except Exception as e:
        error = "Error from go_to_code_chat method: {}".format(e)
        st.error(error)
        raise

def get_history():
    """
    Method to which enables navigation to code chat page
    input: None
    ouput: Sets a session state variable to navigate from home page to Code chat Page
    return: sets code chat in session state
    """
    try:
        if "code_generation" in st.session_state:
            del st.session_state["code_generation"]
        if "code_chat" in st.session_state:
            del st.session_state["code_chat"]
        if "get_history" not in st.session_state:
            st.session_state["get_history"] = True
    except Exception as e:
        error = "Error from get_history method: {}".format(e)
        st.error(error)
        raise

def set_new_chat():
    """
    Method to which enables navigation to code generation page
    input: None
    ouput: Sets a session state variable to navigate from home page to Code generation Page
    return: sets code generation in session state
    """
    try:
        if "chat_with_history" not in st.session_state:
            del st.session_state["chat_with_history"]
        if "new_chat" not in st.session_state:
            st.session_state["new_chat"] = True
    except Exception as e:
        error = "Error from set_new_chat method: {}".format(e)
        st.error(error)
        raise

def set_chat_with_history():
    """
    Method to which enables navigation to code generation page
    input: None
    ouput: Sets a session state variable to navigate from home page to Code generation Page
    return: sets code generation in session state
    """
    try:
        if "new_chat" not in st.session_state:
            del st.session_state["new_chat"]
        if "chat_with_history" not in st.session_state:
            st.session_state["chat_with_history"] = True
    except Exception as e:
        error = "Error from set_new_chat method: {}".format(e)
        st.error(error)
        raise