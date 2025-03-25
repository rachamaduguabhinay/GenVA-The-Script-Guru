from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import Docx2txtLoader
from docx import Document
from langchain_community.chat_message_histories import ChatMessageHistory
from chatmodel import chatmodel
from navigation import go_back_to_codeassistant,set_chat_with_history,set_new_chat
import streamlit as st

def prompt_with_history():
    """
    Method to generate prompt for the chat model
    input: None
    return: prompt with history for the chat model
    """
    try:
        prompt_template_history = ChatPromptTemplate.from_messages([
                                                    ("system",
                                                            """
                                                            You are a helpful assistant that generate {language} code 
                                                            with the transofmration steps provided by the user or
                                                            ask to change any step in the history.If question is general salutation respond it same way as 
                                                            Hell0!!I am help ful code assistance, how can I help you?
                                                            if the query is not related to code or salutation or any coding language you can answer like
                                                            "Requested Query is not related to any coding tech. I cant assist"
                                                            Dont provide code explanations and dont provide addition stesp 
                                                            only provide the transformation asked. dont add any other steps on your own.
                                                            generate the code as per the transformation based on the input given for that step
                                                            for each step use the previous history and use the data frames 
                                                            created in previous step to generate the code.
                                                            only give the code which can be used directly in the pyspark code.
                                                            dont truncate the code even the code is big in the output
                                                            and dont repeat the steps and add any additional steps. and check history if that step is already done dont repeat it.
                                                            include imports required for each step also. dont create spark session and spak apps
                                                            provide the code in below format apart this dont add any other text. 
                                                            and also use the previous history to generate the code.check the dependency of current dataframe with previous dataframe if it is required to cretate from previous table try to use th eprevious df give each table with different name dont just give df.
                                                            ```
                                                            Python

                                                            Code
                                                            ```
                                                            
                                                            """),
                                                        MessagesPlaceholder("history"),
                                                        ("human", "{input}"),
                                                    ]
                                                )
        return prompt_template_history
    except Exception as e:
        error = "Error from prompt_generator method: {}".format(e)
        st.error(error)
        raise

def get_history_session_id(session_id):
    if session_id not in st.session_state.history:
        st.session_state.history[session_id]=ChatMessageHistory()
    return st.session_state.history[session_id]

def chatbot():
    """
    Method to render the chatbot
    """
    try:
        llm = chatmodel()
        # if "history" not in st.session_state:
        #     st.session_state.history = {}
        if "code_chat" in st.session_state:
            st.subheader("Chat with the code assistant")
            language = st.text_input("code langague", value="Pyspark")
            if len(st.session_state.history) == 0:
                st.session_state.history["default_session"]=ChatMessageHistory()
            st.session_state["session_id"]=st.selectbox("Session ID",st.session_state.history.keys(),index =0)
            st.write("Enter your query in the text box below and click on the send button to get the response")
            query= st.text_input("User Input", value = "Hi!!")
            prompt = prompt_with_history()
            chain_with_history = prompt | llm | StrOutputParser()
            chain_with_history = RunnableWithMessageHistory(
                                                chain_with_history,
                                                get_history_session_id,
                                                input_messages_key="input",
                                                history_messages_key="history",
                                            )
            output = ""
            with st.spinner():
                data = chain_with_history.invoke({"language": language, "input": query},
                                            config={"configurable": {"session_id": st.session_state["session_id"]}})
                    
                output += "\n" + data 
            st.code(output)
    except Exception as e:
        error = "Error from chatbot method: {}".format(e)
        st.error(error)
        raise
