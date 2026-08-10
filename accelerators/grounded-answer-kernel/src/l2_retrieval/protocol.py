"""The evidence-source protocol (L2). Imports no store, no domain module.

GENERALISED from ``rate-case-analyzer``'s ``app/retrieval/protocol.py``. The
source module imported ``app.enums.case.JurisdictionCode``, ``app.enums.
corpus.Corpus``, ``app.model.records`` (``Case``, ``Chunk``, ``Claim``,
``Document``, ``Jurisdiction``), and ``app.retrieval.filters.ChunkPredicate``
-- all RCA-domain types. None of those travel with this file; every method
below is typed against generic structural placeholders (``object``, plain
``str``, or a caller-supplied predicate callable) instead.

This is what lets an adopter's answer-composition code be written against a
CAPABILITY rather than a concrete corpus -- which is what makes two
differently-walled answer paths (e.g. RCA's public/work-product split)
structurally unable to reach each other's store: neither path imports a
concrete store, both import only this Protocol.

L2 IS DELIBERATELY THE SEAM WHERE PLA AND RCA DIVERGE. This accelerator does
NOT attempt to unify LangChain/Chroma-style retrieval (``policy-lookup-
assistant``) with a hand-rolled protocol over independent stores (``rate-
case-analyzer``) into one implementation -- they are architecturally
incompatible, and forcing them together would produce an interface
satisfying neither. This Protocol is the shared SHAPE; the Chroma-backed
adapter and the hash-embed-backed store below are two of potentially many
implementations an adopter chooses between, not a merge of the two source
projects.
"""

from __future__ import annotations

from typing import Callable, Iterable, Protocol, runtime_checkable

#: A predicate over a chunk's identity/metadata, supplied by the caller.
#: Left as a plain callable rather than a typed dataclass -- the shape of
#: "what can you filter retrieval by" is exactly the per-adopter decision
#: this file does not make.
ChunkPredicate = Callable[[object], bool]


@runtime_checkable
class EvidenceSource(Protocol):
    """Note what is absent: no method takes a corpus name, and ``corpus`` is
    a read-only property fixed by the implementing class. A retriever bound
    to one corpus at construction has no code path to any other corpus --
    it is not a filter over a shared store that happens to return empty."""

    @property
    def corpus(self) -> str: ...

    def retrieve(self, predicate: ChunkPredicate, question: str, k: int) -> tuple[object, ...]:
        """Return up to ``k`` chunks matching ``predicate`` for ``question``."""
        ...

    def candidate_ids(self, predicate: ChunkPredicate) -> tuple[str, ...]:
        """The full candidate id set a coverage ledger should be seeded
        with -- before ranking narrows it, per L3's seal-invariant."""
        ...

    def claims_for_chunks(self, chunk_ids: Iterable[str]) -> tuple[object, ...]: ...

    def read_case(self, case_id: str) -> object | None: ...

    def all_cases(self) -> tuple[object, ...]: ...

    def read_document(self, doc_id: str) -> object | None: ...

    def document_count(self) -> int: ...
