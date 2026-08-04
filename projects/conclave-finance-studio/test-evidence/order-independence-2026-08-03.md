# Test evidence — order independence, on test-agent's own salted plugin

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The plugin

`scratchpad/p19/ta19_order.py` — **outside the repository**, loaded by
`PYTHONPATH` + `-p ta19_order`, so `dev/` stayed clean at `e00a214` throughout.
Uniform global Fisher–Yates over the whole collected list, seeded from a salt
string:

```
SALT = "test-agent/verify/quartzite-heronwing-8021/2026-08-03"
```

### Scenario: the salt appears nowhere in the project tree
- Status: EXECUTED
- Input: `grep -rl` for `quartzite`, `heronwing`, `CONCLAVE_TA_ORDER`, `ta19_order`
  across `dev/` excluding `.git` and `.venv`
- Expected: zero files
- Actual: **0, 0, 0, 0**
- Result: PASS — no suite can recognise this permutation

This is deliberately **not** `code-agent`'s plugin
(`SALT = "code-agent/gate7-pass18/2026-08-03"`); the fingerprints below differ
from the ones in `PROJECT_CONTEXT.md`'s pass-19 table, which is the point.

## Runs

| Ordering | Result | Exit | Wall | Same-file adjacencies | Order fingerprint |
|---|---|---|---|---|---|
| `file` (control) | 2,987 pass | 0 | 222s | 2,877 | `f129ce908bd65249` |
| `reverse` | 2,987 pass | 0 | 227s | 2,877 | `f9f81e5692a07192` |
| `seed:31337` | 2,987 pass | 0 | 272s | 32 | `ba284ef0f64de489` |
| `seed:8021` | 2,987 pass | 0 | 267s | 31 | `0e09478c9f1f3238` |
| `seed:20260803` | 2,987 pass | 0 | 268s | 45 | `8c56d03e1e8c766e` |

Plus a sixth whole-tree run in canonical order without the plugin (2,987 pass,
exit 0), and a seventh under the S1b mutation (2,987 pass — that one is a
finding, see `sampling-sweep-2026-08-03.md`).

The three shuffles drop same-file adjacency from 2,877 to 31–45, so the
permutation genuinely interleaves files rather than reordering within them.

---

### Scenario: every ordering collects the same 2,987 node ids
- Status: EXECUTED
- Input: the plugin dumps its realised order to a file each run; `sort | md5`
- Expected: identical digests, so no ordering silently dropped a scenario
- Actual: **`15e22b1aa8387286c0783d7c90219d72` for all five, and identical to the
  canonical `--collect-only` dump**
- Result: PASS

### Scenario: the fingerprints are genuinely distinct sequences
- Status: EXECUTED
- Expected: five different digests
- Actual: **five distinct**; `file` and `reverse` share an adjacency count (as
  they must — reversal preserves file grouping) but differ in fingerprint
- Result: PASS

### Scenario: the live ledger is byte-identical after every ordering
- Status: EXECUTED
- Input: md5 of `dev/var/broker_db.sqlite3` before the first run and after each
- Expected: unchanged
- Actual: **`449791062f2f1adb8db41a9d5406fb24` before, and after all five**
- Result: PASS
- Evidence: measured in the same shell invocation as each run

### Scenario: the working tree is clean at `e00a214` after the whole pass
- Status: EXECUTED
- Expected: `git status --porcelain` empty, HEAD `e00a214`
- Actual: **empty, `e00a214a8444e5e89118d5f03f7a1b993f56326b`** at the start;
  all mutation work was done in detached worktrees under the scratchpad
- Result: PASS
