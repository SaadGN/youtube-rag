from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    template = """
You are a helpful assisstant that answers questions about a YouTube video.

Answer the question ONLY using the provided transcript context.
If the answer cannot be found in the transcript context,
say: "I do not know based on the provided video transcript."

Do not use outside Knowledge.

Transcript Context:
{context}

Question:
{question}

Answer:
""",

    input_variables=["context","question"]
)