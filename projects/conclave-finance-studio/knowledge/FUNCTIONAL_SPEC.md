# Functional Specification — conclave-finance-studio

**Gate 4 · Functional Design.** Author: `functional-design-agent`. Date: 2026-07-31.
**Status**: proposed under standing authorization (`batch_authorized`).
**Pass 1** — first run of this gate on this project. This file is a durable
knowledge base: it accumulates across features and enhancements, and it is what
`verification-agent` audits against at the Verification gate.

**Write set for this pass**: this file only. `PLAN.md`, `FEATURES.md`,
`PROJECT_CONTEXT.md` and `pipeline-state.json` are untouched. The Decisions Log
line is owed by the orchestrator after this gate.

Inputs read in full for this pass: `PLAN.md` (§7 backlog, §11 test criteria,
§9.2 assumptions, §3.1 obligations A–S), `PROJECT_CONTEXT.md` Decisions Log,
`INTAKE.md` (scope correction and product direction), `knowledge/DOMAIN_KB.md`
(§6.2, §9, §10.2–§10.5), `knowledge/INDUSTRY_KB.md` (§13.3, §14, §15.2–§15.4).
No `PRD.md` exists for this project.

---

## 0 · How to read this file

Each criterion is a **Given / When / Then** triple carrying a **stable unique
ID** in the form `AC-<feature-id>-<NN>`. The ID is the join key between this
specification and the evidence trail `verification-agent` audits. It is
load-bearing:

- **An ID, once issued, is never reused and never renumbered.** A deleted
  criterion is retired in place in §20 with a one-line note; later IDs are not
  shifted up to close the gap.
- If a criterion's meaning changes materially, a **new** ID is issued and the
  old one retired. The body under a fixed ID is never silently rewritten.
- Every criterion has exactly one ID; every ID appears exactly once.

Every **Then** clause states something observable from outside the code: what is
on a screen, what a file or payload contains, what was persisted, what was
refused, what state changed. No criterion asserts internal structure ("the
handler is registered", "the module imports X"). Where a criterion needs an
instrumented observation (e.g. counting model invocations during a run), it says
so and the observation is still external to the code under test.

**Scope**: the 17 features marked BUILD NOW in `PLAN.md` §7, plus §17 for the
A19–A22 refusal surface, which `PLAN.md` §7.6 records as a **stated design
property in approved scope**, not as a new feature. No feature is added,
removed, deferred or re-cut here — that is `plan-agent`'s lane.

**Not in this file**: layout, flow, spacing, colour, typography, animation,
component hierarchy or screen composition. Observable-UI criteria name *which
component must be visible, on which screen, in which state* and stop there.
Everything about how it looks or where it sits belongs to `ui-ux-designer` at
gate 5. This gate runs first so the designer designs against known required
behaviour.

**Terms used below**

| Term | Meaning as used in criteria |
|---|---|
| **run** | One immutable execution of a skill against a selected dataset set (`PLAN.md` §5.3). A new run supersedes; it never overwrites. |
| **declared expected population** | The population a skill declares it should cover (obligation R). |
| **coverage** | Selected population ÷ declared expected population, as a percentage. |
| **negative assurance** | Any conclusion of the form "no exceptions" / "clean". |
| **decision ID** | The broker's identifier for one policy evaluation (obligation N). |
| **bundle hash** | The content hash of the guardrail bundle in force (obligation L/N). |
| **rendered view** | The exact visual artefact the approver was shown, retained as evidence (obligation A). |
| **R1–R6** | Resolution types per `DOMAIN_KB` §10.2. |
| **CUEC** | Complementary user entity control — Oracle-side configuration we depend on but do not own (obligation S). |

**Screens referenced** (names from `PLAN.md` §6.2; naming is descriptive, and
`ui-ux-designer` owns the final information architecture): **Ask**, **Exceptions**,
**Review**, **Dispositions**, **Catalogue**, **Monitors**, **Inventory**,
**Audit**, **Refusals**.

---

## 1 · Completeness check — binding decisions this specification was checked against

Every binding decision in `PROJECT_CONTEXT.md`'s Decisions Log, in full, and how
this pass satisfies or conflicts with it.

| Binding decision | How this specification satisfies it |
|---|---|
| **2026-07-31 — SCOPE CORRECTION: the system is not the GL; do not imitate GL** | No criterion asserts GL behaviour. Nothing here specifies matching, statement ingestion, certification, period-close mechanics, balancing enforcement or chart-of-accounts control. F40's criteria terminate at an **export file** (`AC-F40-01`) and explicitly assert that no posting path exists (`AC-F40-02`). Every detector criterion is written against warehouse data with an ERP control extract as the tie-out side. |
| **2026-07-31 — PRODUCT DIRECTION part 1: research-driven backlog** | Criteria are written per feature as `PLAN.md` §7 cut them, each traceable to its A-number from `DOMAIN_KB` §10.3. No feature was invented and none was dropped. |
| **2026-07-31 — PRODUCT DIRECTION part 2: NL, skill-based, datasets selected, action under guardrails** | F39 §11 specifies the NL surface as a **parameteriser over certified queries** (`AC-F39-01`) with no free-form SQL path (`AC-F39-02`); F38 §10 specifies dataset selection with live coverage; F36 §9 specifies broker-side enforcement. |
| **2026-07-31 — MVP1 SCOPED TO ERP DATA ONLY** | No criterion requires a non-Oracle source. `AC-F29-09` and `AC-F42-03` require detectors to take a **declared population object**, which is the phase-2 seam `PLAN.md` §8 P1 asks MVP1 to leave open — specified as behaviour ("a run started without a declared expected population does not start"), not as code structure. |
| **2026-07-31 — STANDING AUTHORIZATION to build MVP1; trust SME judgement; make assumptions** | Calls made, not returned. §19 records where a criterion rests on one of `PLAN.md` §9.2's reversible assumptions. Two items are flagged as scope ambiguity in §21 and are **not** resolved here. |
| **2026-07-30 — Product shape: BOTH (pre-built agents and a builder)** | The builder is F16, deferred by `PLAN.md` §7.5. No criteria are written for it, and none are written that would make it harder to add: nothing here assumes skills are a fixed set. |
| **2026-07-30 — Personas: all three** | Staff accountant: F41, F29, F33, F40 criteria. Controller: F9, F32, F12, F36 blast-radius, F1 export criteria — `AC-F9-08`, `AC-F12-08`, `AC-F36-19` are explicitly controller-facing. FP&A: F39's inquiry criteria (`AC-F39-01`, `AC-F39-05`, `AC-F39-07`). Coverage remains partial for FP&A because F45 is deferred; that is `PLAN.md` §7.7's open conflict, carried forward unresolved, not re-decided here. |
| **2026-07-30 — Write-back with per-action approval ("the defining decision")** | `AC-F40-03` makes export impossible without a per-action in-product approval. `AC-F41-01` forbids an "approve all" affordance at every permission level. `AC-F40-05`/`AC-F40-06` specify the two-key model, with the in-product leg as the evidence-bearing one. |
| **A7.2 (worst harm) delegated to SMEs** | Answered by `DOMAIN_KB` §6.2 and specified as F9 §5 (both legs, `AC-F9-01` and `AC-F9-03`), F32 §7, and F36's blast-radius criteria `AC-F36-09`–`AC-F36-13`. |
| **A8.3 (MVP slice) delegated to SMEs** | Settled at gate 3. Not re-opened. |
| **Three surfaces → `solution-architect` non-droppable** | Honoured by omission: no criterion here is written against a mobile surface, because F23/F24 are deferred (`PLAN.md` §9.2 A2). `AC-F36-03` is written so that enforcement is asserted at the broker and therefore inherited by any surface added later, without this file naming a surface. |
| **`responsible-ai-architect` effectively non-droppable; owns the §15.4 anti-recommendation** | Binding on F41. **No criterion in §12 asserts explanation quality, clarity or legibility.** F41's criteria are volume (`AC-F41-09`), override rate (`AC-F41-07`), riskiest-element prominence (`AC-F41-03`) and probes (`AC-F41-08`). §12's preamble records this as a deliberate exclusion so a later gate cannot read it as an omission. |
| **Full roster, 14 agents. Test Policy: all suites blocking, no advisory exceptions** | Every criterion is written to be checkable by a suite or by named evidence. No criterion is written that the build cannot pass; §21 flags the one place I could not fully specify. |
| **Approval-under-pressure (A3.2)** | F41 §12 in full, plus `AC-F41-12` (approval on a superseded run is blocked), which is the 11pm failure `DOMAIN_KB` §5.3 predicts. |
| **Scope is very wide — the MVP slice is the mitigation** | 17 features specified, no eighteenth introduced. §17's refusal criteria carry a non-feature prefix precisely so they cannot be miscounted as a new backlog item. |

**Conflicts**: none contradicted. One carried forward unresolved — FP&A persona
coverage, which is `PLAN.md` §7.7's conflict and belongs to `plan-agent`.

---

## 2 · Cross-cutting conventions the criteria rely on

Stated once so they need not be repeated in every criterion. These are
restatements of decisions already binding, not new requirements.

- **C1 — "Then" clauses about output surfaces mean all three.** Where a
  criterion says an output must state something, and the feature emits to a
  screen, a dossier and an export, the assertion holds in all three unless the
  criterion names one.
- **C2 — Silence is never a pass.** Any check that could not run reports *not
  run*; it never reports clean, zero, or nothing at all. This appears as an
  explicit error-case criterion per feature because `PLAN.md` §2b is emphatic
  that a control that cannot fail trains its reviewer that the dashboard cannot
  fail.
- **C3 — An empty result is a stated result.** Zero findings renders as an
  explicit zero-finding statement carrying its coverage, never as a blank region
  and never as an indefinite spinner.
- **C4 — Approval attaches to a specific run.** A superseding run invalidates a
  prior approval loudly (`PLAN.md` §5.3).

---

## 3 · F26 — Warehouse-to-ERP fidelity + feed staleness (A1, A2)

Band D. Contains no AI, by design. Obligations C, Q.

### AC-F26-01
- **Given** a warehouse fixture seeded with a known set of divergences from the ERP control extract
- **When** an F26 fidelity run completes over the full declared population
- **Then** the run output lists exactly that seeded set of divergences — no additional items and no omitted items — and each listed divergence names the account, the amount of the difference and its direction

### AC-F26-02
- **Given** the same completed F26 run
- **When** its output is read
- **Then** each divergence is attributed to a balance, a segment value and a period, and the run also reports the totals it compared on each side (warehouse and ERP control extract)

### AC-F26-03
- **Given** a warehouse fixture that ties exactly to the ERP control extract
- **When** an F26 run completes at 100% coverage
- **Then** the output states zero divergences across the named population and its coverage, on the Exceptions screen and in the dossier — it is not blank, not a spinner, and not an absent result

### AC-F26-04
- **Given** a fixture in which one scheduled load batch never arrived
- **When** the F26 A2 (staleness/completeness) leg runs
- **Then** the output names the missing batch, its expected arrival, and the population it would have contributed

### AC-F26-05
- **Given** a fixture whose warehouse refresh is older than the current close-clock checkpoint
- **When** the F26 A2 leg runs
- **Then** the staleness is expressed relative to the close clock (for example "refreshed before day-2 cut-off; data is one close-day behind") and not as an absolute timestamp alone

### AC-F26-06
- **Given** an ERP control extract that is unavailable or failed to produce
- **When** an F26 run is attempted
- **Then** the run reports that it could not execute and names the missing control extract, and it does **not** report zero divergences or any coverage figure implying a comparison occurred

### AC-F26-07
- **Given** an instrumented harness that counts model invocations attributable to a run
- **When** a complete F26 run executes over a seeded fixture
- **Then** the observed model-invocation count for that run is zero

### AC-F26-08
- **Given** a fixture in which a single divergence equals the smallest reportable currency unit for the ledger currency
- **When** an F26 run completes
- **Then** that divergence is reported, and its amount is reported exactly, not rounded to zero

### AC-F26-09
- **Given** a fixture with one divergence in the earliest in-scope period and one in the latest in-scope period
- **When** an F26 run completes
- **Then** both are reported, each attributed to its own period

### AC-F26-10 — observable UI
- **Given** a signed-in user and a completed F26 run that found at least one divergence
- **When** they open the Exceptions screen
- **Then** the F26 fidelity findings are visible in the exception list, each showing its account, difference amount, period and the run's coverage statement

---

## 4 · F28 — The five remaining boundary checks (A6, A7, A8, A9, A10)

Band D. Contains no AI, by design. Obligations C, Q, R.

### AC-F28-01
- **Given** a fixture with a seeded break between a subledger and its GL control account (A6)
- **When** an F28 run completes
- **Then** the A6 check reports failed and names the control account, the subledger, and the difference amount

### AC-F28-02
- **Given** a fixture with a seeded intercompany pair imbalance (A7)
- **When** an F28 run completes
- **Then** the A7 check reports failed and names both entities, the pair, and the imbalance amount and direction

### AC-F28-03
- **Given** a fixture in which an account's opening balance does not equal the prior period's closing balance (A8)
- **When** an F28 run completes
- **Then** the A8 check reports failed and names the account, entity, the two periods and the discontinuity amount

### AC-F28-04
- **Given** a fixture in which FX revaluation has been applied twice to the same population (A9)
- **When** an F28 run completes
- **Then** the A9 check reports failed and names the affected accounts and the duplicated revaluation amount

### AC-F28-05
- **Given** a fixture with a suspense/clearing residual above the account's policy threshold (A10)
- **When** an F28 run completes
- **Then** the A10 check reports failed, names the account and the residual balance, and states the threshold in force

### AC-F28-06
- **Given** a fixture in which all five boundary checks are clean
- **When** an F28 run completes at 100% coverage
- **Then** the output names all five checks individually with a clean result and its coverage for each — a check that produced no finding is still listed, not omitted

### AC-F28-07
- **Given** a fixture in which the dataset required by exactly one of the five checks is missing
- **When** an F28 run completes
- **Then** that check reports **not run** with the missing dataset named, the other four report their results, and the run's overall conclusion is not stated as clean

### AC-F28-08
- **Given** an instrumented harness that counts model invocations attributable to a run
- **When** a complete F28 run executes over a seeded fixture
- **Then** the observed model-invocation count for that run is zero

### AC-F28-09
- **Given** an F28 A10 result of any kind
- **When** the result is read on any surface
- **Then** it states that the check covers the residual **balance** only and makes no claim about the residual's composition

### AC-F28-10 — observable UI
- **Given** a signed-in user and a completed F28 run with at least one failed boundary check
- **When** they open the Exceptions screen
- **Then** the five boundary checks are each visible with an individual result state (failed, clean, or not run), and the failed check's detail is reachable from that list

---

## 5 · F29 — Omission detector family (A5+) — **the wedge**

Obligations C, Q, R, G, I. This is the product's headline claim: it detects what
did *not* happen.

### AC-F29-01
- **Given** a fixture in which a recurring accrual posted in periods 1–11 and is absent in period 12
- **When** an F29 run completes over period 12
- **Then** an omission finding is reported naming the expected entry, the eleven periods in which it posted, the expected amount range derived from that history, and the period in which it is missing

### AC-F29-02
- **Given** a fixture containing a journal flagged for scheduled reversal in the following period, where no reversal posted
- **When** an F29 run completes over the following period
- **Then** an omission finding is reported naming the original journal, its expected reversal period and the unreversed amount

### AC-F29-03
- **Given** a fixture in which an interface feed stopped delivering and the entry it drove silently stopped posting
- **When** an F29 run completes
- **Then** an omission finding is reported naming the stopped feed, the last period it delivered, and the entry that consequently did not post

### AC-F29-04
- **Given** a fixture containing an intercompany transaction posted by one entity with no counterparty posting
- **When** an F29 run completes
- **Then** an omission finding is reported naming both entities, the posted side, the missing side and the amount

### AC-F29-05
- **Given** an account whose history contains fewer periods than the expectation model's declared minimum
- **When** an F29 run covers that account
- **Then** the run reports that account as **not evaluable — insufficient history**, naming the periods available and the minimum required, and does **not** report it as having no omissions

### AC-F29-06
- **Given** a fixture in which the recurring entry posted in periods 1–11 and also posted in period 12 within its historical amount range
- **When** an F29 run completes over period 12
- **Then** no omission finding is raised for that entry

### AC-F29-07
- **Given** a fixture in which the recurring entry posted in period 12 but at an amount far outside its historical range
- **When** an F29 run completes over period 12
- **Then** F29 raises no omission finding for that entry (the entry is present; an amount outlier is F42's population, per `PLAN.md` §7.4)

### AC-F29-08 — **the wedge test, F29 side**
- **Given** the shared period-12 omission fixture used by `AC-F42-04` (a recurring entry present in periods 1–11, absent in period 12), with both detectors run over the identical dataset selection and identical declared population
- **When** the F29 run completes
- **Then** the F29 output contains an omission finding for that entry — and the paired result required by `AC-F42-04` (F42 finding nothing) is reported alongside it as a single comparison result naming both detector runs

### AC-F29-09
- **Given** a request to start an F29 run for which no declared expected population is resolvable
- **When** the run is submitted
- **Then** the run does not start, and the response names the missing declared expected population as the reason

### AC-F29-10
- **Given** an F29 run whose underlying dataset becomes unavailable before the run completes
- **When** the run terminates
- **Then** the run is recorded as **incomplete** with the point of failure named, and it emits no omission conclusion of any kind — including no statement that no omissions were found

### AC-F29-11
- **Given** a completed F29 run over a fixture containing at least one omission
- **When** the finding is read on any surface
- **Then** it carries a dossier reference and the run's coverage statement

### AC-F29-12 — observable UI
- **Given** a signed-in user and a completed F29 run that found at least one omission
- **When** they open the Exceptions screen
- **Then** the omission findings are visible in the exception list, each labelled as an omission (distinct from a present-anomaly finding) and showing the expected-entry history that grounds it

---

## 6 · F9 — Cross-period surveillance, two mandatory legs

Obligations G, I. `DOMAIN_KB` §7.2.4: if exactly one safety mechanism survives
scoping, this is it. Both legs are mandatory; the narrative leg is named
separately so it cannot be dropped as an implementation detail.

### AC-F9-01
- **Given** a seeded twelve-period sequence on one account — same direction, each period's movement below the account's threshold, aggregating to a material amount
- **When** F9's numeric accumulation leg runs each period in sequence
- **Then** an escalation is raised before period twelve, and the period number at which it escalated is recorded and displayed as a headline result on the escalation record

### AC-F9-02
- **Given** an F9 numeric escalation on that sequence
- **When** the escalation is read on any surface
- **Then** it presents the iron-curtain aggregate across the accumulated periods as its primary figure, and the single-period delta is not presented as the headline figure

### AC-F9-03
- **Given** a seeded sequence in which each period's explanation materially restates the prior period's, and in which the numeric leg has **not** tripped
- **When** F9's narrative recurrence leg runs
- **Then** an escalation is raised on the narrative leg alone, naming the periods whose explanations recur and quoting the recurring assertion

### AC-F9-04
- **Given** any F9 escalation, numeric or narrative
- **When** the escalation is raised
- **Then** the account's risk grade is observably raised and its auto-pass eligibility is observably revoked (an R6 control-state change readable on the account), rather than only a notification being emitted

### AC-F9-05
- **Given** an account with fewer than two periods of history
- **When** the Monitors screen is opened for that account
- **Then** the account shows an explicit **insufficient history** state naming the periods available, and is not shown as monitored-and-clear

### AC-F9-06
- **Given** two fixtures identical except that one reaches the configured consecutive-period count for escalation and the other stops one period short
- **When** F9's numeric leg runs over each
- **Then** the first escalates and the second does not, and the second's record states how many further periods would trigger escalation

### AC-F9-07
- **Given** a sequence of sub-threshold movements on one account that alternate in direction and do not accumulate
- **When** F9's numeric leg runs
- **Then** no escalation is raised

### AC-F9-08 — observable UI
- **Given** a signed-in controller and at least one open F9 escalation
- **When** they open the Monitors screen
- **Then** the cross-period escalations are visible in a list, each showing the account, the iron-curtain aggregate, the period at which it escalated, and which leg (numeric or narrative) raised it

### AC-F9-09
- **Given** a sequence in which one or more prior-period explanations were never recorded
- **When** F9's narrative leg runs over that sequence
- **Then** the narrative leg reports **not evaluable** for the periods with missing explanations, naming them, and does not report the sequence as clean

---

## 7 · F35 — Resolution typing R1–R6 as first-class outcomes

Obligations A, G, I. `DOMAIN_KB` §10.2: R2 and R5 are the majority outcome.

### AC-F35-01
- **Given** a signed-in user with an open flagged item on the Review screen
- **When** they attempt to close the item without selecting a resolution type
- **Then** the close does not complete, the item remains open, and the response names the missing resolution type as the reason

### AC-F35-02
- **Given** a user closing an item as **R1 — accepted and explained**
- **When** they submit without an expiry date
- **Then** the close does not complete and the item remains open

### AC-F35-03
- **Given** a user closing an item as **R5 — handoff**
- **When** they submit without both a named owner and a due date
- **Then** the close does not complete and the item remains open

### AC-F35-04
- **Given** a user closing an item as **R6 — control-state change**
- **When** the close completes
- **Then** the affected account's risk grade and auto-pass eligibility are observably changed, and an audit record of that change exists carrying the closing user and timestamp

### AC-F35-05
- **Given** an open flagged item on the Review screen
- **When** a user records it as **R2 (data-side fix)** or **R5 (handoff)**
- **Then** the close completes with no posting artefact produced, and reaching completion for R2 and R5 requires no more user interactions than reaching completion for R3 or R4 — the safe outcome is not more effortful to record than the posting outcome

### AC-F35-06
- **Given** an item closed as R1 whose expiry date has passed
- **When** the next period's run covers that account
- **Then** the item is observably re-opened and appears again in the exception queue, labelled as a lapsed R1 with its original explanation attached

### AC-F35-07
- **Given** a signed-in user and a period in which no dispositions are open
- **When** they open the Dispositions screen
- **Then** an explicit zero-open-items state is visible naming the period, not a blank region and not a spinner

### AC-F35-08
- **Given** a user closing an item where persisting the disposition fails
- **When** the failure occurs
- **Then** the item remains open, no partial disposition record exists, and the failure is shown to the user

### AC-F35-09 — observable UI
- **Given** a signed-in user with at least one open flagged item
- **When** they open the Review screen for that item
- **Then** a resolution-type control offering all six types R1–R6 is visible, with no type pre-selected

---

## 8 · F12 — Disposition and review-precision capture (the ground-truth factory)

Obligations A, G. `DOMAIN_KB` §10.9(3): not telemetry — the only source of
labels any phase-2 accuracy claim can be tested against.

### AC-F12-01
- **Given** any item closed by any means, at any permission level
- **When** the closure record is read
- **Then** it carries exactly one resolution type from R1–R6; a closed item with no resolution type does not exist in the store

### AC-F12-02
- **Given** a user who opened a flagged item and later closed it
- **When** the capture record is read
- **Then** it contains the elapsed time between the item being presented and the disposition being submitted

### AC-F12-03
- **Given** a review in which the user expanded some evidence elements and left others collapsed
- **When** the capture record is read
- **Then** it names which evidence elements were expanded and which were not

### AC-F12-04
- **Given** a review in which the user exercised a sanctioned override
- **When** the capture record is read
- **Then** it records the override, its reason code, and the broker decision ID for the overridden evaluation

### AC-F12-05
- **Given** an injected known-error probe presented in a review queue
- **When** the reviewer disposes of it
- **Then** the capture record identifies the item as a probe, records the reviewer's response and whether that response was correct, and the probe is not distinguishable from a genuine item by anything visible on the Review screen before disposition

### AC-F12-06
- **Given** a period in which no items were closed
- **When** the F12 capture report for that period is produced
- **Then** it states zero labels produced for the named period, rather than being absent or empty

### AC-F12-07
- **Given** a close action whose capture write fails
- **When** the failure occurs
- **Then** the close does not complete, the item remains open, and the failure is shown — a disposition is never recorded without its label

### AC-F12-08 — observable UI
- **Given** a signed-in controller and a period containing at least one disposition and one probe
- **When** they open the Monitors screen
- **Then** override rate per agent, per user and per period is visible, alongside the probe results for that period

### AC-F12-09
- **Given** any permission level, including administrator
- **When** the review surfaces are inspected for a control that disposes of more than one item in a single action
- **Then** no such control exists on any surface and no API call accepts more than one item per disposition submission

---

## 9 · F36 — Guardrail engine + action broker

Obligations B, E, F, J, L, M, N, O, P. Enforcement lives at the broker; the UI
is never an enforcement point.

### AC-F36-01
- **Given** a guardrail bundle whose capability allowlist does not include the action "propose accrual"
- **When** an agent requests that action through the broker
- **Then** the action is denied, and the denial record names the action, the bundle hash, a decision ID and the allowlist as the reason — the denial does not depend on the action being named in any prohibition list

### AC-F36-02
- **Given** any action the broker permitted
- **When** the action's record is read
- **Then** it carries both the guardrail bundle hash and the policy decision ID; an action record lacking either does not exist

### AC-F36-03
- **Given** an action that the front end would not offer
- **When** the same action is requested by a direct API call that bypasses the front end entirely
- **Then** the broker denies it and produces a denial record identical in kind to the one produced through the front end, including the same bundle hash and a decision ID

### AC-F36-04
- **Given** a running system
- **When** an Oracle credential is requested from any module or agent context other than the broker
- **Then** no credential is returned and the attempt is recorded as a control event

### AC-F36-05
- **Given** the guardrail bundle currently in force
- **When** the scheduled negative-control suite runs against that live bundle
- **Then** it reports, per rule, the result of a fixture that makes the rule fire and a fixture that makes it not fire; a rule with either fixture missing is reported by name as **unevidenced** and the suite result is a failure

### AC-F36-06
- **Given** a close period in which many rules were evaluated and did not fire
- **When** the action log for that period is read
- **Then** it contains one record per attempted action and contains no records asserting that a rule did not fire — operating effectiveness is evidenced by `AC-F36-05`'s suite, not by logging non-events

### AC-F36-07
- **Given** a denied action for which a sanctioned override is available
- **When** an override is created
- **Then** it requires two distinct authorising identities, a reason code selected from a closed list, and it applies to exactly one action — a second attempt at the same action requires a new override

### AC-F36-08
- **Given** any permission level, including administrator
- **When** an override is created with no expiry, or with a scope broader than a single action
- **Then** the creation is rejected and no standing exemption exists in the store

### AC-F36-09
- **Given** a per-run proposal-count cap of N and a run that would produce N+1 proposals
- **When** the run reaches the cap
- **Then** the run stops producing proposals, the cap trip is recorded as a state change on the run with a decision ID, and the run's output states that it was capped and how many proposals were suppressed

### AC-F36-10
- **Given** a per-period aggregate-value cap and a sequence of individually compliant proposals whose cumulative value crosses it
- **When** the crossing proposal is evaluated
- **Then** it is denied, and the denial record states the cumulative period value and the cap

### AC-F36-11
- **Given** two prior periods each carrying an accepted proposal on the same account in the same direction
- **When** a third consecutive such proposal is evaluated
- **Then** it is escalated rather than permitted silently, and the escalation record names all three periods

### AC-F36-12
- **Given** a proposal whose value exceeds the configured proportion of the target account's balance
- **When** it is evaluated
- **Then** it is denied, and the denial record states the proposal value, the account balance and the proportion cap

### AC-F36-13
- **Given** any permission level, including administrator
- **When** a blast-radius cap is edited toward disabled, removed, or set to an unbounded value through any surface or API
- **Then** the change is rejected and the caps remain in force

### AC-F36-14
- **Given** a new guardrail rule introduced in shadow mode
- **When** an action that the rule would block is evaluated
- **Then** the action proceeds and a record exists stating that the shadow rule would have blocked it, naming the rule

### AC-F36-15
- **Given** a guardrail bundle in force with a known hash
- **When** any rule in it is edited and the bundle re-issued
- **Then** the new bundle has a different hash, the prior bundle remains retrievable at its own hash, and a change record exists naming the rule, the change, the owner and the effective-date range

### AC-F36-16
- **Given** a quantitative guardrail with a threshold of exactly T
- **When** three proposals valued at T minus the smallest currency unit, exactly T, and T plus the smallest currency unit are evaluated
- **Then** each produces a decision record, and the outcomes at the boundary are consistent with the threshold's stated inclusivity as displayed to the user at approval time

### AC-F36-17
- **Given** a system in which the guardrail bundle cannot be resolved or its hash does not verify
- **When** any action is requested
- **Then** every action is denied, and the denial names the unresolvable bundle — the system fails closed

### AC-F36-18 — observable UI
- **Given** a signed-in approver viewing a proposal on the Review screen
- **When** the screen is displayed
- **Then** the applicable threshold and the guardrail bundle version in force are visible on that screen, and where the proposal was denied and is override-eligible, an override control requiring a second authoriser and a closed-list reason code is visible

### AC-F36-19
- **Given** a signed-in controller and an agent that exercised no overrides during the period
- **When** they open the Monitors screen
- **Then** that agent's override rate is visible as an explicit zero for the named period, not omitted and not blank

---

## 10 · F38 — Certified dataset catalogue + coverage

Obligations C, Q, R. `INDUSTRY_KB` §14: dataset selection is a control failure,
not user error, and **under-selection is the failure that bites**.

### AC-F38-01
- **Given** a dataset that has been certified
- **When** a signed-in user opens it on the Catalogue screen
- **Then** its source lineage, as-of timestamp, refresh status, row count, content hash, ERP tie-out result and date, certifying owner and version are all visible on that screen

### AC-F38-02
- **Given** a skill with no declared expected population
- **When** a run of that skill is submitted
- **Then** the run does not start and the response names the missing declared expected population

### AC-F38-03
- **Given** a skill whose declared expected population is known, and a dataset selection covering 70% of it
- **When** the run completes
- **Then** the run reports coverage of 70% and names the portions of the declared population that were not scanned

### AC-F38-04
- **Given** a run at 70% coverage that found no exceptions
- **When** its result is read on screen
- **Then** the conclusion states that no exceptions were found in the scanned 70% and names what was missing; no wording asserting "no exceptions", "clean", or an unqualified all-clear is rendered anywhere on that result

### AC-F38-05
- **Given** the same 70%-coverage clean run
- **When** its dossier is read
- **Then** the dossier's conclusion is qualified by the same coverage figure and the same named gaps, and contains no unqualified negative assurance

### AC-F38-06
- **Given** the same 70%-coverage clean run
- **When** its export is read
- **Then** the export's conclusion is qualified by the same coverage figure and the same named gaps, and contains no unqualified negative assurance

### AC-F38-07
- **Given** two runs of the same skill over the same period, one at 100% coverage and one at 70%, both finding no exceptions
- **When** the two results are compared on screen, in the dossier and in the export
- **Then** they are textually different in every one of the three, and the difference names the coverage and the missing portions — results that are identical are a failure of this criterion

### AC-F38-08
- **Given** a skill whose selected datasets cover 0% of its declared expected population
- **When** the run is submitted
- **Then** the run does not produce a findings conclusion at all; it reports 0% coverage and that nothing was scanned

### AC-F38-09
- **Given** an action-capable or assurance-emitting skill and a selection that includes an uncertified dataset
- **When** the run is submitted
- **Then** the run is refused, the refusal names the uncertified dataset, and the refusal is recorded as a control event

### AC-F38-10
- **Given** an uncertified dataset selected in the exploration tier
- **When** the selection is displayed and while any result derived from it is displayed
- **Then** a state reading, in substance, "not certified — cannot support a posting or a no-exceptions conclusion" is visible, and no control exists that dismisses or hides it

### AC-F38-11
- **Given** any emitted figure on any surface derived from a dataset
- **When** the figure is displayed
- **Then** its dataset version, provenance and staleness relative to the close clock are visible on the same surface as the figure, not only in the underlying payload

### AC-F38-12
- **Given** a dataset whose ERP tie-out most recently failed
- **When** it is viewed on the Catalogue screen and when an action-capable skill attempts to use it
- **Then** the Catalogue shows the failed tie-out with its date, and the action-capable run is refused naming the failed tie-out

### AC-F38-13
- **Given** a tenant in which no dataset has yet been certified
- **When** a signed-in user opens the Catalogue screen
- **Then** an explicit no-certified-datasets state is visible explaining that action-capable and assurance-emitting skills cannot run, not a blank list

### AC-F38-14 — observable UI
- **Given** a signed-in user on the Ask screen who has selected one or more datasets for a skill with a declared expected population
- **When** the selection changes
- **Then** a coverage meter is visible on the Ask screen showing the current coverage percentage against the declared population, and it updates to reflect each change before the run is submitted

### AC-F38-15 — observable UI
- **Given** a completed run below 100% coverage
- **When** the user views its result on screen
- **Then** a partial-run banner is visible on the result, stating the coverage figure and that the run cannot support a no-exceptions conclusion

---

## 11 · F39 — Certified semantic/metric layer + NL skill interface

Obligations Q, R, I. **No free-form SQL in MVP1**: natural language selects and
parameterises a certified query; it never authors one.

### AC-F39-01
- **Given** a signed-in user who has typed a natural-language request on the Ask screen
- **When** the request is resolved
- **Then** the certified query it resolved to is named on screen together with the bound parameter values, and the run cannot be submitted before that resolution is displayed

### AC-F39-02
- **Given** a request engineered so that the model emits a SQL string
- **When** that string reaches the execution path
- **Then** it is not executed, the attempt is denied, and the denial is recorded as a control event naming the attempted execution

### AC-F39-03
- **Given** a natural-language request that cannot be mapped to any certified query or metric
- **When** it is submitted
- **Then** the response states that it cannot be answered from the certified layer and names what is missing (the metric, join, or dataset), and no approximate or best-effort answer is produced

### AC-F39-04
- **Given** any answer produced through the semantic layer
- **When** it is displayed and when its dossier is read
- **Then** the version of each certified metric and join used is stated

### AC-F39-05
- **Given** a certified query that returns zero rows over the declared population
- **When** the run completes
- **Then** the answer states zero rows over the named population together with the run's coverage — it does not render blank and it does not assert that the population is clean

### AC-F39-06
- **Given** a warehouse that is unreachable
- **When** a natural-language request is submitted
- **Then** the response states that the data source is unreachable, names it, and returns no figure — no cached or partial answer is presented as current

### AC-F39-07
- **Given** a natural-language request that maps equally well to two or more certified queries or metrics
- **When** it is resolved
- **Then** the candidates are named on screen and the user must choose before the run is submitted; the system does not select one silently

### AC-F39-08
- **Given** a request naming a period outside the range covered by the certified dataset
- **When** it is submitted
- **Then** the request is refused and the refusal states the range the certified dataset actually covers

### AC-F39-09 — observable UI
- **Given** a signed-in user on the Ask screen
- **When** the screen is displayed
- **Then** a natural-language input, a dataset selector, the resolved certified-query name (once resolved) and the coverage meter are all visible on that screen

---

## 12 · F41 — Risk-graded review and approval surface (desktop web)

Obligations A, B, F, O.

**Deliberate exclusion, binding at gate 5 and gate 8.** `INDUSTRY_KB` §15.4:
clearer AI explanations make reviewers defer **more**, not less. **No criterion
in this section asserts explanation quality, clarity, readability or narrative
legibility, and none may be added.** F41 is specified on volume, override rate,
prominence of the riskiest element, and probes. A later gate reading this section
as incomplete because it does not require good explanations has misread it.

### AC-F41-01
- **Given** any permission level, including administrator, and a queue containing many pending proposals
- **When** every review surface is rendered and inspected
- **Then** no control exists that approves more than one proposal in a single action, on any screen, at any permission level

### AC-F41-02
- **Given** a newly presented proposal
- **When** the Review screen is rendered
- **Then** the proposal's state is not-approved, and no approval control is pre-selected, pre-checked or pre-filled

### AC-F41-03
- **Given** a proposal for which the system has ranked one element as the riskiest (for example the largest-value line, or the segment with the widest blast radius)
- **When** the Review screen is rendered
- **Then** that element is rendered outside any collapsed or expandable region and appears ahead of the proposal's supporting narrative in the reading order — it is never reachable only by expanding something

### AC-F41-04
- **Given** an approver who approved a proposal
- **When** the stored rendered view for that approval is retrieved
- **Then** it reproduces what was displayed at approval time, including the figures, the threshold and the bundle version, and it is retrievable independently of the underlying data having since changed

### AC-F41-05
- **Given** a proposal awaiting approval
- **When** the Review screen is rendered
- **Then** the applicable threshold and the guardrail bundle version in force are both visible on that screen at approval time

### AC-F41-06
- **Given** an approver rejecting a proposal
- **When** they submit the rejection without selecting a structured reason from the closed list
- **Then** the rejection does not complete and the proposal remains pending

### AC-F41-07 — observable UI
- **Given** a signed-in controller and a period containing approvals, rejections and overrides
- **When** they open the Monitors screen
- **Then** override rate and median review dwell time are visible, broken down per agent and per user for the named period

### AC-F41-08
- **Given** a review queue into which known-error probes are injected at the configured rate
- **When** a reviewer works the queue
- **Then** the probes appear in the queue and are not distinguishable from genuine proposals by anything rendered before disposition, and the count of probes presented in the period is retrievable

### AC-F41-09 — observable UI
- **Given** a completed run that produced N detections of which M were routed to a human
- **When** the user views the run's exception queue on the Exceptions screen
- **Then** both N and M are visible for that run, so the proportion of detections reaching a human is readable without leaving the screen

### AC-F41-10
- **Given** a completed run that produced no items requiring review
- **When** the user opens the Exceptions screen for that run
- **Then** an explicit zero-pending-items state is visible carrying the run's coverage statement, not a blank list and not a spinner

### AC-F41-11
- **Given** an approver submitting an approval where persisting it fails
- **When** the failure occurs
- **Then** the proposal remains not-approved, no approval record exists, and the failure is shown to the approver

### AC-F41-12
- **Given** a proposal whose originating run has been superseded by a later run
- **When** an approver attempts to approve it
- **Then** the approval is blocked, and the block names the superseding run and its completion time

### AC-F41-13 — observable UI
- **Given** a signed-in user with at least one pending proposal
- **When** they open the Review screen for that proposal
- **Then** the proposal's evidence set, the approve control, the structured-reject control and the resolution-type control are all visible on that screen, and the approve control is not the only visible terminal action

---

## 13 · F1 — Evidence dossier store + auditor export

Obligations A, C, G, I. With Oracle holding the ledger, the dossier is the only
artefact that explains why Oracle contains what it contains.

### AC-F1-01
- **Given** any proposal the system produced
- **When** its dossier is retrieved
- **Then** the dossier contains the version tuple, the dataset version, the guardrail bundle hash, the broker decision ID, the coverage statement and the rendered view — a dossier missing any one of these does not exist in the store

### AC-F1-02
- **Given** a stored dossier
- **When** an update or delete is attempted against it through any surface, API or administrative path
- **Then** the attempt fails, the dossier is unchanged, and the attempt itself is recorded as an event in the store

### AC-F1-03
- **Given** a stored dossier whose bytes have been altered outside the application
- **When** its integrity is verified
- **Then** the verification reports the dossier as modified and identifies it

### AC-F1-04
- **Given** an F1 export for a period
- **When** it is opened by a party with no application login and no access to the running system
- **Then** it is parseable, and it contains every dossier for that period with all the fields required by `AC-F1-01` — no field renders only as an in-application reference

### AC-F1-05
- **Given** a past decision and its stored artefacts alone
- **When** an auditor reconstructs it
- **Then** they can state what data version was used, what policy bundle was in force, what coverage the run had, what the approver was shown and who approved it. **Re-execution producing an identical output is not asserted by this or any criterion** (`PLAN.md` §11.0).

### AC-F1-06
- **Given** a period in which no proposals were produced
- **When** an F1 export is requested for that period
- **Then** an export is produced containing zero dossiers and an explicit statement that the period contained no proposals — the request does not fail and does not return nothing

### AC-F1-07
- **Given** an export whose generation fails part-way
- **When** the failure occurs
- **Then** no file is presented to the user as complete, and the failure is shown naming the point of failure

### AC-F1-08
- **Given** a dossier at the oldest end of the retention period
- **When** it is retrieved
- **Then** it is returned complete, with all fields required by `AC-F1-01`, and its retention expiry date is stated

### AC-F1-09 — observable UI
- **Given** a signed-in user and a period containing at least one dossier
- **When** they open the Audit screen
- **Then** the dossier list for that period is visible, an individual dossier's full contents including its rendered view are reachable from that list, and an export control for the period is visible

---

## 14 · F2 — Version registry and proposal stamp

Obligations I, J, K.

### AC-F2-01
- **Given** any proposal
- **When** its stamp is read
- **Then** it names the model version, the prompt version, the tool/config version, the corpus version, the dataset version and the guardrail bundle hash, each as an independently identified artefact version

### AC-F2-02
- **Given** a stamped proposal and a subsequent change to any of the underlying artefact versions
- **When** the original proposal's stamp is re-read
- **Then** it still shows the versions in force at the time it was produced

### AC-F2-03
- **Given** a change to a model version, a prompt, or a guardrail policy
- **When** the change is made
- **Then** a change record exists naming what changed, the prior and new version identifiers, the owner and the effective date, and it is retrievable from the changelog for the period

### AC-F2-04
- **Given** a request to run a skill whose model, prompt or bundle version is not present in the registry
- **When** the run is submitted
- **Then** the run does not start and the response names the unregistered artefact

### AC-F2-05
- **Given** a model version marked deprecated by its provider
- **When** the registry is read and when a run uses that version
- **Then** the deprecation is stated with its date, and the run's output carries the deprecation notice

### AC-F2-06
- **Given** a period in which no model, prompt or policy change occurred
- **When** the changelog for that period is read
- **Then** it states explicitly that no changes occurred in the named period

### AC-F2-07 — observable UI
- **Given** a signed-in user viewing a dossier on the Audit screen
- **When** the dossier detail is displayed
- **Then** the full version tuple from `AC-F2-01` is visible on that screen

---

## 15 · F5 — Agent identity, inventory and lineage

Obligations D, G.

### AC-F5-01
- **Given** two different agents that each performed an action in the same period
- **When** the action log is read
- **Then** each action is attributed to a distinct named principal, and the two agents' actions are separable without inference

### AC-F5-02
- **Given** an agent that has been deployed and has performed at least one action
- **When** the Inventory is read
- **Then** the agent appears with its identity, its entitlements and its current version, without any manual registration step having been performed

### AC-F5-03
- **Given** a specific agent version that touched a known set of artefacts
- **When** a lineage query is run for that version
- **Then** the result enumerates every artefact in that set, and the result states that it is complete rather than sampled

### AC-F5-04
- **Given** an agent version that has touched no artefacts
- **When** a lineage query is run for it
- **Then** the result explicitly states zero artefacts for that named version

### AC-F5-05
- **Given** a lineage query that cannot be computed completely
- **When** it returns
- **Then** it is labelled **incomplete** and names what could not be traversed; a partial list is never returned unlabelled

### AC-F5-06
- **Given** an agent that has been retired
- **When** the Inventory is read and a lineage query is run for its versions
- **Then** the retired agent is still listed with its retirement date, and its lineage still resolves

### AC-F5-07 — observable UI
- **Given** a signed-in user and at least one deployed agent
- **When** they open the Inventory screen
- **Then** the agent inventory is visible listing each agent, its version and its entitlements, and a lineage view for a selected agent version is reachable from that list

---

## 16 · F40 — Reclass proposal → Oracle Journal Import export (**Tier 2**)

Obligations A, B, E, F, H, L–P, **S**. MVP1 exports; it does not post
(`PLAN.md` §9.2 assumption A1, reversible).

### AC-F40-01
- **Given** an approved reclass proposal
- **When** its export is generated
- **Then** the file conforms to the Oracle Journal Import shape, carries balanced debit and credit lines, and every line names its ledger, period, account combination and amount

### AC-F40-02
- **Given** the MVP1 build
- **When** any path that would submit a journal to Oracle is exercised, and when the build is inspected for a posting credential
- **Then** no journal is submitted, no posting credential is resolvable anywhere in the build, and the attempt is recorded as a denied action with a decision ID

### AC-F40-03
- **Given** a reclass proposal that has not been approved in-product
- **When** an export is requested for it
- **Then** the export is refused and the refusal names the missing in-product approval

### AC-F40-04
- **Given** a generated export file
- **When** its header is read
- **Then** it carries the journal source and category reserved for this system, and no other source or category value

### AC-F40-05
- **Given** a tenant whose CUEC checklist has not been verified, or whose most recent verification failed
- **When** an export is requested
- **Then** the export is refused and the refusal names the unverified or failed CUEC items

### AC-F40-06
- **Given** a generated export and its dossier
- **When** they are read
- **Then** both state that the in-product approval is the evidence-bearing approval leg, that Oracle journal approval is required on this source as the system-of-record leg, and that the Oracle-side configuration is a customer-controlled prerequisite verified per tenant on the stated date

### AC-F40-07
- **Given** one approved single-line reclass and one approved reclass at the maximum permitted line count
- **When** each is exported
- **Then** both files are produced and conform to `AC-F40-01`; and given a batch that would exceed the per-batch line cap, the export is refused by the blast-radius cap with a decision ID rather than truncated

### AC-F40-08
- **Given** a period in which no reclass proposal was approved
- **When** an export is requested for that period
- **Then** no journal file is produced, and the response states that zero approved proposals exist for the named period — an empty file that could be mistaken for a valid empty batch is not produced

### AC-F40-09
- **Given** an export whose generation fails part-way
- **When** the failure occurs
- **Then** the approval remains valid and recorded, no partial file is presented as complete, and the failure is shown

### AC-F40-10
- **Given** an exported journal that is later reversed
- **When** the original dossier is read
- **Then** it carries a linkage to the reversal record, and the reversal exists as its own record rather than as a modification of the original

### AC-F40-11 — observable UI
- **Given** a signed-in approver viewing an approved reclass proposal on the Review screen
- **When** the screen is displayed
- **Then** the exact journal lines that will be exported are visible on that screen before the export control is used, and that same rendering is what `AC-F41-04` retains as the rendered view

---

## 17 · F33 — GL coding anomaly detection + reclass backtest evidence (A11)

Obligations C, Q, R, I, B. Scoped per `PLAN.md` §9.2 assumptions A3 and A4
(cost-centre and within-caption natural account, single legal entity, single
period; cut-off detect-only). Both are reversible on measured precision.

### AC-F33-01
- **Given** a fixture containing a posting whose cost centre disagrees with the evidence of comparable postings
- **When** an F33 run completes
- **Then** a coding finding is reported naming the posting, the coded cost centre, the proposed cost centre and the evidence supporting the proposal

### AC-F33-02
- **Given** a fixture containing a posting coded to the wrong natural account within the same statement caption
- **When** an F33 run completes
- **Then** a coding finding is reported naming the posting, both accounts, and confirmation that both fall within the same statement caption

### AC-F33-03
- **Given** a fixture containing a posting miscoded on the legal-entity or intercompany segment
- **When** an F33 run completes
- **Then** no proposal touching that segment is emitted; if the condition is surfaced at all it is surfaced as an out-of-scope detection with no proposal attached

### AC-F33-04
- **Given** a fixture containing a posting miscoded across a statement caption (an opex item coded to capex)
- **When** an F33 run completes
- **Then** no proposal crossing the caption is emitted; if surfaced at all it is surfaced as an out-of-scope detection with no proposal attached

### AC-F33-05
- **Given** a fixture containing a cut-off error — a posting whose period disagrees with its evidence
- **When** an F33 run completes
- **Then** it is reported as a detection with no proposal attached, and the finding states that cut-off resolution is not proposed by this system

### AC-F33-06
- **Given** a held-out period of historical reclass journals used as labels
- **When** the F33 backtest runs
- **Then** it reports precision and recall as numeric values, together with the held-out period, the label count and the model and prompt versions used

### AC-F33-07 — **the bias label, asserted as schema**
- **Given** any F33 backtest evidence record
- **When** the record is validated
- **Then** the recall value is accompanied by a mandatory, non-empty label field whose value states that recall is measured **against reclass-journal-caught errors only**; a record in which that field is absent, empty, or does not carry that meaning is invalid, and the run that produced it fails. The label is a required field of the evidence schema, not commentary attached to it.

### AC-F33-08
- **Given** an F33 backtest result displayed on screen, written to a dossier, and written to an export
- **When** each is read
- **Then** the `AC-F33-07` label appears adjacent to the recall figure in all three; a surface that shows recall without the label is a failure

### AC-F33-09
- **Given** a held-out period containing no reclass journals
- **When** the F33 backtest runs
- **Then** it reports that no labels were available for the named period and emits **no** precision or recall figure — it does not report perfect precision

### AC-F33-10
- **Given** a held-out period containing exactly one labelled reclass
- **When** the F33 backtest runs
- **Then** it reports precision and recall together with the label count of one, so the figures cannot be read as more evidenced than they are

### AC-F33-11
- **Given** a label set that cannot be retrieved
- **When** an F33 backtest is requested
- **Then** it reports that it could not run and emits no accuracy claim of any kind

### AC-F33-12 — observable UI
- **Given** a signed-in user and a completed F33 run with at least one coding finding
- **When** they open the Exceptions screen
- **Then** the coding findings are visible in the exception list, each showing the current coding, the proposed coding and its in-scope sub-type; and the run's backtest precision, recall and the `AC-F33-07` label are visible on the same screen for the model version that produced the findings

---

## 18 · F42 — Present-anomaly detection over certified datasets (**table stakes**)

Obligations Q, R, I. Ships; never the headline (`PLAN.md` §1).

### AC-F42-01
- **Given** a fixture containing a balance movement that is a statistical outlier against the account's history
- **When** an F42 run completes
- **Then** an anomaly finding is reported naming the account, the movement, and the historical range it departs from

### AC-F42-02
- **Given** a fixture containing a journal that is an outlier on its scored attributes
- **When** an F42 run completes
- **Then** an anomaly finding is reported naming the journal and the attributes that made it an outlier

### AC-F42-03
- **Given** an F42 run request whose selection includes an uncertified dataset, or for which no declared expected population is resolvable
- **When** the run is submitted
- **Then** the run does not start, and the response names the uncertified dataset or the missing declared population as the reason

### AC-F42-04 — **the wedge test, F42 side**
- **Given** the shared period-12 omission fixture used by `AC-F29-08` (a recurring entry present in periods 1–11, absent in period 12), with F42 run over the identical dataset selection and identical declared population as the F29 run
- **When** the F42 run completes
- **Then** the F42 output contains **no** finding corresponding to that omission — and this negative result is reported as one half of a paired comparison alongside `AC-F29-08`'s positive result. A build in which F42 detects the omission fails this criterion, and a build in which the paired comparison is not produced as a single reportable result also fails it.

### AC-F42-05
- **Given** an F42 run at 100% coverage that found no anomalies
- **When** its result is read
- **Then** it states that no exceptions were found in the scanned population and states that the population was 100% of the declared expected population

### AC-F42-06
- **Given** an F42 run whose dataset becomes unavailable before completion
- **When** the run terminates
- **Then** it is recorded as incomplete and emits no conclusion, including no statement that no anomalies were found

### AC-F42-07
- **Given** a movement exactly at the configured outlier threshold, and one immediately either side of it
- **When** an F42 run completes
- **Then** each produces a determinate result consistent with the threshold's stated inclusivity, and the threshold in force is stated on the result

### AC-F42-08 — observable UI
- **Given** a signed-in user and a completed F42 run
- **When** they open the Exceptions screen
- **Then** the present-anomaly findings are visible in the exception list, each labelled as a present-anomaly finding distinct from an omission finding, and the run's coverage statement is visible on the same screen alongside the findings

---

## 19 · Refusal surface — A19–A22 and the outright refusals

**This is not a new feature and must not be counted as one.** `PLAN.md` §5.8 and
§7.6 record the A19–A22 refusals as a **stated design property of the approved
scope**, and §11.G criterion 42 makes their *presence as refusals* a test
condition. The criteria below carry the prefix `AC-REFUSAL-` rather than a
feature ID precisely so they cannot be mistaken for an eighteenth backlog item.
`plan-agent` owns whether this framing is right; I am specifying what §7.6
already says.

The governing distinction: **"not built yet" and "will never be built" are the
same blank screen to a user and opposite answers to an auditor.** A build in
which these capabilities are merely *absent* fails every criterion below.

### AC-REFUSAL-01 — observable UI
- **Given** a signed-in user
- **When** they open the Refusals screen
- **Then** A19 (estimates, reserves, allowances, impairment, valuation), A20 (materiality / SAB 99 / iron-curtain conclusions), A21 (certification and sign-off) and A22 (contentious cut-off and technical-accounting conclusions) are each visible by name with the reason each is refused

### AC-REFUSAL-02
- **Given** the Refusals screen
- **When** each refusal entry is read
- **Then** it states that the refusal is a design property of the product, not a roadmap gap, and its wording is distinguishable from the wording used for any deferred capability

### AC-REFUSAL-03
- **Given** a signed-in user on the Ask screen
- **When** they ask, in natural language, for an impairment assessment or a reserve estimate
- **Then** a refusal naming A19 is returned, stating that this is refused by design and will not be built — the response is not an empty result, not "no data found", not a spinner, and not a best-effort answer

### AC-REFUSAL-04
- **Given** any request that triggers a declared refusal
- **When** the refusal is issued
- **Then** an event is recorded naming the refusal invoked, the requesting user, the request text and the timestamp, and it is retrievable from the Audit screen

### AC-REFUSAL-05
- **Given** one natural-language request per refused capability — a materiality conclusion (A20), a certification or sign-off (A21) and a contentious cut-off conclusion (A22)
- **When** each is submitted
- **Then** each returns a refusal naming its specific A-number; a null response, an empty result set, a generic "I can't help with that", or an attempt at the answer each fail this criterion

### AC-REFUSAL-06
- **Given** a request for a capability that is **deferred** rather than refused (for example flux driver decomposition, F45)
- **When** it is submitted
- **Then** the response is distinguishable in substance from a refusal response and states that the capability is not available in this release rather than that it will never be built

### AC-REFUSAL-07
- **Given** requests to auto-post below a threshold, to have one agent's review substitute for a human approval, and to run a free-form SQL query over arbitrary datasets
- **When** each is submitted through any surface
- **Then** each is refused, each refusal names why the capability does not exist by design, and each is recorded as a control event

---

## 20 · Retired IDs

None. This is pass 1; no ID has been issued and withdrawn.

When a criterion is deleted or materially re-meaninged, its ID is listed here
with a one-line note and the ID of its replacement where one exists. Later IDs
are never shifted up to close the gap.

| Retired ID | Date | Note | Replaced by |
|---|---|---|---|
| _(none)_ | | | |

---

## 21 · Criteria written against a reversible assumption

`PLAN.md` §9.2 records seven reversible assumptions. Where a criterion depends on
one, it is named here, so that reversing the assumption is a bounded edit to this
file rather than a search.

| Assumption (`PLAN.md` §9.2) | Criteria that depend on it | What changes if reversed |
|---|---|---|
| **A1 — MVP1 exports rather than posts** | `AC-F40-01`, `AC-F40-02`, `AC-F40-04`, `AC-F40-06`, `AC-F40-08`, `AC-F40-09`, `AC-F40-11` | `AC-F40-02` is retired and replaced by posting criteria under new IDs. The two-key criteria (`AC-F40-05`, `AC-F40-06`) strengthen rather than change. |
| **A2 — one surface, desktop web** | every `— observable UI` criterion | New surface criteria are issued under new IDs. `AC-F36-03` is written so broker enforcement is inherited by a new surface without amendment. |
| **A3 — coding scoped to cost centre + within-caption natural account, single LE, single period** | `AC-F33-01` … `AC-F33-05` | `AC-F33-03` and `AC-F33-04` are retired and replaced when measured precision permits the excluded sub-types. |
| **A4 — cut-off is detect-only** | `AC-F33-05` | Retired and replaced with a proposal-generating criterion under a new ID. |
| **A5 — present-anomaly ships but is first to cut** | all of §18 | If F42 is cut, `AC-F42-01`–`AC-F42-03` and `AC-F42-05`–`AC-F42-08` retire — but **`AC-F42-04` cannot simply retire**: the wedge test needs a present-anomaly detector to be the negative side. Cutting F42 removes the ability to demonstrate the wedge, which is a consequence `plan-agent` should see before cutting it. Flagged, not resolved. |
| **A6 — six merges to hit the ≤18 ceiling** | none directly; F9 absorbs old F10's narrative leg (`AC-F9-03`, `AC-F9-09`) and F1 absorbs old F13's export (`AC-F1-04`, `AC-F1-06`, `AC-F1-07`) | Un-merging re-homes those IDs to a new feature section; the IDs themselves do not change. |
| **A7 — A19–A22 refusals are a shipped surface** | all of §19 | Stated by `plan-agent` as not reversible in its view. |

---

## 22 · Coverage summary

### 22.1 Criteria per feature

| Feature | Mark | Criteria | IDs | Observable-UI criteria |
|---|---|---|---|---|
| F26 — warehouse-to-ERP fidelity + staleness | FLOOR | 10 | `AC-F26-01` … `-10` | `AC-F26-10` |
| F28 — five boundary checks | FLOOR | 10 | `AC-F28-01` … `-10` | `AC-F28-10` |
| F29 — omission detector family | **WEDGE** | 12 | `AC-F29-01` … `-12` | `AC-F29-12` |
| F9 — cross-period surveillance | **WEDGE** | 9 | `AC-F9-01` … `-09` | `AC-F9-08` |
| F35 — resolution typing R1–R6 | **WEDGE** | 9 | `AC-F35-01` … `-09` | `AC-F35-09` |
| F12 — disposition & review-precision capture | WEDGE (enabler) | 9 | `AC-F12-01` … `-09` | `AC-F12-08` |
| F36 — guardrail engine + broker | WEDGE + FLOOR | 19 | `AC-F36-01` … `-19` | `AC-F36-18`, `AC-F36-19` |
| F38 — dataset catalogue + coverage | FLOOR | 15 | `AC-F38-01` … `-15` | `AC-F38-14`, `AC-F38-15` |
| F39 — semantic layer + NL interface | FLOOR + table stakes | 9 | `AC-F39-01` … `-09` | `AC-F39-09` |
| F41 — review & approval surface | FLOOR | 13 | `AC-F41-01` … `-13` | `AC-F41-07`, `AC-F41-09`, `AC-F41-13` |
| F1 — evidence dossier + auditor export | **WEDGE** | 9 | `AC-F1-01` … `-09` | `AC-F1-09` |
| F2 — version registry and stamp | FLOOR | 7 | `AC-F2-01` … `-07` | `AC-F2-07` |
| F5 — agent identity, inventory, lineage | FLOOR | 7 | `AC-F5-01` … `-07` | `AC-F5-07` |
| F40 — reclass → Journal Import export | FLOOR (Tier 2) | 11 | `AC-F40-01` … `-11` | `AC-F40-11` |
| F33 — coding anomaly + backtest | NET | 12 | `AC-F33-01` … `-12` | `AC-F33-12` |
| F42 — present-anomaly detection | TABLE STAKES | 8 | `AC-F42-01` … `-08` | `AC-F42-08` |
| **Refusal surface (A19–A22)** — design property, not a feature | — | 7 | `AC-REFUSAL-01` … `-07` | `AC-REFUSAL-01` |

**Total: 186 criteria** — 179 across the 17 build-now features, plus 7 for the
refusal surface. The table above has 16 feature rows plus the refusal row:
**F32's 10 criteria are specified in §22.2 immediately below and are counted
there**, because its retrofit-hostility warrants its own statement rather than a
table row. 169 (table) + 10 (F32) = 179 feature criteria.

### 22.2 F32 — Forward disposition (the most retrofit-hostile item in the backlog)

Specified last for emphasis, not because it is least important. `DOMAIN_KB`
§10.7: the prediction must be recorded in the *prior* period for the control to
exist at all. **If period 1 of production ships without `AC-F32-01`, this
control cannot be added for a year.**

#### AC-F32-01
- **Given** a user recording any disposition on any item
- **When** they submit it without an expected clearing period
- **Then** the save does not complete, the item remains open, and no disposition record exists. This is a hard failure of the save, not a validation warning that can be acknowledged and bypassed, and it applies at every permission level including administrator.

#### AC-F32-02
- **Given** a disposition recorded in period P with an expected clearing period of P+1
- **When** period P+1 closes
- **Then** a verification job runs without any user having requested it, and produces a verification record for that disposition stating met or missed

#### AC-F32-03
- **Given** a disposition whose expected clearing period has passed with the item not cleared
- **When** the verification job produces the missed result
- **Then** the account's risk grade is observably raised and its auto-pass eligibility is observably revoked — an R6 control-state change readable on the account — rather than a notification being emitted

#### AC-F32-04
- **Given** a disposition whose item cleared in the predicted period
- **When** the verification job runs
- **Then** the prediction is recorded as met, and it contributes to the forward-disposition hit rate displayed for the period

#### AC-F32-05
- **Given** a user recording a disposition in period P
- **When** they enter an expected clearing period of P or earlier
- **Then** the save does not complete and the response states that the expected clearing period must be later than the current period

#### AC-F32-06
- **Given** a user recording a disposition in period P
- **When** they enter the earliest permitted expected clearing period (P+1) and, separately, the maximum permitted horizon
- **Then** both save successfully, and a period beyond the maximum horizon does not save and states the maximum

#### AC-F32-07
- **Given** a period in which no predicted clearing periods fall due
- **When** the verification job runs
- **Then** it records that zero predictions were due for the named period, rather than producing no record

#### AC-F32-08
- **Given** a verification job scheduled for a period that has not yet closed in the source data
- **When** it runs
- **Then** it records a deferral naming the reason and the period, and it does not record any prediction as met or missed

#### AC-F32-09 — observable UI
- **Given** a signed-in user with at least one open disposition carrying a forward prediction
- **When** they open the Dispositions screen
- **Then** the open items are visible with their expected clearing periods, and the items whose predictions were missed in prior periods are visible and distinguishable from those still within their predicted horizon

#### AC-F32-10 — observable UI
- **Given** a signed-in controller and at least one closed period containing verified predictions
- **When** they open the Monitors screen
- **Then** the forward-disposition hit rate for that period is visible — the product's own falsifiability measure, displayed whether it is good or bad

**F32: 10 criteria, `AC-F32-01` … `-10`, observable-UI at `AC-F32-09` and
`AC-F32-10`.**

---

## 23 · Observable-UI coverage — stated explicitly

Every one of the 17 build-now features carries at least one observable-UI
criterion, and so does the refusal surface. **There is no UI-bearing feature in
approved scope without one.**

The reason this is stated rather than assumed: on a prior project, four of ten
shipped defects were the same failure — a component built, imported, sometimes
state-managed, and **never rendered**. That class is invisible to typecheck, to
bundle checks and to API tests by construction. Each criterion below is written
as *"the X is visible on the Y screen in state Z"*, never as *"the X exists"* or
*"the X is imported"*.

| Screen | Criteria requiring something visible on it |
|---|---|
| **Ask** | `AC-F38-14`, `AC-F39-09`, `AC-REFUSAL-03` |
| **Exceptions** | `AC-F26-10`, `AC-F28-10`, `AC-F29-12`, `AC-F33-12`, `AC-F42-08`, `AC-F41-09`, `AC-F41-10`, `AC-F38-15` |
| **Review** | `AC-F35-09`, `AC-F36-18`, `AC-F40-11`, `AC-F41-01`–`AC-F41-06`, `AC-F41-13` |
| **Dispositions** | `AC-F32-09`, `AC-F35-07` |
| **Catalogue** | `AC-F38-01`, `AC-F38-12`, `AC-F38-13` |
| **Monitors** | `AC-F9-08`, `AC-F12-08`, `AC-F32-10`, `AC-F36-19`, `AC-F41-07` |
| **Inventory** | `AC-F5-07` |
| **Audit** | `AC-F1-09`, `AC-F2-07`, `AC-REFUSAL-04` |
| **Refusals** | `AC-REFUSAL-01`, `AC-REFUSAL-02` |

Two features are predominantly backend and their observable-UI criteria are
correspondingly narrow, stated here so the narrowness is visible rather than
silent:

- **F2** (version registry) — a single UI criterion, `AC-F2-07`: the version
  tuple visible on the dossier detail. F2's remaining criteria are assertions
  about stamped payloads and change records, which is what F2 is.
- **F12** (disposition capture) — a single UI criterion, `AC-F12-08`: override
  rate and probe results visible to the controller. F12's product is labels in a
  store, and the criteria that matter most (`AC-F12-01`, `AC-F12-07`) are
  assertions about the store.

Neither is a gap; both are recorded so a reviewer can disagree.

---

## 24 · Edge, empty, error and boundary coverage — per feature

Obligation on this gate: every feature covers the empty case, the error case, and
its real boundaries, or records not-applicable with a reason.

| Feature | Empty | Error | Boundary |
|---|---|---|---|
| F26 | `AC-F26-03` | `AC-F26-06` | `AC-F26-08` (smallest unit), `AC-F26-09` (first/last period) |
| F28 | `AC-F28-06` | `AC-F28-07` (check not run ≠ pass) | `AC-F28-09` (balance vs composition scope line) |
| F29 | `AC-F29-05` (insufficient history) | `AC-F29-10` | `AC-F29-06`, `AC-F29-07` (present-but-different is not an omission) |
| F9 | `AC-F9-05` | `AC-F9-09` | `AC-F9-06` (at / one short of the escalation count), `AC-F9-07` (alternating direction) |
| F35 | `AC-F35-07` | `AC-F35-08` | `AC-F35-06` (R1 expiry lapse), `AC-F35-05` (effort parity between safe and risky outcomes) |
| F32 | `AC-F32-07` | `AC-F32-08` | `AC-F32-05` (period ≤ current), `AC-F32-06` (first and last permitted horizon) |
| F12 | `AC-F12-06` | `AC-F12-07` | `AC-F12-09` (no multi-item disposition exists) |
| F36 | `AC-F36-19` (zero-override period) | `AC-F36-17` (fail closed) | `AC-F36-16` (exactly at threshold, either side), `AC-F36-11` (third consecutive period) |
| F38 | `AC-F38-13` | `AC-F38-12` | `AC-F38-08` (0% coverage), `AC-F38-07` (70% vs 100% must differ) |
| F39 | `AC-F39-05` (zero rows) | `AC-F39-06` | `AC-F39-08` (period outside certified range), `AC-F39-07` (ambiguity) |
| F41 | `AC-F41-10` | `AC-F41-11` | `AC-F41-12` (superseded run), `AC-F41-01` (every permission level) |
| F1 | `AC-F1-06` | `AC-F1-07` | `AC-F1-08` (oldest retained dossier) |
| F2 | `AC-F2-06` | `AC-F2-04` (unregistered version) | `AC-F2-05` (deprecated model) |
| F5 | `AC-F5-04` (zero artefacts) | `AC-F5-05` (incomplete lineage) | `AC-F5-06` (retired agent) |
| F40 | `AC-F40-08` | `AC-F40-09`, `AC-F40-05` (unverified CUEC) | `AC-F40-07` (single line and maximum lines) |
| F33 | `AC-F33-09` (no labels) | `AC-F33-11` | `AC-F33-10` (single label), `AC-F33-03`/`-04`/`-05` (the three scope boundaries) |
| F42 | `AC-F42-05` | `AC-F42-06` | `AC-F42-07` (exactly at threshold) |
| Refusals | n/a — a refusal has no empty case; recorded as not-applicable | `AC-REFUSAL-05` (a null or generic response is a failure) | `AC-REFUSAL-06` (refused vs deferred is the boundary) |

---

## 25 · Scope ambiguity found and **not** resolved

Reported for the human and `plan-agent`. I have written criteria against the
reading I state, and I have not resolved either.

1. **The refusal surface has no feature ID.** `PLAN.md` §5.8 and §7.6 make the
   A19–A22 refusals a binding, testable, *shipped surface* (§11.G criterion 42),
   and §6.2's structure gives it both a backend module (`refusal/registry.py`)
   and a frontend component directory (`components/refusal/`). But it is not one
   of the 17 build-now features and has no ID, so it is a shipped surface with no
   line in the backlog and no owner in the count. I have specified it under
   `AC-REFUSAL-NN` and explicitly not counted it as an eighteenth feature.
   **`plan-agent`'s call**: either it gets a feature ID and the count becomes 18,
   or §7.6 is amended to say in terms that it is a cross-cutting property that
   the build-now features collectively carry. Leaving it as it is means a
   surface that must be built has no approval row.

2. **F42's inclusion is load-bearing for the wedge test in a way §7.4 does not
   acknowledge.** `PLAN.md` §7.4 marks F42 "the first thing I would cut", and
   §9.2 A5 says only its priority is at stake. But `PLAN.md` §11 criterion 21 —
   which §11.D calls "the single most important test in this suite" — requires
   F42 to exist as the **negative** side of the comparison. Cutting F42 does not
   merely lose a table-stakes feature; it removes the ability to demonstrate the
   wedge at all. I have written both sides (`AC-F29-08`, `AC-F42-04`) as a paired
   comparison producing one reportable result. **`plan-agent`'s call** whether
   F42 should therefore be re-marked as non-cuttable, or whether an alternative
   negative-side detector is acceptable. I have not changed the mark.

3. **Minor, noted not escalated.** `AC-F41-03` (prominence of the riskiest
   element) sits closest to `ui-ux-designer`'s lane of anything in this file. I
   have specified it as reading order and non-collapsibility — both observable
   and both behavioural — and have deliberately said nothing about size, weight,
   colour or position. If `ui-ux-designer` judges even this to be a design
   constraint, the criterion should be renegotiated at gate 5 rather than
   silently designed around.

---

## 26 · Change history

| Date | Version | Change | Approving decision |
|---|---|---|---|
| 2026-07-31 | 1.0.0 | Initial specification. 17 build-now features from `PLAN.md` §7 plus the A19–A22 refusal surface. 186 criteria issued (`AC-F26-01` … `AC-F42-08`, `AC-F32-01` … `-10`, `AC-REFUSAL-01` … `-07`). No IDs retired. | Standing authorization to build MVP1, `PROJECT_CONTEXT.md` Decisions Log 2026-07-31; gate 4 human approval pending |
