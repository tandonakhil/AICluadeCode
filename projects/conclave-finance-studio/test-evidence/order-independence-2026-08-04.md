# Test evidence — order independence

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
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
and executes all 3,037.

## Result

| Order | Result | Wall |
|---|---|---|
| canonical | **3037 passed** | 232.60s |
| `file` | **3037 passed** | 235.51s |
| `reverse` | **3037 passed** | 241.47s |
| `salt8003` | **3037 passed** | 279.91s |
| `salt29` | **3037 passed** | 276.38s |
| `salt777` | **3037 passed** | 278.94s |

**Six for six, 3,037 every time, exit 0 every time.** No scenario depends on
another having run first, and no scenario is order-sensitive through the
process-scoped state (`process_state.guarded_modules()`) or the shared broker
ledger.

The three seeds are the same three used at pass 20, so the comparison is
against a like-for-like control; the +49 scenarios added this pass have been
shuffled against the whole tree, not run only in file order.

---

### Scenario: canonical order
- Status: EXECUTED
- Input: `pytest -o addopts= -q -p no:cacheprovider` at `7757e0d`
- Expected: 3,037 pass
- Actual: **`3037 passed in 232.60s`**, exit 0
- Result: PASS

### Scenario: grouped by file
- Status: EXECUTED · Input: `TA_ORDER=file`, items sorted by the file part of the node id · Actual: **`3037 passed in 235.51s`** · Result: PASS

### Scenario: reversed
- Status: EXECUTED · Input: `TA_ORDER=reverse`, `items.reverse()` · Actual: **`3037 passed in 241.47s`** · Result: PASS

### Scenario: salted shuffle, seed 8003
- Status: EXECUTED · Input: `random.Random(8003).shuffle(items)` · Actual: **`3037 passed in 279.91s`** · Result: PASS

### Scenario: salted shuffle, seed 29
- Status: EXECUTED · Input: `random.Random(29).shuffle(items)` · Actual: **`3037 passed in 276.38s`** · Result: PASS

### Scenario: salted shuffle, seed 777
- Status: EXECUTED · Input: `random.Random(777).shuffle(items)` · Actual: **`3037 passed in 278.94s`** · Result: PASS

### Scenario: the plugin is not part of the tree under test
- Status: EXECUTED
- Input: `salt_plugin.py` lives in the agent's scratchpad, loaded by `PYTHONPATH` + `-p`; `git status --porcelain` empty throughout
- Expected: no file inside `dev/` participates in the shuffling
- Actual: **confirmed** — the tree is byte-identical before and after the six runs
- Result: PASS

### Scenario: the shuffled runs collect the same population, not a subset
- Status: EXECUTED
- Input: each run's own summary line
- Expected: 3,037 in every order — a shuffle that collected fewer would pass while testing less
- Actual: **3,037 in all six**
- Result: PASS
