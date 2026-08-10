"""``build_sources`` -- the one-parameter contract (L1).

    def build_sources(verified: VerifiedBundleLike) -> tuple[Source, ...]

**Exactly one parameter.** The raw retrieval result set is not in scope, is
not importable here, and cannot be passed in. That is the whole content of
the deviation ``rate-case-analyzer`` made from ``policy-lookup-assistant``,
whose accepted trade-off was ``sources[] = what retrieval pulled``. The most
dangerous hallucination kind is a real quote from a real source that does not
support the proposition next to it; showing retrieval hits beside a claim
MANUFACTURES the appearance of support. Closed here, structurally, in a
signature ``build_sources_arity()`` lets an architecture suite assert.

GENERALISED from ``rate-case-analyzer``'s ``app/answer/sources.py``. The
source module built ``PublicSource``/``WorkProductSource`` instances typed to
RCA's two-corpus domain and imported ``app.enums.claim.ClaimStatus`` and
``app.enums.corpus.Corpus``. Neither travels with this file. In their place:
a single generic ``Source`` dataclass with an open ``extra: dict`` field for
adopter-specific attributes, and a structural ``VerifiedBundleLike`` /
``VerifiedCitationLike`` Protocol rather than an import of L3's concrete
``VerifiedCitations`` type -- L1 does not depend on L3, and does not need to:
whatever produces a verified bundle (this accelerator's L3, or an adopter's
own verifier) can hand it to ``build_sources`` as long as it has the shape
below.

Everything a source needs travels inside the verified bundle: per the L0
contract, a source is built from what was verified and from stored context
resolved upstream -- never filled in from model output.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass, field
from typing import Any, Mapping, Protocol, Sequence


class SourceContextMissing(KeyError):
    """Corpus labelling and record resolution fail CLOSED at the response
    boundary. A source that cannot be built from a stored row is not built
    at all -- it is never filled in from model output."""


@dataclass(frozen=True)
class Source:
    """A generic, renderable source. Fields left deliberately open via
    ``extra`` -- an adopter's domain (docket numbers, witness names, SKU
    ids, ticket numbers ...) does not belong in a shared kernel file."""

    ordinal: int
    corpus_label: str
    chunk_id: str
    document_type: str
    locator: str
    verbatim_quote: str
    claim_status: str = "NOT_STATED"
    extra: Mapping[str, Any] = field(default_factory=dict)


class _ChunkLike(Protocol):
    chunk_id: str
    document_type: str
    locator: str


class _ClaimLike(Protocol):
    claim_status: str
    locator: str
    verbatim_quote: str


class _AssertionLike(Protocol):
    quoted_span: str


class _VerifiedCitationLike(Protocol):
    ordinal: int
    corpus: str
    chunk: _ChunkLike
    assertion: _AssertionLike
    claim: Any  # _ClaimLike | None


class _VerifiedBundleLike(Protocol):
    citations: Sequence[_VerifiedCitationLike]
    #: chunk_id -> resolved-context mapping, e.g. {"title": ..., "url": ...}.
    context: Mapping[str, Mapping[str, Any]]


def build_sources(verified: _VerifiedBundleLike) -> tuple[Source, ...]:
    sources: list[Source] = []
    for index, citation in enumerate(verified.citations, start=1):
        context = verified.context.get(citation.chunk.chunk_id)
        if context is None:
            raise SourceContextMissing(
                f"no resolved record context for chunk {citation.chunk.chunk_id}; "
                "a source is built from stored rows, never from model output"
            )
        claim_status = (
            citation.claim.claim_status if citation.claim is not None else "NOT_STATED"
        )
        verbatim_quote = (
            citation.claim.verbatim_quote
            if citation.claim is not None
            else citation.assertion.quoted_span
        )
        locator = (
            citation.claim.locator if citation.claim is not None else citation.chunk.locator
        )
        sources.append(
            Source(
                ordinal=index,
                corpus_label=citation.corpus,
                chunk_id=citation.chunk.chunk_id,
                document_type=citation.chunk.document_type,
                locator=locator,
                verbatim_quote=verbatim_quote,
                claim_status=claim_status,
                extra=dict(context),
            )
        )
    return tuple(sources)


def build_sources_arity() -> tuple[str, ...]:
    """Reflection helper for an adopting project's architecture suite (H3):
    assert this stays a one-parameter function. Adding a second parameter --
    e.g. the raw retrieval result set -- is the single edit that would reopen
    the failure this file exists to close."""
    return tuple(inspect.signature(build_sources).parameters)
