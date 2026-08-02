# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 2)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`75f5e27`** · parent repo @ **`21af9da`**
**Owner:** `functional-agent` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/functional/run.sh`
**Exit code:** 0 at its own entry point; **1** inside the `reverse` whole-tree ordering
**Scenarios: 354 — PASS 354, FAIL 0, SKIP 0** at the entry point
**Under the six collection orderings: PASS in five, 1 FAIL in `reverse`**

> **This suite carries the one failure of this pass.** It passes its own entry
> point and five of six whole-tree orderings; in `reverse`,
> `test_AC_F12_15_the_rendered_dom_carries_no_probe_rate` failed. See the
> collection-order scenario below and `order-independence-2026-08-02.md` for
> the diagnosis. It is reported as a FAIL and not rounded up.

`test-agent` does not author this suite. It ran it, read its scenario names and
docstrings against the 33-entry deferred-substitution register, and reports the
result.

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/functional/run.sh`
- Expected: exit 0, and specifically not exit 3 (no scenarios) or 4 (cannot execute)
- Actual: `scenarios: 19 file(s)`, 354 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: progress tally `Counter({'.': 354})`, exit 0

### Scenario: the suite passes under every collection order
- Status: EXECUTED
- Input: the suite as collected inside all six whole-tree orderings
- Expected: no scenario depends on what ran before it
- Actual: **green in five of six. In the `reverse` ordering one scenario
  FAILED** —
  `test_f12_probe_criteria.py::test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`
- Result: **FAIL**
- Evidence: `order-independence-2026-08-02.md`. The failure is **not** an order
  dependence and **not** a product defect: the scenario asserts the bare
  substring `"0.02"` (the disclosed band's low bound) appears nowhere in the
  page, and it collided with a rendered wall-clock timestamp
  `…T07:04:40.023468+00:00`. Its two substantive assertions — `"probe rate"`
  absent, and no percentage within 240 characters of the word "probe" — both
  passed, so no probe rate leaked. Re-run in isolation 12 times: 0 failures.
  **The identical `reverse` permutation re-run gave 2,736 pass, exit 0** — the
  same order, the opposite result, which is what an order dependence cannot do.
  It is an **intermittent** assertion that can fail in any ordering, roughly 1
  rendered timestamp in 1,000.
- Gate consequence: this suite is **blocking**. One scenario failing in one of
  six orderings is an unmet gate condition, reported at full weight rather than
  averaged into "five of six green". `test-agent` does not fix it — the narrow
  fix (assert the band value as a number, or only within the probe-adjacent
  windows the scenario already computes) is feedback for `code-agent`.

### Scenario: the suite no longer writes to the developer's decision ledger
- Status: EXECUTED
- Input: `stat` on `dev/var/broker_db.sqlite3` before and after the entry point
- Expected: 0 bytes of growth — this suite was **the** source of the leak I
  reported last pass (`test_emission_gate_criteria.py`, three rows per run)
- Actual: **0**
- Result: PASS
- Evidence: `functional EXIT=0 ledger_delta=0`. Under the fix reverted, the same
  request grew the file by 4,096 bytes — see `architecture-2026-08-02.md`.

### Scenario: no scenario claims a criterion the register denies
- Status: EXECUTED
- Input: all 354 node IDs and every `COVERS` docstring in this suite, scanned
  for the five declared criteria
- Expected: zero claims
- Actual: zero node-name claims. Two `COVERS` docstrings mention `AC-F40-17`
  and both say **"NOT AC-F40-17"** in the same sentence, on scenarios that
  cover `AC-F40-18`.
- Result: PASS
- Evidence: `register-cross-check-2026-08-02.md`

### Scenario: `AC-F40-18` is exercised on the served pilot, not only in the suite
- Status: EXECUTED
- Input: the smoke test's S8 — the export screen the real export path produced
- Expected: `data-authorised-on="synthetic_attestation"`, never a stored CUEC
  pass state
- Actual: `synthetic_attestation`
- Result: PASS
- Evidence: `smoke-test-2026-08-02.md` S6–S8

---

## Test-count delta

| | Before (`fc197a6`) | After (`75f5e27`) | Delta |
|---|---|---|---|
| functional | 354 | **354** | — |

**Added 0, removed 0, changed 0.** Verified by node-ID set difference between
the two commits: no `tests/suites/functional/**` node ID was added or removed,
and `git diff fc197a6..HEAD -- tests/suites/functional` is empty.
