import os
from langchain_openai import OpenAIEmbeddings
from config import EMBEDDING_MODEL


def build_embeddings():
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set — add it to your .env file.")
    print(f"  Using OpenAIEmbeddings (model={EMBEDDING_MODEL})")
    return OpenAIEmbeddings(model=EMBEDDING_MODEL)
