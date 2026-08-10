# Test evidence — unit/integration and per-suite breakdown

**Project:** conclave-finance-studio
**Gate:** 8 · Test — `close-cockpit-home` enhancement close
**Date:** 2026-08-08
**Commit under test:** `dev` @ **`7ecba21`** (parent baseline `b447a11`, gate 11)
**Owner:** `test-agent`
**Blocking:** yes — Test Policy is "all suites blocking, no advisory exceptions"
**Command:** `.venv/bin/python -m pytest` from `dev/`, per suite and whole-tree

## Result — whole tree

**3,192 passed, 0 failed, 0 errors, 0 skipped.**

## Per-suite counts, measured by running each suite alone

| Suite | Owner | Status | Result | Δ vs. `b447a11` |
|---|---|---|---|---|
| unit / integration (`backend/tests`) | `test-agent` | `EXECUTED` | **2,447 / 2,447** | 0 |
| functional | `functional-design-agent` | `EXECUTED` | **399 / 399** | **+34** |
| UX | `ui-ux-designer` | `EXECUTED` | **194 / 194** | 0 |
| red-team | `responsible-ai-architect` | `EXECUTED` | **61 / 61** | 0 |
| security | `security-architect` | `EXECUTED` | **40 / 40** | 0 |
| architecture | `solution-architect` | `EXECUTED` | **28 / 28** | 0 |
| industry | `industry-expert` | `EXECUTED` | **23 / 23** | 0 |
| **whole tree** | — | `EXECUTED` | **3,192 / 3,192** | **+34** |

The seven suite totals sum to 3,192 exactly, so no scenario is counted twice
and none is outside a suite. All growth is in the `functional` suite, which
is where the 22 `AC-COCKPIT-*` and 3 `AC-TYPESIZE-*` criteria this
enhancement built are scenario-owned.

## Test-count delta — measured by node id, not counted

**3,158 -> 3,192: +38 added, -4 removed, net +34.** Measured by collecting
`pytest --collect-only` node ids at `b447a11` (in a scratch clone with the
project's own `.venv` symlinked in for the interpreter, no dependency
installed into it) and at `7ecba21`, sorting both and diffing with `comm`.

### The 4 removals, all named, all superseded by a strictly-equivalent
### successor reflecting the entry-point change this enhancement makes

| Removed | Superseded by |
|---|---|
| `backend/tests/test_ui_ask.py::TestReachability::test_the_entry_point_lands_on_the_queue_and_ask_is_one_link_away` | `...test_the_entry_point_lands_on_the_cockpit_and_ask_is_one_link_away` |
| `backend/tests/test_ui_information_architecture.py::TestTheEntryPointIsTheWorkNotTheQuery::test_the_landing_screen_is_the_queue` | `...test_the_landing_screen_is_the_close_cockpit` |
| `tests/suites/ux/test_ux_journey.py::TestUX13StaffAccountantNight::test_the_entry_point_is_the_queue_and_ask_is_one_click_from_it` | `...test_the_entry_point_is_the_cockpit_and_ask_is_one_click_from_it` |
| `backend/tests/test_ui_brand.py::TestTheBrandLayerChangedNoLayoutRuleItWasNotSupposedTo::test_the_pass_17_layout_rule_is_declared_exactly_once[.navitem]` | not superseded by name — **correctly dropped**: `.navitem` is the removed sidebar's own rule and no longer exists to be declared exactly once. `test_ui_no_orphaned_style_rule.py` and the sidebar-absence checks (see the companion verification note below) are what now cover the space this parametrisation vacated. |

All four are consequences of the entry point changing from the merged queue
to the close cockpit (`AC-COCKPIT-01`) and the sidebar's removal
(`close-cockpit-home` pass 2). None is a coverage reduction: the first three
are renames onto an equivalent claim about the new entry point, and the
fourth's subject (`.navitem`) does not exist in the shipped build for a
declared-once check to hold over.

### The 38 additions, by file

| File | Added |
|---|---|
| `tests/suites/functional/test_close_cockpit_criteria.py` (new) | 35 |
| `backend/tests/test_ui_ask.py` | 1 |
| `backend/tests/test_ui_information_architecture.py` | 1 |
| `tests/suites/ux/test_ux_journey.py` | 1 |

### Changed tests — same node id, changed body

Confirmed by `git diff b447a11 7ecba21 --stat`: seven files change with no
node-id delta in them (their additions/removals net to zero), meaning every
line changed inside them is a same-name body edit. All are widen-or-repoint,
none narrows an assertion:

- `backend/tests/test_ui_approvals.py::TestGoldIsUsedHereAndNowhereElse::*`
  (all methods in the class) — `GOLD_RULES` widened from 5 selectors to 7
  (`a.act.gold`, `a.act.gold .fig` added), because the cockpit's forward-due
  tile is the second of `tokens.py`'s two declared gold bindings and the
  class-level constant every method in the class reads from is what changed.
- `backend/tests/test_ui_boundaries.py::TestEveryScreenIsReachableAndEveryComponentIsMounted::*`
  (mount-coverage test) — now also fetches `?tracker=` demo views so the
  close tracker's four states are in the reachability surface; broadens what
  is checked, narrows nothing.
- `backend/tests/test_ui_chrome.py::TestNavigation::test_a_missing_badge_renders_no_count_rather_than_zero` —
  assertion re-pointed from `"cnt" not in ...` to `"badge" not in ...`,
  because the drawer's badge carrier class changed from the sidebar's `.cnt`
  to `.badge`; same property (absent badge != rendered zero), current markup.
- `backend/tests/test_ui_chrome.py::TestProvenanceAndPilotStrip::test_the_evidential_view_drops_the_shell_but_keeps_the_stylesheet` —
  assertion re-pointed from `'class="nav"' not in markup` (the removed
  sidebar's own marker) to `"<nav" not in markup` and
  `'data-testid="cockpit-topbar"' not in markup` (the current one navigation
  landmark). Same property (shell-off view has no navigation), current markup.
- `backend/tests/test_ui_no_orphaned_style_rule.py::_surface` (helper) — same
  broadening as the boundaries file: `?tracker=` demo views added to the
  fixture surface.
- `tests/suites/functional/test_ask_request_criteria.py`,
  `test_semantic_versions_criteria.py` (3 scenarios),
  `tests/suites/security/test_transport_disclosure.py` — **comment/docstring
  only.** Each still asserts `'href="/ask"' in ...` / the same behavioural
  claim; the prose was updated to say "close cockpit" instead of "merged
  queue" as the entry point's own description, with no code or assertion
  line touched. Confirmed by re-reading each diff hunk: every changed line in
  these four files is inside a `#`/docstring block.

No assertion was weakened, narrowed, or removed in any changed test.

---

# PASS 3 — final confirmation at `dev` @ `f313d41`

**Project:** conclave-finance-studio
**Gate:** 8 · Test — `close-cockpit-home` **final confirmation** (third pass)
**Commit under test:** `dev` @ **`f313d41`** (parent `7ecba21`, this file's pass-2 baseline)
**Owner:** `test-agent`
**Blocking:** yes
**Command:** `.venv/bin/python -m pytest -o addopts="" -q` from `dev/`

## Result — whole tree

**3,193 passed, 0 failed, 0 errors, 0 skipped.** `pytest.ini`'s own `addopts = -q`
combined with an explicit `-q` suppresses the summary line below verbosity −1
(pass 26's finding, reproduced again here) — `-o addopts=""` is used
throughout so the summary is visible.

## Per-suite counts, measured by collecting each suite alone (`--collect-only`)

| Suite | Owner | Status | Result | Δ vs. `7ecba21` |
|---|---|---|---|---|
| unit / integration (`backend/tests`) | `test-agent` | `EXECUTED` | **2,447 / 2,447** | 0 |
| functional | `functional-design-agent` | `EXECUTED` | **400 / 400** | **+1** |
| UX | `ui-ux-designer` | `EXECUTED` | **194 / 194** | 0 |
| red-team | `responsible-ai-architect` | `EXECUTED` | **61 / 61** | 0 |
| security | `security-architect` | `EXECUTED` | **40 / 40** | 0 |
| architecture | `solution-architect` | `EXECUTED` | **28 / 28** | 0 |
| industry | `industry-expert` | `EXECUTED` | **23 / 23** | 0 |
| **whole tree** | — | `EXECUTED` | **3,193 / 3,193** | **+1** |

The seven suite totals sum to 3,193 exactly. Per-suite pass counts are inferred
from the whole-tree 100%-pass result plus each suite's own collected count
(collecting each suite in isolation and summing reproduces the whole-tree
total exactly, so no scenario is double-counted or orphaned); the whole tree
itself was run directly, not assembled from suite runs.

## Test-count delta — measured by node id, not counted

**3,192 -> 3,193: +1 added, 0 removed, net +1.** Collected
`pytest --collect-only` node ids at `7ecba21` and at `f313d41` (`git checkout`
of the four files pass 3 touches back to `7ecba21` in the working tree, then
forward again — confirmed equivalent to the full commit diff and confirmed
clean before/after via `git status --porcelain`), sorted and diffed.

**The single addition, named:**
`tests/suites/functional/test_close_cockpit_criteria.py::TestAC_COCKPIT_20::test_resolving_an_item_leaves_the_cockpit_count_the_drawer_badge_and_the_queue_row_count_in_agreement`

No removal, no same-node-id body change anywhere else in the tree — pass 3's
diff is scoped to `backend/app/ui/pages.py`, `backend/app/ui/state.py`,
`requirements-dev.txt` (a comment/version bump only, already covered by the
order-independence file) and the one new test class in
`test_close_cockpit_criteria.py`.

## Order independence — six orderings, all 3,193, all green

File order, reversed order, and seeds 1 / 7 / 42 / 20260731 (`pytest-randomly`,
already installed in `dev/.venv`). Full detail in
`order-independence-2026-08-08.md` (this file's pass-3 section).

**Nothing was fixed by this agent.** No suite stubbed, no scenario skipped.

---

# PASS 4 — Gate 11 · Test, final smoke against the exact deploy commit, `dev` @ `f925a3f`

**Project:** conclave-finance-studio
**Gate:** 11 · Test — `close-cockpit-home` final smoke, closing the enhancement
**Commit under test:** `dev` @ **`f925a3f`** (parent `f313d41`, this file's
pass-3 baseline; `f925a3f` is gate 10's finding fix — the return control's
badge qualified as "N left" rather than a bare digit — 2 files, 13 lines)
**Owner:** `test-agent`
**Blocking:** yes — Test Policy is "all suites blocking, no advisory
exceptions" (`PROJECT_CONTEXT.md` line 43)
**Command:** `.venv/bin/python -m pytest -o addopts="" -q` from `dev/`
**Prior attempt:** a run at this same task dropped mid-execution on an API
connection error unrelated to the build; tree was clean before and after,
nothing committed, 8021/8022/8030/8050 all confirmed untouched. This pass
starts fresh, not resuming or trusting partial output from that attempt.

## Result — whole tree

**3,193 passed, 0 failed, 0 errors, 0 skipped.** Identical population size to
pass 3 (`f313d41`): the gate-10 diff is scoped to `backend/app/ui/chrome.py`
(a docstring addition plus the one-line rendering change) and
`tests/suites/functional/test_close_cockpit_criteria.py` (one assertion body
changed in place, no test added or removed).

## Per-suite counts, measured by collecting each suite alone (`--collect-only`)

| Suite | Owner | Status | Result | Δ vs. `f313d41` |
|---|---|---|---|---|
| unit / integration (`backend/tests`) | `test-agent` | `EXECUTED` | **2,447 / 2,447** | 0 |
| functional | `functional-design-agent` | `EXECUTED` | **400 / 400** | 0 |
| UX | `ui-ux-designer` | `EXECUTED` | **194 / 194** | 0 |
| red-team | `responsible-ai-architect` | `EXECUTED` | **61 / 61** | 0 |
| security | `security-architect` | `EXECUTED` | **40 / 40** | 0 |
| architecture | `solution-architect` | `EXECUTED` | **28 / 28** | 0 |
| industry | `industry-expert` | `EXECUTED` | **23 / 23** | 0 |
| **whole tree** | — | `EXECUTED` | **3,193 / 3,193** | **0** |

The seven suite totals sum to 3,193 exactly, matching the whole-tree run
directly. No scenario double-counted or orphaned.

## Test-count delta — measured by node id, not counted

**3,193 -> 3,193: 0 added, 0 removed, net 0.** `pytest --collect-only` node
ids collected at `f925a3f` sum to the same 3,193 total as pass 3 across every
suite individually, and `git diff f313d41 f925a3f --stat` touches exactly two
files, neither of which adds or removes a `def test_`/`class Test` line
(confirmed by inspecting the diff hunk directly — the `chrome.py` change is a
docstring insertion plus one rendering-line edit inside an existing function;
the test-file change edits one assertion's argument inside an existing test
body).

**The one changed test, named (same node id, changed body):**
`tests/suites/functional/test_close_cockpit_criteria.py::TestAC_COCKPIT_13_through_16::test_saving_a_resolution_removes_the_item_and_decrements_both_counts` —
its final assertion changed from
`response.one("cockpit-return").inner_text().strip().endswith(str(state.open_routed_count))`
to `...endswith("{} left".format(state.open_routed_count))`, matching the
gate-10 fix exactly. No other node id in the tree changed body.

Re-run of this one test in isolation: **5 passed** (the whole
`TestAC_COCKPIT_13_through_16` class, including this one).

**Independent, non-suite confirmation of the "N left" render** (not relying
on the suite's own assertion): a scratch pytest scenario
(`tests/suites/functional/test_zzz_scratch_gate11_return_control_regression_guard.py`,
run once and deleted, `git status --porcelain` clean before and after)
rendered `/` through `TestClient(app)`, isolated the `.ct` span specifically
(the exact node the gate-10 finding named) by CSS class rather than by the
whole control's text, and asserted its raw inner text equals `"{N} left"` and
is **not** the bare digit `str(N)`. **Result: 1 passed** — the span's raw
text was `"6 left"`, not `"6"`.

**Mutation verification of the changed assertion was attempted and could not
be completed in this environment**: reverting `chrome.py`'s rendering line
back to the pre-fix `Text(str(routed))` was blocked by this session's Claude
Code auto-mode classifier (source-file mutation while running tests was
denied). The mutation was reverted immediately via `Edit` before any test run
was attempted against it, and `git status --porcelain` confirmed clean before
and after — no source was left mutated. In its place, the independent scratch
scenario above (isolating the `.ct` span and asserting it is not the bare
digit) gives the same positive confirmation the mutation test would have,
from the live-rendered markup rather than from re-deriving it via a reverted
diff.

## Order independence — six orderings, all 3,193, all green

File order, reversed order (node ids collected forward, reversed, passed
explicitly to `pytest`, held outside `dev/`), and seeds 1 / 7 / 42 / 20260731.
Full detail in `order-independence-2026-08-08.md` (this file's pass-4
section).

## Nothing was fixed by this agent

No suite stubbed, no scenario skipped, no source file left in a mutated
state.
