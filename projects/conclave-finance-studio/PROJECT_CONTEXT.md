# conclave-finance-studio

## Overview

**Conclave Finance Agentic Studio** — a multi-agent AI system for finance
accountants. Ships working close agents, and lets accountants clone, tweak and
combine them into agentic teams for month-end close.

- **Created**: 2026-07-30
- **Template**: pending `plan-agent` recommendation
- **Surfaces**: **MVP1 desktop web only.** The product remains multi-surface
  (desktop web · mobile web · native mobile) and `solution-architect` stays
  non-droppable on that basis, but MVP1 ships one surface. The header
  previously read as though all three were in MVP1, contradicting the Decisions
  Log, `PLAN` §9.2 A2 and `FUNCTIONAL_SPEC` §21 — caught by `ui-ux-designer` at
  gate 5, which had already designed desktop-only on the correct reading.
- **Data**: financial data warehouse, sourced from Oracle ERP Cloud
- **Write-back**: yes — per-action explicit human approval
- **Current stage**: gate 1 · Intake

## Active Team

**Approved 2026-07-31 — full roster, 14 agents. Nothing dropped.**

Core (8): `plan-agent`, `functional-design-agent`, `code-agent`, `test-agent`,
`verification-agent`, `review-agent`, `deploy-agent`, `ui-ux-designer`.

Optional, all retained, each with a named obligation that would otherwise go
unowned:
- `solution-architect` — **non-droppable by rule** (three surfaces); owes the
  mandatory Impact Analysis on every change
- `responsible-ai-architect` — **non-droppable in practice**; owes the A7.2
  harm analysis delegated to it at Intake
- `security-architect` — owns `industry-expert`'s eleven compliance
  obligations (ICFR scope, IPE testing, 7-year WORM retention, SoD)
- `functional-agent` — devil's advocate at Plan and Architecture; found the
  self-justifying-reconciling-item mechanism and the builder's author-role SoD
  defect
- `industry-expert` — owns the compliance floor, which is the binding
  constraint on this product
- `synthetic-data-agent` — close agents cannot be tested on real ledger data

**Test Policy: all suites blocking.** No advisory exceptions. Ledger write-back
and ICFR scope make an advisory suite a hole in the control narrative.

**Estimate at approval**: 5–8M tokens, from 2 comparable data points
(`conclave-marketing` ~4.8M, `little-milestones` ~5.0M). Stated as a planning
input, not a prediction; upper end uncertain because the MVP slice is
undecided.

## Decisions Log

- **2026-07-30 — Intake.** Gathered one question per turn in the console, per
  the standing rule recorded that same day. Full record: `INTAKE.md`.
- **2026-07-30 — Product shape: BOTH.** Pre-built close agents *and* a builder
  for custom agents/teams. Chosen over builder-only and closed-system-with-
  agents. Widest scope of the three; makes "which half ships first" the central
  MVP question.
- **2026-07-30 — Personas: all three.** Staff accountant, controller/close
  manager, FP&A analyst. Doer, supervisor, explainer.
- **2026-07-30 — Write-back with per-action approval.** Not read-only, not
  autonomous. Creates binding obligations: audit trail per write, rollback,
  segregation of duties, and an approval UI legible under close-deadline
  pressure.
- **2026-07-30 — A7.2 (worst harm) and A8.3 (MVP slice) DELEGATED to SMEs.**
  Recorded as answers, not gaps. Consequence: `responsible-ai-architect`
  becomes effectively non-droppable.

- **2026-07-31 — SCOPE CORRECTION (human).** The system is **not** the General
  Ledger. It runs on top of Oracle ERP Cloud data in a warehouse, triggers
  postings into ERP, and leaves all ERP/GL features in the GL. Its job is to
  **detect and resolve anomalies** during a standard close. *"Do not imitate
  GL."* This invalidated F6/F7/F8/F11 — a matching engine, statement ingestion,
  auto-certification rules and a certification workspace are Oracle Account
  Reconciliation Cloud. `functional-agent` had already called bank rec the most
  commoditised activity in the domain; the correction turns that from a
  positioning risk into a scope error. The spine (F1–F5, F12, F13) and the
  cross-period detectors (F9, F10) survive — all of those are about the agents,
  not the ledger.
- **2026-07-31 — PRODUCT DIRECTION (human), two parts.** (1) Build the backlog
  from research into which close activities AI agents can genuinely automate —
  anomaly detection, balancing, coding issues. (2) The surface is a
  **natural-language, skill-based interface**: select one or more datasets, ask
  an agent to act or automate **under guardrails**.
- **2026-07-31 — STANDING AUTHORIZATION to build MVP1.** Gates go to the SMEs
  for review and their judgement is trusted; the orchestrator makes necessary
  assumptions rather than returning for each. Recorded as `batch_authorized`,
  **not** `approved` — the human authorized the run, not each gate. Every
  assumption lands in this log so it is reviewable after the fact.

- **2026-07-31 — MVP1 SCOPED TO ERP DATA ONLY (human).** Both SMEs independently
  escalated the same undecidable: does the pilot warehouse carry non-Oracle
  sources? Human's answer: **start narrow, ERP-only for MVP1; additional sources
  are future phases.**

  **Why this is viable despite both SMEs warning that single-source Oracle means
  "Oracle's Ledger Agent wins and we are a worse-positioned copy":** the three
  differentiators they identified do not depend on source count.
  1. **Omission detection** — "the product detects what did not happen". The
     evidence of an absence is *not in the ledger*, so a ledger-resident agent
     cannot see it however many systems feed that ledger. Needs a multi-period
     expectation model, which ERP history alone supplies.
  2. **Resolution typing + evidence spine** — R1–R6 resolution model, forward
     disposition, dossier. Source-independent.
  3. **Cross-period surveillance** (`DOMAIN_KB` §6.2) — invisible in-period by
     construction, which is why no incumbent sells it. Source-independent.
  Plus `DOMAIN_KB` §10.4c: most coding errors originate in the subledger, where
  Oracle's Payables Agent codes pre-post one document at a time — **we are the
  net that catches what it let through**, post-hoc and ledger-wide. Explicitly
  survives an all-Oracle estate.

  **Deferred to phase 2, not abandoned**: the cross-system seam as a headline,
  cross-source omission detection, and warehouse-vs-ERP fidelity as a
  *differentiator* (it stays in MVP1 as an integrity check, per `DOMAIN_KB`
  §10.5 — it is the credibility floor, not the wedge).

  **Standing instruction**: continue making assumptions, take SME judgement, and
  loop to MVP1 without returning for per-gate approval.

- **2026-07-31 — Gate 4 ambiguity 1 resolved: the refusal surface gets a feature
  ID, F50.** `functional-design-agent` found it binding (backend module,
  frontend directory, test criterion §11.G-42, seven AC IDs) but with no feature
  row and no approval line. Making it "a cross-cutting property the 17
  collectively carry" means nobody owns it, and an unowned surface is what gets
  cut in week ten. Build-now count → **18**, exactly at the ceiling. A19–A22 are
  load-bearing *refusals*: "not built yet" and "will never be built" are the
  same screen to a user and opposite answers to an auditor.
- **2026-07-31 — Gate 4 ambiguity 2 resolved: F42's cut-marking is withdrawn.**
  `PLAN.md` §7.4 marked F42 "the first thing I would cut", but §11 criterion 21
  — the test that proves the wedge is real rather than asserted — requires F42
  as the **negative** side of a paired comparison. Cutting F42 removes the
  ability to demonstrate the wedge at all. F42 is re-marked **TABLE STAKES,
  not cuttable while criterion 21 stands**. If a later gate wants F42 gone it
  must first say how the wedge gets demonstrated without it.
- **2026-07-31 — Gate 4 closed, `batch_authorized`.** 186 acceptance criteria
  across 18 features. Every UI-bearing feature carries at least one
  observable-UI criterion; F2 and F12 have exactly one each and the narrowness
  is flagged rather than hidden. §12 carries a standing exclusion: **no
  criterion asserts explanation quality and none may be added**, per
  `INDUSTRY_KB` §15.4 — clearer AI explanations make reviewers defer *more*.

- **2026-07-31 — Gate 5 decisions.** (a) `AC-F41-03` **strengthened** at
  `ui-ux-designer`'s request, not weakened: the riskiest element must render at
  the largest type size on the screen, with no other element equal or larger —
  behavioural, checkable by computed font-size, fixes no pixels. An element can
  be first and uncollapsed and still visually recessive. (b) **Routing budget
  accepted**: a per-reviewer-per-night cap requiring a recorded controller
  override. `AC-F41-09` makes volume *visible* but nothing made it *bounded*;
  without a cap the 11pm problem is mitigated, not bounded. (c) **Probe reveal
  timing** routed to `responsible-ai-architect` at gate 6. (d) **Surface header
  corrected** — see above.
- **2026-07-31 — Gate 5 closed, `batch_authorized`.** Rendered mockup, 17
  sections. Central call: **the agent's narrative is collapsed and last**; the
  riskiest element is first, uncollapsible, largest. The decisive argument was
  not the deference research but `AC-F12-03` — if the narrative is open by
  default, "which evidence did the reviewer expand" is a constant carrying zero
  information. Collapsing it is simultaneously the design decision and the
  measurement decision.
  **There is no green anywhere in the product.** Green means "fine, move on" —
  the exact affect a depleted reviewer must not be handed.

- **2026-07-31 — Gate 6 architect disagreements, resolved by the orchestrator.**
  1. **Evidence infrastructure: SEPARATE**, `security-architect`'s position over
     `solution-architect`'s shared cluster. Its argument decides it — the
     difference is whether one compromised credential reaches both the state and
     *the evidence of what changed it*. A shared cluster makes the evidence store
     only as trustworthy as the thing it exists to witness.
  2. **Suppression-by-injection: jointly owned, boundary stated.** The *emission*
     constraint is `responsible-ai-architect`'s (RAI-ARCH-1 — negative assurance
     may never be a model-authored string); the *channel* is
     `security-architect`'s (T2); the *mechanism* is already
     `solution-architect`'s closed sum type. The gap was ambiguity, not absence.
  3. **SA4 accepted** — a platform admin holds no finance capability. A platform
     admin who can approve a finance action is the ITGC finding.
  4. **D1 resolved for G-PROBE-3**: probe results render aggregate only, never
     per-named-user on any management surface. `AC-F12-08` is to be read that
     way, and gate 4 must say so rather than leave `code-agent` to choose.
  5. **D3 resolved**: A23–A25 are refusals under **F50**, which already exists as
     a feature. No breach of the 18-feature ceiling.
  6. **Personal data in the warehouse: ASSUME YES.** GL data carries employee
     expense lines, payroll clearing, and supplier detail in free-text
     descriptions. `solution-architect` asked for this before Code because it
     means per-column exposure classification in the certified query registry
     and a filtered resolver catalogue. Assuming *no* and being wrong is a
     retrofit through the one component the whole no-free-form-SQL guarantee
     rests on. Recorded as reversible: if the pilot warehouse is confirmed
     GL-balances-only, the classification can be relaxed.
- **2026-07-31 — Gate 6 closed, `batch_authorized`.** Three KBs written.
  Load-bearing calls: the trust boundary is a **process** not a module (a module
  boundary is bypassed by `import` and by a prompt-injected tool); no free-form
  SQL by **unroutability** rather than filtering; **no ReAct** because a ReAct
  loop's defining property is that the agent authors its own next step, which is
  what the allowlist exists to refuse; blast-radius caps as a **concurrency**
  property in one `SERIALIZABLE` transaction; and coverage as a **closed sum
  type** whose no-exceptions constructor is private.
  `responsible-ai-architect` overturned the promotion gate: **≥95% precision on
  accepted proposals is inverted** — the labels come from what the human did, so
  a perfectly rubber-stamping reviewer scores 100% and *the worse the deference,
  the faster the gate opens*.

- **2026-07-31 — Gate 4 loop-back closed.** 77 new criteria, 1 retired
  (`AC-F12-08`→`-10`, disambiguating a per-named-user probe score). **261 live.**
  `functional-design-agent` found a requirement nobody listed — gate 6 §16.3's
  policy-cold auto-disposal path — and issued `AC-F35-10`…`-13` for it,
  including third-consecutive-period escalation.
  **It also refused to issue IDs it could not honestly test**, which is the
  behaviour this gate exists for: security §10.1 items 7–8 have a falsifying
  observation seven years out, and it would not write a criterion "a suite could
  only satisfy by simulating a clock it doesn't control."
- **2026-07-31 — P1/P5 promotion-gate mechanics deferred to phase 2, with the
  silent-failure path closed.** Blind re-performance sampling and automatic
  Tier 2 demotion presuppose F17, which is deferred, so they are out of MVP1
  scope. What is NOT deferred: `AC-F12-20` forces every precision figure to
  carry a mandatory **label-source** field (acceptance-derived vs independently
  re-performed), and `AC-F12-21` forces a readiness report to state P1–P5
  individually and **never assert readiness on precision alone**. The inverted
  gate can no longer be used silently, which was the actual risk.

## Current Status

Gate 7 · Code — building MVP1 in staged passes against 261 acceptance criteria.
