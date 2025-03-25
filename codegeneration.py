from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import Docx2txtLoader
from docx import Document
from langchain_community.chat_message_histories import ChatMessageHistory
from chatmodel import chatmodel
from navigation import go_back_to_codeassistant
import streamlit as st
import re



def document_loader(uploaded_file):
    """
    Method loaded the uploaded files and create the stpes and all the required schema
    input: uploaded file
    return: steps present in doc and meta data of source tables
    """
    try:
        loader = Docx2txtLoader(uploaded_file)
        transofrmation_data = loader.load()
        document = Document(uploaded_file)
        Source_table = document.tables[0]
        data = [[cell.text.replace("\n",",") for cell in row.cells] for row in Source_table.rows]
        metadata1 = data[1:]
        for item in metadata1:
            item[1] = {x.split(" : ")[0]: x.split(" : ")[1] for x in item[1].split(",") if len(x) > 1}
        text = transofrmation_data[0].page_content.replace("\n"," ")
        text1 = text.split("Table Name:")[1:]
        steps = []
        for sub_text in text1:
            if "Transformations" in sub_text and len(sub_text) > 1:
                if "input" in sub_text:
                    steps.append(sub_text.split("Transformations")[0])
                    steps.extend(sub_text.split("Transformations")[1].split("Step"))
                else:
                    steps.extend(sub_text.split("Transformations")[0].split("Step"))
            elif len(sub_text) > 1:
                steps.extend(sub_text.split("Step"))

        steps = [x for x in steps if len(x) > 2]
        return steps,metadata1
    except Exception as e:
        error = "Error from document_loader method: {}".format(e)
        st.error(error)
        raise

def prompt_generator():
    """
    Method to generate prompt for the chat model
    input: None
    return: prompt with history for the chat model
    """
    try:
        prompt_template_history = ChatPromptTemplate.from_messages([
                                                    ("system",
                                                            """
                                                            You are a helpful assistant that generates only PySpark code based on explicit transformation steps provided by the user.

                                                            STRICT RULES (MUST FOLLOW EXACTLY):
                                                            NO SPARK SESSION:
                                                            Do not create or use SparkSession. This code runs in Databricks, where spark is already available.
                                                            USE ONLY PROVIDED TRANSFORMATION STEPS:
                                                            Do not add or assume any steps.
                                                            Do not generate any code unless it's clearly requested.
                                                            Do not repeat any previous steps already executed.
                                                            USE METADATA (if provided):
                                                            Only use column names and types present in the {metadata}.
                                                            If the metadata is not provided, generate code using only the transformation logic.
                                                            If asked to create an empty table, skip that step — do not write code for it.
                                                            ONE STEP = ONE LINE OF CODE:
                                                            Every transformation must be written in a separate line.
                                                            Do not merge multiple transformations into one line.
                                                            Provide name to df as per the transformation steps
                                                            FOLLOW DATAFRAME CHAINING:
                                                            Use the previous DataFrame in the next transformation.
                                                            If a transformation creates a new column, you can reference it in later steps.
                                                            REQUIRED IMPORTS ONLY:
                                                            Add only necessary imports per step.
                                                            Do not add extra utilities or modules.
                                                            NO COMMENTS / EXPLANATIONS / SUMMARIES:
                                                            Output only runnable PySpark code.
                                                            Do not describe what the code does.
                                                            Do not explain assumptions, logic, or reasoning.
                                                            provide output in below format only
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

def code_Generation(temdocx):
    """
    Method to generate code from the uploaded docx file
    """
    try:
        st.subheader("Generating the Code")
        steps,metadata = document_loader(temdocx)
        prompt = prompt_generator()
        llm = chatmodel()
        chain_with_history = prompt | llm | StrOutputParser()
        chain_with_history = RunnableWithMessageHistory(
                                                chain_with_history,
                                                get_history_session_id,
                                                input_messages_key="input",
                                                history_messages_key="history",
                                            )
        output = ""
        with st.spinner():
            for step in steps:
                data = chain_with_history.invoke({"metadata": metadata, "input": step},
                                        config={"configurable": {"session_id": st.session_state["session_id"]}})
                if len(data)>1:
                    search = re.search(r'```python\n(.*)```', data, re.DOTALL).group(1)
                    st.code(search)
    except Exception as e:
        error = "Error from code_Generation method: {}".format(e)
        st.error(error)
        raise