"""The coverage ledger (L3) -- an object that must balance before it can exist.

``Coverage`` has **NO PUBLIC CONSTRUCTOR**. The only way to obtain one is
``CoverageLedger.seal()``, which raises unless every candidate is
dispositioned exactly once, so that
``included + excluded + unassessable == candidates_considered`` cannot be
false of any ``Coverage`` that exists. This invariant is preserved EXACTLY
from the source -- every check, every raise path, every property -- with
only the RCA-domain import removed (see below). Do not weaken
``__post_init__``'s enforcement; that check is the entire reason this class
exists.

An unreconciled coverage object fails CLOSED. A user shown ``40 = 0 + 39 + 0``
has no recourse and will still read the answer above it, which converts a
silent bug into a decorative one. The enforcement is here, server-side,
before a response is constructed -- the reconciliation line is still good
pedagogy to print, but the screen is not where it is enforced.

GENERALISED from ``rate-case-analyzer``'s ``app/coverage/ledger.py`` (gate
10, 899 tests). Two changes only, both import-removals, nothing behavioural:

  1. ``from app.enums.corpus import Corpus`` removed. ``corpus`` fields are
     now plain ``str`` (default ``"default"``) instead of an RCA-specific
     closed enum. An adopter that wants a closed corpus vocabulary defines
     its own enum and passes its ``.value`` in -- this file does not care
     what strings it is handed.
  2. ``from app.coverage.standing import STANDING_EXCLUSIONS`` removed.
     ``known_exclusions`` defaults to ``()`` instead of an RCA-specific
     standing-exclusions tuple. An adopter supplies its own at
     ``CoverageLedger(...)`` construction time via the parameter already
     present in the source signature.

Nothing else changed. ``candidates_by_corpus`` still ships because a count
is itself an aggregate, and the merge/seal/balance logic is untouched.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

_SEAL_TOKEN = object()

#: Adopter-supplied. Left empty here -- was RCA's ``STANDING_EXCLUSIONS``
#: import, a project-specific constant that does not belong in a shared
#: kernel file. Pass your own via ``CoverageLedger(..., known_exclusions=)``.
DEFAULT_KNOWN_EXCLUSIONS: tuple[str, ...] = ()


class CoverageNotBalanced(Exception):
    """Raised by ``seal()``. Never caught to produce a partial Coverage."""


class BlankReasonError(ValueError):
    """No blank or placeholder reason, structurally."""


PLACEHOLDER_REASONS = frozenset({"n/a", "na", "none", "-", "--", "unknown", "tbd", "?"})


def _non_empty_str(value: str, *, field_name: str) -> str:
    stripped = value.strip()
    if not stripped or stripped.lower() in PLACEHOLDER_REASONS:
        raise BlankReasonError(
            f"{field_name} may not be blank or a placeholder (got {value!r}). "
            "A reason nobody wrote is a reason nobody can check."
        )
    return stripped


@dataclass(frozen=True)
class Excluded:
    case_id: str
    dimension: str
    reason: str
    corpus: str = "default"
    label: str = ""


@dataclass(frozen=True)
class Unassessable:
    case_id: str
    reason: str
    corpus: str = "default"
    label: str = ""


@dataclass(frozen=True)
class Included:
    case_id: str
    corpus: str = "default"
    label: str = ""


@dataclass(frozen=True)
class Coverage:
    """No public constructor. ``CoverageLedger.seal()`` is the only producer."""

    included: tuple[Included, ...]
    excluded: tuple[Excluded, ...]
    unassessable: tuple[Unassessable, ...]
    candidates_considered: int
    candidates_by_corpus: Mapping[str, int]
    jurisdictions_examined: tuple[str, ...]
    date_span_examined: tuple[str, str] | None
    filters_applied: Mapping[str, str]
    known_exclusions: tuple[str, ...] = DEFAULT_KNOWN_EXCLUSIONS
    _token: object = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        if self._token is not _SEAL_TOKEN:
            raise TypeError(
                "Coverage has no public constructor. Build a CoverageLedger and "
                "call seal(); a Coverage that exists is a Coverage that balances."
            )
        total = len(self.included) + len(self.excluded) + len(self.unassessable)
        if total != self.candidates_considered:
            raise CoverageNotBalanced(
                f"{self.candidates_considered} != {len(self.included)} + "
                f"{len(self.excluded)} + {len(self.unassessable)}"
            )

    # -- the two structurally distinct zero states ---------------------------

    @property
    def nothing_examined(self) -> bool:
        """``candidates_considered == 0`` is a different response SHAPE, not
        a zero in a field. A renderer should select a distinct "nothing
        examined" band rather than a zero-length bar."""
        return self.candidates_considered == 0

    @property
    def none_included(self) -> bool:
        return len(self.included) == 0 and self.candidates_considered > 0

    @property
    def excluded_empty_note(self) -> str:
        """Two zeros, two different sentences. The count alone is never the
        message."""
        if self.excluded:
            return ""
        if self.candidates_considered == 0:
            return (
                "None excluded because nothing reached the comparability "
                "stage -- no candidate matched the filters at all."
            )
        return "None excluded: every candidate examined was comparable on all assessed dimensions."

    @property
    def reconciliation_line(self) -> str:
        if self.candidates_considered == 0:
            return "0 = 0 + 0 + 0 -- there was nothing to account for."
        return (
            f"{self.candidates_considered} = {len(self.included)} + "
            f"{len(self.excluded)} + {len(self.unassessable)} -- "
            "every candidate is accounted for."
        )

    def merge(self, other: "Coverage") -> "Coverage":
        """Merge two sealed objects over DISJOINT candidate sets.

        Re-runs the balance check, so the merge cannot lose a candidate
        either.
        """
        mine = {i.case_id for i in self.included} | {e.case_id for e in self.excluded} | {
            u.case_id for u in self.unassessable
        }
        theirs = {i.case_id for i in other.included} | {e.case_id for e in other.excluded} | {
            u.case_id for u in other.unassessable
        }
        overlap = mine & theirs
        if overlap:
            raise CoverageNotBalanced(
                f"merge requires disjoint candidate sets; both carry {sorted(overlap)}"
            )
        by_corpus = dict(self.candidates_by_corpus)
        for key, value in other.candidates_by_corpus.items():
            by_corpus[key] = by_corpus.get(key, 0) + value
        spans = [s for s in (self.date_span_examined, other.date_span_examined) if s]
        span = (
            (min(s[0] for s in spans), max(s[1] for s in spans)) if spans else None
        )
        return Coverage(
            included=self.included + other.included,
            excluded=self.excluded + other.excluded,
            unassessable=self.unassessable + other.unassessable,
            candidates_considered=self.candidates_considered + other.candidates_considered,
            candidates_by_corpus=by_corpus,
            jurisdictions_examined=tuple(
                dict.fromkeys(self.jurisdictions_examined + other.jurisdictions_examined)
            ),
            date_span_examined=span,
            filters_applied={**self.filters_applied, **other.filters_applied},
            known_exclusions=self.known_exclusions,
            _token=_SEAL_TOKEN,
        )


class CoverageLedger:
    def __init__(
        self,
        candidates: tuple[str, ...],
        *,
        corpus: str = "default",
        labels: Mapping[str, str] | None = None,
        jurisdictions_examined: tuple[str, ...] = (),
        date_span_examined: tuple[str, str] | None = None,
        filters_applied: Mapping[str, str] | None = None,
        known_exclusions: tuple[str, ...] = DEFAULT_KNOWN_EXCLUSIONS,
    ) -> None:
        if len(set(candidates)) != len(candidates):
            raise CoverageNotBalanced(
                f"candidate set contains duplicates: {sorted(candidates)}"
            )
        self._candidates = tuple(candidates)  # immutable, fixed at construction
        self._corpus = corpus
        self._labels = dict(labels or {})
        self._jurisdictions = jurisdictions_examined
        self._span = date_span_examined
        self._filters = dict(filters_applied or {})
        self._known_exclusions = known_exclusions
        self._included: list[Included] = []
        self._excluded: list[Excluded] = []
        self._unassessable: list[Unassessable] = []
        self._seen: set[str] = set()

    @property
    def candidates(self) -> tuple[str, ...]:
        return self._candidates

    def _claim(self, case_id: str) -> None:
        if case_id not in self._candidates:
            raise CoverageNotBalanced(
                f"{case_id!r} is not a candidate; the candidate set is fixed at "
                "construction so a disposition cannot invent one"
            )
        if case_id in self._seen:
            raise CoverageNotBalanced(f"{case_id!r} dispositioned more than once")
        self._seen.add(case_id)

    def include(self, case_id: str) -> None:
        self._claim(case_id)
        self._included.append(
            Included(case_id=case_id, corpus=self._corpus, label=self._labels.get(case_id, ""))
        )

    def exclude(self, case_id: str, dimension: str, reason: str) -> None:
        self._claim(case_id)
        self._excluded.append(
            Excluded(
                case_id=case_id,
                dimension=_non_empty_str(dimension, field_name="dimension"),
                reason=_non_empty_str(reason, field_name="reason"),
                corpus=self._corpus,
                label=self._labels.get(case_id, ""),
            )
        )

    def unassessable(self, case_id: str, reason: str) -> None:
        self._claim(case_id)
        self._unassessable.append(
            Unassessable(
                case_id=case_id,
                reason=_non_empty_str(reason, field_name="reason"),
                corpus=self._corpus,
                label=self._labels.get(case_id, ""),
            )
        )

    def seal(self) -> Coverage:
        """Raises unless every candidate is dispositioned exactly once."""
        undispositioned = tuple(c for c in self._candidates if c not in self._seen)
        if undispositioned:
            raise CoverageNotBalanced(
                f"{len(undispositioned)} candidate(s) undispositioned: "
                f"{sorted(undispositioned)}. Silence is not clearance: a "
                "candidate that was dropped without a reason is exactly the "
                "state coverage exists to make impossible."
            )
        return Coverage(
            included=tuple(self._included),
            excluded=tuple(self._excluded),
            unassessable=tuple(self._unassessable),
            candidates_considered=len(self._candidates),
            candidates_by_corpus={self._corpus: len(self._candidates)},
            jurisdictions_examined=self._jurisdictions,
            date_span_examined=self._span,
            filters_applied=self._filters,
            known_exclusions=self._known_exclusions,
            _token=_SEAL_TOKEN,
        )
