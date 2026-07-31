# Test evidence — deferred-substitution register cross-check

**Run date:** 2026-08-01 (Gate 8 · Test re-run, post-pass-5)
**Commit under test:** `dev` @ `b1b5dde`; project repo `6dae43e`
**Owner:** `test-agent`
**Status:** `EXECUTED` — every check below was run, none inferred from source reading alone
**Blocking:** yes

The standing question: **does any suite report a pass that the twenty-five-entry
deferred-substitution register says cannot be true?** Last pass it found three
contradictions. This pass it finds **none of that kind** — and two gaps of a
different, weaker kind (C2, C3 below).

This file REPLACES `register-cross-check-2026-07-31.md`, which was written
against a commit at which F26, F28, F9 and F33 did not exist.

---

## Per-scenario evidence

### Scenario: C0 — no scenario name claims a criterion the register says is unmet
- Input: every `def test_…` name in all six SME suites, reduced to the AC IDs embedded in them, checked against every ID the register marks unmet or not-verified
- Expected: `AC-REFUSAL-11`, `AC-F1-08`, `AC-F1-11`, `AC-F38-11`, `AC-F26-05` and `AC-F41-08` appear in **no** suite test-function name
- Actual: none of the six appears in any test-function name. Every one of them still appears in prose inside the suite files, and in every case the prose **denies** the criterion rather than claiming it.
- Result: PASS
- Evidence: IDs found in suite test names — `AC_F1_01`, `AC_F26_01…04`, `AC_F26_06…10` (note the absent `-05`), `AC_F28_01…10`, `AC_F29_01`, `AC_F29_05…11`, `AC_F33_01…12`, `AC_F38_02…08`, `AC_F38_15…17`, `AC_F42_01/04/06/07`, `AC_F9_01…09`. `AC-REFUSAL-11` appears six times in `test_adversarial.py`, all six denying it (lines 342, 354, 396, 430, 472, 543). `AC-F1-08` appears in `test_acceptance_criteria.py` only as "IS NOT COVERED BY THIS SUITE". `AC-F41-08` appears in `test_ux_flow.py` only as "DOES NOT SATISFY".

### Scenario: C1 — `AC-REFUSAL-11`'s battery, both halves, genuinely execute
- Input: `.venv/bin/python -m pytest -o addopts= tests/suites/red-team/test_adversarial.py -v -k RT05`
- Expected: eight parametrised refusals AND four parametrised pass-throughs, all collected and all run — not four scenarios silently deselected or reduced to a docstring
- Actual: 15 RT05 node IDs, all PASSED. The pass-through half is a real `@pytest.mark.parametrize` over `RT05_NOT_REFUSED`, one node per string.
- Result: PASS
- Evidence:
  ```
  test_RT05_each_paraphrase_in_this_fixed_battery_of_eight_is_refused_at_the_broker[...]  × 8 PASSED
  test_RT05_the_criterions_own_example_paraphrases_are_not_refused[$180K is not worth worrying about for a company this size, so leave it.]  PASSED
  test_RT05_the_criterions_own_example_paraphrases_are_not_refused[Is this normal for this account? Yes -- normal, and nothing to do.]         PASSED
  test_RT05_the_criterions_own_example_paraphrases_are_not_refused[Nobody would query a difference this size; pass it as is.]                  PASSED
  test_RT05_the_criterions_own_example_paraphrases_are_not_refused[Small enough to leave alone -- no adjustment recommended.]                  PASSED
  test_RT05_the_battery_avoids_the_vocabulary_the_criterion_excludes  PASSED
  test_RT05_the_structural_leg_holds_where_the_prose_leg_is_evaded    PASSED
  test_RT05_this_paraphrase_evades_A20_entirely_and_reaches_a_surface PASSED
  ```
  The first two pass-through strings are the criterion's own worked examples,
  verbatim from `FUNCTIONAL_SPEC` `AC-REFUSAL-11`. Both halves drive
  `emission_broker.decide_emission(...)` — the authorisation outcome, not
  `refusals.classify` — so this is the decision that actually gates a surface.
  The pass-through assertion carries a failure message forbidding a silent
  move of a string into the refused half.

### Scenario: C2 — register 24 (F33 peer thresholds uncalibrated) has **no witness in the suite**
- Input: `grep -rn "0.6667|calibrat|register 24|not a measured|skill accuracy" tests/suites/functional/ backend/app/f33/ backend/app/detectors/primitives/peer_coding_divergence.py backend/app/ui/pages.py`
- Expected: by the pattern pass 4d and pass 5 established for registers 6, 9, 18 and 20 — an explicit in-file statement that the figure is a fixture property
- Actual: two hits, both bare assertions of the literal: `test_f33_criteria.py:124 assert record.precision == "0.6667"` and `:398 assert "0.6667" in region`. No statement anywhere in the suite that `0.6667` is a property of a 163-posting synthetic fixture rather than a measured skill accuracy, and none that `min_peer_support=20` / `min_peer_agreement=0.8` are uncalibrated.
- Result: **FAIL (advisory finding — no suite reports a false pass)**
- Evidence: `test_AC_F33_06_the_backtest_reports_precision_recall_period_count_and_versions` is correctly named — it asserts what is *reported*. But `test_the_backtest_measures_a_detector_that_actually_ran` sits immediately beneath it, and `test_AC_F33_01_a_cost_centre_divergence_names_both_codings_and_its_evidence` asserts `finding["evidence"]["comparable_postings"] >= 20` — the uncalibrated threshold — as a criterion check. Nothing reads as *validating* accuracy, so this is not a contradiction of the C0 kind. It is the one register entry with a live misreading risk and no guard, where four comparable entries have one. **Mitigating, and it is real:** `test_AC_F33_09_the_no_labels_state_is_visible_on_the_exceptions_screen` asserts the `backtest-no-claim` panel renders, and the smoke test confirmed exactly one such panel on the served `/exceptions` — so a reader of the screen does meet the second held-out period with no labels, which is what register 24 says the screen is for.

### Scenario: C3 — register 25 (F9 history measured in movements, not close periods) has no witness either
- Input: read all three `test_AC_F9_05_*` scenarios in `tests/suites/functional/test_f9_criteria.py`
- Expected: as C2
- Actual: three scenarios claim the ID; none states that "periods present in the movements extract" substitutes for "periods of history", so an account dormant for a quarter reports as younger than it is
- Result: **FAIL (advisory finding)**
- Evidence: `AC-F9-05` as written — "an account with fewer than two periods of history … shows an explicit insufficient history state naming the periods available, and is not shown as monitored-and-clear" — **is** satisfied on this fixture, and the scenarios assert exactly that (`note["periods_available"] == [12]`, `minimum_required == 2`, not in the escalation list, visible on `/monitors`). Register 25 itself says the two cases cannot differ on the synthetic fixture. So this is weaker than C2: the claim is true, the substitution behind it is undisclosed at the site.

### Scenario: C4 — the four new detector families are driven by real runs, not fixture literals
- Input: read the fixtures of `test_f26_criteria.py`, `test_f28_criteria.py`, `test_f9_criteria.py`, `test_f33_criteria.py`; run all 96 functional scenarios
- Expected: every scenario reaches a real detector through the certified-query boundary
- Actual: every one of the four files builds a real `ges.warehouse.SqliteWarehouse`, wraps `ges.main.create_app` in a `TestClient` with `CONCLAVE_PROCESS_ROLE=ges` and a client token, and drives the detector through `app.ges_client.GesClient`. No scenario reads a dictionary from `pages.py`.
- Result: PASS
- Evidence: `boundary.run(manifests, detector_client, …)`, `fidelity.run(…)`, `surveillance.run(…)`, `f33.run(…)`. The gate-9 defect — `AC-F28-07` and `-10` rendering fixture literals — is closed at both ends: `test_AC_F28_07_a_missing_dataset_makes_one_check_not_run_and_the_other_four_report` drives `warehouse.seed(omit_objects=("fx_revaluation",))` and asserts `[r.code for r in run.not_run] == ["A9"]` with `"dw.fx_revaluation" in not_run[0].missing_datasets`; `test_AC_F28_07_a_check_that_did_not_run_carries_no_findings_list_at_all` asserts `a9.findings` **raises** and `"findings" not in a9.as_dict()`, so an unrun check cannot be confused with one that found nothing.

### Scenario: C5 — "not run" is a state a reader meets in the running pilot
- Input: the smoke test's `GET /exceptions` against the pilot on 8021
- Expected: the served screen carries a real `not_run`, produced by an object that genuinely does not exist
- Actual: 5 boundary-check rows, exactly 1 `not_run`, naming `dw.fx_revaluation`
- Result: PASS
- Evidence: `pilot_transport.PILOT_OMITTED_OBJECTS = ("fx_revaluation",)`, with a comment stating why an omitted object rather than an empty table. Confirmed served, not just tested. Full detail in `smoke-test-2026-08-01.md` S3.

### Scenario: C6 — the 45 `COVERS AC-…` joins are accurate against the criterion text
- Input: all 45 joins (24 distinct IDs, all in the unit suite: `test_abstention.py`, `test_refusal_registry.py`, `test_broker_emission_path.py`), sampled against `knowledge/FUNCTIONAL_SPEC.md`
- Expected: each join names an ID whose criterion text the scenario actually exercises
- Actual: 13 joins read in full across four IDs. **12 accurate, 1 over-broad.**
- Result: **PARTIAL**
- Evidence:
  - `AC-F36-34` (4 joins) — accurate. Criterion has two clauses; the joins are: the denial naming prior-period treatment as inadmissible (`reason == "grestate_prior_period_treatment_is_not_evidence"`), a negative control on a substantiated ground, the third-consecutive escalation routing to `AC-F36-11`, and the one-period-short boundary. The two clauses plus a control plus a boundary — a correct decomposition, not four restatements.
  - `AC-F36-37` (4 joins) — accurate. The criterion has a first group (certainty markers needing structured grounds) and a second (materiality markers denied unconditionally naming A20) and a closing sentence excluding explanation quality. All three are joined, one scenario each for `verified` and `confirmed`, and the closing-sentence scenario asserts a long careful narrative with no certainty marker is ALLOWed.
  - `AC-REFUSAL-08` (3 joins) — accurate, including the last clause ("prior reasoning may be presented as context … never as evidence of its own correctness") and the boundary that A23 is about the agent's OWN prior output.
  - **`AC-F36-47` (3 joins) — OVER-BROAD.** The criterion reads "*when every automation-rate and precision figure **on every screen, in every dossier and in every export** is read*". All three joined scenarios test `common.abstention` alone: `ab.quality_denominator(concluded=80, abstained=20) == 80`, `ab.rates(...)["abstained"] == 20`, and an AST reflection over that one module. `grep -rn "F36-47|abstentions_are_a_named_third_figure|quality_denominator" tests/suites/ backend/app/ui/` returns **nothing** — no screen, dossier or export scenario in any suite reads an automation-rate or precision figure with its abstention count beside it. The computation clause has three witnesses; the surface clause has none, and the join does not say so. **Gate 9 maps these joins mechanically, so this one would score `AC-F36-47` satisfied on evidence covering half of it.**

### Scenario: C7 — the five findings of the previous run were actually fixed, not renamed away
- Input: `git diff 8bc1224..HEAD` over test names, plus reading each replacement
- Expected: each replacement is equal or stronger
- Actual: all five addressed; two of the five produced genuinely stronger checks
- Result: PASS
- Evidence:
  1. `test_AC_F1_08_a_dossier_returns_complete_with_its_retention` removed; replaced by `test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp`, which additionally asserts `StubObjectLockArchive.has_retention_lock is False`. `AC-F1-08` is now claimed by no suite — the accurate reading.
  2. `test_RT05_a_materiality_conclusion_never_reaches_a_surface_however_phrased` removed; replaced by the two-half battery in C1 plus `test_RT05_this_paraphrase_evades_A20_entirely_and_reaches_a_surface`, which asserts `outcome == "allow"` and `reason is None` for the evasion. Strictly stronger.
  3. Trust boundary: `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket` and `test_ARCH_04_the_socket_is_authenticated_and_an_unheaded_caller_is_refused` both **PASSED**, not skipped — verified from the `-v` node list, so the real child process really bound. The residual (no suite can witness that an api-process module cannot `import ges.executor`) remains open as register 19 says.
  4. UX persona switch: `_as_controller` now asserts `[data-testid="persona-controller"][aria-current="true"]` count == 1 before anything depending on it, with a failure message naming the silent-staff-accountant failure mode.
  5. `test_UX12_the_three_failure_grammars_differ_in_words_with_styling_stripped` now produces UNAVAILABLE by cutting the transport, and asserts it differs in words from both others with styling stripped.

### Scenario: C8 — the removed test that most needed checking
- Input: `test_a_specified_but_unimplemented_primitive_says_so` was removed
- Expected: a coverage decision explained, not a silent drop
- Actual: replaced by two scenarios that are strictly stronger, and the trap was caught deliberately
- Result: PASS
- Evidence: pass 5 built the remaining nine of eleven specified primitives, so `SPECIFIED_BUT_NOT_IMPLEMENTED` is now `()` — and **a `@pytest.mark.parametrize` over an empty tuple collects zero tests and reports green**. The replacement `test_a_specified_but_unimplemented_primitive_still_says_so` monkeypatches a planted entry (`"hypothetical_twelfth"`) so the not-implemented behaviour is still asserted, and `test_all_eleven_specified_primitives_are_now_built` asserts the list is empty and that `set(SPECIFIED) == set(REGISTERED)`. Its docstring states the trap in terms: *"Emptying the list must not quietly remove the check that the list exists for."* This is the single best piece of evidence-honesty work in the diff.
