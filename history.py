import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory

def get_history_session():
    st.subheader("History")
    if len(st.session_state.history)==0:
        st.code("No history available")
    else:
        session_id = st.selectbox("Session ID", list(st.session_state.history.keys()), index=0)
        st.code(st.session_state.history[session_id])