# Plan — conclave-finance-studio

**Gate 3 · Plan & Backlog — RE-CUT.** Author: `plan-agent`. Date: 2026-07-31.
**Status**: proposed under standing authorization (`batch_authorized`).
**This document supersedes the previous `PLAN.md` in full.** The prior cut was
invalidated by the scope correction: F6 (matching engine + statement ingestion),
F7 (auto-certification rules), F8 (reconciling-item model) and F11
(certification workspace) were Oracle Account Reconciliation Cloud, not this
product.

Inputs read in full for this pass: `INTAKE.md` (including the scope correction
and product direction at the foot), `PROJECT_CONTEXT.md` Decisions Log,
`knowledge/DOMAIN_KB.md` (§6.2, §9, and §10 in full),
`knowledge/INDUSTRY_KB.md` (§10–§16, obligations now A–S), and the superseded
`PLAN.md`.

**Write set for this pass**: `PLAN.md` only. `FEATURES.md`, `PROJECT_CONTEXT.md`
and `pipeline-state.json` are untouched; the Decisions Log line is owed by the
orchestrator after this gate, not written by me.

---

## 0 · Completeness check — binding decisions this plan was checked against

Every binding decision in the Decisions Log, and how this re-cut satisfies or
conflicts with it. Three entries are new since the superseded plan and are
marked **NEW**.

| Binding decision | Source | How this plan satisfies it |
|---|---|---|
| **NEW — SCOPE CORRECTION: the system is not the GL; do not imitate GL** | Decisions Log 2026-07-31 | Structural. No matching engine, no statement ingestion, no certification workspace, no auto-certification rules, no period-close mechanics, no balancing-enforcement, no chart-of-accounts control. The build sits on warehouse data, emits proposals, and hands execution to Oracle. F6/F7/F8/F11 are deleted, not renamed — see the supersession map in §7.0. |
| **NEW — PRODUCT DIRECTION part 1: research-driven backlog** | Decisions Log 2026-07-31 | The backlog is derived from `DOMAIN_KB` §10.3's 22-activity inventory (A1–A22) and `INDUSTRY_KB` §11's 13-row automatability table, not from a reconciliation assumption. Every build-now feature names its A-number. |
| **NEW — PRODUCT DIRECTION part 2: NL, skill-based interface, datasets selected, action under guardrails** | Decisions Log 2026-07-31 | F39 (certified semantic layer + NL skill invocation), F38 (dataset catalogue + coverage), F36 (guardrail engine + broker). Per `DOMAIN_KB` §10.6: the interface is natural language, **the product is the governance of what the language invokes** — so the NL layer is built as a parameteriser over certified queries, never an author of them. |
| **NEW — MVP1 SCOPED TO ERP DATA ONLY** | Decisions Log 2026-07-31 | The three ERP-only-survivable differentiators are the build-now headline: omission detection (F29), resolution typing + evidence spine (F35/F32/F12/F1), cross-period surveillance (F9). Plus `DOMAIN_KB` §10.4c's post-hoc coding net (F33). §8 is a phase-2 section naming exactly what this deferred, so expansion is planned rather than remembered. |
| **STANDING AUTHORIZATION to build MVP1; trust SME judgement; make assumptions** | Decisions Log 2026-07-31 | Calls made, not returned. Two assumptions are recorded in §9 as reversible. Exactly one item is escalated as genuinely undecidable without the human (§9.1). |
| **Product shape: BOTH** (pre-built agents *and* a builder) | Decisions Log 2026-07-30 | Satisfied by sequence. Pre-built skills ship first; the authoring surface is F16, deferred and visible, gated on obligation F (author ≠ approver ≠ invoker) which `DOMAIN_KB` §10.8 says does not exist yet. Not silently dropped. |
| **Personas: all three** | Decisions Log 2026-07-30 | **Improved, still partial — flagged not glossed.** Staff accountant: F41, F29, F33, F40. Controller: F9, F32, F12, F36 blast-radius caps, F1 export. FP&A: partially served for the first time — F39's NL inquiry over certified, provenance-stamped datasets is a real FP&A surface. Flux driver decomposition (F45) is still deferred. See §7.4 Conflict 1. |
| **Write-back with per-action approval — "the defining decision"** | `INTAKE.md` §A-write | **Now exercised, not dodged.** MVP1 has one Tier 2 feature: F40, a fully-formed reclass journal in Journal Import shape, approved per action in-product (F41) and **exported for human posting — it does not post**. The two-key model (`INDUSTRY_KB` §15.3) is designed in from day one; direct triggering is behind the concrete promotion gate in §7.3. |
| **A7.2 (worst harm) delegated to SMEs** | `INTAKE.md` A7.2 | Answered by `DOMAIN_KB` §6.2. This plan's response is F9 + F32 + F36's blast-radius caps, and those are the items I will not trade. See §4. |
| **A8.3 (MVP slice) delegated to SMEs; `plan-agent` proposes** | `INTAKE.md` A8.3 | This document is the proposal, re-derived from scratch after the correction. |
| **Three surfaces → `solution-architect` non-droppable, mandatory Impact Analysis** | `INTAKE.md` §A5 | Honoured. I do not cut a surface unilaterally: F23 (mobile read/monitor/notify) and F24 (mobile approval) are both on the list with my pre-selection and reasoning attached, for the human to overrule. |
| **`responsible-ai-architect` effectively non-droppable** | Decisions Log | Its obligations are named in §10 and absorbed into no backlog item. It also now owns the `INDUSTRY_KB` §15.4 anti-recommendation: clearer AI explanations increase reviewer deference, so F41 must not be satisfied by prettier reasoning. |
| **Full roster, 14 agents. Test Policy: all suites blocking, no advisory exceptions** | `PROJECT_CONTEXT.md` Active Team | §11's criteria are written to be machine-checkable or evidence-backed. Exit code `3` is not a pass. The criterion the previous plan could not pass has been removed and the removal is documented in §11.0. |
| **Approval-under-pressure (A3.2)** | `INTAKE.md` §A3.2 | F41, and it is scoped per `INDUSTRY_KB` §15.4 as **volume reduction + override-rate monitoring + injected known-error probes**, not as legibility. "Approve all" does not exist at any permission level. |
| **Scope is very wide — the MVP slice is the mitigation** | `INTAKE.md` recorded risks | 17 build-now features against a hard ceiling of 18, with six merges done specifically to get under it (§7.0). Everything else is visible and deferred. |

**Conflicts**: one, and it is partial — persona coverage (§7.4). No binding
decision is contradicted.

---

## 1 · What I am proposing, in one paragraph

**Build a governed resolution layer over Oracle ERP warehouse data, whose
detection headline is what did *not* happen.** The deliverable is: a
deterministic integrity floor that is always right and contains no AI; an
omission detector built on a multi-period expectation model; cross-period
surveillance; resolution typed R1–R6 with a forward disposition recorded from
period 1 and tested next period; all of it invoked through a natural-language
skill interface over certified datasets, enforced by a guardrail engine and an
action broker, and evidenced in an append-only dossier. The one action-capable
output in MVP1 is a reclass journal in Oracle Journal Import shape, approved per
action in-product and **exported for a human to post**.

### The constraint this plan is written against

Oracle Fusion **26B ships a GA Ledger Agent**: real-time anomaly scanning over
balances and journals, configurable monitoring prompts, natural-language
inquiry, GenAI variance narratives — bundled with the ERP the customer already
owns (`INDUSTRY_KB` §10.1, `DOMAIN_KB` §10.6). Both SMEs reached the same
conclusion independently: **if MVP1's headline is anomaly detection, MVP1 has no
wedge, and it loses to a checkbox in a subscription the customer already pays
for.**

So the plan is aimed at the four things that survive an ERP-only, all-Oracle
estate:

| # | What survives | Why an incumbent cannot copy it from where it sits |
|---|---|---|
| 1 | **Omission detection** (`INDUSTRY_KB` §10.3) | The evidence of an absence is **not in the ledger**. A ledger-resident detector reasons over the population of records that exist. Source count is irrelevant to this claim, which is why the ERP-only decision does not damage it. **F29.** |
| 2 | **Resolution typing + evidence spine** (`DOMAIN_KB` §10.2, §10.6(1)) | Every competitor terminates at a scored item in a queue. Nobody models **R2** (data-side fix) or **R5** (handoff) as first-class — and R2/R5 are the *majority* outcome across the inventory. **F35, F32, F12, F1.** |
| 3 | **Cross-period surveillance** (`DOMAIN_KB` §6.2, §10.6(2)) | Invisible in-period by construction, which is why nobody sells it. It is also the only control that addresses the worst harm this system can cause. **F9.** |
| 4 | **The post-hoc coding net** (`DOMAIN_KB` §10.4c) | Oracle's Payables Agent codes invoices pre-post, one document at a time, inside the transaction. We are the net that catches what it let through — post-hoc, ledger-wide, cross-entity, cross-period. Explicitly survives an all-Oracle estate. **F33.** |

**Present-anomaly detection and NL inquiry are table stakes. They ship (F42, F39)
and they are never the headline.** Every feature in §7 carries an explicit
`WEDGE` / `FLOOR` / `TABLE STAKES` mark so this cannot quietly invert later. If a
later gate positions this as "AI anomaly detection for your GL", that is a
loop-back trigger.

---

## 2 · The three framing calls I am making

**(a) The deterministic integrity layer is ranked first despite containing no
AI** (`DOMAIN_KB` §10.5). A1 (warehouse-to-ERP fidelity) is the precondition for
believing any other number the product emits; without it every downstream output
is unfalsifiable. It is also unsold by every competitor, because they sit on the
ERP and do not have the problem. **The most reliable component of this product
contains no AI and the product should say so out loud.** F26 and F28 are
therefore build-now and ranked above everything clever.

**(b) "Balancing", read literally, is worthless and would be actively harmful.**
Oracle will not post an unbalanced journal; a warehouse check of debits =
credits reports a permanent, meaningless green, and *a control that can never
fail trains its reviewer that the whole dashboard can never fail*
(`DOMAIN_KB` §10.5). The real version is the **six boundary checks** the ERP does
not police: A1 warehouse↔ERP, A6 subledger↔GL control account, A7 intercompany
pair imbalance, A8 roll-forward continuity, A9 FX/CTA arithmetic, A10
suspense/clearing residual. F26 covers A1 (+A2 staleness); F28 covers the other
five.

**(c) The interface is natural language; the product is the governance of what
the language invokes** (`DOMAIN_KB` §10.6 verdict). Frontier models score
**17–21% on Spider 2.0** against real enterprise schemas, and a finance user
cannot distinguish a wrong join from a right one by looking at the answer.
**No free-form SQL in MVP1**: F39 exposes a certified semantic/metric layer with
versioned joins and measures, and NL *parameterises a certified query, never
authors one*. This is a hard architectural line, not a phased ambition.

---

## 3 · Tier model and obligation gating — how to read the backlog

- **Tier 1** — read / analyse / draft. Cannot lead to a posting.
- **Tier 2** — **anything that can lead to a posting**, including producing an
  export a human then posts. F40 is Tier 2 even though MVP1 has no direct
  posting path; calling it Tier 1 because the last hop is manual would be
  exactly the self-serving classification an auditor unwinds.

**MVP1 contains exactly one Tier 2 feature (F40). Everything else is Tier 1.**
Tier is a capability class: an agent cannot acquire Tier 2 by being built, only
by being promoted (§7.3 promotion gate).

### 3.1 Obligations A–S — entry conditions, not backlog items

`INDUSTRY_KB` §12.3 confirms **A–K all still bind** under the corrected scope;
none is discharged by not owning the GL. **C is promoted to a build-now
feature.** **L–S are new** (§13–§15).

| Obl. | In one line | Binds at | Gates |
|---|---|---|---|
| **A** | Approval record incl. the *rendered view* the human saw | Tier 1 | F1, F41, F12 |
| **B** | Thresholds explicit, versioned, shown at approval — now absorbed as the guardrail *Quantitative* class | Tier 1 | F36, F41 |
| **C** | Completeness/accuracy of inputs evidenced (IPE) — **promoted to a feature** | Tier 1 | F26, F38 |
| **D** | Per-agent identity, least privilege, own log stream | Tier 1 | F5 |
| **E** | Preparer/poster split; **the model never holds the Oracle credential** | Tier 1 (design) / Tier 2 (enforced) | F36, F40 |
| **F** | Approver ≠ requester ≠ agent author ≠ invoker | Tier 2 hard; Tier 1 once F16 ships | F36, F40, F16 |
| **G** | Append-only, tamper-evident, ≥7 yr, auditor-consumable export | Tier 1 | F1 |
| **H** | A reversal is a new record — partly discharged by Oracle; we retain linkage | Tier 2 | F40 |
| **I** | Immutable version tuple, **extended with dataset version + guardrail bundle hash** | Tier 1 | F2 |
| **J** | Model/prompt **and guardrail-policy** change = ICFR change control | Tier 1 | F2, F36 |
| **K** | Model deprecation tracked with a migration control | Tier 1 start | F2 |
| **L** | Guardrail = declarative policy object: named owner, effective-date range, executable fixture proving firing *and* non-firing, membership of a versioned bundle. **Deny-by-default allowlist, never a prohibition list, never prompt text** | Tier 1 | F36 |
| **M** | Enforcement at a single action/posting **broker** that holds the credentials. **The UI is never an enforcement point** | Tier 1 | F36, F40 |
| **N** | Every action carries bundle hash + policy decision ID; operating effectiveness evidenced by a **scheduled negative-control suite**, not by logging non-events; new guardrails enter in shadow mode | Tier 1 | F36 |
| **O** | Overrides first-class: dual-authorised, reason-coded from a closed list, time-boxed to one action, never standing, monitored as a rate | Tier 1 | F36, F41 |
| **P** | **Blast-radius guardrails** — per-run count, per-period aggregate value, consecutive-period same-account repetition, footprint vs. account balance. Stateful, broker-enforced, non-disableable | Tier 1 | F36 |
| **Q** | Datasets are governed catalogue objects with certification metadata; action-capable and assurance-emitting skills read **only** certified datasets on the skill's allowlist | Tier 1 | F38, F39 |
| **R** | Every skill declares its expected population; every run computes and displays coverage; a partial run is **structurally incapable of emitting "no exceptions"** | Tier 1 | F38, F42 |
| **S** | Postings enter Oracle only via a dedicated journal source + category with Oracle approval required, per-agent Oracle identity; the Oracle-side prerequisites are CUECs verified per tenant | Tier 2 | F40 |

**Consequence for scoping:** A, C, D, G, I, J, L, M, N, O, P, Q, R are
non-negotiable in MVP1 even though only one feature can lead to a posting. That
is why the build-now set is spine-heavy. It is the entry price, not gold-plating
— and `INDUSTRY_KB` §12.2 is explicit that **the read-only path is not outside
ICFR either**: "we ran the analysis and found nothing" is a claim supplied to a
monitoring control, so negative assurance is a regulated output.

---

## 4 · The items that must survive scoping

If the human cuts scope, cut F42, cut F28's FX leg, cut F33 before you touch
these:

1. **F32 — forward disposition.** The most retrofit-hostile item in the whole
   backlog (`DOMAIN_KB` §10.7). The prediction must have been recorded in the
   *prior* period for the test to exist at all. Ship without it and the control
   cannot be added later without a year of dead time.
2. **F12 — disposition capture.** *Not telemetry.* It is the **ground-truth
   factory** (`DOMAIN_KB` §10.9(3)). Anomaly detection has no ground truth for
   "is this an anomaly"; it has ground truth for "was it acted on", and that
   label exists only if the product manufactures it. Ship late and the first
   year of production generates no labels, and gate 8 for every phase-2 feature
   has nothing to test against.
3. **F9 — cross-period surveillance.** `DOMAIN_KB` §7.2.4: *"If exactly one
   safety mechanism survives scoping, make it this one."* Per-action approval is
   structurally blind to the §6.2 failure because no single approval was wrong.
   Its two legs — numeric sub-threshold accumulation and **narrative
   recurrence** — are both mandatory. `DOMAIN_KB` §9 warns the textual leg will
   be dropped as an "implementation detail"; it is the earlier signal and it is
   named here so it cannot be.
4. **F36's blast-radius caps (obligation P).** `industry-expert` calls this the
   single most valuable guardrail in the system, *precisely because an
   incumbent's per-transaction rules engine cannot express it*. Every other
   guardrail constrains an individual action; the worst case is an accumulation
   of individually compliant ones.

---

## 5 · Key design decisions and their trade-offs

### 5.1 Detection without consequence is a notification into a saturated budget

`DOMAIN_KB` §9.3, carried forward unchanged. A detector needs a **state change**,
not a signal: a trip must raise the account's risk grade, revoke auto-pass
eligibility, and surface at the top of the review queue. That is resolution type
**R6**, and it is why F35 (resolution typing) is build-now rather than a phase-2
nicety. Escalating to a controller who has already certified five prior
instances, in the close window, is not a control.

### 5.2 Resolution is the product, and most resolutions are not postings

`DOMAIN_KB` §10.2: **R2 (data-side fix) and R5 (handoff) are the majority
outcome**, and no competitor models them as first-class. Binding on `code-agent`:
if the architecture treats "posting" as the default terminal state of an
anomaly, it mis-models the domain and produces a UI in which **the safe answer
is harder to record than the risky one**. R1 carries a mandatory expiry date;
R5 carries a named owner and a due date; R6 is a control-state change with an
audit record.

### 5.3 Every analysis object is a re-runnable, immutable-run object

From `DOMAIN_KB` §1: late-arriving upstream data invalidates downstream work —
rework, not addition. Any design that models an analysis as a task with a
completion state will be wrong in practice. A run is immutable; a new run
supersedes and never overwrites; an approval attaches to a *specific run* and a
superseding run invalidates it loudly. Design constraint, not a backlog item.

### 5.4 The review surface: the intuitive design is the wrong design

`INDUSTRY_KB` §15.4's anti-recommendation, and it is binding on `ui-ux-designer`
and `responsible-ai-architect` at gate 5: **clearer AI explanations make
reviewers defer *more*, not less.** F41 therefore cannot be satisfied by "show
the agent's reasoning nicely". The mechanisms that work are:

- **volume reduction** — fewer items reaching a human at all;
- **override / rejection-rate monitoring**, per agent, per user, per period,
  read as evidence that a guardrail is miscalibrated rather than that users are
  wrong;
- **injected known-error probes** to keep attention live;
- **prominence of the riskiest element**, not of the clearest narrative.

Hard constraints, unchanged from the superseded plan because the correction does
not touch them: default state is not-approved; **"approve all" does not exist at
any permission level**; rejection is structured; and the **rendered view** is
stored, not merely the underlying data (obligation A). `DOMAIN_KB` §6.3: a
perfect approval log that records who clicked but not what they were shown
documents blame without documenting context, pointed at the most junior person
in the chain.

### 5.5 Dataset selection is a control failure, not user error

`INDUSTRY_KB` §14 — and this is the framing correction I most want carried into
architecture. A control whose effectiveness depends on the user not making a
mistake the system freely permits is **deficient by design**.

- **Exploration tier** — free selection across the warehouse, uncertified
  datasets selectable, carrying a persistent non-dismissable *"not certified —
  cannot support a posting or a no-exceptions conclusion"* state. Most usage
  lives here and should feel unconstrained.
- **Action-capable tier** — the **skill declares** its dataset allowlist; the
  user chooses among certified options within it. Free-form dataset assembly and
  action capability never combine.

**The failure that actually bites is under-selection**, because a scan over 70%
of the population returns a result pixel-identical to a scan over 100%. So:
coverage is computed against a declared expected population and displayed, a
partial run is labelled partial in the output, the dossier *and* the export, and
it is **structurally incapable of emitting "no exceptions"** — it can only say
"no exceptions in the scanned population, which was 70%, missing X and Y". That
distinction is the whole control and it is impossible to retrofit once users have
learned to read the output format.

### 5.6 Warehouse lag is now a first-class product problem

`DOMAIN_KB` §10.1 promotes §5.7: the warehouse is the *only* source now, not one
of two. Every emitted number carries its provenance, extract timestamp and its
**staleness relative to the close clock** — on its face, not in a tooltip. F26's
A2 leg and F38 own this; full architectural resolution is a gate-6 obligation on
`solution-architect`.

### 5.7 Two-key posting, designed in from day one

`INDUSTRY_KB` §15. Our in-product approval is the **evidence-bearing** leg;
Oracle's journal approval is the **system-of-record** leg and satisfies only
that leg. The trap is explicit: Oracle's approval is a *customer configuration
we do not own*, and in a tenant where AutoPost runs without approval enabled for
our source, **our proposals post with no human leg in Oracle at all and we would
not know**. Hence obligation S — a dedicated journal source and category,
approval required on that source, verified per tenant as a CUEC at deployment and
on configuration change. The dedicated source is also the blast-radius answer
obtained on the customer's own ledger: every entry this system ever caused,
enumerable in Oracle with one query.

### 5.8 What is refused, visibly

`DOMAIN_KB` §10.3: **A19–A22 are load-bearing refusals** — estimates/reserves/
impairment (A19), materiality and SAB 99 conclusions (A20), certification and
sign-off (A21), contentious cut-off and technical-accounting conclusions (A22).
A product that automates A1–A18 and *visibly refuses* A19–A22 is one a
controller can take to an audit committee.

**Design consequence, binding on `ui-ux-designer` and `code-agent`:** these must
appear in the product **as refusals**, not as absences. "Not built yet" and "will
never be built" are the same blank screen to a user and opposite answers to an
auditor. There is a refusal surface, and §11 tests for its presence — not merely
for the absence of the capability.

---

## 6 · Template and structure

### 6.1 Recommendation: `genai-chatbot` — and the correction *strengthens* the fit

| Template | Fit |
|---|---|
| **`genai-chatbot`** | **Chosen.** FastAPI backend + Next.js/TypeScript/Tailwind/shadcn frontend. The corrected product's primary surface is a natural-language skill interface with a tool-using LLM backend and a human review surface — which is closer to this template's shape than the withdrawn reconciliation workspace was. |
| `agentic-workflow` | Rejected. Backend-only, and its manifest switches off `ui-ux-designer` and the Experience Design gate. Per `INTAKE.md` A3.2 and §5.4, the review surface **is a control**, and `INDUSTRY_KB` §15.4 makes its design counter-intuitive. A template that disables the Experience gate is disqualifying. |
| `rag-knowledge-base` | Rejected. No document corpus grounds the answers; the ground truth is a warehouse and a certified metric layer, not retrieval. |

**Three caveats on the fit, for `code-agent`:**

1. The chat metaphor is kept for *invocation* and discarded for *output*. A skill
   run returns a structured exception set, a coverage statement and a dossier
   reference — not a prose stream. The template's `POST /chat` smoke test is
   replaced by §11's criteria.
2. **The template has no notion of a policy broker.** `guardrails/` and
   `broker/` are new top-level concerns and the broker is the only component
   that holds an Oracle credential (obligation M).
3. **No template models a governed authoring environment.** F16 (skill
   authoring) is `/enhance-project` work with its own template question and a
   mandatory `solution-architect` Impact Analysis per `INTAKE.md` §A5.

### 6.2 File and module structure for the build-now set

```
backend/
  app/
    main.py                     # FastAPI app, routers, health
    config.py                   # settings; bundle loading (F36)
    catalogue/                  # F38 — obligations C, Q, R
      datasets.py               # certified dataset objects: lineage, as-of, row count, hash, tie-out, owner, version
      population.py             # declared expected population per skill
      coverage.py               # computed coverage; the partial-run flag that blocks negative assurance
    semantic/                   # F39 — obligation Q; NO free-form SQL exists here
      metrics.py                # certified, versioned measures and joins
      resolver.py               # NL -> selection + parameters over certified queries ONLY
      inquiry.py                # NL inquiry (TABLE STAKES leg)
    integrity/                  # F26, F28 — band D. MUST contain no model call (asserted at test)
      fidelity.py               # A1 warehouse vs ERP, by balance / segment / period
      staleness.py              # A2 feed completeness, refresh age vs close clock
      boundaries.py             # A6 subledger<->GL, A7 IC pair imbalance, A8 roll-forward, A9 FX arithmetic, A10 residual
    guardrails/                 # F36 — obligations L, N, O, P, B, J
      policy.py                 # declarative policy object: owner, effective dates, fixture refs
      bundle.py                 # hash-addressed immutable bundle; the versioned unit
      classes/                  # scope, capability, quantitative, temporal, identity_sod, blast_radius
      blast_radius.py           # STATEFUL caps across a run and across periods
      override.py               # dual-auth, closed-list reason codes, time-boxed, counted
      fixtures/                 # negative-control suite: firing AND non-firing case per rule
    broker/                     # F36/F40 — obligation M, E. The ONLY holder of credentials
      decide.py                 # evaluates bundle, emits decision ID, stamps bundle hash
      actions.py                # deny-by-default capability allowlist
    evidence/                   # F1 — obligations A, G, I
      store.py                  # append-only writer; NO update/delete path
      dossier.py                # dossier schema incl. dataset version, bundle hash, coverage, rendered view
      integrity.py              # hash chaining / tamper-evidence
      export.py                 # auditor export, consumable without application login
    versioning/                 # F2 — obligations I, J, K
      registry.py, stamp.py, changelog.py
    identity/                   # F5 — obligation D
      principals.py, inventory.py, lineage.py
    resolution/                 # F35, F32 — the wedge
      types.py                  # R1..R6 as first-class outcomes; R1 expiry, R5 owner+due date, R6 state change
      disposition.py            # forward disposition: expected clearing period REQUIRED to save
      verification.py           # next-period test of the prior period's prediction
    detectors/
      base.py                   # every detector takes a declared population object, never a table name
      omission/                 # F29 — THE WEDGE
        expectation.py          # multi-period recurrence/expectation model
        missing_entry.py        # A5 recurring accrual/allocation/amortisation that did not run
        unreversed.py           # scheduled reversal that did not reverse
        stopped_feed.py         # feed stopped -> entry silently stopped
        one_sided_ic.py         # A7 counterparty side never posted
      crossperiod/              # F9
        accumulation.py         # numeric sub-threshold recurrence; iron-curtain aggregate
        narrative.py            # textual self-restatement detection
      coding/                   # F33 — the §10.4c post-hoc net
        detect.py               # cost centre + within-caption natural account, single LE, single period
        backtest.py             # historical reclass journals as labels; §10.4b bias label MANDATORY
      anomaly/                  # F42 — TABLE STAKES, over certified datasets only
    telemetry/                  # F12 — the ground-truth factory, not telemetry
      disposition_capture.py    # what a human actually did (R1-R6), dwell, evidence expanded, overrides
    export/
      journal_import.py         # F40 — Oracle Journal Import shape; export only in MVP1
      cuec.py                   # obligation S tenant prerequisite checklist + verification record
    refusal/
      registry.py               # A19-A22 declared refusals, surfaced as refusals (§5.8)
    api/
      skills.py, runs.py, exceptions.py, dispositions.py, dossiers.py, catalogue.py, inventory.py
frontend/
  app/
    ask/                        # F39 — NL skill invocation + dataset selection with live coverage meter
    exceptions/                 # risk-graded queue (F41)
    review/[id]/                # F41 approval surface; renders + captures the rendered view
    dispositions/               # F35/F32 — open items, expected clearing periods, missed predictions
    catalogue/                  # F38 — certification status, tie-out result, staleness
    monitors/                   # F9 cross-period escalations, controller-facing
    inventory/                  # F5 agent inventory + lineage explorer
    audit/                      # F1 dossier browse + export
  components/
    review/                     # NO bulk-approve component exists, by construction (§5.4)
    coverage/                   # partial-run banner; "no exceptions" is unrenderable below full coverage
    refusal/                    # A19-A22 refusal cards (§5.8)
tests/
  suites/                       # per-suite run.sh; exit codes 0/1/3/4 per manifest
    functional/ ux/ security/ industry/ responsible-ai/ ...
```

**Five structural rules binding on `code-agent`:**

- `evidence/store.py` exposes **no update or delete path** — not a private one,
  not an admin one. Where the operational database and the evidence store share
  infrastructure, separation is enforced at the storage layer, not by convention.
- **The model never holds an Oracle credential.** `broker/` is the only place a
  credential is resolved. If the model can reach Oracle directly, every guardrail
  is advisory regardless of how it is written (obligation M).
- **`integrity/` contains no model call.** Using an LLM for a checkable
  arithmetic answer is a defect: it makes a falsifiable answer unfalsifiable
  (`DOMAIN_KB` §10.2 band D). Asserted by test, not by review.
- **No SQL string is ever constructed from model output.** `semantic/resolver.py`
  returns a certified-query identifier plus bound parameters, and nothing else.
- **Every detector takes a declared population object, never a table name.** This
  is the phase-2 compatibility seam: adding a non-ERP source in phase 2 must not
  be a detector rewrite (§8).

---

## 7 · Backlog — 17 build-now, 16 deferred, 5 refused. Every item individually approvable.

**How to read this.** Every feature is its own approval. The **Default** column
is a *pre-selection*, not a decision. Nothing has been filtered out: deferred and
recommend-reject items are all here with their reasoning attached so they can be
pulled forward. **Tier** per §3 (1 = read/draft; 2 = can lead to a posting).
**Gated by** lists the obligations from §3.1 that must be satisfied for the
feature to be built at all.

**Mark**, so the commodity is visible at a glance:

- **WEDGE** — differentiated; survives Oracle 26B and an all-Oracle ERP-only estate.
- **FLOOR** — the credibility floor or a control obligation. Not a differentiator,
  not optional. Ranked first anyway.
- **NET** — differentiated only in the specific §10.4c sense (post-hoc,
  ledger-wide, cross-period). Not to be sold as anomaly detection.
- **TABLE STAKES** — ship it, never lead with it.

### 7.0 Supersession map — what happened to the old IDs

| Old | Status |
|---|---|
| F6 matching engine + statement ingestion | **DELETED** — Oracle ARCS. Bank/custodian statements do not arrive in an ERP-sourced warehouse at all (`DOMAIN_KB` §10.1) |
| F7 auto-certification eligibility | **DELETED** — Oracle ARCS |
| F8 reconciling-item data model | **DELETED** as written; its §9.1(a) forward-disposition idea survives and is promoted to **F32** |
| F11 certification workspace | **DELETED** — certification is A21, a load-bearing refusal (§5.8). Its review-surface constraints survive in **F41** |
| F1, F2, F5, F9, F12 | **Retained**, same IDs, re-scoped (F9 absorbs old F10; F12 promoted from telemetry to ground-truth factory) |
| F3 threshold policy | **Absorbed** into F36 as the guardrail *Quantitative* class (obligation B) |
| F4 extract provenance | **Absorbed** into F38's certified dataset catalogue |
| F13 auditor export | **Absorbed** into F1 (same obligation G artefact) |
| F10 narrative recurrence | **Absorbed** into F9 as a mandatory second leg, named so it cannot be dropped |
| F15 policy-cold/exceptions-hot | **Absorbed** into F36 — a guardrail bundle *is* policy approved cold |

Six merges were made specifically to get under the 18-feature ceiling. Each is
named above so nothing was lost silently.

### 7.1 Build now — deterministic integrity floor (band D, contains no AI)

| ID | Feature | Tier | Gated by | Mark | Default | Reasoning |
|---|---|---|---|---|---|---|
| **F26** | **Warehouse-to-ERP fidelity + feed staleness** (A1, A2) — does the warehouse equal the ledger by balance, segment and period; missing batches, partial loads, refresh age vs the close clock | 1 | C, Q | **FLOOR** | **BUILD NOW — rank 1** | The precondition for believing any other number the product emits; without it every downstream output is unfalsifiable. Hard arithmetic ground truth, zero blast radius, and unsold by every competitor because they sit on the ERP and do not have the problem (`DOMAIN_KB` §10.5(1)). Ranked first **despite containing no AI**, deliberately. |
| **F28** | **The five remaining boundary checks** (A6 subledger↔GL control account, A7 intercompany pair imbalance, A8 roll-forward continuity, A9 FX/CTA arithmetic, A10 suspense/clearing residual balance) | 1 | C, Q, R | **FLOOR** | **BUILD NOW** | This is what "balancing" actually means (§2b). All five are boundaries the ERP does not police and all are visible only from the warehouse. A8 in particular catches a closed period having moved and is three lines of SQL that almost nobody runs. Composition of A10 is *not* claimed here — that needs F12's labels. |

### 7.2 Build now — the wedge

| ID | Feature | Tier | Gated by | Mark | Default | Reasoning |
|---|---|---|---|---|---|---|
| **F29** | **Omission detector family** (A5 +) — recurring accrual/allocation/amortisation that did not run; scheduled reversal that did not reverse; entry that silently stopped when its feed stopped; one-sided intercompany. Built on a shared multi-period expectation model | 1 | C, Q, R, G, I | **WEDGE — the headline** | **BUILD NOW** | `INDUSTRY_KB` §10.3: *the product detects what did not happen.* Evidence of an absence is not in the ledger, so a ledger-resident agent structurally cannot see it — and **source count is irrelevant to this claim**, which is why the ERP-only decision leaves it intact. ERP history alone supplies the expectation model. Omission is a real misstatement and is invisible to every detector that looks at what posted. |
| **F9** | **Cross-period surveillance — two mandatory legs**: (i) numeric sub-threshold accumulation, same account/direction across N periods, escalated on the **iron-curtain aggregate**; (ii) **narrative recurrence** — the agent restating its own prior-period explanation | 1 | G, I | **WEDGE** | **BUILD NOW — do not cut** | `DOMAIN_KB` §6.2/§7.2.4 and §10.6(2): invisible in-period by construction, which is why no incumbent sells it; and it is the only control addressing the worst harm this system can cause. Leg (ii) is named explicitly because `DOMAIN_KB` §9 predicts it will otherwise be dropped as an implementation detail — it is the *earlier* signal. |
| **F35** | **Resolution typing R1–R6 as first-class outcomes** — R1 accepted+explained **with a mandatory expiry**, R2 data-side fix, R3 reclass, R4 correcting/accrual journal, R5 handoff with named owner + due date, R6 control-state change | 1 | A, G, I | **WEDGE** | **BUILD NOW** | `DOMAIN_KB` §10.2: **R2 and R5 are the majority outcome and nobody models them as first-class.** Every competitor terminates at a flagged item in a queue. If posting is the default terminal state, the UI makes the safe answer harder to record than the risky one. R6 is also §5.1's answer to detection-without-consequence. |
| **F32** | **Forward disposition** — every disposition records an expected clearing period; the next period tests the prediction against reality; a miss raises the account's risk grade and revokes auto-pass eligibility (R6) | 1 | A, G, I | **WEDGE** | **BUILD NOW — most retrofit-hostile item in the backlog** | `DOMAIN_KB` §9.1(a)/§10.7: converts an unfalsifiable narrative into a falsifiable one, and it is **impossible to retrofit** — the prediction must have been recorded in the prior period. Ship without it and the control cannot exist for a year. A disposition without an expected clearing period must be *unsaveable*, not merely discouraged. |
| **F12** | **Disposition & review-precision capture** — for every flagged item: what the human actually did (R1–R6), how long they spent, what evidence they expanded, what they overrode | 1 | A, G | **WEDGE — enabler** | **BUILD NOW — promoted** | `DOMAIN_KB` §10.9(3): **this is not telemetry, it is the ground-truth factory.** Detection has no ground truth for "is this an anomaly"; it has ground truth for "was it acted on", and that label exists only if we manufacture it. Every phase-2 accuracy claim and every phase-2 gate-8 suite is unfalsifiable without it. It is simultaneously the staff accountant's defence (`DOMAIN_KB` §6.3): it records what they were shown, not only what they clicked. |

### 7.3 Build now — governance, guardrails and the one action

| ID | Feature | Tier | Gated by | Mark | Default | Reasoning |
|---|---|---|---|---|---|---|
| **F36** | **Guardrail engine + action broker** — six classes (scope, capability, quantitative, temporal, identity/SoD, blast radius); **deny-by-default capability allowlist**; hash-addressed immutable **bundle** as the versioned unit; bundle hash + decision ID on every action; shadow/audit mode for new rules; sanctioned override path; **scheduled negative-control fixture suite**; **stateful blast-radius caps** | 1 | B, E, F, J, L, M, N, O, P | **WEDGE (blast radius) + FLOOR** | **BUILD NOW** | This is what "under guardrails" actually requires (`INDUSTRY_KB` §13). Enforced at the broker, **never the UI** — a guardrail in the approval screen is bypassed by the API, by a scheduled run, and by the next surface we add, and A5.1 gives us three surfaces. The model never holds the Oracle credential. Blast-radius caps are the one guardrail an incumbent's per-transaction rules engine cannot express. Operating effectiveness is evidenced by the negative-control suite, **not** by logging non-events. |
| **F38** | **Certified dataset catalogue + coverage** — governed dataset objects (source lineage, as-of, refresh status, row count, content hash, ERP tie-out result, certifying owner, version); per-skill **declared expected population**; computed, displayed coverage; partial runs labelled everywhere and **structurally incapable of emitting "no exceptions"** | 1 | C, Q, R | **FLOOR** | **BUILD NOW** | `INDUSTRY_KB` §14: dataset selection is a **control failure, not user error**, and under-selection is the one that bites because a 70% scan looks pixel-identical to a 100% scan. Also discharges obligation C (promoted) and absorbs old F4's provenance record. Cheap now, impossible to retrofit once users have learned to read the output format. |
| **F39** | **Certified semantic/metric layer + NL skill interface** — versioned joins and measures; natural language **selects and parameterises a certified query, never authors one**; dataset selection with a live coverage meter; NL inquiry over the same layer | 1 | Q, R, I | **FLOOR** (the certified layer) + **TABLE STAKES** (the NL inquiry leg) | **BUILD NOW** | The human's Part 2 surface. **No free-form SQL in MVP1**: frontier models score 17–21% on Spider 2.0 against real enterprise schemas, and a finance user cannot tell a wrong join from a right one by looking at the answer (`DOMAIN_KB` §10.8). The NL layer is the interface; the governance of what it invokes is the product. |
| **F41** | **Risk-graded review & approval surface (desktop web)** — default not-approved; **no "approve all" at any permission level**; riskiest element most prominent; structured reject; **rendered view captured as evidence**; override-rate and dwell surfaced to the controller; injected known-error probes | 1 | A, B, F, O | **FLOOR** | **BUILD NOW** | `INTAKE.md` A3.2's 11pm problem. Scoped per `INDUSTRY_KB` §15.4's anti-recommendation — **volume reduction and override-rate monitoring, not prettier reasoning**, because clearer AI explanations make reviewers defer *more* (§5.4). This is the leg of the two-key model that we own and that Oracle's journal screen cannot supply. |
| **F1** | **Evidence dossier store + auditor export** — append-only, tamper-evident, ≥7 yr; one dossier per proposal carrying the version tuple, dataset version, guardrail bundle hash, decision ID, coverage statement and rendered view; exportable in a form an auditor consumes **without an application login** | 1 | A, C, G, I | **WEDGE** | **BUILD NOW** | With Oracle holding the ledger, **the dossier is the only artefact that explains why Oracle contains what it contains** (`INDUSTRY_KB` §10.4 rank 3). Absorbs old F13: the export is the same obligation-G artefact and splitting them invited dropping the half auditors actually use. |
| **F2** | **Version registry and proposal stamp** — model, prompt, tool/config, corpus, **dataset version and guardrail bundle hash** as independently versioned artefacts; change record on every model/prompt/**policy** change | 1 | I, J, K | **FLOOR** | **BUILD NOW** | Cheap now, near-impossible to retrofit onto dossiers already written. A guardrail edit is a control change (obligation J), so the bundle diff *is* the change record. |
| **F5** | **Agent identity, inventory and lineage** — each agent a named principal with its own entitlements and log stream; auto-inventoried; every artefact any agent version ever touched enumerable | 1 | D, G | **FLOOR** | **BUILD NOW** | The inventory is the auditor's first request; lineage is the blast-radius answer, and an unanswerable blast-radius question converts a contained error into a scope-wide material weakness. Pairs with obligation S's dedicated Oracle journal source, which gives the same answer on the customer's own ledger. |
| **F40** | **Reclass proposal → Oracle Journal Import export** — a fully-formed journal in Journal Import shape, per-action approved in-product, **exported for a human to post; MVP1 does not post**. Includes the dedicated journal source/category design and the per-tenant CUEC verification checklist | **2** | A, B, E, F, H, L–P, **S** | **FLOOR** (this is how value lands) | **BUILD NOW** | `DOMAIN_KB` §10.7: not because writing is wrong — the human is explicit that we trigger postings — but because of the wholesale property: an agent with a wrong mapping does not err once, it errs **400 times in ninety seconds** through exactly this path. **Concrete promotion gate, so this is a step and not a hedge:** direct triggering of R3 postings is enabled once F12 shows one full closed period at **≥95% precision on accepted reclass proposals**, with a per-batch line cap and **batch-level, not line-level, approval** (400 individual approvals is not a control). |

### 7.4 Build now — the post-hoc coding net, and table stakes

| ID | Feature | Tier | Gated by | Mark | Default | Reasoning |
|---|---|---|---|---|---|---|
| **F33** | **GL coding anomaly detection + reclass backtest evidence** (A11) — scoped to **cost-centre and within-caption natural-account reclasses, single legal entity, single period**. Legal-entity/IC and opex/capex **excluded**; cut-off **detect-only**. Backtested against historical reclass journals on a held-out period | 1 | C, Q, R, I, B | **NET (§10.4c)** — *not* a wedge on its own | **BUILD NOW** | The only feature in the inventory whose accuracy can be **measured before shipping** (`DOMAIN_KB` §10.4b), and its resolution R3 is the safest posting that exists. It survives an all-Oracle estate as the **post-hoc, ledger-wide net that catches what Oracle's pre-post Payables Agent let through** — a different job from single-document classification. **Mandatory caveat in the test-evidence schema, not a footnote:** reclass journals record only the errors someone *caught*, so recall is blind to the `DOMAIN_KB` §6.2 class and must be reported as *"recall against caught errors"*. Excluded sub-types have tax/transfer-pricing and restatement-grade blast radius (§10.4a) and stay out until precision is measured. |
| **F42** | **Present-anomaly detection over certified datasets** — balance-movement and journal outliers | 1 | Q, R, I | **TABLE STAKES** | **BUILD NOW — and this is the first thing I would cut** | Users expect it and its absence reads as a gap, so it ships. It is **bundled inside Oracle 26B**, so it is never the headline, never in a deck, and never a claim (`INDUSTRY_KB` §10.2). Scoped to the smallest credible version, over certified datasets only, subject to obligation R. If scope bites, cut this before anything in §7.1–§7.3. |

**Build-now total: 17.** Ceiling was 18. The previous cut was 13 features and
`functional-agent` estimated it at 9–12 months — this set is larger in count but
has lost the matching engine, statement ingestion and certification workspace,
which were the three heaviest items in it.

### 7.5 Deferred — default OFF, all visible, all pullable-forward

| ID | Feature | Tier | Gated by | Mark | Default | Reasoning |
|---|---|---|---|---|---|---|
| **F43** | **Unposted / incomplete accounting detector** (A3) — SLA entries left in Draft, unaccounted transactions, untransferred batches | 1 | C, Q | FLOOR | **LATER** | Deterministic and cheap. Deferred purely on the count ceiling: it is a *known* gap, loudly visible at close already, so it is the lowest-value deterministic check. Cheapest item to pull forward. |
| **F44** | **Accrual completeness / unrecorded-liability search** (A13) — subsequent disbursements, received-not-invoiced, open PO receipts | 1 | C, Q, R, I | WEDGE-adjacent | **LATER — phase 2 rank 1** | High value and completeness errors are the top restatement category. Deferred because its resolution is R4 (numbers change), its ground truth is retrospective, and it needs F12's labels first. |
| **F45** | **Flux detection + driver decomposition** (A14) — which accounts moved and which transactions/segments explain the move **arithmetically**. Read-only, no narrative | 1 | C, Q, R | FLOOR | **LATER** | Deterministic and genuinely useful, and it is the FP&A persona's feature (§7.6). Deferred over F29/F9; it is the item to pull forward if persona coverage matters more to you than depth. |
| **F14** | **Fresh-eyes re-derivation** — periodic forced re-derivation of an aged item **by a different derivation path** | 1 | G, I | WEDGE | **LATER** | F9 *detects* the §6.2 pattern; this *breaks* it. `DOMAIN_KB` §9.2 is emphatic: re-deriving with the same model and prompt and a suppressed context is **the same eyes with amnesia**, and its agreement gets filed as corroboration — strictly worse evidence than one opinion. Needs a different model, a deterministic check, or a human. Needs ≥2 periods of history, which MVP1 will not have at launch. |
| **F16** | **Skill authoring (Tier 1 only)** — users compose read/draft-only skills; no action capability of any kind | 1 | D, F, G, I, J, L, Q | — | **LATER — first `/enhance-project`** | The second half of the BOTH product decision, not dropped. Gated on **author ≠ approver ≠ invoker**, which `DOMAIN_KB` §10.8 states does not exist yet. Whoever defines a skill's dataset scope and thresholds is an *author* with more effective control than either preparer or approver. |
| **F17** | **Direct triggering of R3 postings into Oracle** | **2** | all A–S | — | **LATER — behind the §7.3 promotion gate** | Not a hedge: the gate is numeric and stated (≥95% precision over one closed period, per-batch line cap, batch-level approval). |
| **F18** | **User-promoted Tier 2** — promotion workflow granting a user-authored skill action capability | **2** | all A–S | — | **LATER** | Promotion *is* the change-control record whose absence would be the audit finding. Cannot exist before F16 and F17. |
| **F20** | **Long-tail onboarding** — the few hundred entity-specific accounts no close platform templated, onto the same spine | 1 | A, C, F, G, I, Q | WEDGE | **LATER** — *my most contestable deferral* | `DOMAIN_KB` §7.3 opening (1): lands in the gap between the platform and the spreadsheet, needs no displacement and no SOX re-baselining. `DOMAIN_KB` §9.5 correctly identifies it as F16 under another name, so it inherits obligation F. Worth arguing about. |
| **F22** | **Accrual / estimate proposal** (A19-adjacent) | 1 → 2 | all A–S if it posts | — | **LATER — recommend not before F12 labels + F17** | Strongest commercial pull *and* the top statistical cause of restatement, with no in-period ground truth. It is `DOMAIN_KB` §6.2 in its purest form. Listed because the pull toward it will be strong and it should be resisted deliberately, not by omission. Note the boundary: proposing an accrual is not A19 (booking an estimate); the line must be re-drawn explicitly when this is picked up. |
| **F23** | **Native mobile: read / monitor / notify only** | 1 | A, G | — | **LATER** | The honest use of the third surface for the controller. Deferred to keep MVP1 at one surface — not because the surface is wrong. |
| **F24** | **Approving from native mobile** | 1 (→2) | A, B, F, O | — | **RECOMMEND REJECT** | Mobile is the lowest-scrutiny approval surface that exists and A3.2's 11pm scenario is exactly where it would be used. A control argument, not a cost one. Shown, not filtered — yours to overrule. |
| **F25** | **Standing PBC / audit-request responder** over the dossier store | 1 | G | WEDGE-adjacent | **LATER** | Falls out of F1 nearly for free (`INDUSTRY_KB` §11 row 13) and creates visible value *between* closes. Not needed to prove anything MVP1 must prove. |
| **F46** | **Flux narrative drafting** (A15) | 1 | C, I | TABLE STAKES | **RECOMMEND REJECT for MVP1** | `DOMAIN_KB` §9.4: the second-most-dangerous item on any list it appears on. Band G, no ground truth, and its product becomes *management's stated explanation of results* in the close pack and audit-committee deck. Low ledger risk, **high representation risk**. Also shipped in Oracle 26B. |
| **F47** | **Duplicate / near-duplicate detection** (A4) | 1 | Q, R | TABLE STAKES | **RECOMMEND REJECT** | Owned by the ERP, the recovery-audit industry and every AP vendor, with a **30–50% false-positive rate** — spending the scarce attention budget on the least differentiated thing we could ship. |
| **F48** | **Journal-entry risk scoring** (A12) | 1 | Q, R, I | TABLE STAKES | **RECOMMEND REJECT** | MindBridge's product, aimed at a **different buyer** (internal/external audit, not the controller's close team) and a different moment. Weakest ground truth in the L band. Building it walks into their product with their buyer. |
| **F49** | **Close task / checklist orchestration** (A17) | 1 | — | TABLE STAKES | **RECOMMEND REJECT** | FloQast's core product. Choosing a fight over the one part of close that is already solved. |

### 7.6 Load-bearing refusals — A19–A22

These are **not** unbuilt backlog items. They are a stated design property, and
per §5.8 they appear in the product **as refusals**, with §11 testing for the
presence of the refusal rather than the absence of the capability. *"Not built
yet" and "will never be built" are the same screen to a user and opposite
answers to an auditor.*

| A# | Refused | Why |
|---|---|---|
| **A19** | Estimates, reserves, allowances, impairment, valuation | Top restatement cause; no in-period ground truth; the purest form of the §6.2 mechanism |
| **A20** | Materiality / SAB 99 / iron-curtain conclusions | An agent that concludes "immaterial" has automated the decision that suppresses its own errors |
| **A21** | Certification and sign-off | The signature *is* the control; automating it removes the thing being evidenced |
| **A22** | Contentious cut-off and technical-accounting conclusions | No ground truth. May be *supported* by F44/F45 output, never concluded |

Also refused outright, carried forward: **auto-post below a threshold /
"autonomous close"** (contradicts §A-write); **agent-reviews-agent as a
substitute for human approval** (fails the fraud-deterrence leg of SoD); and
**free-form NL-to-SQL over arbitrary datasets** (§2c).

### 7.7 Conflict 1 — persona coverage (raised, not resolved)

The Decisions Log binds all three personas as primary. This cut serves the staff
accountant (F41, F29, F33, F40) and the controller (F9, F32, F12, F36, F1) fully,
and the FP&A analyst **partially for the first time** — F39's NL inquiry over
certified, provenance-stamped datasets is a genuine FP&A surface, which the
superseded plan did not have. Full FP&A coverage needs F45 (flux driver
decomposition), which I default to later.

That is still a partial departure from a binding decision. The remedy, if you
want it closed now, is to switch **F45** to build-now — *not* F46, which is the
dangerous one wearing the same clothes.

---

## 8 · Phase 2 — what the ERP-only decision defers

Named here so expansion is planned rather than remembered. Each item states the
seam MVP1 must leave open, because the point of writing this now is that phase 2
must not be a rewrite.

| # | Deferred by the ERP-only decision | Seam MVP1 must leave open |
|---|---|---|
| **P1** | **Cross-source omission detection** — cut-off items sitting in a source system that never reached the ERP; a subledger that closed with a source population smaller than operational activity implies | F29's expectation model keys on an **expected event**, not on a GL table. `detectors/base.py` takes a declared population object, never a table name (§6.2 rule 5) |
| **P2** | **Non-ERP expectation inputs** — procurement, contracts, HR, operational volumes as evidence of what *should* have posted. `DOMAIN_KB` §10.6(3) calls this the scope no single ERP module sees | F38's catalogue is source-agnostic: a certified dataset carries lineage and tie-out status, not an assumption that its source is Oracle |
| **P3** | **The cross-system seam as headline positioning** (`INDUSTRY_KB` §10.4 rank 4) | Nothing in MVP1's copy or UI may claim single-source coverage as completeness. Obligation R's coverage statement is the mechanism |
| **P4** | **Heterogeneous / post-acquisition / multi-ERP estates** — `DOMAIN_KB` §10.6's targeting instruction names this as the strongest market condition | The broker abstracts the ERP; a second ERP is a second broker adapter and a second CUEC checklist, not a detector change |
| **P5** | **Warehouse-vs-ERP fidelity as a *differentiator*** | It stays in MVP1 as F26, the credibility floor. The claim is deferred, the capability is not |
| **P6** | **A10 residual *composition*** (as opposed to balance) — §6.2's home address | Needs F12's labels. F28 ships the balance leg only; the composition leg is a phase-2 detector over the same boundary object |
| **P7** | **Bank / custodian statements** | Structurally out of reach from an ERP-sourced warehouse and out of scope regardless (`DOMAIN_KB` §10.1). If a treasury source appears in phase 2 it enters as a certified dataset — **still not a matching engine** |
| **P8** | **A7 intercompany *cause* diagnosis** | MVP1 ships the imbalance number (F28) and the one-sided case (F29). Cause has no ground truth and waits for labels |

**Deployment prerequisite created by this, for `solution-architect` and
go-to-market:** `INDUSTRY_KB` §10.4 flags that a one-source Oracle replica
warehouse is the weakest case. MVP1 is deliberately built to survive it via the
four items in §1 — but the presence of non-Oracle sources is a **qualification
question for any pilot customer**, belonging in deployment prerequisites rather
than being discovered in implementation.

---

## 9 · Calls made under standing authorization, and the one escalation

The human authorized MVP1 and asked that SME judgement be trusted. So the calls
below are **made**, not returned. Each is recorded here so it is reviewable
after the fact, and each states what would reverse it.

### 9.1 The one genuine escalation — public vs. private filer

**This is the only item I cannot decide, because it is a fact about the customer
rather than a judgement.** `INDUSTRY_KB` §15.5 carries it too, and it has been
open since gate 1.

§404(b) external auditor attestation on ICFR applies only to public filers, and
not to all of them. It determines how hard the whole obligation surface bites.
**I have built on the public-filer assumption**, because it is the harder floor
and because there is no "pilot outside SOX" path once postings are in play. If
the target is private or non-accelerated, a reasonable person would trade some
of F1/F2/F5 for reach — likely F45 and F44 pulled forward.

Note the asymmetry, so "private" is not misread as "safer": restatements are
concentrated in smaller, non-accelerated filers. Private is the lower
*compliance* floor, not the lower *risk* floor.

**No build decision is blocked on this.** It changes the deferred/build-now
split at the margin, not the spine.

### 9.2 Calls I have made (assumptions, reversible)

| # | Call | Basis | What would reverse it |
|---|---|---|---|
| **A1** | **MVP1 exports rather than posts.** One Tier 2 feature, terminating in a Journal Import file | `DOMAIN_KB` §10.7's wholesale-error argument, with a numeric promotion gate so it is a step and not a hedge | F12 showing ≥95% precision over one closed period → F17 |
| **A2** | **One surface: desktop web.** F23 mobile read/monitor/notify deferred; F24 mobile approval recommend-reject | Mobile is the lowest-scrutiny approval surface and A3.2 describes exactly when it would be used. `INTAKE.md` A5's three surfaces are honoured as a roadmap, not cut | Human overrules F23/F24 defaults — both are on the list for exactly that purpose |
| **A3** | **Coding detection scoped to cost-centre and within-caption natural account, single LE, single period** | Excluded sub-types carry tax/transfer-pricing and restatement-grade blast radius (`DOMAIN_KB` §10.4a) | Measured precision from F33's backtest |
| **A4** | **Cut-off is detect-only**, not proposal-generating | It is a real misstatement class and structurally the same query shape, but its resolution is a period-move, not a reclass | Same as A3 |
| **A5** | **Present-anomaly detection ships but is marked as the first thing to cut** | `INDUSTRY_KB` §10.2: bundled inside Oracle 26B, close to zero willingness to pay | Nothing — it ships either way; only its priority is at stake |
| **A6** | **Six merges to hit the ≤18 ceiling** (§7.0) | The 13-feature previous cut was estimated at 9–12 months before guardrails existed | Human un-merges any of them; each is named so that is possible |
| **A7** | **The A19–A22 refusals are a shipped surface, not an absence** | `DOMAIN_KB` §10.3: a product that visibly refuses them is one a controller can take to an audit committee | Not reversible in my view; raise it if you disagree |

### 9.3 Decisions handed to gate 6, not settled here

- **Per-action vs. policy-cold/exceptions-hot approval.** Both SMEs asked for
  this to be re-opened at Architecture. F36's bundle model *is* policy approved
  cold, so MVP1 builds the mechanism without pre-empting the decision about what
  reaches a human hot.
- **Warehouse-lag resolution** (`DOMAIN_KB` §5.7, promoted to a first-class
  product problem by §10.1). MVP1 discloses staleness on the face of every
  number; the architecture must resolve it.
- **Whether the operational store and the evidence store share infrastructure**,
  and how the no-update guarantee is enforced at the storage layer.

---

## 10 · Obligations this plan hands forward

Recorded so they are not rediscovered. None are absorbed into backlog items.

| Owed by | Gate | What |
|---|---|---|
| `responsible-ai-architect` | 2/6 | Written EU AI Act classification assessment — the *not-high-risk* conclusion is itself a document that must exist before service, not an informal view. **Plus**: own the `INDUSTRY_KB` §15.4 anti-recommendation as a design constraint — clearer explanations increase reviewer deference, so F41 must be judged on override rate and volume, not on explanation quality. Per-composed-skill classification gate once F16 ships. |
| `security-architect` | 6 | Whether the warehouse holds personal data (payroll, commission, expense) → GDPR and model-provider transfer analysis. Owns obligations A–S. **New**: the broker is the sole credential holder (M) and the model must be unable to reach Oracle — this is a security boundary, not a code convention. |
| `solution-architect` | 6 | WORM/immutable store selection and ≥7-year retention (G). Model-deprecation migration control (K). **Resolution of the warehouse-lag problem** (`DOMAIN_KB` §5.7/§10.1, now first-class). Enforcement topology for M across three surfaces. Mandatory Impact Analysis per `INTAKE.md` A5. |
| `solution-architect` + deploy | 6/9 | **CUEC verification per tenant** (obligation S): Oracle journal approval enabled for our dedicated source and category, AutoPost unable to post it unapproved, ETL completeness, source extract integrity. Verified at deployment **and on tenant configuration change** — a CUEC relied on but never checked is a finding waiting for the first audit. |
| Gate 6 | 6 | Re-open the per-action approval question (§9.3). |
| `industry-expert` + `test-agent` | 7 | The industry/compliance suite **does not exist yet**. Scenarios derive from obligations A–S and `DOMAIN_KB` §6.2. All suites blocking, so it must exist and return `0`, not `3`. |
| `functional-agent` | 3 | Devil's-advocate pass on this re-cut. I expect the sharpest challenges on F42's inclusion, on whether 17 is genuinely under the ceiling or 18 wearing a merge-shaped disguise, and on my deferral of F20. |
| `ui-ux-designer` | 5 | F41's hard constraints (§5.4), the coverage meter and partial-run banner (§5.5), and the A19–A22 refusal surface (§5.8). Per standing preference, gate 5 requires a **rendered mockup**, not spec text. |
| `synthetic-data-agent` | 7 | Fixture generation for §11 — a 12-period seeded §6.2 sequence, an 11-period recurrence with a period-12 omission, a held-out reclass-journal period, and a population with a known 70% coverage gap. |

---

## 11 · Acceptance criteria for the Test gate

All suites blocking; no advisory exceptions. Exit code `3` (no scenarios
defined) is **not a pass**.

### 11.0 Criteria deliberately removed as unpassable

Stated first, because a criterion the build cannot pass turns a blocking suite
into a permanently red one, which is how blocking suites become advisory in
practice.

- **Removed — the superseded plan's criterion 9**: *"every proposal records the
  warehouse objects read and the as-of timestamp, **with a tie-back to ERP
  source**."* In a zero-write build with no ERP-side extract, there was nothing
  to tie back **to**; the assertion had no achievable implementation. It is
  replaced by **C4** below, which is passable because F26 makes the ERP control
  extract a certified dataset in its own right, so the tie-out has two real
  sides.
- **Retained and re-stated — the evidential-reproducibility trap.** No criterion
  asserts that re-running a proposal yields an identical output. That claim is
  not achievable with a stochastic model and must never be encoded as a passing
  test. The assertion is **reconstruction and explanation from stored
  artefacts** (E5).
- **Not asserted anywhere — recall against *all* coding errors.** Only recall
  against reclass-journal-caught errors is measurable (D2), and the suite fails
  if the evidence schema presents it as anything else.
- **Not asserted anywhere — "the agent is right."** For band-G output there is
  no ground truth; MVP1 ships no band-G feature, and that is by design (§7.5
  F46).

### 11.A Deterministic integrity — machine-checkable, hard ground truth

1. Given a warehouse fixture seeded with a known set of divergences from an ERP
   control extract, **F26 reports exactly that set** by balance, segment and
   period — no false positives, no omissions.
2. Given a fixture with a missing load batch and one with a stale refresh,
   **F26's A2 leg flags both**, and the staleness is expressed relative to the
   close clock, not as an absolute timestamp alone.
3. F28's five boundary checks each detect their seeded break (subledger↔GL
   control account, IC pair imbalance, roll-forward discontinuity, double-applied
   FX revaluation, suspense residual above policy).
4. **`integrity/` executes no model call.** Asserted at runtime by an
   instrumented harness, not by source inspection.
5. **A boundary check that cannot fail is a defect.** Each of the six checks has
   a fixture that makes it fail; a check with no failing fixture fails the suite
   (§2b — a control that can never fail trains its reviewer that the dashboard
   can never fail).

### 11.B Coverage and negative assurance — obligation R

6. Every skill declares an expected population, and a run without one **cannot
   start**.
7. Given a dataset selection covering 70% of a declared population, the run
   reports coverage = 70% and **cannot emit a "no exceptions" conclusion** in
   any surface. Asserted three ways: the UI, the dossier, and the export.
8. The clean-run output over 70% coverage is **textually distinguishable** from
   the clean-run output over 100% coverage, and names what was missing. A test
   that finds them identical is a failure — this is the exact under-selection
   failure the criterion exists to catch.
9. An action-capable or assurance-emitting skill offered an **uncertified**
   dataset refuses, and the refusal is recorded as a control event.
10. Every emitted number carries provenance, dataset version and staleness on
    its face — asserted in the rendered surface, not only in the payload.

### 11.C Guardrails and negative control — obligations L–P

11. Every action carries the **guardrail bundle hash** and a **policy decision
    ID**. An action lacking either fails the suite.
12. **Negative-control suite**: every rule in the live bundle has both a firing
    and a non-firing fixture, and the suite runs **against the live bundle**.
    A rule with a missing fixture fails the suite. There is **no criterion that
    logs non-events** (obligation N — the negative-log trap is explicitly not
    built).
13. **Blast-radius caps trip**: per-run proposal count, per-period aggregate
    value, and the third consecutive same-account same-direction proposal
    escalating. Asserted as a state change, not a warning.
14. Blast-radius caps are **non-disableable by a user**, including an
    administrator.
15. **The UI is not an enforcement point**: a direct API call bypassing the
    front end is denied by the broker with the same decision record.
16. **The model holds no Oracle credential.** No credential is resolvable from
    any module outside `broker/`. Asserted by static and runtime checks.
17. An override requires **dual authorisation**, a reason code from a **closed
    list**, and is **time-boxed to a single action**. A standing exemption cannot
    be created. Override rate is computed per agent, per user, per period.
18. A new guardrail can be introduced in **shadow mode**, logging what it would
    have blocked without blocking.
19. **No free-form SQL execution path exists.** A model-authored SQL string is
    unexecutable by construction; asserted by attempting it.

### 11.D Detection — the wedge

20. **Omission**: given a fixture where a recurring entry ran in periods 1–11 and
    is absent in period 12, **F29 detects it**. Same for an unreversed scheduled
    reversal, a stopped feed, and a one-sided intercompany posting.
21. **The discriminating test**: on the same period-12 omission fixture,
    **F42 (present-anomaly detection) does not detect it and F29 does.** This is
    the criterion that proves the wedge is real rather than asserted, and it is
    the single most important test in this suite.
22. **Coding**: F33 backtested against historical reclass journals on a held-out
    period reports precision and recall — and the evidence schema **labels
    recall as "against reclass-journal-caught errors only"**. A schema that omits
    the label **fails the suite**, per `DOMAIN_KB` §10.4b. This is a schema
    assertion, not a footnote.
23. **Coding scope guard**: F33 emits no proposal touching a legal-entity/IC
    segment or crossing a statement caption (opex/capex), and cut-off findings
    are emitted as detections with no proposal attached.

### 11.E Cross-period safety and evidence spine

24. Given a seeded twelve-period §6.2 sequence — same account, same direction,
    each period below threshold — **F9 escalates before period twelve**, and the
    period at which it escalates is recorded as a headline result.
25. Given a sequence where each period's explanation restates the prior
    period's, **F9's narrative leg flags it independently of whether the numeric
    leg has tripped.**
26. F9's escalation presents the **iron-curtain aggregate**, not the period
    delta.
27. **Forward disposition**: a disposition without an expected clearing period
    **cannot be saved**. Asserted as a hard failure, not a validation warning.
28. The next period's verification job runs automatically and, on a missed
    prediction, produces an **R6 state change** — risk grade raised and auto-pass
    eligibility revoked — not a notification.
29. **Evidential reconstruction**: a past decision can be reconstructed and
    explained from stored artefacts alone (version tuple, dataset version, bundle
    hash, decision ID, coverage statement, rendered view). Re-execution identity
    is **not** asserted (§11.0).
30. The evidence store exposes no update or delete path; an attempted mutation
    fails **and is itself recorded**. A modified stored dossier is detectable.
31. F1's export is parseable and complete **without application access**.
32. F5's lineage query enumerates every artefact a given agent version touched,
    **completely** — asserted, not sampled.

### 11.F Review surface and disposition capture

33. **No "approve all" affordance exists anywhere, at any permission level.**
    Asserted by rendered-UI test, not source inspection.
34. Default state of every proposal is not-approved; no pre-checked control
    exists.
35. The **rendered view** shown to the approver is captured, retrievable, and
    matches what was displayed.
36. The applicable threshold and the guardrail bundle version are visible on
    screen at approval time.
37. Rejection cannot complete without a structured reason.
38. **F12 records a resolution type (R1–R6) for every closed item**, plus dwell,
    evidence expanded and overrides. An item closed without a resolution type
    fails the suite — this is the ground-truth factory and an unlabelled outcome
    is a lost label.
39. An **injected known-error probe** is detectable in F12's output: the suite
    asserts the probe was presented and that the reviewer's response to it was
    recorded.

### 11.G Scope guards — criteria that assert absence and refusal

40. **No code path posts to Oracle in MVP1.** F40 produces a file. No posting
    credential exists in the build. Asserted, not assumed.
41. No Tier 2 capability beyond F40's export exists.
42. **A19–A22 are present as refusals, not absences** — the refusal surface
    exists, names each, and states that it is a design property rather than a
    roadmap gap (§5.8). A build where they are merely missing **fails**.
43. The `industry` compliance suite exists and returns `0`. Scenarios derive
    from obligations **A–S** and `DOMAIN_KB` §6.2.

### 11.H Success metrics — with the warning attached

`DOMAIN_KB` §6.5: *"an agent that is consistently right de-skills the team that
supervises it… Any success metric that measures only close-cycle time reduction
will show this failure as a win."*

- **Primary — omission catches.** Count and materiality of items F29 found that
  no present-anomaly detector could have found. This is the product's claim and
  it must be the number reported.
- **Primary — evidence acceptance.** An external auditor or controller-proxy
  reviews one F1 export end to end and states whether it is sufficient.
- **Secondary — forward-disposition hit rate.** What proportion of predicted
  clearing periods were correct. This is the product's own falsifiability
  measure and it should be published internally even when it is bad.
- **Secondary — coverage.** Median run coverage against declared population.
  A product whose runs are habitually partial is emitting weaker assurance than
  users think.
- **Reported as a positive — abstention rate.** How often a skill declines
  rather than producing a plausible answer. Must be reported alongside accuracy
  so accuracy alone cannot be optimised.
- **Monitored as a control signal — override rate**, per agent, per user, per
  period. A rising override rate is read as a miscalibrated guardrail first and
  as user error second.
- **Explicitly NOT a headline metric — close-cycle time reduction.** It may be
  measured. It must not be what the project is judged on.

---

## 12 · What happens after this gate

1. `functional-agent` challenges this re-cut as devil's advocate. Expected
   pressure points: F42's inclusion at all; whether 17 features with six merges
   is genuinely under the ceiling; the F20 deferral; and whether F40 should exist
   in MVP1 at all rather than shipping detection-and-disposition only.
2. `industry-expert` checks the obligation gating in §3.1 against A–S.
3. The human selects **feature by feature** — the defaults in §7 are
   pre-selections, and the deferred and recommend-reject rows are on the list
   precisely so they can be pulled forward.
4. Only then: `FEATURES.md` is written with the approved split and a one-line
   summary is appended to `PROJECT_CONTEXT.md`'s Decisions Log. **Neither has
   been written by this pass**, and `PROJECT_CONTEXT.md` has not been modified.
