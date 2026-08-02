# Test evidence — collection-order independence (whole tree, six orderings)

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 2)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`75f5e27`** · parent repo @ **`21af9da`**
**Owner:** `test-agent` (authored and executed)
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ORDER=<spec> .venv/bin/python -m pytest -p orderplugin`
**Scenarios: 6 orderings — PASS 5, FAIL 1**

> **Headline: five of six orderings are 2,736/2,736 green. The sixth
> (`reverse`) failed one scenario — and it is NOT an order dependence.** Proved:
> the identical permutation re-run passed 2,736/2,736. It is a latent
> **intermittent** assertion in the functional suite that can fail under *any*
> ordering, including file order, and that this pass happened to draw. Reported
> as a FAIL, not rounded up.

---

## The six orderings

| Ordering | Result | Exit | Scenarios | Order fingerprint | Same-file adjacencies | Items off file position |
|---|---|---|---|---|---|---|
| file order (control) | **2,736 pass** | 0 | 2,736 | `e97caa94aca483b9` | 2,634 | 0 |
| `seed:1` | **2,736 pass** | 0 | 2,736 | `8572b681d7cd5743` | 37 | 2,736 |
| `seed:7` | **2,736 pass** | 0 | 2,736 | `c100caa5cb0cf5d0` | 37 | 2,736 |
| `seed:42` | **2,736 pass** | 0 | 2,736 | `b0fb50e4f73141b9` | 27 | 2,733 |
| `seed:20260731` | **2,736 pass** | 0 | 2,736 | `d4791a479a9da2a5` | 38 | 2,735 |
| `reverse` | **2,735 pass, 1 FAIL** | 1 | 2,736 | `67a2c580ba09549a` | 2,634 | 2,736 |
| `reverse` (re-run, same permutation) | **2,736 pass** | 0 | 2,736 | `67a2c580ba09549a` | 2,634 | 2,736 |

The plugin is **this agent's own**, not `code-agent`'s: a uniform global
Fisher–Yates over the flat list of all 2,736 collected items, with no bucketing
by file. The adjacency column is the measured proof the permutations are real
and different — file order keeps 2,634 same-file neighbours, the shuffles keep
27–38. The fingerprint is the SHA-256 (first 16 hex) of the realised order, so
the permutation used is evidence rather than a claim, and each is reproducible
from the seed against the collected set.

The plugin lives **outside the repository** and is copied in for the run and
removed after; `git status --short` was empty before and after. The tree stayed
at `75f5e27` throughout.

**Runtime: budgeted, not a hang.** Whole-tree wall time in file order was
`2:58.66` (128s user, 31s system). The shuffled orderings force far more
higher-scoped fixture rebuilding and are the reason the per-scenario reset cost
dominates.

---

### Scenario: the whole tree passes in file order
- Status: EXECUTED
- Input: `CONCLAVE_ORDER=file`
- Expected: 2,736 pass, exit 0
- Actual: **2,736 pass**, exit 0
- Result: PASS
- Evidence: `Counter({'.': 2736})`, `file EXIT=0`

### Scenario: the whole tree passes under four independent shuffles
- Status: EXECUTED
- Input: `CONCLAVE_ORDER=seed:1`, `seed:7`, `seed:42`, `seed:20260731`
- Expected: 2,736 pass in each
- Actual: **2,736 pass in all four**, exit 0 each
- Result: PASS
- Evidence: `Counter({'.': 2736})` × 4; fingerprints and adjacency counts above.
  At `55878c9` the same tree gave four different failure sets under four seeds;
  it now gives none.

### Scenario: the whole tree passes reversed
- Status: EXECUTED
- Input: `CONCLAVE_ORDER=reverse`
- Expected: 2,736 pass, exit 0
- Actual: **2,735 pass, 1 FAIL**, exit 1
- Result: **FAIL**
- Evidence: `Counter({'.': 2735, 'F': 1})`;
  `FAILED tests/suites/functional/test_f12_probe_criteria.py::test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`

---

## The one failure, diagnosed

```
    def test_AC_F12_15_the_rendered_dom_carries_no_probe_rate(close):
        ...
        for path in ("/review", "/monitors"):
            body = CLIENT.get(path).text.lower()
            assert "probe rate" not in body
>           assert str(low) not in body and str(high) not in body
E           assert ('0.02' not in '<!doctype h...body></html>'
E             '0.02' is contained here:
E               02t07:04:40.023468+00:00)</td></tr></table><div class="note">the budget
E               is not enforced invisibly. a queue that reached its cap held items back,
E               and who raised a cap is named beside it (ac-f41-19).</div></div></main>
```

**What actually failed.** `DISCLOSED_BAND` is
`(Decimal("0.02"), Decimal("0.08"))`, and the scenario asserts the bare
substring `"0.02"` does not appear anywhere in the page. It appeared inside a
**wall-clock timestamp** rendered in the `AC-F41-19` routing-budget table's
"Cap raised by" cell — `…T07:04:40.023468+00:00`, whose `40.023468` contains
the four characters `0.02`.

- The other two assertions in the same scenario — `"probe rate" not in body`,
  and no percentage within 240 characters of the word "probe" — **passed**.
- So no probe rate leaked into the DOM. The product claim `AC-F12-15` makes is
  not contradicted by this run.

**It is not an order dependence — proved by re-running the same permutation.**
`CONCLAVE_ORDER=reverse` was run again, identical plugin, identical
fingerprint `67a2c580ba09549a`, identical 2,736 items in identical positions:

```
reverse rerun EXIT=0        Counter({'.': 2736})
```

**2,736 pass, exit 0.** The same order gave the opposite result, which is what
an order dependence cannot do. The colliding value is a timestamp of the moment
the run rendered, not state left behind by an earlier scenario; reverse order
simply shifted *when* the page was rendered.

- Deterministic demonstration: `'0.02' in '02t07:04:40.023468+00:00'` → `True`;
  the colliding slice is `04:40.023468`.
- The collision needs a whole-second value ending in `0` and a microsecond
  field beginning `02` — on the order of **1 in 1,000 per rendered timestamp**,
  which is why it has not been seen before and why it can recur in **any**
  ordering, file order included.
- Re-run in isolation **12 times**: `failures in 12 isolated runs: 0`. A run
  that reproduced on demand would have been an order dependence; one that does
  not, and whose failing value is a clock reading, is an intermittent
  assertion.

**Classification: a defect in the scenario, not in the product.** A substring
test for `"0.02"` over a whole rendered page will match any decimal number
whose text happens to contain those characters. `test-agent` does not fix it —
this is feedback for `code-agent`. The narrow fix is to assert the band value
is absent **as a number**, or absent from the probe-adjacent windows the same
scenario already computes, rather than anywhere in the document.

**Gate consequence.** `functional` is a **blocking** suite under this project's
Test Policy (all suites blocking, no advisory exception). One of its scenarios
failed in one of six orderings. That is an unmet gate condition and the gate
stops for human decision. It is reported at full weight here rather than
averaged into "5 of 6 green".

---

## Ledger growth per ordering (the standing finding)

| Ordering | `dev/var/broker_db.sqlite3` growth |
|---|---|
| file | +36,864 bytes |
| `seed:1` | +32,768 |
| `seed:7` | +32,768 |
| `seed:42` | +32,768 |
| `seed:20260731` | +36,864 |
| `reverse` | +32,768 |

Every whole-tree run still grows the developer's live decision ledger, because
`backend/tests/conftest.py`'s `ges_app`/`ges_stack` fixtures build their GES
application with no `broker_factory`. The six **suite** entry points each grow
it by **0**, which is the fix landed at `4e5ee47` working. Full diagnosis in
`unit-integration-2026-08-02.md`.

---

## Test-count delta

| | Before (`fc197a6`) | After (`75f5e27`) | Delta |
|---|---|---|---|
| orderings run | 6 | **6** | — |
| scenarios per ordering | 2,692 | **2,736** | **+44** |

Same six orderings as the previous pass, same plugin, same seeds — so the
comparison is like-for-like and the one new failure is not an artefact of a
changed method.
