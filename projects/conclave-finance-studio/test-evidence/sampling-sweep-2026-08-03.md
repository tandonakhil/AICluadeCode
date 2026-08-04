# Test evidence — sampling sweep (the two gate-8 findings, closed)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The sweep this file records

The sampling sweep looks for scenarios whose **name quantifies** ("each",
"every", "no…anywhere") over a population the scenario does not actually
traverse. Gate 8 raised two findings of this shape. Both are now closed.

**No new finding of this shape was opened this pass.** The sweep was re-run in
its sharpened, instrumented form — see
`vacuous-and-empty-parametrize-sweep-2026-08-03.md`, which measured the real
iteration count of all **397** assert-bearing loops in the tree rather than
reading them.

---

### Scenario: Finding B — the kind vocabulary compared to its own source
- Status: EXECUTED
- Input: `test_each_kind_labels_its_own_fields_in_its_own_words`, at `c428fe5`
- Expected: the words a reviewer reads are pinned to something outside the
  evaluator, and the parametrisation over the build's own kind list is retained
- Actual: **CLOSED.** Expected words in `EXPECTED_KIND_WORDS`, five worded
  fields per kind, key sets asserted equal by a companion scenario. Both
  mutations fail
- Result: PASS
- Evidence: `mutation-tests-2026-08-03.md` B-M1, B-M1b, B-M2

### Scenario: Finding A — `AC-F40-16` quantifying over a one-row register
- Status: EXECUTED
- Input: `test_AC_F40_16_every_produced_file_is_in_the_register_with_its_three_facts`, at `c428fe5`
- Expected: a real, driven population of more than one file, guarded so it
  cannot silently return to one
- Actual: **CLOSED.** Three exports through the real control, `count >= 3` and
  group-id distinctness asserted before the loop. The blanking mutation fails
  full-tree; the idempotency mutation fails at the guard
- Result: PASS
- Evidence: `mutation-tests-2026-08-03.md` A-M1, A-M2, A-M3;
  instrumented count for that loop is now `[3, 3]`

### Scenario: does any other scenario in the tree quantify over a population too small to fail
- Status: EXECUTED
- Input: runtime iteration counts for all 397 assert-bearing loops, over a full
  2,988-scenario run
- Expected: any loop with max 0 or max 1 iterations named and reviewed
- Actual: **1 loop with max 0** (a negative watchdog, reviewed, not a defect —
  its outer population is guarded at `assert len(urls) > 8` and entered 47
  times) and **17 loops with max 1**, all reviewed, all either singular by
  construction or self-guarded. The most exposed of the 17 already carries its
  own population guard: `assert seen >= 7, "expected the readiness screen and
  six dossiers, saw {}"`
- Result: PASS — **no new finding of this shape**
- Evidence: `vacuous-and-empty-parametrize-sweep-2026-08-03.md`; `loops.json`

### Scenario: are the two closures narrower than the criteria they serve
- Status: EXECUTED
- Input: the changed-scenario audit, checking whether closing each finding
  reduced what the scenario asserts
- Expected: coverage held or widened, never narrowed
- Actual: **widened in both cases.** Finding B went from four worded fields to
  five (`summary` was never asserted in any revision). Finding A kept its three
  per-entry assertions byte-identical and added two population guards
- Result: PASS
- Evidence: `changed-scenario-audit-2026-08-03.md`
