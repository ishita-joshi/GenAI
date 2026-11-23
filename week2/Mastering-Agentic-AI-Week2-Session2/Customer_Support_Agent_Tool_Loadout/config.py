import os

from dotenv import load_dotenv

# Load .env here so these constants reflect it regardless of import order.
# (The notebook imports `config` before its own load_dotenv() cell runs, so
# without this the values below would always fall back to their defaults.)
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0"))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")


# Chroma persistence
PERSIST_DIR = os.getenv("PERSIST_DIR", ".chroma_tools")


RETURN_POLICY_DAYS = int(os.getenv("RETURN_POLICY_DAYS", "30"))