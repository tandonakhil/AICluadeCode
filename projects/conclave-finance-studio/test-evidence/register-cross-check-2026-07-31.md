# Test evidence — deferred-substitution register cross-check — 2026-07-31

**Project**: conclave-finance-studio · **Gate**: 8 · Test
**Run**: 2026-07-31, gate-8 verification run by `test-agent`
**Status**: `EXECUTED` — every finding below was produced by running code, not
by reading it.
**Question asked**: *does any suite report a pass that the 22-entry
deferred-substitution register says cannot be true?*

Every one of the 305 SME scenarios and 1,217 unit tests passed. This file
records where a **green scenario name overstates what the green proves**. No
finding below is a code defect discovered by re-running a passing test; each is
a *reporting* defect in which a scenario's name or ID mapping claims more than
its body establishes. That is the class this gate was asked to hunt, and it has
already appeared twice on this project.

---

### Scenario: register 3/4 — does any suite claim `AC-F1-11` is satisfied?
- Input: exhaustive grep for `AC-F1-11`, `retention_lock`, `is_stub`, `anchor`
  across `tests/suites/` and `backend/tests/`; then direct execution of the
  anchor and archive paths.
- Expected: no suite asserts a signed anchor or an applied retention lock.
- Actual: **no suite claims `AC-F1-11`.** The anchor and archive scenarios
  assert the *negative* and are correctly named for it —
  `test_ARCH_11_anchors_record_that_the_signer_is_a_stub`,
  `test_an_anchor_made_by_the_stub_signer_cannot_masquerade_as_signed`,
  `test_the_archive_stub_marks_every_object_as_unlocked`,
  `test_the_stubs_refuse_to_run_in_production`. `AC-F1-11` appears in **no**
  test file at all, so nothing maps a green to it.
- Result: PASS (no false claim)
- Evidence: executed probe —
  ```
  anchor before: STUB-UNSIGNED:c185d717e9103d23931c19e116 | stub: 1
  ```
  The signature is the literal prefix `STUB-UNSIGNED:` plus a digest, with no
  key material anywhere in it. Register 3's residual is confirmed executable:
  an attacker who rewrites the chain can also re-run `write_anchor` and obtain
  an anchor indistinguishable from the legitimate one, because producing one
  requires no secret. `retention_expiry` is a stamped ISO date
  (`backend/app/evidence/store.py:193`, `now.replace(year=now.year + 7)`) with
  nothing enforcing it; `has_retention_lock` is `False` and asserted `False`.

### Scenario: register 3/20 — `AC-F1-08` carries a green scenario in the functional suite
- Input: `tests/suites/functional/test_acceptance_criteria.py::test_AC_F1_08_a_dossier_returns_complete_with_its_retention`
- Expected (by its ID): `AC-F1-08` — a dossier retrievable complete at the
  oldest end of the retention window.
- Actual: the body asserts only that the required payload keys are non-`None`
  and that `stored["_evidence"]["retention_expiry"]` is **truthy**. It reads a
  date string out of a row it wrote seconds earlier. It does not exercise
  retrieval from an archive, does not advance a clock, and does not touch the
  object store — which register entry 20 records as **not existing** ("`AC-F1-08`'s
  oldest-end retrieval has no object store to retrieve from").
- Result: **PASS, but the name and criterion ID overclaim.**
- Evidence: full body is four assertions; `retention_expiry` implementation is
  `now.replace(year=now.year + retention_years).isoformat()`. A reader mapping
  suite scenarios to criteria will mark `AC-F1-08` satisfied. Registers 4 and 20
  say it is not. **This is a test that passes for a reason unrelated to its
  name.**

### Scenario: register 19 — would the architecture suite still pass if the trust boundary were gone?
- Input: `tests/suites/architecture/test_architecture_conformance.py::test_the_api_package_never_imports_the_ges_package`
  — the suite's only boundary check.
- Expected: a check that fails if the analysis/execution boundary collapses.
- Actual: it is a **static regex over the source text of `backend/app/`**
  (`re.compile(r"^\s*(from|import)\s+ges\b")`), with `run.py` exempted. It
  passes unchanged while the boundary is collapsed at runtime, because
  `backend/pilot_transport.py` sits **outside** the `app` package by design.
- Result: **PASS — and YES, it would still pass if the boundary were gone
  entirely.** It is a static-import check, its own docstring says so ("the
  runtime half is in `security`"), and it is doing exactly its job. The finding
  is that **the runtime half it defers to does not exist**.
- Evidence: the security suite's three runtime checks
  (`test_no_credential_resolves_from_a_process_declaring_itself_api`,
  `test_the_api_process_refuses_to_start_holding_a_credential`,
  `test_ges_refuses_to_start_unless_it_declares_itself_the_credential_holder`)
  spawn real subprocesses and are genuine — but they test the **credential**
  boundary, not the **process** boundary. They prove an api-role process cannot
  resolve a secret. Nothing anywhere proves an api-process module cannot
  `import ges.executor` and call it, which is precisely what register 19 says
  the pilot transport enables. And `backend/pilot_transport.py` deliberately
  does **not** set `CONCLAVE_PROCESS_ROLE`, so those three subprocess scenarios
  never run against the pilot configuration at all.

### Scenario: register 19 — is the loopback transport exercised by any suite?
- Input: grep for `GES_TRANSPORT` / `pilot_transport` / `loopback` across all
  suites.
- Expected: at least one suite drives the deployment transport.
- Actual: `pilot_transport.install()` is bound session-wide by
  `tests/suites/ux/conftest.py` and by `backend/tests/conftest.py`. The
  "loopback" appearing in the other five suites is a `TestClient` against the
  GES ASGI object carrying an `X-Ges-Client-Token` header — the HTTP *contract*
  and the token check are exercised; a real socket and a real second process
  are not.
- Result: **PASS, with the gap confirmed.** `tests/suites/ux/README.md` line 109
  already states "nothing in this suite exercises the loopback transport". That
  is true of every suite. No scenario anywhere runs the two-process topology.
- Evidence: grep output; `backend/pilot.py` header; `tests/suites/ux/README.md:109`.

### Scenario: register 9 — does the red-team suite report A20 as *partially* enforced?
- Input: `tests/suites/red-team/test_adversarial.py`, RT-05 block; and a direct
  probe of `Broker.decide_emission`.
- Expected: A20 reported as holding structurally and heuristically in prose,
  never as holding absolutely.
- Actual: **mixed, and the scenario NAME asserts the universal the register
  denies.** Eight of the nine RT-05 scenarios are
  `test_RT05_a_materiality_conclusion_never_reaches_a_surface_however_phrased`
  — *however phrased* — parametrised over eight fixed paraphrases. The ninth,
  `test_RT05_the_structural_leg_holds_where_the_prose_leg_is_evaded`, is the
  honest one, and its evasive string is the same string the unit test
  `test_the_prose_leg_is_evadable_and_here_is_a_paraphrase_that_evades_it`
  proves the prose leg misses — so it is **not** passing for an unrelated
  reason. But the demonstration of the evasion lives in the **unit** suite, not
  the red-team suite. A reader of the red-team suite's own output sees nine
  green lines, eight of them saying "however phrased".
- Result: **PASS, with A20 reported more strongly than register 9 permits.**
- Evidence: direct broker probe, four cases:
  ```
  A  evasive prose + treatment + substantiated ground -> allow   (reason=None)
  B  evasive prose + composition                      -> allow   (reason=None)
  C  evasive prose + treatment + magnitude ground     -> abstain  AB4:refused_by_design:A20
  D  battery phrase + treatment + substantiated       -> abstain  AB4:refused_by_design:A20
  ```
  **Case A is a working evasion that reaches a surface** — an emission the
  prose leg does not catch and the structural leg does not reach, because it
  declares a substantiated ground. The red-team suite tests case C (structural
  leg catches it) and case D (prose leg catches it). **It has no scenario for
  case A**, which is the actual open residual. A20 is enforced absolutely where
  a disposition carries a size-shaped ground, and not at all in the gap.

### Scenario: register 19 / UX — do the UX POST scenarios exercise what they claim?
- Input: re-introduced the pass-4 body-dropping bug in the harness via an
  external pytest plugin (repo unmodified) and re-ran all 186 UX scenarios.
- Expected: every scenario that claims to drive a control should fail when its
  body is discarded.
- Actual: **177 of 186 still passed. 9 failed**, all in
  `TestUX14ControllerNightOverMonitors`, because the persona switch is the only
  body-bearing POST the suite makes. The rest of the surface's POSTs
  (`approve-lines`, `run-submit`, refuse/reject) carry no form fields that
  change the outcome, so the fix is load-bearing for exactly one journey.
- Result: **PASS, with one scenario passing for a reason unrelated to its name
  — see next entry.**
- Evidence: 9 `FAILED` lines, all `TestUX14ControllerNightOverMonitors`.

### Scenario: `test_the_override_rate_is_visible_with_its_denominator` is insensitive to its own persona
- Input: that scenario alone, run with the persona-switch POST body dropped.
- Expected: it should fail — its docstring says "The journey CAUSES the
  decision first, by attempting an approval… that a controller can see what
  happened tonight", and it spends three lines becoming the controller.
- Actual: **`1 passed in 0.83s`.** The persona switch silently did not happen;
  the scenario ran as a staff accountant and every assertion still held
  (`write-failure` count 1, `data-overrides == "0"`), because the approval is
  denied under both personas and the override count is zero under both.
- Result: **PASS — for a reason unrelated to its name.** The scenario
  establishes nothing about the controller persona. Its sibling scenarios in
  the same class do genuinely depend on the switch (they assert
  `[aria-current="true"]`), which is why they failed and this one did not.
- Evidence:
  ```
  $ pytest ...::test_the_override_rate_is_visible_with_its_denominator -p dropbody
  1 passed in 0.83s
  ```

### Scenario: `test_UX12_the_three_failure_grammars_differ_in_words_with_styling_stripped` asserts two of three
- Input: read the rewritten scenario body.
- Expected (by its name and docstring): three grammars distinguished — REFUSED,
  INVALID, UNAVAILABLE.
- Actual: the body exercises **INVALID** (422, "not saved") and **REFUSED**
  (403, "a control refused this") and asserts they differ. **UNAVAILABLE is
  named in the docstring as "the one a reviewer must never read as a denial"
  and is never exercised.** It is covered elsewhere
  (`backend/tests/test_ui_governance_screens.py` cuts the transport), but not
  by the scenario named for it.
- Result: **PASS, name overclaims by one third.**
- Evidence: scenario body contains exactly two `asgi_client.post` calls; the
  string "could not be reached" appears only in a negative assertion.

### Scenario: register — did any test get replaced by something weaker?
- Input: `git diff 2ed6b4e..HEAD` over `backend/tests/` and `tests/suites/`.
- Expected: replacements assert something real.
- Actual: **8 test functions removed, all legitimately.** Six asserted the
  HTTP 501 deferred screen that pass 4 replaced with a real write path
  (`test_approving_returns_a_deferred_and_not_a_recorded_approval`,
  `test_it_says_the_authority_to_approve_is_not_held_by_this_process`,
  `test_no_approval_state_changes_as_a_result`,
  `test_recording_a_resolution_returns_a_deferred_not_a_success`,
  `test_the_refusal_uses_the_DEFERRED_grammar_not_the_refusal_grammar`,
  `test_it_names_what_is_missing`); one UX scenario
  (`test_approving_reaches_a_deferred_screen_and_records_nothing`) and one
  renamed/rewritten (`test_UX12_the_deferred_grammar_…`). Continuing to assert
  a 501 would be asserting the absence of the feature. Each removal names its
  replacement's destination in a docstring, and the destinations are real:
  `test_ui_write_path.py` (+736 lines) and `test_ges_decide_route.py`
  (+438 lines) assert against the store, not the confirmation message.
  What survived in place is the property that outlives the change — the write
  endpoints are POST-only, asserted by a 405 on GET.
- Result: PASS — no weakening.
- Evidence: `git diff --numstat`; 157 test functions added against 8 removed.
