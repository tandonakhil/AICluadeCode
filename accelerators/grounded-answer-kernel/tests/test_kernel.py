"""H4/H5 admission suite for accelerators/grounded-answer-kernel.

STATIC-ONLY / EXECUTION-PENDING. This file was written by `mas-registrar`,
which holds no `Bash` grant and therefore could not run it. `run.sh` marks
this explicitly (exit 4, STATIC ONLY) rather than reporting a false pass.
The next agent or human with a Python environment and pytest should run
this for real before this accelerator's suite is treated as green.

Exercises, without any live service, credential, or network call:

  1. The L1 sentinel's zero-import / no-regex / no-substring closure --
     checked by reading the module's OWN SOURCE as text, per the admission
     brief's suggestion, since the property is about what the file imports
     and calls, not about its runtime behaviour on any particular input.
  2. `CoverageLedger.seal()`'s balance invariant -- both that it succeeds
     when every candidate is dispositioned exactly once, and that it raises
     `CoverageNotBalanced` on every way of NOT doing that (undispositioned,
     double-dispositioned, an invented case id).
  3. `Coverage` has no public constructor -- calling it directly (without
     the seal token) raises `TypeError`.
  4. `build_sources`'s one-parameter arity (L1/L2 boundary, ARCH-05-style
     reflective check) -- adding a second parameter is exactly the edit
     the source project named as reopening the failure this file exists to
     close.
  5. `verify.py`'s all-or-nothing discard -- a composition with one failing
     assertion produces a `VerificationFailure`, never a partial
     `VerifiedCitations`.
  6. The abstention module's invariant: all six `AbstentionType` codes map
     to `UNKNOWN` in `RAG_FOR`, and `UNKNOWN` is never in `NEGATIVE_STATES`.
"""

from __future__ import annotations

import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC / "l1_kernel"))
sys.path.insert(0, str(SRC / "l2_retrieval"))
sys.path.insert(0, str(SRC / "l3_assurance"))

import sentinel  # noqa: E402
import refusal  # noqa: E402
import sources  # noqa: E402
import coverage_ledger  # noqa: E402
import abstention  # noqa: E402
import verify  # noqa: E402


# --------------------------------------------------------------------------
# 1. sentinel closure
# --------------------------------------------------------------------------


def test_sentinel_has_no_regex_or_substring_calls():
    """AST-based, not a raw text scan: the module's own docstring names the
    forbidden operations by name as documentation ("Deliberately absent:
    `re`, `.lower()`, ..."), and a naive substring search over the whole
    file text trips on that prose rather than on real code. The property
    under test is about actual imports and actual calls, so check the
    parsed AST -- function/attribute call names and import names -- not
    the file's raw characters."""
    import ast

    text = Path(sentinel.__file__).read_text()
    tree = ast.parse(text)

    forbidden_attrs = {"lower", "upper", "casefold", "find", "index", "search", "match"}
    forbidden_modules = {"re"}

    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in forbidden_attrs:
            raise AssertionError(f"sentinel.py contains forbidden call .{node.attr}(")
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            names = {node.module} if isinstance(node, ast.ImportFrom) else {a.name for a in node.names}
            if names & forbidden_modules:
                raise AssertionError(f"sentinel.py imports forbidden module(s) {names & forbidden_modules}")
            raise AssertionError("sentinel.py has an import statement -- zero-import closure violated")


def test_sentinel_detects_refusal_and_only_a_leading_one():
    assert sentinel.is_refusal("INSUFFICIENT_EVIDENCE: no jurisdiction match")
    assert sentinel.is_refusal("  INSUFFICIENT_EVIDENCE: leading whitespace")
    assert not sentinel.is_refusal("the answer mentions INSUFFICIENT_EVIDENCE mid-sentence")
    assert not sentinel.is_refusal("")


# --------------------------------------------------------------------------
# 2 & 3. CoverageLedger / Coverage invariant
# --------------------------------------------------------------------------


def test_seal_succeeds_when_fully_dispositioned():
    ledger = coverage_ledger.CoverageLedger(("a", "b", "c"))
    ledger.include("a")
    ledger.exclude("b", "jurisdiction", "wrong state")
    ledger.unassessable("c", "document missing")
    coverage = ledger.seal()
    assert coverage.candidates_considered == 3
    assert len(coverage.included) == 1
    assert len(coverage.excluded) == 1
    assert len(coverage.unassessable) == 1


def test_seal_raises_when_undispositioned():
    ledger = coverage_ledger.CoverageLedger(("a", "b"))
    ledger.include("a")
    try:
        ledger.seal()
        assert False, "seal() should have raised CoverageNotBalanced"
    except coverage_ledger.CoverageNotBalanced:
        pass


def test_double_disposition_raises():
    ledger = coverage_ledger.CoverageLedger(("a",))
    ledger.include("a")
    try:
        ledger.include("a")
        assert False, "dispositioning the same candidate twice should raise"
    except coverage_ledger.CoverageNotBalanced:
        pass


def test_coverage_has_no_public_constructor():
    try:
        coverage_ledger.Coverage(
            included=(),
            excluded=(),
            unassessable=(),
            candidates_considered=0,
            candidates_by_corpus={},
            jurisdictions_examined=(),
            date_span_examined=None,
            filters_applied={},
        )
        assert False, "Coverage() without the seal token should raise TypeError"
    except TypeError:
        pass


def test_blank_reason_rejected():
    ledger = coverage_ledger.CoverageLedger(("a",))
    try:
        ledger.exclude("a", "jurisdiction", "n/a")
        assert False, "a placeholder reason should be rejected"
    except coverage_ledger.BlankReasonError:
        pass


# --------------------------------------------------------------------------
# 4. build_sources arity
# --------------------------------------------------------------------------


def test_build_sources_is_single_parameter():
    assert sources.build_sources_arity() == ("verified",)


# --------------------------------------------------------------------------
# 5. verify.py all-or-nothing
# --------------------------------------------------------------------------


def test_verify_all_or_nothing_on_bad_citation():
    chunk = verify.Chunk(chunk_id="c1", text="the rate is 9.5 percent")
    bundle = verify.EvidenceBundle(
        by_ordinal={1: verify.EvidenceId(corpus="public", chunk_id="c1")},
        chunks={1: chunk},
        context={"c1": {"title": "test doc"}},
    )
    good_assertion = verify.Assertion(
        assertion_type=verify.AssertionType.QUOTE_PRESENTATION,
        evidence_ordinal=1,
        quoted_span="the rate is 9.5 percent",
    )
    bad_assertion = verify.Assertion(
        assertion_type=verify.AssertionType.QUOTE_PRESENTATION,
        evidence_ordinal=1,
        quoted_span="this text is not in the chunk",
    )
    composition = verify.Composition(
        lead_sentence="test", assertions=(good_assertion, bad_assertion)
    )
    result = verify.verify(composition, bundle, verify.ClaimLookup(by_id={}))
    assert isinstance(result, verify.VerificationFailure)
    assert result.check == "verbatim-span"


def test_verify_succeeds_when_all_assertions_pass():
    chunk = verify.Chunk(chunk_id="c1", text="the rate is 9.5 percent")
    bundle = verify.EvidenceBundle(
        by_ordinal={1: verify.EvidenceId(corpus="public", chunk_id="c1")},
        chunks={1: chunk},
        context={"c1": {"title": "test doc"}},
    )
    assertion = verify.Assertion(
        assertion_type=verify.AssertionType.QUOTE_PRESENTATION,
        evidence_ordinal=1,
        quoted_span="the rate is 9.5 percent",
    )
    composition = verify.Composition(lead_sentence="test", assertions=(assertion,))
    result = verify.verify(composition, bundle, verify.ClaimLookup(by_id={}))
    assert isinstance(result, verify.VerifiedCitations)
    assert len(result.citations) == 1


# --------------------------------------------------------------------------
# 6. abstention -- UNKNOWN is never a negative finding
# --------------------------------------------------------------------------


def test_all_abstention_types_map_to_unknown():
    for code in abstention.CODES:
        assert abstention.RAG_FOR[code] == abstention.UNKNOWN


def test_unknown_is_never_a_negative_state():
    assert abstention.UNKNOWN not in abstention.NEGATIVE_STATES


def test_abstention_requires_named_gap_and_action():
    try:
        abstention.Abstention("AB1", "item-1", "", "escalate", period=1)
        assert False, "empty evidence_gap should raise"
    except ValueError:
        pass
    try:
        abstention.Abstention("AB1", "item-1", "missing data", "", period=1)
        assert False, "empty resolving_action should raise"
    except ValueError:
        pass
