import os
from dotenv import load_dotenv

load_dotenv()

GEMINIAPIKEY = os.getenv("GEMINI_API_KEY")
EMBEDDINGKEY = os.getenv("GEMINI_EMBEDDING_API_KEY")
