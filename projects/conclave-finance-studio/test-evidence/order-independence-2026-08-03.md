# Test evidence — order independence

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 20, final confirmation
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`c428fe5`** · parent repo @ **`67d0517`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Method

A collection-order plugin written by `test-agent` and held **outside the tree
under test** (`scratchpad/salt_plugin.py`, loaded by `PYTHONPATH` and
`-p salt_plugin`), so the build cannot influence the order it is shuffled into.
It reorders `items` in `pytest_collection_modifyitems` according to `TA_ORDER`:
`canonical`, `file`, `reverse`, and `salt<N>` (a seeded `random.shuffle`).

Six whole-tree runs. **No `-k`, no deselection, no `-x`** — every run collects
and executes all 2,988.

## Result

| Order | Result | Wall |
|---|---|---|
| canonical | **2988 passed** | 218.37s |
| `file` | **2988 passed** | 221.04s |
| `reverse` | **2988 passed** | 224.44s |
| `salt8003` | **2988 passed** | 264.89s |
| `salt29` | **2988 passed** | 262.26s |
| `salt777` | **2988 passed** | 263.55s |

**Six for six, 2,988 every time, exit 0 every time.** No scenario depends on
another having run first, and no scenario is order-sensitive through the
process-scoped state (`process_state.guarded_modules()`) or the shared broker
ledger.

---

### Scenario: canonical order
- Status: EXECUTED
- Input: `pytest -o addopts= -q -p no:cacheprovider`
- Expected: 2,988 pass
- Actual: **2988 passed in 218.37s**, exit 0
- Result: PASS
- Evidence: pytest summary line

### Scenario: grouped by file
- Status: EXECUTED
- Input: `TA_ORDER=file`, items sorted by the file part of the node id
- Expected: 2,988 pass
- Actual: **2988 passed in 221.04s**
- Result: PASS
- Evidence: `order.log`

### Scenario: reversed
- Status: EXECUTED
- Input: `TA_ORDER=reverse`, `items.reverse()`
- Expected: 2,988 pass
- Actual: **2988 passed in 224.44s**
- Result: PASS
- Evidence: `order.log`

### Scenario: salted shuffle, seed 8003
- Status: EXECUTED
- Input: `TA_ORDER=salt8003`, `random.Random(8003).shuffle(items)`
- Expected: 2,988 pass
- Actual: **2988 passed in 264.89s**
- Result: PASS
- Evidence: `order.log`

### Scenario: salted shuffle, seed 29
- Status: EXECUTED
- Input: `TA_ORDER=salt29`
- Expected: 2,988 pass
- Actual: **2988 passed in 262.26s**
- Result: PASS
- Evidence: `order.log`

### Scenario: salted shuffle, seed 777
- Status: EXECUTED
- Input: `TA_ORDER=salt777`
- Expected: 2,988 pass
- Actual: **2988 passed in 263.55s**
- Result: PASS
- Evidence: `order.log`

### Scenario: the shuffled runs collected the same population as the canonical run
- Status: EXECUTED
- Input: the progress-character count of every run
- Expected: 2,988 in every order — a shuffle that silently dropped scenarios
  would show as a smaller total, not as a failure
- Actual: **2,988 in all six**
- Result: PASS
- Evidence: each run's own summary line

### Scenario: the plugin is not something the build can influence
- Status: EXECUTED
- Input: `salt_plugin.py` lives in the agent's scratchpad, is loaded by
  `PYTHONPATH` + `-p`, and is not importable from, referenced by, or committed
  to `dev/`
- Expected: the ordering authority sits outside the tree under test
- Actual: confirmed — `dev` working tree stayed clean (`git status --porcelain`
  empty) across all six runs
- Result: PASS
- Evidence: `git status --porcelain` empty at `c428fe5` after the runs
