# Test evidence — order independence

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ORDER=<mode> PYTHONPATH=<out-of-tree> .venv/bin/python -m pytest -o addopts= -p no:cacheprovider -p tagent_order -q`
**Exit code:** 0 on every run
**Runs: 8 whole-tree — 1 control + 6 permuted + 1 under the vacuous-pass instrumentation. 2,955 of 2,955 pass in every one.**

The plugin lives **outside the repository**, so the tree stayed clean
(`git status --porcelain` = 0 throughout). It does a **uniform global
Fisher-Yates over the entire collected list** — not round-robin, not per-file —
and fingerprints the realised order so the permutation is evidence rather than a
claim.

## The generator is salted, and the reason is a finding

The obvious implementation — `random.Random(seed)` plus Fisher-Yates — produced
`code-agent`'s **exact** fingerprints: `seed:1` gave `759308beb6c37d78` with 38
same-file adjacencies, identical to the pass-17 table. That is useful
corroboration (the recorded permutation is real) but it is not an independent
check; it is the same run twice. The matrix was discarded and re-run with a
salted RNG (`"test-agent/gate8/2026-08-03"`) walking the array from the other
end, so every seeded permutation below differs from `code-agent`'s.

| Ordering | Result | Exit | Wall | Same-file adjacencies | Order fingerprint | Ledger |
|---|---|---|---|---|---|---|
| file order (control) | 2,955 pass | 0 | 209.4s | 2,846 | — | unchanged |
| `seed:1` (salted) | 2,955 pass | 0 | 243.3s | **28** | `9595c2e4e0f72c1c` | unchanged |
| `seed:7` (salted) | 2,955 pass | 0 | 249.6s | **39** | `d929fa3e6a9f5d91` | unchanged |
| `seed:42` (salted) | 2,955 pass | 0 | 250.2s | **32** | `45a3759ce39c82bb` | unchanged |
| `seed:20260803` (salted) | 2,955 pass | 0 | 247.4s | **34** | `cf3222bf352fa738` | unchanged |
| `reverse` | 2,955 pass | 0 | 215.5s | 2,846 | `fa4584ef39e7c77b` | unchanged |
| `reverse` (2nd time) | 2,955 pass | 0 | 214.9s | 2,846 | `fa4584ef39e7c77b` | unchanged |
| vacuous-pass instrumentation | 2,955 pass | 0 | 209.5s | 2,846 | — | unchanged |

28-39 same-file adjacencies against 2,846 in file order is the signature of a
uniform global shuffle: a round-robin interleave cannot produce it.

---

### Scenario: all 2,955 pass under six independent orderings
- Status: EXECUTED
- Input: the six rows above
- Expected: 2,955 pass, exit 0, in every ordering
- Actual: **2,955 pass, exit 0, in all six**
- Result: PASS
- Evidence: `2955 passed in 243.30s` / `249.61s` / `250.23s` / `247.39s` / `215.49s` / `214.86s`

### Scenario: `reverse` is repeatable, so a green is not an intermittent
- Status: EXECUTED
- Input: `reverse` run twice, fingerprints compared
- Expected: identical fingerprint both times — the same permutation, twice
- Actual: `fa4584ef39e7c77b` **both times**
- Result: PASS
- Evidence: two independent invocations, 215.49s and 214.86s, same fingerprint —
  the permutation is pinned, so the pass is a property of the ordering rather
  than of the run

### Scenario: the developer's decision ledger is untouched in every ordering
- Status: EXECUTED
- Input: md5 of `dev/var/broker_db.sqlite3` captured before and after each run
- Expected: byte-identical every time
- Actual: `ledger_same=yes` on **all six**
- Result: PASS
- Evidence: the live-ledger guard installed by both conftests holds under
  permutation, including under `seed:1` where the previous pass's mutation
  showed a removed refcount produces 6 failures

### Scenario: the permuted collection is the same 2,955 scenarios
- Status: EXECUTED
- Input: `items=` recorded by the plugin on every run
- Expected: 2,955 in each
- Actual: **2,955 in all six**
- Result: PASS
- Evidence: no ordering changed what was collected, only the order
