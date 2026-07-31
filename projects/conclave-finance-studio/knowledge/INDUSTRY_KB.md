# Industry Knowledge Base — conclave-finance-studio

**Industry (A4.2):** Finance & accounting — **corporate controllership**, specifically
the record-to-report (R2R) / financial close function inside a public or
audit-exposed company running Oracle ERP Cloud.

**Author:** `industry-expert` · **Gate:** 1 (Intake) · **Date:** 2026-07-30
**Status:** Complete for Intake. Sections 4–6 are binding inputs to gates 2, 3 and 6.

> **How to read this.** Section 2 is the market reality check the human asked for
> ("crowded space, narrow gap" rather than an encouraging survey). Sections 4–6
> are the parts that constrain architecture and should be treated as requirements
> input, not background reading. Section 7 feeds `plan-agent` at gate 3.
> Everything sourced is linked in Section 9; where I am asserting from
> professional domain knowledge rather than a citation, I say so inline.

---

## 1 · The industry in one paragraph

Corporate controllership owns the integrity of the numbers. The close is a
time-boxed production run — day 1 to day N — in which subledgers are reconciled
to the general ledger, accruals and estimates are booked, intercompany is
eliminated, balances are substantiated, variances are explained, and a controller
signs off so a CFO can certify. The function's defining characteristic, and the
one that most software aimed at it underestimates, is that **it is not optimised
for speed — it is optimised for defensibility.** A close that finishes on day 3
but cannot be evidenced to an auditor is worse than a close that finishes on day
6 and can. Every feature proposal in this project should be read against that
sentence.

The three personas in A2.2 have genuinely different loss functions:

| Persona | Wants | Fears |
|---|---|---|
| Staff accountant | Fewer keystrokes, less tie-out drudgery | Being blamed for something a tool did |
| Controller / close manager | Visibility, evidence, sign-off confidence | A material weakness with their name on the process |
| FP&A analyst | Explanation, driver attribution, narrative | Explaining a variance that turns out to be a posting error |

The controller is the buyer and the blocker. The staff accountant is the user.
FP&A is the beneficiary. A product that delights the staff accountant and
frightens the controller does not get bought — this is the single most common
failure mode for close-adjacent AI tooling, and it is a product-design constraint,
not a compliance footnote.

---

## 2 · Market landscape — honest version

### 2.1 The space is crowded, and the incumbents are not asleep

Close management and reconciliation is a mature category with well-capitalised
incumbents who have all shipped agentic messaging within the last ~18 months.

- **BlackLine** — the reconciliation and account-substantiation standard in
  mid/large enterprise. Its 2026 positioning is explicitly *"Agentic Financial
  Operations,"* framed around closing AI's **governance and trust gap** rather
  than around raw automation ([BlackLine investor release](https://investors.blackline.com/news-releases/news-release-details/blackline-unveils-agentic-financial-operations-close-ais/)).
  Read that positioning carefully: the incumbent has already identified trust,
  not capability, as the competitive battleground. Any differentiation story
  built on "our agents are smarter" is competing where BlackLine has decided not
  to fight.
- **Trintech** — Cadency/Adra; strong in high-volume reconciliation and
  regulated/financial-services close. Now shipping "embedded, finance-native"
  AI marketed on **explainability** inside core R2R workflows
  ([Trintech](https://www.trintech.com/news/trintech-advances-financial-close-with-agentic-ai-built-for-finance/), [Trintech blog](https://www.trintech.com/blog/agentic-ai-in-finance-is-here-what-it-actually-means-for-the-financial-close/)).
- **FloQast** — checklist/close-orchestration leader in mid-market, ERP-integrated,
  AI-assisted reconciliation and anomaly detection. Notably, FloQast is publishing
  on the **SOX risks** of AI in accounting rather than only the upside
  ([FloQast](https://www.floqast.com/blog/7-biggest-sox-compliance-risks-of-using-ai-in-accounting-and-what-to-do-about-them)) —
  again, the vendor conversation has moved to control, not capability.
- **Oracle's own close tooling** — this is the most important competitive fact
  for *this* project, because A6.1 puts us downstream of Oracle ERP Cloud. Oracle
  ships Account Reconciliation and Financial Consolidation & Close in EPM, plus
  automated accounting rules and posting profiles in Fusion GL, and there is an
  active ecosystem of agentic layers over Fusion doing bank-to-cash matching,
  subledger-to-GL rolling reconciliation, break explanation and **drafting
  correcting journals with backup routed for approval before posting**
  ([ChatFin on Oracle Fusion agents](https://chatfin.ai/blog/ai-agents-for-oracle-fusion-cloud-financials-complete-automation-intelligence-platform/)).
  Assume the single-agent "propose a correcting JE in Fusion" use case is
  **already commoditised** by the time this ships. Do not make it the MVP's
  headline.
- **Workday** — strong where Workday Financials is the ERP; less relevant here
  given an Oracle base, but relevant as a portfolio-level competitor if the
  studio is ever positioned as ERP-agnostic.

Independent 2026 surveys of the category read consistently: BlackLine and
Trintech own reconciliation, BlackLine and FloQast own close orchestration, and
**agentic capability for journal entry and variance analysis is still emerging
rather than settled** ([Hypatos](https://hypatos.ai/knowledge-base/agentic-ai-month-end-close-automation), [Kognitos](https://www.kognitos.com/blog/top-ai-automation-tools-controllers-accounting-operations-2026/), [Maxima](https://www.maxima.ai/articles/8-best-blackline-alternatives-in-2026-operating-model-comparison)).

### 2.2 Where AI has actually landed vs. where the marketing says it has

**Actually landed (production, boring, works):**
- Transaction matching and auto-certification of low-risk reconciliations —
  rules plus ML, in production for years, not new.
- Anomaly/outlier detection on journal populations. Notably, the *audit* side has
  moved further than the *preparer* side here: testing 100% of journal entries
  rather than a sample is now normal external-audit practice, not aspirational
  ([Weaver](https://weaver.com/resources/second-line-ready-how-to-use-ai-in-sox-compliance-without-over-complicating-it/)).
- Narrative drafting — flux/variance commentary first drafts, exception
  narratives, reconciliation review notes. Low risk because a human rewrites it
  and it does not touch the ledger.
- Document extraction (invoices, bank statements, contracts) feeding accruals.

**Marketed, but thin in practice:**
- "Autonomous close." Nobody credible is running an unattended close. The
  approve-every-write posture in A-write is not conservatism, it is the *actual*
  state of the market, and it is the right call.
- "Agent understands your accounting policy." In practice this is retrieval over
  a policy document plus a prompt. It degrades silently on edge cases —
  precisely the cases that matter at close.
- "Continuous close." Real for high-volume transactional subledgers; largely
  aspirational for judgmental areas (accruals, reserves, impairment triggers,
  revenue cut-off) which are where the close window actually goes.

### 2.3 The narrow gap — where I think this project can be non-generic

Three candidates, in descending order of my confidence:

**(a) The evidence layer, not the work layer — "close the loop the auditor walks."**
The incumbents automate the *work*. Everyone is now converging on trust
messaging, but the concrete artefact an auditor needs — a per-posting dossier
that reconstructs *what the agent saw, what it proposed, on what model and prompt
version, what the human was shown, and what they approved* — is still mostly
promised rather than shipped. Guidance in this space is converging on exactly
this list: a complete trail capturing **prompts, inputs, outputs, model and
configuration versions, and evidence of human review, sufficient to reconstruct
what the AI acted on** ([Ridgeway](https://www.ridgewayfs.com/internal-controls-over-ai-systems-financial-reporting/), [Kognitos audit-trail checklist](https://www.kognitos.com/blog/ai-audit-trail-requirements-2026-checklist/)).
If this product's differentiator is that **the audit package falls out of the
system for free**, that is a controller-buyable claim and it is defensible
against BlackLine, because BlackLine has to retrofit it across a large legacy
surface. See §4.3–4.4.

**(b) The cross-system seam.** The most-cited practitioner complaint in 2026 is
that discrepancies originate *between* systems (CRM ↔ billing ↔ ERP), not inside
any one of them, and single-ERP-scoped tools structurally cannot see them
([Safebooks](https://safebooks.ai/resources/financial-data-governance/financial-close-automation-software-in-2026-what-finance-teams-should-actually-look-for/)).
A6.1 gives this project a **warehouse**, not just the ERP — which means it can
see across sources in a way an ERP-embedded agent cannot. That is a real,
structural advantage and it is currently under-exploited in the intake record.
**Recommendation: make the warehouse vantage point explicit in positioning.**

**(c) Judgmental-area support, not transactional automation.** Transactional
matching is solved and commoditised. The close window is consumed by accruals,
estimates, cut-off and unexplained variance. Support here is *decision support
with evidence*, not autoposting — which fits the human-approval model well.

**What I would advise against as a differentiator:** "we build agents faster /
our builder is friendlier." Ease of composition is not a controllership purchase
criterion, and — see §6 — the builder is a *risk* to be governed before it is a
feature to be sold.

---

## 3 · How the close actually runs (context for `plan-agent` and `functional-agent`)

Approximate day-N shape in a mid/large Oracle shop. Useful for scoping which
agent earns its place first.

| Day | Activity | Automatable today | Where the pain is |
|---|---|---|---|
| −5 to 0 | Pre-close: cut-off comms, accrual data gathering, subledger prep | Partly | Chasing data owners |
| 1–2 | Subledger close, AP/AR/fixed assets, bank recs, intercompany | Largely | Break investigation |
| 2–3 | Accruals, estimates, reserves, manual JEs | Barely | **Judgment; highest risk** |
| 3–4 | GL reconciliation, balance substantiation, review & sign-off | Partly | **Evidence assembly** |
| 4–6 | Consolidation, eliminations, flux/variance analysis, reporting | Partly | Explanation quality |
| Post | Audit support, PBC requests, control evidence | Almost none | **This is the unglamorous gap** |

Two observations for scoping:

1. **Days 3–4 and "Post" are the under-served rows.** They are also where
   controllers, not staff accountants, feel the pain — i.e. where the budget is.
2. A3.2's "11pm on day 3" is not a hypothetical. Day 3 is *exactly* the accrual
   and manual-JE day. The design consequence recorded at intake lands on the
   single highest-judgment, highest-risk row in the table. Take it seriously.

---

## 4 · Compliance and control obligations — the architecture-constraining part

This section is written to be actionable at gates 2 and 6. Each subsection ends
with **Architectural obligation** lines that `solution-architect` and
`security-architect` should treat as requirements input.

### 4.1 SOX / ICFR — what an auditor expects when a *system* helps produce a journal entry

**The threshold question.** If AI influences numbers, estimates, journal entries,
reconciliations or disclosures, **it is inside ICFR scope** — it is not a
productivity tool sitting outside the control environment
([Ridgeway](https://www.ridgewayfs.com/internal-controls-over-ai-systems-financial-reporting/), [Finrep](https://www.finrep.ai/blog/sox-and-ai-controls-the-governance-framework-for-2026)).
Given A-write, this product is unambiguously in scope on day one. There is no
"pilot outside SOX" path available. Plan for that rather than discovering it.

**Does an AI-generated proposal change the control narrative? Yes.** Two changes:

1. **The control's *nature* changes.** A manual preparer control becomes an
   **IT-dependent manual control** — a human judgment that depends on
   system-generated information (the agent's proposal and its supporting
   evidence). That triggers the auditor's standard IPE / "information produced by
   the entity" testing: completeness and accuracy of the data the agent used must
   itself be evidenced. This is the most commonly under-scoped consequence in my
   experience, and it is the one that turns "we added an AI helper" into
   additional audit work.
2. **The control narrative and RCM must name it.** Working guidance is to
   describe AI controls at the **same level of specificity as any other
   significant automated control**; if the AI touches a significant account, its
   existence and nature belong in the process narrative and risk-and-control
   matrix ([Finrep](https://www.finrep.ai/blog/sox-and-ai-controls-the-governance-framework-for-2026)).

**What constitutes adequate evidence of review.** This is where "AI-assisted"
review controls most often fail testing. An auditor testing a review control
looks for evidence of **precision** — that the reviewer knew what they were
reviewing, at what threshold, and what they did about exceptions. A checkbox and
a timestamp is not evidence of review; it is evidence of clicking. Concretely,
auditors expect: human review and approval, **clear thresholds**, access
controls, **change management over the AI configuration**, and **logs showing
what was proposed** ([Kognitos](https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/)).
"The AI said so" is explicitly not sufficient documentation (ibid.).

For this product, adequate evidence of review means the record must show, per
approval: what the agent proposed **and why**, what evidence it relied on, what
the reviewer was actually shown on screen, what thresholds/materiality applied,
whether the reviewer modified or rejected anything, and how exceptions were
dispositioned.

> **Architectural obligation A — the approval record is a first-class artefact.**
> An approval is not a boolean on a row. It is an immutable record containing the
> proposal, its evidence set, the rendered view presented to the approver, the
> approver identity, timestamp, and disposition. Store the *rendered view*, not
> just the underlying data — otherwise you cannot later prove what the human saw.

> **Architectural obligation B — thresholds and materiality must be explicit,
> configurable, versioned, and shown at approval time.** Auditors test against
> stated thresholds. If the threshold lives implicitly in a prompt, it is
> untestable and the control fails.

> **Architectural obligation C — completeness/accuracy of agent inputs must be
> evidenced.** For every proposal, record which warehouse objects and as-of
> extract were used, with a reconciliation back to the ERP source. This is IPE
> support and it will be asked for.

**Direction of travel.** Auditors are being pushed to audit the IT environment
and data reliability more explicitly, with ITGC and controls over AI models in
scope for calendar-2026 audits, and the PCAOB has signalled AI as an **inspection
focus area for 2026 and beyond** ([Houseblend summary of PCAOB direction](https://www.houseblend.io/articles/pcaob-ai-guidance-sox-icfr-audits-netsuite), [PCAOB speech](https://pcaobus.org/news-events/speeches/speech-detail/shaping-the-future---talent-and-artificial-intelligence), [CAQ April 2026 alert](https://www.thecaq.org/public-policy-and-technical-alert-april-2026)).
Translation: the first external audit that encounters this system will be more
curious about it than a 2023-era audit would have been, and the audit team's own
AI-driven journal-entry testing will see every entry this system posts, not a
sample.

### 4.2 Segregation of duties — does "agent prepares, human approves" satisfy SoD?

**Short answer: partially, and not by default. The agent's preparer role needs
its own treatment.** The human's instinct here is right to question it.

SoD assumes three separable roles — **initiation, authorisation, execution** — and
the recognised failure mode with agents is that a single agent can hold all three
at once ([CloudEagle](https://www.cloudeagle.ai/blogs/segregation-of-duties-ai-agents)).
The A-write model already separates authorisation (named human) from initiation
(agent). Good. But two problems remain:

**Problem 1 — the agent must not also hold execution.** If the same agent
identity that prepared the entry is the identity that posts it to Oracle after
approval, initiation and execution are recombined in one non-human principal, and
the human approval sits to the side rather than in the path. The posting must be
performed by a **distinct, separately-credentialed posting service** that will
only act on a cryptographically-verifiable approval record — not by the preparing
agent "continuing" after a green light.

**Problem 2 — an AI cannot serve as the *human* leg of a fraud-deterrence SoD
control.** The distinction that matters: if the control's purpose is *accuracy*
(a second set of eyes catching errors), an AI reviewer can contribute. If the
purpose is *fraud deterrence and mutual human accountability*, AI does not fill
that seat ([FloQast](https://www.floqast.com/blog/7-biggest-sox-compliance-risks-of-using-ai-in-accounting-and-what-to-do-about-them)).
Most JE-approval controls exist for both reasons. So: never design a flow where
an agent is the *only* reviewer of another agent's output on anything that posts.

**Problem 3 — detectability.** A human SoD violation leaves two names in the log;
an agent SoD collapse leaves one (ibid.). Every agent needs a **distinct
non-human identity** with its own entitlements, and agent-to-agent delegation
must be logged as explicitly as human handoffs. If a "team" of agents (the
builder's core feature) can internally re-route work, the SoD analysis must be
performed on **the composed team**, not on each agent in isolation. See §6.

> **Architectural obligation D — agent identity.** Every agent and every composed
> team is a first-class named principal with its own entitlement set, its own
> Oracle credentials (least privilege), and its own log stream. No shared service
> account across agents.

> **Architectural obligation E — preparer/poster split.** Preparation and posting
> are different services with different credentials. The poster's only trigger is
> a valid, signed human approval record.

> **Architectural obligation F — the approver may not be the requester (already
> in A-write) *and* may not be the person who authored or last modified the agent
> that prepared the entry.** This second clause is the one that is easy to miss
> and it is the one the builder makes necessary.

### 4.3 Audit trail — what must be retained, how long, in what form

**How long.** Two distinct clocks, often conflated:

- **The auditor's records** — SEC rule implementing SOX §802, **17 CFR 210.2-06**,
  requires retention of audit/review workpapers and related records for **seven
  years** after conclusion of the audit or review ([eCFR](https://www.ecfr.gov/current/title-17/chapter-II/part-210/subject-group-ECFR2f5dcb24c1c571e/section-210.2-06), [Cornell LII](https://www.law.cornell.edu/cfr/text/17/210.2-06)).
  That is an obligation on the accounting firm, not directly on the company —
  but in practice, anything the auditor relied on, the company is expected to be
  able to reproduce.
- **The company's own records.** Driven by SOX §802's anti-destruction
  provisions, statute of limitations exposure, and internal record-retention
  policy. **Seven years is the safe default design target**; some organisations
  set longer for tax or statutory reasons in specific jurisdictions.

**Design to seven years and make it configurable upward.** Do not assume the
project's own release cadence is relevant — a journal posted in this system's
first month must still be reconstructible in 2033.

**In what form.** Guidance is consistent that logs must be complete, unaltered,
accessible on request, and stored so evidentiary integrity is preserved —
**non-rewritable, non-erasable (WORM-style)** storage is the referenced pattern
([Pathlock](https://pathlock.com/learn/sox-data-retention-requirements/), [Claudia](https://claudiasop.com/blog/compliance-log-retention-requirements.html)).
For a system whose own database also holds mutable operational state, this means
the audit trail cannot simply be a table in the app database that an admin can
UPDATE.

**What must be retained, per posted journal an agent proposed** — my recommended
minimum dossier:

| # | Item | Why |
|---|---|---|
| 1 | The posted entry as posted, plus Oracle's returned document/reference ID | Tie-out to ledger |
| 2 | The agent's proposal, verbatim, including its stated rationale | The "why" |
| 3 | Every input the agent read: warehouse queries, as-of timestamps, source extracts or content hashes | IPE / completeness & accuracy (§4.1 obligation C) |
| 4 | Model identifier **and version**, prompt **version**, tool/config version, retrieval corpus version | Reproducibility (§4.4) |
| 5 | The rendered approval view — what the human actually saw | Evidence of review precision |
| 6 | Approver identity, authentication strength, timestamp, device/surface | Non-repudiation; three surfaces makes this non-trivial |
| 7 | Disposition: approved / modified (with diff) / rejected (with reason) | Exception evidence |
| 8 | Thresholds and materiality in force at the moment of proposal | Testability |
| 9 | Any rollback/reversal, linked bidirectionally to the original | A-write requires rollback |
| 10 | Full agent lineage: which agent/team, which version of its definition, who authored it and when it was last changed | §6 — the builder makes this mandatory |

> **Architectural obligation G — append-only, tamper-evident audit store,
> separate from operational state, retained ≥7 years, exportable in a form an
> auditor can consume without access to the application.** That last clause
> matters: auditors will want an extract, not a login.

> **Architectural obligation H — a reversal is a new record, never a mutation.**
> Rollback must never overwrite or delete the original posting record.

### 4.4 Auditability of the agent itself — **the human is not wrong; this is the underappreciated one**

The human asked whether reproducibility of a decision made three quarters ago is
underappreciated. **You are not wrong. In my assessment this is the single most
likely source of a gate-6 surprise on this project, and it is the obligation
most likely to be discovered late because nothing in normal application
engineering forces you to confront it.**

The problem in one sentence: **an auditor will ask, in Q3 of next year, "show me
why the system proposed this accrual," and the model that produced it may have
been deprecated, the prompt rewritten nine times, and the retrieval corpus
re-indexed — and even if all three were pinned, the same inputs may not yield the
same output.**

That last clause is the genuinely hard part and it is not a solvable-by-logging
problem. LLM outputs vary with sampling parameters, floating-point arithmetic
and infrastructure-level differences even at temperature zero; nondeterminism is
mechanical, rooted in hardware and architecture, not merely a sampling setting
([survey of determinism in financial AI](https://arxiv.org/html/2605.23955), [LLM output drift study](https://arxiv.org/html/2511.07585)).
Reproducibility guidance for regulated use converges on versioning **models,
prompts and data** together, with model name/version pinned for rollback and
drift detection, and prompts versioned because **prompts encode business rules
and compliance constraints** ([Ruksha, Modern Scientist](https://medium.com/the-modern-scientist/reproducible-ai-versioning-models-prompts-and-data-96dd0337af65), [aimultiple](https://aimultiple.com/reproducible-ai)).
The FINOS AI Governance Framework is the most directly applicable industry
control catalogue for financial-services AI and is worth adopting as the
checklist rather than inventing one ([FINOS AIR](https://air-governance-framework.finos.org/)).

**The resolution I recommend, and it should be stated explicitly at gate 2 so
nobody promises the wrong thing:**

> **Do not promise *re-execution* reproducibility. Promise *evidential*
> reproducibility.**
>
> The auditable claim is not "re-run it and you get the same answer." It is
> "here is the exact model version, prompt version, retrieval corpus version,
> input set, and verbatim output that existed at the time, preserved immutably,
> such that the decision can be **reconstructed and explained**, and the human
> approval that authorised it is inseparable from that record."

That is achievable, defensible to an auditor, and honest. The alternative claim
is not achievable and will collapse the first time it is tested.

**Corollary that bites the roadmap:** a model or prompt change is a **change to
an ICFR-relevant control** and needs change management — auditors expect change
management over the AI configuration ([Kognitos](https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/)).
Silently upgrading the underlying model mid-quarter because the provider
deprecated the old one is a control change without a change record. Provider
deprecation schedules are therefore a **compliance** dependency, not just an
engineering one. Flag to `solution-architect` at gate 2.

> **Architectural obligation I — every proposal is stamped with an immutable
> tuple: {model id+version, prompt id+version, tool/config version, retrieval
> corpus version, parameter set}. All four version namespaces are independently
> versioned artefacts under change control.**

> **Architectural obligation J — model/prompt changes go through a documented,
> approved change process with a recorded before/after and an impact assessment,
> and the change record is retained on the same clock as the audit trail.**

> **Architectural obligation K — model deprecation is a tracked risk with a
> defined migration control, not an operational surprise.**

### 4.5 Jurisdictional and framework flags

- **EU AI Act.** My read: an internal financial-close agent is **most likely NOT
  Annex III high-risk**. Annex III's financial entries concern
  **creditworthiness of natural persons** and **risk assessment/pricing in life
  and health insurance** — both about effects on *natural persons*, not corporate
  financial reporting ([Annex III](https://artificialintelligenceact.eu/annex/3/), [Article 6](https://artificialintelligenceact.eu/article/6/)).
  **Three caveats, and they matter:**
  1. If the studio's builder lets an accountant compose an agent that touches
     employee-affecting decisions (expense-claim adjudication, commission
     accruals, anything scoring an individual), the *composed* agent can land in
     Annex III even though the platform did not. **The builder makes
     classification a per-agent runtime question, not a one-time product
     decision.** This is a strong, concrete argument for §6's controls.
  2. Providers whose system falls under an Annex III use case but who assess it
     as not high-risk must **document that assessment before putting it into
     service** ([Annex III / Art. 6 guidance](https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems)).
     So the not-high-risk conclusion is itself a document you must produce and
     keep, not a conclusion you can hold informally.
  3. GPAI and transparency obligations, and the Act's phased application,
     still apply regardless of high-risk status.
  **Action:** `responsible-ai-architect` should own a written classification
  assessment at gate 2, plus a **per-composed-agent classification gate** in the
  builder.
- **PCAOB.** Not directly binding on the company, but shapes what the external
  auditor asks for. AI is an inspection focus for 2026+ (§4.1). Practical effect:
  expect more, not fewer, questions.
- **COSO / NIST AI RMF / ISO 42001.** The framework triad auditors are
  converging on: NIST AI RMF for lifecycle risk, ISO/IEC 42001 for the management
  system, **COSO to connect AI risk to internal control and accountability** —
  and the key operative test is *if a process would fail or materially change
  without the AI, the AI must be governed as a control*
  ([RSM on COSO](https://rsmus.com/insights/services/risk-fraud-cybersecurity/coso-aligns-ai-governance-with-internal-control-guidance.html), [Wolters Kluwer comparison](https://www.wolterskluwer.com/en/expert-insights/key-differences-between-iso-42001-nist-ai-rmf)).
  Auditors will ask for **inventories, risk assessments, validation results,
  monitoring logs and accountability assignments** (ibid.) — note "inventories,"
  which the builder directly threatens (§6).
- **Model risk management (SR 11-7 lineage).** Formally a banking-supervision
  expectation, but its vocabulary — model inventory, independent validation,
  ongoing monitoring, documented limitations — is increasingly borrowed by
  internal audit at non-bank corporates. Assertion from domain knowledge, not
  cited. Worth pre-empting: a model inventory is cheap to build now, expensive
  to retrofit.
- **Data residency / privacy.** Ledger data is generally not personal data, but
  payroll accruals, expense and commission data can be. If the warehouse contains
  any of it, GDPR and cross-border transfer questions attach to whatever is sent
  to a model provider. Route to `security-architect`.

---

## 5 · A7.2 — the delegated harm question, industry/regulatory angle

`functional-agent` answers this from the domain side. Mine is: **what does it
cost in compliance and audit terms, and who is personally on the hook.**

### 5.1 The worst plausible outcome — and why it is not the obvious one

The intuitive worst case is a large wrong journal. It is not the worst case,
because a large wrong journal is loud: it breaks a reconciliation, trips a flux
threshold, and someone finds it.

**The worst plausible outcome is a *systematic, individually-immaterial,
aggregate-material* error that a confidently-worded agent proposal caused a
pressured human to approve repeatedly across several periods.** Concretely: an
accrual agent applies a subtly wrong cut-off or a stale rate. Each month it is
below the individual posting threshold and below the flux commentary threshold.
It is approved at 11pm on day 3 for six consecutive months by a reviewer relying
on the agent's confident rationale. It is caught in Q4 by the external auditor's
100%-population journal testing (§2.2 — the auditors *do* look at everything now).

The escalation from there is mechanical:

1. **Out-of-period adjustment**, then a materiality assessment (SAB 99
   quantitative *and* qualitative — and "caused by an AI control that management
   did not adequately supervise" is a **qualitative** factor that pushes toward
   materiality even at modest amounts; assertion from domain knowledge).
2. **Material weakness in ICFR.** This is the pivot point. Not because of the
   dollar amount, but because the *control failed for six consecutive periods
   and management's review control did not detect it* — which is close to the
   textbook definition of a review control that was not operating at sufficient
   precision. Once you concede the review control was ineffective, you have
   conceded it was ineffective for **everything else it covered**, not just this
   accrual. That is the contagion property that makes this the worst case.
3. **Adverse ICFR opinion / disclosed material weakness**, with the documented
   consequences: negative market reaction, eroded investor confidence, increased
   audit fees from expanded testing, management time diverted to remediation, and
   heightened exposure to legal proceedings and regulatory inquiry ([Moss Adams](https://www.mossadams.com/articles/2025/04/material-weaknesses-in-public-companies), [Baker Tilly](https://www.bakertilly.com/insights/material-weaknesses-in-public-companies), [Pathlock](https://pathlock.com/learn/what-is-a-material-weakness/)).
4. **Possible restatement** if prior periods are affected. Restatement carries
   its own confidence and litigation consequences (ibid.).

### 5.2 What it costs

Ordered by what actually hurts, not by size:

| Cost | Nature |
|---|---|
| Remediation programme | 2–4 quarters of controller-team time; often external consultants |
| Expanded external audit scope | Higher fees, more sampling, more PBC burden — persists for at least a year |
| **Loss of reliance on the whole system** | The auditor stops relying on *every* control this platform touches, not just the broken one. Manual testing replaces automated reliance. **This is the sleeper cost and it can exceed the error itself.** |
| Market/investor reaction to disclosed MW | Documented negative price reaction (§5.1 refs) |
| Restatement, if triggered | Litigation exposure, D&O consequences |
| Internal | Loss of appetite for AI in finance for years — the project's own death, and arguably its most likely one |

### 5.3 Who is personally on the hook

Bluntly, and in order:

1. **The named human approver.** They approved it. In every control narrative,
   in every audit interview, and in every internal post-mortem, the approver
   owns the entry. "The agent proposed it" is not a defence — "the AI said so"
   is explicitly not adequate documentation ([Kognitos](https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/)).
   A4/A7.4 already places accountability there, correctly. **The product must
   therefore treat the approver as someone taking on personal exposure and
   design for their protection, not merely for their throughput.** That is a
   direct product-design consequence, and it should be visible in the UI.
2. **The controller / process owner.** Owns the control's design and operating
   effectiveness. A review control that failed six times is *their* control.
   They are the most likely person to lose a job over this scenario.
3. **The CFO and CEO.** They personally certify under **SOX §302** (disclosure
   and internal-control effectiveness) and **§906** (criminal provision).
   Unintentional errors sit in §302's civil/controls frame; §906's criminal
   exposure requires knowing/fraudulent certification ([CBIZ](https://www.cbiz.com/insights/article/sox-ipo-readiness-internal-control-impact-of-sox-302-and-906-certifications), [DFIN](https://www.dfinsolutions.com/knowledge-hub/blog/what-sox-section-906)).
   Crucially, **this liability cannot be delegated** — not to subordinates, not
   to external auditors ([Daeryun](https://www.daeryunlaw.com/us/practices/detail/sarbanes-oxley-act)),
   and by extension **not to a vendor and not to an agent**. A CFO who signs a
   §302 certification is certifying over controls that include this system.
4. **Nobody at the vendor.** Worth stating plainly. Contractual liability caps
   are the vendor's exposure; the certification exposure stays with the
   customer's officers. Any positioning that implies the platform absorbs
   accountability is both false and dangerous.

### 5.4 What this implies for design — the concrete asks

These are my A7.2 answers expressed as requirements. They should survive to
gate 2.

1. **Calibrated confidence, and the right to say "I don't know."** The harm is
   driven by *confident* wrongness. An agent that expresses uncertainty and
   escalates rather than proposing is worth more than one with a higher
   auto-proposal rate. Measure and report abstention rate as a **positive**
   metric.
2. **Design for the 11pm approval (A3.2).** Assume the approver will not read
   carefully. Therefore: the *default* state of a proposal is not-approved; the
   riskiest element must be the most visually prominent, not buried in a
   rationale paragraph; high-risk items should be *blocked* from bulk approval;
   and an approver's speed relative to their own baseline is itself a monitorable
   signal. **Never build "approve all."** If it exists, it will be used at 11pm
   and it makes the control cosmetic.
3. **Cross-period, cross-entry monitoring.** The worst case is invisible entry
   by entry. The system must detect *its own* recurring patterns — same agent,
   same account, same direction, N periods running, each below threshold — and
   escalate on the aggregate. **I believe this is the single highest-value
   control feature in the product and I have not seen an incumbent ship it
   convincingly.** It is also, not coincidentally, a strong differentiator
   (§2.3a).
4. **Materiality-aware routing.** Approval friction should scale with risk and
   judgment, not be uniform. Uniform friction trains people to click.
5. **Post-approval detectability.** Every posted entry retains its agent lineage
   permanently, so that when one agent is found to be wrong, **every entry it
   ever touched can be enumerated in minutes**. Without this, the blast-radius
   question after an incident is unanswerable, and an unanswerable blast-radius
   question converts a contained error into a scope-wide material weakness.
   Obligation G's lineage field (row 10) exists for this.

---

## 6 · The builder — is it a regulatory problem? **Yes. Plainly, yes — and it is manageable.**

The human asked to be told now rather than at gate 6. So:

**A user-built agent that can post to the ledger, with no change-control record,
is an audit finding. Not "might be" — it is the textbook shape of one.**

### 6.1 Why — the precedent is already well established

This is not a novel AI question. Controllership has been here before, with
spreadsheets and with citizen-developed RPA. Any spreadsheet directly or
indirectly used in financial reporting is **in SOX scope**, and end-user
computing is a recognised, separately-audited risk category with its own control
expectations: **discovery and inventory, risk classification, version control
with change detection, approval workflow for modifications to high-risk files,
and access logging** ([Apparity](https://apparity.com/euc-resources/spreadsheet-euc-risk-blog/sox-compliance-end-user-applications/), [SOX Made Easy EUC audit programme](https://soxmadeeasy.com/spreadsheets_end_user_computing_applications_audit.html), [CIMCON](https://www.cimcon.com/products/euc-insight-change-management), [Mitratech](https://mitratech.com/resource-hub/blog/lowering-spreadsheet-risk-with-euc-audit/)).

**A user-composed agent that proposes journal entries is an EUC.** It is a
user-authored artefact, outside the change-controlled application, that
materially affects financial reporting. The entire EUC control catalogue transfers
to it almost line for line — and it is *worse* than a spreadsheet in two ways: it
acts rather than calculates, and its behaviour is not deterministic (§4.4).

Compounding it: auditors converging on the COSO/NIST/ISO triad expect an **AI
inventory** with named accountability per use case ([RSM](https://rsmus.com/insights/services/risk-fraud-cybersecurity/coso-aligns-ai-governance-with-internal-control-guidance.html)).
A builder that lets any accountant create an agent is, by construction, a machine
for producing **un-inventoried AI systems inside ICFR scope**. That is the finding
in one sentence.

### 6.2 Does it survive an audit? Yes — under conditions

It survives if the builder is designed as a **governed authoring environment**
rather than a free-form tool. My recommended conditions, and I would treat these
as gate-2 architectural requirements rather than gate-3 backlog candidates:

1. **Hard separation of two capability tiers.**
   - **Tier 1 — read/analyse/draft only.** Free composition. No ledger write, no
     posting, no reconciliation close-out. Accountants can build freely here and
     it is genuinely valuable. Light governance.
   - **Tier 2 — anything that can lead to a posting.** A user-built agent
     **cannot acquire write capability by being built**; it acquires it only by
     being **promoted** through a controlled process. This single design decision
     resolves most of the regulatory problem. **My strongest single
     recommendation in this document.**
2. **Promotion = change control.** Promotion to Tier 2 requires: a named owner,
   a documented purpose and scope, defined thresholds, an independent reviewer
   who is not the author, a recorded approval, and a version stamp. That *is* the
   change-control record whose absence would be the finding. Make the system
   produce it as a by-product of promotion so nobody has to write a memo.
3. **Automatic inventory.** Every agent and team, Tier 1 or 2, appears in an
   inventory with owner, tier, version, last change, and (for Tier 2) posting
   volume and error history. Non-optional, non-bypassable, exportable. This is
   the auditor's first request.
4. **Versioning and immutability of definitions.** An agent definition is an
   immutable version. Editing a promoted agent creates a new version requiring
   re-promotion; it never silently mutates a version that has already posted.
   Every posting references the exact definition version (§4.3 row 10).
5. **SoD on authorship.** Per obligation F: the author or last modifier of an
   agent cannot approve that agent's postings. This is the control that stops
   the builder from becoming a self-approval loop, and it is the one an auditor
   will look for the moment they understand what the builder does.
6. **Team composition is itself a governed artefact.** Composing three Tier-2
   agents into a team creates a new principal with a new combined entitlement
   set and a new SoD profile. **Compose the permissions, then re-run the SoD
   analysis on the composition** — do not inherit. A team that internally routes
   work between agents can silently recombine initiate/authorise/execute (§4.2).
7. **Per-composed-agent EU AI Act classification gate** at promotion (§4.5).
8. **Deprecation and kill switch.** An agent can be suspended immediately, and
   every entry it ever proposed enumerated (§5.4.5).

### 6.3 The honest trade-off to put in front of the human

Tier 1 free / Tier 2 promoted **will** feel like friction to the accountant who
wanted to build an agent and use it. That friction is not a UX failure — it is
the control, and it is the same friction that governs a spreadsheet promoted into
the close binder today. The alternative is a product that is genuinely delightful
in a demo and unbuyable by a controller who has ever sat through a SOX walkthrough.

**Recommendation to `plan-agent` for gate 3: ship Tier 1 (build freely,
read/draft only) plus a small set of *pre-built, vendor-change-controlled* Tier 2
posting agents. Defer user-promoted Tier 2 to a later release.** That gives the
product both halves of the shape recorded in the intake ("pre-built agents *and*
a builder") while keeping every ledger-writing agent inside the vendor's own
change control on day one. It is also, conveniently, a much smaller MVP — which
addresses the intake's own recorded scope risk.

---

## 7 · Trend-informed feature suggestions for gate 3

For `plan-agent` to fold into the MVP proposal; the human approves feature by
feature. **Ordered by what a controllership team would actually pay for**, with
the reasoning stated so it can be argued with. `functional-agent` is briefed to
play devil's advocate on these and should.

### Tier A — buy-it-now, differentiating

| # | Feature | Why a controller pays | Evidence base |
|---|---|---|---|
| A1 | **Audit dossier per posting** — one exportable artefact containing all ten items in §4.3, produced automatically | Turns audit-support (the worst row in §3) from weeks of PBC assembly into an export. Directly addresses the gap in §2.3a | §4.1, §4.3; [Ridgeway](https://www.ridgewayfs.com/internal-controls-over-ai-systems-financial-reporting/), [Kognitos](https://www.kognitos.com/blog/ai-audit-trail-requirements-2026-checklist/) |
| A2 | **Cross-period pattern monitor** — detects the system's own recurring sub-threshold entries and escalates on aggregate | The named worst-case defence (§5.1). I have not seen an incumbent ship this convincingly | §5.4.3 |
| A3 | **Risk-graded approval UI** built for 11pm — default not-approved, riskiest element most prominent, no bulk approve on high-risk, structured reject-with-reason | A3.2 is a stated design consequence; it is also what makes the control real rather than cosmetic | §5.4.2; intake A3.2 |
| A4 | **Agent inventory + lineage explorer** — every agent, owner, version, and every entry it ever touched | First auditor request; blast-radius answer after an incident | §6.2.3, §5.4.5; [RSM/COSO](https://rsmus.com/insights/services/risk-fraud-cybersecurity/coso-aligns-ai-governance-with-internal-control-guidance.html) |
| A5 | **Cross-source reconciliation using the warehouse vantage point** — differences originating *between* systems, which ERP-embedded agents structurally cannot see | The most-cited 2026 practitioner complaint; structural advantage from A6.1 | §2.3b; [Safebooks](https://safebooks.ai/resources/financial-data-governance/financial-close-automation-software-in-2026-what-finance-teams-should-actually-look-for/) |

### Tier B — strong, but table stakes rather than differentiating

| # | Feature | Note |
|---|---|---|
| B1 | Flux / variance explanation agent with driver attribution and cited source rows | High persona value (FP&A), low regulatory risk — read-only. Good Tier-1 builder showcase. Commoditising fast |
| B2 | Reconciliation break investigation and explanation (propose only, no auto-close) | Incumbent core competence; needed for credibility, will not win a deal |
| B3 | Accrual proposal agent with explicit uncertainty and mandatory evidence citation | Highest close-window pain (§3 day 2–3), highest risk. Only viable with A1+A3 |
| B4 | Close status / readiness view across the three surfaces | Controller's day-to-day; mobile is genuinely useful *for status*, see C2 |
| B5 | Standing PBC / audit-request responder over the dossier store | Turns A1 into recurring, visible value between closes |

### Tier C — demos well, defer or refuse

| # | Feature | Why defer |
|---|---|---|
| C1 | Free-form user-built agents with posting rights | §6. Defer to post-MVP behind promotion controls |
| C2 | **Approving postings from native mobile** | Consider refusing outright for the MVP. Mobile is the worst possible surface for an evidence-of-review control under time pressure — small screen, low scrutiny, exactly the 11pm scenario. **Recommend: mobile is read/monitor/notify only; approval happens on desktop web.** This narrows the three-surface scope materially and is a *control* argument, not a cost-saving one |
| C3 | "Autonomous close" / auto-post below a threshold | Contradicts A-write; nobody credible runs it (§2.2) |
| C4 | Natural-language ad-hoc ledger querying as a headline feature | Oracle and everyone else has it; not a purchase driver |
| C5 | Agent-reviews-agent as a substitute for human approval | Fails SoD fraud-deterrence leg (§4.2 problem 2) |

**Compliance features that are not negotiable regardless of MVP scope** —
these are not backlog candidates, they are entry conditions for *any* feature
that writes: obligations A–K in §4, plus §6.2 items 1, 3, 4 and 5 if the builder
ships at all.

---

## 8 · Open items I am carrying to later gates

| Item | Owner | Gate |
|---|---|---|
| EU AI Act written classification assessment, plus per-composed-agent gate | `responsible-ai-architect` | 2 |
| Whether the warehouse contains personal data (payroll/commission/expense) → GDPR & provider-transfer analysis | `security-architect` | 2 |
| Immutable/WORM audit store selection and ≥7-year retention design | `solution-architect` | 2 |
| Model-deprecation migration control (§4.4 obligation K) | `solution-architect` | 2 |
| Public vs. private company status of target customer — changes whether §404(b) external attestation applies, and therefore how hard §4.1 bites | Human | 3 |
| Whether mobile approval is in or out (C2) | Human, advised by `ui-ux-designer` | 3 |
| Industry/compliance test suite — **does not exist yet**; to be created during build at the path `test-agent` establishes for suite entry points. Scenarios derive from obligations A–K and §6.2 | `industry-expert` + `test-agent` | 7 |

---

## 9 · Sources

Market and incumbents
- [BlackLine — Agentic Financial Operations, governance and trust gap](https://investors.blackline.com/news-releases/news-release-details/blackline-unveils-agentic-financial-operations-close-ais/)
- [Trintech — agentic AI for the financial close](https://www.trintech.com/news/trintech-advances-financial-close-with-agentic-ai-built-for-finance/) · [Trintech blog — what it actually means](https://www.trintech.com/blog/agentic-ai-in-finance-is-here-what-it-actually-means-for-the-financial-close/)
- [FloQast — 7 biggest SOX compliance risks of using AI in accounting](https://www.floqast.com/blog/7-biggest-sox-compliance-risks-of-using-ai-in-accounting-and-what-to-do-about-them)
- [Hypatos — AI vendors for month-end close 2026](https://hypatos.ai/knowledge-base/agentic-ai-month-end-close-automation) · [Kognitos — top AI tools for controllers 2026](https://www.kognitos.com/blog/top-ai-automation-tools-controllers-accounting-operations-2026/) · [Maxima — BlackLine alternatives, operating-model comparison](https://www.maxima.ai/articles/8-best-blackline-alternatives-in-2026-operating-model-comparison)
- [ChatFin — AI agents for Oracle Fusion Cloud Financials](https://chatfin.ai/blog/ai-agents-for-oracle-fusion-cloud-financials-complete-automation-intelligence-platform/) · [ChatFin — Oracle Fusion with agentic AI 2026](https://chatfin.ai/blog/oracle-fusion-with-agentic-ai-next-gen-finance-platform-in-2026/)
- [Safebooks — what finance teams should actually look for in close automation](https://safebooks.ai/resources/financial-data-governance/financial-close-automation-software-in-2026-what-finance-teams-should-actually-look-for/)

SOX / ICFR / audit expectations
- [Ridgeway — internal controls over AI systems for financial reporting](https://www.ridgewayfs.com/internal-controls-over-ai-systems-financial-reporting/)
- [Kognitos — what your SOX auditor will ask about your AI automation](https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/) · [Kognitos — AI audit trail requirements 2026 checklist](https://www.kognitos.com/blog/ai-audit-trail-requirements-2026-checklist/)
- [Finrep — SOX and AI controls, 2026 governance framework](https://www.finrep.ai/blog/sox-and-ai-controls-the-governance-framework-for-2026)
- [Weaver — using AI in SOX compliance without over-complicating it](https://weaver.com/resources/second-line-ready-how-to-use-ai-in-sox-compliance-without-over-complicating-it/)
- [Houseblend — PCAOB AI direction, SOX & ICFR audits](https://www.houseblend.io/articles/pcaob-ai-guidance-sox-icfr-audits-netsuite) · [PCAOB speech — talent and AI](https://pcaobus.org/news-events/speeches/speech-detail/shaping-the-future---talent-and-artificial-intelligence) · [CAQ — Public Policy & Technical Alert, April 2026](https://www.thecaq.org/public-policy-and-technical-alert-april-2026)

Segregation of duties
- [CloudEagle — why AI agents break segregation of duties controls](https://www.cloudeagle.ai/blogs/segregation-of-duties-ai-agents)
- [SecurEnds — SoD for SOX compliance](https://www.securends.com/blog/segregation-of-duties-for-sox-compliance/)

Retention and audit trail
- [eCFR — 17 CFR 210.2-06, retention of audit and review records](https://www.ecfr.gov/current/title-17/chapter-II/part-210/subject-group-ECFR2f5dcb24c1c571e/section-210.2-06) · [Cornell LII — 17 CFR 210.2-06](https://www.law.cornell.edu/cfr/text/17/210.2-06) · [Federal Register — adopting release](https://www.federalregister.gov/documents/2002/11/27/02-30036/retention-of-records-relevant-to-audits-and-reviews)
- [Pathlock — SOX data retention requirements](https://pathlock.com/learn/sox-data-retention-requirements/) · [Compliance log retention by regulation](https://claudiasop.com/blog/compliance-log-retention-requirements.html)

AI auditability, reproducibility, governance frameworks
- [FINOS AI Governance Framework](https://air-governance-framework.finos.org/)
- [Survey of determinism in financial AI systems (arXiv)](https://arxiv.org/html/2605.23955) · [LLM output drift: cross-provider validation for financial workflows (arXiv)](https://arxiv.org/html/2511.07585)
- [Reproducible AI: versioning models, prompts and data](https://medium.com/the-modern-scientist/reproducible-ai-versioning-models-prompts-and-data-96dd0337af65) · [Reproducible AI — why it matters](https://aimultiple.com/reproducible-ai)
- [RSM — COSO aligns AI governance with internal control guidance](https://rsmus.com/insights/services/risk-fraud-cybersecurity/coso-aligns-ai-governance-with-internal-control-guidance.html) · [Wolters Kluwer — ISO 42001 vs NIST AI RMF](https://www.wolterskluwer.com/en/expert-insights/key-differences-between-iso-42001-nist-ai-rmf)

EU AI Act
- [Annex III — high-risk AI systems](https://artificialintelligenceact.eu/annex/3/) · [Article 6 — classification rules](https://artificialintelligenceact.eu/article/6/) · [Draft Commission guidelines on high-risk classification](https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems)

Liability and consequences
- [CBIZ — SOX 302 and 906 certifications](https://www.cbiz.com/insights/article/sox-ipo-readiness-internal-control-impact-of-sox-302-and-906-certifications) · [DFIN — what is SOX Section 906](https://www.dfinsolutions.com/knowledge-hub/blog/what-sox-section-906) · [Daeryun — SOX compliance and corporate liability](https://www.daeryunlaw.com/us/practices/detail/sarbanes-oxley-act)
- [Moss Adams — understanding and remediating material weaknesses](https://www.mossadams.com/articles/2025/04/material-weaknesses-in-public-companies) · [Baker Tilly — remediating material weaknesses](https://www.bakertilly.com/insights/material-weaknesses-in-public-companies) · [Pathlock — what is a material weakness](https://pathlock.com/learn/what-is-a-material-weakness/)

End-user computing / citizen development precedent
- [Apparity — SOX compliance and end-user applications](https://apparity.com/euc-resources/spreadsheet-euc-risk-blog/sox-compliance-end-user-applications/) · [Apparity — state of citizen development](https://apparity.com/euc-resources/spreadsheet-euc-risk-blog/the-state-of-citizen-development/)
- [SOX Made Easy — EUC applications audit programme](https://soxmadeeasy.com/spreadsheets_end_user_computing_applications_audit.html) · [CIMCON — EUC change management](https://www.cimcon.com/products/euc-insight-change-management) · [Mitratech — EUC audit and spreadsheet risk](https://mitratech.com/resource-hub/blog/lowering-spreadsheet-risk-with-euc-audit/)

---

*Note on sourcing: vendor blogs are cited for market positioning and practitioner
sentiment, not as authority on legal obligation. Regulatory statements are
anchored to primary sources (eCFR, EU AI Act text) or to accounting-firm and
professional-body publications where noted. Points marked "assertion from domain
knowledge" are my professional judgment and should be challenged.*

---
---

# ADDENDUM — Gate 3 re-cut after the 2026-07-31 scope correction

**Author:** `industry-expert` · **Date:** 2026-07-31 · **Gate:** 3 (re-cut)
**Trigger:** the human's scope correction and two-part product direction recorded
at the bottom of `INTAKE.md`. The system is **not** the GL, does **not** own the
close, sits on **warehouse data sourced from Oracle ERP Cloud**, may **trigger**
postings into Oracle, and its job is to **detect and resolve anomalies during a
standard close** through a **natural-language, dataset-scoped, guardrailed
skill interface**.

> **How this relates to §1–§9.** Sections 1, 3, 4.1–4.5, 5 and 6 survive intact —
> they are about controllership, not about reconciliation. Section 2.3 is
> **revised** by §10 below. Section 7's backlog is **partly invalidated** and
> re-cut in §15. Obligations A–K all still bind; §12 states how each changes and
> adds obligations **L–S**. Where §10–§15 and §1–§9 conflict, §10–§15 wins.

---

## 10 · Competitive re-assessment for the corrected product

### 10.1 The single most important new fact: Oracle now ships the Ledger Agent

Since I wrote §2, Oracle Fusion Cloud Financials **Release 26B** has gone GA with
four finance AI agents, one of which is the **Ledger Agent** — and it does
almost exactly what a naive reading of the corrected scope describes.

Per Oracle's own readiness documentation, the Ledger Agent brings *"automated
monitoring and natural language-based inquiry into the general ledger,"* scans
*"financial balances, journals, and transactions in real time to identify and
flag anomalies or issues as they arise,"* with **user-configurable monitoring
prompts** and GenAI narrative explanation of variances, backed by correlated
ledger and subledger data
([Oracle 26B — Ledger Agent](https://docs.oracle.com/en/cloud/saas/readiness/erp/26b/fins26b/26B-fin-wn-f43814.htm), [Oracle 26B Financials What's New](https://docs.oracle.com/en/cloud/saas/readiness/erp/26b/fins26b/26B-fin-wn-t73594.htm), [Kyte on 26B](https://www.kyteconsulting.com.au/insights/oracle-fusion-cloud-financials-release-26b-ai-agents-take-the-helm), [Oracle Fusion Insider — four agents you can use today](https://blogs.oracle.com/fusioninsider/agentic-ai-in-erp-four-agents-you-can-use-today)).

Read that list against the corrected direction: anomaly detection on GL
balances/journals — shipped. Natural-language inquiry over ledger data —
shipped. Variance explanation narratives — shipped. Configurable monitoring —
shipped. **Inside the ERP the customer already pays for, at no incremental
licence decision.**

BlackLine is in the same place from the other side: the **Journals Risk
Analyser** does GenAI anomaly detection and NL querying across manual journal
entries and is explicitly **ERP-agnostic and rapidly deployable**, and BlackLine
now ships a **Variance Anomaly Detection Agent** that detects outliers in real
time and suggests explanations
([BlackLine Journals Risk Analyser](https://www.blackline.com/products/financial-close/journals-risk-analyser/), [BlackLine — AI-powered journal analysis](https://www.blackline.com/about/press-releases/2024/blackline-announces-ai-powered-innovation-for-analyzing-journal-entries/), [BlackLine — expanded agentic capabilities](https://www.blackline.com/about/press-releases/2025/blackline-expands-agentic-ai-capabilities-to-accelerate-future-ready-financial-operations/)).

### 10.2 The plain answer the orchestrator asked for

**Yes — anomaly detection, as a product, is commoditised, and "we detect
anomalies in your Oracle GL" walks directly into the incumbents' strongest
ground.** Worse than crowded: it is *bundled*. Oracle ships it with the ERP.
A feature whose nearest substitute is already installed, already inside the
system of record, and already free at the margin has close to zero willingness
to pay. If MVP1's headline is "we find anomalies," MVP1 has no wedge.

I am stating that as flatly as I can because the human authorised a build and
this is the moment it is cheap to hear.

**But that does not invalidate the project — it relocates the product.** Three
things are true simultaneously:

1. **Detection is now an input, not the product.** Treat anomaly detection the
   way a modern product treats OCR: necessary, unglamorous, not a claim.
2. **One class of detection is genuinely not commoditised** — see §10.3.
3. **The product is the guardrailed, evidenced, cross-dataset *resolution*
   layer** — what happens between "something is wrong" and "a posting exists
   with a defensible control record behind it." Nobody is selling that well, and
   the corrected scope points at it precisely.

### 10.3 The detection class that is NOT commoditised — detection of *omission*

This is the sharpest finding in this addendum and I want it acted on.

Every incumbent detector — Oracle's Ledger Agent, BlackLine's Journals Risk
Analyser, Trintech, FloQast — detects **anomalies in what is present**: an
outlier journal, an unusual balance movement, a variance beyond threshold, a
break in a match. All of them reason over the population of records that exist.

The close's expensive failures are the opposite shape. They are **things that
are absent**:

- the accrual that was booked in each of the last eleven periods and was not
  booked this period;
- the reversal that was scheduled and did not reverse;
- the recurring entry whose upstream feed stopped delivering, so the entry
  silently stopped;
- the intercompany side that one entity posted and the counterparty never did;
- the subledger that closed with a source-system population smaller than the
  period's operational activity implies;
- the cut-off items sitting in a source system that never reached the ERP at all.

A detector that reasons over the ledger **structurally cannot see any of
these**, because the evidence of the failure is not in the ledger. Seeing them
requires (a) a multi-period expectation model built from history and (b) a
vantage point that spans the source systems and the ERP. **The warehouse
provides both. The ERP-embedded agent has neither.**

This is the same structural argument as §2.3(b), but sharpened from a
positioning claim ("we can see across systems") into a capability claim that an
incumbent cannot copy without leaving its own system of record. It also
subsumes §5.4.3's cross-period pattern monitor, which was already my
highest-value control feature.

**Recommendation, and I would build the MVP around this sentence:** *the product
detects what did not happen.* Present-anomaly detection ships too, because
users expect it and it is table stakes, but it is never the headline and it is
never a differentiator in a deck.

### 10.4 Revised §2.3 — where the defensible position now sits

Re-ranked for the corrected product. My confidence order has changed.

| Rank | Position | Status after correction |
|---|---|---|
| 1 | **Omission / expectation-based detection across warehouse + ERP** (§10.3) | **New #1.** Structurally unavailable to ERP-embedded agents. Directly enabled by A6.1 |
| 2 | **The guardrailed action layer** — policy-enforced, evidenced, reversible triggering of postings into Oracle | **New.** This is what the human's Part 2 actually describes. §13 defines it |
| 3 | **The evidence layer / audit dossier** (was §2.3a) | **Unchanged and still strong.** Now *more* important, because when the system does not own the GL, the dossier is the only artefact that explains why Oracle contains what it contains |
| 4 | Cross-system seam (was §2.3b) | **Confirmed, and now the mechanism for #1 rather than a standalone claim** |
| 5 | Judgmental-area support (was §2.3c) | Unchanged, still valid, still hard |
| — | **Present-anomaly detection on GL data** | **Demoted to table stakes.** Ship it; never claim it |
| — | Reconciliation matching / certification | **Out of scope entirely** per the correction |

**One risk I want on the record.** Positions 1 and 4 depend on the warehouse
actually containing non-ERP sources. If the customer's warehouse is a
one-source Oracle replica, the structural advantage evaporates and we are a
worse Ledger Agent with a longer data latency. **This is a hard qualification
question for any pilot customer and it should be in the deployment
prerequisites, not discovered in implementation.** Flagging to
`solution-architect` and to the human as a go-to-market condition.

---

## 11 · Part 1 research — what in a standard close is actually automatable, and by whom

Research-driven backlog input, as asked. The column that matters is the last
one; a "yes" in **Commoditised** means do not lead with it.

| # | Close activity | Automatable today | Commoditised? | Our angle |
|---|---|---|---|---|
| 1 | Outlier/anomaly detection on posted journals and balances | Yes, mature | **Yes — Oracle Ledger Agent, BlackLine JRA** | Table stakes only |
| 2 | Variance / flux explanation narratives | Yes | **Yes — Oracle 26B, BlackLine Variance Anomaly Agent** | Table stakes only |
| 3 | Natural-language ledger inquiry | Yes | **Yes — Oracle 26B** | Interface, not feature |
| 4 | Transaction matching, bank rec, auto-certification | Yes, mature | **Yes — and out of scope per the correction** | Do not build |
| 5 | Intercompany matching and elimination | Yes | **Largely** — crowded vendor field ([Kognitos 2026 review](https://www.kognitos.com/blog/top-ai-tools-intercompany-accounting-eliminations-2026/), [HighRadius](https://www.highradius.com/resources/Blog/agentic-ai-in-intercompany-accounting/)) | Only the *one-sided/never-posted* case (omission, §10.3) |
| 6 | **GL coding / misclassification detection** — entries whose account coding does not fit historical pattern | Yes | **Partly.** Widely described as an AI capability ([DualEntry](https://www.dualentry.com/blog/intercompany-reconciliation), [Xenett](https://www.xenett.com/blog/month-end-close-automation)) but thinly shipped as a governed control | **Yes — build.** Strong fit for warehouse history; needs guardrails since the resolution is a reclass posting |
| 7 | **Balancing / out-of-balance and suspense-clearing ageing** | Yes | Partly | **Yes — build.** Deterministic, high-precision, low-judgment; ideal first action-capable skill |
| 8 | **Omission detection** (missing accrual, unreversed reversal, stopped recurring entry, missing IC side) | Emerging | **No — this is the gap** | **Yes — build. This is the wedge (§10.3)** |
| 9 | **Cross-period sub-threshold accumulation** | Emerging | **No** | **Yes — build.** Also the §5.1 worst-case defence |
| 10 | Warehouse-to-ERP tie-out (does the analysed population equal the ledger?) | Yes | Not marketed at all | **Yes — build. It is also an IPE obligation (§14), so it is not optional** |
| 11 | Accrual proposal / estimate support | Barely | No | Highest value, highest risk. **Defer past MVP1** — §5.1's worst case lives here |
| 12 | Close-task orchestration / checklist | Yes | **Yes — FloQast, BlackLine** | Do not build |
| 13 | Audit/PBC evidence assembly | Almost none | **No** | **Yes — falls out of the dossier for free (§12 obligation G)** |

**Reading of the table.** Rows 7, 8, 9, 10 form a coherent MVP1: they are
mutually reinforcing, they all exploit the warehouse vantage point, none is
commoditised, and the two action-capable ones (7 and 6) are the *least*
judgmental postings in the close — which is exactly where a first guardrailed
action capability should live. Rows 1–3 ship as the interface's baseline
behaviour without being sold.

---

## 12 · Obligations A–K under the corrected scope

**Headline answer to the orchestrator's question 2: your reading is correct, and
I would put it more strongly. The ICFR analysis gets *sharper*, not lighter, and
"we do not own the GL" reduces the compliance surface only in three narrow ways
that do not touch the write path.**

### 12.1 Does not owning the GL reduce the compliance surface?

**Three genuine reductions, all on the build side:**

1. **Book-of-record retention for ledger data is Oracle's**, not ours. Our
   ≥7-year clock (obligation G) attaches to the **decision dossier**, not to a
   copy of the ledger. That is a materially smaller store, not a smaller
   obligation.
2. **Period-close mechanics, balancing enforcement, chart-of-accounts change
   control, and posting integrity are Oracle's controls.** We do not design,
   document or test them. Real savings.
3. **Reversal mechanics are Oracle's.** Obligation H (a reversal is a new
   record, never a mutation) is satisfied by Oracle's own reversal behaviour on
   the ledger side; we retain the linkage.

**Two genuine *increases* that did not exist when we imagined owning the close:**

4. **A cross-system reliance appears.** We now depend on controls we neither own
   nor test — Oracle's journal approval configuration, the warehouse's ETL
   completeness, the source systems' extract integrity. In control language
   these are **complementary user entity controls (CUECs)** and they must be
   published as explicit customer obligations, not assumed. See §14 and §15.
5. **A warehouse-to-ERP reconciliation obligation appears.** An in-ERP agent
   reasons over the system of record by construction. We reason over a *copy*,
   with latency. Proving the copy was complete and accurate as of the moment of
   analysis is now a standing IPE obligation — it is obligation C, promoted from
   a supporting detail to a build-now feature (§11 row 10).

**Net: neutral at best, slightly worse on the evidence side.** Not lighter.

### 12.2 The sharpening you identified — and one you did not

Confirming §4.1's IT-dependent-manual-control point: **an agent that detects an
anomaly and proposes a posting is inside the control narrative for that
posting.** The preparer control becomes IT-dependent, and IPE testing attaches
to everything the agent read. Under AS 1105 the bar on evidence produced by
company information systems rose for fiscal years ending on or after
2024-12-15, with auditors expected to demand stronger walkthroughs and
independent corroboration over IPE reports
([BDO on IPE](https://www.bdo.com/insights/assurance/it-audit-considerations-for-information-produced-by-the-entity-ipe), [Forvis Mazars — IPE readiness, April 2026](https://www.forvismazars.us/forsights/2026/04/ipe-readiness-in-soc-examinations)). Warehouses are called out explicitly as
part of the pipeline whose controls must be considered from origination through
to reporting (ibid.). That lands directly on us.

**The sharpening nobody has raised, and it is the one I most want on the record:**

> **The read-only path is not outside ICFR either.** The instinct will be
> "detection is safe, only postings are in scope." It is wrong. If a controller
> relies on this system's output to conclude *"we ran the anomaly analysis and
> found nothing,"* the system is supplying evidence for a **monitoring/review
> control's conclusion**. A detector that silently missed a population is then a
> **completeness failure in that control** — and it fails in the direction
> auditors most distrust, because a false negative leaves no artefact.
>
> Consequence: **negative assurance is a regulated output.** "No exceptions
> found" is a claim the system must be able to substantiate with population
> coverage, or must refuse to make. This is obligation **R** below and it is why
> §14's dataset-completeness question is not a UX detail.

### 12.3 Obligation-by-obligation disposition

| Obl. | Was | Under corrected scope |
|---|---|---|
| **A** — approval record as first-class artefact incl. rendered view | Binds | **Binds, sharper.** Oracle stores the journal; only we can store *what the human was shown and why*. If we don't, that evidence does not exist anywhere |
| **B** — thresholds explicit, configurable, versioned, shown at approval | Binds | **Binds, and is absorbed into the guardrail model (§13).** Thresholds are one guardrail class, not a separate mechanism |
| **C** — completeness/accuracy of agent inputs evidenced | Binds | **Binds, promoted to a build-now feature.** Now covers dataset selection and warehouse-to-ERP tie-out (§14). The single most-changed obligation |
| **D** — per-agent identity, least privilege, own log stream | Binds | **Binds, extended:** each agent needs its own **Oracle** identity, and postings need a dedicated journal source/category (obligation S) |
| **E** — preparer/poster split | Binds | **Binds, and gets easier.** Oracle is the executor; our posting broker is the only credentialled path. Do not let the analysing agent hold Oracle credentials |
| **F** — approver ≠ requester ≠ agent author | Binds | **Binds unchanged.** Now must be reconciled against Oracle's own approver identity (§14) |
| **G** — append-only tamper-evident store, ≥7 yr, auditor-consumable export | Binds | **Binds, scope narrows to the dossier** (see 12.1 §1). Retention clock unchanged |
| **H** — reversal is a new record | Binds | **Binds; partly discharged by Oracle.** We retain bidirectional linkage |
| **I** — immutable model/prompt/tool/corpus version tuple per proposal | Binds | **Binds, extended** with dataset-version and guardrail-bundle-version (obligation N) |
| **J** — model/prompt change = ICFR change control | Binds | **Binds unchanged, and now covers guardrail policy changes** — a guardrail edit is a control change |
| **K** — model deprecation as tracked risk | Binds | **Binds unchanged** |

**All eleven still bind. None is discharged by not owning the GL.**

---

## 13 · The guardrail model — what a guardrail must be to satisfy an auditor

The orchestrator asked for correction rather than confirmation. Three of the
four working assumptions are right; one is right in intent but wrong in
implementation and would be expensive to build as stated. There are also two
missing.

### 13.1 The four stated assumptions, adjudicated

**(1) "A guardrail is a stated, versioned, testable policy object, not a prompt
instruction." — CORRECT, but incomplete in a way that matters.**

Right, and this is now industry-consensus rather than opinion: deterministic
rules-based enforcement produces the same decision for identical inputs every
time, whereas model-based enforcement can produce inconsistent outputs under
identical conditions — which **breaks audit-trail integrity**, and a
deterministic rules engine is described as the only architecture satisfying
regulator-ready evidence requirements
([MLflow — AI policy enforcement, 2026](https://mlflow.org/articles/what-is-ai-policy-enforcement-a-2026-compliance-guide/)).
FINRA's 2026 Annual Regulatory Oversight Report treats AI agents as a distinct
supervisory category and names *"implementing guardrails to constrain or
restrict AI agent behaviors, actions, or decisions"* as a required supervisory
consideration, alongside narrow scope, explicit permissions, action audit
trails and human checkpoints before execution
([FINRA 2026 — GenAI](https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai), [Snell & Wilmer analysis](https://www.swlaw.com/publication/finras-2026-oversight-report-signals-a-supervisory-reckoning-for-autonomous-ai/), [DLA Piper](https://www.dlapiper.com/en-us/insights/publications/2025/12/finra-flags-generative-ai-risks-and-governance-expectations)).
FINRA does not bind a corporate controllership function, but it is the clearest
articulation of the supervisory expectation and internal audit will borrow it.

**What is missing from the assumption: a policy object needs four more
properties to be auditable** — a **named owner**, an **effective-date range**,
an **executable test fixture** (the case that proves it fires and the case that
proves it does not), and membership in a **versioned bundle** (13.1(4)). A
versioned rule with no owner and no test is a configuration value, not a
control.

**And a structural correction: express guardrails as a capability allowlist
under deny-by-default, not as a list of prohibitions.** A prohibition list is
unbounded and therefore untestable — you can never evidence that it is
complete. An allowlist is finite and enumerable, and "here are the seven actions
this agent may take" is a sentence an auditor can test. This mirrors the
narrow-scope-and-permissions framing in FINRA's report.

**(2) "It must be enforced outside the model — a model asked not to exceed a
threshold is not a control." — CORRECT, and the strongest of the four. Hold
this line.**

The failure mode is documented: prompt-based guardrails fail because
instructions written into the conversation are probabilistic, and real
enforcement lives at the architectural callback layer — callbacks, MCP gateways
and LLM gateways that intercept a request **before it reaches a tool**
([MLflow](https://mlflow.org/articles/what-is-ai-policy-enforcement-a-2026-compliance-guide/)).
The mature pattern is policy-as-code at an authorisation broker, with OPA/Rego
as the reference implementation and **decision logs recording the input, the
decision, the policy version that produced it, and the timestamp**
([Codilime on OPA for AI agents](https://codilime.com/blog/why-use-open-policy-agent-for-your-ai-agents/), [TrueFoundry OPA guardrails](https://www.truefoundry.com/docs/ai-gateway/opa-guardrails), [Petronella — policy-as-code for enterprise AI agents](https://petronellatech.com/blog/policy-as-code-for-enterprise-ai-agents-identity-least-privilege/)).

**Two additions the assumption does not state, both of which are where real
implementations leak:**

- **Enforce at the narrowest point that can enforce, which is the posting/tool
  broker — never the UI.** A guardrail implemented in the approval screen is
  bypassed by the API, by a scheduled run, and by the next surface we add. With
  three surfaces (A5.1) this is not hypothetical.
- **The model must never hold the Oracle credential.** The broker holds it. This
  is obligation E restated as an enforcement property: if the model can call
  Oracle directly, every guardrail is advisory regardless of how it is written.

**(3) "It must produce evidence when it fires AND when it does not." — RIGHT IN
INTENT, WRONG AS STATED, and building it literally would be costly and would
still not satisfy an auditor.**

Two different things are being conflated:

- **(3a) Evidence that the guardrail was in force and was evaluated.** This is
  per-action and cheap: stamp each action with the **policy bundle version/hash
  and the decision ID**, exactly as OPA decision logs do. This is what proves
  *"the control was operating at the time of this transaction."*
- **(3b) Evidence that the guardrail *would have fired* had conditions been
  met.** This is **not** obtainable by logging non-events. Logging "rule 47 did
  not fire" a million times evidences nothing except that the code path ran; it
  is the classic negative-log trap, it will dominate storage, and no auditor
  tests operating effectiveness that way. The correct instrument is a
  **scheduled negative-control test regime**: a fixture suite that deliberately
  presents violating inputs to the *live* policy bundle on a defined cadence
  (at minimum each close, and on every bundle change), producing a dated pass
  record. That is the artefact that evidences operating effectiveness, and it is
  the same shape as any other automated-control test an auditor already accepts.

So: **correct the assumption to "evidence that it was in force per action, plus
a periodic proof that it fires."** That is cheaper *and* more auditable than the
literal version. Note also the useful intermediate mode the tooling supports:
an **audit/shadow mode** that logs what a policy *would have* blocked without
blocking, which is the right way to introduce a new guardrail into a live close
without breaking it (referenced in the OPA/policy-as-code material above).

**(4) "The set of guardrails in force at the time of an action must be
reconstructable later." — CORRECT, and I would strengthen it.**

Strengthen it by making the **bundle**, not the individual rule, the versioned
unit. Auditors reason about "the control environment as it stood on 31 March,"
not about rule 47 in isolation, and a set reconstructed by replaying individual
rule histories is a reconstruction an auditor has to take on trust. Version the
whole policy set as one immutable, hash-addressed artefact; the action record
carries the hash. This also makes obligation J trivially satisfiable — a bundle
diff *is* the change record.

### 13.2 The two missing requirements

**(5) A guardrail must have a defined override path, and the override must be a
first-class control event.** An architecture with no override is not stricter,
it is naive: the close is time-boxed, the day-3 exception will occur, and if
there is no sanctioned override there will be an unsanctioned one — a manual
journal keyed straight into Oracle outside this system, which is worse in every
respect including evidentially. An override must be **dual-authorised** (never
the requester, never the agent's author), **reason-coded from a closed list**
(free text is not analysable), **time-boxed to the action** (never a standing
exemption), and **counted** — override rate per agent, per user and per period
is a monitored metric and a leading indicator that a guardrail is miscalibrated
rather than that the users are wrong.

**(6) Blast-radius guardrails — rate and aggregate-value caps — are mandatory
and nobody builds them.** Every guardrail model I have reviewed constrains the
*individual* action. The §5.1 worst case is an accumulation of individually
compliant actions. The countermeasure is a class of guardrail that is stateful
across a run and across periods: maximum proposals per run, maximum aggregate
absolute value per agent per period, maximum consecutive periods in which the
same agent may touch the same account in the same direction without escalation,
and a hard stop on the agent's total footprint relative to the account's
balance. **This is the direct enforcement expression of §5.4.3, and I regard it
as the single most valuable guardrail in the system** — precisely because it is
the one an incumbent's per-transaction rules engine does not express.

### 13.3 The guardrail taxonomy to build to

Six classes. This is the enumeration I would put in the architecture, and each
class needs its own test fixtures.

| Class | Constrains | Example |
|---|---|---|
| **Scope** | Which datasets, entities, ledgers, periods an agent may read | "Only certified datasets; only the current open period" |
| **Capability** | Which actions exist at all (allowlist, deny-by-default) | "May propose a reclass; may not propose an accrual" |
| **Quantitative** | Thresholds, materiality, tolerance bands (absorbs obligation B) | "Reclass ≤ $25k; anything above escalates to controller" |
| **Temporal** | Close-calendar state, period status, cut-off | "No proposals after period soft-close without controller unlock" |
| **Identity / SoD** | Who may approve what (absorbs obligation F) | "Approver ≠ requester ≠ agent author ≠ dataset owner" |
| **Blast radius** | Stateful, cross-action, cross-period caps (§13.2(6)) | "≤ 20 proposals/run; ≤ $250k aggregate/period; 3rd consecutive same-account entry escalates" |

> **Obligation L — a guardrail is a declarative policy object with a named
> owner, an effective-date range, an executable test fixture proving both firing
> and non-firing, and membership in a versioned bundle. Expressed as a
> deny-by-default capability allowlist, never as a prohibition list, never as
> prompt text.**

> **Obligation M — enforcement happens at a single action/posting broker that
> holds the credentials. The model never holds an Oracle credential and the UI
> is never an enforcement point. Any surface added later inherits enforcement by
> construction, not by re-implementation.**

> **Obligation N — every action carries the guardrail bundle hash and the policy
> decision ID. Operating effectiveness is evidenced by a scheduled negative-
> control test suite run against the live bundle each close and on every bundle
> change — not by logging non-events. New guardrails enter via shadow/audit mode
> before enforcing.**

> **Obligation O — overrides are first-class: dual-authorised, reason-coded from
> a closed list, time-boxed to a single action, never standing, and monitored as
> a rate. No silent bypass path may exist.**

> **Obligation P — blast-radius guardrails (per-run count, per-period aggregate
> value, consecutive-period same-account repetition, footprint vs. account
> balance) are stateful, enforced at the broker, and non-disableable by users.**

---

## 14 · Dataset selection as a control surface

The human's Part 2 lets users select one or more datasets and ask an agent to
act. **This is the highest-risk element of the interface design and it is
currently framed as a convenience feature.** It is an IPE surface.

### 14.1 Is a wrong dataset selection user error or control failure?

**Control failure. This is not a close call, and the framing needs correcting
before it reaches architecture.**

Auditors evaluate control **design** before operating effectiveness. A control
whose effectiveness depends on the user not making a mistake that the system
freely permits is **deficient by design** — the same reasoning that makes an
unlocked spreadsheet an EUC finding (§6.1) regardless of whether anyone actually
broke it. If the system will act on a stale, partial, or unreconciled dataset
because the user picked it from a list, the deficiency is ours.

"User error" is only an available defence where the system made the correct
choice available, made the incorrect choice **unavailable** for action-capable
work, and evidenced which was used.

### 14.2 The design call

**Two tiers of dataset access, mirroring §6.2's Tier 1 / Tier 2 split — the same
control shape, applied to data instead of agents.**

- **Exploration (read/analyse/draft).** Free selection across the warehouse.
  Uncertified datasets are selectable and carry a persistent, non-dismissable
  state: *"not certified — cannot support a posting or a no-exceptions
  conclusion."* This preserves the natural-language, pick-your-data experience
  the human asked for. Most usage lives here and it should feel unconstrained.
- **Action-capable.** A skill that can trigger a posting, or that can emit a
  negative-assurance conclusion, may read **only from certified datasets on that
  skill's allowlist** (a Scope guardrail, §13.3). The user does not assemble the
  population for an action-capable run; the **skill declares it** and the user
  chooses among certified options within it. Free-form dataset assembly and
  action capability never combine.

A **certified dataset** carries, as governed metadata: source system and
extract lineage, as-of timestamp and refresh status, row count and content hash,
reconciliation status against the ERP (tie-out result and date), the certifying
owner, and a version. That metadata *is* obligation C's evidence, and it is
captured by reference rather than re-derived per proposal.

### 14.3 The failure mode that actually bites: under-selection

Over-selection is visible — the agent surfaces noise and the user complains.
**Under-selection is invisible and it is the dangerous one.** An anomaly scan
run over 70% of the relevant population returns a clean result that is
pixel-identical to a clean result over 100%. The user sees "no exceptions." The
controller relies on it. Per §12.2, that is a completeness failure in a
monitoring control, and it leaves no artefact.

**The design answer: every skill declares its expected population, and the
system computes and displays coverage of the selected datasets against that
declaration.** A run below full coverage is permitted — the close is messy and
partial analysis is legitimate — but it is **labelled as partial in the output,
in the dossier, and in any export**, and it is **structurally incapable of
producing a "no exceptions" conclusion.** It can say "no exceptions in the
scanned population, which was 70% of the declared population, missing X and Y."
It cannot say "clean."

That distinction is the whole control. It is cheap to build now and effectively
impossible to retrofit once the output format is established and users have
learned to read it.

> **Obligation Q — datasets are governed catalogue objects with certification
> metadata (lineage, as-of, row count, hash, ERP tie-out status, owner,
> version). Action-capable and assurance-emitting skills read only from
> certified datasets on the skill's allowlist; free-form selection is confined
> to read-only exploration and is visibly marked as non-evidential.**

> **Obligation R — every skill declares its expected population. Every run
> records and displays coverage against that declaration. A run below full
> coverage is labelled partial everywhere it appears and is structurally
> incapable of emitting a negative-assurance ("no exceptions") conclusion.**

---

## 15 · Triggering postings into Oracle — the control narrative, and the trap

### 15.1 The narrative in one paragraph

Our system is a **proposal originator and evidence custodian**; Oracle ERP Cloud
is the **system of record and executor**. The control chain is: certified
dataset (Q) → agent analysis under a versioned guardrail bundle (L–P) → proposal
with rationale and evidence → **named human approval in our product against the
full evidence set** (obligation A) → signed approval record → **posting broker**
(M/E) submits to Oracle under a dedicated identity and journal source (S) →
**Oracle's own journal approval workflow** → Oracle posts and returns a document
ID → dossier closed and sealed (G).

### 15.2 Does Oracle's approval workflow satisfy the human-approval leg?

**It satisfies the *system-of-record* leg. It does not satisfy the
*evidence-of-review* leg, and relying on it alone is the trap. Three reasons.**

**Trap 1 — the Oracle approver sees a journal, not a decision.** Oracle's
approver is shown the entry: accounts, amounts, description. They are not shown
what the agent examined, which dataset version and as-of, what population
coverage the run had, what thresholds were in force, what alternatives were
rejected, or what the model and prompt versions were. §4.1's precision-of-review
standard, and the AS 1105-era IPE expectations in §12.2, are not met by a
journal screen. If Oracle's approval is our only human leg, the honest answer to
"what evidence do you have that the reviewer knew what they were approving?" is
"none that we hold."

**Trap 2 — the approval leg is a customer configuration we do not own.** Oracle
documents that journal approval *"provides a layer of security for posting, for
example, to require a manager to approve the journal entry before posting is
permitted,"* and that AutoPost criteria sets post batches automatically —
*"if journal approval is being used, the batch proceeds through the approval
process after which posting is automatically submitted"*
([Oracle — automatic or manual journal posting](https://docs.oracle.com/en/cloud/saas/financials/25d/faugl/automatic-or-manual-journal-posting.html), [Oracle — create an AutoPost criteria set](https://docs.oracle.com/en/cloud/saas/financials/25b/faigl/create-an-autopost-criteria-set.html), [Oracle — running AutoPost](https://docs.oracle.com/en/cloud/saas/financials/25c/faiac/how-can-i-run-the-autopost-process.html)).
Note the conditional. Oracle further recommends scheduling AutoPost immediately
after Journal Import specifically to prevent editing of imported data — sound
integrity advice that, in a tenant where approval is **not** enabled for our
source and category, means **our proposals post automatically with no human leg
in Oracle at all.**

That is the trap in one sentence: **a control narrative that says "the human
approves in Oracle" is, in some tenants, describing a control that is switched
off — and we would not know.**

**Trap 3 — identity collapse.** Journal Import via a shared integration account
makes every entry from this system look like one service user in Oracle,
destroying obligation D's per-agent attribution and making Oracle's own approver
unable to tell which agent, which run, or which human authorised it.

### 15.3 The call

**Two-key model. Both legs, neither optional.**

1. **In-product approval is the evidence-bearing leg.** Named human, full
   evidence set, rendered view retained (obligation A). This is the leg that
   satisfies precision of review and it is ours.
2. **Oracle's journal approval stays enabled and is the system-of-record leg.**
   We **never** post through a path that bypasses it. Concretely: a dedicated
   **journal source and category** reserved for this system, with journal
   approval **required** for that source, and AutoPost configured so it cannot
   post our source without approval.

The dedicated journal source is worth more than it costs. It makes every entry
this system ever caused enumerable in Oracle with a single query — which is the
blast-radius answer from §5.4.5, obtained on the customer's own ledger rather
than only in our store, and it is the first thing an auditor will ask for once
they understand what the system does.

**Does this simplify our obligations materially? Partly — and precisely where it
does not matter, which is why it reads as more of a simplification than it is.**

- **Genuinely simplified:** execution, balancing, period validation, reversal,
  and ledger retention are Oracle's. We do not build or defend any of it. Real,
  and it should shrink the architecture.
- **Not simplified at all:** every evidence obligation. A–C, G, I and the new
  L–R are untouched. Oracle stores *what* was posted; only we can store *why*,
  *on what data*, *under what policy*, and *what the human saw*.
- **Newly added:** a dependency on controls we do not own. Oracle's journal
  approval configuration, the warehouse ETL's completeness, and the source
  extracts are **complementary user entity controls**. They must be published as
  named customer obligations, **verified at deployment per tenant** (not
  assumed), and re-verified on tenant configuration change. A CUEC that is
  relied on but never checked is a finding waiting for the first audit.

> **Obligation S — postings enter Oracle only through a dedicated journal source
> and category reserved for this system, with Oracle journal approval required
> on that source, under a per-agent Oracle identity. No path may post that
> bypasses either the in-product approval or Oracle's approval. The Oracle-side
> configuration prerequisites are documented as complementary user entity
> controls and verified per tenant at deployment and on configuration change.**

### 15.4 Re-cut backlog for gate 3

Replacing the invalidated parts of §7. Tier A here is my MVP1 recommendation.

| # | Feature | Why | Replaces / relates to |
|---|---|---|---|
| **A1′** | **Omission detector** — missing accrual, unreversed reversal, stopped recurring entry, one-sided intercompany, missing feed | The wedge (§10.3); not commoditised; only possible from the warehouse | New. Subsumes old F9/F10 |
| **A2′** | **Cross-period sub-threshold accumulation monitor** | §5.1 worst-case defence and a real differentiator | Old A2, unchanged |
| **A3′** | **Guardrail engine + posting broker** — six classes (§13.3), bundle-versioned, deny-by-default, override-controlled | This is the product per the human's Part 2; obligations L–P | New, foundational |
| **A4′** | **Dataset catalogue with certification and coverage** | Obligations Q and R; without it, negative assurance is unsupportable | New; discharges obligation C |
| **A5′** | **Audit dossier per action, auto-exported** | §2.3a, obligation G; now the primary evidence artefact since Oracle holds the ledger | Old A1 |
| **A6′** | **Balancing / suspense-clearing agent** as the first action-capable skill | Deterministic, low-judgment, high-frequency — the right place to prove the guardrail model | §11 row 7 |
| **A7′** | **Risk-graded approval UI built for 11pm** | A3.2; the anti-rubber-stamp control. Documented failure mode: reviewers given clear AI explanations **defer more**, not less ([TechTarget](https://www.techtarget.com/searchcio/feature/Human-in-the-loop-shouldnt-rubber-stamp-decisions), [TianPan — the HITL rubber-stamp problem](https://tianpan.co/blog/2026-04-15-human-in-the-loop-rubber-stamp)) | Old A3 |
| **B1′** | GL coding / misclassification detection with reclass proposal | §11 row 6; second action-capable skill, after A6′ proves the model | New |
| **B2′** | Warehouse-to-ERP tie-out reporting | §11 row 10; obligation C made visible to the user | New |
| **B3′** | Present-anomaly detection + NL inquiry | Table stakes. Ship, never lead with it | Demoted from headline |
| **C1′** | Accrual/estimate proposal | Defer past MVP1 — §5.1 lives here | Old B3 |
| **C2′** | Anything reconciliation-matching shaped | **Out of scope** per the correction | Old F6/F7/F8/F11, B2 |

**One anti-recommendation, stated plainly.** The rubber-stamp research above
says explanation quality *increases* deference. That means A7′ cannot be
satisfied by "show the agent's reasoning nicely" — better explanations make the
control weaker, not stronger. The mechanisms that work are volume reduction,
override/rejection-rate monitoring, injected known-error test cases to keep
attention live, and prominence of the *riskiest* element rather than the
*clearest* narrative. Route to `ui-ux-designer` and `responsible-ai-architect`
as a design constraint, because the intuitive design is the wrong one here.

### 15.5 What I cannot decide without the human

Two items only. Everything else in this addendum is an SME call I am making.

1. **Whether target pilot warehouses contain non-Oracle sources** (§10.4). If
   they do not, positions 1 and 4 collapse and MVP1's premise needs rethinking.
   This is a fact about the customer, not a judgement.
2. **Public vs. private company status** (carried from §8) — determines whether
   §404(b) external attestation applies and therefore how hard §12 bites in
   practice. Still open.

---

## 16 · Sources added by this addendum

Oracle capability and posting mechanics
- [Oracle 26B readiness — Ledger Agent for agentic AI-powered GL experience](https://docs.oracle.com/en/cloud/saas/readiness/erp/26b/fins26b/26B-fin-wn-f43814.htm) · [Oracle 26B Financials What's New](https://docs.oracle.com/en/cloud/saas/readiness/erp/26b/fins26b/26B-fin-wn-t73594.htm) · [Oracle Fusion Insider — agentic AI in ERP, four agents you can use today](https://blogs.oracle.com/fusioninsider/agentic-ai-in-erp-four-agents-you-can-use-today)
- [Kyte — Oracle Fusion Cloud Financials 26B, AI agents take the helm](https://www.kyteconsulting.com.au/insights/oracle-fusion-cloud-financials-release-26b-ai-agents-take-the-helm) · [BluePeak — Oracle AI changelog: Fusion agent releases and what they require](https://bluepeakedm.com/oracle-ai-changelog/)
- [Oracle — automatic or manual journal posting](https://docs.oracle.com/en/cloud/saas/financials/25d/faugl/automatic-or-manual-journal-posting.html) · [Oracle — create an AutoPost criteria set](https://docs.oracle.com/en/cloud/saas/financials/25b/faigl/create-an-autopost-criteria-set.html) · [Oracle — how can I run the AutoPost process](https://docs.oracle.com/en/cloud/saas/financials/25c/faiac/how-can-i-run-the-autopost-process.html)

Incumbent anomaly-detection capability
- [BlackLine — Journals Risk Analyser](https://www.blackline.com/products/financial-close/journals-risk-analyser/) · [BlackLine — AI-powered innovation for analyzing journal entries](https://www.blackline.com/about/press-releases/2024/blackline-announces-ai-powered-innovation-for-analyzing-journal-entries/) · [BlackLine — expanded agentic AI capabilities](https://www.blackline.com/about/press-releases/2025/blackline-expands-agentic-ai-capabilities-to-accelerate-future-ready-financial-operations/)
- [Kognitos — top AI tools for intercompany accounting and eliminations 2026](https://www.kognitos.com/blog/top-ai-tools-intercompany-accounting-eliminations-2026/) · [HighRadius — agentic AI in intercompany accounting](https://www.highradius.com/resources/Blog/agentic-ai-in-intercompany-accounting/) · [DualEntry — intercompany reconciliation with AI](https://www.dualentry.com/blog/intercompany-reconciliation) · [Xenett — what to automate in month-end close](https://www.xenett.com/blog/month-end-close-automation)

Guardrails, policy enforcement, agent supervision
- [MLflow — what is AI policy enforcement: a 2026 compliance guide](https://mlflow.org/articles/what-is-ai-policy-enforcement-a-2026-compliance-guide/)
- [FINRA — 2026 Annual Regulatory Oversight Report, GenAI section](https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai) · [Snell & Wilmer — FINRA's 2026 report and autonomous AI](https://www.swlaw.com/publication/finras-2026-oversight-report-signals-a-supervisory-reckoning-for-autonomous-ai/) · [DLA Piper — FINRA flags GenAI risks and governance expectations](https://www.dlapiper.com/en-us/insights/publications/2025/12/finra-flags-generative-ai-risks-and-governance-expectations)
- [Codilime — why Open Policy Agent is the missing guardrail for your AI agents](https://codilime.com/blog/why-use-open-policy-agent-for-your-ai-agents/) · [TrueFoundry — OPA guardrails](https://www.truefoundry.com/docs/ai-gateway/opa-guardrails) · [Petronella — policy-as-code for enterprise AI agents](https://petronellatech.com/blog/policy-as-code-for-enterprise-ai-agents-identity-least-privilege/)

IPE and evidence expectations
- [BDO — IT audit considerations for information produced by the entity](https://www.bdo.com/insights/assurance/it-audit-considerations-for-information-produced-by-the-entity-ipe) · [BDO — understanding and managing IPE in audits](https://www.bdo.com/insights/assurance/understanding-and-managing-information-produced-by-the-entity-in-audits) · [Forvis Mazars — IPE readiness in SOC examinations, April 2026](https://www.forvismazars.us/forsights/2026/04/ipe-readiness-in-soc-examinations) · [Schneider Downs — IPE 101](https://schneiderdowns.com/our-thoughts-on/ipe-understanding-information-produced-by-entity/)

Human-in-the-loop failure modes
- [TechTarget — human-in-the-loop shouldn't rubber-stamp decisions](https://www.techtarget.com/searchcio/feature/Human-in-the-loop-shouldnt-rubber-stamp-decisions) · [TianPan — the HITL rubber-stamp problem](https://tianpan.co/blog/2026-04-15-human-in-the-loop-rubber-stamp) · [Codebridge — where to place approval, override and audit controls in regulated workflows](https://www.codebridge.tech/articles/human-in-the-loop-ai-where-to-place-approval-override-and-audit-controls-in-regulated-workflows)
