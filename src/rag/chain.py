
from langchain_core.output_parsers import StrOutputParser
from .prompt import RAG_PROMPT
from src.llm.model import get_llm

def format_docs(documents):
    """
    convert Retrieved document into a single context string
    """
    return "\n\n".join(
        document.page_content
        for document in documents
    )

