# Test evidence — order independence

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Orderings: 6 whole-tree runs — 6 × 2,977 passed, exit 0 each**

## The plugin is mine, and it is salted

`tagent18_shuffle.py`, written for this pass, lives outside the project tree
and is loaded with `-p`. The shuffle is seeded from
`sha256("tagent18-9f3c1a7e-salt:" + seed)`.

**Why salted:** a suite could in principle be written to recognise a known
plugin or a known seed. `grep -rl "tagent18" dev` and `grep -rl "9f3c1a7e" dev`
both return **nothing**, so the token appears nowhere the build can see. The
project's own ordering machinery was not used.

Each run dumped its realised order; **all five dumps have distinct MD5s** and
all differ from the canonical collection order, so no two runs exercised the
same sequence.

---

### Scenario: canonical order
- Status: EXECUTED · Input: `pytest` with no reordering
- Expected: 2,977 pass · Actual: **2,977 passed**, exit 0
- Result: PASS · Evidence: MD5 of collected order `5acfc2cb…`

### Scenario: whole-tree REVERSE
- Status: EXECUTED · Input: `TAGENT18_SEED=reverse`
- Expected: 2,977 pass · Actual: **2,977 passed in 219.02s**, exit 0
- Result: PASS · Evidence: order MD5 `14e865b5…`
- Note: reverse is the ordering that found the `_surface()` clean-close
  dependence in the previous pass, which `code-agent` fixed with
  `U.fresh_state()` at the top of the orphan sweep's surface builder. It is
  clean now.

### Scenario: salted shuffle, seed 1
- Status: EXECUTED · Actual: **2,977 passed in 270.20s**, exit 0
- Result: PASS · Evidence: order MD5 `980a9177…`

### Scenario: salted shuffle, seed 7
- Status: EXECUTED · Actual: **2,977 passed in 264.71s**, exit 0
- Result: PASS · Evidence: order MD5 `6d50a1ef…`

### Scenario: salted shuffle, seed 42
- Status: EXECUTED · Actual: **2,977 passed in 259.40s**, exit 0
- Result: PASS · Evidence: order MD5 `f1409e2c…`

### Scenario: salted shuffle, seed 20260803
- Status: EXECUTED · Actual: **2,977 passed in 259.08s**, exit 0
- Result: PASS · Evidence: order MD5 `10dafbf2…`

### Scenario: every ordering collected exactly the same 2,977 scenarios
- Status: EXECUTED
- Input: the five dumped orders plus the canonical one
- Expected: 2,977 lines each, same set, different sequence
- Actual: **2,977 lines in every dump; six distinct MD5s**
- Result: PASS
- Evidence: a shuffle that silently dropped scenarios would show as a shorter
  dump, and none did

### Scenario: the live decision ledger is untouched by any ordering
- Status: EXECUTED
- Input: `dev/var/broker_db.sqlite3` before and after each whole-tree run
- Expected: byte-identical
- Actual: **byte-identical after all six.** `live_ledger_guard`'s
  `assert_nothing_was_refused` raised in none of them
- Result: PASS
