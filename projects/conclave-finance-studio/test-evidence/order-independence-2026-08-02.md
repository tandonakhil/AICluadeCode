# Test evidence — collection-order independence

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`9d605b1`** · parent repo @ **`e14c497`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `.venv/bin/python -m pytest -p ta_shuffle` over the whole tree
**Exit code:** 0 in every ordering
**Orderings: 9 whole-tree runs — 2,774 PASS, 0 FAIL, 0 SKIP in every one**

The plugin is **`test-agent`'s own**, lives **outside the repository**
(`$SCRATCH/ta_shuffle.py`, reached via `PYTHONPATH`), and is a **different
generator** from `code-agent`'s round-robin: a uniform global Fisher–Yates over
all 2,774 collected items with no per-file bucketing. Measured proof they
differ: a strict round-robin can never place two same-file items adjacently,
and this agent's `seed:1` order contains **35** such adjacencies. The realised
order was written to disk and fingerprinted for every run, so the permutation
used is evidence rather than a claim. The tree stayed clean at `9d605b1`
throughout.

---

### Scenario: all eight orderings plus the control
- Status: EXECUTED
- Input: file order, four seeds, and `reverse` **four separate times**
- Expected: 2,774 pass in every one
- Actual: 2,774 pass, exit 0, in every one

| Ordering | Result | Wall | Order fingerprint | same-file adjacencies |
|---|---|---|---|---|
| file order (control) | 2,774 pass, exit 0 | 177.3s | — | — |
| `seed:1` | 2,774 pass, exit 0 | 207.4s | `e97b948ae4f33286` | 35 |
| `seed:7` | 2,774 pass, exit 0 | 204.5s | `c4621632e4f34fcc` | 36 |
| `seed:42` | 2,774 pass, exit 0 | 205.2s | `1704c448fb4807d1` | 30 |
| `seed:20260802` | 2,774 pass, exit 0 | 205.7s | `3f5306a7168b7395` | 30 |
| `reverse` #1 | 2,774 pass, exit 0 | 175.8s | `d0ee639c287714bd` | 2670 |
| `reverse` #2 | 2,774 pass, exit 0 | 174.8s | `d0ee639c287714bd` | 2670 |
| `reverse` #3 | 2,774 pass, exit 0 | 172.5s | `d0ee639c287714bd` | 2670 |
| `reverse` #4 | 2,774 pass, exit 0 | 174.1s | `d0ee639c287714bd` | 2670 |

- Result: PASS
- Evidence: identical fingerprint `d0ee639c287714bd` across all four `reverse`
  runs, so these are the *same permutation* four times — which is what the
  previous pass's intermittent failure required in order to be ruled out

### Scenario: `reverse` re-run more than once — the intermittent failure is gone
- Status: EXECUTED
- Input: the ordering in which
  `functional/test_f12_probe_criteria.py::test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`
  failed at `75f5e27`, run four times
- Expected: no failure in any of the four
- Actual: 0 failures in 4 runs of the exact same permutation
- Result: PASS
- Evidence: the previous failure was a rendered wall-clock timestamp colliding
  with the substring `"0.02"`, at roughly 1 render in 1,000. The assertion no
  longer reads substrings, so the collision cannot recur — this is a *causal*
  fix rather than four lucky runs, and the causal claim is separately proved in
  `functional-2026-08-02.md`.

### Scenario: the four `reverse` runs are not cheaper than the shuffles by accident
- Status: EXECUTED
- Input: wall times across the nine runs
- Expected: `reverse` preserves file locality (2,670 same-file adjacencies) and
  so rebuilds fewer higher-scoped fixtures than a uniform shuffle
- Actual: `reverse` 172–176s; uniform shuffles 204–207s; file order 177s
- Result: PASS (reported, not a pass/fail condition)
- Evidence: the ~17% spread is fixture rebuilding, not a hang; nothing timed out

### Scenario: the ordering that found the guard defect still finds it
- Status: EXECUTED
- Input: MUTATION M3 (the refcount removed) run at `seed:1`
- Expected: the shuffle that originally exposed the two-patch defect exposes it
  again
- Actual: `6 failed, 2768 passed` at `seed:1`, versus `3 failed, 2771 passed` in
  file order
- Result: PASS (the mutation was reverted)
- Evidence: the shuffle is strictly more sensitive here — it interleaves the two
  trees, which is the condition the defect needs. Note the improvement: the two
  pinning scenarios now catch it in file order too, whereas the original defect
  was invisible there.

### Scenario: nothing was left behind by any ordering
- Status: EXECUTED
- Input: `git status --porcelain` and the live-ledger size after every run
- Expected: clean tree, 0-byte ledger delta
- Actual: clean after all nine; `var/broker_db.sqlite3` unchanged at 10,371,072
  bytes with an unchanged mtime
- Result: PASS
- Evidence: `HEAD=9d605b1`, no untracked or modified files at any point
