# Test evidence — functional suite

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`9d605b1`** · parent repo @ **`e14c497`**
**Owner:** `functional-agent` (authored) · executed and reported by `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `dev/tests/suites/functional/run.sh`
**Exit code:** 0
**Scenarios: 354 — PASS 354, FAIL 0, SKIP 0**
**Under all eight collection orderings: PASS 354 in every one, including four
separate `reverse` runs**

> **The one failure of the previous pass is closed.** At `75f5e27`,
> `test_AC_F12_15_the_rendered_dom_carries_no_probe_rate` failed inside the
> `reverse` ordering on a rendered wall-clock timestamp. `reverse` was re-run
> **four** times at `9d605b1`: 2,774 pass, exit 0, every time.

`test-agent` does not author this suite. It ran it, read its scenario names and
docstrings against the 33-entry deferred-substitution register, and reports the
result.

---

### Scenario: the suite executes end to end
- Status: EXECUTED
- Input: `bash tests/suites/functional/run.sh`
- Expected: exit 0, and specifically not exit 3 (no scenarios) or 4 (cannot execute)
- Actual: 354 collected, `EXECUTED — suite passed`
- Result: PASS
- Evidence: progress tally 354 dots, no `F`/`E`/`s`; exit 0

### Scenario: the previously failing scenario now passes in `reverse`, repeatedly
- Status: EXECUTED
- Input: the whole tree under `TA_ORDER=reverse`, run four separate times
- Expected: no failure, and specifically not an intermittent one
- Actual: `2774 passed` on all four, fingerprint `d0ee639c287714bd` each time
- Result: PASS
- Evidence: 175.82s / 174.79s / 172.46s / 174.11s; see
  `order-independence-2026-08-02.md`

### Scenario: the timestamp that broke the old assertion now passes clean
- Status: EXECUTED
- Input: `rendered_numbers.band_is_not_readable("captured at
  2026-08-02T07:04:40.023468+00:00", (0.02, 0.08))`
- Expected: no leak reported — `0.02` inside `40.023468` is not a standalone
  numeric token
- Actual: no leak reported. The old substring form flags it.
- Result: PASS
- Evidence: `timestamp that broke the old form  new=no leak reported
  old_substring=flag`

### Scenario: `0.020` — the case that PASSED DIRTY — is now caught
- Status: EXECUTED
- Input: `band_is_not_readable("rate: 0.020", band)`
- Expected: leak reported — the same rate, a different substring
- Actual: `AssertionError: a number inside the undisclosed probe band
  ('0.02', '0.08') is rendered at …: ['0.020']`
- Result: PASS
- Evidence: exact decimals rather than floats, so `0.020 == 0.02`; the old
  substring form passes this input

### Scenario: a rate strictly BETWEEN the bounds — what `plan_injection` actually draws — is caught
- Status: EXECUTED
- Input: `band_is_not_readable("rate: 0.0473", band)`; `plan_injection` draws
  `rng.uniform(0.02, 0.08)`, so the bounds are the two values it almost never takes
- Expected: leak reported
- Actual: leak reported. **The old substring form passes it.**
- Result: PASS
- Evidence: `0.0473 -- strictly between … new=LEAK REPORTED
  old_substring=pass` — this is the leak the criterion is about, and it was
  never in the old assertion's reach

### Scenario: MUTATION M2 — a real leak on the real leak path fails all four sites
- Status: EXECUTED
- Input: `BAND_STATEMENT` in `app/f12/probes.py` amended to
  `"…is not readable from this product. (rate in force tonight: 0.0473)"` — the
  realistic shape of the leak, a drawn in-band rate appended to the disclosure
  the product already renders
- Expected: all four `AC-F12-15` numeric sites fail
- Actual: **4 failed** — the unit site, both functional sites, and the
  Playwright-driven UX site (which reads `inner_text` from a real browser)
- Result: PASS (the assertion fired; the mutation was reverted)
- Evidence: `4 failed in 0.75s`. Against the same mutated build the **old**
  assertion was evaluated directly and returned
  `/review OLD assertion … PASSES -- leak undetected` with `"0.0473" in body ==
  True`. Reverted with `git checkout`; tree re-verified clean at `9d605b1`.
  The immediately preceding run of the same four scenarios on the unmutated
  tree gave `4 passed`, so the mutation is the only difference.

### Scenario: measured over all twelve served pages — zero in-band tokens
- Status: EXECUTED
- Input: every one of the twelve paths the scenario sweeps, fetched and
  tokenised
- Expected: `code-agent`'s claim of zero in-band tokens on all twelve
- Actual: **confirmed, zero on all twelve**; 81–98 numeric tokens per page and
  none in `[0.02, 0.08]`. Zero old-form substring hits too, so on this build
  the two forms agree and the timestamp collision was genuinely intermittent.
- Result: PASS
- Evidence: `TOTAL in-band tokens across 12 pages: 0` /
  `TOTAL old-substring hits across 12 pages: 0`; all twelve returned 200

### Scenario: is it genuinely STRONGER, or merely different?
- Status: EXECUTED
- Input: both forms evaluated over eleven crafted inputs and over the twelve
  served pages
- Expected: a measured answer, not an assertion
- Actual: **Stronger on every real-leak shape, and not a strict superset.** The
  new form catches everything the old caught that is actually a readable rate
  (`0.02`, `0.08`), plus `0.020` and every value strictly between the bounds.
  The only inputs the old form flagged and the new one does not are digit runs
  sitting *inside* a longer numeric run (`40.023468`, `1.0.02`) — which are
  precisely the false positives, not readable rates.
- Result: PASS, with two qualifications reported as findings below
- Evidence: the eleven-case table; `0.0473` new=LEAK old=pass;
  `1.0.02` new=pass old=flag

### Scenario: FINDING — the collision class is relocated, not eliminated (non-blocking)
- Status: EXECUTED
- Input: the check reads the **whole served document, including the `<style>`
  block**, where in-band decimals are ordinary. `MUTATION`: one CSS declaration
  rewritten from `letter-spacing:.05em` to `letter-spacing:0.05em` — a change
  with **zero rendered effect**.
- Expected: if the concern were closed, a cosmetic CSS rewrite could not fail
  an `AC-F12-15` scenario
- Actual: **3 scenarios FAILED** — `a number inside the undisclosed probe band
  ('0.02','0.08') is rendered at /: ['0.05']`
- Result: FAIL as a *robustness* observation; **not** a suite failure — nothing
  is failing on the build as it stands, and the tree is green
- Evidence: today all 84 in-band leading-dot values on the served pages are CSS
  (`letter-spacing:.06em`, `.08em`, `.05em`) and pass only because the
  stylesheet happens to be authored in leading-dot form. Feedback for
  `code-agent`, not something `test-agent` applied. Mutation reverted; tree
  clean at `9d605b1`.

### Scenario: FINDING — the docstring again claims more than the assertion checks (non-blocking)
- Status: EXECUTED
- Input: `conclave_harness/rendered_numbers.py` names `.02` among the leaks the
  substring form let through, in the passage justifying the replacement. Tested
  directly.
- Expected: if the docstring is accurate, the new form catches `.02`
- Actual: it does **not** — the lookbehind `(?<![\d.,])` means a leading-dot
  decimal produces no token at all. `rate: .02` → no leak reported.
  `2.0e-2` likewise.
- Result: FAIL as a *documentation-accuracy* observation; **not** a suite failure
- Evidence: `.02 leading-dot form  new=no leak reported  old_substring=pass` —
  neither form catches it, so this is not a regression, but it is the **same
  class of defect as the original**: a comment asserting coverage the
  assertion does not have. No rate is rendered in leading-dot form today (the
  156 such decimals on the served pages are all CSS), so nothing leaks.

### Scenario: register cross-check on this suite's 354 names
- Status: EXECUTED
- Input: all 354 node IDs and every `COVERS` join in the suite
- Expected: none of the five declared criteria claimed
- Actual: zero occurrences of `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
  `AC-F40-17`, `AC-F36-48` in this suite's node IDs or joins
- Result: PASS
- Evidence: see `register-cross-check-2026-08-02.md`
