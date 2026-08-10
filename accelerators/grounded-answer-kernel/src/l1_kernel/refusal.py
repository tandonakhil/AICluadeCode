"""Typed refusal kinds, gap-naming, and alternative-suggestion filtering (L1).

GENERALISED from ``rate-case-analyzer``'s ``app/grounding/refuse.py``. The
source module built its refusal strings from RCA-domain vocabulary
(precedent cases, jurisdictions, dockets) and imported three RCA-specific
modules: ``app.comparability.dimensions`` (a closed ``Dimension`` enum),
``app.coverage.ledger`` (``Coverage``), and ``app.enums.quarantine``
(``QueryOutcome``, ``RefusalKind``). None of those travel with this file.

What DOES travel, unmodified in shape:

  - the six-kind closed refusal vocabulary (renamed generically below);
  - "on refusal, discard the model's prose entirely" -- a refusal statement
    is composed here, from typed inputs, never from anything the model wrote;
  - ``examined_lines`` builds its lines from a coverage object's
    ``excluded``/``unassessable`` sequences, never from model output, so a
    fabricated case id surviving a discard is structurally impossible;
  - the "no alternative may relax exactly one dimension of the refused
    combination" rule, preserved as ``relaxes_exactly_one_dimension`` --
    RCA's own finding was that this is precisely how a user hand-blends two
    answers into the harm the tool exists to prevent.

ADAPT, NOT REUSE: the six statement templates below are written in neutral
language ("item", "corpus", "combination") rather than RCA's rate-case
vocabulary. An adopting project should expect to rewrite every string in
``STATEMENT_TEMPLATES`` for its own domain -- the STRUCTURE (typed kind ->
statement, gap-naming, examined-lines-from-coverage-not-from-model) is what
this file exists to preserve, not the wording.

``Coverage`` here is a structural Protocol, not an import of L3's concrete
``Coverage`` dataclass -- L1 does not depend on L3. Any object with
``.excluded`` and ``.unassessable`` sequences of items exposing
``case_id``/``item_id``, ``label``, ``dimension``/``reason`` satisfies it.
"""

from __future__ import annotations

from enum import Enum
from typing import Protocol, Sequence

MAX_ALTERNATIVES = 3


class RefusalKind(str, Enum):
    """The closed refusal vocabulary. Six members, no more -- adding a
    seventh here is a contract change (H1), not a call-site convenience.

    ``str, Enum`` rather than ``enum.StrEnum`` deliberately: StrEnum is
    3.11+ only, and this accelerator's admitted floor (H1) is >=3.9, matching
    every current template's ``pyproject.toml``. ``str, Enum`` gives the same
    str-comparable/str-serializable behaviour on 3.9."""

    NOTHING_EXAMINED = "NOTHING_EXAMINED"
    INSUFFICIENT_COVERAGE = "INSUFFICIENT_COVERAGE"  # was NONE_COMPARABLE in RCA
    UNPARSEABLE = "UNPARSEABLE"
    VERIFICATION_FAILED = "VERIFICATION_FAILED"
    MODEL_UNAVAILABLE = "MODEL_UNAVAILABLE"
    NO_DATED_CORPUS = "NO_DATED_CORPUS"


class QueryOutcome(str, Enum):
    """Generic outcome vocabulary an adopter's telemetry can key on."""

    REFUSED_INSUFFICIENT = "REFUSED_INSUFFICIENT"
    REFUSED_PARSE_FAILED = "REFUSED_PARSE_FAILED"
    REFUSED_VERIFICATION_FAILED = "REFUSED_VERIFICATION_FAILED"
    REFUSED_NO_DATED_CORPUS = "REFUSED_NO_DATED_CORPUS"
    REFUSED_MODEL_UNAVAILABLE = "REFUSED_MODEL_UNAVAILABLE"


OUTCOME_FOR_KIND: dict[RefusalKind, QueryOutcome] = {
    RefusalKind.NOTHING_EXAMINED: QueryOutcome.REFUSED_INSUFFICIENT,
    RefusalKind.INSUFFICIENT_COVERAGE: QueryOutcome.REFUSED_INSUFFICIENT,
    RefusalKind.UNPARSEABLE: QueryOutcome.REFUSED_PARSE_FAILED,
    RefusalKind.VERIFICATION_FAILED: QueryOutcome.REFUSED_VERIFICATION_FAILED,
    RefusalKind.NO_DATED_CORPUS: QueryOutcome.REFUSED_NO_DATED_CORPUS,
    RefusalKind.MODEL_UNAVAILABLE: QueryOutcome.REFUSED_MODEL_UNAVAILABLE,
}


#: ADAPT PER PROJECT. Neutral language, deliberately unfinished for any real
#: product -- see the module docstring.
STATEMENT_TEMPLATES: dict[RefusalKind, str] = {
    RefusalKind.NOTHING_EXAMINED: (
        "Nothing was examined. Nothing in the corpus matched what your "
        "question implies, so nothing was retrieved, ranked, or assessed. "
        "This is not a statement that the corpus supports no answer -- it is "
        "a statement that this corpus has never looked at what you asked "
        "about."
    ),
    RefusalKind.INSUFFICIENT_COVERAGE: (
        "{gap_summary} The corpus holds items of each kind separately, and "
        "combining them would produce a figure that describes nothing real."
    ),
    RefusalKind.UNPARSEABLE: (
        "The question could not be resolved into the fields this corpus is "
        "organised by, so no search was performed."
    ),
    RefusalKind.VERIFICATION_FAILED: (
        "An answer was composed and then discarded. A deterministic verifier "
        "checked each citation against the stored record and one check did "
        "not pass, so the entire answer was discarded rather than repaired "
        "or shown with a caveat. The discarded text is not shown, not "
        "summarised, and not offered behind a link."
    ),
    RefusalKind.MODEL_UNAVAILABLE: (
        "No answer was composed. The evidence for this question was "
        "retrieved and assessed -- the coverage below reflects real work -- "
        "but the model that composes an answer from that evidence did not "
        "run, so nothing was produced to check or discard."
    ),
    RefusalKind.NO_DATED_CORPUS: (
        "This corpus has never completed an ingestion run, so it cannot be "
        "dated. No answer is given over a corpus whose as-of date is "
        "unknown."
    ),
}


def statement_for(kind: RefusalKind, *, gap_summary: str = "") -> str:
    template = STATEMENT_TEMPLATES[kind]
    return template.format(gap_summary=gap_summary) if "{gap_summary}" in template else template


def gap_rows(
    *,
    asked_for: dict[str, str],
    corpus_holds: tuple[str, ...],
    missing_dimensions: tuple[str, ...],
) -> tuple[tuple[str, str], ...]:
    """The gap definition list. Names the dimension explicitly."""
    rows: list[tuple[str, str]] = []
    if missing_dimensions:
        label = " x ".join(missing_dimensions)
        suffix = " (in combination)" if len(missing_dimensions) > 1 else ""
        rows.append(("Missing dimension", f"{label}{suffix}"))
    if asked_for:
        rows.append(("You asked for", " . ".join(f"{v}" for v in asked_for.values() if v)))
    for holds in corpus_holds:
        rows.append(("Corpus holds", holds))
    return tuple(rows)


class _ExcludedLike(Protocol):
    case_id: str
    label: str
    dimension: str
    reason: str


class _UnassessableLike(Protocol):
    case_id: str
    label: str
    reason: str


class _CoverageLike(Protocol):
    excluded: Sequence[_ExcludedLike]
    unassessable: Sequence[_UnassessableLike]


def examined_lines(coverage: _CoverageLike) -> tuple[str, ...]:
    """The items that WERE examined, built from ``coverage.excluded`` and
    ``coverage.unassessable`` -- never from anything the model wrote, because
    on a refusal the model's prose is discarded and an item id surviving that
    discard is fabrication in the place nobody thinks to look.

    ``coverage`` is duck-typed on purpose: this is L1 and does not import
    L3's concrete ``Coverage`` dataclass. Any object exposing ``.excluded``
    and ``.unassessable`` sequences with the fields above satisfies it,
    including L3's ``Coverage`` once an adopter wires the two together.
    """
    lines: list[str] = []
    for item in coverage.excluded:
        label = f" . {item.label}" if item.label else ""
        lines.append(f"{item.case_id}{label} -- {item.dimension}: {item.reason}")
    for item in coverage.unassessable:
        label = f" . {item.label}" if item.label else ""
        lines.append(f"{item.case_id}{label} -- could not assess: {item.reason}")
    return tuple(lines)


def relaxes_exactly_one_dimension(
    refused: frozenset[str], candidate: frozenset[str]
) -> bool:
    """An alternative that drops exactly one dimension of the refused
    combination is a workaround, not a narrower question: ask both halves,
    blend by hand, and the user has manufactured with their own hands the
    exact harm a refusal exists to prevent."""
    dropped = refused - candidate
    return len(dropped) == 1 and candidate <= refused


def filter_alternatives(
    refused_dimensions: frozenset[str],
    candidates: tuple[tuple[str, frozenset[str]], ...],
) -> tuple[str, ...]:
    kept: list[str] = []
    for text, dimensions in candidates:
        if relaxes_exactly_one_dimension(refused_dimensions, dimensions):
            continue
        kept.append(text)
        if len(kept) == MAX_ALTERNATIVES:
            break
    return tuple(kept)
