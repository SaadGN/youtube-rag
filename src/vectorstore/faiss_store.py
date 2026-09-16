from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from src.config.settings import EMBEDDING_MODEL,RETRIEVER_K

def create_vector_store(documents):
    """"
    Create a FAISS vector store from documents 
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model = EMBEDDING_MODEL
    )

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    return vector_store

def create_retriever(vector_store):
    """
    Convert FAISS vector store into a retriever
    """

    retriever = vector_store.as_retriever(
        search_type = "similarity",
        search_kwargs = {
            "k":RETRIEVER_K
        }
    )

    return retriever