"""Ingests backend/data/sample_docs/ into the local Chroma store.

Run with: python -m app.ingest
Re-run any time the document set changes — this rebuilds the store from
scratch rather than incrementally updating it, which is fine at this scale.
"""

import json
import os

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.embeddings import PERSIST_DIRECTORY, get_embeddings

DOCS_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "data", "sample_docs")


def load_documents():
    from langchain_core.documents import Document

    # A manifest entry is required per document, not optional metadata --
    # ingesting silently with only {"source": filename} means a citation can
    # never carry authority/recency information, and a caller has no way to
    # tell a binding policy from an informal FAQ. Hardening delta harvested
    # from policy-lookup-assistant (2026-08-08): missing-manifest ingestion
    # was found to silently degrade every downstream citation.
    manifest_path = os.path.join(DOCS_DIRECTORY, "manifest.json")
    with open(manifest_path) as f:
        manifest = json.load(f)

    documents = []
    for filename in sorted(os.listdir(DOCS_DIRECTORY)):
        if not filename.endswith(".txt"):
            continue
        if filename not in manifest:
            raise ValueError(
                f"No manifest entry for {filename!r} — add one to manifest.json before ingesting."
            )
        entry = manifest[filename]
        path = os.path.join(DOCS_DIRECTORY, filename)
        with open(path, "r") as f:
            documents.append(Document(
                page_content=f.read(),
                metadata={"source": filename, **entry},
            ))
    return documents


def main():
    documents = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=PERSIST_DIRECTORY,
    )
    print(f"Ingested {len(documents)} document(s) -> {len(chunks)} chunk(s) into {PERSIST_DIRECTORY}")


if __name__ == "__main__":
    main()
