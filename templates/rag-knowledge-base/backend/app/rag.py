from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, SystemMessage

from app.embeddings import PERSIST_DIRECTORY, get_embeddings
from app.llm import get_chat_model

INSUFFICIENT_EVIDENCE_TOKEN = "INSUFFICIENT_EVIDENCE"
REFUSAL_MESSAGE = "The available documents don't contain enough information to answer this question."


def get_vectorstore():
    return Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=get_embeddings())


def _extract_text(content) -> str:
    """LangChain's AIMessage.content is typed as str | list[str | dict] --
    some providers/inputs (e.g. Anthropic on certain degenerate prompts)
    return a list of content blocks instead of a plain string. Normalize
    both shapes to plain text rather than assuming .content is always str.
    Hardening delta harvested from policy-lookup-assistant (2026-08-08)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, str):
                parts.append(block)
            elif isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
        return "".join(parts)
    return str(content)


def ask(question: str, k: int = 3) -> dict:
    """Retrieve the k most relevant chunks and ask the chat model to answer
    grounded only in them, citing which source document(s) it used.

    Refusal is a structured signal, not prose-only: the model is instructed
    to open its response with a fixed sentinel token (INSUFFICIENT_EVIDENCE)
    on its own first line if and only if the retrieved context does not
    contain enough information to answer the question. `sources[]` is always
    built by the application directly from retrieval metadata — never parsed
    from the model's own prose — so citation badges stay accurate to what was
    actually retrieved even on a refusal.
    """
    store = get_vectorstore()
    docs = store.similarity_search(question, k=k)

    if not docs:
        return {
            "answer": "No ingested documents found — run `python -m app.ingest` first.",
            "sufficient_evidence": False,
            "sources": [],
        }

    context = "\n\n".join(
        f"[Source: {d.metadata.get('source', 'unknown')} | "
        f"Type: {d.metadata.get('label', 'unknown')} | "
        f"As of: {d.metadata.get('as_of', 'unknown')}]\n{d.page_content}"
        for d in docs
    )
    system_prompt = (
        "Answer the question using ONLY the context below. Cite which source "
        "document(s) you used by name.\n\n"
        "Follow these rules exactly:\n"
        "1. Numeric precision: when the context contains numeric figures "
        "(percentages, dollar amounts, time windows, counts), quote them "
        "exactly as they appear in the source text. Do not paraphrase, "
        "round, average, or otherwise alter numeric values.\n"
        "2. No extrapolation: if the question asks about something adjacent "
        "to but not directly stated in the context (e.g., a program, "
        "document type, or jurisdiction not mentioned in the context), treat "
        "that as insufficient evidence rather than answering by analogy or "
        "inference from a similar case.\n"
        f"3. If, and only if, the context does not contain enough "
        f"information to answer the question, respond with the exact token "
        f"{INSUFFICIENT_EVIDENCE_TOKEN} as the first line of your response, "
        f"with no other characters on that line, and nothing else in your "
        f"response. If the context is sufficient, do not emit this token "
        f"anywhere in your response.\n\n"
        "Context:\n" + context
    )

    model = get_chat_model()
    response = model.invoke([SystemMessage(content=system_prompt), HumanMessage(content=question)])

    content = _extract_text(response.content).strip()
    sufficient_evidence = not content.startswith(INSUFFICIENT_EVIDENCE_TOKEN)
    answer = content if sufficient_evidence else REFUSAL_MESSAGE

    seen = set()
    sources = []
    for d in docs:
        document = d.metadata.get("source", "unknown")
        if document in seen:
            continue
        seen.add(document)
        sources.append({
            "document": document,
            "label": d.metadata.get("label", "unknown"),
            "authority": d.metadata.get("authority", "unknown"),
            "as_of": d.metadata.get("as_of", "unknown"),
        })
    sources.sort(key=lambda s: s["document"])

    return {
        "answer": answer,
        "sufficient_evidence": sufficient_evidence,
        "sources": sources,
    }
