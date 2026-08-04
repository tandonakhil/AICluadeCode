# Test evidence — audit of every scenario that changed since the last run

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

Six commits sit between `c428fe5` (the commit pass 20 reported on) and
`7757e0d`. Between them they touch **four product files and six test files**.
Every changed scenario is audited below — a scenario that changed is a coverage
decision, and this pass's job is that building a ruling did not open a hole.

## The six commits

| Commit | Subject |
|---|---|
| `ced2701` | `AC-F41-24`: the hazard was relocated at pass 17, and arrived unaccompanied |
| `27b832d` | `AC-F5-08`: four agents were named in a paragraph and given no place in the list |
| `afe9e88` | the bare `AC-F5-07` claim stood in the product source, not only in a scenario |
| `4ccad43` | `AC-F41-01` still binds on the approval screen, so the surface is walked for it |
| `5cd4a85` | `AC-F41-04`: the retained view was written beside the screen, not derived from it |
| `7757e0d` | the functional suite's own join for `AC-F41-04`'s export artefact |

| Product file | Lines |
|---|---|
| `backend/app/ui/pages.py` | +330 |
| `backend/app/ui/retained.py` | **new**, 247 |
| `backend/app/ui/state.py` | ±68 |
| `backend/app/ui/components.py` | ±27 |

---

## Removals — five, every one instructed, none a coverage loss

### Scenario: the three `TestNoApproveControlHere` scenarios folded into one
- Status: EXECUTED
- Input: `FUNCTIONAL_SPEC` §28.1 instruction 1 — *"re-point it at `AC-F41-22` and extend it to assert what its two sibling scenarios already assert, so that one ID's evidence is not spread across three independently-named scenarios"*
- Expected: the replacement asserts everything all three did, and the fold is the reason the removals happened
- Actual: **it does.** The replacement asserts co-visibility of the three elements, non-disclosure of each, `approving_controls(document) == []`, absence of `approve-lines`, absence of `approval-control` — the union of the three — and adds two things none of them had: **both personas** ("at any permission level") and a **population guard** (`len(checked) >= 8`, `seen_eligibility == {"true","false"}`)
- Result: PASS — coverage widened, not narrowed
- Evidence: mutation M8 fails four scenarios; instrumented iteration counts 47 / 14 / 3

### Scenario: the two `AC-F5-07` scenarios replaced by three
- Status: EXECUTED
- Input: `FUNCTIONAL_SPEC` §28.2's ruling on what *each agent* quantifies over
- Expected: the removed scenarios were the tautology, and what replaces them both records the criterion unmet and keeps the narrower claim that is true
- Actual: **`test_AC_F5_07_every_agent_is_listed_with_version_and_entitlements`** quantified over the registry's own projection — precisely the shape the ruling names. Replaced by `test_AC_F5_07_IS_NOT_MET_…` (fails in either direction), plus `test_every_REGISTERED_agent_row_carries_its_own_version_and_entitlements` and `test_a_lineage_view_is_reachable_from_each_REGISTERED_listed_version`, whose names now state their scope
- Result: PASS — 2 became 3, and the criterion moved from claimed to recorded-unmet
- Evidence: `register-cross-check-2026-08-04.md`

## The one in-place change

### Scenario: `TestReachability::test_the_approval_object_mounts_its_components` — parametrisation widened
- Status: EXECUTED
- Input: AST comparison of the decorator source at both revisions
- Expected: cases added, no assertion changed
- Actual: **`approval-detection-evidence` and `evidence-set` added**; the function body is byte-identical after `ast.dump`. Both new cases appear as new collected node ids
- Result: PASS

### Scenario: no other scenario changed its assertions while keeping its name
- Status: EXECUTED
- Input: AST comparison of every same-named function in the six touched test files, comparing dumped body and decorator source
- Expected: any silent edit reported
- Actual: **zero.** No body-only edit, no docstring-only edit
- Result: PASS

## Additions — 54, audited

### Scenario: every added scenario can fail
- Status: EXECUTED
- Input: AST over all 54 added node ids — does each carry an `assert` or a `pytest.raises`?
- Expected: 54 of 54
- Actual: **54 of 54.** Zero exceptions
- Result: PASS

### Scenario: the additions are reachability-shaped, not component-shaped
- Status: EXECUTED
- Input: the two new files and the classes added to `test_ui_approvals.py`
- Expected: scenarios drive the real route and query the returned document, per `code-agent`'s reachability obligation — not call a component and assert on its return
- Actual: **they do.** `TestTheNewComponentsAreReachable` renders from the entry point and asserts the component is in the tree the route returned; the export scenarios go through `U.CLIENT.get("/audit/export/file")`; `AC-F41-22` walks `reachable_urls()` from `/`
- Result: PASS
- Evidence: `uihelpers.py`'s own docstring states the rule; the instrumented traversal counts show the walks really happen

### Scenario: the additions are held by mutations, not only by assertions
- Status: EXECUTED
- Input: 11 mutations to product code
- Expected: each new area has at least one mutation that it catches
- Actual: **drift → export refusal (M1, M2), unnamed element (M2), `NOT_RETAINED` integrity (M4, M5, M6), the shipped reject-radio bug (M7), `AC-F41-24` (M8), `AC-F5-08` (M9)** — all caught. **One seam not caught in-tree (M3b)**, reported as an advisory and caught by this gate's own smoke S32
- Result: PASS, with the M3b advisory
- Evidence: `mutation-tests-2026-08-04.md`
