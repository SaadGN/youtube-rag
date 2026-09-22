import streamlit as st
from src.utils.youtube_utils import extract_video_id
from src.ingestion.youtube_loader import get_transcript
from src.processing.text_splitters import split_transcript
from src.vectorstore.faiss_store import (
    create_retriever,
    create_vector_store
)
from src.rag.chain import create_rag_chain

st.set_page_config(
    page_title="Youtube RAG Assistant",
    layout="wide",
)

st.title("Youtube RAG Assistant")

st.write(
    "***Chat with Any YouTube Video***"
)

st.write(
    "Ask questions, get accurate answers, and explore video content using AI."
)

video_id = st.text_input(
    "Enter Youtube video ID",
    placeholder="Gfr50f6ZBvo"
)

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if st.button("Process Video"):
    if not video_id:
        st.warning("Please enter YouTube video ID")
    else:
        try:
            with st.spinner("Processing YouTube video"):
                video_id = extract_video_id(video_id)
                transcript = get_transcript(video_id)
                documents = split_transcript(transcript)
                vector_store = create_vector_store(documents)
                retriever = create_retriever(vector_store)
                rag_chain = create_rag_chain(retriever)

                st.session_state.rag_chain = rag_chain
                st.session_state.video_id = video_id
                st.session_state.chunk_count = len(documents)

            st.success("Video processed successfully")
        except Exception as exc:
            st.error(f"Error while processing video : {str(exc)}")

st.divider()

st.subheader("Ask a question")

question = st.text_input(
    "Your Question",
    placeholder="What is this video about?"
)

if st.button("Ask Question"):
    if st.session_state.rag_chain is None:
        st.warning("Please process a youtube video first")

    elif not question:
        st.warning("Please enter a question first")

    else:
        try:
            with st.spinner("Generating answer..."):
                answer = st.session_state.rag_chain.invoke(question)

            st.subheader("Answer")
            st.write(answer)

        except Exception as exc:
            st.error(
                f"Error while genrating answer: {str(exc)}"
            )