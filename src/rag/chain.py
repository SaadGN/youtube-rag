from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
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

def create_rag_chain(retriever):
    """
    Create the complete LCEL RAG chain
    """

    llm = get_llm()

    parallel_chain = RunnableParallel(
        {
            "context": (
                retriever
                | RunnableLambda(format_docs)
            ),
            "question": RunnablePassthrough()
        }
    )

    rag_chain = (
        parallel_chain
        | RAG_PROMPT
        | llm
        | StrOutputParser()

    )

    return rag_chain