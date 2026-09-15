from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config.settings import CHUNK_SIZE,CHUNK_OVERLAP

def split_transcript(transcript:str):
    """
    Split transcript into overlapping documents
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    documents = splitter.create_documents([transcript])

    return documents