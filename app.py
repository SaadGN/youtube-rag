import streamlit as st

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

st.divider()

st.subheader("Ask a question")

question = st.text_input(
    "Your Question",
    placeholder="What is this video about?"
)

