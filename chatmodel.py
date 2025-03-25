import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

def chatmodel(modelname = "llama-3.1-8b-instant"):
    """
    Returns an LLM model to perform the chat or the code generation
    """
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    llm = ChatGroq(model = modelname )
    return llm
