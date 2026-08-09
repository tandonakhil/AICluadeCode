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

## Process-lifecycle note

Every Chromium launch above (items 1 is pure Python/pytest, no browser;
items 4's two mutation checks) was driven synchronously within a single
`pytest` command invocation — the browser launched, ran, and exited before
the tool call returned. No server or browser was left running past this
agent's turn. No scratch test file was left in the tree — each was created
under `tests/suites/functional/test_zzz_scratch_*.py`, run, and `rm`'d, with
`git status --porcelain` confirmed clean immediately after each.
