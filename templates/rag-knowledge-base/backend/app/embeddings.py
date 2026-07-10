import os

from langchain_openai import OpenAIEmbeddings

PERSIST_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "data", "chroma_db")


def get_embeddings():
    """Embeddings always use OpenAI regardless of LLM_PROVIDER for chat —
    Anthropic has no embeddings API. OPENAI_API_KEY is required for ingestion
    and retrieval even on an Anthropic-only project."""
    return OpenAIEmbeddings(model=os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))
