import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "Google API key is not set"
    )

LLM_MODEL = "gemini-3.6-flash"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
