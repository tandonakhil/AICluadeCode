# Changelog -- `accelerators/grounded-answer-kernel`

## 1.0.0 -- 2026-08-09

Initial harvest. `mas-registrar`, under
`admin/proposals/2026-08-08-accelerator-layer.md` (human-approved
2026-08-08), Seed 3 ("Reusable RAG frameworks").

**Added -- four independently-adoptable layers:**

- `src/l0_contract.md` -- the four laws (refusal is a structured signal;
  sources are built from what was verified, never parsed from model output;
  a refusal names the gap; silence is not clearance).
- `src/l1_kernel/sentinel.py` -- harvested VERBATIM from
  `rate-case-analyzer`'s `app/grounding/sentinel.py` (gate 10, 899 tests).
  Zero-import, no-regex, no-substring closure preserved exactly.
- `src/l1_kernel/refusal.py` -- generalised from `app/grounding/refuse.py`.
  RCA-domain enum imports removed; six-kind closed vocabulary and the
  "no alternative relaxes exactly one dimension" rule preserved.
- `src/l1_kernel/sources.py` -- generalised from `app/answer/sources.py`.
  One-parameter `build_sources(verified)` signature preserved exactly, now
  typed against a structural Protocol instead of RCA's concrete corpus
  types.
- `src/l2_retrieval/protocol.py` -- generalised `EvidenceSource` Protocol
  from `app/retrieval/protocol.py`, RCA domain types removed.
- `src/l2_retrieval/hash_embed.py` -- UNMODIFIED logic from
  `app/retrieval/rank.py` (`hash_embed`, `rank_within`): deterministic,
  stdlib+numpy, no API key required.
- `src/l3_assurance/coverage_ledger.py` -- `Coverage`/`CoverageLedger.seal()`
  from `app/coverage/ledger.py`, invariant preserved exactly; only the two
  RCA-specific imports (`Corpus` enum, `STANDING_EXCLUSIONS`) removed in
  favour of plain strings / an adopter-supplied default.
- `src/l3_assurance/abstention.py` -- near-verbatim from
  `conclave-finance-studio`'s `backend/common/abstention.py` (already
  zero-import beyond stdlib). The fourth RAG state, the denominator rule.
- `src/l3_assurance/verify.py` -- generalised from `app/grounding/verify.py`
  + `app/grounding/normalise.py` (folded together; this harvest's target
  tree does not carry a separate normalise module). All-or-nothing discard
  and the closed six-member assertion vocabulary preserved; RCA's closed
  domain enums replaced with plain-string fields.
- `tests/test_kernel.py` + `tests/run.sh` -- H4 suite. Written but not
  executed by `mas-registrar` (no `Bash` grant) -- see [1.0.1].
- `kb-seed/reference_impl_note.md` -- names the worked-reference-
  implementation gap the prior review flagged ("otherwise L3 reads as
  theory") as a follow-up, not a silent omission.

## [1.0.1] -- 2026-08-09

Two real defects found and fixed by actually executing the suite for the
first time (orchestrator pass), not by the STATIC ONLY review:

- **`src/` fix, PATCH-level (no public-contract change): `enum.StrEnum`
  replaced with `str, Enum`** in `l1_kernel/refusal.py` (`RefusalKind`,
  `QueryOutcome`) and `l3_assurance/verify.py` (`AssertionType`). `StrEnum`
  is Python 3.11+ only; every current template's `pyproject.toml` declares
  `requires-python = ">=3.9"` (confirmed by reading all three), so this
  accelerator's own admitted floor (H1) was silently broken for any adopter
  on 3.9 or 3.10 -- collection failed with `ImportError: cannot import name
  'StrEnum'`. `str, Enum` gives the same str-comparable/str-serializable
  behaviour on 3.9+.
- **Test-only fix**: `test_sentinel_has_no_regex_or_substring_calls` did a
  raw substring search over the whole file's text, including its own
  docstring -- which *documents* the forbidden operations by name
  ("Deliberately absent: `re`, `.lower()`, ..."). The prose tripped the
  literal-text check on itself, a false positive with zero relationship to
  `sentinel.py`'s actual code. Rewritten as an AST-based check (real
  `ast.Attribute`/`ast.Import` nodes only), which is what the property
  ("no regex or substring *calls*") actually means.

After both fixes: `13 passed`, exit code 0. No other `src/` file required a
change.

**Deliberately not done (see ACCELERATOR.md "do not build"):** no unified
implementation spanning `policy-lookup-assistant`'s LangChain/Chroma
retrieval and `rate-case-analyzer`'s hand-rolled protocol-over-SQLite
retrieval. `L2` is the deliberate seam where they diverge.

**Status:** `built` (mechanically harvested, real code) but **not yet
`admitted`** -- H9 responsible-AI co-sign from `responsible-ai-architect` is
outstanding. See ACCELERATOR.md's H9 section for the specific open question
flagged for that review.
