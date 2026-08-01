# Test evidence — register cross-check and suite scrutiny

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run)
**Date:** 2026-08-01
**Commit under test:** `dev` @ **`f56ab9f`** · parent repo @ **`8939ebb`**
**Previous run compared against:** `dev` @ `b1b5dde`
**Owner:** `test-agent`
**Status:** `EXECUTED` — every check below was run, not read

This file is the scrutiny half of the corpus: the seven questions the gate-8
brief posed, plus the standing contradiction question. The per-suite pass/fail
data is in the seven sibling files.

**Method note.** Four of these checks are **mutation tests**: the control is
deliberately broken, the suite is re-run, and the check is only credited if
tests fail. A control that survives its own removal is not evidenced by a green
suite. Every mutation was reverted and `git status --short` confirmed clean
before the corpus was written (verified: clean, HEAD `f56ab9f`).

---

## C1 — `AC-F2-08`'s new control, and the tests it broke

**Question:** the new version-stamp control broke existing tests that had been
approving without a stamp. Did the fixes strengthen those tests, or route
around the control?

### Scenario: C1a — the control has no bypass parameter
- Status: EXECUTED
- Input: `grep -n "skip\|bypass\|force\|allow_missing\|ignore_" backend/ges/versions.py`
- Expected: no flag by which a caller can decline the check
- Actual: two hits, both the word "force" inside prose ("in force"). **No bypass parameter exists.** `check_closure_input` is called from `Broker.decide` *before* the closure, so no path computes an eligibility over a partial input and discards it
- Result: PASS
- Evidence: `versions.py:74 "The six artefact versions in force..."`, `versions.py:77 "...still show what was in force..."` — prose only

### Scenario: C1b — MUTATION: is the control load-bearing?
- Status: EXECUTED
- Input: `check_closure_input` patched to `return ClosureInput(usable=True, reason=None)` unconditionally, then `pytest tests/suites/functional/test_f2_version_criteria.py backend/tests/test_version_registry.py backend/tests/test_authorship_closure.py`
- Expected: if the AC-F2-08 group is real, disabling the control must fail tests
- Actual: **21 failed, 65 passed.** The control is load-bearing
- Result: PASS
- Evidence: `FAILED test_any_single_missing_element_makes_the_closure_input_unusable[guardrail_bundle_hash]`, `FAILED test_an_unresolvable_registry_is_checked_BEFORE_the_stamp`, `FAILED test_a_complete_but_unregistered_stamp_is_unusable_and_names_the_element` … `21 failed, 65 passed in 0.47s`. Reverted; re-run clean at `86 passed`

### Scenario: C1c — the fixes supply a REAL stamp, not a fake one
- Status: EXECUTED
- Input: read `backend/tests/conftest.py::valid_version_stamp` and the diff of every scenario that adopted it
- Expected: the shared helper builds a stamp through the real registry, not a hand-written dict that merely looks complete
- Actual: `valid_version_stamp` calls `versions.stamp_for(...)` — the production constructor — and takes the **fetched** `bundle.bundle_hash` rather than a display literal. Its own docstring states why it is shared: *"so that a test about identity is not silently also a test about stamps"*
- Result: PASS
- Evidence: `return versions.stamp_for(tool_config=..., dataset=..., guardrail_bundle_hash=bundle_hash).as_dict()`

### Scenario: C1d — each adopting scenario says why, and withholds only what it tests
- Status: EXECUTED
- Input: `git diff b1b5dde..HEAD -- backend/tests/test_broker_action_path.py backend/tests/test_ui_write_path.py backend/tests/test_authorship_closure.py`
- Expected: a note at each site distinguishing the two fail-closed layers
- Actual: present at every site. The clearest is `test_an_approval_with_no_authorship_context_is_unevaluable_and_denies`: *"Two fail-closed layers now stand in front of an approval and they deny for different reasons. This scenario is about the second … so it supplies the first layer's input and **withholds only what it is testing**."* One scenario passes `version_stamp={}` deliberately, as the negative case
- Result: PASS
- Evidence: `+ "version_stamp": valid_version_stamp(broker.bundle.bundle_hash),` with `+ # A COMPLETE stamp, deliberately: this scenario is about identity, and AC-F2-08's input-set check now denies before the identity rules are reached. Without a stamp here the scenario would pass for the wrong reason.`

### Scenario: C1e — DID ANY CHANGED TEST LOSE ASSERTIONS?
- Status: EXECUTED
- Input: AST comparison of every same-named test function at `b1b5dde` vs `f56ab9f`, counting `ast.Assert` and `ast.withitem` (`pytest.raises`) nodes per function
- Expected: routing around a control shows up as a changed test with **fewer** assertions
- Actual: **35 test functions changed body. Zero lost an assertion. Three gained one:** `test_the_full_population_conclusion_uses_a_universal_quantifier` (1→2), `test_AC_F33_01_…` (6→7), `test_all_eleven_specified_primitives_are_now_built` (2→4). All other 32 held their count exactly
- Result: PASS
- Evidence: `changed tests with a NET LOSS of assertions: 0`

**C1 verdict: the fixes strengthened or held. None routed around the control.**

---

## C2 — can an undeclared primitive arrive unnoticed?

**Question:** `obligation_gap` and `journal_attribute_outlier` sit outside
`ARCHITECTURE_KB` §7.3's eleven and are declared in `UNSPECIFIED_BUT_BUILT`.
Does that declaration mechanism actually fire?

### Scenario: C2a — the guard is an equality, not a subset
- Status: EXECUTED
- Input: read `backend/tests/test_detector_manifests.py:166`
- Expected: a `<=` subset check would permit any number of undeclared primitives; only an equality closes it
- Actual: `assert set(REGISTERED) - set(SPECIFIED) == set(UNSPECIFIED_BUT_BUILT)` — set **equality**, with a companion `assert set(SPECIFIED) & set(UNSPECIFIED_BUT_BUILT) == set()`. The in-file comment names the exact failure it prevents: *"`<=` alone would permit any number of undeclared ones"*
- Result: PASS
- Evidence: `assert set(REGISTERED) - set(SPECIFIED) == set(UNSPECIFIED_BUT_BUILT)`

### Scenario: C2b — MUTATION: plant an undeclared primitive
- Status: EXECUTED
- Input: `REGISTERED["sneaky_new_primitive"] = lambda x: None`, registered but absent from both `SPECIFIED` and `UNSPECIFIED_BUT_BUILT`; then evaluate the three guard assertions
- Expected: the guard must refuse it
- Actual: **MUTATION KILLED.** The assertion failed and the diff named the intruder
- Result: PASS
- Evidence: `MUTATION KILLED -- undeclared primitive is refused. diff = ['sneaky_new_primitive']`

### Scenario: C2c — the empty `SPECIFIED_BUT_NOT_IMPLEMENTED` list did not lose its check
- Status: EXECUTED
- Input: `test_a_specified_but_unimplemented_primitive_still_says_so`
- Expected: with the real list empty, the not-implemented behaviour must be asserted against a **planted** entry rather than by a `parametrize` over an empty tuple
- Actual: the scenario `monkeypatch`es `SPECIFIED_BUT_NOT_IMPLEMENTED = ("hypothetical_twelfth",)` and asserts `"NOT IMPLEMENTED" in str(exc.value)`. It executed and passed
- Result: PASS
- Evidence: `backend/tests/test_detector_manifests.py::test_a_specified_but_unimplemented_primitive_still_says_so PASSED`

**C2 verdict: the declaration mechanism fires. An undeclared primitive cannot
arrive unnoticed.**

---

## C3 — dossier schema v2, and whether `_read_v1` is genuinely exercised

### Scenario: C3a — v1's required-key list was not retroactively widened
- Status: EXECUTED
- Input: introspect `dossier.REQUIRED_KEYS`
- Expected: v2 adds `semantic_versions`; v1's list is untouched, so no previously written v1 record becomes incomplete
- Actual: `REQUIRED_KEYS[1]` has **11** keys and does **not** contain `semantic_versions`; `REQUIRED_KEYS[2]` has **12** and does. v1 is a strict subset of v2
- Result: PASS
- Evidence: `REQUIRED_KEYS[1] has semantic_versions? False` / `REQUIRED_KEYS[2] has semantic_versions? True` / `v1 list is a strict subset of v2: True` / `v1 list unchanged length: 11 v2: 12`

### Scenario: C3b — a genuine v1 record round-trips complete
- Status: EXECUTED
- Input: `test_the_v1_reader_survives_the_move_to_v2` — builds a payload, sets `payload_schema_version = 1`, **deletes** `semantic_versions`, writes it through the real store, reads it back
- Expected: `write` validates against `REQUIRED_KEYS[1]` (not v2's), `read` dispatches to `_read_v1`, and every v1 required key materialises non-None
- Actual: executed and passed. Asserts `1 in READERS`, every `REQUIRED_KEYS[1]` key non-None, `"semantic_versions" not in read_back`, and `_evidence.payload_schema_version == 1`
- Result: PASS
- Evidence: `backend/tests/test_evidence_store.py::test_the_v1_reader_survives_the_move_to_v2 PASSED`

### Scenario: C3c — MUTATION: drop the v1 reader
- Status: EXECUTED
- Input: `READERS = {2: _read_v2}` (v1 reader removed), then `pytest backend/tests/test_evidence_store.py`
- Expected: at least one test must fail, or `_read_v1` is decorative
- Actual: **2 failed, 42 passed** — `test_the_v1_reader_survives_the_move_to_v2` and `test_every_required_key_list_has_a_reader`. Reverted; tree clean
- Result: PASS
- Evidence: `FAILED backend/tests/test_evidence_store.py::test_the_v1_reader_survives_the_move_to_v2` / `FAILED …::test_every_required_key_list_has_a_reader` / `2 failed, 42 passed in 0.18s`

**C3 verdict: `_read_v1` is genuinely exercised, its removal is caught, and no
v1 record is now reported incomplete.**

---

## C4 — the two rewritten tests

### Scenario: C4a — `test_the_full_population_conclusion_uses_a_universal_quantifier`
- Status: EXECUTED
- Input: `git show b1b5dde:…` vs `HEAD`
- Expected: the replacement must assert something real, not merely re-word
- Actual: **strictly stronger.** Before: one substring, `assert "full declared population" in text`. After: `assert "100% of the declared expected population" in text` **and** `assert "all 10 of 10 declared members" in text` — a proportion and a count, tied to `AC-F42-05`. Its docstring states the reason: the old wording *"reads as a universal quantifier to somebody who already knows the declared population is the denominator, and says nothing about coverage to anybody else"*
- Result: PASS (assertions 1 → 2)
- Evidence: `- assert "full declared population" in text` → `+ assert "100% of the declared expected population" in text` `+ assert "all 10 of 10 declared members" in text`

### Scenario: C4b — `test_a_dossier_round_trips_complete`
- Status: EXECUTED
- Input: same diff
- Expected: a real adaptation to v2, not a loosening
- Actual: `REQUIRED_KEYS[1]` → `REQUIRED_KEYS[CURRENT_SCHEMA_VERSION]`, so it now checks **12** keys rather than 11, and tracks the current version instead of a literal. Content-hash equality against the written record is retained. A new header states that this section no longer covers `AC-F1-08` and why (register 20), so an ID-to-check scan cannot pick it up as evidence for a criterion nothing satisfies
- Result: PASS (assertions 3 → 3, coverage 11 keys → 12)
- Evidence: `- for key in dossier_module.REQUIRED_KEYS[1]:` → `+ for key in dossier_module.REQUIRED_KEYS[dossier_module.CURRENT_SCHEMA_VERSION]:`
- **Advisory (minor):** the version assertion is now `read_back[...] == CURRENT_SCHEMA_VERSION` where the payload was also written at `CURRENT_SCHEMA_VERSION`, so this one assertion can no longer detect a wrong-version write. It is not a gap — `test_the_v1_reader_survives_the_move_to_v2` pins version 1 explicitly and `test_writing_an_unknown_payload_version_is_refused` pins the refusal — but on its own that line is now self-satisfying.

**C4 verdict: both replacements assert something real. One is strictly
stronger; one widened its key coverage and shed a false ID claim.**

---

## C5 — registers 29 and 30: does anything claim what they deny?

### Scenario: C5a — register 30, the uncalibrated `journal_attribute_outlier` threshold
- Status: EXECUTED
- Input: `grep -rni "calibrat"` across the primitive, its unit file and `test_f42_criteria.py`; plus a sweep for any assertion claiming a measured rate
- Expected: `min_attributes: 3` and `rarity_ceiling: 0.05` must nowhere be read as calibrated, and no measured likelihood/precision/false-positive rate may be claimed
- Actual: every hit is a **denial**. Module header: `THE THRESHOLD IS NOT CALIBRATED, AND THAT IS STATED RATHER THAN IMPLIED`. The denial is written into `detail["threshold_calibration"]` **inside the per-finding loop, before `findings.append`**, so every emitted finding carries it: *"…are DECLARED in the detector manifest and are not calibrated against a measured false-positive rate on real close data. This finding states that the journal carries these attributes; it does not assert a measured likelihood."* The sweep for over-claiming assertions returned **nothing**
- Result: PASS
- Evidence: sweep for `assert.*calibrated|false_positive_rate|measured_precision|measured likelihood`, excluding denials → `(end)` (zero hits). `journal_attribute_outlier.py:236-244`
- **Advisory (naming, not coverage):** `test_every_finding_carries_the_uncalibrated_threshold_denial` asserts over **one** finding, not every finding. The module structure guarantees the claim (the assignment precedes `append` in the loop), so the property holds — but the test's name promises a universal it does not itself quantify over.

### Scenario: C5b — register 30, `AC-F42-02` claims only what it can
- Status: EXECUTED
- Input: read the F42 checks
- Expected: `AC-F42-02` asks the journal and the attributes that made it an outlier to be **named**, which does not depend on calibration
- Actual: the checks assert `min_attributes == 3`, `scored_attributes == list(SCORED_ATTRIBUTES)`, and that the threshold statement carries `"3 or more"` and `"inclusive"`. They assert naming and inclusivity — not likelihood
- Result: PASS
- Evidence: `assert "3 or more" in found["threshold_statement"]` / `assert "inclusive" in found["threshold_statement"]`

### Scenario: C5c — register 29, the semantic layer
- Status: EXECUTED
- Input: read `SemanticElement` in `ges/registry/loader.py` and `test_semantic_versions_criteria.py`
- Expected: `AC-F39-04` is satisfied (versions are *stated*), but nothing may claim a metric store or cross-query consistency
- Actual: the in-file denial is present and explicit — *"A real semantic layer holds metrics and joins as artefacts in their own right, versioned INDEPENDENTLY of the queries that use them. This build has no such store"* — and names both consequences, including *"nothing cross-checks that two queries naming `posting_period_join@1.9` mean the same join."* A missing `semantics` key is a **compile error**, not an empty default, so a query cannot produce an answer that states nothing and looks like one with nothing to state
- Result: PASS
- Evidence: `loader.py:94-105` (`SUBSTITUTION, STATED (register entry 29)`), `loader.py:314` (`A MISSING semantics KEY IS A COMPILE ERROR, not an empty default`)

### Scenario: C5d — register 4, the retention lock
- Status: EXECUTED
- Input: `grep -rn "has_retention_lock"`
- Expected: nothing may assert the lock is real
- Actual: `has_retention_lock = True` exists **only on the abstract base** `ObjectLockArchive(abc.ABC)`, which has three `@abc.abstractmethod`s and cannot be instantiated. The concrete `StubObjectLockArchive` overrides it to `False` and raises `StubRefusedInProduction` under `CONCLAVE_ENV=production`. Both tests that touch it assert `is False`
- Result: PASS (no contradiction)
- Evidence: `tests/suites/functional/test_acceptance_criteria.py:369: assert StubObjectLockArchive.has_retention_lock is False`; `backend/tests/test_evidence_store.py:336: assert archive.has_retention_lock is False`

**C5 verdict: registers 29 and 30 are honoured. Nothing claims what they deny.**

---

## C6 — THE STANDING QUESTION: does any suite report a pass the register says cannot be true?

### Scenario: C6a — denied criteria in test function names
- Status: EXECUTED
- Input: the full collected node list (2,223 IDs) searched for each criterion the register denies
- Expected: zero, for every one
- Actual: **zero for all nine**
- Result: PASS
- Evidence:
  ```
  F1_11 0   F1_08 0   F38_11 0   F26_05 0   F41_08 0
  REFUSAL_11 0   F40_17 0   F40_18 0   F36_48 0
  ```

### Scenario: C6b — `COVERS` joins naming a denied criterion
- Status: EXECUTED
- Input: every `COVERS` docstring across `tests/suites` and `backend/tests`, filtered to the nine denied IDs
- Expected: zero, or narrowed to a clause with the denial stated
- Actual: **two hits, both `AC-F36-48`, both narrowed to a named clause** — `"COVERS AC-F36-48's computation clause"` and `"COVERS AC-F36-48's other tail"`. They sit under a 13-line block header naming **register 27** and stating *"That is enough to evidence the COMPUTATION … and it is NOT the criterion's input … nothing here is evidence that the band is calibrated or that a real skill would land in it."* Each docstring restates the bound individually
- Result: PASS with an advisory (below)
- Evidence: `backend/tests/test_abstention.py:309-321` (the `WHAT THESE SCENARIOS ARE NOT — DEFERRED-SUBSTITUTION REGISTER 27` header), `:325`, `:349`

**C6 verdict: no contradiction. No suite reports a pass the register says
cannot be true.** This is the second consecutive pass at which that holds.

### ADVISORY A1 — `AC-F36-48` is the one denied criterion that still has `COVERS` joins
Not a false pass, and it does not stop the gate. The prose is honest and the
clause qualifiers are correct. The residual is **mechanical**: gate 9 maps
`COVERS` joins by ID, and these two strings contain the bare token
`AC-F36-48`, so an ID-keyed scan picks them up and would score the criterion
as covered by two checks. This is the identical shape the `AC-F36-47`
over-broad join had at gate 8. For `code-agent`: put the denial **inside the
join string**, e.g. `COVERS AC-F36-48 (computation clause ONLY — criterion NOT
satisfied, register 27)`, so the qualifier survives a scan that reads only the
`COVERS` line. Every other denied criterion is already at zero joins.

---

## C7 — the empty-`parametrize` sweep

**Question:** a `parametrize` over an empty collection collects zero tests and
reports green. One instance was caught last run. Are there others, now that
many new parametrised checks exist?

### Scenario: C7a — every parametrised function must contribute at least one node ID
- Status: EXECUTED
- Input: AST walk of all 82 test files, collecting every function decorated with `parametrize`, cross-referenced against the 2,223 collected node IDs
- Expected: zero parametrised functions contributing zero nodes
- Actual: **92 parametrised test functions found in source; all 92 contributed at least one node ID. Zero degenerate instances**
- Result: PASS
- Evidence:
  ```
  collected node IDs: 2223 across 82 files
  parametrized test functions found in source: 92
  === PARAMETRIZED FUNCTIONS THAT COLLECTED ZERO NODES ===
  NONE -- every parametrized test function contributed at least one node ID
  ```
- **Method caveat, recorded because it nearly produced a false report.** My first
  run of this sweep passed `--collect-only -q` while `pytest.ini` already sets
  `addopts = -q`. The resulting `-qq` prints per-file *counts* rather than node
  IDs, so zero node IDs parsed and **every one of the 92 functions was reported
  as collecting nothing** — a 92-item false-positive list. The tell was the
  header line `collected node IDs: 0 across 0 files`. Re-run with `-o addopts=`
  it reports 2,223 across 82 files. Any future run of this sweep must assert a
  non-zero collection count before trusting its findings.

### Scenario: C7b — the known instance stays fixed
- Status: EXECUTED
- Input: `SPECIFIED_BUT_NOT_IMPLEMENTED`, the tuple that was emptied at pass 5
- Expected: still empty, and still guarded by a planted-entry scenario rather than by a `parametrize` over it
- Actual: `SPECIFIED_BUT_NOT_IMPLEMENTED = ()`, and both guards executed and passed — `test_all_eleven_specified_primitives_are_now_built` (which asserts the tuple is empty) and `test_a_specified_but_unimplemented_primitive_still_says_so` (planted entry). The former **gained two assertions** this pass (2 → 4)
- Result: PASS
- Evidence: both node IDs `PASSED` in the `-v` list; `primitives/__init__.py:102`

**C7 verdict: no empty-`parametrize` instances remain.**

---

## C8 — test-count delta, measured rather than asserted

The previous run's counts were re-derived by checking out `b1b5dde` into a
**git worktree** and collecting there, rather than trusted from the recorded
table. They reconcile exactly with what `PROJECT_CONTEXT.md` recorded.

| Suite | `b1b5dde` | `f56ab9f` | Added | Removed | Changed (same name, new body) |
|---|---|---|---|---|---|
| unit/integration (`backend/tests`) | 1,428 | 1,663 | +235 | **0** | 24 |
| functional | 96 | 268 | +172 | **0** | 5 |
| architecture | 23 | 23 | 0 | **0** | 1 |
| security | 14 | 14 | 0 | **0** | 0 |
| red-team | 46 | 46 | 0 | **0** | 2 |
| ux | 186 | 186 | 0 | **0** | 1 |
| industry | 23 | 23 | 0 | **0** | 0 |
| **total** | **1,816** | **2,223** | **+407** | **0** | **35** |

- Status: EXECUTED
- Input: `git worktree add --detach <tmp> b1b5dde`, `--collect-only` in both trees, then a name-level `comm` diff and an AST body diff
- Expected: name every removed and changed test; an unexplained drop is a finding
- Actual: **zero test functions were removed.** 324 unique new function names, 35 changed bodies, none with a net assertion loss (C1e)
- Result: PASS
- Evidence: `unique test FUNCTIONS: old=1456 new=1780` / `=== REMOVED (present at b1b5dde, gone now) ===` → *(empty)* / `=== ADDED count === 324`

### FINDING F1 — the headline "2,223, up from 1,428" is not a like-for-like comparison
The gate brief states the suite went from 1,428 to 2,223 tests. Those two
numbers measure different things:

- **1,428** was the *unit/integration suite alone* at `b1b5dde` — the figure in
  that row of `PROJECT_CONTEXT.md`'s table. The full pytest run at `b1b5dde`
  was **1,816** (1,428 + 388 across the six SME suites), which the same table
  records as its total.
- **2,223** is the *full pytest run* at `f56ab9f` — every suite, because
  `pytest.ini` sets `testpaths = backend/tests tests/suites`.

The like-for-like figures are **unit/integration 1,428 → 1,663 (+235)** and
**total 1,816 → 2,223 (+407)**. The growth is real and substantial either way;
this is a reporting correction, not a defect, and it is recorded because a
+795 headline against a +407 actual would compound at the next gate.

---

## Summary of advisories (none stops the gate)

| # | Advisory | For |
|---|---|---|
| A1 | `AC-F36-48`'s two `COVERS` joins carry the bare ID; the clause qualifier lives in prose an ID-keyed scan will not read | `code-agent` |
| A2 | `state.select_tier`'s docstring first line ("falls back to CERTIFIED") contradicts both the code and its own next paragraph | `code-agent` |
| A3 | `test_every_finding_carries_the_uncalibrated_threshold_denial` asserts over one finding, not every finding | `code-agent` |
| A4 | `test_a_dossier_round_trips_complete`'s version assertion is now self-satisfying in isolation (covered elsewhere) | `code-agent` |
| F1 | The headline test-count delta compares unit/integration-then against total-now | orchestrator / gate 9 |
| D1 | Corpus date is `2026-08-01`; the system clock and every commit date read `2026-07-31` | orchestrator |
