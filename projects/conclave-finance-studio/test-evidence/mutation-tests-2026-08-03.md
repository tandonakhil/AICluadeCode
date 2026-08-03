# Test evidence — mutation tests (brief items 3, 4, 8)

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

Every mutation was applied to a working tree at `6bf8ed9`, run, and reverted;
`git status --porcelain` returned **0 modified files** after each revert and the
affected file's scenarios were re-run green before the next mutation.

---

### Scenario: M1 — break one edge's TARGET, mid-chain
- Status: EXECUTED
- Input: `components.py`, edge **E5** (run → agent): `graph.agent_href(principal_id)`
  → `graph.agent_href(principal_id + "-mutated")`
- Expected: the chain fails **where it breaks**, not somewhere downstream; the
  per-edge scenario for E5 fails; E1–E4 and E6–E8 still pass
- Actual: **2 failed, 33 passed.** The two are
  `test_the_edge_is_rendered_as_a_followable_link_on_its_source_screen[E5]` and
  `test_the_evidential_chain_walks_finding_to_run_to_agent_to_readiness`, and
  the chain scenario fails at line 130 — **the agent hop** — not at the
  readiness hop after it
- Result: PASS
- Evidence: `AssertionError: /evidence/agent/agent.crossperiod-surveillance-mutated
  returned 404` raised from `U.fetch(agent_href)` at
  `test_ui_object_graph.py:130`, with the run hop's assertion
  (`run-h1 == RUN-2026-06-0412`) already passed above it. The chain really does
  walk using the href the previous screen rendered — a chain that hard-coded its
  URLs would have failed at the readiness hop or not at all.

### Scenario: M2 — delete an edge ROW from the declared table
- Status: EXECUTED
- Input: the `E8` `Edge(...)` row removed from `graph.EDGES` (the dossier's way
  back to the finding)
- Expected: the guard `test_exactly_the_eight_declared_edges_exist` fails —
  "deleting the anchor leaves the row and the row's test fails; deleting the
  anchor AND the row fails the guard"
- Actual: **12 failed, 23 passed**, and the guard is among them
- Result: PASS
- Evidence: `FAILED test_exactly_the_eight_declared_edges_exist`, plus
  `…[E8]` and `test_the_dossier_returns_to_the_finding_it_evidences`. The eight
  `test_the_source_screen_of_every_edge_is_itself_reachable…` failures are
  collateral — the dossier page raises when the row is absent, so the traversal
  cannot complete. The table is genuinely load-bearing: the renderer builds from
  it and the tests assert against it, and it cannot be shrunk quietly.

### Scenario: M3 — can an alias be added from a TEST? (brief item 4)
- Status: EXECUTED
- Input: three probes. (a) search the tree for a test-side alias constant to
  widen. (b) add `routes.SCREEN_ALIASES["/not-a-screen"] = "/queue"` from a test
  and replay the guard. (c) mutate `routes.SCREEN_ALIASES["/exceptions"] = "/ask"`
  and check whether the router consults the mutated table. Then the realistic
  abuse: (d) de-link `/refusals` from the navigation so it is genuinely
  served-but-unreachable, and add `routes.SCREEN_ALIASES["/refusals"] = "/queue"`
  at import time from a test module collected before `test_ui_boundaries.py`.
- Expected: an alias cannot be introduced from a test
- Actual, in four parts:
  - (a) **CONFIRMED** — there is no test-side alias constant anywhere. The only
    alias table in the tree is `app/ui/routes.py:81`; tests only read it.
  - (b) **CAUGHT** — a bogus alias returns non-200, so
    `test_every_alias_serves_a_screen_that_is_itself_reachable` fails on it.
  - (c) **INERT** — the router does **not** consult `SCREEN_ALIASES` at request
    time. After mutating `/exceptions → /ask`, `/exceptions` still served the
    queue. The table is a declaration the tests read, not a routing input.
  - (d) **NOT CAUGHT — this is a finding.** With `/refusals` de-linked, the
    sweep correctly failed with `AssertionError: {'/refusals'}`. Adding **one
    line** to a test file made all 8 scenarios pass: the forged row satisfies
    both guards, because `/refusals` still serves 200 and the canonical
    `/queue` is reachable. Nothing checks that an alias's target is the screen
    it actually serves, except for the three hard-coded queue addresses.
- Result: **FAIL on (d)** — reported, not fixed
- Evidence: `1 failed, 6 passed` with the orphan exposed; `8 passed` with the
  test-added alias row present. **Nothing in the build does this today** — the
  grep shows only reads — so no suite currently reports a false pass on this
  path. It is a robustness gap in the mechanism, not a live defect. For
  `code-agent`.

### Scenario: M4 — the gold colour law (brief item 2b context)
- Status: EXECUTED
- Input: `chrome.py`, `.thread{stroke:var(--accent)}` → `.thread{stroke:var(--gold)}`
  — the exact law `site.css` states verbatim: "GOLD IS USED ONLY FOR THE
  PULL-LINE + ITS TERMINUS DOT, never the core, never the threads"
- Expected: the set-equality scenario and the explicit law scenario both fail
- Actual: **3 failed, 38 passed** —
  `test_only_the_approval_selectors_reference_the_gold_token`,
  `test_the_gold_bearing_classes_are_the_approval_ones_and_the_mark`,
  `test_the_mark_never_puts_gold_on_its_core_or_its_threads`
- Result: PASS
- Evidence: the widening from three selectors to five is not a weakening — the
  assertion is set **equality**, so a sixth gold selector fails, and the
  negative half of the law is separately enforced

### Scenario: M5 — is the independent ordering generator actually independent?
- Status: EXECUTED
- Input: an out-of-tree plugin doing an unsalted `random.Random(seed)` +
  Fisher–Yates, the obvious implementation
- Expected: permutations different from `code-agent`'s, since an independent
  check that reproduces the original permutation is the same run twice
- Actual: **identical.** `seed:1` produced fingerprint `759308beb6c37d78` with
  **38** same-file adjacencies — byte-for-byte the row `code-agent` recorded in
  `PROJECT_CONTEXT.md`.
- Result: this is **two findings at once**
  1. It **corroborates** `code-agent`'s recorded fingerprints: the permutation
     in that table is really the permutation that was used.
  2. The generator was **not independent**, so the matrix was discarded and
     re-run with a salted RNG walking the array from the other end. Salted
     `seed:1` gives `9595c2e4e0f72c1c` / 28 adjacencies.
- Evidence: `scratchpad/order-corroboration-seed1.report` holds the unsalted
  fingerprint; `order-independence-2026-08-03.md` holds the salted matrix

### Scenario: M6 — this agent's own driver defects, recorded rather than quietly corrected
- Status: EXECUTED
- Input: two of this pass's own driver bugs, found by their results being wrong
- Expected: a failure caused by the harness is reported as the harness's, not
  the build's
- Actual: **two, both this agent's**
  1. **Smoke S7 reported two links on the dossier where there is one anchor.**
     The driver's `href="([^"]+)"` also matched `data-href="…"` on the same
     anchor. Verified against `Document.hrefs()` (which returns `['/review/
     ITEM-21400-CP']`) and against the raw tag. Driver fixed with a
     word-boundary lookbehind; the whole smoke re-run.
  2. **Rendered R7 passed on an empty set.** The gold detector used a guessed
     colour range requiring `r > 140`; light `--gold` is `#8A5A17`, `r = 138`,
     so it matched nothing and the scenario reported PASS having measured
     nothing — a vacuous pass in this agent's own suite. Rewritten to resolve
     the document's own `--gold` token through the engine and to carry a
     **non-vacuity guard** (the approval screen must actually paint gold, or the
     scenario fails). Re-run: 28 gold elements, all lawful.
- Result: both fixed inside the pass, both recorded
- Evidence: the same class as the previous pass's `<option>`-vs-radio defect —
  a guessed field tests the guess
