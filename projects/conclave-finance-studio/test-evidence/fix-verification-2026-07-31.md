# Test evidence — pass-13 fix verification (the gate-8 loop-back's four items)

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run)
**Date:** 2026-07-31
**Commit under test:** `dev` @ **`55878c9`** · parent repo @ **`8697994`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

Each of the four was **re-driven by the check that originally caught it**, not
accepted on the commit message. Where the original catch was a mutation, the
mutation was re-planted; where it was an HTTP drive against the served pilot,
the pilot was re-served and re-driven. A negative control — the same input
against `9d819c1` — was run for F1, because a fix that cannot be shown to have
changed anything is not evidence.

---

## F1 — the persisted warehouse

### Scenario: F1-1 — the pilot AS FOUND, over HTTP, through the real export path
- Status: EXECUTED
- Input: `dev/var/warehouse.sqlite3` untouched (md5 `1d018fb4a6020e629b7fbdab2567ee3a`);
  `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`; then, over stdlib HTTP
  to `127.0.0.1:8021` and never through `TestClient`:
  `POST /pilot/viewing-as persona=controller` → `POST /proposal/PROP-2026-06-0031/approve`
  → the override control the denial rendered → `POST /proposal/PROP-2026-06-0031/export`
- Expected: the drive that returned `403 revalidation_could_not_run / no such
  column: period_status` at gate 8 now completes
- Actual: approve `403` (denied on value, as designed) → override `200` →
  **export `200`**, no `revalidation_could_not_run`, no `no such column`
- Result: PASS
- Evidence: `{"export_status": 200, "export_says_revalidation_could_not_run": false,
  "export_says_no_such_column": false, "group_id": "CS-E1F420D4F62A",
  "export_file_status": 200, "export_file_lines": 3}`

### Scenario: F1-2 — the NEGATIVE CONTROL: the same stale file still fails at `9d819c1`
- Status: EXECUTED
- Input: a warehouse file carrying all three gap kinds, built mechanically from
  the pilot's own seed — `erp_control_extract` rebuilt with the six pre-POAR
  columns (rows preserved), `suspense_residuals` dropped entirely,
  `fx_revaluation` created and populated. That one file placed in a `9d819c1`
  git worktree's `var/`, and the identical HTTP drive run against it.
- Expected: if my plant does not reproduce the original defect, the F1-3 pass
  below proves nothing
- Actual: **`403`**, `revalidation_could_not_run` present, `no such column` present
- Result: PASS (the defect is reproduced, so the plant is a fair one)
- Evidence: `{"export_status": 403, "export_says_revalidation_could_not_run": true,
  "export_says_no_such_column": true, "group_id": null}`. Also
  `"not_run_count": 2` — the missing `suspense_residuals` produced a *second*
  boundary check reporting "not run", degrading `AC-F28-07`'s signal.

### Scenario: F1-3 — that same file, byte-identical, at `55878c9`
- Status: EXECUTED
- Input: the same planted warehouse copied into `dev/var/warehouse.sqlite3`; pilot
  served; same HTTP drive
- Expected: 200, and the file repaired on all three gap kinds
- Actual: **`200`**, `group_id CS-3B2162F286C9`, file served with 3 lines.
  Warehouse after the run: `erp_control_extract` carries `period_status`,
  `latest_journal_ts`, `extract_as_of` again (50 rows); `suspense_residuals`
  restored **and populated** (24 rows, not an empty recreated table);
  `fx_revaluation` **gone**. `not_run_count` back to **exactly 1**.
- Result: PASS
- Evidence: `erp cols: [..., 'period_status', 'latest_journal_ts', 'extract_as_of']`,
  `suspense_residuals 24 / gl_je_lines 110 / erp_control_extract 50 /
  wh_account_balances 48`, `{"not_run_count": 1, "export_status": 200}`

### Scenario: F1-4 — the THIRD gap kind alone: an object declared absent but present
- Status: EXECUTED
- Input: the as-found warehouse with **only** `fx_revaluation` added — every
  declared object present and current, so gap kinds 1 and 2 cannot trigger the
  rebuild. This is the case the brief singles out: a persisted file from an
  earlier full seed silently restoring the object the pilot omits so
  `AC-F28-07`'s "not run" is reachable.
- Expected: the rebuild still fires, `fx_revaluation` is removed, and the pilot's
  deliberate omission survives
- Actual: `fx_revaluation present after seed: False`; `not_run_count` **1**;
  `gl_je_lines` 110 (reseeded, not left empty); export `200`
- Result: PASS
- Evidence: `fx_revaluation present after seed: False` / `{"not_run_count": 1,
  "export_status": 200, "export_says_exported": true}`

### Scenario: F1-5 — `seed()` on an already-current warehouse is a no-op
- Status: EXECUTED
- Input: the as-found file, four full pilot boots across this run
- Expected: no gratuitous rebuild
- Actual: md5 unchanged at `1d018fb4a6020e629b7fbdab2567ee3a` before and after
- Result: PASS
- Evidence: `md5 -q var/warehouse.sqlite3` → `1d018fb4a6020e629b7fbdab2567ee3a`,
  identical to the backup taken before any drive.

### Scenario: F1-6 — the suite's own three new ARCH_05 scenarios drive the real bootstrap
- Status: EXECUTED (reviewed as well as run)
- Input: `tests/suites/architecture/test_architecture_conformance.py`
- Expected: they go through `pilot_transport.seeded_dev_warehouse()` — the exact
  call `pilot.py` makes — rather than `SqliteWarehouse(tmp).seed()`
- Actual: they do; `persisted_var_dir` redirects the default path with
  `CONCLAVE_VAR_DIR` to `tmp_path` and asserts the redirect took, so the suite
  never writes the developer's `var/`. `test_ARCH_05_the_certified_query_the_export_refused_on_now_executes`
  drives `poar.export_basis@1` through the real GES query route, not raw SQL.
- Result: PASS
- Evidence: `assert path.startswith(str(tmp_path)), path` in the fixture;
  `assert warehouse.last_migration is not None`; `assert all(row["period_status"] for row in rows)`

**F1 verdict: FIXED and verified, including the third gap kind in isolation.**

---

## F2 — the viewer-session leak

### Scenario: F2-1 — `_restore_run_tier` is gone, not renamed
- Status: EXECUTED
- Input: `grep -rn "_restore_run_tier"` across the tree
- Expected: no definition anywhere
- Actual: exactly one hit, and it is a comment in `tests/suites/ux/conftest.py`
  explaining why it was removed
- Result: PASS
- Evidence: `tests/suites/ux/conftest.py:87:# \`_restore_run_tier\` used to live here and restored the tier by name. It was`

### Scenario: F2-2 — the reverse-order permutation that found the persona leak
- Status: EXECUTED
- Input: `ORDER_MODE=reverse` over `tests/suites/ux`, and separately over the whole tree
- Expected: pass in both
- Actual: `186 passed in 14.58s`; whole tree `2664 passed in 54.13s`
- Result: PASS
- Evidence: `ORDER MODE: reverse items: 186` / `items: 2664`

### Scenario: F2-3 — the shuffle permutations, `ux` suite
- Status: EXECUTED
- Input: `ORDER_MODE` ∈ {1, 7, 20260731}
- Expected: 186 pass at every seed
- Actual: 186, 186, 186
- Result: PASS
- Evidence: `186 passed in 14.76s` / `14.64s` / `14.67s`

### Scenario: F2-4 — the AST guard fails when a third public attribute is planted
- Status: EXECUTED (mutation)
- Input: `self.last_persona_switch = key` appended to `PilotState.view_as` in
  `backend/app/ui/state.py`
- Expected: the guard fails and names the attribute and the method that set it
- Actual: **2 failed, 7 passed.** The guard fired, and so did its own negative
  control (`test_the_guard_would_notice_a_new_attribute`), which is what stops
  the guard passing on a scan that silently found nothing.
- Result: PASS (mutation killed)
- Evidence:
  ```
  test_ui_state_session.py:136: AssertionError: these attributes of the
  process-wide PilotState are set outside __init__ and are not in
  VIEWER_SESSION_ATTRS, so nothing restores them between scenarios:
  {'last_persona_switch': 'view_as'}
  test_ui_state_session.py:149: AssertionError: assert {'last_person...'select_tier'} == {'persona': '...'select_tier'}
  ```
  Mutation reverted; `9 passed`; `git status --short` empty.

**F2 verdict: FIXED and verified. The restore is now over the declared set
(`VIEWER_SESSION_ATTRS = ("persona", "tier")`), it lives in the shared
`tests/suites/conftest.py` so every suite that renders a screen gets it, and the
guard demonstrably fails on a third attribute.**

---

## F3 — `export.build`

### Scenario: F3-1 — my exact gate-8 mutation, re-planted
- Status: EXECUTED (mutation)
- Input: `integrity: Dict[str, Any] = {}` restored as a default on **both**
  `Export.__init__` and `build()`
- Expected: the mutation that survived all 2,602 scenarios at `9d819c1` now dies
- Actual: **3 failed**, 2,661 passed
- Result: PASS (mutation killed)
- Evidence: `test_integrity_has_no_default_on_the_construction_path[build]`,
  `[Export.__init__]`, and
  `test_omitting_integrity_is_a_TypeError_rather_than_an_empty_statement`

### Scenario: F3-2 — the second gate-8 mutation: `Export(..., integrity={})` constructs
- Status: EXECUTED (mutation)
- Input: with the default restored, construct
  `Export(period=202606, tenant_id='t', dossiers=[], completeness_statement='s', integrity={})`
- Expected: at gate 8 this constructed cleanly and produced JSON naming neither
  `AC-F1-11` nor `AC-F1-08`. It must now refuse.
- Actual: **refused at construction**
- Result: PASS
- Evidence: `REFUSED: IntegrityStatementMissing the export failed at
  evidence_integrity: this export states nothing about anchor. An export silent
  on it reads as one whose anchors are signed and whose retenti...`

### Scenario: F3-3 — the enforcement is on CONTENT, and each leg is load-bearing
- Status: EXECUTED (two mutations)
- Input: (B) delete the "declares the residual and says nothing about it in
  words" check; (C) delete the "declares the residual without naming its
  criterion" check
- Expected: each kills scenarios; a contract enforced only on presence would
  survive both
- Actual: B → 2 failed (`[anchor]`, `[retention]`); C → 2 failed
  (`[anchor-AC-F1-11]`, `[retention-AC-F1-08]`)
- Result: PASS (both killed)
- Evidence: `test_declaring_the_residual_with_an_empty_sentence_is_refused[anchor]`;
  `test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`

### Scenario: F3-4 — registers 3 and 4 unchanged: nothing claims `AC-F1-11` or `AC-F1-08`
- Status: EXECUTED
- Input: all 2,664 collected node IDs scanned for both IDs in both spellings,
  plus every textual occurrence in `backend/tests` and `tests/suites` read
- Expected: zero claims
- Actual: **zero claims.** Two node IDs now contain the strings —
  `test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor-AC-F1-11]`
  and `[retention-AC-F1-08]` — and both are parametrize labels on a scenario
  asserting the export is **refused unless it names the criterion it does not
  meet**. That is the denial, stated at the strongest possible place. Every one
  of the 13 textual occurrences is either such a denial (`"AC-F1-08" IS NOT
  COVERED BY THIS SUITE`, `"do not map it to that ID"`) or an assertion that the
  **product's own disclosure** carries `unmet_criterion == "AC-F1-08"`.
- Result: PASS
- Evidence: `AC-F1-08 -> 0` / `AC-F1-11 -> 0` in the underscored form used by
  claiming test names; the two dashed hits are the parametrize IDs above.
  `tests/suites/functional/test_acceptance_criteria.py:326: """AC-F1-08 IS NOT
  SATISFIED BY THIS SCENARIO — do not map it to that ID.`

**F3 verdict: FIXED and verified. Registers 3 and 4 remain open and are claimed
nowhere.**

---

## A2 — the unknown run tier

### Scenario: A2-1 — driven on the SERVED pilot, both directions
- Status: EXECUTED
- Input: over real HTTP to `127.0.0.1:8021`, in this order:
  `/ask?tier=certified` → `?tier=nonsense_typo` → `?tier=certified` →
  `?tier=exploration` → `?tier=nonsense_typo` → `?tier=exploration`.
  Order matters because the tier is process state shared by every later caller,
  which is the whole defect.
- Expected: 400 from both directions, and the current tier untouched
- Actual: typo-from-certified **400**, typo-from-exploration **400**; certified
  renders 23,076 bytes before and after the typo; exploration renders 24,864
  before and after. The two tiers still render differently, so the refusal is
  not a route that refuses everything.
- Result: PASS
- Evidence: `{"detail":"'nonsense_typo' is not a run tier. The declared tiers
  are: certified, exploration"}`

### Scenario: A2-2 — the second route that accepts the parameter
- Status: EXECUTED
- Input: `GET /exceptions?tier=nonsense_typo`
- Expected: the same refusal — a fix applied to one of the two GET routes would
  leave the leak reachable
- Actual: **400**, same body
- Result: PASS
- Evidence: `{"detail":"'nonsense_typo' is not a run tier. The declared tiers are: certified, exploration"}`

### Scenario: A2-3 — the edge values
- Status: EXECUTED
- Input: `/ask?tier=` (empty) and `/ask?tier=CERTIFIED` (wrong case)
- Expected: refused, not silently defaulted
- Actual: both **400**
- Result: PASS
- Evidence: 81-byte and 90-byte 400 bodies naming the declared tiers
- Note: an empty `tier=` is a refusal rather than "no selection". `routes.py`
  only calls `_select_tier` when the parameter is present at all, so a caller
  omitting it entirely is unaffected; a caller sending `tier=` gets a 400.
  Recorded as behaviour, not as a defect — no criterion asks for leniency here,
  and leniency is the shape the fix removed.

### Scenario: A2-4 — the docstring gate 8 flagged as contradicting the code
- Status: EXECUTED (read)
- Input: `state.select_tier`'s docstring
- Expected: the "An unknown value falls back to CERTIFIED" line is gone or true
- Actual: rewritten — "Set the run tier. An unknown value is REFUSED, not
  ignored." followed by the gate-8 finding in full
- Result: PASS
- Evidence: `backend/app/ui/state.py:429-448`

**A2 verdict: FIXED and verified. No value of this parameter now selects a tier
the caller did not name, and no value leaves a tier an earlier caller chose.**

---

## Carried forward, NOT fixed — the interleaved-shuffle order dependence

`code-agent` discloses that a shuffle interleaving `backend/tests` with
`tests/suites` is not order-clean, that the cause is wider than the viewer
session, and that **it reproduces at `9d819c1`**, so it predates pass 13. The
brief asks me to verify that reproduction claim independently rather than accept
it.

### Scenario: OD-1 — it reproduces at `55878c9`
- Status: EXECUTED
- Input: whole-tree shuffle at seeds 1, 7, 42, 20260731
- Expected: some seeds fail
- Actual: **2, 1, 1 and 0 failures** respectively
- Result: FAIL (the limitation is real at the tree under test)
- Evidence: see `unit-integration-2026-07-31.md` for the node IDs

### Scenario: OD-2 — it reproduces at `9d819c1` with DIFFERENT scenarios failing
- Status: EXECUTED
- Input: `9d819c1` checked out into a git worktree, its own baseline confirmed
  (`2602 passed`, exit 0), then the identical plugin and the identical four seeds
- Expected: if the claim is true, failures at `9d819c1` too, and not the same ones
- Actual: **4, 2, 3 and 0 failures** — and **not one node ID overlaps** the
  `55878c9` set except `test_AC_F35_09_all_six_types_are_visible_and_none_is_preselected`,
  which fails at seed 1 there and seed 42 here
- Result: **The disclosure is ACCURATE.** This is a pre-existing limitation, not
  a pass-13 regression. On the same four seeds the failure count is **lower**
  after pass 13 (2/1/1/0 vs 4/2/3/0), though the collected sets differ by 62
  items so a seed does not produce the same ordering in both trees and the
  comparison is directional only.
- Evidence:
  ```
  9d819c1 seed 1  (4) test_ui_review.py::TestReachability::...[rejection-reasons]
                      test_ui_review.py::TestStructuredRejection::test_free_text_sits_underneath_the_list_rather_than_instead_of_it
                      tests/suites/ux/test_ux_flow.py::test_UX8_only_the_posting_capable_types_carry_a_posts_flag
                      test_ui_review.py::TestResolutionTyping::test_AC_F35_09_...
  9d819c1 seed 7  (2) test_ui_review.py::TestReachability::...[resolution-row]
                      test_ui_review.py::TestResolutionTyping::test_a_type_the_broker_does_not_allow_is_disabled_and_says_so_rather_than_being_absent
  9d819c1 seed 42 (3) test_emission_gate_criteria.py::test_AC_F36_29_an_emission_denial_and_an_action_denial_share_one_store
                      test_emission_gate_criteria.py::test_AC_F36_29_each_record_states_which_kind_it_denied_as_a_field_not_a_guess
                      test_f40_criteria.py::test_AC_F40_09_the_broker_decision_record_is_unchanged_by_the_failure
  9d819c1 seed 20260731 — 2602 passed
  ```

### Scenario: OD-3 — the class is what `code-agent` says it is
- Status: EXECUTED
- Input: the seed-1 failure text at `55878c9`
- Expected: accumulated process state other than the viewer session
- Actual: the two failures are (a) `no control event was recorded for a refused
  selection / assert []` — the control-event sink, which
  `tests/suites/conftest.py` resets autouse for suite scenarios but which
  `backend/tests` scenarios can consume or clear; and (b) `reject-submit is
  mounted nowhere on /review/ITEM-21400-CP` — the item was already disposed of by
  an earlier scenario, so the control is legitimately absent. Neither is the
  persona or the tier.
- Result: confirms the disclosure's characterisation (accumulated dispositions,
  workflow records, probe queue, control events)
- Evidence: `AssertionError: no control event was recorded for a refused
  selection / assert []`; `AssertionError: reject-submit is mounted nowhere on
  /review/ITEM-21400-CP / assert False`

**Verdict on the disclosure: ACCURATE. Recorded as a known limitation, not a
regression. It is nonetheless a real gap: it means the two trees are only
order-clean as whole blocks and file-reversed, not interleaved, and the fixture
isolation that would close it does not exist.**
