"""Deterministic citation verification (L3) -- a PURE FUNCTION over an
EvidenceBundle.

``verify`` takes no store handle, no model client, no network. All record
reads happen upstream into ``EvidenceBundle`` / ``ClaimLookup``, which is
what makes the whole check unit-testable without a corpus.

Checks, in order, ALL-OR-NOTHING: any single failure discards the entire
answer, because a result is constructible only from a complete
``VerifiedCitations`` -- there is no code path that removes one bad
assertion and serves the rest.

GENERALISED from ``rate-case-analyzer``'s ``app/grounding/verify.py`` (gate
10, 899 tests) and ``app/grounding/normalise.py``, folded into this single
file because the target layer tree for this accelerator does not carry a
separate normalise module -- the verbatim-span comparison logic is small
enough, and tightly enough coupled to this file's one caller, to live here
without losing anything.

ADAPT, NOT REUSE -- THE PART OF L3 THIS FILE IS THE CLEAREST EXAMPLE OF: the
source module imported RCA's closed domain enums (``Basis``, ``ClaimStatus``,
``Corpus``, ``Parameter``, ``Scope``, ``Unit``, ``DocumentType``) and
validated a Pydantic schema built from them. None of those enums, and no
Pydantic dependency, travel with this file. In their place: plain dataclasses
with ``str`` fields for anything that was a closed RCA enum. The CHECK
STRUCTURE -- evidence-was-supplied, verbatim-span-equality, claim-must-be-
selected-not-restated, exact-tuple-equality-no-converter, all-or-nothing
discard -- is what is being harvested. The six-member ``AssertionType``
vocabulary (PARAMETER_VALUE / CLAIM_STATUS_STATEMENT / ABSENCE_STATEMENT /
CASE_ATTRIBUTE / QUOTE_PRESENTATION / COMPARABILITY_STATEMENT) is kept
because it reads as a genuinely general RAG-assertion taxonomy rather than
RCA-domain vocabulary, but an adopter should confirm that before relying on
it; nothing here enforces that these six remain exhaustive for a new domain.

RAI-G1, preserved: for a numeric assertion the model SELECTS a claim id --
the product renders value/unit/scope/basis/status from the stored row, never
from model text. A caller integrating this file must resolve ``claim_id`` to
a stored ``Claim`` upstream of ``verify``; this module never re-derives a
number from prose.
"""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Mapping, Union

# --------------------------------------------------------------------------
# normalisation (folded in from RCA's normalise.py -- unmodified logic)
# --------------------------------------------------------------------------

SOFT_HYPHEN = "­"
_LINE_BREAK_HYPHENS = ("-\n", "‐\n", "‑\n")


def normalise(text: str) -> str:
    """Return the comparison form of a span.

    NFKC, whitespace-run collapse, soft-hyphen removal, line-break-hyphen
    joining -- and nothing else. Deliberately absent: case folding,
    punctuation stripping, stemming, any fuzzy or semantic matcher, and any
    unit converter. "950 bp" asserted against a stored "9.50 %" therefore
    fails, because nothing here knows how to make them equal -- a
    unit-equivalence coincidence is not evidence that the model read the
    document.

    Order matters: line-break hyphens are joined BEFORE whitespace collapse,
    otherwise "distri-\\nbution" becomes "distri- bution" and never rejoins.
    """
    value = unicodedata.normalize("NFKC", text)
    value = value.replace(SOFT_HYPHEN, "")
    for marker in _LINE_BREAK_HYPHENS:
        value = value.replace(marker, "")
    value = " ".join(value.split())
    return value


def contains_span(haystack: str, needle: str) -> bool:
    """Whether ``needle`` appears verbatim in ``haystack``, after
    normalisation. A substring test is correct here: the question is
    whether a quote is present in a chunk."""
    return normalise(needle) in normalise(haystack)


def spans_equal(left: str, right: str) -> bool:
    """Span EQUALITY, not mere containment. A quote merely present
    somewhere in a chunk can say the opposite of the assertion it is cited
    for (e.g. "it would not be appropriate to adopt the requested 10.4%"
    supporting a claim that 10.4% WAS adopted); for a value-bearing
    assertion the span must EQUAL the stored claim's verbatim quote."""
    return normalise(left) == normalise(right)


# --------------------------------------------------------------------------
# the closed assertion vocabulary
# --------------------------------------------------------------------------


class AssertionType(str, Enum):
    """The admissible vocabulary. See the module docstring's ADAPT note --
    confirm these six remain exhaustive for your own domain before relying
    on the closure.

    ``str, Enum`` rather than ``enum.StrEnum`` deliberately -- StrEnum is
    3.11+ only; this accelerator's floor is >=3.9 (H1)."""

    PARAMETER_VALUE = "PARAMETER_VALUE"
    CLAIM_STATUS_STATEMENT = "CLAIM_STATUS_STATEMENT"
    ABSENCE_STATEMENT = "ABSENCE_STATEMENT"
    CASE_ATTRIBUTE = "CASE_ATTRIBUTE"
    QUOTE_PRESENTATION = "QUOTE_PRESENTATION"
    COMPARABILITY_STATEMENT = "COMPARABILITY_STATEMENT"


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    text: str
    document_type: str = ""
    locator: str = ""
    order_date: object = None
    superseded: bool = False


@dataclass(frozen=True)
class Claim:
    claim_id: str
    chunk_id: str
    claim_status: str = "NOT_STATED"
    verbatim_quote: str = ""
    locator: str = ""
    #: (value, unit, scope, basis) as plain strings/Decimal -- was a typed
    #: tuple over four RCA enums in the source; genericised to whatever an
    #: adopter's own comparison key is.
    comparison_tuple: tuple = ()


@dataclass(frozen=True)
class Assertion:
    assertion_type: AssertionType
    evidence_ordinal: int
    quoted_span: str
    claim_id: str = ""
    asserted_document_type: str = ""
    asserted_claim_status: str = ""
    asserted_value_text: str = ""
    asserted_unit: str = ""
    asserted_scope: str = ""
    asserted_basis: str = ""


@dataclass(frozen=True)
class Composition:
    lead_sentence: str
    assertions: tuple[Assertion, ...]


@dataclass(frozen=True)
class EvidenceId:
    corpus: str
    chunk_id: str


@dataclass(frozen=True)
class EvidenceBundle:
    """Ordinal -> typed evidence. The model never sees a real id."""

    by_ordinal: Mapping[int, EvidenceId]
    chunks: Mapping[int, Chunk]
    #: chunk_id -> resolved-context mapping, e.g. {"title": ..., "url": ...},
    #: read from stored rows upstream so ``build_sources`` (L1) can render
    #: with exactly one parameter.
    context: Mapping[str, Mapping[str, object]] = field(default_factory=dict)

    def ordinals(self) -> tuple[int, ...]:
        return tuple(sorted(self.by_ordinal))


@dataclass(frozen=True)
class ClaimLookup:
    """Claims reachable from the supplied evidence, keyed by claim_id."""

    by_id: Mapping[str, Claim]


@dataclass(frozen=True)
class VerifiedCitation:
    ordinal: int
    corpus: str
    chunk: Chunk
    assertion: Assertion
    claim: Claim | None


@dataclass(frozen=True)
class VerifiedCitations:
    lead_sentence: str
    citations: tuple[VerifiedCitation, ...]
    context: Mapping[str, Mapping[str, object]] = field(default_factory=dict)


@dataclass(frozen=True)
class VerificationFailure:
    check: str
    detail: str
    ordinal: int | None = None


VerificationResult = Union[VerifiedCitations, VerificationFailure]


def _decimal(value: str) -> Decimal | None:
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        return None


def verify(
    composition: Composition,
    supplied: EvidenceBundle,
    claims: ClaimLookup,
) -> VerificationResult:
    verified: list[VerifiedCitation] = []

    for assertion in composition.assertions:
        ordinal = assertion.evidence_ordinal

        # (a) the evidence id was actually supplied
        if ordinal not in supplied.by_ordinal:
            return VerificationFailure(
                check="evidence-supplied",
                detail=(
                    f"E{ordinal} was cited but never supplied. Supplied: "
                    f"{['E%d' % o for o in supplied.ordinals()]}."
                ),
                ordinal=ordinal,
            )

        evidence_id = supplied.by_ordinal[ordinal]
        chunk = supplied.chunks[ordinal]

        # (b) the quoted span is verbatim in that chunk
        if not contains_span(chunk.text, assertion.quoted_span):
            return VerificationFailure(
                check="verbatim-span",
                detail=(
                    "the quoted span was not found character-for-character "
                    f"in the cited chunk E{ordinal}"
                ),
                ordinal=ordinal,
            )

        # (c) asserted document_type matches the stored record
        if (
            assertion.asserted_document_type
            and assertion.asserted_document_type != chunk.document_type
        ):
            return VerificationFailure(
                check="document-type",
                detail=(
                    f"asserted document_type {assertion.asserted_document_type} "
                    f"!= stored {chunk.document_type} for E{ordinal}"
                ),
                ordinal=ordinal,
            )

        claim: Claim | None = None
        needs_claim = assertion.assertion_type in (
            AssertionType.PARAMETER_VALUE,
            AssertionType.CLAIM_STATUS_STATEMENT,
            AssertionType.ABSENCE_STATEMENT,
        )
        if needs_claim:
            if not assertion.claim_id:
                return VerificationFailure(
                    check="claim-selected",
                    detail=(
                        f"a {assertion.assertion_type.value} assertion must "
                        "select a claim_id: the product renders the figure "
                        "from the stored row, never from model text"
                    ),
                    ordinal=ordinal,
                )
            claim = claims.by_id.get(assertion.claim_id)
            if claim is None:
                return VerificationFailure(
                    check="claim-resolves",
                    detail=f"claim_id {assertion.claim_id!r} does not resolve to a stored claim",
                    ordinal=ordinal,
                )
            if claim.chunk_id != chunk.chunk_id:
                return VerificationFailure(
                    check="claim-belongs-to-evidence",
                    detail=(
                        f"claim {assertion.claim_id} belongs to chunk "
                        f"{claim.chunk_id}, not to the cited E{ordinal}"
                    ),
                    ordinal=ordinal,
                )

            # asserted claim_status matches the stored record
            if (
                assertion.asserted_claim_status
                and assertion.asserted_claim_status != claim.claim_status
            ):
                return VerificationFailure(
                    check="claim-status",
                    detail=(
                        f"asserted claim_status {assertion.asserted_claim_status} "
                        f"!= stored {claim.claim_status}. An asked figure is "
                        "never rendered as a granted one."
                    ),
                    ordinal=ordinal,
                )

        if assertion.assertion_type is AssertionType.PARAMETER_VALUE:
            assert claim is not None

            # For a PARAMETER_VALUE assertion the span must EQUAL the stored
            # claim's quote, not merely be found inside the chunk.
            if not spans_equal(assertion.quoted_span, claim.verbatim_quote):
                return VerificationFailure(
                    check="span-equals-claim-quote",
                    detail=(
                        "for a PARAMETER_VALUE assertion the quoted span "
                        "must EQUAL the stored claim's verbatim quote. A "
                        "span merely present in the chunk can say the "
                        "opposite of the assertion."
                    ),
                    ordinal=ordinal,
                )

            # Exact tuple equality over (value, unit, scope, basis). No
            # converter exists -- "950 basis points" never equals "9.50
            # percent" here.
            asserted = (
                _decimal(assertion.asserted_value_text)
                if assertion.asserted_value_text
                else None,
                assertion.asserted_unit or None,
                assertion.asserted_scope or None,
                assertion.asserted_basis or None,
            )
            stored = claim.comparison_tuple
            if any(part is None for part in asserted):
                return VerificationFailure(
                    check="numeric-tuple-complete",
                    detail=(
                        "a PARAMETER_VALUE assertion must state value, "
                        "unit, scope and basis; a bare number is not "
                        "comparable to a stored claim"
                    ),
                    ordinal=ordinal,
                )
            if asserted != stored:
                return VerificationFailure(
                    check="numeric-tuple",
                    detail=(
                        f"asserted {asserted} != stored {stored}. Comparison "
                        "is exact over (value, unit, scope, basis); there is "
                        "no unit converter anywhere in this module."
                    ),
                    ordinal=ordinal,
                )

        if assertion.assertion_type is AssertionType.ABSENCE_STATEMENT:
            assert claim is not None
            if claim.claim_status != "NOT_STATED":
                return VerificationFailure(
                    check="absence-requires-not-stated",
                    detail=(
                        "an ABSENCE_STATEMENT must cite a claim whose stored "
                        f"status is NOT_STATED; this one is {claim.claim_status}"
                    ),
                    ordinal=ordinal,
                )
            if not claim.verbatim_quote.strip():
                return VerificationFailure(
                    check="absence-requires-evidence-of-silence",
                    detail="the system never asserts silence without a quote proving it",
                    ordinal=ordinal,
                )

        verified.append(
            VerifiedCitation(
                ordinal=ordinal,
                corpus=evidence_id.corpus,
                chunk=chunk,
                assertion=assertion,
                claim=claim,
            )
        )

    return VerifiedCitations(
        lead_sentence=composition.lead_sentence,
        citations=tuple(verified),
        context=dict(supplied.context),
    )
