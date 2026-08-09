# Test evidence — `close-cockpit-home` independent re-verification

**Project:** conclave-finance-studio
**Gate:** 8 · Test — `close-cockpit-home` close
**Date:** 2026-08-08
**Commit under test:** `dev` @ **`7ecba21`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED` for every scenario below

## 1. `AC-COCKPIT-08`'s differential probe-arithmetic test, mutation-tested

`tests/suites/functional/test_close_cockpit_criteria.py::TestAC_COCKPIT_08_probe_arithmetic_differential::test_routed_count_moves_by_exactly_the_probe_delta_and_coverage_does_not`
renders the cockpit twice (zero probes, one probe via a monkeypatched
`probes_module.plan_injection`) and asserts (a) `open_routed_count` moves by
exactly 1 and (b) `cockpit-coverage-strip`, `cockpit-act-noscan` and
`cockpit-act-forward-due` are byte-identical text across both renderings.

**Mutation performed:** `backend/app/ui/state.py::PilotState.cockpit_no_scan_accounts`
was edited to append a sentinel entry (`"MUTATION-TEST-SENTINEL"`) whenever
any probe item is present, making the no-scan tile move with the probe count
— exactly the class of defect `AC-COCKPIT-08` exists to catch.

- Before mutation: `2 passed`
- After mutation: **`1 failed, 1 passed`** — `AssertionError: cockpit-act-noscan`,
  diff showing `'3 Accounts...'` vs `'4 Accounts...MUTATION-TEST-SENTINEL...'`
- Mutation reverted (`git status --porcelain` on `backend/app/ui/state.py`
  confirmed clean before and after); re-run: **`2 passed`**

**Result: PASS.** The test genuinely checks the delta it claims to and would
catch a second figure moving with the probe count.

## 2. `AC-COCKPIT-04`'s single-return-control claim, re-verified independently

A scratch pytest scenario (not committed; `git status --porcelain` clean
before and after) rendered every screen `code-agent` checked plus screens
they had not: post-resolution landing (both the "next item or cockpit" case
and the "resolved to an explicit zero" empty-queue case), an error state
(422 on a resolve missing required fields), `/review/{id}`, and
`/dossier/{id}` — using `Document.hrefs()` against the real rendered markup
(not `inner_text`, which strips markup and produced a false "0 everywhere"
signal on a first attempt, corrected before recording this result).

| Screen / state | `href="/"` count |
|---|---|
| `/`, `/ask`, `/approvals`, `/monitors`, `/refusals`, `/catalogue`, `/queue`, `/exceptions`, `/review`, `/readiness`, `/dispositions`, `/audit`, `/inventory`, `/my-probe-history` | 1 each |
| `/review/{id}` | 1 |
| post-resolution empty-queue landing (explicit zero) | 1 |
| post-resolution landing (single, next item or cockpit) | 1 |
| error state (422 resolve failure) | 1 |
| `/dossier/{id}` | **0** |

**The `/dossier/{id}` zero is correct, not a defect.** The dossier is the
documented "shell-off exhibit" (`backend/app/ui/chrome.py:1009`,
`backend/app/evidence/provenance.py:11`, `backend/tests/test_ui_object_graph.py:146`,
`backend/tests/test_ui_brand.py:73`) — rendered with the application shell
entirely off, by design, so it carries no chrome and no return control of any
kind; `routes.py`'s own route map states `/dossier/{id}` goes "back to the
finding it evidences" (i.e. `/review/{id}`), not to `/`. `AC-COCKPIT-04`'s
claim is about screens the shell wraps, and the dossier is deliberately not
one. Every other screen and state checked, including the three
`code-agent` had not covered, carries exactly one.

**Result: PASS**, with the dossier's 0 explained as by-design rather than
folded silently into a "PASS everywhere" claim.

## 3. The sidebar is genuinely gone, not hidden by CSS

- `grep -rn '\bnav(\|\.navitem\|\.navgrp'` over `backend/app/` and every
  test tree: **every** hit is inside a comment or docstring recording the
  removal's history (`chrome.py` lines 521, 1084, 1089, 1124, 1132, 1162,
  1195, 1285; `test_ui_brand.py`, `test_ui_typography_floor.py`,
  `test_ui_information_architecture.py`). **No live call site, no CSS rule
  block** (`grep -n '\.navitem\s*{'` / `'\.navgrp\s*{'` over `chrome.py`:
  zero matches).
- `grep -n '"nav"'` over `chrome.py`: exactly one construction site
  (line 1180, the `cockpit-topbar`'s `el("nav", ...)`), carrying the drawer
  and the return control, `aria-label="Primary"` — the shell's own comment at
  that site states it is deliberately the **one** navigation landmark, "now
  that the sidebar's own `<nav aria-label="Primary">` is gone."
- No second, differently-classed construction of sidebar-equivalent markup
  found anywhere in `backend/app/ui/`.

**Result: PASS** — the sidebar is gone from the build, not merely hidden.

## 4. The two pass-2 test corrections, mutation-tested (revert and confirm the original defect reappears)

### `innerText` → `textContent` (`tests/suites/ux/test_ux_accessibility.py`)

Reverted `el.textContent.trim()` back to `el.innerText.trim()` in
`test_UX3_every_form_control_has_an_accessible_name`, ran the parametrized
scenario against a real Chromium instance (Playwright, in-process ASGI, no
port bound, launched and closed synchronously within one command):

- Before revert: `13 passed`
- After revert (defect reintroduced): **`12 failed, 1 passed`** — every
  screen carrying the persona-switch buttons flagged them as unnamed, e.g.
  `('/readiness', ['<button ... data-testid="persona-staff" ...>A. Reyes ...', '<button ... data-testid="persona-controller">D. Okafor ...'])`
- Reverted back; `git status --porcelain` clean before and after; re-run:
  **`13 passed`**

**Result: PASS.** The `innerText` version wrongly flags the persona buttons
exactly as the commit message predicted.

### Direct `.click()` → drawer-aware `click_nav()`/`click_persona()` helpers (`tests/suites/ux/harness.py`, `test_ux_journey.py`)

Reverted `_to_ask`'s `click_nav(page, "ask")` back to a direct
`page.locator('[data-testid="nav-ask"]').click(timeout=3000)` (timeout
shortened from the default only to make the mutation check itself fast; the
default-timeout behaviour is the same failure, slower), ran
`TestUX13StaffAccountantNight::test_the_entry_point_is_the_cockpit_and_ask_is_one_click_from_it`:

- Before revert: `1 passed`
- After revert (defect reintroduced): **`1 failed`** —
  `playwright._impl._errors.TimeoutError: Locator.click: Timeout 3000ms exceeded`,
  log: `element is not visible` (the closed `<details>` hides its non-summary
  children)
- Reverted back; `git status --porcelain` clean before and after; re-run:
  **`1 passed`**

**Result: PASS.** The direct-click version times out against the closed
drawer exactly as the commit message predicted.

## 5. FP&A is genuinely absent — reachability sweep from `/`

The functional suite's `TestNoThirdPersona` (state carries exactly 2
personas; switching to `fpa` is refused 400; no route path contains `"fpa"`)
was re-verified, and independently supplemented with a real BFS reachability
crawl from `/` (scratch scenario, not committed): 18 nodes visited following
only rendered `href`s from the entry point, scanning both link targets and
rendered text (lower-cased) for `"fp&a"` / `"fpa"`.

- **FPA hits: NONE** — zero rendered text mentions, zero link targets,
  across every screen a user can actually reach from `/`.

**Result: PASS.**

## 6. The nine overridden MVP1 criteria and `AC-F41-13`/`AC-F12-08` remain claimed nowhere

Per `test-evidence/register-cross-check-2026-08-04.md`, the forbidden set of
nine is `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`,
`AC-F5-02`, `AC-F5-03`, `AC-F5-05`, `AC-F5-07`. Re-swept over the current
tree (`7ecba21`) in both hyphenated and underscored form, filtering out the
already-documented self-denying node IDs (the `_IS_NOT_MET_`-shaped tests and
the explicitly-narrowed `COVERS ONLY...` lines that assert the criterion is
**not** met):

- **Zero unfiltered `COVERS` claims** for any of the nine.
- The only node-id/`COVERS` hits present are the same self-denying ones
  already on record (`AC_F5_02`, `AC_F5_03`, `AC_F5_07` — each an
  `_IS_NOT_MET_`-shaped scenario or an explicitly-narrowed `COVERS`).
- `AC-F41-13` and `AC-F12-08`: **0 occurrences of any kind** under `dev/`
  (source, tests, docstrings), matching the record at `b447a11`.

**Result: PASS.** This enhancement's diff (`backend/app/ui/*.py` and the
test files listed in `unit-integration-2026-08-08.md`) does not touch any
file that carries a claim on these nine, and none of the nine gained a
claim.

---

# PASS 3 — final confirmation at `dev` @ `f313d41`

**Owner:** `test-agent` · **Blocking:** yes · **Status:** `EXECUTED` for every
scenario below. This is the third pass on `close-cockpit-home`; every item
gate 8 already covered is re-verified against the current commit rather than
carried forward from pass 2's evidence above.

## 1. `AC-COCKPIT-20` as amended, verified against the test, mutation-tested

**The amendment, confirmed against `knowledge/FUNCTIONAL_SPEC.md` §29.5**,
not taken on the commit message's word: `functional-design-agent`'s pass-6
review rewrote the Then-clause from an internal-computation claim ("both read
from the same computation … not from a second count that happens to agree
with it today") to pure observable value equality — "the drawer's `nav-queue`
badge reads K−1, `/queue`'s own row listing no longer includes that item as a
row, and both equal the routed-item count rendered on the close cockpit in
the same state — three independent readings that must agree, and a check
that confirms only one of the three does not satisfy this criterion." ID,
Given and When unchanged; a wording amendment under the existing ID, not a
new criterion.

**The test, read against that wording:**
`tests/suites/functional/test_close_cockpit_criteria.py::TestAC_COCKPIT_20::test_resolving_an_item_leaves_the_cockpit_count_the_drawer_badge_and_the_queue_row_count_in_agreement`
asserts `after_badge == after_cockpit` and `after_rows == after_cockpit` —
three surfaces (`state.open_routed_count`, the drawer badge fetched from
`/ask`, and `/queue`'s own row count) read independently and compared for
equality, exactly the amended Then-clause and not the rejected
internal-computation wording (no test line inspects which property or method
produced any of the three numbers).

**Mutation performed:** reverted `backend/app/ui/pages.py` and
`backend/app/ui/state.py` to their pre-fix (`7ecba21`) state
(`git diff 7ecba21 f313d41 -- <the two files> | git apply -R`), which makes
the drawer badge and `/queue`'s row count **both** wrong relative to the true
open count **and equal to each other** (both stale at the pre-resolution
value) — the case a two-way badge-vs-rows check would pass and a check
against the true count catches.

- Before revert (current fix in place): `1 passed`
- After revert (bug reintroduced): **`1 failed`** —
  `assert after_badge == after_cockpit` → `assert 6 == 5`. Both the badge and
  `/queue`'s row count landed on 6, in agreement with each other and both
  wrong against the cockpit's true `open_routed_count` of 5.
- Reverted back (`git checkout -- backend/app/ui/state.py backend/app/ui/pages.py`);
  `git status --porcelain` confirmed clean before and after; re-run:
  **`1 passed`**

**Result: PASS.** The three-way equality check catches the exact defect
class the amendment was written to guarantee: two surfaces silently agreeing
with each other while both diverge from the true count.

## 2. The fix's root cause, confirmed independently — no fourth "what's open" computation

Traced every read site of `routed_to_human`, `disposition_for`,
`rejection_for`, `open_routed_items`, `open_routed_count`, `queue_rows` and
`nav_badges` across `backend/app/`:

- `state.py:777` (`nav_badges["queue"]`) and `pages.py:728` (`/queue`'s row
  source, `queue_rows`) both now resolve to `open_routed_count` /
  `open_routed_items`, as the fix intends.
- `chrome.py:1178` (`cockpit-return`, `AC-COCKPIT-04`'s non-drawer control)
  independently confirmed to read `state.open_routed_count` — the same
  property the cockpit's own tile reads, unchanged by this pass and already
  the third surface the amended `AC-COCKPIT-20` holds in agreement.
- `state.py:809` (`routed_items`/`routed_count`) is a **different, correctly
  distinct** question — "ever routed," not "still open" — used only for
  routing-budget setup (`state.py:2405`) and left alone by design, per the
  comment at `state.py:815-825`; it does not compete with `open_routed_*` for
  the "what's open" answer and nothing renders it as an open count.
- `disposition_for`/`rejection_for` are only used as per-item lookups
  (`pages.py:1480`, `2819`, `3375`) for rendering a single item's own state,
  not as an aggregate.
- `test_ui_chrome.py:40`'s `nav_badges = {"queue": 5, ...}` and
  `test_f12_probes.py`'s local variable named `queue_rows` are unrelated —
  a hardcoded stub for a chrome-rendering unit test and an unrelated local
  name in a probe-miss-rate test, respectively, neither computing "what's
  open."

**Result: PASS.** No third or fourth independent re-derivation of "what's
still open" exists in the codebase; every surface that states an open count
now traces to `open_routed_count`/`open_routed_items`.

## 3. Full re-run of everything gate 8 already covered

- **Whole tree, six orderings**: file, reversed, seeds 1/7/42/20260731 — all
  **3,193 / 3,193**, all green. Detail:
  `unit-integration-2026-08-08.md` (pass 3 section),
  `order-independence-2026-08-08.md` (pass 3 section).
- **`AC-COCKPIT-08`'s differential probe-arithmetic test** and
  **`AC-COCKPIT-04`'s single-return-control claim**: re-run
  (`TestAC_COCKPIT_08_probe_arithmetic_differential`, `TestAC_COCKPIT_04`) —
  `4 passed`. Underlying code (`chrome.py`'s coverage/no-scan/cockpit-return
  logic) is untouched by pass 3's diff (scoped to `pages.py`/`state.py`'s
  queue/badge properties only), so item 1 above's mutation-test standard is
  not re-applied to these two here; they were already deep-mutation-verified
  at pass 2 (`close-cockpit-home-verification-2026-08-08.md`, items 1-2
  above) against code that has not since changed.
- **`AC-COCKPIT-04`'s single-return-control claim, independently re-verified
  across screens/states, pass 3**: a scratch pytest scenario
  (`tests/suites/functional/test_zzz_scratch_single_return_recheck.py`, run
  once and deleted, `git status --porcelain` clean before and after) rendered
  the twelve navigable/aliased routes, `/dossier/{id}`, the post-resolution
  landing, the fully-resolved empty-queue landing, and a 404 error state.
  Result: exactly one `href="/"` on all sixteen chromed screens/states;
  **zero** on `/dossier/{id}`, by design (the documented shell-off exhibit).
- **Sidebar absence**: re-swept at `f313d41` — `.navitem`/`.navgrp`/`def nav(`
  have no live call site anywhere in `backend/app` (every hit is inside a
  comment); zero CSS rule blocks for either class.
- **FP&A absence**: re-confirmed live, via this pass's own smoke test (item 4
  below) — `/fpa`, `/fp-and-a`, `/fpna` all `404`; no `FP&A`/`FPNA` string
  anywhere on the served entry point.
- **The nine overridden MVP1 criteria plus `AC-F41-13`/`AC-F12-08`**:
  re-swept over `f313d41` for `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
  `AC-F40-17`, `AC-F36-48`, `AC-F5-02`, `AC-F5-03`, `AC-F5-05`, `AC-F5-07` in
  both hyphenated and underscored form: **zero unfiltered `COVERS` claims**
  for any of the nine. `AC-F41-13` and `AC-F12-08`: **0 occurrences of any
  kind** under `dev/` (source, tests, docstrings).

**Result: PASS** on every item re-run.

## 4. The smoke test — executed against a freshly stood-up instance on 8021/8022

`deploy-agent`'s manual walk at `7ecba21` (recorded in `PROJECT_CONTEXT.md`,
2026-08-08) is not a substitute for an executed suite result, and the prior
gate-8 pass recorded the smoke test as `STATIC ONLY — NOT EXECUTED` because no
process was listening at gate time. This pass stood up its own instance,
synchronously within one command invocation (the pilot process launched,
driven over real HTTP, torn down, before the invocation returned) — never a
long-lived process left running past this agent's turn.

**Method:** `CONCLAVE_ENV=pilot API_PORT=8021 GES_PORT=8022 .venv/bin/python
backend/pilot.py`, started in its own process group (`start_new_session=True`),
`CONCLAVE_VAR_DIR` pointed at a scratch copy of `dev/var` so this run could not
write into the SQLite files the human's live 8030 session is reading. Torn
down by `SIGTERM` to the process group inside the same invocation.

**13 scenarios, 13 pass, 0 FAIL.**

### Scenario: startup — /health reachable within 30s
- Status: EXECUTED · Expected: 200 within 30s · Actual: reachable · Result: PASS

### Scenario: G2 — /health payload
- Status: EXECUTED
- Expected: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`
- Actual: exact match
- Result: PASS
- Evidence: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`

### Scenario: G1 — twelve routes all 200
- Status: EXECUTED
- Actual: `{"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}`
- Result: PASS

### Scenario: ENTRY — / renders the close cockpit, not the queue
- Status: EXECUTED
- Expected: `cockpit-h1`, `close-tracker`, `cockpit-acts`, `cockpit-coverage-strip` present; `exception-queue` absent
- Actual: all four cockpit markers present, `exception-queue` absent
- Result: PASS

### Scenario: NAV — drawer present, no sidebar markup on /
- Status: EXECUTED
- Expected: `drawer` testid present, no `.navitem`/`.navgrp`/`.shell` classes
- Actual: drawer present, no sidebar markup
- Result: PASS

### Scenario: DISCLOSURE — pilot-strip present on /
- Status: EXECUTED · Actual: present · Result: PASS

### Scenario: DISCLOSURE — topology-strip present on /
- Status: EXECUTED · Actual: present · Result: PASS

### Scenario: FPA — /fpa /fp-and-a /fpna all 404, no FP&A string on /
- Status: EXECUTED
- Actual: `{"/fpa": 404, "/fp-and-a": 404, "/fpna": 404}`, no "FP&A"/"FPNA" string on `/`
- Result: PASS

### Scenario: AC-COCKPIT-20 setup — badge/row counts readable before any action
- Status: EXECUTED · Actual: `before_badge=6 rows_before=6` · Result: PASS

### Scenario: AC-COCKPIT-20 — resolve returned 200
- Status: EXECUTED · Input: `POST /review/<open item>/resolve` (R2, explanation, clears_by)
- Actual: 200 · Result: PASS

### Scenario: AC-COCKPIT-20 — drawer badge decremented on a live served instance
- Status: EXECUTED · Expected: 6 -> 5 · Actual: 6 -> 5 · Result: PASS

### Scenario: AC-COCKPIT-20 — /queue row count decremented on a live served instance
- Status: EXECUTED · Expected: 6 -> 5 · Actual: 6 -> 5 · Result: PASS

### Scenario: AC-COCKPIT-20 — resolved item no longer a /queue row
- Status: EXECUTED · Actual: absent from `/queue`'s rendered rows · Result: PASS

**Process lifecycle, this smoke run:** pilot pid confirmed dead (`ps -p <pid>`
returns nothing) and `lsof -nP -iTCP -sTCP:LISTEN` confirms 8021/8022 free
immediately after teardown. The human's pilot (8030, pid 48206) and the
design preview (8050, pid 85436) were checked by `lsof` PID before and after
this run and are unchanged, never probed or signalled. One harness note: the
follow-up `SIGKILL` to the process group after `SIGTERM` raised
`PermissionError` because the group's only process was already reaped by the
`SIGTERM` — cosmetic, confirmed by the independent `ps`/`lsof` checks above,
not by the exit path.

**Result: EXECUTED, 13/13 PASS.** This satisfies the smoke test's blocking
obligation for this gate — the prior `STATIC ONLY — NOT EXECUTED` verdict is
superseded, not carried forward.

## Process-lifecycle note

Every Chromium launch above (items 1 is pure Python/pytest, no browser;
items 4's two mutation checks) was driven synchronously within a single
`pytest` command invocation — the browser launched, ran, and exited before
the tool call returned. No server or browser was left running past this
agent's turn. No scratch test file was left in the tree — each was created
under `tests/suites/functional/test_zzz_scratch_*.py`, run, and `rm`'d, with
`git status --porcelain` confirmed clean immediately after each.
