# Test evidence — audit of every scenario that changed since the last run

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

Three commits sit between `e00a214` (the commit pass 19 reported on) and
`c428fe5`. Between them they touch **three test files and no product file**.
Every changed scenario is audited below — a scenario that changed is a coverage
decision, and this pass's whole job is that a change made to close a finding
did not open another.

## The three commits

| Commit | Files | Lines |
|---|---|---|
| `6da659e` — *Words a reviewer reads, compared to a second copy and not to their source* | `backend/tests/test_obligation_gap.py` | +60 −7 |
| `05be347` — *"Every produced file" needs more than one file to be a claim about* | `tests/suites/functional/test_f40_criteria.py` | +18 −7 |
| `c428fe5` — *The assertion was right and the sentence above it was not* | `tests/suites/functional/test_unclaimed_criteria.py` | +10 −2 |

**No product code changed.** The two findings were both about what the tests
compare against, not about what the build does.

---

### Scenario: `test_each_kind_labels_its_own_fields_in_its_own_words` — comparison target moved outside the code under test
- Status: EXECUTED
- Input: the diff at `6da659e`, then mutations B-M1, B-M1b
- Expected: the expected words now live in the test file, not in
  `obligation_gap.KIND_VOCABULARY`, and coverage does not narrow
- Actual: **compares against `EXPECTED_KIND_WORDS`, a literal table in the test
  file.** Coverage **widened**: five worded fields per kind
  (`finding_type`, `summary`, `origin_label`, `period_label`, `amount_label`)
  against the four asserted before pass 19 — `summary` had never been asserted
  in any revision. The parametrisation still enumerates
  `sorted(obligation_gap.KIND_VOCABULARY)`, so a fourth kind still arrives with
  a scenario pointed at it
- Result: PASS
- Evidence: both mutations fail (see `mutation-tests-2026-08-03.md`, B-M1 and
  B-M1b)

### Scenario: `test_every_kind_the_build_holds_has_its_words_written_out_in_this_file` — the new scenario, and whether it can fail
- Status: EXECUTED
- Input: `assert sorted(obligation_gap.KIND_VOCABULARY) == sorted(EXPECTED_KIND_WORDS)`;
  mutation B-M2 adds a benign, internally consistent fourth kind
- Expected: it is what makes the parametrisation able to fail on a fourth kind,
  rather than a restatement of something already asserted
- Actual: **it fails under B-M2**, at `test_obligation_gap.py:297`. Two other
  scenarios fail alongside it, so the fourth-kind case is triple-covered
- Result: PASS — a genuine addition, not a tautology
- Evidence: `3 failed, 25 passed` under B-M2

### Scenario: `test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts` — fixture change, not assertion change
- Status: EXECUTED
- Input: the diff at `05be347`; mutations A-M1, A-M2, A-M3
- Expected: the per-entry assertions are unchanged and the *population* is what
  moved; the population is driven through the real control, not fabricated
- Actual: **the three per-entry assertions are byte-identical** to the pass-18
  version. What changed: the export control is driven **three times** through
  `POST /proposal/{id}/export` (the same route a user reaches), and two
  population guards were added **before** the loop —
  `assert register["count"] >= 3` and group-id distinctness
- Result: PASS
- Evidence: A-M1 (blank the three facts on all but the newest row) now fails,
  **on the full tree**, `1 failed, 2987 passed`; A-M3 (idempotent re-export)
  fails at line 904, the population guard, not at line 909

### Scenario: does the guard-first ordering do what its comment claims
- Status: EXECUTED
- Input: mutation A-M3 makes re-export idempotent per proposal
- Expected: the scenario **fails at the population assertion** rather than
  passing over one row — which is the whole reason the guard is first
- Actual: **`AssertionError: 1` / `assert 1 >= 3` at `test_f40_criteria.py:904`**
- Result: PASS — the ordering is load-bearing and was verified, not assumed
- Evidence: the failure line number is the guard's, not the loop's

### Scenario: is the three-export population real, or a fixture pretending to be one
- Status: EXECUTED
- Input: mutation A-M2 makes re-export idempotent keyed on `content_hash`
- Expected: no effect — the three exports are genuinely distinct files
- Actual: **`1 passed`**, population unaffected. The three are distinct
  artefacts with distinct content hashes and distinct group ids, produced by
  three real trips through the export control
- Result: PASS — recorded as a negative control, so the guard is shown not to
  fire on things it should not fire on
- Evidence: A-M2 in `mutation-tests-2026-08-03.md`

### Scenario: `test_the_broker_answers_the_population_question_UNKNOWN_and_not_none` — docstring only
- Status: EXECUTED
- Input: the diff at `c428fe5`
- Expected: no assertion changed; the prose now matches F3-M2's result
- Actual: **+10 −2 lines, all inside the docstring.** The scenario now states
  that it **fails** on the day findings become ledger-recorded, and says why
  that is the intent: *"the UNKNOWN is correct only while the ledger cannot
  carry the answer"*
- Result: PASS
- Evidence: `git show c428fe5` — the diff hunk contains no executable line

### Scenario: nothing else in the tree changed
- Status: EXECUTED
- Input: `git diff --stat e00a214..c428fe5`
- Expected: three test files, zero product files
- Actual: **three test files, 88 insertions, 16 deletions, zero product files**
- Result: PASS
- Evidence: the per-commit stats above
