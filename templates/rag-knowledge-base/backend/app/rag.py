from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, SystemMessage

from app.embeddings import PERSIST_DIRECTORY, get_embeddings
from app.llm import get_chat_model


def get_vectorstore():
    return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=get_embeddings())


def ask(question: str, k: int = 3) -> dict:
    """Retrieve the k most relevant chunks and ask the chat model to answer
    grounded only in them, citing which source document(s) it used."""
    store = get_vectorstore()
    docs = store.similarity_search(question, k=k)

    if not docs:
        return {
            "answer": "No ingested documents found — run `python -m app.ingest` first.",
            "sources": [],
        }

    context = "\n\n".join(
        f"[Source: {d.metadata.get('source', 'unknown')}]\n{d.page_content}" for d in docs
    )
    system_prompt = (
        "Answer the question using ONLY the context below. Cite which source "
        "document(s) you used by name. If the context doesn't contain the "
        "answer, say so rather than guessing.\n\n" + context
    )

    model = get_chat_model()
    response = model.invoke([SystemMessage(content=system_prompt), HumanMessage(content=question)])

    return {
        "answer": response.content,
        "sources": sorted({d.metadata.get("source", "unknown") for d in docs}),
    }
