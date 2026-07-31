# Plan — conclave-finance-studio

**Gate 3 · Plan & Backlog.** Author: `plan-agent`. Date: 2026-07-31.
**Status**: proposed — awaiting feature-by-feature human approval.
Challenged next by `functional-agent` as devil's advocate.

Inputs read in full: `INTAKE.md`, `PROJECT_CONTEXT.md` (Active Team +
Decisions Log), `knowledge/DOMAIN_KB.md` (`functional-agent`),
`knowledge/INDUSTRY_KB.md` (`industry-expert`), the three
`templates/*/TEMPLATE_MANIFEST.md`, `pipeline-state.json`.

---

## 0 · Completeness check — binding decisions this plan was checked against

Per contract, every binding decision recorded before this pass, and how this
plan satisfies or conflicts with it.

| Binding decision | Source | How this plan satisfies it |
|---|---|---|
| **Product shape: BOTH** (pre-built agents *and* a builder) | Decisions Log, 2026-07-30 | Satisfied by sequence, not by simultaneity. The pre-built half ships first (F6 + spine). The builder half is F16–F18, explicitly `/enhance-project` work, not silently dropped. §6 says which half ships first and why. |
| **Personas: all three** | Decisions Log, 2026-07-30 | **Partially — flagged as a conflict, not glossed.** The build-now set serves the staff accountant (F6) and the controller (F11, F12, F13). It does **not** serve the FP&A analyst; F21 (flux narrative) is the FP&A feature and I default it to later. See §7 · Conflict 1. |
| **Write-back with per-action approval — "the defining decision"** | `INTAKE.md` §A-write; Decisions Log | The build-now set has **zero ledger write**, so per-action *posting* approval is not exercised at all in the MVP. It is neither implemented nor overturned. It stays live for gate 6, which is what both SMEs asked for. See §5. |
| **A7.2 (worst harm) delegated to SMEs** | Decisions Log; `INTAKE.md` A7.2 | Answered by both KBs, converging. This plan's response is F9 + F10 + F14, and they are the features I refuse to trade away. See §4. |
| **A8.3 (MVP slice) delegated to SMEs; `plan-agent` proposes** | `INTAKE.md` A8.3 | This document is the proposal. It is my call, made, not deferred back. |
| **Three surfaces → `solution-architect` non-droppable, mandatory Impact Analysis on every enhancement** | `INTAKE.md` §A5 | Honoured. I do **not** unilaterally cut a surface; the mobile scope question is put to the human as decision **D2** in §8, with `industry-expert`'s recommendation attached. |
| **`responsible-ai-architect` effectively non-droppable** | Decisions Log | Its gate-2/6 obligations are named in §9 (EU AI Act classification, per-composed-agent gate) and are not absorbed into any backlog item. |
| **Full roster, 14 agents, nothing dropped. Test Policy: all suites blocking, no advisory exceptions** | `PROJECT_CONTEXT.md` Active Team | Reflected in §10 acceptance criteria: every criterion is written to be machine-checkable or evidence-backed, because none of them can pass advisorily. The `industry`/compliance suite does not exist yet (`INDUSTRY_KB.md` §8) and its creation is a gate-7 dependency, named in §10.5. |
| **Approval-under-pressure (A3.2) is a design consequence, not a footnote** | `INTAKE.md` §A3.2, recorded risks | F11 and F12 are its direct response. F11 forbids "approve all" as a hard constraint (§5.3), not a UX preference. |
| **Scope is very wide — the MVP slice is the mitigation** | `INTAKE.md` recorded risks | 12 build-now features: one agent, the control spine around it, one desktop surface. Eleven features deferred, all of them visible in §7. |

No binding decision is contradicted by this plan. One is only partially served
(personas), and that is raised as a decision, not buried.

---

## 1 · What I am proposing, in one paragraph

**Build the evidence and control spine, and prove it on the one close activity
that has deterministic ground truth.** The deliverable is not "a bank
reconciliation agent." It is an audit-grade evidence layer — dossier store,
version stamping, input provenance, agent lineage, cross-period monitoring, and
a risk-graded certification surface — with an agent-prepared reconciliation for
externally-verifiable accounts (bank, cash-in-transit) as the first thing that
exercises it, end to end, with **zero ledger write**.

`functional-agent` proposed the reconciliation slice and, correctly, warned
against its own proposal: bank rec is the most commoditised activity in this
domain and auto-matching has been solved for a decade (`DOMAIN_KB` §8). I take
that warning as binding on **framing**, so I have inverted the emphasis. The
reconciliation is the test harness. The spine is the product. That inversion is
not cosmetic — it changes what gets built (F1–F5 and F9–F13 are the majority of
the build-now set, not scaffolding around F6), it changes what gets measured
(§10), and it is written here so that no later gate can quietly re-promote bank
rec to the value proposition.

**Stated explicitly, per `DOMAIN_KB` §8's closing instruction:** bank and
cash-in-transit reconciliation is a **proving ground, not the product**. It must
not be positioned, marketed, or measured as the value proposition. If a later
gate treats it as such, that is a loop-back trigger.

---

## 2 · Why this slice and not another

| Candidate first slice | Verdict | Reason |
|---|---|---|
| Externally-verifiable reconciliation, zero write | **Chosen** | Hard external ground truth (`DOMAIN_KB` §2) → machine-checkable pass/fail at gate 8, which no other close activity offers. Blast radius zero. It is day 2, the volume day. Above all, it exercises the evidence machinery **in front of a real auditor before that machinery is what stands between an agent and the ledger** (`DOMAIN_KB` §8) — the cheapest possible way to discover the evidence package is unacceptable. |
| Accrual estimation | Rejected for first slice | Top statistical cause of restatement (`DOMAIN_KB` §4), no in-period ground truth, and the `DOMAIN_KB` §6.2 self-justifying mechanism in its purest form. Do not make the first slice the one whose errors are undetectable for a year. Deferred as F22. |
| Journal posting / write-back | Rejected for first slice | Write-back is the defining feature and should be the *second* thing proven. Prove the evidence chain first. Deferred as F17. |
| The builder | Rejected for first slice | Until author-role SoD governance exists (`DOMAIN_KB` §7.1, `INDUSTRY_KB` §6), a builder is a machine for manufacturing un-inventoried AI systems inside ICFR scope. Deferred as F16–F18. |
| Flux / variance narrative | Rejected for first slice, kept visible | Low risk, reaches the FP&A persona, genuinely painful. But it adds **no learning to the control spine** — it is read-only narrative with no evidence chain to test against an auditor — and it is commoditising fast (`INDUSTRY_KB` §7 B1). Deferred as F21. This is the deferral I hold with least confidence; see §7 · Conflict 1. |
| Cross-source reconciliation (warehouse vantage) | Rejected for first slice, kept visible | `industry-expert`'s strongest differentiator (§2.3b) and structurally unavailable to ERP-embedded competitors. But it needs the spine (F1–F5) and the single-source rec (F6) working first. Deferred as F19, and it is the feature I would pull forward first after MVP. |

---

## 3 · Tier model and obligation gating — how to read the backlog

**Tier**, per `INDUSTRY_KB` §6.2, is not a size estimate. It is a capability
class, and an agent **cannot acquire Tier 2 by being built, only by being
promoted**.

- **Tier 1** — read / analyse / draft. No ledger write, no posting, no
  reconciliation close-out into the system of record.
- **Tier 2** — anything that can lead to a posting.

**Every build-now feature in this plan is Tier 1. The MVP contains no Tier 2
capability of any kind.**

### 3.1 The eleven obligations are entry conditions, not features

Obligations **A–K** (`INDUSTRY_KB` §4) are listed nowhere in the backlog as
items to approve. They are conditions that gate features. But a correction to a
common misreading, and it matters for scoping:

> **Not all eleven are write-only.** `INDUSTRY_KB` §4.1 is explicit that AI which
> influences reconciliations is inside ICFR scope regardless of whether it
> posts. A reconciliation prepared by an agent and certified by a human is an
> **IT-dependent manual control**, which triggers IPE testing on the agent's
> inputs. So a subset of the obligations binds the MVP even at Tier 1.

| Obligation | Binds at | Gates which features |
|---|---|---|
| **A** — approval record is a first-class artefact incl. the *rendered view* | **Tier 1** | F1, F11, F12 |
| **B** — thresholds/materiality explicit, configurable, versioned, shown at approval | **Tier 1** | F3, F6, F8, F11 |
| **C** — completeness/accuracy of agent inputs evidenced (IPE) | **Tier 1** | F4, F6, F8 |
| **D** — agent identity: named principal, own entitlements, own log stream | **Tier 1** | F5 |
| **E** — preparer/poster split, distinct credentials | **Tier 2 only** | F17, F18 |
| **F** — approver ≠ requester ≠ agent author/last-modifier | **Tier 2 hard; Tier 1 once F16 ships** | F16, F17, F18 |
| **G** — append-only, tamper-evident store, ≥7yr, exportable without app access | **Tier 1** | F1, F5, F9, F13 |
| **H** — a reversal is a new record, never a mutation | **Tier 2 only** | F17, F18 |
| **I** — immutable version tuple {model, prompt, tool/config, corpus, params} | **Tier 1** | F1, F2, F9 |
| **J** — model/prompt change goes through documented change control | **Tier 1** | F2 |
| **K** — model deprecation is a tracked risk with a migration control | **Tier 2 entry condition; start at Tier 1** | F2, F17 |

**Consequence for scoping, stated plainly:** A, B, C, D, G, I and J are
**non-negotiable in the MVP**. That is why the build-now set is spine-heavy. It
is not gold-plating; it is the entry price for having an agent touch a
reconciliation at all.

---

## 4 · The one thing that must survive scoping

Both SMEs, briefed separately, converged independently:

> Per-action human approval is **structurally blind** to a systematic,
> individually-immaterial, aggregate-material error, because no single approval
> was wrong. The failure lives in the *sequence*, and there is no approval step
> for a sequence. (`DOMAIN_KB` §6.2 / §7.2.4; `INDUSTRY_KB` §5.1 / §5.4.3.)

`DOMAIN_KB` §7.2.4: *"If exactly one safety mechanism survives scoping, make it
this one."* `INDUSTRY_KB` §5.4.3: *"the single highest-value control feature in
the product."*

**F9 (cross-period pattern monitor) and F10 (narrative-recurrence detector) are
therefore the two features I will not trade.** If the human cuts scope, cut F13,
cut F12, cut F7 — do not cut F9 or F10. I have kept F10 as a separate line item
rather than folding it into F9 precisely so that it cannot be dropped as an
"implementation detail" of F9: F9 detects a *numeric* pattern (same account,
same direction, N periods, each sub-threshold), F10 detects a *textual* one (the
agent restating its own prior-period explanation). `DOMAIN_KB` §6.2's mechanism
needs both, and the textual one is the earlier signal.

**F14 (fresh-eyes rotation) is the third leg and I have defaulted it to later.**
I do this uneasily and I want the human to see the reasoning: `DOMAIN_KB` §6.2
notes that the periodic arrival of a fresh pair of eyes is *the actual,
undocumented control* that catches this class of error in a human-staffed team,
and that this product removes it without anyone deciding to remove it. F9 and
F10 **detect** the pattern; F14 **breaks** it. Detection before breaking is
defensible, and F14 needs ≥2 periods of history to do anything, which the MVP
will not have at launch. But this is a deferral the human may reasonably
overrule, and it is the strongest candidate on the "later" list for pulling
forward.

---

## 5 · Key design decisions and their trade-offs

### 5.1 Zero ledger write in the MVP — and what that does to the A-write decision

`INTAKE.md` records per-action approval as "the defining decision." Neither SME
overturned it; both said re-open it at Architecture (`DOMAIN_KB` §7.2;
`INDUSTRY_KB` §5.4.4).

This plan does not settle it, and is deliberately constructed so that it cannot
be settled by accident. With zero write, the MVP exercises **certification of a
reconciliation**, not **approval of a posting**. Those are different controls
with different failure modes. Building the first is not a commitment to
per-action approval on the second.

**Trade-off, stated honestly:** deferring write means the MVP does not
demonstrate the product's defining capability, and a demo of "we prepared a bank
rec and a human certified it" is not an impressive demo. I accept that cost. In
exchange, the hardest architectural obligations — rollback semantics against an
append-only ledger (`DOMAIN_KB` §5.5: reversal is the *only* correction
primitive, there is no undo), preparer/poster credential split (obligation E),
author-role SoD (obligation F) — are deferred without being dodged, and gate 6
gets to make the A-write call with F9 and F10 already built and producing
evidence, rather than in the abstract.

**What gate 6 must decide, informed by this build:** whether per-action approval
stays as recorded, or is replaced by `DOMAIN_KB` §7.2's alternative — approve
the policy cold (outside the close window, when attention exists), approve the
exceptions hot. That alternative is F15 on the backlog, defaulted to later
precisely because it is a gate-6 decision, not a gate-3 one.

### 5.2 A reconciliation is a re-runnable versioned object, not a one-shot task

Binding on `code-agent`, from `DOMAIN_KB` §1: late-arriving upstream data
invalidates downstream work — a late AP batch on day 3 invalidates the accrual
from day 2, the rec certified on day 2, and the flux narrative from day 3. That
is rework, not addition. **Any design that models a reconciliation as a task
with a completion state will be wrong in practice.**

Therefore: a reconciliation is an object with an ordered series of immutable
**runs**. A new run supersedes but never overwrites a prior run. A certification
attaches to a specific run, and a superseding run invalidates the certification
and says so loudly. This is a design constraint recorded here rather than a
backlog item, because it is a property of F6 and not separately approvable.

### 5.3 Hard constraints on the certification surface

From `INDUSTRY_KB` §5.4.2 and `DOMAIN_KB` §7.2, binding on `ui-ux-designer` at
gate 5 and `code-agent` at gate 7:

- The default state of any proposal is **not certified**. There is no
  pre-checked path.
- **"Approve all" / "certify all" must not exist.** Not as a power-user feature,
  not behind a permission. If it exists it will be used at 11pm and it makes the
  control cosmetic.
- The riskiest element of a proposal is the most visually prominent element, not
  a line in a rationale paragraph.
- Rejection is structured (reason required, selectable-plus-freetext), and for
  high-judgment items the required input must not be selectable from a list —
  deliberate friction that should survive `ui-ux-designer`'s likely usability
  objection (`DOMAIN_KB` §7.2.2).
- What was **rendered** to the approver is stored, not just the underlying data
  (obligation A). Otherwise you cannot later prove what the human saw.

`DOMAIN_KB` §7.2 also warns that better approval UI is not the answer to the
attention-budget problem and that treating it as such will waste a design cycle.
F11 is therefore scoped as a *risk-differentiation* surface — making unequal
risks look unequal — not as a legibility improvement. F12 exists because the
measurable defence is telemetry, not layout.

### 5.4 The audit trail must document context, not only blame

`DOMAIN_KB` §6.3 makes a point no one else on the roster will: a perfect
per-action approval log is also a perfect liability-allocation device pointed at
the most junior person in the chain. If the system records *who approved* but
not *what evidence they were shown and how long they had*, it documents blame
without documenting context.

F12 (review-precision telemetry) is therefore not a controller dashboard
feature. It is the staff accountant's defence, and it should be framed that way
to the user. It captures dwell time, which evidence was expanded, which
exceptions were overridden, and approval speed relative to that individual's own
baseline. It is simultaneously the evidence of *review precision* that
`INDUSTRY_KB` §4.1 says auditors test for and that "a checkbox and a timestamp"
fails.

### 5.5 Warehouse lag is a design defect to resolve, not a latency inconvenience

`DOMAIN_KB` §5.7: an agent reasoning over yesterday's warehouse snapshot while
the ledger changes hourly during close is a design defect. The MVP's zero-write
posture reduces this from "defect" to "staleness that must be disclosed" — but
F4 must record the as-of timestamp of every extract and surface it on the
certification screen, and a certification against a stale extract must be
visibly marked as such. Full resolution is a gate-6 obligation on
`solution-architect`, not something F4 closes.

### 5.6 Positioning — what this is competing against

Recorded here so gate 9 does not rediscover it. `DOMAIN_KB` §7.3: a displacement
pitch against BlackLine is dead for years, because the switching cost is not
licence fees but re-baselining the SOX control narrative with the external
auditor — a 6–12 month project no controller starts voluntarily. `INDUSTRY_KB`
§2.1: BlackLine's April 2026 positioning is explicitly about closing AI's
*governance and trust gap*, so any differentiation built on "our agents are
smarter" competes where the incumbent has decided not to fight.

Both SMEs independently point at the same opening: the **evidence layer**
(`INDUSTRY_KB` §2.3a — the audit package falls out of the system for free) and
the **long tail** (`DOMAIN_KB` §7.3 — the few hundred accounts every BlackLine
implementation left as spreadsheets, which are disproportionately the judgmental
accounts where the §6.2 failure lives). This plan builds toward the first (F1,
F13) and defers the second (F20) while keeping it visible, because F20 is
arguably the real product and my deferral of it is contestable.

---

## 6 · Template and structure

### 6.1 Recommendation: `genai-chatbot`, **for the first slice only**

This confirms the recommendation already recorded in `pipeline-state.json`.

| Template | Fit |
|---|---|
| **`genai-chatbot`** | **Chosen.** Gives FastAPI backend + Next.js/TypeScript/Tailwind/shadcn frontend, which is the shape the MVP needs: a tool-using LLM backend plus a required human-facing desktop web surface (F11, F12, F13). |
| `agentic-workflow` | Rejected. Backend-only, and its manifest states `ui-ux-designer` and the Experience Design gate are **not applicable**. Given `INTAKE.md` A3.2 and §5.3 above, the certification surface *is a control*, not a presentation layer. A template that switches off the Experience gate is disqualifying here. |
| `rag-knowledge-base` | Rejected. There is no document corpus to ground answers in. The ground truth is a warehouse and an external statement, not retrieval. (Note: if F16's builder later needs policy-document retrieval, that is an `/enhance-project` structural question, not a reason to pick it now.) |

**Two honest caveats on the fit:**

1. The primary UI is **not a chat stream**. It is a review-and-certification
   workspace. `code-agent` replaces the template's chat surface entirely; what
   is being kept is the Next.js + shadcn + FastAPI scaffold and the streaming
   plumbing, not the chat metaphor. The template's own smoke test
   (`POST /chat` → non-empty stream) will need replacing with the acceptance
   criteria in §10.
2. **No template carries both halves of the product shape.** The builder
   (F16–F18) is a governed authoring environment with versioning, an inventory
   and a promotion workflow. Nothing in `templates/` models that. It is
   explicitly `/enhance-project` work with its own template question at that
   time — and per `INTAKE.md` §A5, a mandatory `solution-architect` Impact
   Analysis.

### 6.2 File and module structure for the build-now set

```
backend/
  app/
    main.py                     # FastAPI app, routers, health
    config.py                   # settings; threshold policy loading (F3)
    evidence/                   # THE SPINE — obligations A, C, G, I
      store.py                  # append-only dossier writer; no UPDATE path (F1)
      dossier.py                # dossier schema: the 10 items of INDUSTRY_KB §4.3 (F1)
      integrity.py              # hash chaining / tamper-evidence (F1, obligation G)
      export.py                 # auditor export, consumable without app login (F13)
    versioning/
      registry.py               # model/prompt/tool/corpus version artefacts (F2)
      stamp.py                  # immutable version tuple on every proposal (F2, obligation I)
      changelog.py              # change-control record for prompt/model changes (F2, obligation J)
    policy/
      thresholds.py             # explicit, versioned materiality/tolerance objects (F3)
      risk_rating.py            # per-account risk grade driving F11's presentation (F3)
    provenance/
      extract.py                # warehouse query capture, as-of stamping (F4)
      ipe.py                    # tie-back of extract to ERP source (F4, obligation C)
    identity/
      principals.py             # one named principal per agent; no shared accounts (F5, obligation D)
      inventory.py              # auto-inventory, non-bypassable, exportable (F5)
      lineage.py                # blast-radius query: everything an agent version touched (F5)
    agents/
      recon/
        graph.py                # the reconciliation agent's tool-using graph (F6)
        matching.py             # deterministic matching against external statement (F6)
        items.py                # reconciling items; citation REQUIRED (F8)
        run.py                  # the immutable-run model of §5.2 (F6)
    monitors/
      cross_period.py           # numeric recurrence, aggregate/iron-curtain view (F9)
      narrative_recurrence.py   # textual self-restatement detection (F10)
    telemetry/
      review_precision.py       # dwell, expansions, overrides, speed-vs-baseline (F12)
    api/
      reconciliations.py, certifications.py, monitors.py, dossiers.py, inventory.py
frontend/
  app/
    reconciliations/            # work queue, risk-graded (F11)
    reconciliations/[id]/       # the certification surface; renders + captures view (F11, obligation A)
    monitors/                   # cross-period escalations, controller-facing (F9, F10)
    inventory/                  # agent inventory + lineage explorer (F5)
    audit/                      # dossier browse + export (F13)
  components/
    certification/              # no bulk-certify component exists, by construction (§5.3)
    evidence/                   # citation rendering; uncited residual styled as exception (F8)
    risk/                       # risk-grade prominence primitives (F11)
tests/
  suites/                       # per-suite run.sh; exit codes 0/1/3/4 per manifest
    functional/ ux/ security/ industry/ responsible-ai/ ...
```

**Two structural rules binding on `code-agent`:**

- `evidence/store.py` exposes **no update or delete path**. Not a private one,
  not an admin one. `INDUSTRY_KB` §4.3 is explicit that the audit trail cannot
  be a table an admin can `UPDATE`. Where the operational database and the
  evidence store share infrastructure at gate 6, the separation is enforced at
  the storage layer, not by convention.
- No shared service account across agents (obligation D). `identity/principals.py`
  is the only place credentials are resolved.

---

## 7 · Proposed backlog — 25 features, each individually approvable
### (13 build-now, 12 later — plus three explicitly refused, listed for the record)

**How to read this.** Every feature is its own approval. The **Default** column
is my recommendation as a *pre-selection*, not a decision — the human selects
feature by feature. Nothing has been filtered out: deferred and
recommend-reject items are all here, with reasoning, so they can be pulled
forward. **Tier** per §3. **Gated by** lists the obligations from §3.1 that must
be satisfied for that feature to be built at all.

### 7.1 Build now — the control spine (default: ON)

| ID | Feature | Tier | Gated by | Default | Reasoning |
|---|---|---|---|---|---|
| **F1** | **Evidence dossier store** — append-only, tamper-evident, ≥7yr, one dossier per agent proposal carrying all ten items of `INDUSTRY_KB` §4.3 | 1 | A, C, G, I | **BUILD NOW** | This is the product. `INDUSTRY_KB` §2.3a says the concrete artefact an auditor needs is still promised rather than shipped by incumbents — everything else in the MVP exists to fill this. |
| **F2** | **Version registry and proposal stamp** — model, prompt, tool/config and corpus as independently versioned artefacts; every proposal stamped with the immutable tuple; prompt/model changes produce a change record | 1 | I, J, K | **BUILD NOW** | `INDUSTRY_KB` §4.4 calls this the single most likely source of a gate-6 surprise. Cheap now, near-impossible to retrofit onto dossiers already written. |
| **F3** | **Threshold and materiality policy object** — explicit, configurable, versioned, and displayed at certification time | 1 | B | **BUILD NOW** | Obligation B: a threshold living implicitly inside a prompt is untestable and the control fails. Auditors test *against stated thresholds*. |
| **F4** | **Warehouse extract provenance / IPE record** — every query, as-of timestamp and source extract recorded and tied back to the ERP source | 1 | C | **BUILD NOW** | Obligation C is IPE support and `INDUSTRY_KB` §4.1 calls it the most commonly under-scoped consequence. Also the honest surface for the warehouse-lag defect (`DOMAIN_KB` §5.7, §5.5 above). |
| **F5** | **Agent identity, inventory and lineage explorer** — every agent a named principal with its own entitlements and log stream; auto-inventoried; every artefact any agent version ever touched enumerable | 1 | D, G | **BUILD NOW** | The inventory is the auditor's first request (`INDUSTRY_KB` §6.2.3). Lineage is the blast-radius answer — and an unanswerable blast-radius question converts a contained error into a scope-wide material weakness (`INDUSTRY_KB` §5.4.5). |

### 7.2 Build now — the proving-ground agent (default: ON)

| ID | Feature | Tier | Gated by | Default | Reasoning |
|---|---|---|---|---|---|
| **F6** | **Externally-verifiable reconciliation agent** — bank and cash-in-transit; ingests warehouse GL balance + external statement, matches, itemises, assembles support, stops at *ready for certification*. **Zero ledger write.** | 1 | A, B, C, G, I | **BUILD NOW** | Deterministic ground truth means gate 8 gets real pass/fail criteria instead of judgment about whether output "looks right" (`DOMAIN_KB` §2, §8). Proving ground, **not the product** (§1). |
| **F7** | **Auto-certification eligibility rules** — zero-balance / no-activity / within-tolerance accounts certified in aggregate by stated rule, not individually | 1 | B, A | **BUILD NOW** | The control model auditors already accept (`DOMAIN_KB` §2). Without it, F11 spreads fixed attention evenly across items that do not deserve equal treatment — which `DOMAIN_KB` §7.2 argues is *worse than the status quo*. This is the cheapest defence against the attention-budget problem. |
| **F8** | **Citation-required reconciling items** — every reconciling item must cite a source transaction; an uncited residual **cannot** be classified as a reconciling item, only as an unexplained difference | 1 | B, C | **BUILD NOW** | This is the code-level defence against `DOMAIN_KB` §6.2. The line between "reconciling item with an explanation" and "plug with a story" is exactly the line an LLM is least equipped to hold — so remove the LLM's ability to cross it by making citation a schema requirement rather than a quality expectation. |

### 7.3 Build now — cross-period safety (default: ON, and not tradeable)

| ID | Feature | Tier | Gated by | Default | Reasoning |
|---|---|---|---|---|---|
| **F9** | **Cross-period pattern monitor** — detects same agent / same account / same direction recurring below threshold across N periods; escalates on the **aggregate**, presented in iron-curtain terms | 1 | G, I | **BUILD NOW — do not cut** | Both SMEs, independently: the one safety mechanism that must survive scoping (`DOMAIN_KB` §7.2.4; `INDUSTRY_KB` §5.4.3). Per-action approval is blind to this by construction. Also `INDUSTRY_KB` has not seen an incumbent ship it convincingly — it is the safety feature *and* the differentiator. |
| **F10** | **Narrative-recurrence detector** — flags when an agent's current-period explanation is substantially a restatement of its own prior-period explanation | 1 | G, I | **BUILD NOW — do not cut** | The precise mechanism of `DOMAIN_KB` §6.2: prior-period treatment is legitimate evidence, so the agent's narrative gets *stronger* every month while the underlying error grows. Textual recurrence is the earlier signal than numeric drift. Listed separately from F9 so it cannot be dropped as an implementation detail. |

### 7.4 Build now — the certification surface, desktop web (default: ON)

| ID | Feature | Tier | Gated by | Default | Reasoning |
|---|---|---|---|---|---|
| **F11** | **Risk-graded certification workspace (desktop web)** — default not-certified; riskiest element most prominent; **no "certify all" anywhere**; structured reject-with-reason; the rendered view is captured as evidence | 1 | A, B | **BUILD NOW** | `INTAKE.md` A3.2 made this a design consequence at intake. Scoped as risk *differentiation*, not legibility — `DOMAIN_KB` §7.2 warns that treating it as a layout problem wastes a design cycle. |
| **F12** | **Review-precision telemetry** — dwell time, evidence expanded, exceptions overridden, speed vs. the individual's own baseline; visible to controller and internal audit | 1 | A | **BUILD NOW** | Two jobs at once: the evidence of *precision* auditors test for (`INDUSTRY_KB` §4.1), and the staff accountant's defence — it records what they were shown, not only what they clicked (`DOMAIN_KB` §6.3). |
| **F13** | **Auditor export package** — dossiers exportable in a form an auditor consumes **without an application login** | 1 | G | **BUILD NOW** | Obligation G's last clause: auditors want an extract, not a login. And per `DOMAIN_KB` §8, the whole point of the cheap slice is to put the evidence package in front of a real auditor early — you cannot do that without this. |

**Build-now total: 13 features.** One agent, the spine around it, one surface.

### 7.5 Later — default OFF, all visible, all pullable-forward

| ID | Feature | Tier | Gated by | Default | Reasoning |
|---|---|---|---|---|---|
| **F14** | **Fresh-eyes rotation control** — periodic forced re-derivation of an aged residual from source, without prior-period context in the agent's window | 1 | G, I | **LATER** — *my least confident deferral* | It restores the undocumented human control this product removes (`DOMAIN_KB` §6.2). F9/F10 *detect* the pattern; F14 *breaks* it. Deferred only because it needs ≥2 periods of history to act and the MVP launches with none. Pull it forward if you disagree — I would not argue hard. |
| **F15** | **Policy-cold / exceptions-hot approval model** — pre-approve rules and thresholds outside the close window; see only exceptions inside it | 1 | B, A | **LATER — gate 6** | This is the alternative to per-action approval (`DOMAIN_KB` §7.2.1). Building it now would pre-empt a decision `INTAKE.md` records as the human's defining one. It belongs to gate 6, informed by F9's output. Listed so it is not forgotten. |
| **F16** | **Tier 1 builder** — accountants compose read/draft-only agents freely; no write capability of any kind | 1 | F, D, G, I, J | **LATER** | `industry-expert` §6.3 recommends exactly this shape, and it is the second half of the BOTH product decision. Deferred because it requires author-role SoD (obligation F), definition versioning and a non-bypassable inventory to be *already working* — which is what F2 and F5 build. First `/enhance-project`. |
| **F17** | **Pre-built, vendor-change-controlled Tier 2 posting agents** — a small set of ledger-writing agents inside the vendor's own change control | **2** | **all A–K**, esp. E, F, H, K | **LATER** | The write-back half — the defining feature of the product, and the *second* thing to prove, not the first (`DOMAIN_KB` §8). Entry conditions are the full eleven obligations plus a gate-6 resolution of the A-write question and of `DOMAIN_KB` §5.5 rollback semantics. |
| **F18** | **User-promoted Tier 2** — promotion workflow granting a user-built agent write capability: named owner, documented scope, thresholds, independent reviewer ≠ author, recorded approval, version stamp | **2** | **all A–K** | **LATER** | `industry-expert` §6.3 explicitly defers this. Its value is that promotion *is* the change-control record whose absence would be the audit finding — but it cannot exist before F16 and F17. |
| **F19** | **Cross-source reconciliation using the warehouse vantage** — differences originating *between* systems (CRM ↔ billing ↔ ERP), which ERP-embedded agents structurally cannot see | 1 | A, B, C, G, I | **LATER — first to pull forward** | The most-cited 2026 practitioner complaint and a structural advantage from `INTAKE.md` A6.1 that BlackLine cannot easily match (`INDUSTRY_KB` §2.3b). Deferred only because it needs the spine and single-source rec working first. This is the feature I would build immediately after MVP. |
| **F20** | **Long-tail account onboarding** — bring the few hundred entity-specific accounts your close platform never templated onto the same evidence spine | 1 | A, B, C, G, I | **LATER** — *and my deferral here is contestable* | `DOMAIN_KB` §7.3 opening (1): lands in the gap between the platform and the spreadsheet, needs no displacement and no control re-baselining. It is arguably the actual commercial wedge, not F6. I defer it only because it is unbounded in shape until the spine exists. Worth arguing about. |
| **F21** | **Flux / variance narrative agent** — driver attribution with cited source rows, read-only | 1 | C, I | **LATER** | Reaches the FP&A persona — the one the MVP does not serve (§7 Conflict 1) — with zero ledger risk. Deferred because it adds no learning to the control spine and is commoditising fast (`INDUSTRY_KB` §7 B1). Pull forward if persona coverage matters more than spine depth. |
| **F22** | **Accrual proposal agent** — with explicit uncertainty and mandatory evidence citation | 1 (proposal) → 2 (if posting) | A–K if it ever posts; A, B, C, G, I as Tier 1 | **LATER — recommend not before F9 + F17** | Highest close-window pain and the strongest commercial pull, *and* the top statistical cause of restatement (`DOMAIN_KB` §4), with no in-period ground truth. It is `DOMAIN_KB` §6.2 in its purest form. Only viable once F1, F9, F10 and F11 are proven. Shown here because the pull toward it will be strong and it should be resisted deliberately, not by omission. |
| **F23** | **Native mobile: read / monitor / notify only** — close status, monitor escalations, notifications. No approval, no certification. | 1 | A, G | **LATER** — *see decision D2* | Genuinely useful for the controller persona and the honest use of the third surface. Deferred to keep MVP scope at one surface, not because the surface is wrong. |
| **F24** | **Approving or certifying from native mobile** | 1 (→2 later) | A, B | **RECOMMEND REJECT — see D2** | `industry-expert` §7 C2: mobile is the worst possible surface for an evidence-of-review control under time pressure — small screen, low scrutiny, exactly the 11pm scenario. A control argument, not a cost argument. Shown, not filtered, because it is your decision to overrule. |
| **F25** | **Standing PBC / audit-request responder** — answers recurring auditor requests directly over the dossier store | 1 | G | **LATER** | Turns F1/F13 into recurring visible value *between* closes, in the "Post" row `INDUSTRY_KB` §3 calls the unglamorous gap. Genuinely good; simply not needed to prove anything the MVP must prove. |

### Explicitly refused (shown for completeness, not proposed)

These appear in `INDUSTRY_KB` §7 Tier C and I am not putting them forward as
features at all. Listed so the record shows they were considered and why they
are absent.

- **Auto-post below a threshold / "autonomous close."** Contradicts `INTAKE.md`
  §A-write and nobody credible runs it (`INDUSTRY_KB` §2.2).
- **Agent-reviews-agent as a substitute for human approval.** Fails the
  fraud-deterrence leg of SoD (`INDUSTRY_KB` §4.2 problem 2). An agent may
  contribute to accuracy review; it may never be the only reviewer of anything
  that posts.
- **Natural-language ad-hoc ledger querying as a headline feature.** Oracle and
  everyone else has it; not a purchase driver (`INDUSTRY_KB` §7 C4).

### Conflict 1 — persona coverage (raised, not resolved)

The Decisions Log binds all three personas as primary. The build-now set serves
**two**: the staff accountant (F6, F8, F11, F12) and the controller (F5, F9,
F10, F12, F13). **The FP&A analyst is not served by the MVP.** Their feature is
F21, defaulted to later.

I did this deliberately — F21 teaches the control spine nothing — but it is a
partial departure from a binding decision and it is the human's to accept or
overrule. The remedy, if you want three-persona coverage in the MVP, is to
switch F21 to build-now, at the cost of a second agent's worth of scope. I do
not recommend it; I do flag it.

---

## 8 · Decisions I am putting to the human at this gate

### D1 · Public vs. private target customer — **open question, I am not answering it**

`INDUSTRY_KB` §8 flags this as a human decision and it is the one I most need
answered.

**§404(b) external auditor attestation on ICFR applies only to public filers**
(and not to all of them — non-accelerated filers are exempt). It determines how
hard the entire §4 compliance surface bites:

- **Public accelerated filer** — an external auditor independently tests and
  opines on the controls this system participates in. The evidence layer is not
  a nice-to-have; it is tested annually by someone with no incentive to be
  generous, and the `DOMAIN_KB` §6.2 scenario ends in an Item 9A disclosure.
  This makes F1, F2, F13 unambiguously correct as MVP scope, and it makes F13's
  "consumable without an app login" a hard requirement rather than a
  convenience.
- **Private or non-accelerated** — management still asserts on controls, but no
  §404(b) attestation. The compliance floor is materially lower, the buyer's
  urgency is lower, and a lighter evidence layer would be commercially
  defensible. Some of the spine could arguably be traded for reach.

**This changes the recommended MVP.** If the answer is "private," a reasonable
person would cut some of F1–F5 and add F19 or F21 instead. I have built the
backlog on the **public-filer assumption**, because that is the harder floor and
because `INDUSTRY_KB` §4.1 states there is no "pilot outside SOX" path once
A-write is in play. If that assumption is wrong, say so now and I will re-cut
the split rather than have gate 6 discover it.

Note also (`INDUSTRY_KB` §4.4): restatements are concentrated in smaller,
non-accelerated filers — so "private/small" is the lower *compliance* floor but
not the lower *risk* floor.

### D2 · The mobile surface — narrow it, or keep all three?

`industry-expert` §7 C2 recommends: **native mobile is read / monitor / notify
only; approval and certification happen on desktop web.** This is a control
argument — mobile is the lowest-scrutiny approval surface that exists, and
shipping it early ships the theatre before the control (`DOMAIN_KB` §8).

`INTAKE.md` A5 records three surfaces as binding, so this is yours to decide,
not mine to cut. Three options:

1. **Adopt the recommendation** — F23 (read/monitor/notify) later, F24 (mobile
   approval) rejected. *My default.*
2. **Keep mobile approval on the roadmap** — F24 moves from reject to later,
   with a gate-6 obligation on `responsible-ai-architect` and `ui-ux-designer`
   to show how evidence-of-review precision survives a phone screen.
3. **Reduce to two surfaces** — desktop web + mobile web only. Note this would
   change the `INTAKE.md` A5 consequence and should be recorded as an amendment
   if chosen; `solution-architect` remains non-droppable either way.

Whatever is chosen, it affects gate 5 (Experience Design) directly and should be
settled here rather than there.

---

## 9 · Obligations this plan hands forward

Recorded so they are not rediscovered. None are absorbed into backlog items.

| Owed by | Gate | What |
|---|---|---|
| `responsible-ai-architect` | 2/6 | Written EU AI Act classification assessment. Note `INDUSTRY_KB` §4.5: the *not-high-risk* conclusion is itself a document that must exist before service, not an informal view. Plus a per-composed-agent classification gate once F16 ships. |
| `security-architect` | 6 | Whether the warehouse holds personal data (payroll, commission, expense) → GDPR and model-provider transfer analysis. Owns obligations A–K per the Active Team roster. |
| `solution-architect` | 6 | WORM/immutable audit store selection and ≥7-year retention design (obligation G). Model-deprecation migration control (obligation K). **Resolution of the warehouse-lag defect** (`DOMAIN_KB` §5.7). Mandatory Impact Analysis per `INTAKE.md` A5. |
| Gate 6 | 6 | **Re-open the per-action approval decision**, per both SMEs. F15 is the alternative on the table. |
| `industry-expert` + `test-agent` | 7 | The industry/compliance test suite **does not exist yet** (`INDUSTRY_KB` §8). Scenarios derive from obligations A–K and `DOMAIN_KB` §6.2. Test Policy is all-suites-blocking, so this suite must exist and return `0`, not `3`. |
| `ui-ux-designer` | 5 | F11's hard constraints (§5.3), including the deliberate friction that this agent is expected to object to. Per standing preference, gate 5 requires a **rendered mockup**, not spec text. |

---

## 10 · Acceptance criteria for the Test gate

All suites blocking; no advisory exceptions (`PROJECT_CONTEXT.md` Active Team).
Exit code `3` (no scenarios defined) is **not a pass**.

### 10.1 Reconciliation correctness — machine-checkable

1. Given a synthetic GL balance and a synthetic external statement with a known
   set of differences, F6 identifies **exactly** that set — no false positives,
   no omissions.
2. Where the account ties exactly, F6 reports *ties* and raises no reconciling
   item.
3. Where a difference exists that F6 cannot attribute to a source transaction,
   it is emitted as an **unexplained difference**, never as a reconciling item
   (F8). *A test that produces a fluent explanation for an uncitable residual is
   a failure, not a pass.*
4. A superseding run invalidates any certification attached to the prior run and
   the invalidation is visible (§5.2).

### 10.2 Evidence spine

5. Every proposal has a dossier containing all ten items of `INDUSTRY_KB` §4.3.
   A missing item fails the suite.
6. The evidence store exposes no update or delete path. An attempted mutation
   fails and is itself recorded.
7. Tamper-evidence: a modified stored dossier is detectable.
8. Every proposal carries a complete version tuple {model, prompt, tool/config,
   corpus, params} (obligation I). An unstamped proposal fails.
9. Every proposal records the warehouse objects read and the as-of timestamp,
   with a tie-back to ERP source (obligation C).
10. **Evidential, not re-execution, reproducibility** (`INDUSTRY_KB` §4.4): the
    test asserts that a past decision can be *reconstructed and explained* from
    stored artefacts. It must **not** assert that re-running yields an identical
    output — that claim is not achievable and must not be encoded as a passing
    test.
11. F13's export is parseable and complete **without application access**.

### 10.3 Cross-period safety — the criteria that matter most

12. Given a seeded twelve-period sequence reproducing `DOMAIN_KB` §6.2 — same
    account, same direction, each period individually below threshold — **F9
    escalates**, and does so before period twelve. The period at which it
    escalates is recorded as a headline result.
13. Given a sequence where each period's explanation is a restatement of the
    prior period's, **F10 flags it**, independent of whether F9's numeric
    threshold has tripped.
14. F9's escalation presents the **aggregate** (iron-curtain) figure, not the
    period delta.
15. F5's lineage query enumerates every artefact a given agent version touched,
    completely. Blast-radius completeness is asserted, not sampled.

### 10.4 Certification surface

16. **No "certify all" / "approve all" affordance exists anywhere in the UI, at
    any permission level.** Asserted by rendered-UI test, not by source
    inspection.
17. Default state of every uncertified proposal is not-certified; no pre-checked
    control exists.
18. The rendered view presented to the certifier is captured and retrievable,
    and matches what was displayed (obligation A).
19. The applicable threshold is visible on screen at certification time
    (obligation B).
20. Rejection cannot be completed without a structured reason.
21. F12 records dwell time, evidence expansions and overrides for every
    certification event.

### 10.5 Scope guards — criteria that assert absence

22. **No code path writes to Oracle or to any ledger.** No posting credential
    exists in the build. This is asserted, not assumed.
23. No Tier 2 capability exists in the build.
24. The `industry` compliance suite exists and returns `0`. Scenarios derive
    from obligations A–K and `DOMAIN_KB` §6.2 (owed by `industry-expert` +
    `test-agent`, §9).

### 10.6 Success metric — with the warning attached

`DOMAIN_KB` §6.5: *"an agent that is consistently right de-skills the team that
supervises it… Any success metric proposed at gate 3 that measures only
close-cycle time reduction will show this failure as a win."*

Taking that instruction directly, the MVP's success metrics are:

- **Primary — evidence acceptance.** An external auditor (or a
  controller-proxy) reviews an F13 export for one reconciliation and states
  whether it is sufficient. This is the whole point of the slice.
- **Secondary — detection.** F9/F10 escalate the seeded §6.2 sequence, early.
- **Reported as a positive, per `INDUSTRY_KB` §5.4.1 — abstention rate.** How
  often the agent declines to explain rather than producing a plausible
  narrative. Higher is better, and it must be reported alongside accuracy so
  that accuracy alone cannot be optimised.
- **Explicitly NOT a headline metric — close-cycle time reduction.** It may be
  measured. It must not be the metric the project is judged on, for exactly the
  reason above.

---

## 11 · What happens after this gate

1. `functional-agent` challenges this proposal as devil's advocate (`INTAKE.md`
   A8.3). I expect the sharpest challenges on: my deferral of F20 (long-tail),
   my deferral of F14 (fresh-eyes), and whether 13 build-now features is
   genuinely narrow or is the wide scope `INTAKE.md` warned about wearing a
   spine-shaped disguise.
2. The human approves feature by feature and answers **D1** and **D2**.
3. Only then: `FEATURES.md` is written with the approved split, and a one-line
   summary is appended to `PROJECT_CONTEXT.md`'s Decisions Log. **Neither has
   been written by this pass.**
