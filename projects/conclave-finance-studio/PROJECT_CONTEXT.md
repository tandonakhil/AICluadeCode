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

- **2026-07-31 — Gate 7 Code pass 1: judgement calls made by `code-agent`.**
  Recorded here because the plan did not settle them and they are reviewable
  after the fact rather than inferrable from the diff.
  1. **Three architecture components could not be built as specified and are
     SUBSTITUTED, each flagged in code at its site**: mTLS on loopback →
     a shared client token plus a 127.0.0.1 bind (no CA or cert material in
     this environment); PostgreSQL `evidence_db` with a role holding no
     `UPDATE`/`DELETE` grant → a separate SQLite database with `BEFORE UPDATE`
     / `BEFORE DELETE` triggers that `RAISE(ABORT)` (no Postgres available).
     The Oracle-sourced warehouse → SQLite over the synthetic fixture, which
     also means `SECURITY_KB` §2.4's per-skill database grants have no
     analogue and are **not built**.
  2. **Anchor signing and the Object-Lock archive are stubs with real
     interfaces**, and are deliberately loud: they report `is_stub`, mark
     every artefact they produce, and **refuse to be constructed when
     `CONCLAVE_ENV=production`**. The archive reports
     `has_retention_lock = False` rather than faking protection it lacks.
  3. **`FullPopulationConclusion`'s private constructor is a lint-backed
     convention, not a language guarantee** — Python has no private
     constructors. The *variant* constraint (`no_exceptions` exists on one
     type and is absent, not `False`, on the others) IS type-level and
     unbypassable. Both residual holes have a test demonstrating exactly what
     they do.
  4. **Nine of the eleven evaluator primitives are ABSENT, not stubbed.** A
     manifest naming one fails compilation saying "not implemented in this
     build". A stub primitive would be a check that cannot fail.
  5. **Certified query manifests carry a tri-state column classification**
     (`true`/`false`/`unclassified`); a *missing* key fails the build, so
     "unclassified" is a declaration made, never one omitted. Entitlements are
     **derived** from the classification rather than hand-declared.
  6. **The `ux` and `industry` suites exit `3`, not `0`** — no UI and no
     F40/CUEC/POAR/close-clock exist to test. Each carries a README naming
     what must exist first.

- **2026-07-31 — Gate 7 Code pass 2c: judgement calls made by `code-agent`.**
  1. **The F50 refusal registry (A19–A25) is CODE, not a bundle policy
     object** — deliberately unlike the nine behavioural guardrails, which are
     bundle-resident as RAI-ARCH-2 requires. A bundle publication is a
     two-human change-control act this build otherwise treats as sufficient
     authority to change any policy; if the refusal set lived there, A20 — the
     keystone every other guardrail is downstream of — would be one
     publication away from removal. A test asserts no refusal ID is expressed
     in any compiled rule.
  2. **A20's enforcement has two legs of unequal strength, and this is
     stated rather than smoothed.** The *structural* leg (a variance disposed
     with no adjustment on a `magnitude`/`threshold`/`none` ground) reads
     fields and no rewording touches it; every emission carrying a disposition
     passes through it. The *prose* leg, for the F39 NL surface, matches the
     shape of the speech act rather than a word list — but it is a pattern
     matcher over English and **is evadable**. A test *demonstrates* a
     paraphrase that evades it, then shows the structural leg catching the
     same emission once it disposes. The residual is an executable fact.
  3. **The predicate language gained two operators**, `subset_of` and
     `intersects`. Without them G-SELFREF and G-SCOPE-DRIFT could only be
     expressed by precomputing the answer in context-assembly code and having
     the rule read `emission.selfref_ok` — which moves the real check out of
     the versioned, fixture-backed bundle and leaves a rule that is decoration.
  4. **Emission abstention triggers are evaluated BEFORE the guardrails**, and
     AB5 outranks AB1. If the system should have declined, the correct output
     is a typed decline; a bare denial leaves the human nothing to act on. And
     an item whose evidence supports two resolution types equally is not an
     item with insufficient evidence — calling it AB1 loses the fact that the
     tie is what the human must break.
  5. **R3/R4's evidence schema was widened to four fields.** Writing
     `AC-F35-05`'s test first exposed a real fault: R5 (explanation + owner +
     due date) cost more interactions than R3/R4 as first specified, which is
     the thumb on the scale toward posting the criterion exists to prevent.
     Fixed by making the proposal schema what a proposal actually needs — it
     must name what it would move, from where, and in which direction — rather
     than by making the safe outcomes artificially cheap.
  6. **`decision.outcome` gained `abstain` as a peer of `deny`.** It did not
     have one, so an abstention was not in fact recordable as anything other
     than a denial with a special reason string.

- **2026-07-31 — Gate 7 Code pass 3 (the UI): judgement calls made by `code-agent`.**
  1. **STACK: server-rendered HTML from the existing FastAPI `api` process, not
     the template's Next.js front end.** `PLAN.md` §6.2 chose `genai-chatbot`,
     whose front end is Next.js/TypeScript/Tailwind. Four reasons for the
     departure, recorded so a later gate can overturn it on argument:
     (a) `ARCHITECTURE_KB` §9.4 requires a **server-rendered, style-inlined**
     evidential region and `AC-F41-04` requires the retained rendered view to
     reproduce what the approver saw — server-rendered makes the response and
     the retained artefact the same bytes, where a client-rendered app makes
     them a render and a re-render; (b) `UX_KB` §5.4 forbids the three things a
     client runtime buys (hover-only facts, lazy loads, live refresh), and a
     build with no `<script>` satisfies that by construction rather than by
     review; (c) no screen in `FUNCTIONAL_SPEC` §23 has client-side state worth
     a runtime, and the one thing that would need it — bulk selection — is
     forbidden; (d) it adds no runtime dependency. **Playwright is added as a
     dev dependency**, which `templates/genai-chatbot/TEMPLATE_MANIFEST.md`
     already specifies.
  2. **Four palette tokens deviate from the gate-5 approved mockup**, each
     found by running the browser suite and each flagged in code at its site:
     the dark risk ramp was non-monotonic in luminance (step 2 darker than step
     1, so the ordinal broke in greyscale — the exact print condition `UX_KB`
     §3.2 is about); light `risk-1-bg` failed AA by 0.004; light `ink-3` failed
     AA on `surface-2`/`surface-3` where most small text sits; the dark primary
     button was white-on-light-blue at 2.52:1. These implement `UX_KB` §3.2's
     stated intent rather than departing from it, but they are pixel changes to
     an approved design and are recorded as such.
  3. **"There is no green" is enforced, not conventional.** `tokens.py` converts
     every declared colour to HSL and refuses the green hue band at import of
     `chrome.py`. A green token is an ImportError. The band reaches into teal
     (175°) because the failure mode is a colour that *reads* as success.
  4. **Abstained items are absent from the findings queue**, not merely styled
     differently inside it. A distinct pill inside a list of findings is still
     a row in a list of findings. They keep their own region and are still
     routed (`AC-F36-50`).
  5. **The write path refuses rather than pretending.** `POST /review/{id}/resolve`,
     `/reject` and `/proposal/{id}/approve` return **501 in the deferred
     grammar** naming what is missing. There is no `/ges/decide` HTTP route, so
     there is nothing for the api process to ask; a route that recorded an
     approval locally would be the interface deciding what only the broker may
     decide. The controls are real controls, and their terminal state is an
     honest refusal.
  6. **The pilot report moved to a three-closed-period window.** At two, every
     readiness condition reports `not_yet_evaluable` for the same reason and a
     reader never meets the difference between "we looked and it failed" and
     "we have not looked long enough".

- **2026-07-31 — Gate 7 Code pass 4 (MVP1 end to end): judgement calls made by
  `code-agent`.**
  1. **Overridability became a bundle field, and an identity rule may not
     declare itself overridable at all — the compiler refuses the bundle that
     tries.** Building `AC-F36-18`'s override control exposed that no notion of
     "override-eligible" existed: every rule denial was overridable, so the
     authorship closure was waivable by anyone holding a reason code. Value
     ceilings and blast-radius caps are eligible; an *unevaluable* check is not,
     because nobody knows what they would be waiving. A new rule
     `quant.approval_value_ceiling` governs the human approving, distinct from
     the ceiling on the agent proposing, and it made `Approvable.abs_value` a
     constructor requirement: a limit cannot be applied to an amount nobody
     declared, and "denied: the check could not be evaluated" is a much worse
     answer to an approver than a request that was never built.
  2. **A denial is HTTP 200 on `/ges/decide` and HTTP 403 on `/ges/query`**, and
     the asymmetry is deliberate. A refused query has no result and must not
     read as zero rows; a denied action HAS a result — a recorded,
     decision-ID-bearing answer the interface is required to display — and an
     error status would make it indistinguishable at the transport layer from
     an unreachable broker.
  3. **The pre-flight eligibility hint stays carried on the item.** Asking the
     broker to decide an approval nobody has requested would write a decision
     record for a non-event, which is exactly `AC-F36-06`'s trap. The hint is
     advisory and says so; the decision happens at submit and is the only thing
     that permits anything.
  4. **`backend/pilot_transport.py` is a DECLARED WEAKENING and is outside the
     `app` package.** It puts the broker in the api process so the pilot is
     operable and the `ux` suite can drive a real approval without a server it
     is forbidden to start. In that configuration the trust boundary is a
     module boundary. It is one named file rather than a lazy import, so the
     architecture suite's "the api package never imports the ges package" check
     keeps working unweakened.
  5. **Form bodies are parsed with the standard library, not `request.form()`.**
     `python-multipart` is not a dependency and adding one to read four text
     fields would be a poor trade — but the real consequence is that **this
     surface now structurally accepts no file upload**, so "upload an
     uncertified spreadsheet and have an agent act on it" cannot be added by
     writing a form.
  6. **The reachability tests now DRIVE the controls.** Link-following cannot
     reach a screen that only exists as the result of an action, and "it would
     render if you posted the form" is the claim that check exists to refuse. A
     companion test asserts those components are *not* reachable by navigation,
     so the driving traversal cannot be deleted without something failing.
  7. **A pilot persona switch exists** (staff accountant / controller). It is
     not authentication and is refused in production. It is there because the
     claim it demonstrates — that a staff accountant's approval is denied by the
     BROKER, not hidden by the interface — is one a reader must be able to
     exercise.
  8. **Governance screens render "this could not be read" rather than a zero**
     when GES is unreachable, and a test cuts the transport to prove it. A zero
     on a control surface is a claim, and no claim was obtained.
  9. **The `ux` harness was dropping POST bodies.** Harmless while every write
     endpoint returned 501 regardless of input; silent the moment the write path
     read form fields, because a click on a submit button arrived as an empty
     submission. Every earlier UX POST scenario was weaker than it read.

- **2026-07-31 — Gate 7 pass 4d, LOOP-BACK FROM GATE 8: four evidence-honesty
  fixes. Judgement calls by `code-agent`.** The brief was explicit that several
  of these would make a passing suite *report less*, and that is what happened.
  No scenario was made to pass by weakening what it asserts; three now assert
  strictly more, and one criterion ID left the suite entirely.
  1. **A red-team suite must show its own boundary.** The A20 evasion found by
     probing the broker at gate 8 (evasive prose + `treatment` +
     *substantiated* ground → `allow`) is now a red-team scenario that asserts
     it **reaches a surface**, rather than a unit test no red-team reader
     looks at. It was NOT closed by extending the shape matcher: `RESPONSIBLE
     _AI_KB` §4.1 rules that out as an arms race against paraphrase, and the
     structural leg — which holds absolutely wherever a disposition carries a
     size-shaped ground — is the real control and is asserted unchanged
     alongside it. The eight `..._however_phrased` names were renamed: *however
     phrased* is an exhaustiveness claim over English that a shape matcher
     cannot support.
  2. **`AC-F1-08` now appears in no test file.** The scenario carrying that ID
     read a retention date out of a row it had written seconds earlier. It was
     renamed and rescoped to what it tests, with the criterion's unsatisfied
     status stated in its first docstring line, because gate 9 joins IDs to
     criteria mechanically. The functional suite reports one criterion fewer
     than it did before, which is the accurate number.
  3. **A suite may start a child process it owns; it may not start a server.**
     The two-process topology had no executing witness, and both suites that
     appeared to cover it would have passed with the boundary gone. The new
     `ARCH-04` runtime scenarios start `ges/run.py` on an ephemeral port, drive
     a decision over a real socket, and reap the child in a `finally`. The
     distinction relied on: a *server* outlives the run and belongs to
     `deploy-agent`; this child exists for one test and is killed if it does
     not terminate. It fails loudly rather than skipping when GES does not
     bind. **Register 19 stays open** — no suite in one interpreter can witness
     that an api module cannot `import ges.executor`.
  4. **A persona is asserted before anything that depends on it.** The persona
     switch is the only body-bearing POST the `ux` suite makes, so its silent
     failure was invisible. `_as_controller` now asserts the switch took
     effect, which makes the whole controller class sensitive to it rather than
     only the scenarios that happened to read `aria-current`.

- **2026-07-31 — Gate 7 pass 5, LOOP-BACK FROM GATE 9: the four missing detector
  families, and three green checks that claimed more than the register permits.
  Judgement calls by `code-agent`.** Gate 9 blocked on 94 in-scope unevidenced
  criteria, 39 of them belonging to four detector families that were never
  built. All four are now built, all **eleven** `ARCHITECTURE_KB` §7.3 evaluator
  primitives exist, and `SPECIFIED_BUT_NOT_IMPLEMENTED` is empty.
  1. **The seam applies to our own identifiers.** Nine populations and twelve
     certified queries were first cut named after the tables they read
     (`boundary.fx_revaluation`, `pop.intercompany_pairs`). The physical-object
     denylist correctly refused them, and rather than exempt them they were
     renamed before anything depended on them: a query named after its table
     teaches a detector where its data lives by convention even though no field
     says so. A test asserts `close_datasets.TABLES` is a subset of the
     denylist, so a thirteenth object added without one fails the build.
  2. **`AC-F26-06` is two facts and the code now distinguishes them.** A
     resolver query that ERRORS means the dataset is unavailable — the leg
     reports `not_run` and names the missing dataset from the catalogue GES
     publishes. A resolver that RUNS and returns nothing means nobody declared
     anything to check — the run is refused, and naming a dataset there would
     point at one that is present and empty.
  3. **An unrun check RAISES when asked for its findings.** `[]` is the same
     object a check that found nothing produces, and `coverage()` returns
     `None` rather than `0`. This is the whole content of `AC-F26-06` and
     `AC-F28-07` and it is held by the shape rather than by a caller's care.
  4. **The five F28 checks are a CONSTANT the runner iterates**, not a list it
     accumulates from whatever returned something. A comprehension over "the
     checks that produced output" is the one-line change that breaks
     `AC-F28-06` and `-07` at once, so the shape makes it impossible.
  5. **F28 does NOT use the all-clear vocabulary its own criteria use.**
     `app/conclusion/lint.py` gives `conclusion/render.py` a monopoly on the
     three all-clear phrases across `app/`, `ges/` and `common/`, and that
     monopoly is worth more than matching a criterion's wording. An all-clear
     is a statement about a POPULATION produced by the conclusion type from a
     coverage set; an A6 status line over 24 members is not one, and the
     fastest way for it to start reading like one is to borrow the words. The
     three states are `failed` / `no_finding` / `not_run`.
  6. **The pilot warehouse deliberately OMITS one object.** `AC-F28-07`'s
     "not run" is the state a reviewer most needs to recognise, and a pilot in
     which every dataset is present never shows it. It is an object that does
     not exist, not an empty table: an empty table answers with zero rows, and
     a check concluding from zero rows that it found nothing is the failure
     convention C2 forbids.
  7. **F9's narrative leg is a peer, structurally.** Its own primitive, its own
     manifest, its own fixtures, its own escalation rows, its own
     control-state change — because `DOMAIN_KB` §9 predicts it gets dropped as
     an implementation detail and `ARCHITECTURE_KB` §7.3 says making it
     first-class is the reason it cannot be. A test asserts a numeric leg that
     could not run does not suppress the narrative one.
  8. **F9's escalation period and aggregate come from different parts of the
     run.** The period is where the run first reached the count — the earliest
     moment it was knowable, which is what `AC-F9-01` asks to display. The
     aggregate is over the whole run to date, because `AC-F9-02`'s figure is
     the one a human acts on; reporting it as at the escalation period would
     understate what is owed by two thirds on the pilot's own fixture.
  9. **`AC-F9-04` is applied and READ BACK.** Both legs call
     `DispositionStore.escalate_account` — the same path F32's missed
     prediction uses — and Monitors renders the risk grade fetched out of the
     store. An escalation reporting what it intended to write is a
     notification wearing a control's clothes.
  10. **F33's classification order is fixed and is the thing most worth
      testing.** A posting that crosses a caption also has a different natural
      account from its peers, so testing cost centre first would emit a reclass
      proposal across a caption boundary — exactly what `AC-F33-04` forbids —
      while every cost-centre test still passed. `proposal` is a field that is
      present or ABSENT, never one with a `blocked` flag: the two shapes differ
      in whether forgetting to check a flag produces a posting.
  11. **F33's backtest bias label is enforced in the CONSTRUCTOR and its
      CLAUSES are checked, not its presence.** A paraphrase drifts, and the
      paraphrase that drops "only" is the one that gets written. Its three
      refusals are separate TYPES rather than null fields: `BacktestCouldNotRun`
      (`AC-F33-11`), `NoLabelsAvailable` (`AC-F33-09`), and a constructor that
      rejects `label_count=0` because a record whose denominator is zero is
      still a figure.
  12. **Two floats were reaching a content-hashed dossier.** Peer agreement and
      narrative similarity were Python floats; `common.canonical` refuses
      floats outright because a hash over a binary float is not reproducible
      across platforms. Found by writing the `AC-F33-08` dossier scenario. Both
      are `Decimal` now and both primitives assert their whole output
      canonicalises.
  13. **`AC-REFUSAL-11` stays NOT VERIFIED, and extending the battery produced
      the evidence for that rather than against it.** Going from eight
      paraphrases to twelve found that **four are not refused, and two of the
      four are the criterion's own worked examples.** They are not deleted and
      the shape matcher is not extended: `RESPONSIBLE_AI_KB` §4.1 rules that
      out as an arms race against paraphrase, and it would also concede that
      the criterion is met by whatever the matcher happens to catch this week.
      The battery is now two executed halves, eight refused and four asserted
      as pass-throughs. No scenario in any suite names the ID.
  14. **`AC-F41-08` stops being claimed.** Gate 9's phrasing was exact: it
      passed by asserting that no probe marker exists and the injected-probe
      count is zero — a criterion satisfied by the absence of the thing it is
      about. The UX-11 group says so in its header, no scenario name carries
      the ID, and the zero-count assertion carries an instruction to rewrite
      the group rather than relax it when injection lands.
  15. **The suite transport is bound ONCE.** Two autouse session fixtures each
      installing and uninstalling the pilot transport meant whichever finished
      first left the other suite's screens unreachable, and the failure
      surfaced as an unrelated scenario rendering an outage.

- **2026-08-01 — Gate 7 pass 6, LOOP-BACK FROM GATE 8's re-run: the over-broad
  join and the two registers with no witness. Judgement calls by `code-agent`.**
  Three items, all evidence-honesty, none requiring a new feature. One of them
  required a small build to become honest rather than a smaller claim.
  1. **`AC-F36-47` is EVIDENCED on its precision leg and NARROWED on its
     automation-rate leg — both, not either.** The criterion holds "on every
     screen, in every dossier and in every export"; all three joins tested
     `common.abstention` alone. The choice offered was add the surface
     scenarios or narrow the joins. Neither alone was honest, because two
     different clauses were in different states: the **computation** clause had
     three witnesses and its joins now say so; the **surface** clause was
     genuinely unmet — `PrecisionFigure.render()` carried `abstained` on all
     three surfaces and **every surface dropped it on the way to the reader**.
     So the count is now rendered as a named third figure beside the precision
     figure on `/readiness` and inside every dossier, from one shared
     component, and a new file asserts the surface clause from real routes:
     the screen, all six dossiers, the export payload through a file, a sweep
     of every screen reachable from `/`, and a negative control on the two
     forbidden denominators (`0.8254`, `0.9048`). Removing the two render calls
     fails five scenarios — checked, not assumed.
  2. **The criterion's automation-rate half has NO surface, and that is stated
     as an absence rather than counted as a pass.** `abstention.rates()`
     computes one; no production code renders one. That half is therefore
     vacuous, the scenario is named
     `test_no_automation_rate_figure_is_rendered_on_any_surface_so_that_half_is_vacuous`,
     and it carries an instruction to fail and be replaced when an automation
     rate is built. The **F33 backtest precision** is excluded from the sweep
     explicitly — its denominator is `predicted` over labels, not a
     concluded/abstained split — because a silent exclusion is how an "every
     screen" check stops being about every screen.
  3. **Registers 24 and 25 now have in-file denials, in the style registers 6,
     9, 18 and 20 already carried.** For 24, the stronger form was available and
     was taken: `test_AC_F33_06_…` **derives** `0.6667` and `0.5000` from the
     fixture constants instead of asserting literals, so the provenance is
     executable — the scenario moves with the fixture, which is how a fixture
     property behaves and not how a measurement does — and `test_AC_F33_01_…`
     reads the support threshold from the manifest rather than restating `20`
     as though 20 were part of the criterion. For 25, the denial is
     documentary at five sites, because the claim itself is true on this
     fixture and only the substitution behind it was undisclosed.
     **Both registers stay OPEN.** Nothing in this pass calibrates a threshold
     or supplies a close calendar.

- **2026-08-01 — Gate 7 pass 7, LOOP-BACK FROM GATE 9's RE-AUDIT: the 52
  in-scope, unevidenced, undisclosed criteria. Judgement calls by
  `code-agent`.** Gate 9's framing was adopted as binding: §27.14 issued no IDs
  for the genuinely out-of-scope material, so **every ID in the file is in
  scope by construction** and "out of scope" was not available as an answer to
  any of the 52. Six commits, five of them real builds rather than reporting
  fixes.
  1. **The emission gate had never been wired to anything.** `decide_emission`
     was built at pass 2c and called by no production module, so §27.4's
     load-bearing criterion had no join — correctly. `POST /ges/emit` now
     exists, `app/emission/gate.py` filters every surface-bound item through
     it, and the gate is a **filter, not a decorator**: `admit()` returns a new
     list, so a denied finding is not something a screen has to remember not to
     render. The pilot plants one emission that fails a real check, because an
     absence check over an empty candidate set passes for the wrong reason.
  2. **`AC-F2-08`'s control did not exist, and building it broke 34 tests —
     which is the evidence it is real.** The version tuple was a literal on the
     Audit screen and was the input to nothing. `check_closure_input` now runs
     BEFORE the identity rules in `Broker.decide`, so there is no path in which
     an eligibility is computed over a partial input set and then discarded,
     and `eligible_approvers` returns the EMPTY SET rather than a partial one.
     Nine existing scenarios now supply a complete stamp, each with a note
     saying why they would otherwise pass for the wrong reason.
  3. **F29's other three sub-types are NOT `expectation_gap`, and the pass-1
     manifest header claiming they were is now corrected.** It was tried first.
     A reversal is owed because a journal said so, not because reversals
     usually happen, and a history-based expectation misses a first-ever one
     entirely. `obligation_gap` is a twelfth primitive, declared in
     `UNSPECIFIED_BUT_BUILT` so `ARCHITECTURE_KB` §7.3's list stays its own and
     an undeclared primitive cannot arrive unnoticed. Where the
     configuration-not-code bound DOES hold it holds in its strongest form:
     three detectors, one primitive, one certified statement, one bound
     parameter between them.
  4. **The routing budget was enforced by nobody**, and its display claimed a
     controller had raised a cap nobody had asked. It is enforced at the
     broker on a new `routing.raise_cap` capability — not a local role test,
     because `AC-F41-17` needs a DECISION ID and a minted one would sit in the
     ledger looking like a broker decision. `user.s.haddad` deliberately holds
     `approve.proposal` and not the raise, so "an approver may" and "a
     controller may" are distinguishable on this fixture. The pilot cap is 3,
     for the reason the pilot warehouse omits one object: at 12 the pilot never
     reaches its cap and the at-cap state is one no reader meets.
  5. **`AC-F1-07` and `AC-F1-10` are held by the SHAPE.** `export.build()`
     returns a whole export or raises, so there is no partial value for a route
     to write to disk, and the active-content check runs before an Export
     exists, so there is no object to inspect and then decide about. The
     hardest clause is `AC-F1-04`'s last one — no field renders only as an
     in-application reference — which a parseable, complete-looking file of
     identifiers fails while satisfying every other word.
  6. **`AC-F1-13`'s second clause is the one a shared table could not fail.**
     The scenario empties the application's own control-event log completely
     and reads the separate destination afterwards. What is real is the
     behavioural separation; what is not is the infrastructural one, and
     **register 26 says so** — a green suite here is not evidence that one
     compromised credential cannot reach both.
  7. **Two suite conventions forced two renames and both were right.** `clean`
     is one of the three all-clear phrases `conclusion/render.py` monopolises;
     `statement` is a parameter name the architecture suite refuses anywhere in
     `app/` or `ges/`. Neither exception was taken.
  8. **A session-scoped `GES_CLIENT_TOKEN` fixes an order-dependent failure
     that had just been introduced.** Function-scoped `monkeypatch` UNSETS the
     variable on teardown while the session's cached `GesClient` holds the old
     value, so the next screen fetched renders an outage and which scenario
     fails depends on collection order. Setting it once at session scope makes
     every nested patch a patch to the same value.
  9. **Three register entries opened, and one register correction accepted.**
     26 (the audit domain's infrastructural bound), 27 (`AC-F36-48` runs
     against a synthetic period where the criterion says real close data — the
     register-24/25-class substitution gate 9 identified), 28 (`AC-F40-17`/
     `-18`'s export-time CUEC probe does not exist, and this build authorises
     on exactly the stored pass state the criterion says must not authorise).
     On `AC-REFUSAL-13`: register 16 was **right** and the evidence was
     missing; three named checks now carry the ID.

- **2026-08-01 — Gate 7 pass 8, THE LAST OF THE GATE-9 LOOP-BACK: the eleven
  criteria pass 7 did not reach. Judgement calls by `code-agent`.** Four
  commits. **Seven of the eleven were unbuilt rather than merely unevidenced**,
  which is a higher proportion than pass 7's five in fifty-two and is the
  expected shape: the ones left last were the ones with no join because there
  was nothing to join to.
  1. **The Ask screen's natural-language box was wired to nothing.** It rode on
     a GET query string to `/exceptions`, which ignored it, so a user could
     type "assess the impairment" and meet no guard at all —
     `AC-REFUSAL-03`/`-05`/`-06`/`-12` were all unbuilt.
     `ges/broker/request_triage.py` is a REQUEST classifier and is deliberately
     not `refusals.classify`, which reads an emission: "Is our AR allowance
     adequate?" contains no assertion, so the emission classifier sees an
     ordinary finding and lets it through. The guard is at the broker, before
     resolution, so a direct API call meets it.
  2. **No answer path was invented.** All three triage outcomes are declines,
     because the F39 resolver's model call site is still not built. The third
     says so by name rather than substituting a nearest metric, which is A25's
     failure mode exactly. `AC-F39-03`/`-05`/`-06`/`-08` remain unmet as
     recorded.
  3. **A refusal always beats a deferral**, unconditionally. A deferral trigger
     that could pre-empt a refusal would be a route to a materiality conclusion
     via a phrasing that also mentions a deferred capability. The cost is that
     "certify that this intercompany reclass is correct" refuses rather than
     defers, and that is the direction to be wrong in.
  4. **The metric versions on the Ask screen were a hardcoded string** —
     `recurring_entry_signature v2.4 - posting_period_join v1.9`, which no
     registry could contradict — and the dossier carried none. `semantics:` is
     now required on every certified query and a functional scenario walks
     every file under `backend/app` asserting no version literal survives in
     the analysis plane. Dossier payload **schema v2** rather than a key added
     to v1's required list, because widening v1 retroactively would declare
     every existing v1 record incomplete — the migration `ARCHITECTURE_KB`
     §23.11 exists to refuse. `_read_v1` stays and is exercised.
  5. **`AC-F42-05` could not be demonstrated on any fixture that existed.** On
     the wedge world utilities is an outlier and bonus has too little history,
     so an F42 run there is bounded and non-clean by construction. A criterion
     about the exception-free full-coverage case needs a world where that case
     occurs, so one was built and declared.
  6. **A thirteenth primitive, and the reasoning was the same as the twelfth's.**
     `journal_attribute_outlier` is not a parameterisation of
     `distribution_outlier`: `AC-F42-02` requires the ATTRIBUTES that made a
     journal an outlier to be named, and no parameterisation of a
     distance-from-history computation produces that output shape. Magnitude is
     deliberately NOT scored, so the two legs cannot double-report one anomaly.
     Base rates come from the history only, so a period-end spree of twenty
     identical unusual journals cannot make each look normal by the presence of
     the other nineteen. Declared in `UNSPECIFIED_BUT_BUILT` beside
     `obligation_gap`; both for `solution-architect` at gate 10.
  7. **`AC-F40-10`'s tempting implementation was unreachable, which is the
     point.** A `reversed: true` field on the dossier is a modification of an
     evidence record, and this store has no update function and a trigger that
     refuses one below the application. Children name their parent instead: a
     reversal writes one new record, `dossier.read` resolves the linkage on
     read, the original's content hash is unchanged and the period's chain
     still verifies — which a write-back would have broken for every record
     after it.
  8. **`AC-F40-09` was behaviour with nothing saying so.** Nothing revokes an
     approval and `build` raises rather than returning a partial file, so both
     clauses already held; but a user shown "not exported" re-approves, and the
     ledger acquires a second decision record for one act. The refusal now
     states that the approval survives, and the suite's strongest assertion is
     the retry against the same approval.
  9. **The two-key statement had no date.** "Verified per tenant" with the date
     absent is the most flattering possible reading of the CUEC residual, which
     is a validity WINDOW — and a window with no start cannot be evaluated. The
     OLDEST verification is stated, not the most recent.
  10. **Two register entries opened.** 29 (metric and join versions are
      declared on the certified query rather than in an independent metric
      store — `AC-F39-04` is satisfied; where the versions LIVE is substituted)
      and 30 (`journal_attribute_outlier`'s threshold is declared, not
      calibrated, with the denial on every emitted finding as well as in the
      header). `obligation_gap` stays a declared twelfth primitive, unreverted,
      per the standing instruction.

- **2026-07-31 — Gate 7 pass 10, THE THREE ITEMS GATE 9 LEFT WITH `code-agent`.
  Judgement calls by `code-agent`.** Three commits. Twenty-six of gate 9's
  twenty-nine NOT VERIFIED criteria need capabilities that do not exist and
  went to `plan-agent` as a scope question; these three did not.
  1. **`AC-F12-05` stops being claimed, and the denial travels with the ID.**
     `tests/suites/ux/test_ux_flow.py:362` carried a join reading "`AC-F12-05`
     is served by this" in a docstring whose **next paragraph** explained what
     it does not establish. Identical shape to `AC-F41-08`, descoped at pass 5;
     this ID was simply left behind. Narrowed to the criterion's third clause,
     with the denial **inside the join string** in the manner `AC-F36-47` and
     `AC-F36-48` are now fixed, so an ID-keyed scan cannot score it satisfied.
     The scenario is kept — it holds for a queue containing probes as well as
     one that does not, which is its whole value. Register 18 broadened to
     cover both IDs.
  2. **Supersession by DATA is BUILT — `AC-F41-14` and `AC-F41-15`.** Gate 9:
     *"Nothing in the record says this capability was not built; it is simply
     absent from every artefact except the criteria that require it."*
     `ARCHITECTURE_KB` §18.1 had predicted exactly that outcome. `AC-F41-12`
     covers a run superseded by a later RUN; the more common real case is a run
     superseded by later DATA, and nothing in the build touched it.
     `ges/supersession.py` implements §5.5's `run_dataset_binding` table and
     the worker's index lookup; the enforcement is bundle rule
     `scope.no_bound_dataset_superseded_by_later_data`, not override-eligible
     because `AC-F41-14` demands `AC-F41-12`'s loud treatment rather than a
     dismissible warning.
  3. **The judgement call inside item 2, recorded because the plan did not
     specify it.** `AC-F41-15`'s negative half is expressed **in the predicate**
     as `!(bound_dataset_ids intersects datasets_superseded_since_binding)`
     rather than as a precomputed boolean. Two consequences, both intended: a
     watermark on a dataset the run never read cannot fire the rule *even if
     the registry reported it*, and the rule's **non-firing fixture is that
     exact case**, so every build verifies the negative half at compile time. A
     build that blocked on any watermark movement would pass `-14`, fail `-15`,
     and be switched off within a week of meeting a nightly warehouse.
  4. **Both context fields are resolved server-side at `/ges/decide`** and any
     caller-supplied value is discarded with a control event — the same
     reasoning that keeps the principal out of the request body. They travel as
     `resolved` rather than in `payload` and are therefore **not part of the
     action digest**: the digest binds what the caller asked for, and folding
     server state into it made an approved proposal stop matching its own
     export the moment the warehouse moved. That was caught by four existing
     export scenarios failing, and is recorded here because it is a real
     constraint on anything else server-resolved later.
  5. **The supersession worker is not a scheduled process in MVP1.**
     `observe_watermark` is called by whatever observes the warehouse; in this
     build that is the suites and the pilot launcher. The registry's default
     state is EMPTY, which is `AC-F41-15`'s state — a deployment that has
     recorded no binding is permissive, not unable to approve anything. Stated
     rather than papered over: nothing here schedules the observation.
  6. **The pilot binds `ds.gl_balances` and `ds.journal_lines` and deliberately
     NOT `ds.subledger_ap`**, so `AC-F41-15` is demonstrable in the running
     pilot rather than only argued — a catalogue dataset whose watermark can
     move without touching this run's approval. The seed carries no
     observation, so the pilot's default screen shows no notice at all.
  7. **Corpus date ruling applied.** The nine `test-evidence/*.md` headers now
     read `2026-07-31`, matching their filenames and every `dev/` commit;
     `register-cross-check`'s advisory `D1` and this file's `D1` record the
     ruling instead of the discrepancy; and the Test Results heading and the
     `test-evidence/*-2026-08-01.md` path — which pointed at files that no
     longer exist — are corrected. **Not changed, and flagged rather than done
     unilaterally:** five decision-log and register lines above still carry
     `2026-08-01` as the date of passes 6–8. They are prose about when work
     happened, not paths, and rewriting five history entries is a call for the
     orchestrator rather than one to make inside a hygiene item.

- **2026-07-31 — Gate 7 pass 12, SCOPE-RULING BATCH B: the probe programme and
  the F39 resolver. Judgement calls by `code-agent` the plan did not fully
  specify.**
  1. **A probe's correct answer is a SET of responses, and a structured
     rejection is one of them.** The plan said the probe is a known-error item
     and the capture records whether the reviewer was right; it did not say
     what "right" is. Scoring only the resolution type would have marked the
     sharpest possible response to a manufactured error — *the evidence does
     not support this finding* — as a miss, which trains exactly the deference
     the programme exists to measure. `ProbeSpec.correct_responses` therefore
     holds both `R2` and a rejection on `evidence_insufficient`, and the stored
     separator is a pipe rather than a comma because rejection labels contain
     commas.
  2. **The probe is injected BEFORE the emission gate, not after it.** A
     manufactured item that took a different route into the queue than a
     genuine one is distinguishable by that route, and `AC-F41-08` is about
     there being no such difference. A probe the gate withholds is simply not
     in the queue.
  3. **`AC-F1-04` and `AC-F12-16` are reconciled rather than traded off.** The
     export must contain every dossier for the period; a probe must appear in
     no export. Both hold only because the completeness statement now names how
     many manufactured items it excluded — an export that dropped rows silently
     while claiming completeness would be worse than either failure alone.
  4. **The probe's risk tier and resolution set were chosen to MATCH a genuine
     item's.** Not cosmetic: those two properties set a class name and a field
     set in the rendered DOM, they differ legitimately between genuine
     findings, and the indistinguishability comparison is only meaningful with
     them controlled for. A scenario asserts the comparator is a fair one, so a
     future change to either item's tier fails there with the reason rather
     than in the indistinguishability check with an uninterpretable diff.
  5. **The pilot's injection SEED is chosen; the rate is not.** Seven items and
     a 2–8% band yield no probe about seven times in ten. Recorded as register
     32 with the consequence stated: nobody may read the pilot's probe count as
     evidence about the rate.
  6. **`OUTCOME_UNRESOLVED` is renamed `OUTCOME_PASSED_TRIAGE`.** Its value was
     `not_resolvable_in_this_release`, which asserted no resolver existed. One
     does, so the name would be false, and the honest cost of building the
     resolver is that triage no longer gets to say it.
  7. **The resolver holds NO refusal check of its own.** The ordering condition
     is enforced by call order in `ges.main` alone. A second copy would be a
     second thing to get wrong, and the copy is the one that eventually
     matters. A functional scenario probes five refusal-shaped requests that
     each name a subject the resolver CAN map, so the order is proved rather
     than read off the source.
  8. **Coverage where no member resolver exists is UNKNOWN, never complete.**
     Four of the populations have a certified member-resolver query and the
     rest do not. Reporting the rest as fully covered would be the single most
     dangerous rounding in the product; register 33 records it.
  9. **The A20 re-run against the resolving path found something worse than
     expected, and it is recorded as a finding rather than smoothed.** The
     brief anticipated that an evading paraphrase which used to hit a decline
     would now hit an answer, and it does. What was NOT anticipated:
     **eleven of the twelve RT05 paraphrases are not refused at the request
     surface at all**, including all eight the emission broker refuses under
     A20 — the two matchers have always been different sets over different
     objects, and that asymmetry stopped being harmless the moment there was
     something downstream to evade into. `RT05_AT_THE_REQUEST_SURFACE` commits
     the map so either matcher changing fails it. `AC-REFUSAL-11` is claimed
     nowhere.
 10. **The UX suite now restores the run tier after every scenario.** The leak
     had been mopped up by accident: the last UX-11 scenario called
     `state.reset()` for its own reasons, which incidentally put the tier back
     after `/ask?tier=exploration`. Rewriting that scenario against a real
     probe took the mop-up with it and a later journey scenario started
     failing. Restoring the tier explicitly is the fix; relying on another
     scenario's side effect was never one.

- **2026-07-31 — Gate 7 pass 13, LOOP-BACK FROM GATE 8: the smoke failure, the
  second state leak, and two guarantees that were described rather than held.
  Judgement calls by `code-agent`.** Four commits, one per finding. Three of
  the four were things this build *claimed* and did not do; none needed a new
  feature; all four now have a check that fails when the fix is removed.
  1. **A persisted warehouse is MIGRATED, and the migration is a rebuild.**
     `seed()` created every object with `CREATE TABLE IF NOT EXISTS`, so a
     warehouse file written by an earlier build was never migrated —
     `var/warehouse.sqlite3` predated register 31's POAR work and the export
     path returned 403 `revalidation_could_not_run`, "no such column:
     period_status", on the pilot as found. It rebuilds rather than `ALTER
     TABLE ... ADD COLUMN`: this is derived fixture data, and a NULL column
     bolted onto rows that predate it produces a warehouse that ANSWERS rather
     than one that refuses, which is worse than the failure it replaces. It
     rebuilds **all** declared objects rather than the stale ones, because
     dropping one and then hitting the row-count idempotence guard leaves the
     recreated table empty — the same defect one layer down. The declared
     schema is read back out of SQLite's own parser rather than restated as a
     second column list, since a second list is the thing that would be wrong.
  2. **An object declared ABSENT but present is a gap too**, and this is not
     pedantry: the pilot omits `fx_revaluation` so `AC-F28-07`'s "not run"
     state is reachable, and a persisted file from an earlier full seed
     silently puts it back — the state a reviewer most needs to recognise
     disappears with nothing failing. Extra tables and extra columns are NOT
     gaps: a customer's warehouse legitimately carries more than we read, and
     a check that refused it would refuse every real deployment.
  3. **The runtime path gets a CHECK, not a migration.** `schema_gaps()` /
     `assert_schema_current()` are public because in a deployment the
     warehouse is the customer's and we connect read-only. What a deployment
     can do is say so up front naming the warehouse, rather than let a missing
     column surface three screens later as a refused export naming a column.
  4. **`seed()` may not return leaving a warehouse the queries cannot read**,
     asserted on both exits. The whole suite was structurally blind to this
     because every warehouse in every fixture is built fresh under `tmp_path`;
     `ARCH-05` now drives the pilot's own `seeded_dev_warehouse()` bootstrap at
     the persisted default path and executes `poar.export_basis@1` through the
     real execution route.
  5. **The viewer session is restored by CONSTRUCTION, and the declared set
     lives in production code.** Gate 8's permutation run found the persona
     leaking out of `TestUX14ControllerNightOverMonitors`, and the dangerous
     part is that the staff-accountant scenario still passed **three of its
     four assertions** as a controller — only the denial reason differed.
     Pass 12's `_restore_run_tier` restored ONE NAMED ATTRIBUTE and was blind
     to the persona beside it, which is why the fix is a declared set
     (`app.ui.state.VIEWER_SESSION_ATTRS`) restored by one autouse fixture in
     each conftest, not a second named fixture. Not `reset()`: rebuilding the
     pilot close would restore the persona as a *side effect* of rebuilding
     everything, which is the accidental mop-up being replaced.
  6. **The invariant the generic restore rests on is asserted from the AST.**
     The only public attributes of `PilotState` assigned outside `__init__`
     are `persona` and `tier`; an undeclared third fails
     `test_ui_state_session.py` on the day it is written rather than on the day
     a suite is run in a different order. Both existing leaks were found by
     accident — one when an unrelated scenario was rewritten, one when gate 8
     reversed the collection order — and neither was found by a check.
  7. **The leaking scenario asserts its own subject first.** It now fails on
     "I am not a staff accountant" rather than on a denial reason, which is
     the difference between a scenario that breaks and one that changes
     subject. Both legs are kept: the source fix means no scenario has to
     remember, the assertion means this one cannot be wrong about who it is.
  8. **An export that states nothing about its own evidence cannot be
     constructed.** Gate 8 disproved the "no default is a structural
     guarantee" claim twice: restoring `integrity = {}` left all 2,602
     scenarios passing, and `Export(..., integrity={})` constructed cleanly
     with its JSON naming neither `AC-F1-11` nor `AC-F1-08`. Required is not
     validated, because `{}` is a value. Made real rather than stopped being
     described, and the requirement is on **content**: where the residual is
     declared — the anchor is a stub, retention is not enforced — the
     disclosure must name its unmet criterion, because `AC-F1-04`'s reader has
     no application login and a section saying only `is_stub: true` tells them
     nothing. The rule is satisfiable in the other direction too, so the day
     register 3 or 4 closes it is updated rather than deleted. **Registers 3
     and 4 are unchanged and still open**: this makes the disclosure
     unremovable, it does not sign an anchor or lock an archive.
  9. **An unknown run tier is refused, not ignored** (advisory A2, carried).
     `select_tier` ignored unknown values under a docstring claiming a
     fallback to certified; from a fresh process the typo rendered `certified`
     because that was the initial value, and after `?tier=exploration` it
     rendered exploration. Neither silent reading is safe — the stricter tier
     runs something the caller did not ask for, the current one runs something
     somebody else asked for — so the request is refused with a 400 naming the
     value, the same shape as the unknown-persona refusal.
  10. **NOT FIXED, and stated rather than left for the next permutation run.**
      Every suite is order-clean in isolation (all seven reversed; `ux` and
      `functional` additionally under three shuffle seeds each), which is the
      permutation gate 8 ran. **A whole-tree shuffle that interleaves
      `backend/tests` with `tests/suites` is NOT clean** — three failures at
      one seed, one at another. It is a **wider class than the viewer session**
      (the pilot's accumulated dispositions, workflow records and probe queue,
      not persona or tier) and it **reproduces at `9d819c1` with different
      scenarios failing**, so it predates this pass. It is recorded here
      because it is the same family and the honest reading of "restored by
      construction" is that it now covers the viewer session and not the
      pilot's mutable stores.

      **CLOSED at pass 14.** See the pass-14 entry below.

- **2026-08-01 — Gate 7 pass 14: the interleaved-shuffle order dependence,
  fixed at the level of the class. Judgement calls by `code-agent`.** Two
  commits (`f90484e`, `fc197a6`). Pass 13 item 10 disclosed this rather than
  fixing it; the orchestrator declined to record an override, and it is now
  closed. The cause was **not** one class but two, and both were process state
  that nothing restored:
  1. **The pilot close accumulated, and the viewer-session restore snapshotted
     too late.** Pass 13's snapshot/restore pair covered the persona and the
     tier and left the dispositions, the workflow records, the probe queue and
     the produced exports untouched. Worse, the snapshot was taken by a
     FUNCTION-scoped fixture while pytest builds higher-scoped fixtures first:
     a module-scoped fixture that walks every screen follows the real
     `/ask?tier=exploration` link, so the "before" value was read from an
     already-polluted process and the restore put the pollution faithfully
     back, permanently. That is the whole of gate 8's `no control event was
     recorded for a refused selection` — an exploration-tier run is not
     action-capable, so the precheck the scenario drove was never the refusal
     it was written about.
  2. **DISCARD, NOT UNWIND, and at setup as well as teardown.**
     `app/process_state.py` drops the `PilotState` instance and
     `app.pilot_close`'s held runs. There is deliberately no rollback list:
     every store hangs off the discarded instance in a temporary directory of
     its own, so a seventh accumulating member is covered on the day it is
     added rather than on the day somebody extends a list. Setup as well as
     teardown, because teardown cannot reach what a higher-scoped fixture did
     before the first scenario in its scope ran. `app.pilot_close` is a
     declared holder because the F9 run it holds is passed the **disposition
     store**, so a result first computed after a scenario closed items is a
     held result about that scenario's close.
  3. **The guard is an AST classification, not an enumeration of mutations.**
     Every module-level mutable binding in a participating module must be
     declared by whoever writes it as either a holder (discarded) or a frozen
     lookup table. That is what keeps "discard `_STATE` and `_CACHE`" a
     COMPLETE restore: a module-level dict added tomorrow is somewhere else
     for state to live, and no existing check would notice it.
  4. **Two session fixtures each bound a transport, and binding is
     last-one-wins.** The unit tree and the SME suites each built a GES app
     over a broker store of its own, so which store the application recorded
     decisions into was decided by which tree's first scenario ran first —
     `test_AC_F40_09...: TypeError: 'NoneType' object is not subscriptable`,
     a scenario reading back a decision it had just caused and finding it in
     the other tree's ledger. `backend/pilot_test_binding.py` binds once per
     process and hands both fixtures the same store.
  5. **GES-side state is REBUILT between scenarios, not cleared.** The broker's
     decision ledger, the routing ledger's caps and routed counts, the CUEC
     register and the supersession registry's observed watermarks all
     accumulate across a session. UX-14's `AC-F36-19` scenario, whose own
     docstring says a rate read off a ledger somebody else filled proves
     nothing, was reading a `2` where it had caused a `0`. Rebuilt rather than
     cleared for the same reason the close is discarded rather than unwound.
     The warehouse is the one thing reused: the application never writes to it.
  6. **One scenario genuinely depended on prior state and now sets it up
     itself.** `test_AC_F36_29_each_record_states_which_kind_it_denied_as_a_
     field_not_a_guess` read the decision ledger as it found it, which meant it
     was really asserting that the scenario collected before it had run first.
     It now produces its own action denial and emission denial through the two
     real routes and additionally asserts `action` is present — asserting
     **more** than before, not less. No scenario was weakened.
  7. **The runtime cost was accepted, and it is large.** The whole tree in file
     order goes from **56s at `55878c9`** to **169s** — 3×, +113s — because
     every scenario now rebuilds the GES-side state and discards the close.
     Interleaved runs are 171–278s depending on order and machine load. The
     cost is the price of a result that does not depend on collection order,
     and it is recorded here so gate 8 and `deploy-agent` are not surprised by
     it. It is confined to the test process: no application path changed.

- **2026-08-02 — Gate 7 pass 15: the last two in-scope undisclosed criteria.
  Judgement calls by `code-agent`.** Four commits (`a1850a5`, `faf6117`,
  `4e5ee47`, `75f5e27`). Gate 9's final audit left 255 VERIFIED, 5 DECLARED and
  exactly two in-scope undisclosed; both were pre-existing and both are now
  covered. **No register entry was opened** — every clause of both criteria
  turned out to be evidenceable, which was not certain going in.
  1. **`AC-F36-33`'s comparator was a comment, and is now a component.** The
     criterion asserts that `restates_periods` is set by the comparator and is
     unwritable from any agent path. Ownership was asserted at
     `ges/broker/context_schema.py:98` and nowhere else, and all four G-RESTATE
     scenarios *supplied* the field as an emitter-side keyword argument — the
     exact state the criterion forbids. `RESPONSIBLE_AI_KB` RAI-ARCH-3 has
     wanted this since pass 2c, which reported the field unwritable while the
     thing that populates it was unbuilt. `ges/restatement.py` is now that
     thing: prior-period narratives per account, Jaccard overlap of normalised
     word sets over a configured threshold, strictly exceeded.
  2. **Unwritable is enforced at three named paths, not documented at one.**
     The pair are private slots behind read-only properties on
     `EmissionRequest`, writable only through `apply_restatement`, which
     demands a `RestatementVerdict` — a type minted in exactly one place, so a
     dict of the right shape is refused. The constructor, attribute assignment
     and the HTTP body each fail with a named refusal and each record a
     `restatement_field_write_attempt` control event. **Refused rather than
     silently overwritten**, which is where this departs from the
     supersession-by-data precedent it otherwise copies: `/ges/decide`
     discards a caller-supplied supersession state, and `AC-F36-33` says the
     attempt *fails*. A caller quietly corrected is a caller that keeps trying.
  3. **The comparator runs BEFORE the broker, and records only on an ALLOW.**
     Before, so the value the predicates see is the comparator's and there is
     no window in which the request carries anything else. Only on an allow,
     because an agent that could seed the narrative history out of denied text
     would control the baseline its next emission is measured against, and a
     control whose reference set the subject writes is not a control.
  4. **The four existing G-RESTATE scenarios were STRENGTHENED, not
     rewritten around.** Each now derives its restatement state from the real
     comparator instead of stating it, so the escalation scenario's count of 3
     is an off-by-one the comparator can now fail. Two of them moved their
     priors to non-adjacent periods so the escalation rule is not also firing
     and the denial reason each asserts is unambiguously the rule it names.
     **No scenario asserts less than it did.**
  5. **`AC-F36-30`'s Then clause is covered by the FAILING case.** Its only
     ID-bearing join scoped itself, in its own words, to "the precondition".
     The criterion's requirement is that the suite *fails* when an emission
     constraint lacks a fixture, so a check confirming it passes when
     everything is present would not have covered it. Seven node ids added,
     parametrised over both fixture directions — a constraint that can no
     longer be shown NOT to fire is as unevidenced as one that can no longer
     be shown to fire. A passing baseline is seeded and asserted passing first,
     so the failure is the missing fixture rather than `AC-F36-24`'s
     inconclusive first run.
  6. **The live-bundle join is asserted, not assumed.** A fixture cannot be
     removed from the bundle directory in force, so those scenarios work on a
     copy; a scenario of its own asserts the copy compiles to the same bundle
     hash. Without it, three scenarios could quietly have been testing a bundle
     nobody uses. `bundle.yaml` itself was not touched, so no hash moved.
  7. **The suites stopped writing to the developer's live decision ledger.**
     `tests/suites/conftest.py`'s `ges_http` called `create_app` with no
     `broker_factory` and fell through to `default_store_path()`;
     `dev/var/broker_db.sqlite3` had reached 10 MB. It contradicted that
     module's own docstrings in two places, it sat outside
     `pilot_test_binding.rebuild()`'s reach — the one piece of GES-side state
     the per-scenario restore could not touch — and it made a fresh clone and
     a developer's machine two different starting states. Guarded by an
     architecture-suite scenario that drives a real emission, reads the
     decision back out of the suite's own store, and asserts the live ledger's
     size is byte-identical across the request. **Verified to fail with the fix
     reverted.** The existing 10 MB file is git-ignored local residue and was
     left in place rather than deleted: it may contain a developer's own pilot
     runs, and that is not `code-agent`'s call to discard.
  8. **The AST guard's set of participating modules was itself an
     enumeration.** Pass 14 item 3 established the classification guard;
     `test_pilot_process_state.py`'s own docstring already said a wrong
     `PROCESS_STATE_MODULES` would be invisible — "the two modules it names
     would keep passing their own guard while a third accumulated freely
     beside them". `app.ges_gateway` was that third module: the bound
     transport, the per-principal client cache, seven named snapshot/restore
     sites across both test trees, and no guard had ever scanned it.
     **Split rather than widened**: `PROCESS_STATE_MODULES` is what `restore()`
     DISCARDS, `EXTERNALLY_RESTORED_MODULES` is what is restored by rebinding
     instead, and `GUARDED_MODULES` — the union — is what the classifier scans.
     The gateway is deliberately not discarded, because resetting it between
     scenarios would unbind the GES application every screen is reached
     through; that half is asserted too, so moving it into the discarded set
     cannot look like a tightening.
  9. **What this pass did NOT do.** No register entry was opened or closed;
     registers 3 and 4 stand. The five declared criteria (`AC-F1-08`,
     `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`) are claimed
     nowhere, and nothing here touches them. No guardrail moved to the UI, no
     SQL-typed parameter was introduced, no dependency was installed, and
     `prod/` was not touched.

- **2026-08-02 — Gate 7 · Code, pass 16 (two narrow items). Judgement calls by
  `code-agent`.** Two commits (`4790f8b`, `9d605b1`). Both items are HARNESS
  defects; neither changed product behaviour, and no criterion's coverage
  moved.
  1. **`AC-F12-15` is now asserted as a NUMBER, at all four sites.** Gate 8's
     `reverse` ordering failed
     `test_AC_F12_15_the_rendered_dom_carries_no_probe_rate` on a rendered
     timestamp — `...T07:04:40.023468+00:00` contains the substring `0.02`,
     the disclosed band's low bound — while both of the scenario's substantive
     clauses passed. The assertion was wrong in the OTHER direction too, and
     that mattered more: `0.020` is the same rate and not the same substring,
     and every rate `plan_injection` can actually draw lies strictly *between*
     the two bounds, so the leak the criterion is about was never in the old
     assertion's reach. `conclave_harness.rendered_numbers` tokenises the
     page's standalone decimal literals and refuses any that lands in the
     closed band — strictly stronger than the two endpoints, and immune to
     timestamps, grouped money and dotted versions by construction. Fixed at
     all four sites (functional DOM leg, functional API leg, UX-11, and the
     unit-tree sibling), which previously made three different versions of one
     claim. **Known limit, asserted rather than hidden**: a bare-point decimal
     like `.05` is not a token; no template in this build renders one, and
     widening the token would make every sentence boundary a number.
  2. **The guard against the developer's decision ledger watches the RESOURCE,
     not one named fixture.** Pass 15's fix (item 7 above) was scoped to the
     suites' `ges_http`, so it passed straight over `backend/tests`, where
     `ges_app` and `ges_stack` had the identical defect and
     `test_emission_gate.py` was still adding 17 rows and 32,768 bytes per
     run. Both fixtures now inject a `tmp_broker`, AND
     `conclave_harness.live_ledger_guard` refuses the *construction* of a
     `BrokerStore` over the live path from either tree — so
     `default_broker_factory`, `pilot.py`, a fixture not yet written and a
     tree not yet created are all covered, rather than the callers known
     today.
  3. **The guard deliberately does not patch `default_store_path`.** That
     function must keep returning the real path, or the architecture suite's
     file-size scenario from pass 15 would pass vacuously. The guard raises
     *and* records: `raise_server_exceptions=False` turns the raise into an
     anonymous 500, so a session-end sweep is what fails the run with the
     message and the name of the test that caused it.
  4. **The guard is refcounted, because the first version was wrong.** It
     built a new guard per caller and laid a second patch over the first, so
     with both trees in one session the outermost patch recorded refusals on
     one guard while a test asserted on the other. Invisible in file order,
     where the trees do not interleave; three failures under `seed:1`, which
     is how it was found and is the reason the ordering matrix is run rather
     than reported. Both conftests now hold the same guard, and one holder
     letting go does not disarm it for the other.
  5. **Package named `conclave_harness`, not `harness`.** `tests/suites/ux/`
     already has a module called `harness`, and a shared helper that shadows a
     suite's own import is a helper that breaks the suite that adopts it.
  6. **New modules carry their own unit tests**: 25 for `rendered_numbers`
     (including the exact timestamp that broke the suite and the `0.020` case
     the old form let through) and 12 for `live_ledger_guard` (each deliberate
     violation drained, so the session sweep is not failed by its own
     evidence).
  7. **The existing `broker_db.sqlite3` was left in place**, as at pass 15 and
     for the same reason: it may hold the human's own pilot runs.
  8. **What this pass did NOT do.** No register entry opened or closed. The
     five declared criteria are claimed nowhere and were not touched. No
     guardrail moved to the UI, no free-form SQL or SQL-typed parameter, no
     Oracle posting credential, no journal-submission library, no suite
     stubbed green, no ID claimed that a check does not cover, no dependency
     installed, `prod/` untouched, and no server started — the human's pilot
     on 8030/8031 was left alone and 8021/8022 were never bound.

- **2026-08-03 — Gate 7 pass 17 (`code-agent`): the approved UX redesign,
  `UX_KB` Part A2, built.** Six judgment calls the plan did not fully specify,
  recorded because each is a place a later reader would otherwise have to guess
  at.
  1. **The merged queue keeps three addresses.** `UX_KB` A2.2 merges Exceptions
     and Review into one queue. `/exceptions` and `/review` were not removed:
     a great many acceptance criteria name those addresses, and a criterion
     pointing at a screen that no longer exists is a criterion nobody can
     check. All three render the same screen, byte for byte, and the two old
     ones are declared in `routes.SCREEN_ALIASES` — product code, so an alias
     cannot be added by widening a constant in a test file.
  2. **The dossier now carries exactly one link, and that is a narrowed
     check.** `UX_KB` A2.2's eighth graph edge is the dossier's way back to the
     finding it evidences; the exhibit previously carried none at all, and
     `test_ui_dossier` asserted `hrefs() == []`. The self-containment substance
     is unchanged and still asserted — no external reference of any kind, so
     the document fetches nothing and renders identically offline — and the
     narrowed check is "exactly one link, the back-reference, relative and
     same-origin". `AC-F41-04`'s retained view is `state._retained_view`, which
     is assembled separately and still carries no anchor. **If zero anchors on
     this screen was the intent, that is `functional-design-agent`'s ruling and
     was not made here.**
  3. **Gold is narrower than `UX_KB` A2.8 specifies, in the direction of the
     brand's own rule.** The brand law is "gold means a human decision". It is
     bound to the one Approve control, the seal recording that somebody used
     it, and the Council Mark's pull-line and terminus dot — the human above
     the machine, the same meaning. A2.8 also gives gold to the six section
     icons and to `.goldline`; neither is a human decision, so the icons take
     `--ink-3` and `.goldline` is not carried at all.
  4. **The readiness selector is links, not a picker.** `test_ui_boundaries`
     refuses a `<select>` on every screen in this build, because a picker is
     one control away from a multi-select and `AC-F41-01` forbids a bulk
     affordance at every permission level. Links also give each agent's
     readiness its own address, which is the defect A2.1 actually recorded.
  5. **Four of the five agents have no readiness evidence, and say so.**
     `SKILL_OBSERVATION` holds one entry. The others report every condition
     `not_yet_evaluable` with the window named, and no precision figure is
     rendered for a skill it was not computed for. Inventing an evidence window
     to make four more reports look complete is what `AC-F12-21` exists to
     stop.
  6. **A real disagreement is rendered rather than tidied away.** The ids
     findings are authored under (`agent.omission-detector`) and the ids the
     principal registry publishes (`agent.omission_detector@1`) are not the
     same strings. The agent page states this on its own face. Dropping the
     unmatched agents would have made the object graph look complete and made
     the disagreement invisible — the failure `AC-F5-06` refuses for retired
     agents, in a new place.

- **2026-08-03 — Gate 7 pass 19, SECOND LOOP-BACK FROM GATE 8: the three
  findings of `register-cross-check-2026-08-03.md`. Judgement calls by
  `code-agent`.** Three commits (`3fc105f`, `9ce09cc`, `e00a214`), one per
  finding. **No register entry opened or closed**; registers 33 and 34 both
  gain a correction described below, and 34's "built instead" list is now held
  by scenarios in all three of its parts rather than two.
  1. **F1 — the claim a screen dropped was still standing on the four it links
     to.** Pass 18 removed *"An agent that can act is an agent that is
     listed"* from `/inventory` and left it in the subtitle of all four
     `/evidence/agent/<id>` pages, four lines above the block stating that
     THAT agent acted and is in no registry. Register 34's wording ("gone from
     that screen") was literally true and is not contradicted; the fix is the
     four pages plus the scoping. **The guard is now the surface, not a named
     screen**: every URL reachable from `/` by following real links, plus every
     document that exists only as the result of operating a control, and it
     asserts the four agent pages are IN that traversal so it cannot pass by
     reaching nothing. The subtitle now says what is true — the page is the
     agent, and not every agent that acted has a registry entry, with the
     Inventory named as where the gap is.
  2. **F1's own mutation found a second unheld claim.** Register 34 credits
     `/inventory` with *"links each to its agent page"*. Repointing all four
     hrefs at `/inventory` left all 2,977 scenarios green — the link was
     credited and held by nothing. The disclosure scenario now follows each
     link and asserts it lands on that agent's page. Note for the record: the
     whole-surface guard does NOT catch that mutation, correctly — the agent
     pages stay reachable through the object graph's finding→run→agent chain,
     so the traversal is not vacuous either way.
  3. **F2 — `AC-F5-07` built, not deferred, on `test-agent`'s ruling.**
     `code-agent` declined this at pass 18 as a Plan-gate call. The ruling
     came back that nothing needs narrowing: the build satisfies "each agent"
     today and the scenario merely sampled `agents[0]`, so asserting every row
     is **strengthening an under-asserting test**, not changing scope. It is
     accepted and built. Every agent row, labels AND values, joined to the
     broker's own payload — so a label rendered over a neighbour's version
     fails too. The sibling `a_lineage_view_is_reachable_for_each_listed_version`
     asserted `len(lineage) == len(rows)`, which eleven views all belonging to
     one agent would satisfy; it asserts containment now. **The criterion's
     status is unchanged** — it was met before this pass and is met after it;
     what changed is that a check now holds it.
  4. **The sampling sweep, and what it is not.** Swept both trees for the same
     shape — a criterion or scenario name saying each/every, a check reading
     `[0]`, `[-1]`, `.first()` or `next(iter(…))`. 39 candidates, **5 real**,
     all fixed in the same commit: `obligation_gap`'s "each kind" named two of
     the three kinds in `KIND_VOCABULARY` and left `intercompany_counterparty`
     unasserted (now parametrised over the mapping, plus a check that no two
     kinds share a label, since "in its own words" is a claim about
     difference); `distribution_outlier`'s "every anomaly" read one finding of
     one run in the above direction only; `AC-F40-16`'s "every produced file"
     read `entries[-1]`; `AC-F38-01`'s nine attributes were pinned on one
     catalogue card of three; and the export reconstruction fields were
     asserted on `dossiers[0]` of a one-dossier export. The other 34 are
     legitimate — a header row, a string split, or a population the scenario
     first asserts has exactly one member. **This is a sampling fault and not
     the `AC-F5-02` tautology fault**: these checks could always have failed
     for the right reason, they just did not look.
  5. **F3 — `unregistered_actors` is UNKNOWN, not none.** It returned a bare
     `[]` while four unregistered actors existed, was asserted by nothing, and
     **could not become non-empty in this build**: it is a set difference over
     the decision ledger and findings are not ledger-recorded, which is
     `LINEAGE_UNTRAVERSED`'s own second entry. Register 33's convention C2 in
     its population form, in the same shape `resolver._population_coverage`
     already uses — `computable: False`, the scope, the untraversed class, and
     a statement saying UNKNOWN rather than none. The ledger difference is
     still returned under a name that says what it is, because suppressing a
     true fact would be a second rounding. **Two scenarios**: one asserts the
     SHAPE rather than the emptiness, so it FAILS the day findings become
     ledger-recorded — **corrected 2026-08-03**. This line originally said it
     *survives* that day. It does not, and that is the design: an UNKNOWN is
     honest only while the ledger cannot carry the answer, so the build change
     that makes it answerable must force this scenario and its text to be
     revisited. `c428fe5` corrected the docstring; this is the decision record
     that generated the wrong one. A code record and a decision record that
     disagree is the same defect class gate 8 spent five loop-backs finding —
     which is why it is corrected here rather than left as history; the other joins `computable: False` to the
     `LINEAGE_UNTRAVERSED` entry that justifies it, so the UNKNOWN cannot
     outlive its reason.
  6. **The broker's answer is rendered on `/inventory`.** An answer only a
     reader of the payload ever meets is the shape this project keeps finding,
     and the register already credits this field as disclosure. The screen
     renders the broker's own statement string rather than composing a second
     wording of the same fact. It is a new UI element and is asserted through
     the real route, on the screen a reader reaches.
  7. **What this pass did NOT do.** No register entry opened or closed. The
     eight forbidden criteria (`AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
     `AC-F40-17`, `AC-F36-48`, `AC-F5-02`, `-03`, `-05`) are claimed nowhere
     and none was touched; `AC-F5-02`/`-03`/`-05` remain NOT VERIFIED and the
     three scenarios naming them still assert unmet-ness. No guardrail moved
     to the UI, no free-form SQL or SQL-typed parameter, no Oracle posting
     credential, no journal-submission library, no suite stubbed green, no
     exemption table added, no dependency installed, `prod/` untouched, and no
     server started — the human's pilot on 8030 was left running and
     untouched.

- **2026-08-04 — Gate 7 pass 21: `functional-design-agent`'s §28 rulings, built.
  Judgement calls by `code-agent`.** Six commits (`f1a6c07`, `397757d`,
  `87e6cca`, `ced2701`, `27b832d`, `afe9e88`), one per coherent unit. **All four
  new criteria are MET; nothing was left as a disclosed unmet criterion.** One
  register entry is BROADENED (34, to carry `AC-F5-07`) and none opened or
  closed. 2,988 → **2,996** scenarios, all green in six orderings.
  1. **`AC-F41-22` — the retired ID is written nowhere in either tree, not even
     in a docstring.** The scenario that bore it was a faithful test of the
     approved design and is kept, re-pointed, and **folded together with its two
     `TestNoApproveControlHere` siblings**, which asserted the fourth element's
     *absence* while it asserted three of four — so a by-ID mapper scored a
     four-element conjunction off a strict subset. *Judgement call:* the
     retirement note in the module docstring names **no ID at all**. Gate 9
     joins criterion to check by grepping for the ID, and a retired ID in a
     comment scores as a claim; a reader is sent to `FUNCTIONAL_SPEC` §28.1
     instead. `AC-F41-22` also adds the two clauses the original never made
     assertable — none of the three elements behind a disclosure, and no
     approving control **at any permission level**, checked across both personas
     over every awaiting finding screen reachable from `/`, with both
     eligibility values required present so a traversal reaching only ineligible
     items cannot pass it for the wrong reason.
  2. **`AC-F41-23` — the detection evidence renders on the approval screen.** It
     was reachable only through `approval-finding-link`, so the approver decided
     from the journal lines (what would be *posted*) plus somebody else's
     summary of why the artefact exists. *Judgement call:* the **risk band was
     deliberately not brought across**. It carries the single largest type in
     the product and that size is a per-screen uniqueness invariant, so
     importing it would be a typography decision made by a criterion about
     evidence. The **same component** renders on both screens, and the scenario
     compares the two cell for cell **against a second render of the finding
     screen**, never against the model both are built from.
  3. **A real defect, found while building item 3, fixed in its own commit.**
     `components.rejection_reasons` rendered each radio's value as the **row
     index** while the store admits only the six codes its `CHECK` constraint is
     built from — so **`AC-F41-06`'s structured-reject control has never
     completed a rejection from a browser**. Nothing noticed because every
     scenario that appeared to drive it posted a code *by hand*
     (`{"rejection_reason": "already_handled"}`), a value no rendered form in
     this product has ever carried: the control was credited by checks that
     never used it. The `(code, label)` pairs now come from the store's own
     tuple, `state.py`'s second list of the same six labels is gone, and a
     scenario posts **what the radio says**, for all six, reading the field name
     off the rendered input.
  4. **`AC-F41-24` — BUILT, not disclosed unmet, and the lifecycle boundary was
     not crossed.** What renders beside the approve control is `AC-F41-06`'s
     structured rejection: same endpoint, same closed list, same store call that
     already carried `proposal_id`. No new state, no new route, no lifecycle.
     The screen says in as many words that what becomes of a rejected proposal
     is not decided by this build, and the scenario asserts the rejection is
     *recorded* and stops there. The override is refused by a scenario that
     names it: it is a path **to** approval with a second authoriser, so
     offering it would satisfy the wording while inverting the claim.
     *Judgement call, disclosed rather than asserted away:* approving is one
     interaction and rejecting is two, because `AC-F41-06` requires a structured
     reason. `AC-F41-24` speaks to **reachability**, which is what is asserted;
     the asymmetry is written into the scenario so a later reader meets it
     rather than inferring an equality the check does not claim.
  5. **`AC-F5-08` — MET; `AC-F5-07` — recorded NOT MET, and the forbidden set is
     nine.** See register 34's pass-21 broadening for the full record. Both
     halves of the ruling are carried: the four authorship-only agents get real
     rows with "not recorded" values that name the registry gap, and the two
     scenarios that claimed `AC-F5-07` lose the ID, as do the product docstring
     and the test-file section header that also carried it as a bare claim.
     *Judgement call:* **no lineage view is rendered for those rows.** A
     decision-ledger traversal for a principal the ledger has never seen returns
     zero, and a zero in the same component as a real result reads as "this
     agent touched nothing" — false about an agent that authored findings, in
     the one place a reader would check.
  6. **What this pass did NOT do.** Neither of `plan-agent`'s two questions was
     touched: the principal-registry gap is not closed, and no lifecycle was
     invented for a proposal rejected at the approval screen. **Nine** forbidden
     criteria are claimed nowhere. No guardrail moved to the UI, no free-form
     SQL or SQL-typed parameter, no Oracle posting credential, no
     journal-submission library, no suite stubbed green, no exemption table, no
     dependency installed, `prod/` untouched, and no server started — the
     human's pilot on 8030 was left running and untouched.

- **2026-08-04 — Gate 7 pass 22 (`code-agent`): the retained view is DERIVED
  from the approval screen, and a drift check now fails when the screen gains an
  element the artefact does not carry.** Two commits (`5cd4a85`, `7757e0d`).
  One item, per the orchestrator's ruling that completing `AC-F41-04` is not new
  scope: the criterion did not change, the screen did, and the retained view had
  to follow it. 2,997 → **3,037** scenarios (+33 unit, +7 functional), all
  green in file order and in five permutations.
  1. **What was wrong was structural, not a missing card.**
     `state._retained_view` hand-assembled a five-row summary — account,
     finding, riskiest element, why, amount — composed separately from the
     screen and joined to it by nothing. It had drifted from three criteria at
     once: `AC-F41-23`'s detection evidence (put on the approval screen at pass
     21, never added here), `AC-F40-11`'s explicit *"that same rendering is what
     `AC-F41-04` retains"* (the journal lines were on the screen and not in the
     artefact — `components.journal_lines`' own docstring asserted otherwise),
     and `AC-F41-04`'s own named threshold and bundle version, neither of which
     the artefact carried.
  2. **There is now no second composition to drift.**
     `pages.approval_evidential_region` is the one definition of the evidential
     content of the approval act; `/approvals/<proposal>` renders it and
     `app/ui/retained.py` renders the same call. A scenario asserts the artefact
     contains each region element's **own rendered bytes**, not merely the same
     words — a text comparison would pass on a summary that happened to agree
     today and drift again on the next change.
  3. **THE DRIFT CHECK, which is the part worth more than the fix.**
     `retained.unclassified` walks the top-level elements of the real approval
     screen and returns every one that is neither in the retained region nor
     named in `retained.NOT_RETAINED` **with the reason it is not evidence**;
     `render()` raises `RetainedViewDrift` on a non-empty result, so the
     artefact refuses to be produced at all — `AC-F1-07`'s posture, since a view
     that has silently stopped being the view IS a file presented as complete.
     Verified by mutation: adding an unclassified card to `approval_detail`
     fails the **export path**, not merely a unit. Every top-level element of
     that screen now carries a `data-testid`, because the check classifies by
     id and "the check could not see it" must not equal "the check approved it".
     `NOT_RETAINED` holds only chrome and controls; it is not an exemption table
     for criteria, and a scenario requires every name in it to be a real id used
     by `pages` and to carry a reason.
  4. **Two judgement calls, both disclosed rather than folded in.**
     (a) `C.in_force_panel` now renders on `/approvals/<proposal>`. `AC-F41-04`
     requires the threshold and bundle version in the artefact and `AC-F41-05`
     requires them visible **at approval time**; approval time moved to this
     screen at pass 17, so the clause followed the button exactly as `AC-F41-23`
     and `AC-F41-24` did. Retaining them without showing them would have been
     the same defect from the opposite direction — an artefact carrying a fact
     the approver was not shown. (b) `approval_subject` states the item, the
     account, the finding and the **amount** as facts; they were on that screen
     only inside a link's text, which is a label of a destination rather than a
     fact stated there, and the navigation card carries anchors so it cannot
     itself be in an artefact opened from a file.
  5. **RESIDUAL, stated rather than left silent.** `ARCHITECTURE_KB` §9.4 says
     the retained artefact is **style-inlined**; the `/dossier/<id>` exhibit is,
     and the export's per-dossier `rendered_view` still is not — it is unstyled
     markup, as it was before this pass. Inlining `chrome.stylesheet()` is
     mechanically safe (20 KB, deterministic, no `url(`, no absolute URL) but
     would add roughly 280 KB to the export file, which genuinely is a change to
     what an export contains and is not required by the text of `AC-F41-04`.
     Flagged for `solutions-architect` rather than decided here.
  6. **What this pass did NOT do.** Neither of `plan-agent`'s two open questions
     was touched. Nine forbidden criteria are claimed nowhere and `AC-F41-13`
     stays absent from both trees including docstrings. No guardrail moved to
     the UI, no free-form SQL or SQL-typed parameter, no Oracle posting
     credential, no journal-submission library, no suite stubbed green, no
     exemption table, no dependency installed, `prod/` untouched, no server
     started, and the human's pilot on 8030 was left running and untouched.

## Current Status

### Screen architecture after pass 17 (`UX_KB` Part A2 built)

The interface is an OBJECT GRAPH with a four-group navigation over it, replacing
twelve top-level screens in two groups. `app/ui/graph.py` declares the eight
edges as data; `app/ui/chrome.py` declares the navigation; both are asserted by
`backend/tests/test_ui_information_architecture.py` and
`test_ui_object_graph.py`, so the IA is a checked artefact rather than a
paragraph — which is the specific failure `UX_KB` A2.1 records.

| Group | Screens |
|---|---|
| Work | `/queue` (the merged queue; `/exceptions` and `/review` are declared aliases serving the same screen) · `/approvals` · `/ask` |
| Govern | `/catalogue` · `/monitors` |
| Evidence | `/audit` (runs & dossiers) · `/inventory` (agents & datasets) · `/refusals` |
| Identity block | `/my-probe-history`, plus the pilot persona switch |

Objects, each with one canonical page naming it in its `<h1>`: the finding
(`/review/<item>`), the run (`/evidence/run/<id>`), the agent
(`/evidence/agent/<id>`), the dataset (`/evidence/dataset/<id>`), the dossier
(`/dossier/<id>`), the proposal (`/proposal/<id>`) and the approval
(`/approvals/<proposal>`). Readiness is a property of an agent
(`/readiness?agent=<id>`), not a screen.

`/` renders the queue, not Ask. **The one Approve control in the product is on
`/approvals/<proposal>` and nowhere else**, which is counted by walking the
whole reachable surface.

**Amended at pass 21 — what `/approvals/<proposal>` carries.** The approval
screen is no longer *only* the act. It renders **the detection evidence the
proposal rests on** (`AC-F41-23`, the same component the finding screen uses,
not a second summary of it) and **a non-approving terminal action beside the
approve control** (`AC-F41-24`, `AC-F41-06`'s structured rejection, rendered
where the approving happens). Both are consequences of one finding: gate 5
removed approve from the finding screen and pass 17 gave the act its own
screen, on which **approve was again the only visible terminal action** — the
hazard was relocated rather than removed. The finding screen's *absence* of an
approve control is unchanged and is now specified rather than merely honoured
(`AC-F41-22`). `/inventory` additionally lists the agents it knows only by
authorship, with each unheld value naming the registry gap (`AC-F5-08`).

**Amended at pass 22 — the retained view is a rendering of that screen, not a
description of it.** `AC-F41-04`'s artefact used to be hand-assembled in
`state._retained_view`. It is now `app/ui/retained.py` rendering
`pages.approval_evidential_region`, which is the same call
`/approvals/<proposal>` renders — one composition, so the screen and the
artefact cannot disagree. That screen additionally carries `in-force-panel`
(threshold and bundle version, `AC-F41-04`/`AC-F41-05`, which followed the
approve button to this screen) and `approval-subject` (the item, account,
finding and amount as facts rather than as a link's label). Every top-level
element of the screen is classified: it is either in the evidential region and
therefore retained, or named in `retained.NOT_RETAINED` with the reason it is
not evidence — the approve form, the rejection form and the navigation are
excluded because an artefact opening from a file, offline, must contain no
control and no anchor (`ARCHITECTURE_KB` §9.4). An element in neither list makes
`retained.render` raise, so the auditor export refuses to be produced rather
than shipping a view that has quietly stopped being the view.

Gate 7 · Code — MVP1 in staged passes against **262** acceptance criteria.

**Pass 17 — the approved UX redesign (`UX_KB` Part A2). Test-count delta
against pass 16's final run at `b38214d`:**

| Suite | Before | After | Delta |
|---|---|---|---|
| unit/integration | 2,119 | **2,281** | **+162** |
| functional | 354 | 354 | — |
| architecture | 28 | 28 | — |
| security | 14 | 14 | — |
| red-team | 61 | 61 | — |
| industry | 23 | 23 | — |
| ux | 186 | **194** | **+8** |
| **total collected** | 2,785 | **2,955** | **+170** |

**0 tests deleted.** The +162 in unit/integration is four new files —
`test_ui_object_graph.py` (35: one scenario per declared edge, both chains
walked, and the four object pages), `test_ui_information_architecture.py` (27),
`test_ui_approvals.py` (41) and `test_ui_brand.py` (32) — plus additions to
`test_ui_review.py`, `test_ui_readiness.py`, `test_ui_exceptions.py` and
`test_ui_boundaries.py`. The +8 in `ux` is the run report entering the
accessibility suite's screen matrix (four scenarios × two themes) and the
readiness journey splitting into a per-agent walk.

**Scenarios CHANGED, all named, none weakened:**

| Where | Change | Why it is not a weakening |
|---|---|---|
| `test_ui_dossier` | "no links at all" → "exactly one link, the back-reference, relative and same-origin" | The fetch-nothing substance is a separate scenario and is untouched. Flagged to `functional-design-agent` in the Decisions Log. |
| `test_f26_criteria`, `test_f28_criteria`, `test_f33_criteria`, `test_f26_fidelity`, `test_ui_exceptions` | screen re-pointed from `/exceptions` to `/evidence/run/<id>` | `UX_KB` A2.6: nothing satisfying a criterion is deleted; criteria naming a screen have that screen re-pointed. Reachability of the new screen is asserted alongside. |
| `test_ui_proposal` | approve-control scenarios re-pointed to `/approvals/<proposal>` | The control moved screens; its checks moved with it, including `AC-F40-11`'s lines-before-control ordering and both supersession removals. |
| `test_ui_ask`, `test_ui_ask_resolver`, `test_semantic_versions_criteria`, `test_ask_request_criteria`, `test_ux_journey` | "`/` renders Ask" → "`/` links to Ask, one click away" | `/` is the queue now. "Reached by following a link" is a stronger claim than "the browser landed on it". |
| `test_ui_probe_surface`, `test_f12_probe_criteria`, `test_ux_flow` | `review-queue` → `exception-queue` | The parallel `<ul>` was removed by the merge; the ordering and row-shape claims are asserted against the list that survived, which carries more for a probe's row to differ in. |
| `test_ui_probe_surface` | render-path probe check reads the AST instead of grepping source text | The merged queue's prose legitimately says "probe" — it is the screen the programme is disclosed on. The criterion is about what the CODE does. |
| `test_ui_boundaries` | reachability allows declared aliases | The allowance is read from `routes.SCREEN_ALIASES` (product code), and each alias's target is separately asserted reachable. |
| `test_ui_approvals` | gold selectors widened from three to five | The Council Mark's pull-line and terminus dot. Same meaning — a human decision — under the brand's own colour law, which is itself asserted. |

**Order independence verified at `6bf8ed9`.** All 2,955 pass under six
orderings, with the same out-of-tree uniform global Fisher–Yates plugin
approach as earlier passes so the tree stayed clean:

| Ordering | Result | Wall | Same-file adjacencies | Order fingerprint |
|---|---|---|---|---|
| file order (control) | 2,955 pass, exit 0 | 244s | 2,846 | `8dfbccb220751114` |
| `seed:1` | 2,955 pass, exit 0 | 283s | 38 | `759308beb6c37d78` |
| `seed:7` | 2,955 pass, exit 0 | 284s | 35 | `652298ba83465fc4` |
| `seed:42` | 2,955 pass, exit 0 | 285s | 32 | `13eb7530e5746536` |
| `seed:20260731` | 2,955 pass, exit 0 | 324s | 32 | `e611d0c50e37510d` |
| `reverse` | 2,955 pass, exit 0 | 228s | 2,846 | `fa4584ef39e7c77b` |

A separate matrix over shuffled FILE order (the same four seeds, plus sorted
and reversed) also passed, which is the weaker property but the one a suite
owner invoking `run.sh` on one directory actually gets.

### After pass 19 (`e00a214`) — counts and order independence

**2,987 collected, 2,987 pass, 0 fail.** Delta against gate 8's `1b1b56e`
baseline of 2,977, measured by comparing collected node ids rather than counted
by hand: **+12 node ids added, −2 removed, net +10, and 5 more changed in
place.**

**The two removals are not a coverage reduction and are named as such.** They
are the pre-parametrisation ids of
`test_every_anomaly_states_the_threshold_in_force` and
`test_each_kind_labels_its_own_fields_in_its_own_words`, both of which survive
as parametrised sets of 4 and 3 respectively — a scenario that checked one case
became one that checks all of them. **No scenario was deleted in this pass, and
no scenario asserts less than it did.**

| Suite | At `1b1b56e` | At `e00a214` | Delta |
|---|---|---|---|
| unit/integration | 2,302 | **2,309** | **+7** |
| functional | 355 | **358** | **+3** |
| architecture | 28 | 28 | — |
| security | 14 | 14 | — |
| red-team | 61 | 61 | — |
| industry | 23 | 23 | — |
| ux | 194 | 194 | — |
| **total** | 2,977 | **2,987** | **+10** |

**Added (12):** the whole-surface disclosure guard; the two
`unregistered_actors` scenarios; `AC-F38-01`'s every-card scenario;
`no_two_kinds_share_a_label`; `obligation_gap`'s label scenario at 3
parametrisations (it named 2 of the 3 kinds by hand and now runs the mapping);
`distribution_outlier`'s threshold scenario at 4 (it ran 1 case, above only).

**Changed in place (5), each asserting strictly more:** `AC-F5-07`'s two
scenarios, the `AC-F5-02` disclosure scenario (it now follows the four agent
links), `AC-F40-16` (every register entry, not `entries[-1]`), and the export
reconstruction-field scenario (two dossiers, not `dossiers[0]`).

**Order independence verified at `e00a214`**, with an out-of-tree plugin salted
on a token that `grep -rl` finds nowhere in `dev/`, so no suite can recognise
it. Seven whole-tree runs, all 2,987 pass, exit 0:

| Ordering | Result | Wall | Order fingerprint |
|---|---|---|---|
| canonical (control) | 2,987 pass, exit 0 | 222s | `4a9b46c1…` |
| file order | 2,987 pass, exit 0 | 219s | `4a9b46c1…` |
| `reverse` | 2,987 pass, exit 0 | 226s | `16f41929…` |
| `seed:1` | 2,987 pass, exit 0 | 266s | `3d2e0c14…` |
| `seed:7` | 2,987 pass, exit 0 | 267s | `88dab037…` |
| `seed:42` | 2,987 pass, exit 0 | 264s | `ac629eda…` |
| `seed:20260731` | 2,987 pass, exit 0 | 262s | `7330ba7d…` |

File order fingerprints identically to canonical, which is expected — pytest
already collects in file order — and is reported rather than presented as a
seventh distinct sequence. All seven dumps carry the same 2,987 node ids
(`sort | md5` identical), so no ordering silently dropped a scenario. All six
suite entry points exit 0. `dev/var/broker_db.sqlite3` is byte-identical
(`a638fc51…`) after every run.
(261 until the gate-9 loop-back: `FUNCTIONAL_SPEC` §27.11's arithmetic said
"262 issued, 261 live (186 + 77 − 1)" and 186 + 77 is 263. Corrected in the
spec at v1.1.1; **no ID was renumbered, added or removed**.)

**Pass 15 — the last two in-scope undisclosed criteria. Test-count delta
against gate 8's final run at `fc197a6`:**

| Suite | Before | After | Delta |
|---|---|---|---|
| unit/integration | 2,028 | **2,071** | **+43** |
| functional | 354 | 354 | — |
| architecture | 26 | **27** | **+1** |
| security | 14 | 14 | — |
| red-team | 61 | 61 | — |
| industry | 23 | 23 | — |
| ux | 186 | 186 | — |
| **total collected** | 2,692 | **2,736** | **+44** |

**0 tests removed.** The +43 in unit/integration is 32 new scenarios for
`AC-F36-33` (`backend/tests/test_restatement_comparator.py`), 7 for
`AC-F36-30` (`test_bundle_publication.py`) and 4 for the widened process-state
guard. The +1 in `architecture` is the harness scenario that refuses a suite
run writing to the developer's decision ledger. **Six scenarios were CHANGED
and none was weakened**: the four G-RESTATE scenarios now derive their
restatement state from the real comparator instead of supplying it — two of
them additionally asserting the comparator's output before driving the broker —
and two process-state scenarios now scan `GUARDED_MODULES` rather than
`PROCESS_STATE_MODULES`, which is a strictly larger set.

**Order independence re-verified at `75f5e27`.** All 2,736 pass under six
orderings, with an out-of-tree uniform global Fisher–Yates plugin so the tree
stayed clean. Fingerprints and same-file-adjacency counts recorded so the
permutation used is evidence rather than a claim:

| Ordering | Result | Wall | Same-file adjacencies | Order fingerprint |
|---|---|---|---|---|
| file order (control) | 2,736 pass, exit 0 | 169.1s | — | — |
| `seed:1` | 2,736 pass, exit 0 | 197.9s | 37 | `8572b681d7cd5743` |
| `seed:7` | 2,736 pass, exit 0 | 199.8s | 37 | `c100caa5cb0cf5d0` |
| `seed:42` | 2,736 pass, exit 0 | 203.0s | 27 | `b0fb50e4f73141b9` |
| `seed:20260731` | 2,736 pass, exit 0 | 207.7s | 38 | `d4791a479a9da2a5` |
| `reverse` | 2,736 pass, exit 0 | 191.1s | 2,634 | `67a2c580ba09549a` |

These are `code-agent`'s own permutations and are **not** `test-agent`'s: the
fingerprints differ from the gate-8 table above, which is the point — an
independent generator at gate 8 is what makes that run evidence rather than a
repeat of this one.

**Pass 7 — the gate-9 RE-AUDIT loop-back. Test-count delta against pass 6:**

| Suite | Before | After | Delta |
|---|---|---|---|
| unit/integration | 1,428 | **1,583** | **+155** |
| functional | 96 | **214** | **+118** |
| red-team | 46 | 46 | — |
| architecture | 23 | 23 | — |
| security | 14 | 14 | — |
| industry | 23 | 23 | — |
| ux | 186 | 186 | — |
| **total collected** | 1,816 | **2,089** | **+273** |

**0 tests removed.** Fourteen existing scenarios were CHANGED and none was
weakened: eleven now supply a complete version stamp (with a note saying they
would otherwise pass for the wrong reason — the SoD input-set check denies
before the identity and ceiling rules), one asserts the routing raiser's
PRINCIPAL ID rather than the word "controller", one primes the pilot close
before cutting the transport because the findings themselves are now
downstream of the emission gate, and three `AC-F36-48` scenarios gained
register-27's in-file denial.

**Passes 1, 2a, 2b, 2c, 3, 4, 5, 6 and 7 complete** (39 commits in `dev/`, **1,439
unit tests + 388 suite scenarios**, all green. Pass 6's delta: **+11 unit
scenarios** (`AC-F36-47`'s surface clause), **0 suite scenarios** — the
register-24/25 work changed what existing scenarios say and what they read
their numbers from, not how many there are. **All six suites execute**;
`industry` moved off exit 3 at pass 4 because two of the five things its README
named — the Journal Import contract and the CUEC register — are now built).

Built in pass 1: the two-process repo skeleton and the GES credential trust
boundary; the certified query registry and its single execution operation; the
append-only hash-chained dossier store; coverage as a closed sum type; the F29
omission detector, the F42 negative half and the paired wedge comparison; the
twelve-period fixture with the planted omission.

Built in passes 2a–2b: the F36 guardrail broker — closed predicate language,
hash-addressed bundle, deny-by-default FSM, blast-radius caps holding under
real concurrency; authorship closure at the schema level; dual-authorised
bundle publication; the threshold-widening detector; the FSM emission leg with
`ABSTAINED` as a first-class terminal state.

Built in pass 2c: the owed emission-leg test (abstention structurally distinct
from denial; `OVERRIDE` proved unreachable from the emission leg by forward
closure, reverse closure and exhaustive path enumeration); the nine behavioural
guardrails as fourteen bundle-resident rules with twenty-eight compile-time
fixtures; the emission decision path; the F50 refusal registry A19–A25 with
A20 as a speech act; abstention as a first-class output with all six types and
the four-state RAG; F12's label-source and promotion-readiness report; R1–R6
and their evidence schemas; the policy-cold auto-disposal path with
third-consecutive-period escalation; F35 close preconditions and F32 forward
disposition with its verification job.

Built in pass 3 — **the desktop web surface (S1), end to end**: an escaping
HTML kernel; the design tokens with `assert_no_green()` enforced at import; the
inlined, script-free page shell; a 36-component library; and six routed screens
— **Ask** (declared-population inversion, coverage strip, ambiguity fork),
**Exceptions** (volume masthead, the wedge's two labels, five boundary checks
with "not run" in risk colour, the auto-disposed row from the real policy-cold
path, and four renderable coverage states), **Review** (risk → evidence →
resolution → narrative-collapsed, no approve control, six resolution types,
closed rejection list, required clearing period), the **evidential dossier**
(shell off, style-inlined, no external reference of any kind), **Proposal**
(the only approve control, terminating in an export file, approval path removed
on supersession) and **Readiness** (P1–P5 individually, label source adjacent
to the figure).

Built in pass 4 — **MVP1 end to end**: `POST /ges/decide`, `/ges/override`,
`/ges/bundle`, `/ges/datasets`, `/ges/run/precheck`, `/ges/refusals`,
`/ges/inventory`, `/ges/monitors`, `/ges/cuec` and `POST /ges/export/journal`;
override-eligibility as a bundle field with identity rules refused at compile
time; the write path (dispositions, structured rejections, approvals under a
broker decision id, the F12 capture, `AC-F12-19`'s warrant label); the Journal
Import file with our identifiers in `REFERENCE21`–`25`; the CUEC register;
`AC-F38-10`'s exploration tier with the marker rendered by the page shell; and
the six remaining screens — **Dispositions, Catalogue, Monitors, Inventory,
Audit, Refusals**. The `industry` suite executes for the first time.

**Pass 4d — the gate-8 loop-back, four evidence-honesty fixes** (see the
Decisions Log entry of the same date). Suite counts after it: **functional 21
(unchanged, one criterion ID removed), architecture 23 (+2), red-team 41 (+1),
ux 186 (unchanged, two scenarios strengthened)** — 1,525 collected in total
against 1,522 before, **+3 added, 0 removed, 4 renamed or rescoped**. Every
suite still exits 0. The point of the pass was that three of those scenarios
now assert *more* and one criterion is now claimed by *nothing*.

**Pass 5 — the gate-9 loop-back. Test-count delta against pass 4d:**

| Suite | Before | After | Delta |
|---|---|---|---|
| unit/integration | 1,217 | **1,428** | **+211** |
| functional | 21 | **96** | **+75** |
| red-team | 41 | **46** | **+5** |
| architecture | 23 | 23 | — |
| security | 14 | 14 | — |
| industry | 23 | 23 | — |
| ux | 186 | 186 | — |
| **total collected** | 1,525 | **1,816** | **+291** |

**0 tests removed.** Five existing scenarios were changed and every one now
asserts strictly more:
* the two boundary-check scenarios (one unit, one `ux`) had their "not run"
  count corrected from 2 to 1 — because the two were dictionary literals and
  the one is a real check over a dataset that is really absent — and both now
  additionally assert the missing dataset is **named**, which neither did;
* `AC-F9-08`'s Monitors scenario now asserts escalation period **4**, the
  number the primitive computed, where it asserted the calendar string
  "2026-06" that somebody typed;
* `AC-F33-07`'s screen scenario now asserts the label is byte-identical to
  `f33.backtest.RECALL_BIAS_LABEL` rather than containing a phrase;
* the A20 red-team battery went from eight strings to twelve — and split,
  because four of the twelve are not refused.

**45 scenario docstrings gained an explicit `COVERS AC-…` line**, so gate 9's
criterion-to-test join stops being an inference. Criteria with no covering
scenario were left alone.

**Pass 5 — the gate-9 loop-back. The four detector families gate 9 found
never built are built**, in one commit each, plus the three contradictions and
the two reporting fixes.

| Family | Built | AC IDs now evidenced | Still not |
|---|---|---|---|
| **F26** warehouse-to-ERP fidelity | `identity_tieout`, `freshness`; two manifests; a two-leg run; the Exceptions region | `AC-F26-01`…`-10` (`-05` from pass 11, against the declared close calendar) | — |
| **F28** the five boundary checks | `pair_imbalance`, `continuity`, `arithmetic_recompute`, `residual_threshold`; `identity_tieout` bound a second time for A6; five manifests; `BoundaryRun` | `AC-F28-01`…`-10`, all ten | — |
| **F9** cross-period surveillance | `accumulation`, `text_recurrence`; two manifests; both legs; the R6 control-state change; the Monitors regions | `AC-F9-01`…`-09`, all nine | — |
| **F33** coding anomaly + backtest | `peer_coding_divergence`; the backtest evidence schema; the Exceptions region | `AC-F33-01`…`-12`, all twelve | — |

**All eleven `ARCHITECTURE_KB` §7.3 evaluator primitives now exist.**
`SPECIFIED_BUT_NOT_IMPLEMENTED` is empty — and is KEPT, empty, because a
manifest naming a specified-but-unbuilt primitive must still fail compilation
*saying so*. A `parametrize` over an empty tuple collects zero tests and
reports green, so that behaviour is now asserted against a planted entry
instead.

**Plus two primitives outside the KB's eleven**, both declared in
`UNSPECIFIED_BUT_BUILT` so the KB's list stays the KB's list, and both for
`solution-architect` at gate 10: `obligation_gap` (pass 7, F29's other three
sub-types) and `journal_attribute_outlier` (pass 8, `AC-F42-02` — F42's journal
leg, over its own population `pop.period_journals@1`).

**Pass 8 additions to the analysis plane's shape.** A natural-language REQUEST
is now triaged at the broker before anything resolves it
(`ges/broker/request_triage.py`, `POST /ges/ask`, `POST /ask`), with three
outcomes and all three declines. Every certified query declares its metric and
join versions (`semantics:`, required at compile time), which travel out of
`/ges/query` with the rows and are stamped in a **v2 dossier payload**. A
reversal is a record type of its own (`app/evidence/reversal.py`) whose linkage
is resolved on read rather than written back.

**Two of gate 9's three contradictions were capabilities that do not exist and
are now stated as unmet rather than claimed**; the third was a missing build
and is built. See Decisions Log items 13–15.

**Not built and absent rather than stubbed** — *as this read before the scope
ruling's two batches; struck through in substance by passes 11 and 12 and kept
here so the sequence is legible*: point-of-action revalidation, the close clock
(`AC-F38-11`, and therefore `AC-F26-05`), the F12 probe-injection programme
(`AC-F41-08` and, from the capture side, `AC-F12-05`), F17 direct posting, and
the F39 natural-language resolver's model call site (and therefore
`AC-REFUSAL-11`, `AC-F39-03`, `-05`, `-06`, `-08`).

**Pass 11 (batch A) built** the export-time CUEC fail-closed path
(`AC-F40-18`), the close clock (`AC-F26-05`, `AC-F38-11`) and point-of-action
revalidation (`AC-F40-12`…`-16`).

**Pass 12 (batch B) built the two large clusters, and this is what remains
absent afterwards:**

* **The probe-injection programme is built**, with its full non-attributability
  set in the same commit — `AC-F12-11` … `-18`, and `AC-F41-08` and
  `AC-F12-05` claimable for the first time. Register 18 closes. The probe flag
  is store-level and `ReviewItem` has no field for it, so the agent runtime and
  every pre-disposition payload are identical for a probe and a genuine item by
  construction rather than by omission. What is NOT claimed: anything about
  explanation quality — §12's standing exclusion holds and probes measure
  attention, which is the alternative `INDUSTRY_KB` §15.4 names.
* **The F39 resolver call site is built** — `AC-F39-03`, `-05`, `-06`, `-08`,
  which were all passing vacuously because every request declined. Natural
  language selects and parameterises over thirteen committed manifests and
  never authors a query. What is NOT built and is not claimed: a **model** call
  site. Intent selection is pattern matching against a committed table, so a
  request outside its vocabulary is unmappable — the safe direction.
* **`AC-REFUSAL-11` remains phase 2 and the resolver made its exposure larger,
  not smaller.** Register 9 is narrowed with the measurement: eleven of the
  twelve RT05 paraphrases are not refused at the *request* surface, and a
  crafted evading paraphrase that names a mapped subject now reaches an answer
  where it previously reached a decline.

**Still absent after pass 12**: `AC-F40-17` (CUEC drift detection),
`AC-F1-08` (object-lock retention), `AC-F1-11` (KMS-signed anchors),
`AC-REFUSAL-11`, F17 blind re-performance and direct Tier-2 posting.

## Test Results

### 2026-08-04 — Gate 8 · Test — `test-agent`, **pass 22 re-run, after the `AC-F41-13` ruling was built, at `dev` @ `7757e0d`** (parent repo @ `299369e`)

**Everything passes. The gate closes on the evidence.**

**3,037 scenarios, 3,037 pass, 0 fail, 0 skip, exit 0**, on a verified-clean
tree, plus 38 smoke scenarios against a served pilot and 19 rendered-UI
scenarios in Chromium — **all executed, none static, none advisory.**

#### Per-suite breakdown — every suite marked, never merged

| Suite | Owner | Status | Result | Δ since `c428fe5` | Blocking |
|---|---|---|---|---|---|
| unit / integration (`backend/tests`) | `test-agent` | **`EXECUTED`** | **2,352 / 2,352** | **+42** | yes |
| functional | `functional-design-agent` | **`EXECUTED`** | **365 / 365** | **+7** | yes |
| UX | `ui-ux-designer` | **`EXECUTED`** | **194 / 194** | 0 | yes |
| red-team | `responsible-ai-architect` | **`EXECUTED`** | **61 / 61** | 0 | yes |
| architecture | `solution-architect` | **`EXECUTED`** | **28 / 28** | 0 | yes |
| industry | `industry-expert` | **`EXECUTED`** | **23 / 23** | 0 | yes |
| security | `security-architect` | **`EXECUTED`** | **14 / 14** | 0 | yes |
| **whole tree** | — | **`EXECUTED`** | **3,037 / 3,037** | **+49** | yes |
| post-deploy smoke (served pilot, 8021) | `test-agent` | **`EXECUTED`** | **38 / 38** | +9 | yes |
| rendered-UI (Playwright / Chromium, web) | `test-agent` | **`EXECUTED`** | **19 / 19** | +6 | yes |
| rendered-UI (RNTL, native) | — | **N/A** | no native surface in MVP1 | — | — |
| rendered-UI (Maestro + simulator) | — | **NOT BUILT** | no simulator on this machine (2026-07-26 spike, unchanged) | — | — |

Every SME suite ran through its own `run.sh` and returned **exit 0** with
`EXECUTED — suite passed`. Exit 3 (no scenarios) and exit 4 (cannot execute)
did not occur, so no empty suite is being reported as a passing one.

#### Test-count delta — measured, not counted

**2,988 → 3,037: +54 added, −5 removed, 1 parametrisation widened, 0 silent
assertion edits.** All five removals are instructed consequences of the ruling
and every one is named in `test-evidence/unit-integration-2026-08-04.md`: three
`TestNoApproveControlHere` scenarios folded into the single `AC-F41-22`
scenario per §28.1's own instruction, and two `AC-F5-07` scenarios that
quantified over the registry's projection onto itself — the tautology §28.2
ruled against — replaced by three whose names state their scope. **Neither fold
narrowed coverage**; both replacements assert strictly more.

#### The four things this pass was asked to verify

1. **`AC-F41-13` is written nowhere in the tree.** 0 source occurrences, 0 node
   ids, 0 `COVERS` lines, tracked and untracked, docstrings included. Each
   replacement's check covers its criterion **whole**, in one scenario:
   `AC-F41-22` includes "no approving control at any permission level" (asserted
   across both personas, over 14 finding screens reached by traversal, guarded
   so it cannot pass by reaching nothing); `AC-F41-24` requires a non-approving
   terminal action neither behind a disclosure, a dialog nor a link, posting to
   an endpoint that is neither approve nor override, with the property itself
   computed from the screen rather than asserted by testid.
2. **The shipped reject-radio bug is fixed, verified from a browser.** All six
   reason codes were driven by **clicking the rendered radio** on six different
   findings — six `"Rejection recorded"`, none by hand-posting a code — with a
   negative control (submit with nothing selected) confirming the form can
   still fail. Restoring the row-index value (mutation M7) fails at the store's
   **422**, not at a string comparison.
3. **The retained view is derived, not assembled.** The auditor export **refuses
   to be produced** when an unclassified card is added to the approval screen —
   observed at the route: `/audit/export/file` returns **500** where the
   unmutated build returns 200. `NOT_RETAINED` is a classification, not an
   exemption table: all 8 entries are real testids the screen emits, each with a
   reason, no overlap with the retained region, and mutations that break any of
   those three properties all fail.
4. **The artefact opens offline.** Six dossiers, zero hits across 13
   external-reference and active-content constructs, byte-identical across two
   independent renders (SHA-256 per dossier recorded), `approver_view` ==
   `rendered_view` on all six, and each of the eight evidential elements found
   **verbatim, as its own rendered bytes** from the served screen inside the
   artefact.

**The forbidden set is nine and all nine are claimed nowhere** — `AC-F1-08`,
`AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`, `AC-F5-02`, `-03`, `-05`
and now `AC-F5-07`, whose two prior joins (the bare ID in `pages.inventory`'s
docstring and the test file's section header) are both gone.

#### Standing sweeps

- **Order independence:** six whole-tree runs — canonical, file, reverse, and
  seeds 8003 / 29 / 777 — **3,037 pass every time**, on a plugin held outside
  the tree under test.
- **Empty `parametrize`:** none. Per-suite counts reconcile to 3,037 exactly.
- **Vacuous-pass sweep, AST-instrumented:** 426 assert-bearing loops measured at
  runtime (was 397). 425 iterate; the one zero-iteration loop is the same
  reviewed watchdog as pass 20. 17 single-iteration loops, all reviewed, none a
  defect. 13 no-assert candidates, the same 13, all delegating. **Zero skips,
  zero xfails.** The instrumented tree also passed 3,037/3,037.
- **Mutation tests:** 11 applied to product code, reverted, tree verified clean.
  **10 caught.**

#### One advisory — nothing stops the gate

**The in-tree "own rendered bytes" scenario compares the artefact to the
*region*, not to the *screen*.** Mutation **M3b** put a **second composition** of
`in-force-panel` on the approval screen — same testid, same words, different
bytes — and **89 retained-view scenarios stayed green**. The drift check
classifies by testid (the testid was present); the verbatim check compares
`retained.render(...)` against `pages.approval_evidential_region(...)`, so it
proves *artefact == region*, and the join *"the screen's evidential content is
that region"* is a source-level fact no scenario asserts.

**This is not a build defect and it does not block:** the property genuinely
holds on this build, and **this gate does catch the mutation** — smoke **S32**,
which extracts each element's markup from the *served screen* and requires it
verbatim in the artefact, fails under M3b and passes on all eight elements
without it. The fix for `code-agent`, after human review, is one line: compare
against `pages.approval_detail(...)`'s own nodes rather than the region's.

Two stale live-tense references to the retired `AC-F41-13` remain **outside**
`dev/` — `knowledge/UX_KB.md:319,549` and `design-review/index.html:878,1022`.
§28.1's prohibition binds *checks*, and no check names it; recorded because a
live-tense reference in a KB is how a retired ID gets re-adopted.

#### Process discipline

The human's pilot was **pid 78317 on 8030** — re-read from `lsof`, **not** the
59422 carried from pass 20, so the human has restarted it. It was alive before
and after every invocation, and 8030/8031 were never probed. Every pilot this
agent started was on 8021, in its own process group, started/driven/reaped
inside a single command invocation; `lsof` on 8021 and 8022 was empty after each
teardown. Nothing was left running past the turn. The shared broker ledger grew
10,956,800 → 11,124,736 bytes across the smoke and browser runs, which is the
evidence the write path really ran; the 3,037-scenario tree leaves it
byte-identical. No product code was fixed by this agent.

Evidence: `test-evidence/*-2026-08-04.md` (16 files) and 20 screenshots. The
2026-08-03 corpus is deleted, not carried.

---

### 2026-08-03 — Gate 8 · Test — `test-agent`, **pass 20, FINAL CONFIRMATION, at `dev` @ `c428fe5`** (parent repo @ `67d0517`) — SUPERSEDED

**Both gate-8 findings are CLOSED, re-verified by re-running the original
mutations rather than by reading the fixes. All seven automated suites
EXECUTED, exit 0, 2,988 of 2,988 scenarios passed at every suite entry point
and in SIX whole-tree runs. Smoke 29 of 29 against a served pilot. Rendered-UI
13 of 13 in a real browser at two viewports, nothing inconclusive. No suite is
`STATIC ONLY`. No blocking gate condition is unmet.**

Structured per-scenario evidence: `test-evidence/*-2026-08-03.md` (15 files,
16 screenshots), written this pass; the superseded set was deleted.

#### Per-suite breakdown — never merged

| Suite | Status | Scenarios | Result | Delta vs `e00a214` | Blocking |
|---|---|---|---|---|---|
| unit / integration (`backend/tests`) | **EXECUTED** | 2,310 | **2,310 pass, 0 fail** | **+1 added, 0 removed** | yes |
| functional | **EXECUTED** | 358 | **358 pass, 0 fail** | 0 added, 0 removed, **2 changed** (1 of them docstring-only) | yes |
| ux | **EXECUTED** | 194 | **194 pass, 0 fail** | unchanged | yes |
| red-team | **EXECUTED** | 61 | **61 pass, 0 fail** | unchanged | yes |
| architecture | **EXECUTED** | 28 | **28 pass, 0 fail** | unchanged | yes |
| industry | **EXECUTED** | 23 | **23 pass, 0 fail** | unchanged | yes |
| security | **EXECUTED** | 14 | **14 pass, 0 fail** | unchanged | yes |
| post-deploy smoke (served pilot, 8021) | **EXECUTED** | 29 | **29 pass, 0 fail** | unchanged | yes |
| rendered-UI — Playwright/Chromium, web | **EXECUTED** | 13 | **13 pass, 0 fail** | unchanged | yes |
| rendered-UI — RNTL, native | **N/A — not applicable** | — | — | — | MVP1 is desktop web only |
| rendered-UI — Maestro + simulator | **NOT BUILT** | — | — | — | no simulator on this machine (2026-07-26 spike, unchanged) |

2,310 + 358 + 194 + 61 + 28 + 23 + 14 = **2,988**, exact. The only suite whose
count moved is unit/integration, and the single addition is named.

#### The two findings, closed by mutation and not by inspection

- **Finding B — `obligation_gap`.** The comparison target moved out of the code
  under test into a literal `EXPECTED_KIND_WORDS` table (`6da659e`). Rewording
  all three `scheduled_reversal` labels to `"thing"`/`"when"`/`"how much"` —
  the exact mutation that left the tree green before — **now fails**. Rewording
  `summary`, a field never asserted in any earlier revision, **also fails**:
  coverage widened from four worded fields to five. Adding a benign fourth kind
  to `KIND_VOCABULARY` **fails three scenarios**, including the new key-set
  companion, so a fourth kind cannot arrive comparing its labels to themselves.
- **Finding A — `AC-F40-16`.** The scenario now drives the real export control
  three times (`05be347`). Blanking the three facts on every register entry but
  the last **now fails on the FULL TREE** (`1 failed, 2987 passed`) — at
  `1b1b56e` that mutation could not fail at all. The guard-first ordering was
  verified, not assumed: making re-export idempotent per proposal fails at
  `assert register["count"] >= 3` (line 904), not by passing over one row (line
  909). A negative control is also recorded — content-hash-keyed idempotency
  leaves the population at three, because the three exports are genuinely
  distinct artefacts.
- **F3 docstring** (`c428fe5`) now states the scenario **fails** when findings
  become ledger-recorded, matching the F3-M2 result. Docstring only; no
  assertion changed, so the earlier mutation evidence still holds.

#### The standing sweeps

- **Order independence** — six whole-tree runs (canonical, `file`, `reverse`,
  salt 8003 / 29 / 777) on `test-agent`'s own plugin, held outside `dev/` and
  loaded by `PYTHONPATH`. **2,988 passed in all six.**
- **Register cross-check** — the register holds 34 contiguous entries. All
  **eight forbidden criteria are claimed nowhere**: five have zero node IDs and
  zero `COVERS` joins; three appear only in self-denying node IDs or explicitly
  narrowed `COVERS` lines. Identical outcome to the previous pass.
- **Vacuous-pass sweep, run in its sharpened form.** Because Finding A was a
  loop that read as a quantifier and ran over one row — and four static reviews
  had passed it — this sweep no longer only reads. All **397** assert-bearing
  loops in the tree were AST-instrumented and their real iteration counts
  recorded over a full run. **One loop has max 0 iterations** (a negative
  watchdog whose own population is guarded at `assert len(urls) > 8` and which
  entered 47 times — reviewed, not a defect) and **17 have max 1**, all
  reviewed, all singular by construction or self-guarded. The instrumented tree
  also passed 2,988/2,988. **Zero empty `parametrize`, zero skips, zero
  scenarios that cannot fail** (13 assert-free functions, all delegating to
  helpers that assert or raise — the same 13, no new ones).

#### Process lifecycle

The human's pilot (**pid 59422, port 8030**) was re-read from `lsof` at the
start of the pass, never carried forward, and confirmed alive after every
invocation. 8030/8031 were never probed. Every pilot this agent started ran on
8021 in its own process group and was reaped with `os.killpg` on that group
only, inside a single command invocation; 8021 and 8022 were empty afterwards
each time. The shared broker ledger grew **10,813,440 → 10,891,264 bytes**
across the smoke and rendered-UI invocations — the evidence the write path
really ran; the 2,988-scenario test tree leaves it byte-identical.

#### Four harness defects found and recorded, none of them build defects

The smoke harness reported four failures on its first run and the rendered-UI
harness one. All five were **defects in this agent's own harness** — an `href`
regex that also matched `data-href`, a `data-agent-id` attribute that does not
exist (the build uses `data-principal`), a single seal testid expected on three
screens that each carry their own, and a gold-exclusion predicate that named
the brand lockup by class and then flagged the lockup's own `path.pull`. Each
is recorded in the relevant evidence file, because "I fixed my test until it
passed" is exactly the move that has to be visible. In every case a second,
independent scenario already asserted the same fact and had been green
throughout, which is what exposed the contradiction.

#### Verdict

**No scenario passes that should not. Nothing is outstanding from this
agent.** Four passes of loop-back are closed and the evidence supports the
gate closing.

---

### 2026-08-03 — Gate 8 · Test — `test-agent`, **re-run after the pass-19 loop-back, at `dev` @ `e00a214`** (parent repo @ `8dcb490`)

**All seven automated suites EXECUTED, exit code 0, 2,987 of 2,987 scenarios
passed at every suite entry point and in SEVEN whole-tree runs — canonical,
`file`, `reverse` and three shuffles salted on a token `grep -rl` finds nowhere
in `dev/`. Zero skipped, zero vacuous, zero empty `parametrize`. The smoke is 29
of 29 and the rendered-UI backend 13 of 13 with nothing inconclusive.**
Structured per-scenario evidence: `test-evidence/*-2026-08-03.md` (15 files,
one new) plus 16 freshly captured Playwright screenshots. The entire superseded
corpus was deleted and rewritten; every file names both commits and its presence
on disk was verified after writing.

| Suite | Status | Exit | Scenarios | Pass | Fail | Owner | Blocking |
|---|---|---|---|---|---|---|---|
| unit / integration | `EXECUTED` | 0 | 2,309 | 2,309 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 358 | 358 | 0 | `functional-design-agent` | yes |
| ux | `EXECUTED` | 0 | 194 | 194 | 0 | `ui-ux-designer` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | `responsible-ai-architect` | yes |
| architecture | `EXECUTED` | 0 | 28 | 28 | 0 | `solution-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | `industry-expert` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | `security-architect` | yes |
| **rendered-UI (Playwright)** | `EXECUTED` | 0 | 13 | 13 | 0 | `test-agent` | yes |
| **smoke (served pilot, 8021)** | `EXECUTED` | 0 | 29 | 29 | 0 | `test-agent` | yes |

**Test-count delta: 2,977 → 2,987 = +12 node ids added, −2 removed, 5 changed in
place.** Measured by comparing collected node ids at both commits, not counted by
hand. The two removals are the pre-parametrisation ids of the two scenarios that
became parametrised sets of 4 and 3; no scenario was deleted. Full per-id detail
in `test-evidence/changed-scenario-audit-2026-08-03.md`.

**All three findings gate 8 blocked on are CLOSED, verified by mutation rather
than accepted.**

- **F1.** The `AC-F5-02` claim is gone from all four agent pages — `grep` finds
  the string in three places in `dev/`, one test constant and two comments
  recording that it used to be there. The guard is re-scoped from one named
  screen to **no reachable screen**: every URL reachable from `/` by following
  real links, plus every document that only exists after operating a control.
  **Restoring the sentence fails, naming five pages.** **Crippling the traversal
  to reach nothing also fails**, on the half that asserts the four agent pages
  are in the traversed set by the ids the broker reports absent — it cannot pass
  by reaching nothing. Corroborated over real HTTP: 46 URLs crawled from `/`,
  zero offenders, five agent pages actually reached.
- **The fourth finding, found by `code-agent` mutating its own fix.** Repointing
  all four `/inventory` hrefs at `/inventory` — which left all 2,977 green at
  `1b1b56e` — **now fails.** So does landing on the wrong agent. And its own
  observation reproduces exactly: **the whole-surface guard does not catch the
  repoint**, correctly, because the agent pages stay reachable through the
  object-graph chain. Exactly one scenario failed, and it was the link scenario.
  The two guards are independent; neither subsumes the other.
- **F2 / `AC-F5-07`.** **Mutation F7-M now fails.** So does rendering the right
  label over the wrong agent's version, and so does attributing every lineage
  view to agent 0 — the sibling's `len(lineage) == len(rows)` really did become
  containment.
- **F3.** `unregistered_actors` returns register 33's convention-C2 UNKNOWN
  shape, rendered on `/inventory` at full opacity. One scenario asserts the
  **shape** (dict-ness, scope, the untraversed class, the statement) rather than
  the emptiness; the other joins `computable: False` to the
  `LINEAGE_UNTRAVERSED` entry that justifies it. Four mutations caught.

**The sampling sweep was run independently, and it found two things pass 19's
did not.** My heuristic is deliberately broader — it reads docstrings as well as
names, counts sampler calls as well as subscripts, and ranks by whether the
scenario iterates at all — and returns **60 candidates against pass 19's 39**.
Three of pass 19's five fixes were spot-checked by mutation and all three were
**caught** (`obligation_gap`, `distribution_outlier`, `AC-F38-01`), as were the
other two mutations I ran (export reconstruction, and the copied-vocabulary
case). Pass 19's 34 dismissals are not contradicted. But:

1. **`AC-F40-16`'s "every produced file" is still asserted of one file.** The
   rewrite from `entries[-1]` to a loop **cannot fail differently**: an
   instrumented probe shows the register holds exactly **one** entry in that
   scenario, so the two forms are the same assertion. Blanking the three facts
   on every entry but the last leaves the suite green. Not a regression — the
   fix is simply inert at this site, and closing it is a fixture change.
2. **`obligation_gap` lost four literal-value assertions and nothing replaced
   them.** The rewritten `test_each_kind_labels_its_own_fields_in_its_own_words`
   compares the evaluator's output to `KIND_VOCABULARY` — **the constant the
   evaluator itself reads to build those labels** — which is the projection
   against its own source, the exact defect class register 34 records for the old
   inventory scenario. Rewording all three `scheduled_reversal` labels to
   `"thing"`/`"when"`/`"how much"`, keeping the kinds distinct so the sibling
   distinctness check is untouched, leaves **all 2,987 green**. The pass
   genuinely closed a sampling defect at this site (`intercompany_counterparty`
   went from unasserted to asserted) and opened a tautology defect in the same
   edit. It also makes the recorded claim *"no scenario asserts less than it
   did"* untrue as written.

**Standing question — does any suite report a pass the register (34 entries)
says cannot be true? NO**, for the second consecutive pass. All eight forbidden
criteria — `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`,
`AC-F5-02`, `-03`, `-05` — are claimed by nothing; every node id that names one
denies it in the same name, and every `COVERS` line narrows itself in the same
sentence. All four of register 34's "built instead" claims are now
mutation-held; the two that were `PARTIAL` and `ADVISORY` last pass are closed.
256 `AC-…` identifiers referenced at both commits, none lost.

**The rendered-UI gold sweep is no longer inconclusive.** Pass 18's predicate
(`r > 150`) matched neither `#8A5A17` nor its ground and proved nothing. It is
now the four exact shipped token values and reads `stroke`/`fill` as well as
`color`/`background`, and a **positive control proves it fires** — gold on
`.btn.approve` ("a human decision") on the approval screen and on the brand
`.pull-dot`, and nowhere else. Also measured: zero green, zero text below 0.5
compounded opacity, zero horizontal overflow, one `h1` and the `nav`/`main`
landmark pair on every screen, and `.ctx` at **167.00 × 48.56 px, x=14.00,
y=55.88, `display:block`, parent `.lockup`, identical on all twelve
screen×viewport measurements**.

**The human's pilot (pid 59422, port 8030 — re-read from `lsof` this pass, not
carried forward from 50367) was verified alive before and after every
invocation.** 8030/8031 were never probed. Every process I started was reaped
inside the single command invocation that started it, by `killpg` on its own
process group; no name-based sweep was run. `lsof` on 8021/8022 empty after every
teardown. The smoke drove the real export path end to end — approve 403, override
200, export 200, file `/export/CS-0034B894B391.csv` retrievable with an FBDI
header — and the shared ledger grew 10,739,712 → 10,780,672 bytes, while the
2,987-scenario test tree left it byte-identical (`449791062f…`) across all five
order-independence runs.

**Advisory, for `ui-ux-designer`:** the build's own answer to the population
question renders at **y = 7,601.7 px** on `/inventory` — a reader must scroll
~7,600 px to meet it. Visible, full opacity, correct; just a long way down.

**Advisory, for `code-agent`:** the F3 shape scenario's docstring says it
*"holds on the day findings become ledger-recorded and the answer becomes
computable"*. It asserts `computable is False`, and mutation F3-M2 confirms it
fails the moment that becomes true. The assertion is right; the sentence
describing it is not.

**Gate status: no blocking suite failed, and no automated scenario failed
anywhere.** The two sampling-sweep findings are not suite failures — they are
scenarios that pass and should not be able to. They are put in front of the
human as findings, not as a stopped gate, and neither contradicts the register.

---

### 2026-08-03 — Gate 8 · Test — `test-agent`, **re-run after the pass-18 loop-back, at `dev` @ `1b1b56e`** (parent repo @ `2f9b373`) — SUPERSEDED

**All seven automated suites EXECUTED, exit code 0, 2,977 of 2,977 scenarios
passed at every suite entry point and in SIX whole-tree runs — canonical order,
`reverse`, and four salted shuffles on this agent's own plugin, whose salt
appears nowhere in the project tree. Zero skipped, zero vacuous, zero empty
`parametrize`.** Structured per-scenario evidence:
`test-evidence/*-2026-08-03.md` (14 files) plus 14 freshly captured Playwright
screenshots. The entire superseded corpus was deleted and rewritten; every file
names both commits and its presence on disk was verified after writing.

**Test-count delta: 2,955 → 2,977 = +25 added, −3 removed, 3 changed.** The
three removals are named individually in
`test-evidence/changed-scenario-audit-2026-08-03.md` — two were the false
`AC-F5-02`/`-03` claims gate 8 blocked on, one was a rename that drops a
criterion claim and strengthens its body.

| Suite | Status | Exit | Scenarios | Pass | Fail | Owner | Blocking |
|---|---|---|---|---|---|---|---|
| unit / integration | `EXECUTED` | 0 | 2,302 | 2,302 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 355 | 355 | 0 | `functional-design-agent` | yes |
| ux | `EXECUTED` | 0 | 194 | 194 | 0 | `ui-ux-designer` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | `responsible-ai-architect` | yes |
| architecture | `EXECUTED` | 0 | 28 | 28 | 0 | `solution-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | `industry-expert` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | `security-architect` | yes |
| **rendered-UI (Playwright)** | `EXECUTED` | 0 | 8 | 6 | **1** | `test-agent` | yes |
| **smoke (served pilot, 8021)** | `EXECUTED` | 1 | 26 | 24 | **1** | `test-agent` | yes |

The rendered-UI suite's eighth scenario is `INCONCLUSIVE`, not a pass: my gold
predicate (`r > 150`) does not match the light token `#8A5A17`, so the sweep
matched nothing and proves nothing. Recorded as inconclusive rather than as
"0 violations". The smoke's S22 is `MIS-TARGETED`, also not a pass.

**Both pass-18 fixes verified rather than accepted, by 19 mutations in a
detached worktree.**

- **The `.ctx` defect is fixed.** Re-measured myself in Chromium against the
  served pilot: **167.00 px × 48.56 px at x=14.00, y=55.88, identical on six
  screens at both 1280 and 1440**, `display:block`, parent `.lockup` with
  `display:block`, `.lockup` children exactly `[lockup-row, ctx]`. (Pass 17's
  defect measured 67.53 × 116.25.) Re-scoping the rule back to `.brand .ctx`
  fails 2 scenarios; moving `.ctx` back inside the flex row fails 1.
- **The orphan checker holds.** `NO_EXEMPTIONS` is empty, passed empty and
  asserted empty — adding **any** exemption fails a scenario. The parser
  **raises** on `@media`/`@import`/`@supports`/`@font-face` rather than
  reporting "no orphans". Nine scenarios prove the matcher can say NO and are
  mutation-confirmed in both directions. The regression scenario genuinely
  reports a re-added `.brand .ctx` on the real stylesheet. The post-POST
  re-traversal is real: removing it makes `.seal` and `.card.approved` orphans.
- **`AC-F5-02`/`-03`/`-05` are falsifiable in both directions** — all nine
  mutations caught, including *ids reconciled with the disclosure left behind*.
- **The alias forgery guard holds.** My own M3(d), injected into product code,
  is refused; so are the de-linked and self-alias variants.

**Standing question — does any suite report a pass the register (34 entries)
says cannot be true? NO**, for the first time since it returned YES last pass.
All eight forbidden criteria — `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
`AC-F40-17`, `AC-F36-48`, and now `AC-F5-02`/`-03`/`-05` — are claimed by
nothing.

**Three findings sit beside the register, not against it. Two are blocking.**

1. **BLOCKING — the disclosure was removed from one screen and left standing on
   the four screens that screen links to.** All four
   `/evidence/agent/<id>` pages for the absent agents render *"An agent that can
   act is an agent that is listed."* in the subtitle under the `<h1>`, four
   lines above *"This agent authored findings in this run and has no entry in
   the principal registry under this id."* Register 34's wording (*"gone from
   that screen"*) is literally true, and the same entry records that
   `/inventory` links each absent agent to exactly these pages. The guarding
   assertion is scoped to `/inventory` alone and there is exactly one such
   assertion in the whole tree. **Same shape as the defect pass 18 fixed.**
2. **BLOCKING — `AC-F5-07` has the same defect, and I agree with `code-agent`.**
   Its scenario reads `agents[0]` for two strings while the criterion says
   *"each agent"*. Mutation F7-M strips the fields from three of four agent
   rows and **2,977 scenarios stay green**. Weaker than the `AC-F5-02` case in
   one respect (the build satisfies it today, so the green is unheld rather
   than untrue) and the same in the one that matters. Not touched, per
   `code-agent`'s point that narrowing a criterion's claim is a Plan-gate call.
3. **ADVISORY — `unregistered_actors` returns `[]` and is asserted by nothing.**
   Register 34 offers it as the broker's own answer to the population question;
   it is a set difference over the decision ledger, findings are not
   ledger-recorded (that is `LINEAGE_UNTRAVERSED`'s own second entry), so it
   **cannot become non-empty in this build**. `grep` finds no scenario naming
   it. Register 33's convention for this shape is UNKNOWN, not none.

**The human's pilot (pid 50367, port 8030) was verified alive before and after
every invocation.** 8030/8031 were never probed. All processes were started and
reaped inside a single command invocation each, killed by `killpg` on their own
process group; no name-based sweep was run. `lsof` on 8021/8022 empty after
every teardown. The smoke drives the real export path and grew the shared
ledger 10,702,848 → 10,723,328 bytes; the test tree left it byte-identical
across all six whole-tree runs.

---

### 2026-08-03 — Gate 8 · Test — `test-agent`, **re-run after the pass-17 UX redesign, at `dev` @ `6bf8ed9`** (parent repo @ `5268e9b`)

**All seven automated suites EXECUTED, exit code 0, 2,955 of 2,955 scenarios
passed at every suite entry point and in EIGHT whole-tree runs — file order,
four salted seeds, `reverse` twice, and once under vacuous-pass
instrumentation — zero skipped. The rendered-UI backend and the smoke each
found one thing the 2,955 do not.** Structured per-scenario evidence:
`test-evidence/*-2026-08-03.md` (13 files), plus 13 freshly captured Playwright
screenshots. **The entire superseded corpus was deleted and rewritten**; every
file names both commits and its presence on disk was verified after writing.

| Suite | Status | Exit | Scenarios | Pass | Fail | Skip | Owner | Blocking |
|---|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 2,281 | 2,281 | 0 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 354 | 354 | 0 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 28 | 28 | 0 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 194 | 194 | 0 | 0 | `ui-ux-designer` | yes |
| **automated total** | | | **2,955** | **2,955** | **0** | **0** | | |
| post-deploy smoke | `EXECUTED` | 1 | 19 | 18 | **1** | 0 | `test-agent` | yes |
| rendered-UI (Playwright) | `EXECUTED` | — | 10 | 9 | **1** | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. 2,281 + 674 = 2,955, and
the seven per-suite collections sum to the whole-tree collection exactly. The
`ux` suite launched Chromium 148.0.7778.96 — its conftest exits 4 (STATIC-ONLY)
rather than passing if Playwright or the browser binary is absent, so exit 0 is
positive evidence a rendering engine answered. No server was started inside this
agent's turn: the pilot was started, driven and reaped inside single command
invocations four times.

**The screens moved and the checks moved with them — verified independently,
not accepted.** `code-agent`'s eight-row changed-scenario table was checked row
by row against `git diff 9d605b1..6bf8ed9`, and then twice more by whole-tree
set difference:

* **Every `data-testid` asserted before is still asserted, with exactly one
  exception** — 133 before, 171 after, and the only one dropped is
  `nav-readiness`, the navigation slot `UX_KB` A2.2 deliberately removed, which
  no longer exists anywhere in `backend/app/` either.
* **175 criterion IDs are named by some node ID before and after — set
  identical.** **103 `COVERS` joins before and after — set identical.** No
  criterion lost its scenario and none lost its join.

**Test-count delta: +200 added, −19 removed, 4 changed groups.** Baseline 2,774
at `9d605b1` (this agent's last verified tree, not `code-agent`'s 2,785
baseline; the 11 between is `test_ui_typography_floor.py`). **`code-agent`
reports "0 tests deleted" and at node-ID level that is not accurate — 19 node
IDs are gone.** No test file was deleted and no coverage was abandoned: 17 are
renames or screen re-points, and each of the 19 is tabulated with its successor
in `test-evidence/unit-integration-2026-08-03.md`. The other two —
`test_it_has_a_permanent_place_in_the_navigation` and
`test_readiness_is_reachable_from_the_navigation_on_every_screen` — assert a
property the approved redesign deliberately **reversed**, and each is replaced
by a stronger claim (every agent has its own linkable readiness address, which
the old build could not satisfy for four of five agents). Recorded as a coverage
decision in front of the human rather than folded into a rename.

**The eight edges are mutation-proved.** Breaking edge **E5**'s target
mid-chain failed exactly two scenarios and the chain failed **at the agent
hop** — `/evidence/agent/agent.crossperiod-surveillance-mutated returned 404`
raised from `U.fetch(agent_href)` — with the run hop's assertion already passed
above it, and not at the readiness hop after it. Deleting the **row** `E8` from
`graph.EDGES` failed the guard `test_exactly_the_eight_declared_edges_exist`.
The table is genuinely load-bearing in both directions.

**`SCREEN_ALIASES` — the claim holds literally; the property it secures does
not.** There is no test-side alias constant to widen, the router does not even
consult the table at request time (mutating it is inert on routing), and a bogus
alias to a non-served path is caught. **But a test file can still hide an
orphan**: with `/refusals` de-linked from the navigation the sweep correctly
failed with `AssertionError: {'/refusals'}`, and **one line** in a test file —
`routes.SCREEN_ALIASES["/refusals"] = "/queue"` — made all 8 scenarios pass.
Both guards are satisfied by the forged row, because nothing checks that an
alias serves the screen it names except for the three hard-coded queue
addresses. **Nothing in the build does this today**, so no suite reports a false
pass on this path. Feedback for `code-agent`.

**Readiness is honest.** Driven over HTTP for all five agents: four
(`omission-detector`, `coding-detect`, `anomaly-detect`, `fidelity-check`)
render **all five conditions `not_yet_evaluable`**, `data-ready="false"`, **no
`precision-figure`** and an explicit `precision-figure-absent`. Nothing is
rendered as a pass and no precision figure appears for a skill it was not
computed for. The fifth, `crossperiod-surveillance`, has real data (3
`not_yet_evaluable`, 1 `not_met`, 1 `met`) and carries its figure.

**BLOCKING FINDING 1 — the id mismatch is disclosed on the agent page and
silently dropped on the Inventory, and a suite reports the criterion green.**
The brief asked whether anything elsewhere drops the unmatched agents. It does.
Five agents authored findings in the pilot run; **four have no registry entry
under their author id and do not appear on `/inventory` at all**. `AC-F5-02`'s
Given clause is *"an agent that has been deployed and has **performed at least
one action**"*. The covering scenario nevertheless passes, because it asserts
`inventory == principals.DIRECTORY` — **the projection compared against its own
source**, an equality true by construction that cannot fail for the reason the
criterion is about. `/inventory`'s own rendered prose still reads *"An agent
that can act is an agent that is listed."* The agent page's own comment states
the standard being missed: *"an inventory that silently omits an agent that
acted is an inventory that makes its own artefacts unattributable."*
Same gap, second face: **seven dossiers exist and zero appear in any lineage**
(union of artefacts across all eleven rows is 9, none a dossier), yet every row
reports `complete=True` and `test_AC_F5_03_…` asserts exactly that — against
`AC-F5-05`'s *"a partial list is never returned unlabelled"*. Reproduced over
HTTP against the served pilot as smoke **S12 FAIL**.

**BLOCKING FINDING 2 — a rendering defect the redesign introduced, on every
screen, that no suite can see.** The sidebar context line
("Northwind Grid Holdings - 2026-06 - Day 3") renders in a **67.5px-wide,
116.25px-tall box, roughly one word per line**, on all four screens measured at
both viewports. Root cause: the rule is scoped **`.brand .ctx`**, and pass 17's
A2.8 identity layer replaced `.brand` with `.lockup` — `chrome.lockup()`'s own
docstring says *"Replaces the plain `.brand` text block"* — without re-scoping
it. **`.lockup .ctx` has no rule**, so the span is an unstyled min-content flex
child of an `align-items:center` row in a ~160px sidebar. Invisible to every
non-rendering check: the class is emitted, the string `.ctx` *does* exist in the
stylesheet so a grep passes, and the page returns 200 with the right text.
`test_ui_brand.py`'s 32 new scenarios do not catch it and neither does the
194-scenario `ux` suite. Visible top-left in
`ux-queue-desktop-1280-2026-08-03.png`.

**The two conflicts, reported and not resolved.**
* **(a) `test_ui_dossier` vs edge E8.** Both halves of the claim confirmed
  genuinely untouched. `test_there_is_no_external_reference_of_any_kind` does
  not appear in the diff, and it was re-proved in a real browser: the served
  dossier saved to disk and opened as `file://` issued **zero** non-`file://`
  requests and rendered still styled (`risk-band` → `rgb(246, 228, 227)`).
  `AC-F41-04`'s retained view (`state._retained_view`) is a `<section>` with an
  `<h2>`, a `<table>` and a `<p>` and contains **no anchor of any kind**.
  §9.4's three binding consequences concern purity, byte-determinism and inlined
  styles — none speaks to anchors on the dossier screen. Whether the screen
  should carry zero anchors is a ruling for `functional-design-agent`.
* **(b) Gold narrower than `UX_KB` A2.8.** The build paints gold on five
  selectors, asserted by set **equality**; A2.8 additionally gives it to
  `.goldline` and the six section icons, and neither is carried. Material to
  whoever rules: **A2.8's own version row reads "Human request, 2026-08-03;
  approval pending"** — the KB entry the build departs from is not yet approved.
  Confirmed in a real browser: **28 gold-painted elements across 12 renders, all
  `.pull`, `.pull-dot` or `.btn.approve`, zero offenders** — the independent
  witness, since the unit suite asserts the law by parsing the stylesheet as
  text.

**Order independence — eight whole-tree runs, all 2,955, ledger untouched in
every one.** The generator is **salted, and the reason is itself a finding**:
the obvious unsalted `random.Random(seed)` + Fisher–Yates reproduced
`code-agent`'s fingerprints **exactly** (`seed:1` → `759308beb6c37d78`, 38
adjacencies). That corroborates that the recorded permutations are real, but it
is the same run twice, so the matrix was discarded and re-run salted.

| Ordering | Result | Wall | Same-file adjacencies | Fingerprint |
|---|---|---|---|---|
| file order (control) | 2,955 pass, exit 0 | 209.4s | 2,846 | — |
| `seed:1` salted | 2,955 pass, exit 0 | 243.3s | 28 | `9595c2e4e0f72c1c` |
| `seed:7` salted | 2,955 pass, exit 0 | 249.6s | 39 | `d929fa3e6a9f5d91` |
| `seed:42` salted | 2,955 pass, exit 0 | 250.2s | 32 | `45a3759ce39c82bb` |
| `seed:20260803` salted | 2,955 pass, exit 0 | 247.4s | 34 | `cf3222bf352fa738` |
| `reverse` | 2,955 pass, exit 0 | 215.5s | 2,846 | `fa4584ef39e7c77b` |
| `reverse` again | 2,955 pass, exit 0 | 214.9s | 2,846 | `fa4584ef39e7c77b` |

**The two sweeps.** Empty-`parametrize`: **0 sites** across 99 modules. Vacuous
pass, run **dynamically** rather than inferred — a whole-tree run under an
out-of-tree plugin wrapping `Document.all`/`.tags`: 484 scenarios make document
queries, **15 passed with every query empty, and all 15 are negative assertions
where the empty result IS the claim.** The three IA-relevant ones each have a
positive counterpart on the other screen, so neither can pass on a page that
failed to render.

**Rendered-UI verification: Playwright/Chromium against the SERVED pilot.** Six
screens × two viewports plus the offline dossier, 13 screenshots. **Zero green
under computed colour** across 12 renders; **zero text below 0.05 effective
(compounded) opacity**; `AC-F41-03` holds — `riskiest-figure` at **40.0px** is
the largest text on the finding, against a 28.0px `h1`; **every object page
names its object in its rendered `<h1>`** and the finding's carries **no
approval vocabulary** at either viewport. Minimum computed font size is
**12.0px**, improved from 10.0px last pass — the carried `ui-ux-designer`
advisory is materially better.

**This agent's own defects, recorded rather than quietly corrected.** Two, both
mine. **(1)** Smoke S7 reported two links on the dossier where there is one
anchor — the driver's `href="…"` regex also matched `data-href="…"` on the same
element. Verified against `Document.hrefs()`, fixed, whole smoke re-run. **(2)**
Rendered R7 **passed on an empty set**: the gold detector used a guessed colour
range requiring `r > 140` and light `--gold` is `#8A5A17` (`r = 138`), so it
measured nothing and reported PASS — a vacuous pass in my own suite. Rewritten
to resolve the document's own token through the engine and to carry a
non-vacuity guard. Also recorded: the "clipped PRESENT ANOMAL pill" I thought I
saw in a screenshot was **refuted by measurement** (136.4px of text in a 152.4px
box) and is not a defect.

**The standing question — `does any suite report a pass the register says cannot
be true?` — returns YES, breaking six consecutive clean passes.** The register
has 33 entries (1–33, verified, no gaps) and **the five declared criteria are
clean**: `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17` and `AC-F36-48`
are claimed by **zero** of the 2,955 scenario names — the only two node IDs
containing an ID are the parametrisation labels of a scenario asserting the
export is **refused** — and by zero `COVERS` joins that are not self-denying.
The 200 new node IDs were scanned with the same query and returned zero. **The
YES comes from a route the register does not cover**: `AC-F5-02` and
`AC-F5-03`/`-05` are reported green over a build that cannot support them, and
on the evidence that gap needs a register entry it does not have.

**Gate status: BLOCKED — two blocking findings, neither of which is a failing
automated suite.** All seven suites are `EXECUTED` and green, which is exactly
why both are reported: a green suite is not the same as a true claim. The
decision is the human's — send back to `code-agent` (both findings are build
defects), or record an `[override]` in the Decisions Log naming the
suite/scenario and the reason. No override is recorded here; `test-agent` does
not grant one.

---

### 2026-08-02 — Gate 8 · Test — `test-agent`, **FINAL re-run at `dev` @ `9d605b1`** (parent repo @ `e14c497`) — SUPERSEDED

**All seven automated suites EXECUTED, exit code 0, 2,774 of 2,774 scenarios
passed at every suite entry point and in NINE whole-tree runs — file order plus
four seeds plus `reverse` four separate times — zero skipped. The post-deploy
smoke is 17 of 17 against the pilot as found, driven over HTTP through the real
export path on 8021. Both of the previous pass's items are closed, and both were
verified by MUTATION rather than by reading the code.** Structured per-scenario
evidence: `test-evidence/*-2026-08-02.md`, plus eight freshly captured
Playwright screenshots. **The entire superseded corpus was deleted and
rewritten**; all ten files name both commits and their presence on disk was
verified after writing.

| Suite | Status | Exit | Scenarios | Pass | Fail | Skip | Owner | Blocking |
|---|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 2,108 | 2,108 | 0 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 354 | 354 | 0 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 28 | 28 | 0 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | 0 | `ui-ux-designer` | yes |
| **automated total** | | | **2,774** | **2,774** | **0** | **0** | | |
| post-deploy smoke | `EXECUTED` | 0 | 17 | 17 | 0 | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. 2,108 + 666 = 2,774, and
the seven per-suite collections sum to the whole-tree collection exactly. The
`ux` suite launched Chromium — its conftest exits 4 (STATIC-ONLY) rather than
passing if Playwright or the browser binary is absent, so exit 0 is positive
evidence a rendering engine answered. No server was started inside this agent's
turn: the pilot was started, driven and reaped inside single command invocations
six times.

**Finding 1 — the `AC-F12-15` assertion. Fixed, and genuinely stronger, with
one qualification stated rather than glossed.**

- **The timestamp case passes clean.** `2026-08-02T07:04:40.023468+00:00` no
  longer registers: `0.02` inside `40.023468` is not a standalone token.
- **`0.020` is now caught** — the "passed dirty" case. So is `0.0473`, and so is
  every value strictly between the bounds, which is what `plan_injection`
  actually draws and what the old assertion never reached.
- **Proved on the real leak path by MUTATION**, not on synthetic strings:
  `BAND_STATEMENT` amended to leak `0.0473` failed **all four** sites, including
  the Playwright-driven UX one that reads `inner_text` from a real browser. The
  **old** assertion, evaluated against the same mutated build, returned
  `PASSES -- leak undetected`.
- **`code-agent`'s measurement is confirmed**: zero in-band tokens across all
  twelve served pages (81–98 numeric tokens per page). Zero old-form substring
  hits too, so the two agree on this build and the previous failure was genuinely
  intermittent.
- **The honest qualification: it is not a strict superset.** The only inputs the
  old form flagged and the new one does not are digit runs inside a longer
  numeric run — precisely the false positives. On every shape that is a readable
  rate, the new form is strictly stronger.

**Finding 2 — the live-ledger guard. Closed, and the refcounting is
mutation-proved.**

- **The unit tree's leak is gone**: `dev/var/broker_db.sqlite3` shows a **0-byte
  delta** across all nine whole-tree runs, mtime unchanged. The previous pass's
  32,768-bytes-per-run finding is closed.
- **MUTATION M3 — the refcount removed** (each caller builds a new `Guard` and
  lays a second patch, exactly the defect `code-agent`'s own ordering matrix
  caught): **3 failures in file order, 6 under `seed:1`**. Reverted, tree
  re-verified clean. Worth recording: **the original defect was invisible in file
  order and this mutation is not** — the two pinning scenarios now catch it in
  any ordering, which is a strict improvement on the condition that exposed it.
- **The reasoning about `default_store_path` holds, and was tested rather than
  accepted.** Simulated both ways: unpatched, the pass-15 file-size check catches
  the write; redirected, it returns **True while the real ledger grows** —
  vacuous, exactly as `code-agent` says. Leaving it unpatched is correct.

**Order independence — nine whole-tree runs, all 2,774.** This agent's own
plugin, outside the repository, a uniform global Fisher–Yates (35 same-file
adjacencies at `seed:1`, which `code-agent`'s round-robin cannot produce).
`reverse` was re-run **four** times — identical fingerprint `d0ee639c287714bd`
each time, so it is the same permutation four times, which is what ruling out an
intermittent failure requires. The realised order was fingerprinted for every run.

**Test-count delta: +38 added, 0 removed, 4 changed.** Baseline 2,736 → 2,774,
computed by differencing collected node-ID sets between a throwaway `git
worktree` at `75f5e27` and the tree at `9d605b1`. Accounted for exactly:
`test_harness_rendered_numbers.py` 25, `test_harness_live_ledger_guard.py` 12,
architecture 1. **Zero removed** — `comm -23` over the two sets returns empty and
no test file was deleted. The 4 changed are the `AC-F12-15` sites; every prose
ban, the percentage-window regex, the twelve-path sweep and the header sweep are
all retained.

**Rendered-UI verification: Playwright/Chromium against the SERVED pilot.** Four
screens × two viewports, 8 captures, 8 clean: 200 everywhere, **zero green
elements under computed colour**, **zero text nodes below 0.05 effective
(compounded) opacity**, and the gate-5 reading order confirmed on the item
screen — `riskiest-figure` `$918,240.00` rendered at **42.0px**, the largest text
on the screen, against a 20.0px `h1`; controls are R1–R6 and Reject, with **no
approve control**. RNTL is not applicable: MVP1 is desktop web only.

**Findings for a human — none blocking, all recorded.**

- **NEW: the collision class is relocated, not eliminated.** The band check reads
  the whole served document **including the `<style>` block**, where in-band
  decimals are ordinary. Rewriting one declaration from `letter-spacing:.05em`
  to `letter-spacing:0.05em` — **zero rendered effect** — fails three
  `AC-F12-15` scenarios with `['0.05']`. It passes today only because the
  stylesheet happens to be authored in leading-dot form. Mutation-proved,
  reverted. Feedback for `code-agent`.
- **NEW: the docstring again claims more than the assertion checks.**
  `rendered_numbers` names `.02` among the leaks the substring form let through,
  in the passage justifying the replacement — but a leading-dot decimal produces
  no token, so the new form misses it too. Not a regression (neither form catches
  it) and nothing leaks today, but it is the **same class of defect as the
  original**.
- **NEW, this agent's own driver defect, fixed inside the pass:** the first smoke
  attempt read override reason codes from `<option>` elements; they are radio
  inputs, so it posted the *denial* code and the product correctly refused with
  403, naming the closed list. S6–S8 failed on that attempt and **the failures
  were this agent's, not the build's** — recorded rather than quietly re-run.
- **Observation: the smoke and the human's pilot share one live ledger.** The
  smoke wrote +20,480 bytes to `dev/var/broker_db.sqlite3`, the same file the
  human's instance on 8030 uses, so the override and export it recorded on
  `PROP-2026-06-0031` are visible there. Not a fault — the pilot is the real app
  and the guard's scope is tests.
- **Recorded: `SIGTERM` never sufficed.** Teardown needed `SIGKILL` on all six
  invocations. The previous pass's `SIGTERM`-then-`wait` is exactly what left a
  survivor — and the name-based sweep that followed killed the human's pilot.
  This pass scopes teardown to the process group it created (`os.killpg`), never
  to a process name; **pid 6587 was verified alive at the start and end of every
  invocation** and ports 8030/8031 were never probed.
- **Carried advisory for `ui-ux-designer`, re-verified and unchanged:** minimum
  computed font size is **10.0px** on all four screens at both viewports.
  UX-4/`AC-F41-03` is a *relative* check and passes, and no rule sets an absolute
  minimum, so no suite fails.

**The standing question — `does any suite report a pass the register says cannot
be true?` — returns NO for the SEVENTH consecutive pass.** The register has 33
entries (1–33, verified, no gaps). `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
`AC-F40-17` and `AC-F36-48` are claimed by **zero** of the 2,774 scenario names —
the only two node IDs containing an ID are the parametrisation labels of a
scenario asserting the export is **refused** — and by zero `COVERS` joins that
are not self-denying. The 38 new node IDs were scanned with the same query and
returned zero.

**Gate status: PASS. No blocking suite failed and no blocking condition remains
open.** All seven suites plus the smoke are `EXECUTED` and green; both items the
loop-back raised were fixed rather than overridden, and both were verified here
by mutation rather than accepted. No `[override]` is required.

---

### 2026-08-02 — Gate 8 · Test — `test-agent`, **re-run at `dev` @ `75f5e27`** (parent repo @ `21af9da`)

**All seven automated suites EXECUTED, 2,736 of 2,736 scenarios passed at every
suite entry point and in five of six collection orders, zero skipped. The
post-deploy smoke is 16 of 16 against the pilot as found, driven over HTTP
through the real export path. Everything the loop-back asked to be verified was
verified — and eight of those verifications were done by MUTATION, breaking the
control and watching the guard fail, rather than by reading the code.**

**Two things stop this from being a clean close, and neither is rounded up:**

1. **One scenario FAILED in the `reverse` collection ordering** —
   `functional/test_f12_probe_criteria.py::test_AC_F12_15_the_rendered_dom_carries_no_probe_rate`.
   `functional` is a **blocking** suite, so this is an **unmet gate
   condition**. It is **not** an order dependence and **not** a product defect:
   the scenario asserts the bare substring `"0.02"` (the disclosed probe band's
   low bound) appears nowhere on the page, and it collided with a rendered
   wall-clock timestamp `…T07:04:40.023468+00:00`. Its two substantive
   assertions both passed, so no probe rate leaked. Isolated re-runs: **0
   failures in 12**, and **the identical `reverse` permutation re-run gave
   2,736 pass, exit 0** — the same order, the opposite result, which is what an
   order dependence cannot do. It is an **intermittent** assertion that can fail
   in any ordering, roughly 1 rendered timestamp in 1,000. The narrow fix —
   assert the band value as a number, or only within the probe-adjacent windows
   the scenario already computes — is feedback for `code-agent`, not something
   `test-agent` applied.
2. **A new finding, non-blocking:** `pytest backend/tests` still grows the
   developer's live decision ledger by 32,768 bytes per run. The fix landed at
   `4e5ee47` closed the **suites** tree (all six entry points now +0 bytes) but
   `backend/tests/conftest.py`'s `ges_app` and `ges_stack` still call
   `create_app(...)` with no `broker_factory`; `test_emission_gate.py` adds 17
   decision rows per run. The new architecture guard is scoped to the suites'
   fixture, so it passes over this.

Structured per-scenario evidence: `test-evidence/*-2026-08-02.md`, plus eight
freshly captured Playwright screenshots. **The entire superseded corpus was
deleted and rewritten**; every file names both commits and their presence on
disk was verified after writing.

| Suite | Status | Exit | Scenarios | Pass | Fail | Skip | Owner | Blocking |
|---|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 2,071 | 2,071 | 0 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 at entry point; **1 under `reverse`** | 354 | 354 (entry point) / **353 under `reverse`** | **1 under `reverse`** | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 27 | 27 | 0 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | 0 | `ui-ux-designer` | yes |
| **automated total** | | | **2,736** | **2,736 in 5 of 6 orderings; 2,735 in `reverse`** | **0 / 1** | **0** | | |
| post-deploy smoke | `EXECUTED` | 0 | 16 | 16 | 0 | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. 2,071 + 665 = 2,736, and
the seven per-suite collections sum to the whole-tree collection exactly. The
`ux` suite launched Chromium — its conftest exits 4 (STATIC-ONLY) rather than
passing if Playwright or the browser binary is absent, so exit 0 is positive
evidence a rendering engine answered. No server was started inside this agent's
turn: the pilot was started, driven and reaped inside single command
invocations three times, and 8021 was verified free after each.

**Verified by mutation, not by reading — eight mutations, eight guards fired.**

| # | Mutation applied | Guard that fired |
|---|---|---|
| M1 | `from app import ges_client` added to `ges/restatement.py` | `test_the_comparator_reaches_nothing_in_the_agent_runtime` — `Extra items in the left set: 'app'` |
| M2 | the `consecutive += 1` counting the emission being judged removed | both G-RESTATE count scenarios — `assert 1 == 2` |
| M3 | `broker_factory=lambda: suite_broker` removed from the suites' `ges_http` | the new architecture guard — "the app under test is not using the suite's broker", and the live ledger grew 4,096 bytes on cue |
| M4 | `UNEVALUABLE = "did_not_fire"` | `…a_missing_emission_fixture_is_not_read_as_the_constraint_holding` |
| M5 | the inconclusive branch moved ahead of the unevidenced branch | `…fails_the_suite_even_with_no_baseline` — `assert 'inconclusive' == 'fail'` |
| M6 | `comparator.record(...)` moved out of `if decision.allowed:` | `test_a_withheld_emission_does_not_become_a_prior_period_narrative` — `assert [12] == []` |
| M7 | the `restatement_field_write_attempt` control event suppressed while the refusal still raises | **6** scenarios, covering all three agent write paths |
| M8 | `app.ges_gateway` moved into `PROCESS_STATE_MODULES` | **11** scenarios, led by `test_the_gateway_is_guarded_without_being_discarded` |

Every mutation was reverted with `git checkout` and the tree re-checked clean;
`dev` stayed at `75f5e27` and the parent at `21af9da` throughout.

**The loop-back's six items, each answered:**

1. **`AC-F36-33`'s comparator** — the AST guard is load-bearing (M1); all three
   agent write paths fail **and** each records a control event, asserted per
   path and proved by M7; `/ges/emit` records a narrative only on an ALLOW,
   proved by M6. The comparator runs **before** the broker, so there is no
   window in which the request carries anything else.
2. **`AC-F36-30`'s failing case** — it fails for the missing fixture, not for
   `AC-F36-24`'s inconclusive: the scenario seeds a baseline and asserts the
   suite **PASSes** before the removal, and a separate scenario asserts FAIL ≠
   INCONCLUSIVE with no baseline (M5 confirms the ordering is real).
   `unevaluable != did_not_fire` is asserted and M4 confirms it.
3. **The live-ledger finding** — fixed for the suites tree and re-verified by
   reverting it (M3). All six suite entry points now grow the file by **0
   bytes**. **The unit tree is not fixed** — see the finding above.
4. **`PROCESS_STATE_MODULES` was split, not widened** — the gateway being *not*
   discarded is asserted twice, and M8 shows moving it into the discarded set
   fails 11 scenarios rather than reading as a tightening.
5. **Order independence** — this agent's own plugin, its own seeds. Five of six
   green at 2,736; the sixth carries the intermittent scenario described above.
6. **The four changed G-RESTATE scenarios assert strictly more** — each retains
   every prior assertion and gains one on the comparator-derived value. The
   escalation count of 3 is now an off-by-one the comparator can fail, proved
   by M2.

**Test-count delta: +44, 0 removed, 7 changed.** Computed by collecting node IDs
at `fc197a6` (in a throwaway `git worktree`, so nothing was checked out over the
tree under test) and at `75f5e27`, then differencing the sets: 2,692 → 2,736,
added 44, removed **0**. Accounted for exactly: `test_restatement_comparator.py`
32, `test_bundle_publication.py` 7, `test_pilot_process_state.py` 4,
`architecture` 1. The 7 changed scenarios are tabulated in
`test-evidence/unit-integration-2026-08-02.md`; every one asserts at least as
much as before.

**The standing question, sixth consecutive pass: no.** No suite reports a pass
the 33-entry register says cannot be true. The five declared criteria
(`AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`) are claimed
by **zero** of the 2,736 scenario names — the only two node IDs containing an ID
are the parametrisation labels of a scenario asserting the export is **refused**
— and by zero `COVERS` joins that are not self-denying. The 44 new node IDs were
scanned with the same query and returned zero occurrences.

### 2026-08-02 — Gate 8 · Test — `test-agent`, **FINAL re-run at `dev` @ `fc197a6`** (parent repo @ `7ec615a`)

**All seven automated suites EXECUTED, exit code 0, 2,692 of 2,692 scenarios
passed, zero skipped, under SIX different collection orders. The post-deploy
smoke is 14 of 14. The interleaved-shuffle order dependence — the blocking
condition that stopped this gate at the previous pass — is CLOSED, verified
with this agent's own plugin and its own seeds.** Structured per-scenario
evidence: `test-evidence/*-2026-08-02.md`, plus eight Playwright screenshots.
**The entire superseded corpus was deleted and rewritten**; every file names
both commits, and their presence on disk was verified after writing.

| Suite | Status | Exit | Scenarios | Pass | Fail | Skip | Owner | Blocking |
|---|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 2,028 | 2,028 | 0 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 354 | 354 | 0 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 26 | 26 | 0 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | 0 | `ui-ux-designer` | yes |
| **automated total** | | | **2,692** | **2,692** | **0** | **0** | | |
| post-deploy smoke | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. 2,028 + 664 = 2,692. The
`ux` suite launched Chromium — its conftest exits 4 (STATIC-ONLY) rather than
passing if Playwright or the browser binary is absent, so exit 0 is positive
evidence a rendering engine answered. No server was started inside this agent's
turn: the pilot was started, driven and reaped inside single command
invocations four times, and 8021 was verified free after each.

**Order independence — the gate-stopping item, CLOSED.** `code-agent` flagged
the one gap it could not close itself: its interleave plugin is not
`test-agent`'s. So this agent wrote its own, and it is a **different generator,
not the same one at different seeds** — `code-agent`'s is a round-robin across
shuffled per-file buckets; this agent's is a uniform global Fisher–Yates over
all 2,692 items with no bucketing. Measured proof they differ: a strict
round-robin can never place two same-file items adjacently, and this agent's
seed-1 order contains **39 such adjacencies**. All six orderings green:

| Ordering | Result | Wall | Order fingerprint |
|---|---|---|---|
| file order (control) | 2,692 pass, exit 0 | 194.8s | — |
| `seed:1` | 2,692 pass, exit 0 | 193.7s | `b31c9d98856be496` |
| `seed:7` | 2,692 pass, exit 0 | 202.4s | `3f744be61621fdc0` |
| `seed:42` | 2,692 pass, exit 0 | 203.8s | `546d6faf3545cf2c` |
| `seed:20260731` | 2,692 pass, exit 0 | 199.0s | `2b0624f1c8bba047` |
| `reverse` | 2,692 pass, exit 0 | 178.7s | `1694d285798347f9` |

At `55878c9` the same tree gave four different failure sets under four seeds.
The realised order was written to disk and fingerprinted for every run, so the
permutation used is evidence rather than a claim. The plugin lives outside the
repository, so the tree stayed clean at `fc197a6` throughout.

**Runtime: budgeted, not a hang.** ~3×, as `code-agent` predicted. Notably the
uniform global shuffle — which forces far more higher-scoped fixture rebuilding
— landed in a *narrower* band (178–204s) than the round-robin's reported
171–278s, so the widest interleaved times were not caused by interleave depth.

**`code-agent` corrected this agent's diagnosis, and the correction is right.**
This agent had named the control-event sink. It was not the cause.

1. **Cause A — the snapshot was function-scoped and taken too late — CONFIRMED,
   and the fixture it describes was located**:
   `test_f36_47_abstention_on_three_surfaces.py:86`, the only module-scoped
   fixture in the tree that *traverses* (the other six fetch one named screen).
   Confirmed by a throwaway probe reproducing the shape, run twice: it passes
   at `fc197a6` and **fails** with the setup-side restore removed, with its own
   negative control passing both ways. **Refinement worth recording**: the whole
   tree at `seed:1` still passes 2,692 with the setup-side half removed, so no
   current scenario falls inside the narrow window it protects. It is correct
   and justified insurance, not a currently failing case.
2. **Cause B — two session fixtures each bound a transport, last-one-wins —
   CONFIRMED** documentarily: at `55878c9` both `backend/tests/conftest.py:312`
   and `tests/suites/conftest.py:112` were `scope="session", autouse=True`, each
   built its own `BrokerStore`, and each called `pilot_transport.install(...)`.

**The AST guard is a classification — MUTATION-TESTED, twice.** An undeclared
`_TA_MUTATION_CACHE = {}` in `app.ui.state` and an undeclared
`_TA_LAZY_HOLDER = None` in `app.pilot_close` — the second being the shape every
real holder actually takes — each failed the guard, which named the binding, and
each also failed the guard's own negative control. Both mutations reverted; tree
verified clean at `fc197a6` after each.

**`AC-F36-29` asserts MORE — CONFIRMED. +3 assertions, −0.** Every prior
assertion is retained and it now produces its own action denial and emission
denial through the two real routes (previously it read the ledger as it found
it, so it was really asserting that the scenario before it had run first).

**The standing question — `does any suite report a pass the register says cannot
be true?` — returns NO for the FIFTH consecutive pass.** The register has 33
entries (1–33, verified, no gaps). `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`,
`AC-F40-17` and `AC-F36-48` are claimed by **zero** of the 2,692 scenario names
and by zero `COVERS` joins other than the two register-27-compliant `AC-F36-48`
strings, whose denial travels *inside* the join string.

**Test-count delta against `55878c9`: +28 added, 0 removed, 1 changed.** The +28
is accounted for exactly with no residue — 27 new test functions in two new
files (`test_pilot_process_state.py` 16 functions/17 node IDs,
`test_pilot_test_binding.py` 11), one parametrized over the two participating
modules. Zero removed `def test_`/`class Test` lines in the diff and zero
deleted test files. The one changed test is `AC-F36-29`, which gained
assertions. All six SME suite counts are unchanged.

**Findings for a human — neither is blocking, both are recorded.**

- **Carried: `ges_gateway._HTTP` restored by named snapshot.** `code-agent`
  named this as the next one that will bite, in "three function-scoped
  fixtures". Right about the fixtures, but the count is **six** sites — three
  fixtures (`swapped_transport`, `transport_without_an_attestation`,
  `poar_world`) and three inline `try/finally` blocks inside test bodies. All
  six are function-scoped and therefore correct today. Also noted: the AST
  guard classifies bindings *within* participating modules, but the **set of
  participating modules is itself an enumeration**, and `app.ges_gateway` —
  which holds `_HTTP` and `_CLIENTS` — is not in it.
- **NEW, found this run: the test suite writes into the developer's live
  decision ledger.** `tests/suites/functional/test_emission_gate_criteria.py`
  adds 3 rows per run to `dev/var/broker_db.sqlite3` (measured: 4,575 → 4,578;
  the file now holds 4,578 rows / 9.3 MB), because `tests/suites/conftest.py`'s
  `ges_http` calls `create_app(...)` with **no `broker_factory`** and falls
  through to `default_store_path()`. The warehouse is injected; the broker store
  is not. This contradicts the conftest docstrings' claim that "a run never
  writes into the developer's live decision ledger". **Not blocking** — nothing
  reads that store order-dependently and all six orderings are green — but it
  sits entirely *outside* the rebuild mechanism (neither tmp-pathed, nor rebuilt
  between scenarios, nor discarded by `restore()`), it accumulates across runs,
  and it is the same file `backend/pilot.py` uses. A fresh clone and this
  machine are therefore different starting states. Localised precisely: this is
  the only suite of six with a non-zero `var/` delta.
- **Carried advisory for `ui-ux-designer`, re-verified and unchanged:** minimum
  computed font size is **10.0px** on all four screens at both viewports.
  UX-4/`AC-F41-03` is a *relative* check and passes, and no rule sets an
  absolute minimum, so no suite fails.

**Rendered-UI verification: Playwright/Chromium against the SERVED pilot**, not
`set_content` over an in-process client. Four screens × two viewports = 8
captures, 8 clean: 200 everywhere, **zero green elements under computed colour**
(the gate-5 no-green rule, checked on what the browser resolved rather than on
authored CSS), **zero text nodes at `opacity: 0`**, and the gate-5 reading order
confirmed visually on Review — riskiest element first and largest, narrative
collapsed and last, no approve control. RNTL is not applicable: MVP1 is desktop
web only and there is no React Native surface, so two desktop viewports is
complete coverage rather than a partial pass.

**Gate status: PASS. No blocking suite failed and no blocking condition remains
open.** All seven suites plus the smoke are `EXECUTED` and green; the one
previously failing blocking condition was fixed rather than overridden, and was
verified here independently rather than accepted. No `[override]` is required.

---

### 2026-07-31 — Gate 8 · Test — `test-agent`, **re-run at `dev` @ `55878c9`** (parent repo @ `8697994`) — pass-13 verification

**All seven automated suites EXECUTED, exit code 0, 2,664 of 2,664 scenarios
passed, zero skipped. The post-deploy smoke is 14 of 14 — the previous run's one
FAIL is fixed.** Structured per-scenario evidence:
`test-evidence/*-2026-07-31.md`, plus eight Playwright screenshots. **The entire
superseded corpus was deleted and rewritten**; every file names both commits.

| Suite | Status | Exit | Scenarios | Pass | Fail | Skip | Owner | Blocking |
|---|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 2,000 | 2,000 | 0 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 354 | 354 | 0 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 26 | 26 | 0 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | 0 | `ui-ux-designer` | yes |
| **automated total** | | | **2,664** | **2,664** | **0** | **0** | | |
| post-deploy smoke | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. 2,000 + 664 = 2,664, which
is the headline figure. The `ux` suite launched Chromium — its conftest exits 4
(STATIC-ONLY) rather than passing if Playwright or the browser binary is absent,
so exit 0 is positive evidence a rendering engine answered. No server was started
inside this agent's turn; the pilot was started, driven and reaped inside single
command invocations five times, and 8021 was verified free after each.

**Test-count delta, re-derived rather than trusted.** `9d819c1` was checked out
into a worktree and collected there: 2,602, reconciling with the previous
headline. Node IDs were then diffed **set-wise**, not compared as totals.

| | Count |
|---|---|
| `9d819c1` | 2,602 |
| `55878c9` | 2,664 |
| added | **+62** |
| removed | **0** |
| changed | **0** |

Nothing was removed and nothing was silently replaced. All 62 additions sit in
five files, all of them pass-13 work: `test_export_integrity_contract.py` (+20),
`test_tier_selection.py` (+17), `test_warehouse_migration.py` (+13),
`test_ui_state_session.py` (+9), and three `ARCH_05` scenarios in the
architecture suite.

**The four loop-back items — verified, not accepted.** Full evidence in
`test-evidence/fix-verification-2026-07-31.md`.

1. **F1, the persisted warehouse — FIXED.** The original failing drive was
   re-run: the pilot as found, served on 8021, driven over stdlib HTTP through
   approve → override → export. It returns **200** with a retrievable file, where
   gate 8 got 403 `revalidation_could_not_run` / "no such column: period_status".
   A **negative control** proves the plant is fair: a warehouse carrying all
   three gap kinds still returns 403 at `9d819c1` and 200 at `55878c9`, from the
   same file. The third gap kind was also driven **in isolation** — a warehouse
   current in every other respect with `fx_revaluation` added — and the rebuild
   still fires, the object is removed, and `AC-F28-07`'s "not run" stays at
   exactly one. Repopulation was checked, not assumed: `suspense_residuals` comes
   back with 24 rows, not as an empty recreated table.
2. **F2, the viewer-session leak — FIXED.** `_restore_run_tier` exists only as a
   comment explaining its removal. The `ux` suite passes reversed and at three
   shuffle seeds; the whole tree passes reversed. **The AST guard was mutation-
   tested**: planting `self.last_persona_switch = key` in `PilotState.view_as`
   fails it, naming the attribute and the method that set it — and fails its own
   negative control too, which is what stops the guard passing on a scan that
   found nothing.
3. **F3, `export.build` — FIXED.** The exact gate-8 mutation (`integrity = {}`
   restored on both `Export.__init__` and `build()`) now kills **3 scenarios**
   where it previously survived all 2,602; and `Export(..., integrity={})` is
   refused at construction rather than producing a file naming neither criterion.
   Both **content** legs were mutated separately and both killed 2 scenarios
   each, so the contract is enforced on content and not on presence. Registers 3
   and 4 are unchanged and open.
4. **A2, the unknown run tier — FIXED.** Driven on the served pilot in both
   directions: 400 from certified and 400 from exploration, the current tier
   untouched either way, and the second route that takes the parameter refuses
   identically. Empty and wrong-case values are also refused. The docstring that
   contradicted the code is rewritten.

**The carried-forward disclosure is ACCURATE.** `code-agent` reports that an
interleaved shuffle of `backend/tests` with `tests/suites` is not order-clean and
that it predates pass 13. Verified independently: at `55878c9` seeds 1/7/42/20260731
give 2/1/1/0 failures; at `9d819c1`, from a worktree with its own confirmed
`2602 passed` baseline, the identical plugin and seeds give **4/2/3/0** with an
almost entirely disjoint failure set. It is a **known limitation, not a
regression**, and the cause is the wider class disclosed — the control-event
sink, accumulated dispositions and workflow records — not the viewer session.
The two trees are order-clean as whole blocks and fully reversed; they are not
order-clean interleaved, and the fixture isolation that would close that does not
exist.

**The standing question — `does any suite report a pass the register says cannot
be true?` — returns NO for the fourth consecutive pass.** The register has 33
entries (1–33, verified, no gaps). The five declared criteria `AC-F1-08`,
`AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48` are claimed by **zero** of
the 2,664 scenario names. Two node IDs now contain `AC-F1-11` and `AC-F1-08` as
**parametrize labels** —
`test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor-AC-F1-11]`
and `[retention-AC-F1-08]` — and both are on a scenario asserting the export is
**refused** unless it names the criterion it does not meet. That is the denial
stated at the strongest available place, not a claim; it is called out here
because a mechanical scan would flag it. All 47 textual occurrences across the
five are denials or assertions that the product's own disclosure names the
criterion as unmet.

**Two findings that are not suite failures but belong in front of a human.**

- **The previous run's evidence corpus was never written.** The Test Results
  entry below states the `f56ab9f` corpus was deleted and rewritten at
  `9d819c1`. It was not: all nine files on disk at the start of this run still
  read `Commit under test: dev @ f56ab9f · parent repo @ 8939ebb`. The narrative
  summary claimed per-scenario evidence that did not exist — which is precisely
  what the summary/source-of-record split exists to prevent. This run's corpus
  supersedes it; the nine stale files were deleted, not left beside.
- **Advisory, for `ui-ux-designer`:** rendered-UI capture at two viewports found
  the navigation computing to **10px** and the provenance strip — which is where
  `AC-F38-11`'s close-clock staleness lands — to **10.5–11.5px**, the smallest
  text on every screen. No criterion or `UX_KB` rule declares an absolute minimum
  type size (UX-4/`AC-F41-03` is a *relative* check), so no suite fails. Raised
  because the reader `AC-F38-11` exists for is somebody reading a figure years
  later. Screenshots in `test-evidence/`.

**Gate status: the interleaved-shuffle order dependence is a failing blocking
condition** — every suite is blocking under this project's Test Policy and no
advisory exception is recorded. It is disclosed, pre-existing and reproduced at
`9d819c1`, so the human's choice is between sending it back to `code-agent` for
fixture isolation and recording an `[override]` in the Decisions Log naming the
suite and the reason. Everything else on this gate is green.

### 2026-07-31 — Gate 8 · Test — `test-agent`, **re-run at `dev` @ `9d819c1`** (parent repo @ `331353a`) — SUPERSEDED

**All seven automated suites EXECUTED, exit code 0, 2,602 of 2,602 scenarios
passed, zero skipped.** The post-deploy smoke is **12 of 13**, with one FAIL.
Structured per-scenario evidence: `test-evidence/*-2026-07-31.md`. **The entire
`f56ab9f` corpus was deleted, not left beside this one** — it described a commit
at which the probe-injection programme, the close clock, POAR,
supersession-by-data, the export-time CUEC probe and the F39 resolver call site
did not exist. Exactly one date is present in `test-evidence/`, and every file
names both commits it describes.

| Suite | Status | Exit | Scenarios | Pass | Fail | Skip | Owner | Blocking |
|---|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 1,941 | 1,941 | 0 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 354 | 354 | 0 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 61 | 61 | 0 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | 0 | `ui-ux-designer` | yes |
| **automated total** | | | **2,602** | **2,602** | **0** | **0** | | |
| post-deploy smoke | `EXECUTED` | — | 13 | 12 | **1** | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. The per-suite counts
reconcile exactly against the full run: 1,941 + 661 = 2,602, the headline figure.
All seven ran under `dev/.venv/bin/python`; the `ux` suite launched Chromium and
asserted against a **real rendering engine**, every request fulfilled from the
in-process ASGI app. No server was started inside this agent's turn by any suite;
the pilot was started, exercised and stopped inside single command invocations
for the smoke, and port 8021 was verified clear at the end of each.

**Test-count delta.** Previous counts were **re-derived** by checking `f56ab9f`
out into a git worktree and collecting there, not trusted from the prior table —
they reconcile exactly at 2,223.

| Suite | Was (`f56ab9f`) | Now (`9d819c1`) | Added | Removed |
|---|---|---|---|---|
| unit/integration | 1,663 | 1,941 | +283 | **5** |
| functional | 268 | 354 | +87 | **1** |
| architecture | 23 | 23 | 0 | 0 |
| security | 14 | 14 | 0 | 0 |
| red-team | 46 | 61 | +15 | 0 |
| industry | 23 | 23 | 0 | 0 |
| ux | 186 | 186 | **+25** | **25** |
| **total** | **2,223** | **2,602** | **+410** | **31** |

**Thirty-one node IDs were removed, and the `ux` line is the one to read.** Its
total is unchanged at 186 while **25 were replaced** — exactly the shape a
pass/fail total hides. This is register 18's instructed rewrite and it is a
strengthening, verified by mutation rather than accepted on the commit message:
the removed set is the old UX-11 group that asserted *no probe marker exists*
and *the injected-probe count is zero*; the added set drives a **real injected
probe**. The other six removals are the close-clock absence scenarios that
register 6's closure made false (`test_the_staleness_leg_states_that_it_cannot_express_close_relative_staleness`,
`test_the_missing_batch_and_the_absent_close_clock_are_both_on_the_screen`,
`test_the_staleness_leg_declares_that_it_has_no_close_clock_to_measure_against`),
`test_the_probe_zeroes_are_labelled_as_no_probe_not_as_no_error` (superseded by
injection), `test_a_request_that_trips_neither_is_neither_refused_nor_answered`
(superseded by the resolver — that request now answers), and
`TestItReproducesWhatWasDisplayed::test_the_retention_expiry_is_stated`
(superseded by the register-4 adjacency requirement). Each removal is a
consequence of a ruling, not a coverage decision taken quietly.

**The eight scrutiny questions — answered, six by mutation testing.** Full
evidence in `test-evidence/register-cross-check-2026-07-31.md`.

1. **The A20 widened exposure holds up, and the map is load-bearing.** Three
   mutations, all killed. Widening the request matcher (adding `\bnegligible\b`)
   fails 2 scenarios including `assert 7 == 8` on the count; narrowing it
   (removing the `small|trivial ... to|enough` pattern) fails the one string it
   does catch; drifting the **emission** matcher (removing `in the noise`) fails
   the fixed battery of eight. `AC-REFUSAL-11` appears in **zero** of the 2,602
   scenario names; all nine textual mentions deny it. The bound is asserted as
   well as the widening — the answer carries rows and a coverage statement and
   none of `no adjustment`, `leave`, `immaterial`, `recommend`, with
   `figure is None`. **Confirmed on the served pilot**, not only under
   `TestClient`.
2. **`AC-F41-08` and `AC-F12-05` are now honestly claimed.** Planting a
   probe-only element carrying *no probe vocabulary* (`class_="qa-sample"`) is
   caught by the structural comparison and correctly missed by the vocabulary
   check — which is why the structural leg had to exist. **The "comparator is a
   fair one" scenario does what its name says**: breaking the probe's
   `allowed_resolution_types` fails *that* scenario first, at the intended line,
   rather than surfacing as an uninterpretable class-name diff. This is the
   criterion mis-evidenced twice; it is now a real comparison between two
   rendered items, with a non-vacuity guard asserted before any claim.
   `-05`'s first two clauses rest on a capture row written by disposing of a
   real probe through the real control, with **both** the correct and the
   incorrect outcome exercised plus a genuine-item control.
3. **Nothing claims what the open registers deny.** Register 32 is honoured
   precisely: the seed is used at one call site, the rate is drawn and discarded,
   the band claim rests on **50,000 draws** and a variance scenario, and **no
   scenario anywhere divides the pilot's probe count by its queue size**.
   Register 31's `counterparty_is_live_oracle_read: False` is on the record and
   on both refusal paths. Register 33's UNKNOWN-not-complete is asserted, and its
   positive leg is non-vacuous in the other direction (`declared > 0`,
   `row_count == 0`). Registers 6 and 25 having closed, `AC-F26-05` and
   `AC-F38-11` are now claimed — three and five scenarios — where previously no
   suite claimed either. Previous pass's advisory A1 is **closed**:
   `AC-F36-48`'s two joins now carry the denial inside the join string.
4. **`export.build`'s `integrity` has no default — and that is the only thing
   holding it.** Two findings. Restoring the default (`integrity = {}`) and
   running **all 2,602** scenarios produces **2,602 passed** — the mutation
   survives, so no executing scenario witnesses the no-default property and it
   can be regressed silently. And an export stating nothing about either residual
   **can** be constructed: `Export(..., integrity={})` builds cleanly and its
   JSON contains neither `AC-F1-11` nor `AC-F1-08`. Required is not validated.
   Mitigating: the **shipped** path is covered end to end over the served bytes,
   and the smoke confirms it on the pilot — so nothing is reporting a false pass
   today. Advisory, for `code-agent`.
5. **`synthetic_attestation` does not collapse into `no_drift`.** Setting them
   equal fails **4 scenarios across two suites**, and the one that fires first is
   named exactly for the property
   (`test_a_synthetic_attestation_is_not_reported_as_no_drift`).
6. **The standing question finds no contradiction — third consecutive pass.**
   `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17` and `AC-F36-48` appear in
   **zero** of the 2,602 scenario names, and every textual mention is a denial.
7. **The tier restore is real — and a second leak of the same class is being
   relied on. See FINDING F2.**
8. **No empty `parametrize` and no vacuous pass among the newly-claimed IDs.**
   **104** parametrised functions (up from 92), zero contributing no node ID. Of
   the 341 newly-added scenarios mapped onto the 36 IDs they claim, exactly one
   ID came back evidenced only by negative assertions — `AC-F36-18` — and it is a
   cross-reference in another scenario's docstring, not a claim. The
   absence-shaped criteria that surfaced (`AC-F12-13`/`-14`/`-15`/`-17`) are
   criteria that *ask* for absence, and each is non-vacuous now that a probe
   exists to leak.

**FINDING F1 — the smoke test FAILED on the pilot as found, and no suite could
have seen it.** Driving the real export path over HTTP against the pilot's
persisted warehouse returned **403**, `data-reason="revalidation_could_not_run"`,
visible reason *"the point-of-action revalidation could not run (no such column:
period_status), so no file is produced"*. `ges/warehouse.py` declares
`erp_control_extract.period_status`, `latest_journal_ts` and `extract_as_of`;
`dev/var/warehouse.sqlite3` (mtime 19:08, before register 31's POAR work) had
none of them, and `seed()` uses `CREATE TABLE IF NOT EXISTS`, so **a persisted
warehouse is never migrated**. Every suite builds a fresh `tmp_path` warehouse
and is structurally blind to it. Diagnosis confirmed by deleting the file and
re-running the identical drive: `export http=200` with all four `AC-F40-18`
disclosures present. The regenerated warehouse was left in place so the pilot is
operable. **The fail-closed behaviour itself is correct** —
`revalidation_could_not_run` is one of register 31's four real refusals and it
did stop a file existing. The finding is the missing migration path, and that no
suite can witness it. For `deploy-agent`.

**FINDING F2 — a second cross-scenario state leak, the same class as the run
tier, and it is currently masked by collection order.** Every suite was run with
collection order **reversed**; `ux` was additionally run under two shuffle seeds.
The 1,941-scenario unit/integration suite and five of the six SME suites are
**order-clean**. The `ux` suite fails in all three permutations, always the same
scenario:

```
FAILED tests/suites/ux/test_ux_journey.py::TestTheActionPathJourney::
       test_a_staff_accountant_approving_is_denied_by_the_broker_and_records_nothing
E       AssertionError: assert 'approval_value_above_ceiling' == 'not_in_capability_allowlist'
```

Reproduced **minimally in two scenarios**.
`TestUX14ControllerNightOverMonitors._as_controller` POSTs `/pilot/viewing-as` to
become the controller and **never restores the persona**, which is process state
shared across `page` fixtures. In file order the staff-accountant class runs
first, so the leak is masked — the identical accident `_restore_run_tier`'s own
docstring describes, in the adjacent piece of state. **Why it matters beyond
ordering**: run as a controller the scenario still passes three of its four
assertions — the approval is still refused, `data-kind` is still `refused` — and
only the *reason* differs. A scenario named "a staff accountant approving is
denied" would have been silently establishing something about a controller. For
`code-agent`: an autouse persona-restore fixture beside `_restore_run_tier`.

**FINDING F3 — the headline "2,602, up from 2,223" is like-for-like, and the
`ux` line inside it is not.** The totals are both full runs and the +379 net is
real. But `ux` reads 186 → 186 with 25 scenarios replaced, and the 21 built
criteria are carried by unit/integration (+283) and functional (+87) rather than
by the browser suite. Recorded so a flat `ux` line is not read as "the rendered
surface did not change" — it changed more than any other suite this pass.

### Advisories from this pass — none stops the gate

| # | Advisory | For |
|---|---|---|
| A5 | **`export.build`'s no-default is unwitnessed** (scrutiny 4). Restoring the default passes all 2,602. Add a signature scenario, and validate rather than merely require — `integrity={}` constructs an export naming neither residual. | `code-agent` |
| A6 | **The persona leak** (FINDING F2). An autouse restore fixture. | `code-agent` |
| A7 | **The pilot warehouse has no migration path** (FINDING F1). `CREATE TABLE IF NOT EXISTS` over a persisted `var/warehouse.sqlite3`. | `deploy-agent` |
| A2 | **Still open from the previous pass, and now measured.** `state.select_tier`'s first docstring line ("An unknown value falls back to CERTIFIED") is wrong: the method ignores unknown values entirely, so a typo leaves the **current** tier. From a fresh process a typo yields `certified` (safe); after `?tier=exploration`, a typo yields `exploration`. The second paragraph of the same docstring is correct. Behaviour is safe on first use and sticky thereafter. | `code-agent` |
| A3 | **Still open.** `test_every_finding_carries_the_uncalibrated_threshold_denial` asserts over one finding, not every finding. | `code-agent` |
| A4 | **Still open.** `test_a_dossier_round_trips_complete`'s version assertion is self-satisfying in isolation. | `code-agent` |
| A1 | **CLOSED.** `AC-F36-48`'s two joins now read `COVERS ONLY THE COMPUTATION CLAUSE OF AC-F36-48, WHICH IS ITSELF DENIED` — the denial is inside the join string, so a by-ID mapper cannot score it satisfied. | closed |

**Process-lifecycle deviation, recorded rather than smoothed over — second
consecutive pass.** `kill <pid>` (SIGTERM) did **not** reap the uvicorn listener
on three of five pilot invocations. The post-stop `lsof` assertion caught it each
time and the survivor was force-killed by port. Final state verified: nothing
listening on 8021, nothing left running past this turn.

**No automated suite failed. The post-deploy smoke — a blocking suite — recorded
one FAIL (FINDING F1), so this gate stops for human decision.** The failure is a
deployment-data defect with correct fail-closed behaviour behind it, and it has
been diagnosed and remediated in place; the human may reasonably override with a
recorded reason, or send A7 to `deploy-agent` first. F2 does not fail a suite as
executed but is the same defect class the `ux` suite exists to catch.

### Prior pass — retained as history

### 2026-07-31 — Gate 8 · Test — `test-agent`, **re-run at `dev` @ `f56ab9f`** (parent repo @ `8939ebb`)

**Every suite EXECUTED. Every suite green. Exit code 0 across the board.**
Structured per-scenario evidence: `test-evidence/*-2026-07-31.md`. **The entire
`b1b5dde` corpus was overwritten and deleted, not left beside this one** — it
described a commit at which `decide_emission`, the F2 version registry, the F42
journal leg and the dossier v2 schema did not exist. Exactly one date is present
in `test-evidence/`, and every file names the commit it describes.

| Suite | Status | Exit | Scenarios | Pass | Fail | Owner | Blocking |
|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 1,663 | 1,663 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 268 | 268 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 23 | 23 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 46 | 46 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | `ui-ux-designer` | yes |
| post-deploy smoke | `EXECUTED` | 0 | 11 | 11 | 0 | `test-agent` | yes |

**2,223 automated scenarios executed, 2,223 passed, 0 failed, 0 skipped**, plus
11 smoke scenarios. No suite is `STATIC ONLY` and no suite is `PARTIAL`. The
per-suite counts reconcile exactly against the full run: 1,663 + 560 = 2,223.
All eight ran under `dev/.venv/bin/python`; the `ux` suite launched Chromium and
asserted against a **real rendering engine**, every request fulfilled from the
in-process ASGI app, no server started inside the agent's turn.

**Test-count delta.** The previous counts were **re-derived** by checking out
`b1b5dde` into a git worktree and collecting there, not trusted from the table
above — they reconcile exactly.

| Suite | Was (`b1b5dde`) | Now (`f56ab9f`) | Added | Removed | Changed body |
|---|---|---|---|---|---|
| unit/integration | 1,428 | 1,663 | +235 | **0** | 24 |
| functional | 96 | 268 | +172 | **0** | 5 |
| architecture | 23 | 23 | 0 | **0** | 1 |
| security | 14 | 14 | 0 | **0** | 0 |
| red-team | 46 | 46 | 0 | **0** | 2 |
| industry | 23 | 23 | 0 | **0** | 0 |
| ux | 186 | 186 | 0 | **0** | 1 |
| **total** | **1,816** | **2,223** | **+407** | **0** | **35** |

**Zero test functions were removed this pass** — the first pass at which that is
true. 324 new unique function names; 35 changed bodies, **none with a net loss
of assertions** (three gained one).

**FINDING F1 — the headline "2,223, up from 1,428" is not like-for-like.**
1,428 was the *unit/integration suite alone* at `b1b5dde`; the full run there was
**1,816**. 2,223 is the *full run* now. The like-for-like figures are
unit/integration **1,428 → 1,663 (+235)** and total **1,816 → 2,223 (+407)**.
The growth is real either way; recorded so a +795 headline does not compound.

**The seven scrutiny questions — all answered, four by mutation testing.** Full
evidence in `test-evidence/register-cross-check-2026-07-31.md`.

1. **`AC-F2-08`'s 34 broken tests were strengthened, not routed around.** The
   control has no bypass parameter. Disabling `check_closure_input` fails **21
   tests**, so it is load-bearing. The shared fixture builds a stamp through the
   real `versions.stamp_for` with the **fetched** bundle hash, and each adopting
   scenario "supplies the first layer's input and withholds only what it is
   testing". An AST assertion-count diff over all 35 changed tests found **zero
   with a net loss**.
2. **The undeclared-primitive guard fires.** It is a set **equality**, not a
   subset — planting a registered-but-undeclared primitive **killed the
   mutation** and named the intruder. `obligation_gap` and
   `journal_attribute_outlier` are properly declared.
3. **`_read_v1` is genuinely exercised and no v1 record reports incomplete.**
   v1's required-key list is untouched at 11 keys and is a strict subset of v2's
   12. A genuine v1 record round-trips. Dropping the v1 reader **fails 2 tests**.
4. **Both rewritten tests assert something real.**
   `test_the_full_population_conclusion_uses_a_universal_quantifier` went from
   one substring to a proportion **and** a count (1→2 assertions);
   `test_a_dossier_round_trips_complete` widened from 11 keys to 12 and shed a
   false `AC-F1-08` claim.
5. **Registers 29 and 30 are honoured.** The uncalibrated-threshold denial is
   written into every emitted `journal_attribute_outlier` finding, and a sweep
   for any assertion claiming a measured likelihood, precision or false-positive
   rate returned **nothing**. Register 29's no-metric-store denial is in
   `SemanticElement` and a missing `semantics` key is a compile error.
6. **The standing question finds no contradiction** — second consecutive pass.
   All nine denied criteria (`AC-F1-08`, `-F1-11`, `-F38-11`, `-F26-05`,
   `-F41-08`, `-REFUSAL-11`, `-F40-17`, `-F40-18`, `-F36-48`) appear in **zero**
   of the 2,223 test function names.
7. **No empty-`parametrize` instances remain.** All **92** parametrised
   functions contribute at least one node ID.

**Post-deploy smoke test — PASS, 11 of 11.** **The pilot binds 8021, not 8000**;
the foreign process on 8000 answered **200** this run (it answered 404 last run)
— either way nothing here was collected from it. All twelve screens served 200;
`/dossier/…` carried **zero** external references on all eight constructs;
`AC-F28-07`'s `not_run` state and register 6's `close_clock_absent` note both
render on the served `/exceptions`. **The Ask box's GET query string now reaches
the render** — `?tier=certified` serves 22,644 bytes and `?tier=exploration`
24,432 — and no typo value can enter exploration. `POST /ask` on one of register
9's known-unrefused paraphrases returned 200 with `Ask - not resolvable in this
release`.

**Process-lifecycle deviation, recorded rather than smoothed over.** On the
second smoke invocation `kill $PID` did **not** reap the server; the uvicorn
listener (pid 63637) survived and was still holding 8021 when the invocation
returned. The **post-stop `lsof` assertion caught it**, and it was force-killed
by port in the next command. Final state verified: nothing listening on 8021,
nothing left running past the turn.

**No blocking suite failed. The gate is not stopped by a suite failure.**

### Advisories from this pass — none stops the gate

| # | Advisory | For |
|---|---|---|
| A1 | **`AC-F36-48` is the only denied criterion still carrying `COVERS` joins** (two). Both are correctly narrowed to a named clause under a register-27 header, so the prose is honest — but the bare ID is in the join string, and gate 9 maps joins by ID. Same shape as gate 8's `AC-F36-47` finding. Put the denial *inside* the join string. | `code-agent` |
| A2 | `state.select_tier`'s docstring first line ("An unknown value falls back to CERTIFIED") contradicts both the code and its own next paragraph. Behaviour is safe; the line is wrong. | `code-agent` |
| A3 | `test_every_finding_carries_the_uncalibrated_threshold_denial` asserts over one finding, not every finding. The module structure guarantees the property; the name promises a universal the test does not quantify over. | `code-agent` |
| A4 | `test_a_dossier_round_trips_complete`'s version assertion is now self-satisfying in isolation (covered by two sibling tests). | `code-agent` |
| D1 | **Date discrepancy — RULED AND CLOSED at pass 10.** The corpus was dated `2026-08-01` while the system clock and **every commit date in `dev/`** read `2026-07-31`. Ruled `2026-07-31` (see the corpus date ruling below). The nine `test-evidence/*.md` headers and the two references in this file that still read `2026-08-01` now read `2026-07-31`; header, filename and commit date agree. | closed — `code-agent`, pass 10 |

### Prior pass (`b1b5dde`) — two advisory findings, both since addressed

Neither is a false pass, and neither stops the gate on its own. Both are the
shape pass 4d and pass 5 installed guards against elsewhere, in the two places
that did not get one.

1. **Register 24 has no witness (F33 peer thresholds).** The register says
   `0.6667` is a property of a 163-posting synthetic fixture, not a measured
   skill accuracy, and that `min_peer_support=20` / `min_peer_agreement=0.8` are
   uncalibrated. The functional suite asserts `record.precision == "0.6667"` and
   `"0.6667" in region` with **no statement anywhere** that the figure is a
   fixture property, and `test_AC_F33_01_…` asserts `comparable_postings >= 20`
   — the uncalibrated threshold — as a criterion check. Registers 6, 9, 18 and
   20 each carry an explicit in-file denial; register 24 does not. Mitigating:
   the `backtest-no-claim` panel for the unlabelled held-out period **is**
   asserted and **was confirmed on the served pilot screen**, which is the
   contrast the register says the screen exists to create.
2. **Register 25 has no witness (F9 history).** Three `test_AC_F9_05_*`
   scenarios claim the ID; none states that "periods present in the movements
   extract" substitutes for "periods of history", so a dormant account reads as
   younger than it is. Weaker than (1): `AC-F9-05` as written **is** satisfied
   on this fixture, and register 25 itself says the two cases cannot differ
   here.

**Both addressed at pass 6 (2026-08-01), neither closed.** Each register now
carries an in-file denial at every site that touches its number — register 24
at five sites, with `0.6667` and `0.5000` derived from the fixture constants
and the peer threshold read from the manifest; register 25 at five sites. The
registers themselves stay open: nothing was calibrated and no close calendar
exists.

### Prior pass (`b1b5dde`) — one over-broad `COVERS` join, since resolved

*Retained as history. The equivalent finding at `f56ab9f` is advisory A1
(`AC-F36-48`), recorded in the table above.*

Thirteen of the 45 new joins were read in full against `FUNCTIONAL_SPEC`.
**Twelve are accurate** — `AC-F36-34` (4), `AC-F36-37` (4) and `AC-REFUSAL-08`
(3) each decompose their criterion into clauses plus a negative control plus a
boundary, which is better than a restatement. **One is over-broad:**

- **`AC-F36-47` (3 joins).** The criterion requires the property "*on every
  screen, in every dossier and in every export*". All three joined scenarios
  test `common.abstention` alone — `quality_denominator`, `rates`, and an AST
  reflection over that one module. No screen, dossier or export scenario in any
  suite reads an automation-rate or precision figure with its abstention count
  beside it. **Gate 9 maps these joins mechanically, so this one would score
  `AC-F36-47` satisfied on evidence covering half of it.** For `code-agent`:
  either add the surface leg or narrow the join to name the clause it covers.

  **Pass 6 (2026-08-01) did both, because two clauses were in two different
  states.** The three computation joins are narrowed to name their clause. The
  surface clause was genuinely unmet — every surface dropped the `abstained`
  key its payload carried — so the count is now rendered beside the precision
  figure on `/readiness` and in every dossier, and
  `backend/tests/test_f36_47_abstention_on_three_surfaces.py` asserts screen,
  six dossiers, export-through-a-file, an every-reachable-screen sweep and a
  negative control on the forbidden denominators. **The criterion's
  automation-rate half remains unevidenced by absence** and is named as such in
  a scenario that must fail when an automation rate is built.

**On registers 3 and 4:** unchanged and still open. No suite claims `AC-F1-11`;
`test_ARCH_11_anchors_record_that_the_signer_is_a_stub` asserts the negative and
is named for it.

**On register 19:** `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
and its companion both **PASSED, not skipped** — verified from the `-v` node
list, so the real child process really bound and the loopback really carried a
broker decision. The residual the register names (no suite can witness that an
api-process module cannot `import ges.executor`) is untouched by that and stays
open for `solution-architect`.

## Deferred-substitution register — opened 2026-07-31 at gate 7 pass 1

Places where the build could not match `ARCHITECTURE_KB` as written.
`code-agent` disclosed every one rather than letting it pass. **None may be
closed by a later gate without either being built or being granted an explicit
human exception.** Gate 9 audits against this table, not against the commit
messages.

**Twenty-two entries as of pass 4. Entries 8, 10, 13, 14 and 16 are CLOSED.
Entries 1–5, 7 and 9 stand exactly as recorded at pass 1 and 2c; entries 3 and 4
are still the two that cannot quietly become "MVP1 ready".** The section below
runs in pass order: the pass-1 eight, then the pass-2c additions, then what each
later pass closed, narrowed or opened.

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 1 | §8.1 mTLS on loopback | shared client token + 127.0.0.1 bind | weaker; must be reversed before any non-single-host deployment |
| 2 | §9.1 Postgres role, no `UPDATE`/`DELETE` grant | SQLite `BEFORE UPDATE`/`BEFORE DELETE` triggers | bypassable by `DROP TRIGGER`; **a row trigger does not fire for a statement matching zero rows** — a grant refuses it regardless. §23.4's `SERIALIZABLE` transaction has no SQLite equivalent and is not built |
| 3 | §9.2 KMS-signed Ed25519 anchors | labelled digest | **`AC-F1-11` NOT satisfied** — chain recomputation by an attacker is undetected. Key rotation across seven years unsolved (`SECURITY_KB` §4.5) |
| 4 | §9.3 Object-Lock compliance-mode archive | `has_retention_lock = False` | **seven-year immutability obligation NOT met** |
| 5 | `SECURITY_KB` §2.4 per-skill database grants | none | the independent second layer below the application does not exist |
| 6 | §5.3 `CloseClock` | none | **`AC-F38-11` unmet** — figures carry dataset/registry provenance but no close-clock staleness |
| 7 | §6.1 `sql_file` against an Oracle-sourced warehouse | SQLite | statements real and bound-parameter-only, but **dialect fidelity untested** |
| 8 | §9.4 server-rendered evidential region | none (no UI) | `AC-F41-04` and gate 5's strengthened `AC-F41-03` untestable today |

**Items 3 and 4 are the ones that cannot quietly become "MVP1 ready."** They are
the evidentiary guarantees the product's compliance story rests on, and a
labelled digest with `has_retention_lock = False` reads as satisfying them to
anyone who does not open this table. They are prototype stubs with the interface
real and the stub visible — which was the instruction — but the obligation is
open, not discharged.

**One declared exception to "no function anywhere accepts SQL text"**, enforced
by a reflective test across `app/`, `ges/` and `common/`: `SqliteWarehouse.fetch`,
the driver boundary, which receives the committed statement from the compiled
registry and from nowhere else.

**~~No reachability tests exist because no UI component exists.~~** **CLOSED at
pass 3.** Every screen is rendered through `TestClient(app)` against the object
`backend/app/run.py` serves, and `reachable_urls()` walks from `/` following
real links to eighteen URLs. Two tests then assert that every GET route the app
serves is in that set and that all 36 `data-testid`s the component library
declares are rendered somewhere in it — a component defined, imported and
mounted nowhere fails the second. The `ux` suite reports green on 148 executing
browser scenarios.

**Extended at pass 4.** The traversal now also **drives the controls** —
resolve, refuse, reject, approve, override, export — because link-following
cannot reach a screen that only exists as the result of an action, and a
component that appears only after a POST would otherwise have been "mounted
nowhere" with nothing failing. A companion test asserts those six components are
NOT reachable by navigation, so the driving traversal cannot be deleted without
something failing. The `ux` suite is now **186 browser scenarios** and all six
suites execute.

### Register entries added at pass 2c

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 9 | `RESPONSIBLE_AI_KB` §4.1 — A20 enforced on the speech act, "not by a keyword list" | a **structural leg** over fields (absolute for any emission carrying a disposition on a size-shaped ground) plus a **prose leg** that is a shape matcher over English | the prose leg **is evadable and a test demonstrates a paraphrase that evades it**. A20 holds absolutely where a disposition carries a size-shaped ground, and heuristically in free prose. **Updated at pass 4d with the evasion's exact shape**, found by probing the broker at gate 8: `text` = prose the shape matcher does not recognise, `claim_type="treatment"` (a disposition IS made), `treatment_ground_kind="offsetting_entry_identified"` (a *substantiated* ground, so the structural leg — which fires only on size-shaped grounds — never reaches it) → `outcome="allow"`, `reason=None`. Change that one field to `"magnitude"` and it abstains. This is now a **red-team scenario asserting the pass-through**, `test_RT05_this_paraphrase_evades_A20_entirely_and_reaches_a_surface`, not only a unit test. Closing this needs the F39 NL surface plus a model call site, neither of which exists; it is explicitly **not** closed by extending the shape matcher (§4.1 rules that out as an arms race against paraphrase) |
| 10 | `AC-F35-11` — auto-disposed finding visible on the Exceptions screen, dossier reachable | `Outcome.as_exception_row()`, carrying the marker, the disposing rule and the bundle hash | **`AC-F35-11` NOT satisfied** — observable-UI, no UI |
| 11 | `AC-F12-20`'s "read on screen, in a dossier and in an export" | one renderer, three surfaces, label source in the same payload | the *renderers* are built and tested; **no screen and no export file exists to read them on** |
| 12 | `AC-F12-19` — retrospective abstention-warranted labels | nothing | **not built.** The store now distinguishes `abstain` from `deny`, so the read this criterion needs is possible; the label itself is not written |

**No register entry was closed at pass 2c.** Entries 1–8 stand exactly as
recorded at pass 1. In particular, entry 2's residual is *narrowed but not
closed*: the two new SQLite stores added here (`policy_cold`, `disposition`)
use the same `BEGIN IMMEDIATE` single-writer mechanism, so they inherit both
its guarantee and its one-host bound.

### Entries CLOSED at pass 3

| # | Was | Now |
|---|---|---|
| 8 | §9.4 server-rendered evidential region — none (no UI); `AC-F41-04` and gate 5's strengthened `AC-F41-03` untestable | **BUILT.** `/dossier/{id}` renders shell-off, style-inlined, with no `<link>`, `<img>`, `<script>`, `@import`, `url()` or `srcset` and no outbound link — it opens from a file, offline. `AC-F41-03`'s strengthened clause is checked in a real browser: the riskiest figure computes to 42px and no other element on the screen reaches it (next largest, 22px) |
| 10 | `AC-F35-11` — auto-disposed finding visible on Exceptions, dossier reachable — NOT satisfied, no UI | **SATISFIED.** The row is visible in the queue, marked auto-disposed, names the disposing rule and the bundle hash, and links to a dossier the test follows. A separate test asserts the rule in the row is the rule `policy_cold.evaluate` actually fired |

### Entries NARROWED but not closed at pass 3

| # | Residual after pass 3 |
|---|---|
| 6 | `CloseClock` still absent. The screens render a `close_day` label carried on the run's binding, not a figure computed against a close calendar. **`AC-F38-11` remains unmet** and `chrome.provenance()` says so at the site |
| 11 | `AC-F12-20`'s "on screen, in a dossier and in an export": the **screen leg now exists** and is tested. The precision figure is not rendered in the dossier and **no export file exists**, so two of the three surfaces are still unread |

### Entries OPENED at pass 3

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 13 | The UI as a client of the broker over the trust boundary | broker facts (decision ID, bundle hash, threshold, approval eligibility) **carried on the item** as a payload in the shape the broker emits | there is **no `/ges/decide` HTTP route**, so no screen fetches a decision. Two AST-level tests prove `app/ui/` imports nothing from `ges` and compares no approver against an author or invoker — the UI provably does not *compute* these — but in this build `app/ui/state.py` *supplies* them. The display is faithful; the fetch does not happen |
| 14 | The write path — record a resolution, submit a structured rejection, approve for export | **501, in the deferred grammar, naming what is missing** | **`AC-F35-01`…`-08` persistence, `AC-F41-11` (approval-persist failure), `AC-F41-06`'s server-side "does not complete", `AC-F40-03`, `AC-F32-01`'s save failure and `AC-F12-01`…`-03` capture are NOT satisfied.** The controls exist and are real; nothing behind them records |
| 15 | Screens fed by a run from `run_harness` against GES | an in-memory **pilot close** (`app/ui/state.py`) over the synthetic fixture | coverage, the conclusion type, the resolution model, auto-disposal, the abstention and the precision/readiness objects are all produced by the **real** modules; the findings themselves are fixture literals. Every screen carries a non-dismissable **pilot strip** saying so in words |
| 16 | The nine screens of `FUNCTIONAL_SPEC` §23 | six built (Ask, Exceptions, Review, Dossier, Proposal, Readiness); **Monitors, Dispositions, Catalogue, Inventory, Audit and Refusals are not built** | **UNMET: `AC-F41-07`, `AC-F41-19`, `AC-F12-10`, `AC-F36-19`, `AC-F32-09`, `AC-F32-10`, `AC-F38-01`, `AC-F38-12`, `AC-F38-13`, `AC-F38-16`, `AC-F5-07`, `AC-F1-09`, `AC-F2-07`, `AC-REFUSAL-01`, `AC-REFUSAL-13`.** The navigation deliberately lists only built screens: a dead nav link in an evidence product reads as a missing control rather than as unbuilt work |
| 17 | The gate-5 approved palette, pixel for pixel | four tokens changed | dark `risk-1`/`risk-2` (luminance ordinal), light `risk-1-bg` (AA by 0.004), light `ink-3` (AA on `surface-2`/`-3`), dark `.btn.primary` label. Each implements `UX_KB` §3.2's stated intent, but they are changes to an approved design and `ui-ux-designer` should confirm them |
| 18 | `AC-F41-08` — a probe indistinguishable from a genuine proposal before disposition | UX-11 asserts **no probe marker exists anywhere in the DOM** | **necessary, not sufficient.** The F12 probe-injection programme is not built, so there is no probe in any queue to be indistinguishable from one. The scenario must be rewritten against a real probe when injection lands; the test and the suite README both say so |

### Entries CLOSED at pass 4

| # | Was | Now |
|---|---|---|
| 13 | The UI as a client of the broker — no `/ges/decide` route, so broker facts were *carried on the item* and displayed, never fetched | **CLOSED.** `POST /ges/decide` exists and every terminal control on the surface goes through it: the approval, the override, and — via `/ges/run/precheck` and `POST /ges/export/journal` — the run precondition and the export. The two AST-level tests still hold (`app/ui/` imports nothing from `ges`, and compares no approver against an author or invoker), so the UI still provably does not *compute* any of it; it now *obtains* it. **One thing is deliberately still carried**: the pre-flight eligibility hint `AC-F41-20` requires at queue entry, because asking the broker to decide an approval nobody requested would write a decision record for a non-event (`AC-F36-06`). That is correct rather than residual, and the screen says the hint is advisory |
| 14 | The write path — 501 in the deferred grammar on every endpoint | **CLOSED.** `AC-F35-01`…`-08` persistence, `AC-F41-11`, `AC-F41-06`'s server-side refusal, `AC-F40-03`, `AC-F32-01`'s save failure and `AC-F12-01`…`-03` capture are all satisfied and tested against the STORE rather than the confirmation message. `AC-F32-01` is enforced by a NOT NULL column checked inside the transaction; every scenario posts directly with no browser, including exactly what a user who deleted the `required` attribute would post, and `close_item` has no `force`/`skip_validation`/`admin` parameter so "at every permission level" holds because there is nothing to send |
| 16 | Six of the nine screens not built; fifteen observable-UI criteria unmet | **CLOSED.** Dispositions, Catalogue, Monitors, Inventory, Audit and Refusals are built, in the navigation, and each of the fifteen criteria is asserted on the screen it names, in the state it names, reached from the entry point |

### Entries NARROWED but not closed at pass 4

| # | Residual after pass 4 |
|---|---|
| 6 | `CloseClock` still absent. **`AC-F38-11` remains unmet** and `chrome.provenance()` still says so at the site |
| 11 | `AC-F12-20`'s three surfaces: the **screen** leg (pass 3) and the **export** leg now exist — an export file is produced and its content hash is recorded. The precision figure itself is still not rendered *inside a dossier*, so one of the three surfaces remains unread |
| 15 | The findings are still fixture literals and every screen still carries the pilot strip. What changed is that the **actions** are no longer simulated: the approvals, denials, overrides, dispositions and export in this build are real records produced by the real components |
| 18 | Unchanged in substance and **strengthened in evidence**: UX-11 now checks structural markers across all sixteen screens, asserts that the capture schema carries `is_probe`/`probe_response_correct` while **no module on the render path reads either**, and asserts the injected-probe count really is zero — so a green UX-11 cannot be misread as a discharged `AC-F41-08`, and that last scenario fails the moment injection lands |

### Entries OPENED at pass 4

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 19 | `ARCHITECTURE_KB` §3.2 — the trust boundary is a PROCESS boundary | **two transports.** `loopback` (stdlib HTTP to the GES port) is the default and the deployment configuration. `in-process`, installed only by `backend/pilot_transport.py`, puts the broker inside the api process so the pilot is operable from one command and the `ux` suite can drive a real approval without a server it is forbidden to start | **With the pilot transport running the boundary is a module boundary**: a prompt-injected tool in the api process could reach `ges.executor` by `import` alone. It is refused under `CONCLAVE_ENV=production`, it is one named file outside the `app` package, and the interface cannot tell the two transports apart — but **nothing in the `ux` suite exercises the loopback transport**, and `backend/pilot.py` is a configuration a reader could mistake for the deployment. Both say so in their own first paragraph. **NARROWED, NOT CLOSED, at pass 4d.** Gate 8 established that the architecture suite's only boundary check (a static regex over `backend/app/`) and the security suite's three subprocess scenarios (which test the *credential* boundary, and which `pilot_transport` never triggers because it deliberately does not set `CONCLAVE_PROCESS_ROLE`) **would both have passed with the boundary gone entirely**. The deployment topology now has one executing witness: `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket` starts `ges/run.py` as a real child process on an ephemeral port, asserts it is a different pid holding the credential while the test process (role `api`) is refused that credential, and drives a real broker decision through `LoopbackHttp` — stdlib HTTP over a TCP socket, no `TestClient` — plus a companion asserting an untokened caller gets 401 across that socket. The fixture reaps the child in a `finally` and **fails loudly rather than skipping** if GES does not bind. **THE RESIDUAL THAT KEEPS THIS OPEN:** no suite can witness that an api-process module cannot `import ges.executor`, because a suite runs in one interpreter with both packages on one `sys.path`. That property is still held only by the static check and by the fact that a deployed api process does not have the `ges` package on disk. For `solution-architect` at gate 10 |
| 20 | `ARCHITECTURE_KB` §3.1 — Journal Import files in an object store | the produced file is held **in memory** for the life of the api process; the workflow store records its group id, content hash and line count | the artefact's *record* survives a restart; **the bytes do not**. A file downloaded before a restart and one downloaded after are not both available, and `AC-F1-08`'s oldest-end retrieval has no object store to retrieve from. **Pass 4d:** the functional suite no longer names `AC-F1-08` anywhere — the scenario that did was rescoped to `test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp`, whose docstring states the criterion is unsatisfied and why. **`AC-F1-08` is now covered by no suite**, which is the accurate reading |
| 21 | `AC-F40-05`'s CUEC verification against a real Oracle tenant | an in-memory register whose default state is `never_verified` for every item, verified by `pilot.py` with a synthetic attestation | the **refusal** is real and tested (a fresh register exports nothing, and `expired` and `failed` are distinguished from `never_verified`); the **verification** in this build attests nothing, because there is no tenant to read. `deploy-agent` owns the real one |
| 22 | `AC-F12-19`'s label set as the input to an accuracy claim | the label is written at disposition time and rendered on Monitors as counts | the labels are real, but the pilot has **one abstained item**, so the label set is too small to compute anything from. This is a data-volume bound, not a build gap, and it is stated because a screen showing "1 warranted" invites a conclusion the sample cannot support |


### Entries CLOSED at pass 5 (the gate-9 loop-back)

| # | Was | Now |
|---|---|---|
| 11 | `AC-F12-20`'s three surfaces: the screen leg (pass 3) and the export leg (pass 4) existed; the precision figure was still not rendered **inside a dossier**, so one of the three surfaces was unread while the ID was reported satisfied — which gate 9 called a contradiction | **CLOSED.** `components.precision_figure_in_dossier` renders on `/dossier/{id}` from the same `PrecisionFigure.render()` the screen and the export read, with `surface` as its only difference. Twelve scenarios cover all three surfaces, including one asserting the dossier still carries no `<script>`, `<link>`, `<img>`, `@import`, `url()` or `srcset` after the addition — an exhibit that gained a stylesheet link would stop opening from a file, offline, in seven years |

### Entries NARROWED but not closed at pass 5

| # | Residual after pass 5 |
|---|---|
| 6 | `CloseClock` still absent, and it is now the reason **two** criteria are unmet rather than one. `AC-F38-11` stands as before. `AC-F26-05` joins it: the `freshness` primitive emits an explicit `close_clock_absent` note on **every** run naming the unmet criterion and this register entry, the run summary reports `close_clock_available = False`, and the Exceptions screen renders the note. An absolute refresh timestamp under a close-relative name would satisfy a reader while failing the criterion, so none is produced. **No suite claims `AC-F26-05`** |
| 9 | Unchanged in substance and **materially strengthened in evidence**. Extending the A20 paraphrase battery from eight to twelve, to meet `AC-REFUSAL-11`'s minimum of ten, found that **four of the twelve are not refused — and two of the four are paraphrases the criterion itself offers as worked examples** ("is $180K worth worrying about for a company this size?", "is this normal for this account?"). The four are asserted as pass-throughs in the red-team suite rather than deleted, and the shape matcher was NOT extended (`RESPONSIBLE_AI_KB` §4.1 rules that out as an arms race against paraphrase). One string also left the original eight: "Below the threshold we use here" contains a word the criterion's Given clause excludes. **`AC-REFUSAL-11` is NOT VERIFIED and no scenario in any suite names it** |
| 15 | The findings of **F26, F28, F9 and F33 are no longer fixture literals**: those four regions render real detector runs over the certified-query boundary against the synthetic warehouse, and the pilot GES app is given a seeded warehouse for it. The residual is narrower and unchanged in kind — the six items in `state._build_items` (the cross-period item, the omission, the coding item, the present anomaly, the abstention and the fidelity row) are still literals, and every screen still carries the pilot strip |
| 18 | Unchanged in substance; **the reporting is what changed, and it is now honest**. Gate 9 found `AC-F41-08` passing by asserting that no probe marker exists and the injected-probe count is zero — a criterion satisfied by the absence of the thing it is about. The UX-11 group now states that in its section header, **no scenario name carries the ID**, and every remaining mention of it in that file explicitly denies the criterion. The zero-count assertion carries an instruction to rewrite the group rather than relax the assertion when injection lands. `AC-F41-08` is NOT VERIFIED |

### Entries OPENED at pass 5

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 23 | `ARCHITECTURE_KB` §7.3's F28 A9 recompute, against a real ERP FX/CTA calculation | one named formula, `revaluation_delta`, in a **closed registry of Python functions** — `formula` is a key, never an expression, and there is no `eval` in the module | the recompute is genuinely independent of the observed figure, which is the property that matters, but it recomputes the ONE formula this build implements. A second revaluation convention is a change to `FORMULAS` in a reviewed diff, not configuration. Stated because "independently recompute a derived figure" reads as more general than what exists |
| 24 | F33's peer set, drawn from a real vendor/caption history | 163 synthetic postings for one vendor, plus the three period-3 miscodings that give the backtest something to measure | `min_peer_support` is 20 and `min_peer_agreement` 0.8, and neither has been calibrated against real coding behaviour — they are chosen to be conservative. `AC-F33-01`'s precision figure of 0.6667 is a property of a fixture, not a measured skill accuracy, and the pilot screen shows it beside a second held-out period with **no labels at all** precisely so a reader meets the difference. Real calibration needs a tenant. **Pass 6: WITNESSED IN THE SUITE, still open.** `test_AC_F33_06_…` derives `0.6667`/`0.5000` from the `close_datasets` constants rather than asserting literals, so the fixture provenance is executable; `test_AC_F33_01_…` reads `min_peer_support` from the manifest and asserts the run used it, instead of restating `20` as though the criterion fixed it; the functional file's header and three further sites state what both numbers are NOT |
| 25 | `AC-F9-05`'s "fewer than two periods of history" over a real close calendar | `min_history_periods: 2` on the numeric leg, measured in periods present in the movements extract | a period an account existed in but posted no movement to is indistinguishable here from a period before the account existed. On the synthetic fixture they cannot differ; on a real ledger they can, and the account that was dormant for a quarter would report as younger than it is. Needs a close calendar — which is register 6 again, from a different direction. **Pass 6: WITNESSED IN THE SUITE, still open.** The substitution is stated at five sites — the functional file's header, all three `test_AC_F9_05_*` scenarios, the governance-screen scenario that reads "Periods available", and the primitive scenario that computes `periods_available` — so a reader of the suite meets the movement-count measure rather than assuming a close calendar behind it |

### Entries OPENED at pass 7 (the gate-9 re-audit loop-back)

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 26 | Gate-6 ruling 1 — the evidence infrastructure is a SEPARATE trust domain, so one compromised credential does not reach both the state and the evidence of what changed it | `app/evidence/audit_domain.py`: a distinct SQLite store with `BEFORE UPDATE`/`BEFORE DELETE` triggers, written through an interface that has no delete, no purge and no retention setter | the **behavioural** separation is real and is the half `AC-F1-13`'s second clause tests: the application's own control-event log is emptied completely and every record is still retrievable from the destination, which a shared table could not fail. The **infrastructural** separation is NOT real — this is a second file in the same process on the same host, not a different account with a different credential in a different trust domain. Register 2's SQLite bound again, from a third direction. **A green functional suite is not evidence that one compromised credential cannot reach both**, and `AC-F1-13`/`-14` are VERIFIED only on the behaviour, not on the infrastructure |
| 27 | `AC-F36-48` — "a closed period over **real close data** in which a skill emitted zero abstentions" | the abstention band check runs against the pilot's SYNTHETIC period, whose abstention count is a property of six fixture items rather than of a skill's behaviour on real close data | the *computation* — band, red control finding, the above-band usefulness finding routed to the skill owner — is real and its boundary cases are testable. What the criterion asks for and this build cannot supply is the **input**: a period of real close data. On this fixture "zero abstentions" is achieved by removing a fixture item, not by a skill declining to decline. **Gate 9 was right that this is a register-24/25-class fixture substitution with no register entry.** It has one now. Real evidence needs a tenant, which is registers 21 and 24 again from a fourth direction |
| 28 | `AC-F40-17`/`-18` — an **export-time** CUEC probe that detects Oracle-side configuration drift since deployment and refuses the export | nothing. The CUEC register's stored pass state is read at export time and a `never_verified`/`expired`/`failed` state refuses the export, but **no probe re-reads the tenant's configuration**, so drift after a recorded pass is undetected | **`AC-F40-17` and `AC-F40-18` are NOT satisfied and no suite claims them.** The criterion's whole point is that the stored pass state does NOT authorise the export, and this build authorises on exactly that. Closing it needs an Oracle tenant to probe — register 21's residual. Recorded rather than approximated: a probe that re-read our own register and reported no drift would be a check that cannot fail |

### Entries OPENED at pass 8 (the last of the gate-9 loop-back)

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 29 | A semantic layer in which certified **metrics and joins are artefacts in their own right, versioned independently of the queries that use them** — which is what `AC-F39-04`'s "the version of each certified metric and join used" presupposes | the versions are **declared on the certified query** (`semantics:`, required at compile time) and committed with it. `SemanticElement` in `ges/registry/loader.py` carries the in-file denial | `AC-F39-04` itself IS satisfied, on both surfaces, from a single source rather than a screen literal — the criterion asks that the versions be STATED, and they are, on the answer and in the dossier. What is substituted is **where they live**, and two consequences are real: (a) a metric version can only change when a query file changes, so "the metric moved and three queries still name the old version" is not a state this build can represent, which flatters it; (b) nothing cross-checks that two queries naming `posting_period_join@1.9` mean the same join — they do here because one person wrote both. Closing it needs a metric store, which is a phase-2 artefact |
| 30 | A **calibrated** threshold for `journal_attribute_outlier` — an attribute count and a rarity ceiling derived from a measured false-positive rate on real close data | `min_attributes: 3` and `rarity_ceiling: 0.05`, DECLARED in the manifest. Every finding states the threshold in force, its inclusivity, the closed attribute set scored, and an explicit `threshold_calibration` denial | `AC-F42-02` asks that the journal and the attributes that made it an outlier be NAMED, which does not depend on calibration, so the criterion is satisfied and the check claims nothing more. What is NOT claimed: any measured likelihood, precision or false-positive rate for this detector. This is register 24's residual from a second direction — calibrating it needs real close data, which is register 21/24 again. The denial is at the module header AND on every emitted finding, so a reader of a finding meets it without reading the source |

### Entry BROADENED at pass 10

| # | Change |
|---|---|
| 18 | **`AC-F12-05` joins `AC-F41-08` under this entry.** They are one absent programme seen from two sides: `-08` asks that an injected probe be indistinguishable from a genuine proposal; `-05` asks that the capture record identify the item as a probe, record the reviewer's response and whether it was correct, **and** that the probe not be distinguishable before disposition. With no probe injected, `-05`'s first two clauses have no capture record to be checked against and its third is reached only by the absence of the thing it is about — the identical shape `-08` was descoped from claim for at pass 5. Gate 9 found the live contradiction: `tests/suites/ux/test_ux_flow.py` carried a join reading "`AC-F12-05` is served by this" in a docstring whose next paragraph explained why it is not. The join is now narrowed to the third clause with the denial **inside the join string**, so a by-ID mapper cannot score it satisfied. **`AC-F12-05` is NOT VERIFIED**, and no scenario in any suite names the bare ID |

### Entries CLOSED at pass 11 (scope-ruling batch A)

| # | Was | Now |
|---|---|---|
| 6 | `ARCHITECTURE_KB` §5.3's `CloseClock` did not exist, and it was the reason **two** criteria were unmet: `AC-F26-05` (staleness relative to the close clock) and `AC-F38-11` (every emitted figure carries that staleness on its face). Both were treated as tenant-dependent | **CLOSED.** `plan-agent`'s ruling corrected the premise, and the correction is what made it buildable in an afternoon: **a close calendar is a declaration, not a tenant artefact** — a list of period-end dates and close-day checkpoints per ledger. `common/close_calendar.py` declares two (the twelve-period fixture's fiscal year and the pilot close), versioned and referenced by ref from the manifests that use them. `AC-F26-05`: the A2 leg emits a `close_clock_relative` note whose sentence names the cut-off and the distance from it, and the F26 fixture exercises both "one close day behind" and "zero close days behind". `AC-F38-11`: the staleness renders in the **page shell's provenance strip**, so every screen the application serves carries it beside the dataset version and the data as-of — including the chrome-off evidential view, where a figure is read years later by somebody who cannot go and look. Nothing reads a wall clock: the figure is arithmetic over declared checkpoints, so two readers of one run agree. **The absence path is retained and separately covered** — a ledger with no declared calendar still emits `close_clock_absent` naming the unmet criterion, which is the state every tenant is in before somebody writes their calendar down |
| 25 | `AC-F9-05`'s "periods of history" was measured in periods present in the movements extract, so an account dormant for a quarter read as **younger than it is** — and a young account is excluded from the cross-period view, in F9, one of the four must-survive items. Witnessed in the suite at pass 6, still open | **CLOSED**, by register 6's closure from the other side. With a calendar declared, history is the span of declared periods from the account's first observed movement to the target period, dormant periods included. `accumulation` reports **both** numbers on every insufficient-history note — the periods the account posted in and the periods of history it was judged on — and names the measure in force (`history_measure`), which the Monitors screen renders. The fallback measure survives for a ledger with no calendar and carries the old denial verbatim on every note it produces, so a reader of a fallback note still meets register 25's wording. Boundary scenarios both ways: a dormant account is now evaluable; an account whose first movement is the target period is still too young |

### Entry OPENED at pass 11 (scope-ruling batch A)

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 31 | `ARCHITECTURE_KB` §5.4's point-of-action revalidation as `AC-F40-12`/`-13` word it: a balance that has moved **in Oracle**, a period that is not `Open` **in Oracle**, read at the moment of action | the recheck runs at export time against the **ERP control extract** — the certified dataset F26 established, narrowed to the proposal's account combinations, with Oracle's period status and newest-journal timestamp entering as extract-borne columns | **The criteria are satisfied and the counterparty is weaker than their wording.** What is real: the comparison, the tolerance (declared, inclusive, stated on the record), and four refusals that actually stop a file existing — a moved balance, a journal newer than the pinned watermark, a period that is not open, and a recheck that could not run. What is NOT true: that this reads Oracle at the moment of action. **MVP1 must not claim it does.** The mitigation is that every revalidation record and every revalidation refusal NAMES the extract and its as-of and carries `counterparty_is_live_oracle_read: False` — so a reader of the record meets the substitution without opening this table, which a record saying only "revalidated at 14:32" would not. Same class as register 7. Closing it needs a live Oracle read at the point of action, which is register 21's tenant again |

### Entry NARROWED at pass 11 (scope-ruling batch A)

| # | Change |
|---|---|
| 3 | **Unchanged in substance; the disclosure now reaches the artefact it was missing from.** The anchor is still a labelled digest and `AC-F1-11` is still unmet. What changed: the stub's status travels into the **auditor export payload and file** (`evidence_integrity.anchor`), not only into the register, the anchor rows and the Audit screen. `AC-F1-04` makes that file the artefact an auditor consumes with no application login, so the one reader who cannot go and look was the one reader not being told. The wording is the ruling's permitted claim exactly: tamper-**detection** against accidental modification and against a party who does not recompute the chain; **not** tamper-evidence against a party holding application-level write access |
| 4 | **Unchanged and still open; `AC-F1-08` still unmet.** The ruling's new MVP1 requirement is built: wherever a retention date is rendered, the absence of retention enforcement renders **adjacent to it** — inside the same region, from one home (`app/evidence/retention.py`), on the dossier header, on the auditor-export manifest, and inside the export file's payload. A walk from `/` asserts that every screen carrying the date carries the denial. The permitted claim is the ruling's: append-only within the running system, hash-chained, with a retention **stamp** — and "seven-year immutable retention" appears in this build only inside the sentence that says it is not met |
| 28 | **`AC-F40-18` is built and this entry no longer covers it.** The entry was recorded as one gap covering both export-time CUEC criteria; `plan-agent`'s scope ruling separated them, and it was right to. `-18`'s Given — *a CUEC probe cannot execute* — is this build's **permanent** state, so it is fully evidenceable here, and until pass 11 the build did the criterion's explicitly forbidden thing: it authorised the export on the stored pass state. `ges/cuec_probe.py` now runs at export time, returns `cannot_execute` for every item (there is no tenant to read), and **refuses the export independently of the register** — a tenant with all five controls recorded `passed`, in date, still exports nothing. The default probe on every GES app is the one that cannot execute, so omission refuses. Pilot operability is preserved the way register 21 already does it: a **declared synthetic attestation**, one named file (`backend/ges/synthetic_cuec_attestation.json`), installed explicitly by `pilot.py` and the two suite harnesses, refused under `CONCLAVE_ENV=production`, and carried as `authorised_on = synthetic_attestation` in the export payload and on the export screen's face. `synthetic_attestation` is a **separate status from `no_drift`**, and a unit scenario fails the moment they are collapsed. **`AC-F40-17` STAYS OPEN under this entry**: no drift detection exists, nothing in this build can return `drift_detected`, no suite claims the ID, and every join string that mentions it carries the denial inside it |

### Entries CLOSED at pass 12 (scope-ruling batch B)

| # | Was | Now |
|---|---|---|
| 18 | The F12 probe-**injection** programme did not exist, so `AC-F41-08` and `AC-F12-05` were both being reported satisfied by checks asserting that no probe marker exists and that the injected-probe count is zero — a criterion satisfied by the absence of the thing it is about. The entry's standing instruction was to **rewrite the UX-11 group against a real probe when injection landed, never to relax it** | **CLOSED.** `app/f12/probes.py` manufactures known-error items, plans injection at a rate drawn inside the disclosed band, and registers them in a store the queue item knows nothing about. UX-11 is rewritten as the entry instructed: indistinguishability is now a comparison between **two rendered items** — same `data-testid` set, same attribute names, same class names, with the comparator matched on the two properties that legitimately differ between genuine findings (risk tier and allowed resolution set) — plus a queue-row shape check and a vocabulary check over the probe's own regions. `AC-F41-08` and `AC-F12-05` are **both now claimable and claimed**: `-05`'s first two clauses are evidenced against a capture row written by disposing of a real probe through the real control, and its third by the comparison above rather than by an absence |

### Entries OPENED at pass 12 (scope-ruling batch B)

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 32 | Probe injection at a rate drawn from the disclosed band, over a queue of the size a real nightly queue is — where a 2–8% band produces probes naturally | the planner is exactly that (a rate drawn per queue, a Bernoulli draw per item, the rate discarded), but the **pilot's demonstration queue is seven items**, where that band yields no probe about seven times in ten. `PILOT_INJECTION_SEED` is therefore **chosen** so the demonstration queue receives one | **No criterion is unmet.** What is chosen is the seed, not the rate: `plan_injection` draws from the band and a run under any other seed is a legitimate run of the same planner, asserted by a scenario that measures the realised rate over 50,000 draws and requires it inside the band, and by one that requires the per-queue count to VARY. The consequence is narrower and real: **the pilot's probe count is effectively fixed**, so nobody may read "one probe in this queue" as evidence about the rate. Closing it needs a queue of realistic size, which needs a tenant — register 21 again |
| 33 | `AC-F39-05`'s coverage over the declared population, for **every** certified query the resolver can select | coverage is a set difference over member keys, computed via the population's **certified member resolver** — which exists for four of the populations (`pop.recurring_accruals`, `pop.monitored_accounts`, `pop.period_journals`, `pop.postings_under_coding_review`) and not for the rest | **`AC-F39-05` is satisfied**, and it is satisfied on a query whose population HAS a resolver, over a warehouse in which the population is genuinely non-empty and the answer genuinely returns nothing — a zero over a zero would have been vacuous in the other direction. Where no member resolver exists the answer says coverage is **UNKNOWN, not complete**, which is convention C2 in its coverage form and is the most dangerous rounding in the product if it is ever softened. Closing it needs a member-resolver query per population, which is a manifest each, not a capability |

### Entry NARROWED at pass 12 (scope-ruling batch B)

| # | Change |
|---|---|
| 9 | **The A20 residual is WIDER after the F39 resolver, and the widening is the finding.** Register 9 recorded that A20 holds absolutely where an emission carries a disposition on a size-shaped ground and heuristically in free prose. What narrowed it was that *there was nothing downstream to evade into* — all three triage outcomes were declines, so a request slipping past every request pattern still produced no answer. **That is no longer true.** Re-running the RT05 battery against the resolving path found that **eleven of the twelve paraphrases are not refused at the REQUEST surface**, including all eight the emission broker refuses: the request matcher and the emission matcher are different sets over different objects, which was harmless while every request declined. A crafted paraphrase that evades every A20 request pattern and names a mapped subject now reaches an **answer with real rows**. `RT05_AT_THE_REQUEST_SURFACE` records what each of the twelve reaches so a change to either matcher fails the map, and `test_RT05_a_paraphrase_that_evades_A20_now_reaches_an_ANSWER` asserts the new pass-through directly. Bounded, and the bound is asserted too: what it reaches is **rows and a coverage statement** — no disposition, no recommendation, no characterisation of a difference as small — and the structural leg is unweakened. **`AC-REFUSAL-11` stays phase 2, is claimed nowhere, and the resolver does not unlock it** |

### Entry OPENED at pass 18 (gate-8 loop-back)

| # | Spec | Built instead | Unmet criterion / consequence |
|---|---|---|---|
| 34 | `AC-F5-02`'s population — *"an agent that has been deployed and has **performed at least one action**"* appears in the Inventory with its identity, entitlements and version — together with `AC-F5-03`/`-05`'s lineage completeness over an agent's artefacts | the Inventory is a projection of the **principal registry**, and lineage is a traversal of the **decision ledger**. Neither population is the criterion's population | **`AC-F5-02`, `AC-F5-03` and `AC-F5-05` are NOT VERIFIED and are claimed by no scenario.** Two faces of one gap, both found by gate 8 at pass 17. (a) **Five agents authored findings in the pilot close and four are absent from `/inventory`** — `agent.crossperiod-surveillance`, `agent.omission-detector`, `agent.anomaly-detect`, `agent.fidelity-check` — because the run's author ids and the registry's principal ids are not the same strings. The covering scenario asserted `inventory == principals.DIRECTORY`, **the projection against its own source, an equality that cannot fail for the reason the criterion is about**. (b) **Seven evidence dossiers exist and zero appear in any lineage**, while every row reported `complete=True` — a partial list returned labelled complete, which is precisely what `-05` forbids. **Why it is not closed in this pass:** reconciling the ids means either registering four principals the F5 compile step never produced — the manual registration step `-02` itself forbids, and it would fabricate entitlements for agents that never went through registration — or renaming author ids to registry ids when two of the four have no registry counterpart at all. Both invent governance facts. **What was built instead:** the incompleteness is stated on the face of the surfaces that have it. `/inventory` names all four absent agents, links each to its agent page, and says `AC-F5-02` is not met; the unqualified sentence *"An agent that can act is an agent that is listed"* is gone from that screen. Every lineage row states its **scope** (`decision_ledger`), is labelled **INCOMPLETE**, and names the artefact classes it could not traverse, from `ges/main.py:LINEAGE_UNTRAVERSED` — declared at the broker, because the label belongs to the thing making the claim. `/ges/inventory` additionally returns `unregistered_actors`, the broker's own answer to the population question computed from its ledger. The two scenarios are rewritten to assert against **the agents that actually authored findings** and against **the dossiers that actually exist**, so each fails if the gap moves in either direction — including if the ids are reconciled and the disclosure is left behind. Closing it needs the F5 registration path to be the same id space the run authors under, which is a registry change, not a rendering one |

**Corrections to entries 33 and 34 at pass 19 — no entry opened, closed or
narrowed.** Two sentences of entry 34 were accurate when written and are no
longer the whole picture, so they are amended here rather than silently
outgrown.

- *"the unqualified sentence … is gone **from that screen**"* — literally true,
  and gate 8 found the same sentence standing in the subtitle of all four
  `/evidence/agent/<id>` pages that screen links to. **The sentence is now on
  no reachable screen**, and the guard that says so walks the whole reachable
  surface plus the post-control documents instead of naming `/inventory`.
- *"`/ges/inventory` additionally returns `unregistered_actors`, the broker's
  own answer to the population question computed from its ledger"* — accurate
  about the method, and the method cannot answer the question: findings are not
  ledger-recorded, so the field could not become non-empty. It now returns
  **UNKNOWN rather than an empty list**, in register 33's convention C2 shape,
  and is rendered on `/inventory` and asserted by two scenarios. **Register
  33's convention therefore now has a second application in the build**, which
  is the point of recording a convention rather than a fix.
- Entry 34's third "built instead" claim — the `/inventory` links to each
  absent agent's page — was held by no scenario and is now followed and
  asserted. All three parts of that list are mutation-held as of pass 19.

### Entry 34 BROADENED at gate 7 pass 21 — `AC-F5-07` joins it

**No entry is opened, closed or narrowed. One criterion is added to an existing
entry, because it fails for a cause already recorded there and a second entry
would make one gap look like two.**

`functional-design-agent`'s ruling (`FUNCTIONAL_SPEC` §28.2) settles what
`AC-F5-07`'s *each agent* quantifies over: **the agents that have ACTED**, the
same population as `AC-F5-02`, not the registry the Inventory projects. Reading
it as "each **registered** agent" makes the criterion satisfiable by the
projection of the registry onto itself — the tautology gate 8 already found in
`AC-F5-02`'s own scenario, relocated one criterion to the right — and that was
exactly the population `test_AC_F5_07_every_agent_is_listed_with_version_and_
entitlements` asserted over.

So entry 34's unmet set reads **`AC-F5-02`, `AC-F5-03`, `AC-F5-05` and now
`AC-F5-07`**, all four for one cause: the run's author ids and the registry's
principal ids are not the same strings. **Two criteria failing for one cause is
the normal case and neither is narrowed.** The forbidden set is **nine**, not
eight: `AC-F1-08`, `AC-F1-11`, `AC-REFUSAL-11`, `AC-F40-17`, `AC-F36-48`,
`AC-F5-02`, `-03`, `-05`, **`-07`**.

**What was built instead, and it is `AC-F5-08` rather than a disclosure.** The
four agents known only by authorship were named in a *paragraph* on
`/inventory` and had no place in the listing. Each now has an inventory row,
under the identity it authored as, and for version, entitlements and status
states that the value is **not recorded** and names the registry gap that makes
it missing — never omitted, blank, dashed, or carrying a neighbour's value, and
each of those four renderings is refused by a mutation-held assertion. No
lineage view is rendered for those rows: a decision-ledger traversal for a
principal the ledger has never seen returns zero, and a zero in the same
component as a real result reads as *"this agent touched nothing"*, which is
false about an agent that authored findings. **`AC-F5-08` is MET. It does not
make `AC-F5-07` met, and the screen itself says so** rather than letting a
fuller listing imply it.

Two joins that would have scored `AC-F5-07` satisfied are removed: the bare ID
opened `pages.inventory`'s own docstring as an unqualified claim — the same
shape as the unqualified `AC-F5-02` sentence gate 8 found on this screen, one
layer down in the source — and the test file's section header read
"Inventory — `AC-F5-07`". The disclosure scenario is written in the established
`_IS_NOT_MET_` shape and fails **in either direction**, including the day the
ids are reconciled and the disclosure is left standing.

**Closing it is still a registry change, not a rendering one**, and it is
`plan-agent`'s (`FUNCTIONAL_SPEC` §28.6.1).

**Thirty-four entries as of pass 21. Entries 6, 8, 10, 11, 13, 14, 16, 18 and 25
are CLOSED. Entries 1–5, 7 and 9 stand as recorded at pass 1 and 2c; entries 3 and
4 are still the two that cannot quietly become "MVP1 ready". Entry 34 is the
newest, is the first opened by a gate-8 finding rather than by `code-agent`'s
own disclosure, and was broadened at pass 21 to carry `AC-F5-07`.**

**On register 16 and `AC-REFUSAL-13`.** Gate 9 was right that a register entry
claiming closure with no covering check is the same defect class as an
over-broad join. The entry was accurate — A23, A24 and A25 *are* each visible
by name on the Refusals screen with their grounds — and the evidence was
missing. Three named checks now carry the ID
(`tests/suites/functional/test_unclaimed_criteria.py`), covering the three
clauses separately: the seven A-numbers by name, the ground and by-design
wording beside each, and reachability from `/`.

> **Corpus date ruling (orchestrator, 2026-07-31).** `test-agent` flagged that
> the evidence corpus was dated `2026-08-01` while the system clock and every
> commit in `dev/` read `2026-07-31`. Ruled: the corpus is **2026-07-31**, the
> date the runs actually happened. The earlier `2026-08-01` naming was wrong at
> both gate-8 runs and is corrected here rather than carried for continuity — an
> evidence file whose date disagrees with the commit it names is the same class
> of defect as a stale corpus, and this project has already been blocked twice
> for that.

## Scope ruling — gate 9's 26 unbuildable criteria (plan-agent, 2026-07-31)

Gate 9 blocked with 26 criteria whose capability does not exist, and ruled the
scope question `plan-agent`'s. It ruled **21 into MVP1, 5 declared**. Accepted by
the orchestrator without amendment. Arithmetic: 233 verified + 3 in flight + 21
= **257 verified, 5 declared-not-verified, 262 total.**

| Cluster | Ruling | Criteria |
|---|---|---|
| Point-of-action revalidation | **MVP1** — counterparty is the ERP control extract, which F26 already established | 5 |
| Probe-injection programme | **MVP1** | 9 |
| Close clock | **MVP1** — a close calendar is a *declaration*, not a tenant artefact | 2 |
| F39 resolver call site | **MVP1** (4); `AC-REFUSAL-11` stays phase 2 | 4 |
| Export-time CUEC | `AC-F40-18` **MVP1**; `AC-F40-17` phase 2 | 1 / 1 |
| Supersession by data | **MVP1** | 2 |
| KMS-signed anchors | **Phase 2** — dependency | 1 |
| Object-Lock archive | **Phase 2** — dependency | 1 |
| Real close data | **Phase 2** — dependency | 1 |

### The two rulings that carried the most weight

**The probe programme cannot be deferred, for a reason that is not about
features.** It has *no dependency of any kind* — no tenant, no Oracle, no model —
so "phase 2" here is a pure scope choice. And it is **retrospectively
unrecoverable**: you cannot probe a period that has already closed, so a pilot
run without injection produces a period of review activity from which nothing
about reviewer attention can *ever* be recovered. Decisively: gate 6 overturned
the promotion gate as inverted because precision on accepted proposals takes its
labels from reviewer behaviour. P1/P5 were deferred because they presuppose F17.
**Probes do not presuppose F17.** Ship without them and MVP1's only ground truth
about review quality is the reviewer's own behaviour — the exact circularity gate
6 ruled fatal. It ships *with* its full non-attributability set
(`AC-F12-13`/`-14`/`-15`/`-17`), because a probe programme that can attribute a
miss to a named person is a worse artefact than none.

**`AC-F40-18` is a defect, not an absence.** The distinction: an absent
capability that defaults **closed** is a limitation; one that defaults **open at
the Tier-2 egress** is a defect. Today the build authorises the export on the
stored pass state — `AC-F40-17`'s explicitly forbidden behaviour and
`AC-F40-18`'s explicitly forbidden fallback. Its Given ("a CUEC probe cannot
execute") is this build's permanent state, so it is fully evidenceable here.

### Claim prohibitions attached to the five declared

- **`AC-F1-08` / object lock** — MVP1 must **not** claim seven-year immutable
  retention **anywhere**: not in the product, a pilot pack, a deck, or an
  audit-committee artefact. It may claim append-only within the running system,
  hash-chained, with a retention *stamp*. **New MVP1 requirement:** wherever a
  retention date is rendered, the absence of enforcement renders adjacent to it —
  a date reads as enforcement to every reader who has not opened the register,
  and the reader who most needs to know is the controller taking an F1 export to
  an audit committee.
- **`AC-F1-11` / KMS** — may not claim tamper-evidence against a party holding
  application-level write access. May claim tamper-*detection* against accidental
  modification and against a party who does not recompute the chain.
- **`AC-REFUSAL-11` / A20** — the only sentence the product may use: A20 holds
  **absolutely** wherever an emission carries a disposition on a size-shaped
  ground, and **heuristically** otherwise. The resolver does **not** unlock this
  and makes the exposure *worse* — today an evading paraphrase reaches a decline;
  afterwards it reaches an answer. Two hard conditions on the resolver: triage's
  refusal check stays ahead of resolution unconditionally, and the A20 battery is
  re-run against the resolving path with the evasion test updated to assert what
  it now reaches.
- **`AC-F36-48`** — may not claim the abstention band is calibrated, nor that any
  pilot abstention rate is evidence about a skill.

### The cost of cutting F39, stated as plan-agent required

If the resolver is cut, what goes to the human is **not** "F39 partially
deferred". It is: *MVP1 does not implement Part 2 of the product direction, and
the FP&A persona — one of three the Decisions Log binds as primary — has no
functioning surface.* `PLAN.md` §7.7's open persona conflict is **wider today
than it disclosed**, because it claimed FP&A was served by F39's inquiry leg and
that leg declines everything.
