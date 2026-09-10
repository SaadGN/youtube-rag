from langchain_google_genai import ChatGoogleGenerativeAI

from src.config.settings import LLM_MODEL

def get_llm():
    """
    Create and return the gemini LLM
    """

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        temperature=0
    )

    return llm
