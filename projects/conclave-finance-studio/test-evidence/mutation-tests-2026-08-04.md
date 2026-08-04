# Test evidence — mutation tests against the pass-21/22 work

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

Every mutation below was applied to **product code**, run, and reverted. The
harness refuses to start on a dirty tree and asserts `git status --porcelain`
is empty again after each revert. Working tree verified clean at `7757e0d`
after the last one, and the whole tree re-run (`3037 passed`, exit 0).

## Result

**11 mutations applied. 10 caught. 1 not caught by the in-tree suite** — and
that one **is** caught by this gate's own smoke scenario S32, which is why it
is reported as an advisory rather than a blocking failure. Detail at M3/M3b.

## The commits under test

| Commit | Closes |
|---|---|
| `ced2701` … `27b832d` | `AC-F41-24` / `AC-F5-08` — the relocated hazard and the four agents with no place in the list |
| `afe9e88` | the bare `AC-F5-07` claim standing in product source |
| `5cd4a85` | **the retained view was written beside the screen, not derived from it** |
| `7757e0d` | the functional suite's own join for `AC-F41-04`'s export artefact |

---

### Scenario: M0 — control: the unmutated build PRODUCES the export
- Status: EXECUTED
- Input: `/audit/export/file` on a served pilot, unmutated
- Expected: 200 — otherwise every "it refuses" result below would be vacuous
- Actual: **200**, `dossier_count 6`
- Result: PASS
- Evidence: an in-process `TestClient(app)` was tried first and admitted **zero** items, so an in-process check would have exercised a zero-dossier export and proved nothing. Every export assertion below is therefore driven against a **served pilot**, started and reaped inside the one call

### Scenario: M1 — an unclassified card is added to `approval_detail`
- Status: EXECUTED
- Input: `body.append(el('div', Text('a fact added later'), class_='card', data_testid='late-arrival'))` appended to the real approval screen
- Expected: the drift check names it, `retained.render` refuses, and **the auditor export is not produced at all** (`AC-F1-07`'s posture — no file rather than a file presented as complete)
- Actual: **CAUGHT.** `26 failed, 8 passed, 6 errors`; and **`/audit/export/file` → 500** on the served pilot, where the unmutated build returns 200
- Result: PASS (the mutation is caught)
- Evidence: this is the exact test the brief asked for — the refusal is observed at the **route**, not only at `retained.render`

### Scenario: M2 — an UNNAMED card is added to `approval_detail`
- Status: EXECUTED
- Input: a top-level `<div class="card">` with no `data-testid`
- Expected: refused rather than ignored — "the check could not see it" and "the check approved it" must not be the same result
- Actual: **CAUGHT.** `25 failed, 8 passed`, including `test_an_element_with_no_test_id_is_refused_rather_than_ignored`; **`/audit/export/file` → 500**
- Result: PASS

### Scenario: M3 — an evidential element is dropped from the region but left on the screen
- Status: EXECUTED
- Input: `in-force-panel` filtered out of the region as composed into `approval_detail`, and a stub card with the same testid appended to the screen
- Expected: caught
- Actual: **caught by the tree** (`1 failed, 39 passed` — `test_the_threshold_and_the_bundle_version_are_visible_at_approval_time`), but **NOT by the drift check**: `/audit/export/file` still returned **200**. The drift check classifies by **testid**, and the testid was still present
- Result: PASS (caught), with the seam recorded below

### Scenario: M3b — the same seam, with every word kept (the honest version of M3)
- Status: EXECUTED
- Input: the screen re-renders `in-force-panel` as a **second composition** of the same facts — same testid, all the same words, different bytes
- Expected: something in the tree notices that the artefact and the screen have diverged
- Actual: **NOT CAUGHT. `89 passed`** across `test_ui_retained_view.py`, `test_f41_retained_view.py` and `test_ui_approvals.py`
- Result: **FAIL of the in-tree check — reported as an ADVISORY, not a blocking failure**, because (a) the build itself is correct, and (b) **this gate does catch it**: with M3b applied, smoke **S32 fails** (`in-force-panel: verbatim_in_artefact false`); with it reverted, S32 passes on all eight elements
- Evidence, and the precise reason:
  `test_every_evidential_element_of_the_screen_is_in_the_artefact_verbatim`
  compares `retained.render(...)` against **`pages.approval_evidential_region(...)`** —
  the region, not the rendered screen. So it proves *artefact == region*. The
  drift check proves *every top-level testid on the screen is classified*. The
  join **"the screen's evidential content is that region"** is a source-level
  fact (`approval_detail` calling `body.extend(approval_evidential_region(...))`)
  that no scenario asserts. Closing it costs one line: compare against
  `pages.approval_detail(...)`'s own nodes rather than the region's. **For
  `code-agent`, after human review — not fixed here.**

### Scenario: M4 — `NOT_RETAINED` gains an entry for an element no screen renders
- Status: EXECUTED
- Input: a new key `"an-element-that-does-not-exist"` with a long reason
- Expected: refused — a list of exclusions that has outlived what it excludes is a list nobody reads
- Actual: **CAUGHT.** `1 failed, 32 passed` — `test_every_name_in_the_not_retained_list_is_on_the_screen_with_a_reason`
- Result: PASS

### Scenario: M5 — an evidential element is ALSO declared `NOT_RETAINED`
- Status: EXECUTED
- Input: `"in-force-panel"` added to `NOT_RETAINED` while it stays in the region
- Expected: overlap refused
- Actual: **CAUGHT.** `2 failed, 31 passed` — including `test_a_retained_element_cannot_also_be_declared_not_retained`
- Result: PASS

### Scenario: M6 — a `NOT_RETAINED` entry's reason is replaced by a token
- Status: EXECUTED
- Input: `"approval-control": "n/a"`
- Expected: refused — an exemption with no reason is an exemption table
- Actual: **CAUGHT.** `1 failed, 32 passed`, `assert 3 > 30` on the reason length
- Result: PASS

### Scenario: M7 — THE SHIPPED BUG, RESTORED: the reject radio's value goes back to the row index
- Status: EXECUTED
- Input: `value=str(_i)` over `enumerate(reasons)` — the exact pre-pass-21 code
- Expected: FAIL, and fail because the *rendered form* cannot complete a rejection
- Actual: **CAUGHT.** `1 failed, 62 passed` —
  `test_AC_F41_06_every_reason_the_form_RENDERS_completes_a_rejection`, with
  `AssertionError: /review/ITEM-21400-CP/reject returned 422 … <title>Not rejected</title>`
- Result: PASS
- Evidence: **the assertion fails at the store's refusal, not at a string comparison** — which is the property the pass-21 fix was for. Corroborated in a real browser: with the fix in place, all six rendered radios drive a rejection to completion (`rendered-ui-2026-08-04.md`)

### Scenario: M8 — the non-approving terminal action is removed from the approval screen
- Status: EXECUTED
- Input: the `non-approving-terminal-action` form suppressed
- Expected: `AC-F41-24` fails
- Actual: **CAUGHT.** `4 failed, 45 passed` — `test_AC_F41_24_…`, `test_the_non_approving_action_actually_records_something`, `test_AC_F41_01_the_new_action_is_per_proposal_and_appears_on_no_queue`, `test_the_override_is_not_offered_as_the_alternative`
- Result: PASS

### Scenario: M9 — an `AC-F5-08` unheld value is rendered as a blank instead of stated
- Status: EXECUTED
- Input: `UNRECORDED_VERSION = ""`
- Expected: refused — the criterion forbids omitted, blank, dashed, or a neighbour's value
- Actual: **CAUGHT.** `2 failed, 45 passed` — `test_AC_F5_08_an_agent_known_only_by_authorship_is_LISTED_and_says_what_is_missing` and `test_AC_F5_07_IS_NOT_MET_…`
- Result: PASS

---

### Scenario: the tree is clean after every mutation
- Status: EXECUTED
- Input: `git status --porcelain` after each `git checkout --`, and once more at the end
- Expected: empty every time
- Actual: **empty every time**; `HEAD` still `7757e0d`; final whole-tree run `3037 passed`, exit 0; both scratch worktrees removed
- Result: PASS
