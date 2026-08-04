# Test evidence — mutation tests against the two gate-8 findings

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

Every mutation below was applied to **product code**, run, and reverted. The
working tree was verified clean (`git status --porcelain` empty, HEAD
`c428fe5`) after the last revert.

## The commits under test

| Commit | Closes |
|---|---|
| **`6da659e`** — *"Words a reviewer reads, compared to a second copy and not to their source"* | Finding B — `obligation_gap` kind vocabulary compared to itself |
| **`05be347`** — *"'Every produced file' needs more than one file to be a claim about"* | Finding A — `AC-F40-16` quantified over a one-row register |
| **`c428fe5`** — *"The assertion was right and the sentence above it was not"* | the F3 docstring, which claimed the opposite of what its assertions do |

---

## Finding B — `obligation_gap`

### Scenario: B-M1 — reword all three `scheduled_reversal` labels
- Status: EXECUTED
- Input: in `backend/app/detectors/primitives/obligation_gap.py`,
  `origin_label` → `"thing"`, `period_label` → `"when"`,
  `amount_label` → `"how much"` (the exact mutation that left the tree green at
  `1b1b56e`)
- Expected: FAIL — the words are now pinned to a second copy in the test file
- Actual: **FAIL.**
  `test_each_kind_labels_its_own_fields_in_its_own_words[scheduled_reversal]`,
  `AssertionError: ('scheduled_reversal', 'origin_label', 'thing')` /
  `assert 'thing' == 'original journal'` at `test_obligation_gap.py:314`.
  `1 failed, 25 passed`
- Result: PASS (the mutation is caught)
- Evidence: the mutation is applied to the source mapping the evaluator reads;
  the comparison target is `EXPECTED_KIND_WORDS`, which the mutation does not
  touch. That is the whole point of the fix

### Scenario: B-M1b — reword `summary`, the field that was never asserted at all
- Status: EXECUTED
- Input: `summary` for `scheduled_reversal` →
  `"something happened"`
- Expected: FAIL — `summary` is one of the five worded fields now covered
  (it was outside the four asserted before pass 19 as well)
- Actual: **FAIL**, same node id, `+ something happened` against the expected
  sentence. `1 failed, 25 passed`
- Result: PASS
- Evidence: this field carried no assertion in any earlier revision; the fix
  widened coverage rather than merely relocating it

### Scenario: B-M2 — add a fourth kind to `KIND_VOCABULARY`
- Status: EXECUTED
- Input: a fourth entry `accrual_release` added to the source mapping, complete
  and internally consistent (`unreleased_accrual`, its own summary and three
  labels) — i.e. the *benign* form of the change, which is what makes it the
  right probe
- Expected: FAIL at the key-set scenario, so a new kind cannot arrive comparing
  its labels to themselves
- Actual: **3 failed, 25 passed** —
  `test_every_kind_the_build_holds_has_its_words_written_out_in_this_file`
  (`AssertionError` at `:297`, the key-set comparison),
  `test_each_kind_labels_its_own_fields_in_its_own_words[accrual_release]`
  (`KeyError: 'accrual_release'` at `:311`), and
  `test_the_vocabulary_is_the_three_sub_types_and_has_not_silently_emptied`
- Result: PASS — caught, and caught three times over
- Evidence: the parametrisation still enumerates from the build's own kind list
  (so the new kind arrives with a scenario pointed at it) while comparing
  against the second copy (so that scenario can fail)

---

## Finding A — `AC-F40-16`

### Scenario: A-M1 — blank the three facts on every register entry but the last
- Status: EXECUTED
- Input: in `backend/ges/export_register.py`, `as_dict` returns deep copies with
  `export_decision_id = ""`, `approval_decision_id = ""` and
  `revalidation["outcome"] = ""` on `rows[:-1]` — exactly the failure the
  criterion's "every produced file" exists to catch, and exactly what the
  one-row register made unreachable
- Expected: FAIL, **and fail on the full tree**, not only in the targeted file
- Actual: targeted — **`1 failed, 22 passed`**; full tree — **`1 failed, 2987
  passed in 219.72s`**.
  `test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts`,
  `AssertionError: {'approval_decision_id': '', …, 'export_decision_id': '', …}`
  at `test_f40_criteria.py:909`
- Result: PASS
- Evidence: at `1b1b56e` this same mutation could not fail, because the register
  held one row and `for entry in entries` and `entries[-1]` were the same
  assertion

### Scenario: A-M2 — make re-export idempotent, keyed on `content_hash`
- Status: EXECUTED
- Input: `ExportRegister.register` returns the existing row when an entry with
  the same `content_hash` is already registered
- Expected: **no change** — each export legitimately produces a distinct file
  with a distinct content hash, so the population stays at three real files and
  the scenario should still pass
- Actual: **`1 passed`** — population unaffected
- Result: PASS (recorded as a negative control: the guard is not firing on
  something it should not fire on)
- Evidence: reported here rather than dropped, because a guard that fires on
  everything is as uninformative as one that fires on nothing

### Scenario: A-M3 — make re-export idempotent per proposal (the real shape of the change the guard is for)
- Status: EXECUTED
- Input: `ExportRegister.register` returns the existing row when an entry with
  the same `proposal_id` is already registered — a second export of the same
  proposal reuses the file rather than producing a new one
- Expected: FAIL **at the population assertion**, not by passing over one row
- Actual: **FAIL at `assert register["count"] >= 3`** —
  `AssertionError: 1` / `assert 1 >= 3`, `test_f40_criteria.py:904`
- Result: PASS — the guard-first ordering does exactly what its comment claims:
  the scenario stops rather than quietly reverting to quantifying over one row
- Evidence: the failure is on line 904 (the population guard), before line 909
  (the per-entry loop) is reached

---

## Finding F3 — the docstring

### Scenario: the F3 shape scenario's docstring now states that it FAILS when findings become ledger-recorded
- Status: EXECUTED (read at `c428fe5`, and matched against the F3-M2 mutation
  result recorded earlier this gate)
- Input: `tests/suites/functional/test_unclaimed_criteria.py`,
  `test_the_broker_answers_the_population_question_UNKNOWN_and_not_none`
- Expected: the prose matches the assertions — the scenario does **not**
  survive the day the answer becomes computable
- Actual: the docstring now reads *"It does NOT survive findings becoming
  ledger-recorded, and the earlier wording here claimed it did. On that day
  `computable` becomes True and `untraversed` loses its findings entry, and
  this scenario fails — as does its sibling below, deliberately."*
- Result: PASS — matches F3-M2, which showed the scenario asserts
  `computable is False` and pins `untraversed` to the findings entry
- Evidence: `c428fe5`, `+10 −2` lines, docstring only; no assertion changed, so
  the mutation result recorded against the old text still holds against the new
