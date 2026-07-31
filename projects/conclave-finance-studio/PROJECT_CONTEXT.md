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

## Current Status

Gate 7 · Code — MVP1 in staged passes against **262** acceptance criteria.
(261 until the gate-9 loop-back: `FUNCTIONAL_SPEC` §27.11's arithmetic said
"262 issued, 261 live (186 + 77 − 1)" and 186 + 77 is 263. Corrected in the
spec at v1.1.1; **no ID was renumbered, added or removed**.)

**Passes 1, 2a, 2b, 2c, 3, 4 and 5 complete** (36 commits in `dev/`, **1,428
unit tests + 388 suite scenarios**, all green. **All six suites execute**;
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
| **F26** warehouse-to-ERP fidelity | `identity_tieout`, `freshness`; two manifests; a two-leg run; the Exceptions region | `AC-F26-01`…`-04`, `-06`…`-10` | `AC-F26-05` (no close clock, register 6) |
| **F28** the five boundary checks | `pair_imbalance`, `continuity`, `arithmetic_recompute`, `residual_threshold`; `identity_tieout` bound a second time for A6; five manifests; `BoundaryRun` | `AC-F28-01`…`-10`, all ten | — |
| **F9** cross-period surveillance | `accumulation`, `text_recurrence`; two manifests; both legs; the R6 control-state change; the Monitors regions | `AC-F9-01`…`-09`, all nine | — |
| **F33** coding anomaly + backtest | `peer_coding_divergence`; the backtest evidence schema; the Exceptions region | `AC-F33-01`…`-12`, all twelve | — |

**All eleven `ARCHITECTURE_KB` §7.3 evaluator primitives now exist.**
`SPECIFIED_BUT_NOT_IMPLEMENTED` is empty — and is KEPT, empty, because a
manifest naming a specified-but-unbuilt primitive must still fail compilation
*saying so*. A `parametrize` over an empty tuple collects zero tests and
reports green, so that behaviour is now asserted against a planted entry
instead.

**Two of gate 9's three contradictions were capabilities that do not exist and
are now stated as unmet rather than claimed**; the third was a missing build
and is built. See Decisions Log items 13–15.

**Not built and absent rather than stubbed**: point-of-action revalidation, the
close clock (`AC-F38-11`, and therefore `AC-F26-05`), the F12 probe-injection
programme (`AC-F41-08`), F17 direct posting, and the F39 natural-language
resolver's model call site (and therefore `AC-REFUSAL-11`, `AC-F39-03`, `-05`,
`-06`, `-08`).

## Test Results

### 2026-07-31 — Gate 8 · Test — `test-agent`, gate-8 verification run

**Every suite EXECUTED. Every suite green. Exit code 0 across the board.**
Structured per-scenario evidence: `test-evidence/*-2026-07-31.md`.

| Suite | Status | Exit | Scenarios | Pass | Fail | Owner | Blocking |
|---|---|---|---|---|---|---|---|
| unit/integration | `EXECUTED` | 0 | 1,217 | 1,217 | 0 | `test-agent` | yes |
| functional | `EXECUTED` | 0 | 21 | 21 | 0 | `functional-agent` | yes |
| architecture | `EXECUTED` | 0 | 21 | 21 | 0 | `solution-architect` | yes |
| security | `EXECUTED` | 0 | 14 | 14 | 0 | `security-architect` | yes |
| red-team | `EXECUTED` | 0 | 40 | 40 | 0 | `responsible-ai-architect` | yes |
| industry | `EXECUTED` | 0 | 23 | 23 | 0 | `industry-expert` | yes |
| ux | `EXECUTED` | 0 | 186 | 186 | 0 | `ui-ux-designer` | yes |
| post-deploy smoke | `EXECUTED` | 0 | 7 | 7 | 0 | `test-agent` | yes |

No suite is `STATIC ONLY` and no suite is `PARTIAL`. The `ux` suite ran under
`dev/.venv/bin/python` with Playwright present and Chromium launched — 186
scenarios against a **real rendering engine**, every request fulfilled from the
in-process ASGI app, no server started inside the agent's turn.

**Test-count delta.** No previous `test-agent` run exists, so these are a
**baseline**, not a delta. They reconcile exactly with `code-agent`'s pass-4
figures (1,217 unit + 305 suite scenarios), which is itself a check. Against
gate 7 pass 3 (`2ed6b4e..HEAD`): **157 test functions added, 8 removed, 0
silently changed.** All 8 removals asserted the HTTP 501 deferred screen that
pass 4 replaced with a real write path; each names its replacement's
destination, and the destinations (`test_ui_write_path.py` +736 lines,
`test_ges_decide_route.py` +438 lines) assert against the **store**, not the
confirmation message. Verified: no replacement is weaker.

**Post-deploy smoke test — PASS.** `CONCLAVE_ENV=pilot backend/pilot.py`
started, all thirteen routed screens served 200, the pilot strip rendered, the
dossier carried zero external references, a staff approval was refused 403 by
the broker, and the process was stopped with nothing left running. Started,
exercised and stopped inside one command invocation. **Note the pilot binds
8021, not 8000** — an unrelated process answers 404 on 8000 and a smoke test
aimed there reports thirteen false failures.

**No blocking suite failed. The gate is not stopped by a suite failure.**

**But five green scenarios claim more than they prove**, and this is the
finding of the run rather than the counts. Full evidence:
`test-evidence/register-cross-check-2026-07-31.md`.

1. **`test_AC_F1_08_a_dossier_returns_complete_with_its_retention`** (functional,
   green) asserts only that a `retention_expiry` date string it wrote seconds
   earlier is truthy. It never retrieves from an archive and never advances a
   clock. Register entries 4 and 20 say the seven-year obligation is unmet and
   that `AC-F1-08`'s oldest-end retrieval has no object store. **A reader
   mapping suite IDs to criteria will mark `AC-F1-08` satisfied. It is not.**
   *(Fixed at pass 4d: renamed to
   `test_a_just_written_dossier_reads_back_complete_and_carries_a_retention_stamp`
   and rescoped to what it tests — a round trip plus the presence of a
   retention stamp, asserted alongside `StubObjectLockArchive.has_retention_lock
   is False` so it cannot be misread as retention being in force. The string
   `AC-F1-08` no longer appears in any test file.)*
2. **A20 is reported more strongly than register 9 permits.** Eight of nine
   red-team RT-05 scenarios are named
   `…a_materiality_conclusion_never_reaches_a_surface_however_phrased`.
   *(Fixed at pass 4d: renamed to
   `…each_paraphrase_in_this_fixed_battery_of_eight_is_refused_at_the_broker`,
   and the evasion now has its own red-team scenario asserting it reaches a
   surface. Register 9 carries the exact shape.)*
   *However phrased* is exactly what register 9 denies. Probing the broker
   directly found a **working evasion the suite has no scenario for**: evasive
   prose + a `treatment` claim + a *substantiated* ground returns `allow`. The
   suite tests the two cases that are caught and not the one that is not; the
   test that demonstrates the evasion lives in the **unit** suite, not the
   red-team suite.
3. **The architecture suite's only trust-boundary check would still pass if the
   boundary were gone entirely.** `test_the_api_package_never_imports_the_ges_package`
   is a static regex over `backend/app/` source text; `pilot_transport.py` sits
   outside that package by design. Its docstring defers the runtime half to the
   `security` suite — but the security suite's three real-subprocess scenarios
   test the **credential** boundary, not the process boundary, and
   `pilot_transport` deliberately does not set `CONCLAVE_PROCESS_ROLE`, so they
   never run against the pilot configuration. **No scenario in any suite
   exercises the two-process loopback topology.**
4. **`test_the_override_rate_is_visible_with_its_denominator`** (ux) passes with
   its persona-switch POST body discarded — proven by re-introducing the pass-4
   body-dropping bug and running it: `1 passed in 0.83s`. It spends three lines
   becoming the controller and every assertion holds as a staff accountant.
   **It establishes nothing about the controller persona.** Its siblings in the
   same class do depend on the switch, which is why 9 UX scenarios failed under
   that probe and this one did not.
5. **`test_UX12_the_three_failure_grammars_differ…`** exercises two of the three
   it names. UNAVAILABLE — "the one a reviewer must never read as a denial" —
   is never posted in the scenario named for it.

**On the POST-harness disclosure (pass 4 judgement call 9):** re-introducing the
bug failed **9 of 186** UX scenarios, all in `TestUX14ControllerNightOverMonitors`.
The persona switch is the only body-bearing POST the suite makes; the other
write controls carry no form fields that change the outcome. The fix was real
and necessary, and it is load-bearing for exactly one journey.

**On registers 3 and 4:** no suite claims `AC-F1-11`. `AC-F1-11` appears in no
test file at all. The anchor and archive scenarios correctly assert the
*negative* and are named for it. Executed probe confirms the residual is real —
the anchor signature is the literal string `STUB-UNSIGNED:<digest>`, requiring
no secret to produce, so an attacker who recomputes the chain can also
recompute the anchor.

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
| 24 | F33's peer set, drawn from a real vendor/caption history | 163 synthetic postings for one vendor, plus the three period-3 miscodings that give the backtest something to measure | `min_peer_support` is 20 and `min_peer_agreement` 0.8, and neither has been calibrated against real coding behaviour — they are chosen to be conservative. `AC-F33-01`'s precision figure of 0.6667 is a property of a fixture, not a measured skill accuracy, and the pilot screen shows it beside a second held-out period with **no labels at all** precisely so a reader meets the difference. Real calibration needs a tenant |
| 25 | `AC-F9-05`'s "fewer than two periods of history" over a real close calendar | `min_history_periods: 2` on the numeric leg, measured in periods present in the movements extract | a period an account existed in but posted no movement to is indistinguishable here from a period before the account existed. On the synthetic fixture they cannot differ; on a real ledger they can, and the account that was dormant for a quarter would report as younger than it is. Needs a close calendar — which is register 6 again, from a different direction |

**Twenty-five entries as of pass 5. Entries 8, 10, 11, 13, 14 and 16 are
CLOSED. Entries 1–5, 7 and 9 stand as recorded at pass 1 and 2c; entries 3 and
4 are still the two that cannot quietly become "MVP1 ready".**
