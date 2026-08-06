# Architecture Knowledge Base — `conclave-finance-studio`

Owner: `solution-architect` · Gate 6 · Architecture (joint owner with
`security-architect`; `responsible-ai-architect` advisory)
Created 2026-07-31 · **Status: proposed under standing authorization
(`batch_authorized`), awaiting joint presentation with `security-architect`**

**Write set for pass 2 (gate 10 review-and-rule, 2026-08-05), declared:**

1. `projects/conclave-finance-studio/knowledge/ARCHITECTURE_KB.md` — this file
   (**`Edit` only**; it exists, so `Write` is off the table for this path).
   Sections amended: §3.2 (deployment gate for the pilot transport), §7.3 (two
   primitives ruled in), §9.4 (the export's rendered view), §18.1 (**stale —
   now resolved**), §20.1 (**execution status: the suite was re-run for real**),
   new §25 (the four gate-10 rulings + Impact Analysis), §24 (change history).

**Nothing in `dev/` is touched by this pass** — it is a review-and-rule pass;
where a ruling implies work, the owning agent is named and the work is theirs.
`PROJECT_CONTEXT.md`'s register is likewise not edited by me; §25.6 states which
entries each ruling closes, narrows or leaves open, for the orchestrator to record.

**Write set for pass 1 (2026-07-31), declared:**

1. `projects/conclave-finance-studio/knowledge/ARCHITECTURE_KB.md` — this file (new).

Nothing else is created or modified. `PLAN.md`, `FUNCTIONAL_SPEC.md`,
`UX_KB.md`, `PROJECT_CONTEXT.md`, `FEATURES.md` and `pipeline-state.json` are
untouched; the Decisions Log line for this gate is owed by the orchestrator.

**Inputs read in full for this pass:** `PLAN.md` (all of it — §5 design
decisions, §6.2 module structure, §7 backlog, §8 phase-2 seams, §9.3 decisions
handed to this gate, §10 obligations handed forward, §11 test criteria),
`knowledge/FUNCTIONAL_SPEC.md` (§0–§2 conventions, all criteria for F36, F38,
F39, F41, F1, F2, F5, F40, F33, F42, and §21–§25),
`knowledge/UX_KB.md` (complete, both parts),
`knowledge/DOMAIN_KB.md` §5, §6.2, §6.3, §10.7, §10.8, §10.9,
`knowledge/INDUSTRY_KB.md` §4.3, §13.2, §13.3, §14, §15 (obligations A–S),
`PROJECT_CONTEXT.md` Decisions Log **in full**, and
`templates/genai-chatbot/` (manifest, `pyproject.toml`, `package.json`,
`tests/suites/`). No `PRD.md` exists for this project.

**How to read this file.** It is durable. It accumulates across enhancements,
and every enhancement adds its own **Impact Analysis** section under §19. §17
is the register of judgement calls I made; §18 is what I could not settle;
§20 is the architecture suite I own at the Test gate.

---

## 0 · The one-paragraph architecture

A **read-only analytical system** sits beside Oracle ERP Cloud, never inside
it. Detection is deterministic Python over a warehouse the customer owns; the
model does exactly three narrow jobs and holds no credential of any kind.
Everything that touches a credential, a policy decision or an egress artefact
runs in a **separate process — the Governed Execution Service (GES)** — whose
only public surface is a set of named, typed operations: *evaluate this policy
decision*, *run this certified query by id*, *emit this approved export*. There
is no endpoint anywhere in the system that accepts SQL text, and there is no
code path in the application process from which an Oracle or warehouse
credential is resolvable. Findings, dispositions and approvals are written to an
**append-only, hash-chained evidence store in a separate database with a
separate role that holds no `UPDATE` or `DELETE` grant**, anchored daily by a
signature the application cannot forge and archived to object storage under a
seven-year retention lock. Coverage is not a validation rule but a **type**: the
only conclusion object capable of expressing "no exceptions" is constructible
only from a run whose uncovered-member set is empty, and all three output
surfaces render from that one object. Detectors are **YAML manifests binding a
declared population object to a registered evaluator primitive**, so the long
tail and phase 2's non-Oracle sources are configuration, not a detector rewrite.

---

## 1 · Completeness check — binding decisions this architecture was checked against

Per my contract I re-read `PROJECT_CONTEXT.md`'s Decisions Log **in full**, not
only the entries relevant to this gate's brief. Every binding decision, and how
this design satisfies it or where it conflicts.

| Binding decision (Decisions Log) | How this architecture satisfies it |
|---|---|
| **2026-07-30 — Product shape: BOTH** (pre-built agents *and* a builder) | The skill is already an **artefact** (`skills/*.yaml` + a detector manifest + a dataset allowlist + a capability set), compiled and registered exactly like a hand-authored one (§7, §8). F16's authoring surface is therefore a *writer* for an artefact type that already exists, plus an author-identity field in the registry and an SoD rule in the bundle — not a new runtime. Nothing here assumes the skill set is fixed. |
| **2026-07-30 — Personas: all three** | Staff accountant and controller are served by the desktop web surface as designed at gate 5. FP&A is served by F39's inquiry path, which in this architecture is the *same* certified-query execution path as everything else (§6) — so the FP&A leg inherits provenance, versioning and coverage rather than being a second, weaker read path. `PLAN` §7.7's partial-coverage conflict is carried forward unresolved, not re-decided here. |
| **2026-07-30 — Write-back with per-action approval ("the defining decision")** | §10. Approval is a first-class evidence record bound to a specific run and a specific rendered view; export is refused at GES without it (`AC-F40-03`). §16 decides the per-action vs. policy-cold question `PLAN` §9.3 handed to this gate — **per-action stays, and what reaches a human is governed by cold-approved policy that is itself under cross-period surveillance.** |
| **2026-07-30 — A7.2 (worst harm) delegated to SMEs** | `DOMAIN_KB` §6.2's self-justifying reconciling item is the failure this architecture is shaped around: run immutability and supersession (§13), stateful blast-radius state co-committed with the decision (§8.5), the narrative-recurrence detector as a first-class evaluator primitive rather than a text field (§7.3), and §16's constraint (c) — a cold-policy auto-disposal repeating on the same account escalates hot, so the cold path cannot *become* the §6.2 mechanism in automated form. |
| **2026-07-31 — SCOPE CORRECTION: not the GL; do not imitate GL** | No component performs ledger function. There is no matching engine, no period-status mutation, no balancing enforcement, no chart-of-accounts control. The only write to the outside world is a file (§10). The ERP is contacted read-only, for exactly two purposes: F26's control extract and §5.4's point-of-action revalidation — both reads. |
| **2026-07-31 — PRODUCT DIRECTION part 1: research-driven backlog** | Not re-litigated. This gate designs *how*, and every component in §3 maps to a build-now feature ID. |
| **2026-07-31 — PRODUCT DIRECTION part 2: NL, skill-based, datasets selected, action under guardrails** | §6 (semantic layer), §7 (detector runtime), §8 (guardrail broker). The NL resolver returns a `Resolution` object whose query field is a **closed enum of registered query ids**; it has no field capable of carrying SQL. |
| **2026-07-31 — MVP1 SCOPED TO ERP DATA ONLY** | Honoured, and the seams `PLAN` §8 P1–P8 require are specified concretely in §21: `Population` carries a `source_class`, never a table name; `CertifiedDataset` carries lineage and tie-out status without asserting its source is Oracle; the ERP is reached through an adapter interface with exactly one MVP1 implementation. |
| **2026-07-31 — STANDING AUTHORIZATION; trust SME judgement; make assumptions** | Twelve judgement calls made and registered in §17, each with its reversal condition. Two items escalated in §18, both genuinely undecidable by me. |
| **2026-07-31 — Gate 4 ambiguity 1: refusal surface is F50, build-now count → 18** | The refusal registry is a compiled, versioned artefact like every other (§14.4), and refusal events are written to the evidence store (`AC-REFUSAL-04`). It is treated as an 18th feature with a component of its own, not as a cross-cutting property. |
| **2026-07-31 — Gate 4 ambiguity 2: F42 is not cuttable while criterion 21 stands** | Architecturally reinforced: F29 and F42 are two **evaluator primitives over the same `Population` object and the same `RunScope`** (§7.3). The paired wedge comparison (`AC-F29-08` / `AC-F42-04`) is a single artefact emitted by the run harness because both sides are the same run shape. Cutting F42 removes a registered primitive and the comparison artefact stops being producible — which is now a structural fact, not a policy. |
| **2026-07-31 — Gate 5 (a): `AC-F41-03` strengthened — riskiest element at the largest computed font size** | Supported and constrained by §9.4's rendered-view mechanism: the evidential region is server-rendered with **inlined** styles, so computed font size is determinate in the retained artefact and checkable offline, not only in a live browser. |
| **2026-07-31 — Gate 5 (b): routing budget accepted** | Implemented as a field of the routing policy inside the guardrail bundle (§16.3), so raising the cap is a policy decision with a decision ID and an owner rather than a config toggle. It still needs an acceptance criterion — flagged in §18.3. |
| **2026-07-31 — Gate 5 (c): probe reveal timing routed to `responsible-ai-architect`** | **Not pre-empted.** §9.6 specifies a data model that supports either ruling with no schema change and states what each choice costs architecturally. I make no recommendation. |
| **2026-07-31 — Gate 5 (d): surface header corrected — MVP1 desktop web only** | Honoured. §19's surface register lists **six** surfaces the *product* has, marks the two in MVP1 scope, and gives a falsifiable reason for every one marked not-reached. |
| **2026-07-31 — Gate 5 closed: narrative collapsed and last; no green anywhere** | Both are presentation decisions I do not touch. The architecture makes the first *measurable* (§9.5: expansion events are captured by the same evidential payload that renders the region, so `AC-F12-03` reads real data), and makes the second checkable in the retained artefact because styles are inlined. |
| **Full roster, 14 agents. Test Policy: all suites blocking, no advisory exceptions** | §20 defines the architecture suite. Exit code `3` is not a pass; §20.1 states plainly that the entry point does not exist yet and everything is `STATIC ONLY — NOT EXECUTED`. |
| **Three surfaces → `solution-architect` non-droppable; mandatory Impact Analysis** | §19, and it enumerates surfaces the **project** has rather than surfaces this pass happens to touch. |

**Conflicts with a binding decision: none.** Three items are *carried forward
unresolved* and are labelled as such — FP&A persona coverage (`PLAN` §7.7),
public-vs-private filer (`PLAN` §9.1), and probe reveal timing (deliberately
left to `responsible-ai-architect`). Two **new** findings that were not visible
before this gate are raised in §18.1 and §18.2 and one of them (§18.1) would
change an acceptance criterion.

---

## 2 · The seven settled constraints, and where each one lands in the build

The brief states seven things as settled. They are not restated as goals here;
each is traced to the component that makes it structurally true, so a reviewer
can check the claim rather than accept it.

| # | Settled constraint | Where it becomes structural | Falsifiable by |
|---|---|---|---|
| 1 | Guardrail broker: deny-by-default allowlist, enforced at the broker never the UI; model never holds the Oracle credential; hash-addressed bundles; scheduled negative controls; dual-auth time-boxed overrides; stateful blast-radius caps | §8 in full. GES is a **separate OS process with its own secret mount** (§8.1); the app process has no credential in its environment to leak. Capability check is a set-membership test executed *before* rule evaluation (§8.3). Blast-radius state is co-committed with the decision in one serializable transaction (§8.5) | ARCH-03, ARCH-04, ARCH-05, ARCH-06, ARCH-07 (§20.2) |
| 2 | No free-form SQL; certified semantic layer; NL parameterises, never authors | §6. The only execution entry point is `POST /ges/query {query_id, query_version, params}`. There is no parameter of type "SQL" in any schema in the system, so a model-emitted SQL string has nowhere to be sent — it is unexecutable because it is unroutable | ARCH-02 |
| 3 | Evidential, not re-execution, reproducibility; provider deprecation becomes a compliance dependency | §14.1 version registry + §14.2 model-lifecycle control. Nothing anywhere asserts output identity on re-run; the dossier's completeness assertion (`AC-F1-01`) is enforced at the **write path**, so a dossier missing a tuple element cannot be persisted | ARCH-10, ARCH-11 |
| 4 | Two-key posting boundary; dedicated Oracle source + category; CUEC verified per tenant | §10. Export refuses at GES — not at the UI — on missing in-product approval, stale CUEC verification, or failed point-of-action revalidation. Our identifiers are stamped into the Journal Import reference columns so enumerability survives loss of our store | ARCH-12, ARCH-13 |
| 5 | Forward disposition from period 1 — retrofit-hostile | §12.2. `expected_clearing_period` is a **NOT NULL column on the disposition record** and the disposition write path has no overload without it. The next-period verification job is registered at deploy, not added later | ARCH-14 |
| 6 | Coverage as a control — a partial run structurally unable to emit "no exceptions" | §11. `Conclusion` is a closed sum type; the `no_exceptions` variant exists only on `FullPopulationConclusion`, whose constructor is private and reachable only through a factory that requires an empty uncovered set. One object, three renderers | ARCH-08, ARCH-09 |
| 7 | Phase-2 seam: detectors take a declared population object, never a table name | §7.2. `Population` has no field capable of holding a table name; it holds a `resolver_query_id` and a `source_class`. A detector manifest that names a table fails bundle compilation | ARCH-15 |

---

## 3 · Component model

### 3.1 Five planes and one hard boundary

The system is five planes. The only architecturally load-bearing line is the one
between the **Analysis plane** and the **Governed Execution plane** — that line
is a process boundary, not a module boundary, and everything in constraint 1
depends on it being real.

```
┌───────────────────────────────────────────────────────────────────────────┐
│ EXPERIENCE PLANE            (Next.js, desktop web — MVP1's only UI)       │
│  Ask · Exceptions · Review · Dispositions · Catalogue · Monitors ·        │
│  Inventory · Audit · Refusals                                             │
│  Renders the server-produced evidential region verbatim; owns no policy.  │
└──────────────────────────────┬────────────────────────────────────────────┘
                               │  HTTPS, session auth
┌──────────────────────────────┴────────────────────────────────────────────┐
│ ANALYSIS PLANE  — process: `api` (FastAPI)   NO CREDENTIALS IN ENVIRONMENT│
│  ┌────────────┐ ┌────────────┐ ┌───────────┐ ┌──────────┐ ┌────────────┐  │
│  │ run        │ │ detector   │ │ agent     │ │resolution│ │ conclusion │  │
│  │ harness    │ │ runtime    │ │ runtime   │ │ + dispo. │ │ builder    │  │
│  │ (F38 cov.) │ │ (F26/28/29 │ │ (3 narrow │ │(F35/F32/ │ │ (§11 type) │  │
│  │            │ │  /9/33/42) │ │  LLM jobs)│ │  F12)    │ │            │  │
│  └────────────┘ └────────────┘ └───────────┘ └──────────┘ └────────────┘  │
│  ┌────────────┐ ┌────────────┐ ┌───────────┐ ┌──────────┐ ┌────────────┐  │
│  │ catalogue  │ │ semantic   │ │ evidence  │ │ identity │ │ refusal    │  │
│  │ (F38 meta) │ │ registry   │ │ writer    │ │ (F5)     │ │ registry   │  │
│  │            │ │ (read-only)│ │ (F1/F2)   │ │          │ │ (F50)      │  │
│  └────────────┘ └────────────┘ └───────────┘ └──────────┘ └────────────┘  │
└──────────────────────────────┬────────────────────────────────────────────┘
                               │  mTLS on loopback — the ONLY way out
        ═══════════════════════╪═══════════════ TRUST BOUNDARY ═════════════
                               │
┌──────────────────────────────┴────────────────────────────────────────────┐
│ GOVERNED EXECUTION PLANE — process: `ges`   SOLE CREDENTIAL HOLDER        │
│  ┌──────────────┐  ┌──────────────────┐  ┌────────────────────────────┐   │
│  │ policy       │  │ certified query  │  │ egress                     │   │
│  │ broker       │  │ executor         │  │ (journal export, POAR,     │   │
│  │ (F36)        │  │ (F39 execution)  │  │  auditor bundle signing)   │   │
│  │ bundle+state │  │ bound params only│  │  (F40, F1 export)          │   │
│  └──────────────┘  └──────────────────┘  └────────────────────────────┘   │
│  Public surface: /decide  /query  /export/journal  /revalidate  /bundle   │
│  There is no endpoint that accepts SQL and none that returns a secret.    │
└───────┬────────────────────┬──────────────────────┬───────────────────────┘
        │ read-only          │ read-only            │ write (files only)
┌───────┴────────┐  ┌────────┴────────┐   ┌─────────┴──────────────────────┐
│ DATA PLANE     │  │ ERP CONTROL     │   │ EGRESS                         │
│ customer       │  │ READ (Oracle    │   │ object store: Journal Import   │
│ warehouse      │  │ Fusion REST/BI) │   │ files, auditor export bundles, │
│ (Oracle-sourced│  │ F26 tie-out +   │   │ evidence archive (WORM lock)   │
│  MVP1)         │  │ §5.4 POAR       │   │                                │
└────────────────┘  └─────────────────┘   └────────────────────────────────┘

  PERSISTENCE (Postgres 16, two databases, two roles)
   app_db      — runs, findings, dispositions, catalogue, blast-radius state
   evidence_db — dossiers, decisions, approvals, control events, hash chain
                 role grants: INSERT, SELECT.  No UPDATE. No DELETE. No DDL.
```

### 3.2 Why the trust boundary is a process, not a module

`PLAN` §6.2 rule 2 says the broker is "the only place a credential is
resolved". A module cannot enforce that: any other module can `import` it, and a
tool-calling agent that is prompt-injected reaches whatever the process can
reach. Two processes with separate secret mounts is the cheapest construction in
which the statement is *true rather than agreed*. It costs one extra service in
the deployment unit and one HTTP hop on the read path.

The cost is real and I am taking it deliberately, because the entire product
claim — obligations E, M, and `AC-F36-04` — reduces to this one boundary.

**Note for MVP1 specifically.** MVP1 has *no* Oracle posting credential at all
(`AC-F40-02`). The boundary is therefore exercised in MVP1 by the **warehouse
read credential and the ERP control-read credential**, which do exist. That is
deliberate: the boundary must be load-bearing and tested before the posting
credential arrives in phase 2, or its first real use will be its first test.

**Amended 2026-08-05 (gate 10 ruling 3, §25.3) — the pilot transport, and the
gate before the first tenant.** `backend/pilot_transport.py` puts the broker
inside the api process, so **in the running pilot this boundary is a module
boundary, not a process boundary.** That is acceptable for a pilot on the
conditions in §25.3.1 and unacceptable for any tenant deployment. §25.3.2 states
the precondition as three conjunctive deploy-time gates — the operative one being
that **the `ges` package is not on the api host's disk**, which converts the
residual nobody can witness in one interpreter into something a deployment can be
checked for. Register entry 19 is narrowed by this ruling and does **not** close.

This is jointly owned with `security-architect` — see §22.

### 3.3 Component → feature map

| Component | Features | Obligations |
|---|---|---|
| `ingest/` — connector, certifier, watermark, tie-out | F26, F38 | C, Q |
| `catalogue/` — dataset objects, populations, coverage | F38 | C, Q, R |
| `semantic/` — certified query + metric registry, NL resolver | F39 | Q, R, I |
| `detectors/` — manifests + evaluator primitives | F26, F28, F29, F9, F33, F42 | C, Q, R, G, I |
| `agents/` — the three narrow model jobs | F39, F41 (rationale drafting) | I, J, K |
| `resolution/` — R1–R6, forward disposition, verification | F35, F32 | A, G, I |
| `capture/` — disposition & review-precision capture, probes | F12 | A, G |
| `ges/broker/` — bundle, decision, blast radius, override | F36 | B, E, F, J, L, M, N, O, P |
| `ges/query/` — certified query executor | F39 | Q |
| `ges/egress/` — journal export, POAR, bundle signing | F40, F1 | A, E, H, S |
| `evidence/` — dossier, hash chain, anchors, export | F1, F2 | A, C, G, I, J, K |
| `identity/` — principals, inventory, lineage | F5 | D, G |
| `refusal/` — refusal registry and events | F50 | — |
| `render/` — evidential region renderer | F41, F40 | A |

---

## 4 · Data flow — the five paths that matter

### 4.1 Certification path (scheduled, per close day and on demand)

```
scheduler → api.catalogue.certify(dataset_id)
  → ges.query(certified_query="catalogue.profile", params={dataset})   # row count, XOR content hash, max watermark
  → ges.query(certified_query="tieout.erp_control_extract", ...)       # F26 A1 leg
  → dataset_version row written to app_db
  → certification control event written to evidence_db (append-only)
  → status = COMPUTED   (NOT certified)
human certifying owner attests → status = CERTIFIED, owner + timestamp recorded
```

`COMPUTED` is treated as **uncertified** everywhere action capability or
negative assurance is concerned (`AC-F38-09`). Obligation Q names a certifying
owner; a system that certifies itself has not discharged it.

### 4.2 Analysis path (the common case — Tier 1, no action)

```
Ask screen: NL text + dataset selection
  → agents.resolver → Resolution{query_id ∈ closed enum, params, alternatives}
     ├─ unresolvable  → REFUSED, names the missing metric/join/dataset (AC-F39-03)
     └─ ambiguous     → candidates named, user chooses (AC-F39-07)
  → run harness opens an immutable Run:
       binds skill@version, detector manifests@version, population@version,
       dataset_versions[] (pinned watermarks), bundle_hash, model/prompt versions
  → ges.decide(action="run_skill", scope=…) → Decision(allow|deny) + decision_id
       (Scope + Temporal + Capability classes evaluated here, before any read)
  → coverage computed: expected_members ∖ covered_members  → RunScope
       0 members covered → NoScanConclusion, run terminates (AC-F38-08)
  → detector runtime executes each manifest's evaluator primitive,
       reading ONLY via ges.query(query_id, params)  — deterministic, no LLM
  → findings → routing policy (§16) → auto-disposed | routed to a human
  → conclusion builder → Conclusion (type determined by coverage, §11)
  → evidence writer → dossier(s) + run record, hash-chained
  → three renderers: screen payload · dossier · export
```

### 4.3 Review and disposition path

```
Review screen renders evidential region = render(review_payload, template@version)
  → reviewer records a resolution R1–R6 (no generic "approve" — UX §5.4)
  → capture: dwell, expansion events, override, probe response
  → disposition write path: expected_clearing_period NOT NULL, enforced in DB
  → evidence writer: approval record + rendered_view (bytes + sha256) + decision_id
```

### 4.4 Export path (Tier 2 — the only egress that leaves the building as an action artefact)

```
approved reclass proposal
  → ges.export/journal {proposal_id, approval_id}
     GES checks, in order, each producing a decision_id on refusal:
       1. approval exists, is for THIS run, and the run is not superseded
       2. CUEC verification current for this tenant and not failed  (AC-F40-05)
       3. blast-radius: per-run count, per-period aggregate, consecutive-period
          repetition, footprint vs. balance, per-batch line cap  (AC-F40-07)
       4. POINT-OF-ACTION REVALIDATION (§5.4) — warehouse basis still agrees
          with the ERP for the affected account combinations and period
       5. Journal Import file emitted with the dedicated source + category and
          our identifiers stamped into the reference columns
  → dossier sealed; file written to object store; no posting occurs (AC-F40-02)
```

### 4.5 Evidence path

Every write in every path above goes through **one** evidence writer with one
signature. There is no second way to write an evidence record, which is what
makes the lineage completeness claim in `AC-F5-03` structural rather than a join
somebody has to remember to extend (§14.3).

---

## 5 · Warehouse ingest, and the resolution of warehouse lag

`PLAN` §9.3 hands this gate the warehouse-lag problem explicitly, and
`DOMAIN_KB` §5.7 states it in its sharpest form: *an agent reasoning over
yesterday's warehouse snapshot and writing into today's ledger is a design
defect, not a latency inconvenience.* Here is the resolution, in four parts.

### 5.1 We do not own the ETL, so "ingest" means "certify and pin"

The warehouse is the customer's. We connect **read-only** and we never write to
it. Our ingest layer is therefore a *certification and pinning* layer, not a
pipeline:

- **Connector** — one read-only connection per warehouse, credential held only
  by GES. SQLAlchemy dialect chosen per tenant; MVP1 targets an Oracle-sourced
  warehouse but the connector is not Oracle-specific (phase-2 seam P2/P4).
- **Watermark** — every certified dataset carries `extract_watermark`, the
  maximum source-side change timestamp observed, plus `as_of` (when we read it).
- **Content hash** — XOR-aggregate of per-row SHA-256 over the dataset's
  canonical projection. Chosen over an ordered digest because it is
  order-independent and incrementally maintainable; a warehouse does not
  guarantee row order and an ordered digest would produce false tamper signals.
- **Row count, tie-out result and date, certifying owner, version** — the
  remaining five of `AC-F38-01`'s nine attributes.

### 5.2 A run is pinned; it cannot see data that arrives mid-run

A `Run` binds `dataset_versions[]` at open. Every `ges.query` call inside that
run passes `run_id`, and GES adds the pinned watermark as a predicate. A row
that lands after the run opened is invisible to that run. This is what makes
`PLAN` §5.3's immutable-run rule true at the data layer and not only at the
record layer.

### 5.3 Staleness is expressed against the close clock, because that is the fact a close professional acts on

A first-class `CloseClock` object per `(ledger, period)`:

```
CloseClock { ledger, period, oracle_period_status, close_day_zero,
             soft_close_at, hard_close_at, now_close_day }
```

Staleness rendered with every figure (`AC-F38-11`) is
`now_close_day − as_of_close_day`, expressed in close days and hours — *"2 days
behind close clock"*, per `UX_KB` §5.8 — never as a bare timestamp. `CloseClock`
is populated from the ERP control read (period status) plus tenant
configuration (the close calendar).

### 5.4 Point-of-Action Revalidation (POAR) — the actual answer to the defect

Disclosure is not a resolution. The resolution is that **the staleness window is
closed at the moment of action, not at the moment of analysis.**

Before any Tier 2 egress, GES performs a **narrow, scoped, read-only ERP query**
covering exactly the account combinations and period the proposal touches, and
compares:

| Compared | Refusal condition |
|---|---|
| Account balance, ERP vs. the warehouse snapshot the proposal was built on | any difference beyond a configured rounding tolerance |
| Latest journal effective timestamp on those combinations | ERP has a journal newer than the pinned watermark |
| Oracle period status for the target period | not `Open` |

Any refusal produces a `stale_basis` denial with a decision ID, marks the run
`SUPERSEDED_BY_SOURCE`, and invalidates the pending approval loudly (the same
treatment `AC-F41-12` gives a superseded run — the action area is structurally
replaced, per `UX_KB` §5.4).

**Why this costs nothing new in scope.** `PLAN` §11.0 already establishes that
F26 makes *"the ERP control extract a certified dataset in its own right, so the
tie-out has two real sides"* — the ERP read channel is therefore already in
approved MVP1 scope. POAR is a scoped, on-demand invocation of that same
channel, not a new integration. `DOMAIN_KB` §5.7's defect is closed by reusing a
capability F26 already requires.

Rejected alternative: *"refresh the warehouse before acting."* We do not own the
ETL and cannot make that promise. Rejected alternative: *"only act on data less
than N hours old."* A four-hour-old snapshot is just as wrong if a journal
landed three hours ago on the exact account we are about to reclass; freshness
is not the property that matters, **agreement on the affected population** is.

### 5.5 Late-arriving data supersedes completed runs

`DOMAIN_KB` §1: late-arriving upstream data invalidates downstream work. A
`run_dataset_binding(run_id, dataset_id, watermark)` table lets a supersession
worker, on observing a new watermark, mark exactly the affected runs
`SUPERSEDED_BY_DATA` — an index lookup, not a scan of every run. Pending
approvals on those runs are blocked with the same UI treatment as `AC-F41-12`.

**This is a finding, not just a design.** `AC-F41-12` is written against
supersession by a *later run*. Supersession by *later data* is the more common
real-world case and no criterion covers it. See §18.1.

---

## 6 · The semantic layer — how "no free-form SQL" is made structural

### 6.1 The certified query is a reviewed artefact, not a generated string

```yaml
# semantic/queries/gl.residual_by_account.yaml
query_id: gl.residual_by_account
version: 3
title: Clearing-account residual by account and period
sql_file: gl.residual_by_account.sql          # human-authored, reviewed, static
parameters:
  - {name: ledger_id,   type: int,      required: true}
  - {name: period,      type: period,   required: true}
  - {name: account_set, type: enum,     domain: account_sets, required: true}
joins_used:    [gl_balances__ledger@2, gl_je_lines__accounts@4]
measures_used: [residual_amount@1]
datasets_required: [dw.gl_balances, dw.gl_je_lines]
population_compatibility: [pop.clearing_accounts]
result_contract:
  grain: [account_combination, period]
  columns: [{name: residual_amount, type: decimal(28,6)}, ...]
```

The registry (`queries/`, `joins/`, `measures/`) is compiled at build time into
an immutable, hash-addressed artefact. A query, a join and a measure each carry
their own version, which is what `AC-F39-04` requires the answer to state.

### 6.2 The execution boundary makes SQL unroutable

GES exposes exactly one execution operation:

```
POST /ges/query
  { query_id, query_version, params: {…}, run_id, population_ref }
→ { rows, dataset_versions[], result_contract, coverage_members[] }
```

There is **no parameter of type SQL anywhere in the system**. GES resolves
`query_id` against the compiled registry (unknown id → refusal), validates each
parameter against its declared type and domain, and executes with **bound
parameters only** — no string interpolation exists on the execution path.

`AC-F39-02` asks that a model-emitted SQL string be denied and recorded. The
implementation: the resolver's output model has no SQL field, so a model that
emits SQL fails schema validation at the resolver and the attempt is recorded as
a control event. The string never reaches an execution path because **there is
no execution path it could be addressed to**. `PLAN` §11 criterion 19 —
"unexecutable by construction" — is satisfied by unroutability, which is a
stronger and cheaper property than filtering.

### 6.3 The NL resolver

The model's entire job here is *classification and slot-filling*:

```python
class Resolution(BaseModel):
    query_id: QueryId          # closed Enum generated from the compiled registry
    query_version: int
    params: dict[str, ParamValue]
    alternatives: list[QueryId] = []
    unresolvable_reason: str | None = None
```

The model is shown the catalogue of query titles, descriptions and parameter
schemas — never the schema of the warehouse. Server-side validation is
independent of the model's compliance: an id outside the enum, a parameter
outside its domain, or a period outside the certified dataset's coverage
(`AC-F39-08`) each produce a refusal naming what was missing. Two or more
candidates within a configured margin produce `AMBIGUOUS` and the user chooses
(`AC-F39-07`) — the system never picks silently.

**Judgement call J-4 (§17):** the resolver runs at *temperature 0 with a
constrained tool schema*, and its output is validated rather than trusted. The
reason is `DOMAIN_KB` §10.8 — 17–21% on Spider 2.0 — but note the architecture
does not depend on the resolver being accurate. A wrong `query_id` is a *visible*
wrong answer, because `AC-F39-01` shows the resolved query name and bound
parameters before submit is available. The design converts an invisible failure
(wrong join) into a visible one (wrong named question). That is the whole point.

---

## 7 · The detector runtime — how a new detector becomes configuration

### 7.1 The claim, stated honestly and bounded

"A new detector is configuration rather than code" is true for the long tail and
false for a genuinely new mathematical shape. Concretely: **a new detector is a
YAML manifest binding an existing evaluator primitive to a population, a key and
parameters. A new *primitive* is code.** I would rather bound the claim than
have `code-agent` discover the boundary in week ten.

The evidence that the bound is in the right place: **all four of F29's
sub-detectors are one primitive.** A recurring entry that did not run, a
scheduled reversal that did not reverse, an entry that stopped when its feed
stopped, and a one-sided intercompany posting are the same computation —
*expected member present in history, absent in the current period* — over four
different population/key pairs. That is the wedge, and it is one primitive plus
four manifests.

### 7.2 The declared population object (the phase-2 seam, P1/P2/P4)

```yaml
# catalogue/populations/pop.recurring_accruals.yaml
population_id: pop.recurring_accruals
version: 2
source_class: erp_warehouse          # NEVER a table name — this is the seam
member_key: [ledger_id, legal_entity, account_combination, recurrence_key]
resolver_query_id: population.recurring_accrual_members@3
dimensions:
  - {name: ledger_id,    binding: run_param}
  - {name: period,       binding: close_clock}
  - {name: legal_entity, binding: run_param, multi: true}
expected_cardinality_source: resolver          # enumerable, not merely counted
```

Three properties matter and each is checkable:

1. **No field can hold a table name.** `source_class` is a closed enum
   (`erp_warehouse` in MVP1; `procurement`, `contracts`, `hr`, `operational` in
   phase 2 per `PLAN` §8 P2). Bundle compilation rejects a manifest naming a
   physical object. The detector never learns where its data lives.
2. **Members are enumerable, not counted.** Coverage is a *set difference over
   member keys*, which is the only way the Ask screen can name the unmet
   segments (`UX_KB` §5.1's declared-population panel, `AC-F38-03`). A
   percentage derived from row counts cannot name what is missing.
3. **Populations are versioned artefacts** in the registry, so the same skill
   over a different population is a different control (`DOMAIN_KB` §10.8(2)) and
   the dossier records which.

### 7.3 The registered evaluator primitives (MVP1) — **thirteen as of gate 10**

**Amended 2026-08-05 (gate 10 ruling 2, §25.2).** This list held eleven at pass 1.
`code-agent` built two more, declared them in `UNSPECIFIED_BUT_BUILT` rather than
quietly widening my list, and referred them here. **Both join §7.3. Neither is
folded into an existing primitive.** They are rows 12 and 13 below and are marked
as such; the reasoning, and what `code-agent` must now change, is in §25.2.

| Primitive | Computation | Detectors it serves |
|---|---|---|
| `identity_tieout` | two populations must agree on a key within tolerance | F26 A1, F28 A6 |
| `freshness` | watermark / batch completeness vs. close clock | F26 A2 |
| `pair_imbalance` | two-sided key must net to zero | F28 A7 |
| `continuity` | closing(p−1) + movements(p) = closing(p) | F28 A8 |
| `arithmetic_recompute` | independently recompute a derived figure | F28 A9 FX/CTA |
| `residual_threshold` | residual balance vs. policy threshold | F28 A10 |
| `expectation_gap` | member present in N of last M periods, absent now | **F29 — all four sub-detectors** |
| `accumulation` | same key, same direction, N consecutive periods; reports the **iron-curtain aggregate**, never the period delta | F9 leg (i) |
| `text_recurrence` | successive explanations on the same key exceed a similarity bound | F9 leg (ii) |
| `peer_coding_divergence` | posting's coding disagrees with comparable postings | F33 |
| `distribution_outlier` | movement outside the account's historical range | F42 |
| **12. `obligation_gap`** *(added gate 10)* | a **declared** obligation with no discharging posting within tolerance. Declaration-derived, not history-derived. Three closed obligation kinds — `scheduled_reversal`, stopped-feed, `intercompany_counterparty` — sharing one computation and differing only in the vocabulary each finding carries | F29 sub-types 2, 3, 4 (`AC-F29-02`/`-03`/`-04`) |
| **13. `journal_attribute_outlier`** *(added gate 10)* | scores a journal against a **closed attribute set** and returns *which attributes* made it an outlier. Attribution, not a distance scalar. **Thresholds are DECLARED, not calibrated** — see the standing rule below | F42 (`AC-F42-02`) |

**Standing rule, introduced at gate 10 with primitive 13 and binding on every
future primitive (§25.2).** A primitive whose thresholds are *declared* rather
than *calibrated against measured performance on real data* must carry an
explicit calibration denial in two places: at its module header, and **on every
finding it emits** — stating the threshold in force, its inclusivity, the closed
set it scored, and that no likelihood, precision or false-positive rate is
claimed. `journal_attribute_outlier` already does this and is the reference
implementation. The rule is stated here rather than left as a property of one
module because the fourteenth primitive is the one that will arrive uncalibrated
and silent, and a reader who meets only the finding must still meet the denial.

**F9 leg (ii) is a registered primitive, not a field on leg (i).** `DOMAIN_KB`
§9 predicts it will be dropped as an implementation detail. Making it a
first-class primitive with its own manifest, its own fixtures and its own
escalation row on Monitors (`UX_KB` §5.9) is the structural reason it cannot be.
Its similarity computation is deterministic (normalised token-set / embedding
cosine against a fixed local model) — **not an LLM judgement**, because a
model asked "are these the same explanation?" reintroduces the nondeterminism
the whole cross-period control exists to escape.

### 7.4 The detector manifest

```yaml
# detectors/manifests/omission.recurring_accrual.yaml
detector_id: omission.recurring_accrual
version: 4
family: omission
population: pop.recurring_accruals@2
inputs: [gl.entries_by_recurrence@5]
evaluator:
  kind: expectation_gap
  params: {min_history_periods: 6, required_hit_ratio: 0.8, tolerance_pct: 0.0}
emits:
  finding_type: omission
  severity_model: sev.by_expected_amount@1
  resolution_types_allowed: [R1, R2, R4, R5, R6]
capabilities_required: [detect.read_certified]
fixtures:
  positive: fixtures/omission/period12_absent.json
  negative: fixtures/omission/period12_present.json
```

Manifests are versioned registry artefacts; their hash enters the dossier and a
manifest change is a control change (obligation J). `resolution_types_allowed`
is where `DOMAIN_KB` §10.2's warning is enforced architecturally: posting types
are *permissioned per detector*, so "posting" can never be the default terminal
state of a finding — most detectors do not permit R3 at all.

Every manifest declares both fixtures. `AC-F36-05`'s negative-control principle
is applied to detectors as well as guardrails: a detector with no failing
fixture is a check that cannot fail, which `PLAN` §2b identifies as actively
harmful.

### 7.5 `integrity/` contains no model call — enforced at runtime

The model client is a single injected object. Entering any `integrity` or
detector evaluator sets a `contextvars` flag; the client raises
`ModelCallForbidden` while it is set, and the harness counts invocations per
run. `PLAN` §11.A criterion 4 asks for a runtime assertion rather than source
inspection, and this gives it one: the test asserts *zero model invocations
observed during an integrity run*, and a violation fails loudly in production
too, not only under test.

---

## 8 · The guardrail broker

### 8.1 Shape

GES runs as its own process, with its own OS user, its own secret mount, its own
log stream, listening on loopback with mTLS. Its public surface:

```
POST /ges/decide          {action_request, context}      → Decision
POST /ges/query           {query_id, version, params, …} → rows + dataset_versions
POST /ges/export/journal  {proposal_id, approval_id}     → file_ref | refusal
POST /ges/revalidate      {proposal_id}                  → POAR result
GET  /ges/bundle                                          → {hash, version, state}
GET  /ges/health
```

No endpoint returns a secret. No endpoint accepts SQL. No endpoint accepts a
policy override as a parameter.

### 8.2 The bundle is a compiled, hash-addressed artefact

Source: a directory of YAML policy files under change control. Build: a compiler
produces a canonical JSON document (RFC 8785 canonicalisation) whose SHA-256 is
the **bundle hash**. The bundle is immutable; an edit produces a new hash and the
prior bundle remains retrievable at its own hash (`AC-F36-15`).

```yaml
bundle_version: 2026.07.31-3
capabilities:
  allow: [detect.read_certified, propose.reclass, export.journal_import]   # DENY-BY-DEFAULT
rules:
  - rule_id: quant.reclass_ceiling
    class: quantitative
    owner: controller.jdoe
    effective_from: 2026-07-01
    effective_to: null
    mode: enforce                       # enforce | shadow
    predicate: "action.kind == 'propose.reclass' && action.abs_value <= money(25000)"
    inclusivity: inclusive              # rendered to the user at approval time
    fixtures: {firing: fx/quant_ceiling_fire.json, non_firing: fx/quant_ceiling_pass.json}
blast_radius:                            # all four REQUIRED; compiler rejects null/unbounded
  max_proposals_per_run: 20
  max_aggregate_value_per_agent_period: {amount: 250000, currency: USD}
  max_consecutive_same_account_periods: 2      # the 3rd escalates
  max_footprint_pct_of_account_balance: 5.0
  max_lines_per_export_batch: 200
routing: …                               # §16
```

**Predicate language.** A closed expression grammar (comparison, decimal
arithmetic, membership, and named accessors from a declared context schema),
evaluated by an AST interpreter. Not Python `eval`, not a plugin, not prompt
text. Two reasons: an auditor must be able to read a rule, and a
Turing-complete rule is not exhaustively testable.

**Compile-time schema binding is the quiet high-value part.** Every predicate is
resolved against the declared context schema at compile time; an unknown field
fails the build. Without this, a typo produces a rule that *silently never
fires* — which is the exact failure obligation N's negative-control suite exists
to catch after the fact. Catching it at compile time is cheaper and earlier.

### 8.3 Deny-by-default is a set test executed before rules

```python
if action.capability not in bundle.capabilities.allow:
    return Decision(deny, reason="not_in_capability_allowlist", ...)
```

This runs *before* any rule evaluation, so a denial never depends on a
prohibition being written (`AC-F36-01`). Capabilities are additionally scoped
per principal: the effective allowlist is
`bundle.capabilities.allow ∩ principal.entitlements`.

### 8.4 The decision record

```
Decision { decision_id (UUIDv7), bundle_hash, principal_id, run_id, action_digest,
           outcome: allow | deny | escalate | allow_shadow_flagged,
           rule_results: [{rule_id, class, mode, fired, reason}],
           blast_radius_state_after, override_ref?, ts }
```

Written to `evidence_db` in the **same transaction** as the state mutation it
authorises. `AC-F36-02` says an action record lacking a bundle hash or decision
ID "does not exist" — enforced by `NOT NULL` plus a foreign key from every action
record to its decision. It is not possible to write one without the other.

**Fail-closed (`AC-F36-17`).** If the bundle cannot be resolved or its hash does
not verify, GES sets `bundle_state = UNRESOLVED` and every `decide()` returns
deny naming the unresolvable bundle. There is no fallback to a cached bundle and
no "last known good" path — a cached-bundle fallback is a silent policy
downgrade, which is worse than an outage.

### 8.5 Blast radius — the part that is genuinely hard, and where it is easy to get wrong

`industry-expert` calls this the highest-value guardrail in the system. It is
also the only one whose correctness is a **concurrency** property.

State lives in `app_db.blast_radius_ledger`, keyed at three grains:

| Grain | Key | Cap |
|---|---|---|
| Run | `(tenant, run_id)` | `max_proposals_per_run` |
| Agent-period | `(tenant, principal_id, period)` | `max_aggregate_value_per_agent_period` |
| Account-direction | `(tenant, principal_id, account_combination, direction)` | `max_consecutive_same_account_periods` |
| Proposal | evaluated against target balance | `max_footprint_pct_of_account_balance` |

**The decision and the counter increment commit in one `SERIALIZABLE`
transaction, with the aggregate row taken `FOR UPDATE`.** If they are separate,
two concurrent runs each read a counter below the cap and both pass — the cap is
then advisory in exactly the circumstance it exists for. Denials do not
increment; allows do; overrides increment *and* set a flag.

`AC-F36-13` (non-disableable at every permission level, including
administrator): the caps live in the bundle and **there is no runtime write path
to them at all** — no API, no admin screen, no environment variable. Editing
requires a new bundle, and the compiler rejects a bundle in which any of the four
caps is absent, null or unbounded. So "edit toward disabled" fails at build time
and there is no other door.

### 8.6 Overrides

`Override { override_id, decision_id, authoriser_a, authoriser_b, reason_code
∈ closed list, created_at, consumed_at, scope: single_action }`. Three
constraints, all at the storage layer rather than in validation code: a partial
unique index enforces one consumption per override; `authoriser_a ≠
authoriser_b ≠ requester ≠ agent_author` is a check constraint plus an SoD rule
in the bundle's identity class; and **there is no column in which a standing or
open-ended scope could be represented** (`AC-F36-08`). Override rate per agent,
per user, per period is a materialised view feeding Monitors, and zero renders
as an explicit zero with its denominator (`AC-F36-19`).

### 8.7 Negative controls, and the trap in obligation N

The scheduled negative-control suite runs **against the live bundle** each close
and on every bundle change: for each rule, execute its firing fixture and its
non-firing fixture and assert both outcomes. A rule missing either fixture is
reported by name as `unevidenced` and the suite fails (`AC-F36-05`).

Obligation N's trap is explicit and I want it named for `code-agent`: **do not
log non-events.** There is no "rule evaluated and did not fire" record. The
action log carries one record per attempted action, and rule results live inside
that record — so `AC-F36-06`'s assertion ("contains no records asserting that a
rule did not fire") is about *standalone* non-event records, and the `rule_results`
array inside a decision record is not one. That distinction is easy to
misimplement in either direction and I am stating which side is correct.

### 8.8 Shadow mode

`mode: shadow` rules evaluate, do not block, and emit
`allow_shadow_flagged` with the rule named (`AC-F36-14`). A new rule enters in
shadow, runs for a configured observation period, and is promoted by a bundle
change — which is itself a change record with an owner (obligation J).

---

## 9 · Evidence: the dossier store, tamper-evidence and retention

### 9.1 Technology choice, and the one I rejected

**Chosen: PostgreSQL 16, a separate database (`evidence_db`) with a separate
application role granted only `INSERT` and `SELECT`, plus a hash chain, plus
daily signed anchors, plus nightly archival to object storage under an Object
Lock retention of seven years.**

Rejected: a dedicated WORM/immutable-ledger product (QLDB-style ledger
databases, blockchain-backed stores, per-row object-lock writes). Reasons: (a)
per-row WORM object writes on an operational latency path is over-engineering
for MVP1 and would put an availability dependency in front of every finding;
(b) ledger-database products bind the customer's evidence to one cloud vendor,
which is a poor property for a seven-year artefact; (c) the property obligation G
actually demands is *append-only, tamper-evident, exportable without the
application* — all three of which the design below delivers with parts the team
already operates.

`PLAN` §9.3 asks specifically whether the operational store and the evidence
store share infrastructure and how the no-update guarantee is enforced at the
storage layer. The answer: **they share a Postgres cluster and nothing else.**
Separate database, separate role, separate connection pool, separate credential.
The application's evidence role has no `UPDATE`, no `DELETE`, no `TRUNCATE` and
no DDL grant; migrations run under a different role that is not available at
runtime. `evidence/store.py` exposes no update or delete function — but the
grant is what makes it true, because a missing function is a convention and a
missing grant is an error.

`AC-F1-02` requires that an attempted mutation *fail and itself be recorded*.
Implementation: the failed statement raises at the database; the application
catches the error and appends a `mutation_attempt` control event (an insert,
which the role can do).

### 9.2 Tamper-evidence: hash chain plus signed anchors

```
record.content_hash = SHA256(JCS(record.payload))
record.entry_hash   = SHA256(prev_entry_hash ‖ content_hash ‖ seq ‖ ts ‖ tenant)
```

One chain per tenant, serialised by a Postgres advisory lock on append. Daily
(and on every bundle change, and at every period close), an **anchor** is
written: `{seq_range, head_entry_hash, ts}` signed **Ed25519 by a key held in
KMS in sign-only mode** — the application can request a signature and cannot
read the private key. Anchors are also written to the object store under Object
Lock.

Why this is enough and not more: a row edit breaks the chain from that row
forward (`AC-F1-03` — verification reports the dossier as modified and
identifies it); rewriting the chain forward requires forging every subsequent
anchor signature, which requires the KMS key. That is tamper-*evidence*, which
is what obligation G asks for. Tamper-*proofing* is a different and much more
expensive property that nobody has asked for.

**Verification is offline-capable.** The auditor export ships the chain
segment, the anchors and their public key; recomputation needs `sha256sum` and
an Ed25519 verifier, not our application (`AC-F1-04`).

### 9.3 Retention — seven years, attaching to the decision

`INDUSTRY_KB` §4.3: seven years is the design target, configurable upward, and
the obligation attaches to *our* decision record, not to the ledger, which is
Oracle's. Every dossier carries `retention_expiry` (computed at write:
`created_at + tenant.retention_years`, default 7) and returns it on retrieval
(`AC-F1-08`). Nightly, a job writes each period's sealed dossiers as an
immutable bundle to object storage with `retain-until = retention_expiry` in
compliance mode — so the archive cannot be deleted by us, by an administrator,
or by a compromised credential, for seven years.

A dossier at the oldest end of retention must return **complete** (`AC-F1-08`),
which means no schema migration may ever drop or rename a dossier field. Dossier
payloads are therefore versioned and read through a **schema-versioned reader**
that can materialise every historical version. This is cheap now and impossible
later; `code-agent` must not treat the dossier payload as an ordinary evolving
model.

### 9.4 The rendered view — the mechanism `AC-F41-04` depends on

This is the piece most likely to be built wrong, so it is specified concretely.

**The evidential region of the Review screen is server-rendered.** Given
`review_payload` (an immutable JSON document produced when the proposal is
created) and `presentation_template@version`, a pure server-side renderer emits
**self-contained HTML with all styles inlined, no external assets and no
JavaScript**. The browser displays exactly those bytes inside the Review page;
the interactive controls (resolution row, reject dialog) sit *outside* the
evidential region.

Retained in the dossier: the HTML bytes, their SHA-256, the template version and
the payload id. Retrieval reproduces what the approver saw regardless of how the
underlying data has since changed, because nothing in the artefact reads the
database.

Three consequences, all binding on `code-agent`:

1. **The evidential region must be a pure function of `(review_payload,
   template_version)`.** This is the architectural statement of `UX_KB` §5.4's
   rule that nothing may be hover-only, lazy-loaded or live-refreshing — a fact
   fetched after render is a fact absent from the evidence.
2. **Determinism is testable**: same payload + same template ⇒ byte-identical
   HTML (ARCH-16). If it is not byte-identical, the retained artefact is not the
   thing that was shown.
3. ~~Because styles are inlined, gate 5's strengthened `AC-F41-03` (riskiest
   element at the largest computed font size) is checkable *in the retained
   artefact*, offline, years later — not only in a live browser.~~
   **WITHDRAWN 2026-08-06. This sentence was wrong when I wrote it on
   2026-07-31, and wrong for a reason that has nothing to do with styling —
   see §25.4bis. `AC-F41-03` is a *Review screen* criterion; the retained
   rendered view is of the *approval* screen. I asserted a property of one
   screen was checkable in an artefact of a different screen.** The replacement
   consequence is: *the retained artefact reproduces what the approver was
   shown, and the approver was not shown the risk band, so the artefact does
   not carry it and must not.*

**Amended 2026-08-05 (gate 10 ruling 4, §25.4) — "the retained artefact" is two
artefacts, and only one of them is style-inlined.**

`code-agent` flagged the divergence rather than letting it pass, and it is a real
one:

| Artefact | Produced by | Style-inlined? |
|---|---|---|
| The `/dossier/<id>` exhibit | `chrome.page(..., chrome_on=False)`, which emits `<style>` with `chrome.stylesheet()` | **Yes** |
| The **export's** per-dossier `rendered_view` | `app.ui.retained.render()` → a bare `tree.render()`, written straight into the export at `app/evidence/export.py` | **No** |

~~**Ruling: inline it in the export copy too. The consequence-3 claim above stands
as written and the build must meet it.** The deciding fact is not the 280 KB —
it is that the size emphasis exists *only* in the stylesheet
(`.riskband .big{font-size:__RISK__px}`), so the export's copy carries no
font-size information at all and `AC-F41-03` is not merely hard to check there,
it is **unverifiable in principle**.~~

**SUPERSEDED 2026-08-06 (gate 11) — this reasoning was falsified in a browser.**
The artefact carries **neither** the size nor the element: `riskiest-figure` is
absent from it entirely, because the retained region derives from the *approval*
screen and the risk band lives on Review. Inlining the stylesheet would not have
made `AC-F41-03` checkable here, because the element it is about is not present
to size. The outcome — inline it — survives; **the reason does not, and the
reason is what a future reader would have relied on.** Re-ruled at §25.4bis.

A PNG rendering is generated at auditor-export time for convenience and is
labelled **derived**; the HTML plus its hash is the evidence.

### 9.5 Capture (F12) rides the same payload

Expansion events (`AC-F12-03`) are emitted by the evidential region's disclosure
controls against element ids that exist in `review_payload`. Because the payload
and the rendered artefact are the same object, "which evidence did the reviewer
expand" is recorded against identifiers that still resolve years later. Gate 5's
decision to collapse the narrative is what gives this column information
(`UX_KB` §2), and this is the mechanism that makes the column meaningful rather
than merely present.

### 9.6 Probes — the data model, deliberately not the decision

`responsible-ai-architect` rules on reveal timing; I am not pre-empting it. The
schema supports either ruling with no migration:

```
Probe { probe_id, injected_at, run_id, presented_at, disposed_at,
        reviewer_response, correct_answer, revealed_at NULL | ts, reveal_policy }
```

What the architecture must guarantee either way (`AC-F41-08`, `UX_KB` §5.6):
probe status is absent from the response payload, the DOM and any distinguishing
class name **before disposition**. Implementation: the probe flag is never
serialised into `review_payload`; it lives only in a server-side join. That is
the property to test (ARCH-17), and it holds under both rulings.

The one architectural cost worth stating for `responsible-ai-architect`:
immediate reveal requires a *second* server round-trip after disposition that
returns the correct answer, and that round-trip must not be able to mutate the
disposition already recorded. Deferred reveal has no such requirement. Neither
is expensive; I note it so the ruling is made with the cost visible.

---

## 10 · The export path and the two-key boundary

### 10.1 What MVP1 emits

An Oracle **Journal Import**–shaped file (FBDI/`GL_INTERFACE` column set),
balanced, every line naming ledger, period, account combination and amount
(`AC-F40-01`), with:

- `USER_JE_SOURCE_NAME` = the dedicated source reserved for this system;
- `USER_JE_CATEGORY_NAME` = the dedicated category;
- one `GROUP_ID` per export batch;
- **our identifiers stamped into the reference/attribute columns**:
  `proposal_id`, `dossier_id`, `decision_id`, `run_id`, `principal_id`.

That last item is a deliberate design decision (J-9). It makes every entry this
system ever caused joinable back to its dossier *from the customer's own
ledger*, which is obligation S's enumerability property obtained where it
survives the loss of our store. It also supplies the mechanism for `AC-F40-10`:
the Oracle document ID for a posted (or later reversed) entry is matched back
through F26's ERP control extract on these reference columns, and the reversal
linkage is written as a new append-only record — never a mutation of the
original (obligation H).

### 10.2 Enforcement is at GES, in a fixed order

Listed in §4.4. The order matters: approval validity first (cheapest and most
common refusal), CUEC next (a tenant-level fact), blast radius next (needs a
transaction), POAR last (the only check that costs an external round trip).
Every refusal produces a decision ID and is recorded.

`AC-F40-02` — no posting credential resolvable anywhere in the build — is
satisfied structurally: MVP1's GES secret mount contains a warehouse read
credential, an ERP control-read credential and the export signing key. It
contains no Oracle posting credential, and the export component has no code path
that submits anything. Phase 2's F17 adds a credential to the *existing* boundary
rather than creating one.

### 10.3 CUECs as data, verified per tenant

```
CuecItem { cuec_id, description, verification_method, tenant_id,
           last_verified_at, verified_by, result, validity_days, next_due }
```

MVP1's checklist: journal approval enabled and required for our source and
category; AutoPost unable to post our source unapproved; per-agent Oracle
identity provisioned; ETL completeness attested; source-extract integrity
attested. `deploy-agent` runs verification at deployment and records the result;
export refuses on missing, failed or expired verification (`AC-F40-05`).

**Honest limitation, stated rather than glossed.** We cannot detect an Oracle
tenant configuration change on our own. Obligation S wants re-verification "on
configuration change"; MVP1 approximates it with a **validity window (default 30
days) plus re-verification at every deploy**, which means there is a window in
which a customer could disable journal approval on our source and we would
export against a verification that is stale-but-valid. Two mitigations, both
cheap and both in scope: the CUEC verification date is rendered on the export
screen (`UX_KB` §5.5 already shows it), and POAR reads Oracle period status
anyway, so the ERP read channel exists to extend into an approval-configuration
probe. **I am not adding that probe to MVP1 scope** — it is `plan-agent`'s call —
but the channel is there and the gap is named rather than discovered at audit.

---

## 11 · Coverage as a type, not a validation

`UX_KB` §5.3 states the requirement precisely: *coverage changes the grammar of
the conclusion.* That is a type-level statement and it is implemented as one.

```python
class FullPopulationConclusion:   # the ONLY type with a no-exceptions variant
    __private_init__ = True
    scanned: int; declared: int   # invariant: scanned == declared

class BoundedConclusion:
    scanned: int; declared: int
    named_gaps: NonEmptyList[SegmentRef]     # required, non-empty, by type
    # no field, method or template can produce an unqualified all-clear

class NoScanConclusion:
    # renders NO findings region at all (AC-F38-08)

Conclusion = FullPopulationConclusion | BoundedConclusion | NoScanConclusion

def conclusion_for(run: Run) -> Conclusion:      # the only constructor
    if not run.scope.covered:            return NoScanConclusion(...)
    if run.scope.uncovered:              return BoundedConclusion(..., named_gaps=run.scope.uncovered)
    return FullPopulationConclusion(...)          # unreachable with a non-empty gap set
```

Three properties fall out:

1. **`no_exceptions` is unreachable below full coverage** — not validated out,
   not guarded by an `if`. There is no object in the program that can hold the
   state "clean at 70%".
2. **One object, three renderers.** Screen, dossier and export each render from
   the same `Conclusion`. `AC-F38-04`, `-05`, `-06` and `-07` require the same
   qualification in all three; three independent implementations would drift,
   and `AC-F38-07`'s "identical is a failure" test would eventually be satisfied
   by accident in one surface and not another. One object makes drift impossible.
3. **A lint gate makes the claim falsifiable.** The strings `"no exceptions"`,
   `"clean"` and `"all clear"` may appear in exactly one module — the conclusion
   templates — and only within the `FullPopulationConclusion` template. CI fails
   otherwise. That is the cheap check that keeps the expensive property true as
   the codebase grows.

Coverage itself is `|covered_members| / |expected_members|` over the population's
**member keys** (§7.2), and `named_gaps` are the uncovered members rolled up to
their declared segments — which is what lets the Ask screen name them.

---

## 12 · Resolution, forward disposition and the R6 state change

### 12.1 Resolution types are permissioned data, not a UI enum

`Finding.resolution_types_allowed` comes from the detector manifest (§7.4), so
R3/R4 are unavailable on detectors that must not propose postings. This is the
architectural half of `DOMAIN_KB` §10.2 — the safe answer must not be harder to
record than the risky one — and it complements gate 5's equal-weight resolution
row rather than duplicating it.

Type-specific required fields, enforced as `NOT NULL` conditional constraints:
R1 → `expiry_date` and typed explanation; R5 → `owner_principal` and `due_date`;
R6 → the target control-state change. R2 requires nothing beyond the clearing
period, which is why it is the three-step path in `UX_KB` §5.4.

### 12.2 Forward disposition — retrofit-hostile, so it is a column constraint

`expected_clearing_period` is `NOT NULL` on `disposition`, and the write path
has **no overload without it**. `AC-F32-01` says unsaveable at every permission
level, as a hard failure and not an acknowledgeable warning — a database
constraint is the only implementation of that sentence that survives a future
"admin bypass" feature request.

The verification job is registered **at deploy time**, not added later: a
scheduled worker task that, on each period rollover, tests every prior-period
prediction against reality and, on a miss, executes an **R6 state change** —
risk grade raised, auto-pass eligibility revoked — written as a state transition
with its own decision record, not a notification (`AC-F32-03`, `PLAN` §11.E-28).
A lapsed R1 re-enters the queue **carrying its original explanation** as an
attached artefact reference, which the evidence store makes trivial because the
original is immutable.

### 12.3 R6 is why detection has consequence

`PLAN` §5.1: a detector needs a state change, not a signal. `AccountControlState
{ account_combination, risk_grade, auto_pass_eligible, last_changed_by_decision }`
is read by the routing policy (§16), so an R6 change *mechanically* alters what
reaches a human next period. Without that read, R6 is a label; with it, it is a
control.

---

## 13 · Runs are immutable; supersession is loud

`Run` is append-only: `OPEN → COMPLETE → (SUPERSEDED_BY_RUN | SUPERSEDED_BY_DATA
| SUPERSEDED_BY_SOURCE)`. A re-run never overwrites. An approval binds to a
`run_id` and a `review_payload_id`; supersession invalidates it and the action
area is structurally replaced rather than warned over (`UX_KB` §5.4 — a disabled
approve button still tells a tired reviewer that approving was expected, so the
control is *absent*).

Three supersession causes, one treatment. The second is not covered by any
criterion today — §18.1.

---

## 14 · Cross-cutting spine

### 14.1 Version registry (F2, obligations I, J)

One table, one shape, for every versioned artefact: model, prompt, tool/config,
corpus, dataset, guardrail bundle, detector manifest, population, certified
query, join, measure, presentation template, refusal registry.

`Run` validates at open that **every** artefact version it intends to use is
registered, and refuses naming the unregistered one (`AC-F2-04`). Stamps are
copied by value into the dossier, never referenced by "current" (`AC-F2-02`).
Change records carry what changed, prior and new identifiers, owner and
effective date (`AC-F2-03`); a period with no changes says so explicitly
(`AC-F2-06`).

### 14.2 Model deprecation as a compliance dependency (obligation K)

Constraint 3 says provider deprecation schedules become a compliance dependency.
Concretely:

```
ModelLifecycle { provider, model_id, status, announced_deprecation_at,
                 retirement_at, source_ref, owner, last_checked_at }
```

Maintained from a curated `provider_lifecycle.yaml` under a named human owner,
refreshed by a scheduled job. Controls:

- A run using a deprecated version carries the deprecation notice in its output
  and its dossier (`AC-F2-05`).
- Inside 90 days of retirement, a control event is raised and surfaced on
  Monitors.
- A deprecated version may not be **introduced** to a skill; an existing skill
  migrates via a change record that requires the negative-control suite to be
  re-run and a sample of prior-period findings to be re-verified before the swap.

**And the corollary that makes this survivable**: because reproducibility here
is *evidential* rather than re-executional (constraint 3), a retired model does
not destroy a past decision's defensibility. The dossier still states what data
version, what policy bundle, what coverage, what the approver saw, and who
approved. This is the single largest reason the evidential-reproducibility
decision is correct, and it should be said out loud to auditors rather than
discovered by them.

### 14.3 Identity, inventory and lineage (F5, obligation D)

Principals are registered at **bundle/skill compile time** from the skill
manifests, so the Inventory is a projection of the registry and there is no
manual registration step (`AC-F5-02`). Each principal has its own entitlement set
and its own log stream.

Lineage completeness (`AC-F5-03`, "complete rather than sampled") is made
structural by an **`artefact_touch` ledger** written by the single shared
evidence write path (§4.5): `(principal_id, principal_version, run_id,
artefact_type, artefact_id, ts)`. Lineage is then one index scan, not a join
across N tables that a future feature forgets to extend — which is exactly how
this claim normally becomes false. Where traversal genuinely cannot complete, the
result is labelled `incomplete` and names what could not be traversed
(`AC-F5-05`); a retired principal's rows are never removed (`AC-F5-06`).

### 14.4 The refusal registry (F50)

`refusal/registry.yaml` — a compiled, versioned artefact listing A19–A22 and the
three outright refusals, each with `kind: refused_permanently | deferred`,
reason, and the wording that carries the distinction **in text alone with all
styling stripped** (`AC-REFUSAL-06`). Refusal events are written to the evidence
store like any other control event (`AC-REFUSAL-04`). Making this a compiled
artefact rather than hard-coded strings is what lets `AC-REFUSAL-05` — a null or
generic response is a failure — be checked against a list rather than against a
reviewer's memory.

---

## 15 · Where the agent runtime sits, and why there is no LangGraph

### 15.1 The decision

**No LangGraph in MVP1. No ReAct loop. The agent runtime is an explicit,
bounded finite-state machine in the `api` process, invoking the model at exactly
three call sites.**

The template ships `langchain`, `langchain-anthropic` and `langchain-openai`;
those stay, used **only** as provider SDK wrappers for a single completion call
with a tool schema. No new dependency is added. `plan-agent` noted that porting
the react-agent pattern is cheap; I am declining it, and the reasoning is not
cost.

### 15.2 Why

The model has three jobs in this product, and none of them is planning:

| # | Job | Input | Output | Determinism |
|---|---|---|---|---|
| 1 | **NL resolution** (F39) | user text + query catalogue | `Resolution` (closed enum + params) | temperature 0, schema-validated, user-confirmed before submit |
| 2 | **Finding rationale drafting** | a *completed* deterministic finding | prose attached to a finding | never alters the finding; band-G output is refused elsewhere |
| 3 | **Structured-field extraction** for a proposal (e.g. suggested reclass target from `peer_coding_divergence` evidence) | detector output | typed fields, guardrail-checked | validated against the certified layer |

Detection is deterministic Python. Guardrails are a policy engine. Export is a
file writer. There is no multi-step autonomous plan for a graph to orchestrate —
and a ReAct loop's defining property is that *the agent authors its own next
step*, which is precisely what the deny-by-default capability allowlist exists
to prevent. Adopting an agent framework here would import an execution model the
product's control narrative refuses, and then spend the rest of the build
constraining it back.

There is a second, quieter reason. An agent framework's value is state
management across a long, branching interaction. This system's durable state is
the `Run` — already immutable, already versioned, already evidence. A framework
checkpointer would be a *second* state model sitting beside the one the auditor
reads.

### 15.3 Keeping `plan-agent`'s cheap port cheap

The FSM's step interface is deliberately shaped like a graph node:

```python
def step(state: RunState) -> tuple[RunState, StepOutcome]: ...
```

Pure, serialisable state in and out. If phase 2 brings a skill that genuinely
needs branching, checkpointed, multi-step execution — cross-source omission
detection (P1) is the plausible candidate — LangGraph can wrap these functions
as nodes without rewriting them. **Reversal condition (J-6):** a phase-2 skill
requiring ≥3 conditional branches with durable mid-run checkpointing.

### 15.4 Model invocation discipline

One injected client, one wrapper, every call stamped with model version, prompt
version, temperature and token counts into the run record. The `contextvars`
guard of §7.5 makes calls from `integrity/` and from detector evaluators raise.
Provider selection stays `LLM_PROVIDER`-driven per the template.

---

## 16 · The decision `PLAN` §9.3 handed to this gate: per-action vs. policy-cold / exceptions-hot

### 16.1 The decision

**Both, and the seam between them is the guardrail bundle.** Per-action approval
is retained, unchanged, for everything that reaches a human. What *reaches* a
human is governed by routing policy that is approved cold, versioned, hashed and
owned — and that cold path is itself under cross-period surveillance.

### 16.2 Why this is not a weakening of per-action approval

`DOMAIN_KB` §7.2's attention-budget argument is that a fortieth approval at 11pm
is not a control. The remedy the research supports is **volume reduction**, and
volume reduction means some findings are disposed without a human. The honest
framing is that this already exists in the design — `UX_KB` §5.2's mockup shows
205 of 214 detections not routed — and the only question was whether the
mechanism would be a policy artefact or an accident of thresholds.

Making it a bundle object means every auto-disposal carries a bundle hash, a
rule id, an owner and an effective date, and is therefore an ICFR change-control
object rather than a configuration setting.

### 16.3 The four constraints, without which this is a defect

1. **Auto-disposal is never available to a Tier 2 / posting-capable outcome.**
   A finding whose `resolution_types_allowed` includes R3 or R4 is always hot.
2. **An auto-disposed finding still gets a dossier** carrying the bundle hash and
   the disposing rule, and is listed and reachable on Exceptions — `UX_KB`
   §10.2's assumption U1, which I am adopting architecturally rather than
   leaving as a UI courtesy. A suppression nobody can inspect is the trust this
   product should be earning.
3. **Cold policy is under cross-period surveillance.** A finding auto-disposed
   on the same account, same direction, in three consecutive periods escalates
   hot regardless of the rule that disposed it — the same `accumulation`
   primitive F9 uses, pointed at the cold path. **Without this constraint,
   policy-cold disposal reconstructs `DOMAIN_KB` §6.2's self-justifying
   reconciling item in automated form and removes the human who was the last
   chance to notice.** This is the constraint I will not trade.
4. **The routing budget is a routing-policy field** (gate 5 decision (b)):
   `max_routed_per_reviewer_per_night`. When a run would exceed it, the run says
   so and a controller either raises the cap — a bundle-scoped, decision-ID'd,
   recorded control event — or splits the queue. It still needs an acceptance
   criterion (§18.3).

---

## 17 · Judgement calls register

Each is a call I made under the standing authorization, with what would reverse
it. Recorded so they are reviewable after the fact rather than inferred from
code.

| # | Call | Why | What reverses it |
|---|---|---|---|
| **J-1** | **GES is a separate process, not a module** | A module boundary is bypassed by `import` and by a prompt-injected tool; obligations E and M reduce entirely to this line being real | `security-architect` proposing a stronger boundary (separate host/VPC) — that is a strengthening, not a reversal. Nothing weaker is acceptable |
| **J-2** | **Postgres + hash chain + KMS-signed anchors + Object-Lock archive**, not a WORM/ledger product | Delivers append-only, tamper-evident, 7-year, exportable-without-the-app with parts the team operates; avoids a per-row availability dependency and vendor lock on a 7-year artefact | A customer contractually requiring a named immutable-store product, or a regulator rejecting hash-chain-plus-anchor as tamper evidence |
| **J-3** | **Evidence and operational data share a Postgres cluster, nothing else** — separate DB, role, pool, credential; no `UPDATE`/`DELETE` grant | Answers `PLAN` §9.3 directly. Storage-layer enforcement, not convention | Evidence volume or a tenancy requirement forcing physical separation |
| **J-4** | **NL resolver at temperature 0 with a closed-enum output, validated server-side and confirmed by the user before submit** | Converts an invisible failure (wrong join) into a visible one (wrong named question) | Nothing foreseeable; the alternative is the failure `DOMAIN_KB` §10.8 describes |
| **J-5** | **No LangGraph, no ReAct; explicit FSM** | The model does three narrow jobs; a self-directing loop is what the capability allowlist exists to refuse | A phase-2 skill needing ≥3 conditional branches with durable mid-run checkpointing (§15.3) |
| **J-6** | **Detectors = manifest + registered primitive**; new primitive is code | Bounds the "configuration not code" claim honestly. All four F29 sub-detectors are one primitive, which is the evidence the bound is placed right | A long tail that repeatedly needs new primitives — that would mean the primitive set is wrong, not the model |
| **J-7** | **Coverage as a closed sum type with a private full-population constructor**, plus a one-module lint gate on the words | `UX_KB` §5.3 asks for structural impossibility; validation can be bypassed and types cannot | None; this is the cheapest implementation of a stated requirement |
| **J-8** | **POAR before every Tier 2 egress**, reusing F26's ERP control-read channel | Closes `DOMAIN_KB` §5.7 at the moment of action rather than disclosing it at the moment of analysis; adds no new integration | A tenant with no ERP read access at all — in which case Tier 2 should not be enabled for that tenant |
| **J-9** | **Our identifiers stamped into Journal Import reference columns** | Obligation S's enumerability obtained on the customer's ledger, surviving loss of our store; also the mechanism for `AC-F40-10` reversal linkage | Oracle column-availability constraints in a specific tenant |
| **J-10** | **Server-side rendered, self-contained, style-inlined evidential region** as the retained rendered view | Client-side screenshotting is unverifiable and non-deterministic; this makes `AC-F41-04` and gate 5's font-size criterion checkable offline | A requirement to retain a pixel-exact image as primary evidence rather than as a derived convenience |
| **J-11** | **Decision and blast-radius state commit in one SERIALIZABLE transaction** | Otherwise concurrent runs each pass the cap and the highest-value guardrail is advisory exactly when it matters | Nothing; this is a correctness requirement, not a preference |
| **J-12** | **CUEC re-verification approximated by a 30-day validity window plus per-deploy verification** | We cannot observe an Oracle config change; the honest approximation is stated in §10.3 rather than the obligation being claimed as fully met | `plan-agent` adding an Oracle approval-configuration probe to scope — the read channel already exists |

---

## 18 · What I could not settle, and two new findings

### 18.1 ~~FINDING~~ **RESOLVED 2026-08-05 (gate 10)** — supersession by *data* now has two criteria, and they are built and executing

> **This finding was stale, not merely disclosed, and `review-agent` was right to
> say so.** The text below asserted an *absence* — "nothing at the Test gate
> would catch it being dropped" — that another KB and the build have since
> filled. A KB that keeps asserting a gap somebody else closed is worse than one
> that never raised it: a reader trusts the assertion and stops looking. The
> original text is retained verbatim below because the request it made is what
> was answered, and striking it would hide that the mechanism worked. **What is
> no longer true is marked.**
>
> **What closed it.** `functional-design-agent` issued exactly the requested
> shape — `AC-F41-14` (block, naming the dataset and the newer as-of) and
> `AC-F41-15` (**the negative half**: a newer watermark on a dataset the run did
> *not* bind must not block and must show no notice), `FUNCTIONAL_SPEC` §27.1.
> `-15` was not requested by me and is the better half of the pair: without it a
> build passes `-14` by blocking every pending approval whenever any warehouse
> object moves, which on a nightly warehouse means the control is switched off
> within a week.
>
> **How it is built** (`code-agent`): computation in `dev/backend/ges/supersession.py`
> over §5.5's `run_dataset_binding`, with no global "the warehouse moved" flag
> anywhere — the module states that omission as deliberate, and it is the design.
> Enforcement is **not** in that module and **not** in the UI: it is bundle rule
> `scope.no_bound_dataset_superseded_by_later_data`, `mode: enforce`,
> `override_eligible: false`, whose two context fields `/ges/decide` resolves
> server-side from the GES registry and discards if a caller supplies them. The
> screen's `approval-blocked-by-data` element is *display* of a fact the broker
> already enforced; deleting it does not make the approval succeed.
>
> **Why the Test gate now catches it being dropped — including the negative half.**
> The rule carries `fixtures: {firing, non_firing}`, and §8.2 makes fixture
> evaluation part of **bundle compilation**. `AC-F41-15`'s case *is* the
> `non_firing` fixture. So the negative half is verified at compile time on every
> build, not only when somebody remembers to run a scenario — which is a stronger
> position than the one this finding asked for. Watermarks are compared as
> instants and an unparseable one raises rather than comparing false.
>
> **Verified by me at gate 10** by reading the criteria, the module, the bundle
> rule and the UI element — not by accepting the report. `test_supersession_by_data.py`
> exists in the functional suite; I do not own that suite and do not claim its result.
>
> **Consequence for the architecture: none.** §5.5 described this behaviour
> correctly all along; what was missing was the criterion, and it is no longer
> missing. No design change follows.

**Original text, 2026-07-31 — retained as history. The struck sentence is the
one that is now false.**

`AC-F41-12` covers a run superseded by a **later run**. §5.5 establishes that the
more common real case is a run superseded by **later data** — the warehouse
watermark moves after a run completes but before its proposal is approved. The
architecture handles it identically, but no criterion asserts it, so ~~nothing at
the Test gate would catch it being dropped~~ **[FALSE as of `AC-F41-14`/`-15`;
see the resolution block above]**.

**Requested**: a new ID from `functional-design-agent`, in the shape —

> *Given a completed run whose bound dataset version has since been superseded
> by a newer watermark; when an approver attempts to approve a proposal from
> that run; then the approval is blocked and the block names the dataset and the
> newer as-of.*

I am not issuing the ID; that is `functional-design-agent`'s lane.

### 18.2 FINDING — native mobile approval (F24) is architecturally incompatible with the rendered-view mechanism as designed

`PLAN` §7.5 marks F24 **RECOMMEND REJECT** on control grounds. There is now an
architectural reason as well, and it is worth recording because it will
resurface as a "just add a mobile client" request.

`AC-F41-04`'s retained rendered view is the **server-rendered, self-contained
HTML** of §9.4. A native mobile client that renders its own approval screen from
JSON produces a *different* artefact from the one retained, and the evidence
then does not reproduce what the approver saw — obligation A fails silently, on
the lowest-scrutiny surface, which is the worst possible place for it to fail.

Native mobile approval is therefore only viable if the native client displays
the same server-rendered artefact in a webview. That is buildable, but it means
the mobile approval surface cannot be a native-feeling screen — which removes
most of the reason to want it. **This does not block anything in MVP1**; it is a
constraint recorded now so F24 is re-decided with it visible. Mobile
*read/monitor/notify* (F23) is unaffected — it retains nothing evidential.

### 18.3 ~~Carried forward, needing a criterion~~ **SUPERSEDED 2026-08-05** — the routing budget

> **No longer open.** `AC-F41-16` (items beyond the cap are not routed; the run
> states the cap was reached, for which reviewer, and how many were held) and
> `AC-F41-17` (raising the cap is a controller-only control event carrying a
> decision ID, prior and new cap and the night; rejected at every other
> permission level including administrator) exist in `FUNCTIONAL_SPEC` §27.1.
> The sentence "it is currently unenforced at the Test gate" is false. Corrected
> in the same sweep as §18.1 rather than left as a second stale absence — see
> §25.1.

**Original text, 2026-07-31 — retained as history:**

Gate 5 decision (b) accepted a per-reviewer-per-night routing budget and
`UX_KB` §9.2 flagged that no criterion makes volume *bounded*. §16.3(4)
implements it as a routing-policy field. It still has no acceptance criterion, so
it is currently unenforced at the Test gate. `functional-design-agent`'s lane.

### 18.4 Genuinely undecidable by me — carried, not re-opened

- **Public vs. private filer** (`PLAN` §9.1, `INDUSTRY_KB` §15.5). Open since
  gate 1. It does not change this architecture: every component here is built to
  the public-filer floor, and a private-filer answer would relax *scope*
  decisions, not design ones. No build decision is blocked.
- **Probe reveal timing.** Deliberately left to `responsible-ai-architect`
  (§9.6). The architecture is indifferent; the cost of each option is stated.

---

## 19 · IMPACT ANALYSIS — mandatory (Architecture pass 1, MVP1 baseline)

This is pass 1, so this section does double duty: it establishes the project's
**surface register**, which every future enhancement must enumerate against, and
it performs the analysis for this pass. A future enhancement that does not list
every row below — reached or not, with a reason — blocks the Architecture gate.

### 19.1 The surface register — every surface this *project* has

Enumerated from the project, not from what this change happens to touch. Six
surfaces. `PROJECT_CONTEXT.md` names three (desktop web, mobile web, native
mobile); the other three are surfaces the system genuinely has and that a
UI-only enumeration would miss — which is the exact under-counting my contract
exists to stop.

| # | Surface | In MVP1? | Independently shipped face |
|---|---|---|---|
| **S1** | **Desktop web** — nine screens | **Yes** | The product's only human UI in MVP1 |
| **S2** | **Backend HTTP API** (`api` and `ges`) | **Yes** | Reachable independently of the front end — `AC-F36-03` asserts exactly this. A surface by construction |
| **S3** | **Data / export pipeline** — Oracle Journal Import file | **Yes** | Consumed by a human loading it into Oracle; drifts independently of the UI |
| **S4** | **Evidential deliverables** — F1 auditor export, dossiers, CUEC checklist, published customer obligations | **Yes** | Consumed by an auditor **with no application login**; the surface most likely to go stale unnoticed |
| **S5** | **Mobile web** | No | Product roadmap; no MVP1 build target |
| **S6** | **Native mobile** (F23 read/monitor, F24 approval) | No | Product roadmap; F24 recommend-reject |

### 19.2 Which surfaces this pass reaches

| Surface | Reached? | Reasoning — falsifiable |
|---|---|---|
| **S1 Desktop web** | **REACHED** | Three architecture decisions change what the front end may do: (a) §9.4 — the evidential region is server-rendered and the client renders those bytes verbatim, so the Review screen is not free to compose its own approval view; (b) §11 — the conclusion component consumes a `Conclusion` sum type and cannot construct its own conclusion text; (c) §5.3 — every figure carries `dataset_version`, provenance and close-clock staleness from the payload, so no screen may render a bare number. Falsify by finding a screen that composes conclusion text or renders a figure without those fields. |
| **S2 Backend API** | **REACHED** | This pass *creates* the surface's shape: the api↔GES contract (§8.1), the absence of any SQL-bearing endpoint (§6.2), fail-closed bundle resolution (§8.4), and the property that a direct API call bypassing the front end is denied identically (`AC-F36-03`). Falsify by finding an endpoint that accepts SQL, returns a secret, or enforces a rule the front end also enforces. |
| **S3 Data / export pipeline** | **REACHED** | §10 fixes the file's shape (dedicated source + category, reference-column stamping), the GES-side precondition order, and adds POAR as a hard gate before emission. Falsify by finding an export path that does not traverse `/ges/export/journal`. |
| **S4 Evidential deliverables** | **REACHED** | §9 fixes the dossier schema, the hash chain, the anchor signing, the 7-year Object-Lock archive, the schema-versioned reader, and the offline-verifiable export bundle. §10.3 adds the CUEC checklist as a published, per-tenant-verified artefact. Falsify by finding a dossier field written outside the single evidence writer, or an export that cannot be verified without the application. |
| **S5 Mobile web** | **NOT REACHED** | No MVP1 build target exists for it and no artefact in this pass renders on it. More usefully: the two decisions that *would* constrain it are both neutral for mobile web specifically — enforcement lives at GES (§8), so a mobile web client inherits every guardrail without re-implementation; and the evidential region is server-rendered self-contained HTML (§9.4), which a mobile **web** client can display verbatim in a browser, so obligation A is satisfiable on this surface with no architectural change. `UX_KB` §3.3 records that no responsive breakpoint below tablet exists in the product design — that is a design gap, not an architectural one. Falsify by showing an api/GES contract element that assumes a desktop viewport. |
| **S6 Native mobile** | **NOT REACHED — but pre-constrained, and this is a finding** | No MVP1 build target. Read/monitor/notify (F23) is unaffected for the same reason as S5: it inherits GES enforcement and retains nothing evidential. **Approval on native mobile (F24) is *not* neutral**: a native client rendering its own approval screen produces a different artefact from the retained rendered view, so `AC-F41-04` and obligation A would fail silently — §18.2. This is a genuine architectural constraint on a not-reached surface, and stating it is the point of enumerating surfaces the project has rather than surfaces this pass touches. |

### 19.3 What must be re-tested, per reached surface

Concrete enough for `test-agent` and the suite owners to act on. Named surfaces
whose evidence the Test gate must show:

| Surface | Suite(s) | What must be shown |
|---|---|---|
| **S1 Desktop web** | `ux` (`ui-ux-designer`), `functional` | `UX_KB` §8.2's UX-1…UX-14 **executed, not static**. Specifically: UX-6/UX-7 (70% vs 100% textual difference; "no exceptions" unrenderable) must be run against the real `Conclusion` renderer, not a fixture — that is the point of §11. Plus gate 5's strengthened `AC-F41-03`: riskiest element at the largest computed font size — ~~asserted **on the retained rendered artefact** as well as live (§9.4)~~ **CORRECTED 2026-08-06: asserted on the *Review screen*, which is the only surface the criterion and `UX_KB` UX-4 scope it to. It is NOT assertable on the retained rendered view, which is an artefact of the approval screen and does not contain the risk band. See §25.4bis.2.** Plus `AC-F38-11` — no figure renders without dataset version, provenance and close-clock staleness. |
| **S2 Backend API** | `architecture` (**mine**, §20), `security` (`security-architect`) | ARCH-01…ARCH-07 and ARCH-15…ARCH-18. Above all: **the direct-API bypass test (`AC-F36-03`) must be executed against the running `api` and `ges`, not asserted from source** — a UI-bypass test that reads code proves nothing about the surface. Plus credential-isolation (`AC-F36-04`), fail-closed (`AC-F36-17`), and the concurrency test ARCH-06, which no other suite will write. |
| **S3 Data / export pipeline** | `architecture`, `industry` (`industry-expert`), `functional` | ARCH-12, ARCH-13. The Journal Import file must be validated against the Oracle FBDI column contract by a schema check, not by eyeballing a sample. Refusal paths must each be exercised with their decision ID: no approval, stale CUEC, blast-radius cap, POAR divergence. `AC-F40-02` — no posting credential resolvable — asserted at runtime in the deployed process, not by grep. |
| **S4 Evidential deliverables** | `architecture`, `industry`, `security` | ARCH-08…ARCH-11. The auditor export must be opened and verified **by a process with no application access and no database credential** — hashes recomputed with standard tools against the shipped anchors. `AC-F1-02` (mutation fails *and* is recorded) must be exercised against the real role grants, because a test against a mocked store tests nothing about the grant. `AC-F1-08`'s oldest-dossier completeness must be exercised through the schema-versioned reader against a v1 payload. |

**Surfaces whose evidence the Test gate must show: S1, S2, S3, S4.** S5 and S6
require no test evidence this pass, for the reasons in §19.2 — and if either
acquires a build target, this Impact Analysis is re-run before it does.

---

## 20 · The architecture test suite (owned by `solution-architect`)

### 20.1 Execution status — **EXECUTED (re-run for real, 2026-08-05)**

**This section was stale in the same way §18.1 was, and is corrected here.** The
standing commitment below — that a suite once reported "could not execute" is
re-run for real and never waved through on the strength of a static pass — was
discharged at gate 10.

**Run at gate 10, by me, `dev` @ `142c734`+:**

```
bash projects/conclave-finance-studio/dev/tests/suites/architecture/run.sh
── suite: architecture ──
interpreter: dev/.venv/bin/python
scenarios:   1 file(s)
............................                          [100%]
EXECUTED — suite passed          exit 0
```

**28 scenarios, 0 failures, exit 0** (exit `0` = EXECUTED/all passed per
`tests/suites/_runner.sh`; `3` and `4` are not passes). The suite started no
long-lived process of its own: `ARCH_04` starts `ges/run.py` as a **child**,
reaps it in a `finally`, and fails loudly rather than skipping if GES does not
bind. Nothing in `dev/` was modified and nothing was installed.

**What the 28 cover, stated honestly against §20.2's twenty specified scenarios.**
Executed: ARCH-02 (4), ARCH-04 (2, including the two-process topology witness and
the 401 on the socket), ARCH-05 (3), ARCH-08 (4), ARCH-09, ARCH-10 (2), ARCH-11
(2), ARCH-15 (3), ARCH-18 (2), plus the api-never-imports-ges static check and two
guards that the suite's own GES app cannot write to the live decision ledger.
**Not present as architecture-suite scenarios: ARCH-01, ARCH-03, ARCH-06, ARCH-07,
ARCH-12, ARCH-13, ARCH-14, ARCH-16, ARCH-17, ARCH-19, ARCH-20.** Several are
covered by other suites (`functional`, `security`, `industry`) and I do not claim
their results as mine; **ARCH-06 (blast-radius concurrency under retry-on-
serialization-failure) is the one §19.3 said no other suite would write, and it is
still not written** — register entry 2 records that the `SERIALIZABLE` transaction
it would exercise has no SQLite equivalent and is not built, so the scenario has
nothing to assert against today. That is a disclosed gap, not a pass.

**Prior status, retained as history — no longer true:**

~~**The entry point `projects/conclave-finance-studio/dev/tests/suites/architecture/run.sh`
does not exist.**~~ There is no `dev/` directory in this project as of 2026-07-31;
`code-agent` has not run. Every scenario below is therefore
**`STATIC ONLY — NOT EXECUTED`**, and none may be reported as passing.

What would have to exist for them to run: `dev/` scaffolded from
`templates/genai-chatbot/` (which ships
`tests/suites/architecture/run.sh` and `_runner.sh`), a project venv with
`pytest`, and — for ARCH-01…ARCH-07 and ARCH-12…ARCH-14 — the `api` and `ges`
processes already started by `deploy-agent` or the orchestrator, since a process
started inside my turn dies with it.

**Standing commitment, per my contract:** once the entry point exists, this
suite is **re-run for real**. No scenario below is waved through on the strength
of this static pass.

### 20.2 Scenarios

Contract tests between components, and design-conformance checks on what was
actually designed here.

| # | Scenario | Kind | Asserts |
|---|---|---|---|
| ARCH-01 | api↔GES contract: every GES operation's request/response schema matches the api client's expectations; an unknown field is rejected rather than ignored | Contract | §8.1 |
| ARCH-02 | **No SQL-bearing endpoint exists.** Enumerate every GES route schema; assert no parameter of type string is documented or handled as SQL; POST a SQL string to every route and assert refusal + control event | Contract / conformance | `AC-F39-02`, `PLAN` §11 c.19 |
| ARCH-03 | **Direct API bypass**: an action the front end would not offer, requested straight against `api`, is denied by GES with a decision record identical in kind | Conformance | `AC-F36-03` |
| ARCH-04 | **Credential isolation**: from the `api` process, no warehouse/ERP/signing credential is resolvable from environment, config or any imported module; the attempt is recorded | Conformance | `AC-F36-04`, obligation M |
| ARCH-05 | **Fail closed**: corrupt the bundle hash; assert every action is denied naming the unresolvable bundle, and that no cached bundle is used | Conformance | `AC-F36-17` |
| ARCH-06 | **Blast-radius concurrency**: two concurrent runs at the cap boundary; assert exactly one proposal is admitted and the counter is correct. Repeat under retry-on-serialization-failure | Scalability / correctness | §8.5, `AC-F36-09`–`-12` |
| ARCH-07 | **Caps non-disableable**: compile a bundle with a null/unbounded/absent cap → build fails; attempt a runtime write to a cap through every route → no such route exists | Conformance | `AC-F36-13` |
| ARCH-08 | **Conclusion type**: assert `FullPopulationConclusion` is unconstructible with a non-empty uncovered set; assert the three conclusion strings appear in exactly one module | Conformance | §11, `AC-F38-04`–`-08` |
| ARCH-09 | **One object, three renderers**: same `Conclusion` rendered to screen payload, dossier and export; assert all three carry the same coverage figure and the same named gaps | Contract | `AC-F38-07` |
| ARCH-10 | **Evidence store grants**: with the runtime evidence role, `UPDATE`/`DELETE`/`TRUNCATE` fail at the database, and each failure appends a `mutation_attempt` event | Conformance | `AC-F1-02`, obligation G |
| ARCH-11 | **Hash chain**: alter one stored dossier's bytes; assert verification identifies that record; assert re-chaining forward fails signature verification against the anchor | Conformance | `AC-F1-03` |
| ARCH-12 | **Export preconditions**: exercise all five refusal paths in order; assert each produces a decision ID and no file | Contract | `AC-F40-03`, `-05`, `-07`, §5.4 |
| ARCH-13 | **Journal Import contract**: emitted file validates against the FBDI column contract; source/category are the dedicated values and nothing else; reference columns carry proposal/dossier/decision/run/principal ids | Contract | `AC-F40-01`, `-04`, J-9 |
| ARCH-14 | **Forward disposition is a constraint**: attempt a disposition insert without `expected_clearing_period` at every permission level; assert database-level failure, not a validation message | Conformance | `AC-F32-01` |
| ARCH-15 | **Population seam**: a detector manifest naming a physical table fails compilation; a detector executes end-to-end against a `Population` whose `source_class` is switched to a non-ERP value with no detector code change | Conformance / phase-2 seam | `PLAN` §8 P1, §7.2 |
| ARCH-16 | **Rendered-view determinism**: same `review_payload` + template version ⇒ byte-identical HTML; the artefact contains no external asset reference and no script tag | Conformance | `AC-F41-04`, §9.4 |
| ARCH-17 | **Probe invisibility**: probe status absent from the pre-disposition response payload, DOM and class names; asserted on the serialised payload, independent of reveal policy | Conformance | `AC-F41-08`, §9.6 |
| ARCH-18 | **Zero model calls in the deterministic path**: instrumented run of every `integrity` and detector evaluator; assert model invocation count is 0 | Conformance | `PLAN` §11.A c.4, §7.5 |
| ARCH-19 | **Registry completeness at run open**: a run naming an unregistered artefact version does not start and names it | Contract | `AC-F2-04` |
| ARCH-20 | **Lineage completeness**: every evidence write appears in `artefact_touch`; a lineage query enumerates all of them and states completeness; an artificially untraversable edge produces `incomplete` with the edge named | Conformance | `AC-F5-03`, `-05` |

Evidence goes to `projects/conclave-finance-studio/test-evidence/` in
`test-agent`'s documented per-scenario format (Input / Expected / Actual /
Result / Evidence).

---

## 21 · Phase-2 seams — what MVP1 leaves open, concretely

`PLAN` §8 names eight. Each below states the mechanism, so a phase-2 reviewer
can check whether it survived rather than trusting that it did.

| `PLAN` §8 | Seam | Mechanism in this architecture |
|---|---|---|
| **P1** cross-source omission | `Population.source_class` is a closed enum with room for non-ERP values; `expectation_gap` keys on member presence, never on a table. Adding a source adds a `CertifiedDataset` and a `Population`, not a detector | §7.2, §7.3 |
| **P2** non-ERP expectation inputs | `CertifiedDataset` carries lineage and tie-out status with no field asserting Oracle provenance; the certifier is connector-agnostic | §5.1 |
| **P3** cross-system positioning | Coverage's `named_gaps` is the mechanism that prevents a single-source run from reading as complete; it is already load-bearing in MVP1 | §11 |
| **P4** multi-ERP estates | The ERP is reached through an adapter interface with one MVP1 implementation. A second ERP is a second adapter + a second CUEC checklist, not a detector change | §5.4, §10.3 |
| **P5** fidelity as differentiator | F26 ships as an ordinary detector manifest; nothing in the architecture ties its positioning to its implementation | §7.4 |
| **P6** A10 residual *composition* | The boundary object F28 produces already carries member-level detail; the composition detector is a new manifest over the same object once F12 has labels | §7.2 |
| **P7** treasury sources | Would enter as a `CertifiedDataset` with a new `source_class`. **Still not a matching engine** — no evaluator primitive performs matching and none should be added | §7.3 |
| **P8** intercompany cause | `pair_imbalance` emits the imbalance; cause needs labels. No architectural work is owed | §7.3 |

Two more the architecture creates and `PLAN` §8 does not name:

- **Tier 2 direct posting (F17)** is a credential added to an existing boundary
  plus a submit method on the existing egress component. No new trust boundary,
  no new enforcement point — which is the whole reason §3.2's boundary is built
  in MVP1 where no posting credential exists.
- **Multi-tenancy.** `tenant_id` is present on every table and every hash chain
  from day one. Cheap now; a migration later.

---

## 22 · Joint ownership, and where `security-architect` and I must present together

I own this gate jointly with `security-architect` and have not seen their pass.
Four items in this design are **theirs to adjudicate or to strengthen**, and we
must present them together rather than my resolving them here:

1. **The GES process boundary (J-1)** — I have specified separate process,
   separate OS user, separate secret mount, loopback mTLS. Whether that is
   sufficient, or whether it should be a separate host/network zone, is
   `security-architect`'s call. I would accept any strengthening; I would object
   to any weakening to a module boundary, and if that disagreement arises it goes
   to the human rather than being settled between us.
2. **Whether the warehouse holds personal data** (payroll, commission, expense) —
   `PLAN` §10 assigns this to `security-architect`. It affects §6's certified
   query registry (which columns may be exposed to a model at all) and §15.4's
   provider selection. **If the answer is yes, the certified query registry needs
   a per-column exposure classification and the resolver's catalogue must be
   filtered by it.** That is a real design change and I want it flagged now
   rather than discovered at Code.
3. **KMS key custody and the anchor signing model** (§9.2) — I have specified
   sign-only, application cannot read the private key. Key rotation across a
   seven-year retention horizon is a security design problem I have not solved
   here: an anchor signed in 2026 must remain verifiable in 2033 across at least
   one rotation. `security-architect` owns the rotation and key-archival design.
4. **Authentication strength on the approval action.** `INDUSTRY_KB` §4.3 item 6
   requires approver identity *and authentication strength* in the dossier. My
   schema has the field; what value must go in it — and whether approval requires
   step-up authentication — is `security-architect`'s.

`responsible-ai-architect` is advisory here and owns probe reveal timing (§9.6),
which I have deliberately not pre-empted.

---

## 23 · Binding instructions for `code-agent`

Consolidated so they are not scattered. These are the statements that, if
violated, make a stated property false rather than merely making the code
different.

1. **GES is a separate process.** The `api` process's environment contains no
   warehouse, ERP or signing credential. Not "should not" — must not, and
   ARCH-04 checks it in the running process.
2. **No function anywhere accepts SQL text as a parameter.** Not private, not
   internal, not "for tests".
3. **`evidence/store.py` exposes no update or delete function, and the runtime
   evidence role holds no such grant.** The grant is the enforcement; the missing
   function is the reminder.
4. **The decision and its blast-radius state mutation commit in one
   `SERIALIZABLE` transaction.** Retry on serialization failure; never split them.
5. **`Conclusion` is a closed sum type with a private full-population
   constructor.** The three conclusion strings live in one module. No screen,
   dossier writer or exporter composes conclusion text.
6. **The evidential region is a pure function of `(review_payload,
   template_version)`** — no data fetch, no hover-only content, no lazy load, no
   live refresh inside it.
7. **`expected_clearing_period` is `NOT NULL` and the disposition write path has
   no overload without it.**
8. **Every detector takes a `Population` object. No detector, manifest or
   evaluator receives a table name.**
9. **`integrity/` and every detector evaluator run with the model-call guard
   set.** A model call from inside raises.
10. **Every evidence write goes through the one evidence writer**, which appends
    to `artefact_touch`. A second write path breaks the lineage completeness
    claim and there is no test that will notice until an auditor does.
11. **Dossier payloads are schema-versioned and read through a versioned
    reader.** No migration may drop or rename a dossier field, ever.
12. **The guardrail bundle has no runtime write path.** Caps and rules change by
    rebuilding the bundle.

---

## 25 · Gate 10 rulings (Architecture pass 2, 2026-08-05)

Placed before §24 so the change history stays last. Four items were held for an
architect's ruling rather than a builder's decision. Each is ruled here, and each
names the agent who owns any work that follows — **I do none of it myself.**

### 25.0 Completeness check — binding decisions checked against, for this pass

Per my contract I re-read `PROJECT_CONTEXT.md`'s Decisions Log **in full**, not
only the gate-10 brief. §1 records the pass-1 check and every entry in it still
holds. **Binding decisions recorded since my last pass**, and how this pass
satisfies each:

| Binding decision since pass 1 | How this pass satisfies it |
|---|---|
| **2026-08-05 — `[override]` at gate 9, all nine AC IDs named, human chose to ship the pilot now** | Not re-litigated: shipping is the human's call and it is made. None of my four rulings reverses it and none holds the pilot. Rulings 3 and 4 are written as **preconditions on the first tenant / first real auditor export**, not as pilot blockers, which is the only shape consistent with a decision to ship now. Ruling 3 does, however, find that the override's claim-prohibition list is **incomplete** — §25.3.3. |
| **2026-08-05 — the override does NOT close the four closeable F5 criteria; they ship unbuilt with `/inventory` disclosing it** | Untouched. ARCH-19/ARCH-20 remain unwritten in my suite and §20.1 now says so explicitly rather than letting a green 28 imply coverage. I do not fold them into any pass count. |
| **2026-08-05 — "Claims the pilot must not make", unchanged by the override** | Honoured, and extended: §25.3.3 proposes a sixth prohibition. I do not add it myself — the list is the human's, held in the Decisions Log. |
| **2026-08-05 — orchestrator correction: `UX_KB` Part A2 only *partially* built; the Close cockpit and Period record do not exist; J3/J4 unwalkable** | Checked for collision with ruling 4, which touches the export's rendered view. No collision: the retained region composes from `pages.approval_evidential_region`, which exists and is walkable. Ruling 4 adds no screen. |
| **2026-08-05 — orchestrator correction on what "approval pending" may say on a KB face** | This file's header still reads *proposed under standing authorization, awaiting joint presentation with `security-architect`*. Accurate and unchanged: gate 6 was closed jointly, and §25 is a pass-2 amendment presented for the same joint sign-off. I have not upgraded the header's status on my own authority. |
| **2026-07-31 — Test Policy: all suites blocking, no advisory exceptions** | §20.1 reports a real execution with a real exit code and names eleven §20.2 scenarios that are **not** in the suite, rather than reporting 28 green as coverage of twenty. |
| **2026-07-31 — MVP1 desktop web only; three surfaces → `solution-architect` non-droppable, Impact Analysis mandatory** | §25.5, enumerating all six surfaces from §19.1 — reached and not-reached, each with falsifiable reasoning. |

**Conflicts with a binding decision: none.** One **gap** found against a binding
decision, raised not resolved: §25.3.3.

---

### 25.1 Ruling — §18.1 is amended, and the lesson is bigger than the entry

**Ruled: amend, and mark the false sentence rather than deleting it.** Done in
§18.1. `review-agent`'s distinction is the right one and I am adopting it as a
standing habit for this file: **a KB assertion of an absence has a shelf life,
and it is my job to expire it, not the job of whoever fills the gap.**
`functional-design-agent` issued `AC-F41-14`/`-15`, `code-agent` built it, and
neither had any reason to come and edit my file. The finding was the mechanism
working; leaving it standing afterwards was the mechanism failing.

Two things I checked rather than accepted, because a stale finding replaced by an
unverified closure is no improvement: the enforcement point is the **bundle rule**
`scope.no_bound_dataset_superseded_by_later_data` (`mode: enforce`,
`override_eligible: false`, context resolved server-side and caller values
discarded), not the UI element; and `AC-F41-15`'s negative case is the rule's
declared `non_firing` fixture, so §8.2's compile-time fixture evaluation verifies
the negative half on **every build**. That is stronger than what §18.1 asked for,
and it is worth naming why: the criterion that stops the control over-blocking is
verified by the same mechanism that verifies the control fires, so a build cannot
keep one and lose the other.

**Work implied: none.** No agent owes anything.

**Consequential sweep I owe and am doing here:** §20.1 asserted the same shape of
absence ("the entry point does not exist… STATIC ONLY — NOT EXECUTED") and was
equally stale. It is corrected in the same pass. I checked §18.2, §18.3 and §18.4
for the same defect: §18.2 (F24 vs. the rendered view) is still true and still
open; §18.3 (routing budget) is **now closed by `AC-F41-16`/`-17`, which exist in
`FUNCTIONAL_SPEC` §27.1** — I am marking it below rather than leaving a second
stale absence behind while fixing the first; §18.4's two items are genuinely open.

**§18.3 is superseded.** `AC-F41-16` bounds the routed volume and names the
reviewer and the held count; `AC-F41-17` makes raising the cap a controller-only
control event with a decision ID. The sentence "it is currently unenforced at the
Test gate" is no longer true. The pilot additionally sets `PILOT_ROUTING_CAP = 3`
against a product default of 12 specifically so the at-cap state is reachable by a
reader of the running pilot — a pilot configuration, correctly placed in
`pilot_transport.py` with the pilot's other compromises rather than changed in
`ges.routing.DEFAULT_CAP`. I endorse that placement.

---

### 25.2 Ruling — both primitives join §7.3; neither is folded

**Ruled: `obligation_gap` becomes primitive 12 and `journal_attribute_outlier`
becomes primitive 13.** §7.3 is amended. Neither is folded into an existing
primitive, and `obligation_gap` is **not** split into three.

First, the mechanism worked and should be said so plainly: `code-agent` built two
primitives my list did not contain, and instead of widening my list or hiding them,
declared them in a named `UNSPECIFIED_BUT_BUILT` tuple under a **set-equality**
check that refuses a registered-but-undeclared primitive. That is the correct
behaviour for a builder meeting the edge of a design, and the reason this ruling
is a five-minute decision instead of an archaeology exercise.

**Why `obligation_gap` is a primitive and not a parameterisation of `expectation_gap`.**
The two have different *input contracts*, not different parameters.
`expectation_gap` derives an expectation from **history** — present in N of the
last M periods, absent now. `obligation_gap` derives it from a **declaration** —
a journal said a reversal was owed. Three consequences make the distinction
structural rather than stylistic, and each is falsifiable:

1. A first-ever reversal, flagged in its first period, has **no history at all**
   and is still owed. `expectation_gap` cannot see it at any `required_hit_ratio`.
2. A quarterly settlement feed posts in four periods of twelve. Loosening
   `required_hit_ratio` until `expectation_gap` catches its omission reports it
   as missing in the eight periods where nothing was owed — a detector that is
   wrong in eight periods to be right in one.
3. An intercompany counterparty posting is owed **the moment the first side
   posts**. There is no prior period to look at.

`code-agent` reports reaching this by trying `expectation_gap` first, on the
fixture. That is the right order and it is the evidence I am ruling on.

**Why it stays one primitive covering three kinds, rather than three.** The three
share the whole computation — *for each declared obligation: not yet due → note;
discharged within tolerance → nothing; else → omission* — and differ only in the
vocabulary a finding carries and in where the declaration came from. Splitting
them would be three copies of one computation, which is precisely the failure
§7.1 exists to prevent: §7.1's honest bound is *a new detector is configuration,
a new primitive is code*, and three primitives that differ by a vocabulary table
would make that bound a fiction in the other direction. `intercompany_counterparty`
adds *which side posted and which did not* — an **output field on a two-sided
obligation**, not a second computation. The `KIND_VOCABULARY` mapping is closed
and an unknown kind fails the run rather than emitting a generic summary; that
closure is what makes one primitive safe here, and it must stay closed.

**Why `journal_attribute_outlier` is not a parameterisation of `distribution_outlier`.**
`AC-F42-02` requires the journal **and the attributes that made it an outlier** to
be named. `distribution_outlier` computes a distance from an account's historical
range and returns a scalar verdict; no parameterisation of a distance computation
yields an attribution. The output *shape* differs, not the threshold — and output
shape is exactly where a primitive boundary belongs, because it is what a detector
manifest cannot change.

**The calibration caveat travels with it into §7.3, and generalises.** Promoting
this primitive **does not calibrate it**: `min_attributes: 3` and
`rarity_ceiling: 0.05` are declared, and no likelihood, precision or false-positive
rate is claimed for it. Register entry 30 stays open. What I have added is the
standing rule in §7.3 — the calibration denial must sit on the module header **and
on every emitted finding**. `journal_attribute_outlier` already satisfies it and
is the reference implementation. The rule is in the KB rather than in one module
because the failure it prevents is the *fourteenth* primitive arriving uncalibrated
and quiet, and because a reader who meets only a finding must still meet the denial.

**Work implied — owner `code-agent`, one commit, not urgent and not a pilot blocker:**

1. `SPECIFIED` becomes **thirteen** names, in the order §7.3 now lists them.
2. `UNSPECIFIED_BUT_BUILT` becomes **empty** — and, exactly as was done when
   `SPECIFIED_BUT_NOT_IMPLEMENTED` was emptied, the tuple and its set-equality
   check **stay**, with a test asserting both that it is empty *and* that a
   planted registered-but-undeclared primitive is still refused. Emptying a
   declaration must not quietly remove the check that made the declaration
   meaningful. This is the single most important half of this work item.
3. The header comment naming me as the gate-10 reviewer is replaced by a pointer
   to this section, so the file does not keep asking for a ruling that exists.

**Work implied — owner `test-agent`:** no new scenario. The existing set-equality
check covers it once `SPECIFIED` is updated; a green suite after step 2 is the
evidence.

---

### 25.3 Ruling — the pilot transport: sufficient for the pilot, gated for the tenant

Register entry 19. I am stating this as a gate, not a preference, as asked.

#### 25.3.1 For the pilot: SUFFICIENT — and it is conditional, not free

**Ruled sufficient**, on five conditions that all currently hold and none of which
may be relaxed without returning here:

1. It **refuses to install under `CONCLAVE_ENV=production`**.
2. It is **one named file, outside the `app` package**, with the loss stated in
   its own first paragraph — `grep -l "^from ges" backend/app` still returns only
   `run.py`.
3. The **api-never-imports-ges** static check still executes and still passes
   (verified in my §20.1 run).
4. **`ARCH_04` is a real topology witness**, and this is what moved the entry from
   "disclosed" to "narrowed": it starts `ges/run.py` as a child on an ephemeral
   port, asserts a *different pid* holds the credential while the test process
   (role `api`) is refused it, drives a real broker decision over stdlib HTTP on a
   TCP socket — no `TestClient` — and a companion asserts 401 for an untokened
   caller. Both executed in my §20.1 run. Gate 8's finding that the prior checks
   *would have passed with the boundary gone entirely* is what makes this witness
   load-bearing rather than decorative.
5. Every screen rendering a broker fact obtained through it **says so, in words**,
   in the pilot strip.

The reasoning: a pilot's job is to be operated and read, on one host, over
synthetic fixture data, by people who know what they are looking at. Against that
job, a module boundary whose collapse is declared in five places and whose
deployed alternative has an executing witness is a proportionate trade. It would
not be proportionate for one hour of real tenant data.

#### 25.3.2 Before the first tenant deployment: THREE CONJUNCTIVE GATES

The residual is stated exactly right in the register — *no suite can witness that
an api-process module cannot `import ges.executor`, because a suite runs in one
interpreter with both packages on one `sys.path`*. **The answer is not a better
test. It is that a deployment is not one interpreter.** These three gates convert
an unwitnessable property into a checkable one. All three must hold; any one
failing means the boundary is a convention again.

> **GATE T1 — the `ges` package is not on the api host's disk.** The api role's
> deployment artefact is built without it, and a **deploy-time** check in the api
> image asserts `import ges` raises `ModuleNotFoundError`. This is the operative
> gate: it makes the property true by construction rather than by agreement, and
> it is checkable in the artefact by anyone, including an auditor. A prompt-
> injected tool cannot import a package that is not there.
>
> **GATE T2 — `backend/pilot_transport.py` is absent from the api image**, not
> merely refused at runtime. `CONCLAVE_ENV` is read *inside the process the
> boundary is supposed to protect*; a runtime refusal is a check the attacker's
> process performs on itself. Absence is not.
>
> **GATE T3 — at least one full approval is exercised end-to-end over
> `LoopbackHttp`** by a suite, so the transport that ships is the transport that
> is tested. Today `ARCH_04` witnesses the topology and drives a broker decision
> over the socket, while the `ux` suite drives approvals **in-process**; no
> scenario drives a complete approval over the socket. That is the last place the
> two configurations can diverge unobserved.

**Owners.** T1 and T2: `deploy-agent`, with `code-agent` for the packaging split.
T3: `test-agent` with `code-agent`. **None of this is mine to build**, and none of
it is buildable in a single-host pilot — which is why entry 19 cannot close now
and should not be made to look closeable.

**Relationship to register entry 1** (mTLS on loopback, replaced by a shared token
+ 127.0.0.1 bind, "must be reversed before any non-single-host deployment"). T1–T3
are its peers, not its subset: entry 1 secures the *channel* between two processes,
T1–T3 establish that there *are* two processes. Both are preconditions on the same
event and should be presented to the human together, once, as the deployment gate —
not discovered one at a time during a tenant onboarding.

**Register entry 19: NARROWED again, NOT CLOSED.** It closes when T1 and T2 are
verifiable in a real deploy artefact and T3 is executing.

#### 25.3.3 A gap in the override's claim-prohibition list — raised, not resolved

The 2026-08-05 override records five claims the pilot must not make. Checking my
ruling against them, **none of the five covers the fact that the running pilot's
analysis/execution split is a module boundary.** That is a claim the product's
own architecture makes loudly — §3.2 calls this one boundary the thing the entire
product claim reduces to — and a pilot audience that has read the architecture
will reasonably assume it is in force unless told otherwise.

The pilot strip discloses it per-screen, which is real and is why this is a gap
rather than a defect. But the claim-prohibition list is the artefact that travels
to people who never see a screen. **Proposed sixth prohibition, for the human via
the orchestrator — I am not writing it into the Decisions Log myself:**

> *No claim that the analysis/execution trust boundary is enforced as a process
> boundary. In the pilot's single-command configuration it is a module boundary:
> a prompt-injected tool in the api process could reach `ges.executor` by import
> alone. The two-process topology is built and has an executing test witness; it
> is not what the pilot runs.*

`security-architect` should co-sign this or say why not — it is on the boundary we
jointly own (§22), and it is exactly the kind of item my contract says to surface
rather than resolve quietly.

---

### 25.4 Ruling — inline the stylesheet in the export's rendered view

**Ruled: inline it, and §9.4's claim stands.** Not a deliberate divergence.
§9.4 is amended with the two-artefact table and this ruling.

`code-agent` was right to decline and right about why: *"genuinely a change to
what an export contains"* is a scope judgement, not a build judgement, and
bringing it here is the behaviour I want. But the 280 KB is not what decides it.
280 KB on an auditor deliverable that is already a complete evidential record is
not a cost worth a defect.

**What decides it** is that the size emphasis lives **only** in the stylesheet —
`.riskband .big{font-size:__RISK__px}`. The markup carries a class name and no
size. So in the export's copy, gate 5's strengthened `AC-F41-03` (riskiest element
at the largest computed font size) is not "harder to check": there is **nothing to
check against**. And `AC-F1-04`'s reader is defined as *a party with no application
login* — the one person who cannot open `/dossier/<id>`. Satisfying a binding gate-5
decision only on the surface that reader cannot reach satisfies it for everyone
except them.

Two supporting reasons, neither sufficient alone:

- Two artefacts both called "the retained view", differing in whether they render
  as shown, is the same class of drift `retained.py` was rewritten to eliminate.
  Its `unclassified()` check catches a *card* that diverges and would not catch
  this, because this divergence is not in the tree.
- `AC-F41-04`'s own text — *what the approver saw* — is not obviously satisfied by
  a document in which the riskiest element is typographically indistinguishable
  from the rest. `AC-F41-04` does not *require* inlining, as `code-agent` correctly
  noted; §9.4 does, and §9.4 is the reason gate 5 accepted the strengthening.

**Four constraints, so this stays buildable and does not create a worse defect.**
Owner `code-agent`; constraint 3 is the one that would bite.

1. **The block is inlined per dossier, not hoisted to one export-level copy.**
   Duplication is the point: each `rendered_view` must be independently openable
   when extracted, which is what §9.4 means by self-contained and what the
   auditor's actual workflow does. A shared block makes every view non-self-
   contained to save 260 KB.
2. **Byte-identical across dossiers in one export**, with the stylesheet's SHA-256
   recorded once in the export's integrity section, so a reader can verify every
   copy is the same block without diffing 14 of them.
3. **The retained hash must be of the bytes that ship.** `AC-F41-04` retains the
   HTML bytes *and their SHA-256*. If the hash is computed pre-inlining and the
   export carries post-inlining bytes, the export contains an artefact whose hash
   does not match its own recorded hash — strictly worse than either current
   state. Verify this before anything else.
4. **`check_no_active_content` runs on the shipped bytes, after inlining.**
   `ACTIVE_CONTENT_PATTERNS` forbids `<link`, `url(`, `@import`, `<img` and
   `srcset` and does **not** forbid `<style>` — so an inlined block passes only
   because `chrome.stylesheet()` genuinely contains no `url(` and no absolute URL.
   That is a property of today's stylesheet, not a guarantee, and the check must
   be what enforces it rather than this paragraph. `retained.render()`'s separate
   anchor refusal is unaffected: a `<style>` element is not an `<a>`.

**Timing.** Not a hold on the shipped pilot — its exports carry synthetic-fixture
data under the pilot strip, and no real auditor is relying on them. **Precondition
on the first export handed to a real auditor**, which is the same event as the
first tenant deployment.

**Work implied — `code-agent`:** constraints 1–4. **`test-agent`:** ARCH-16
(rendered-view determinism) extends to assert the export copy contains the
`<style>` block, that the block is byte-identical across dossiers, and that its
digest matches the one recorded in the integrity section. Until that scenario
exists, ARCH-16 remains unwritten and §20.1 continues to say so.

---

### 25.4bis RE-RULING 2026-08-06 (gate 11) — §25.4's premise was false. The outcome stands; the reason is replaced

`test-agent` verified §25.4's deciding argument in Chromium and falsified it.
Routed back rather than built on. **This section replaces §25.4's reasoning.
Where the two conflict, this one governs.**

#### 25.4bis.1 What was actually wrong — and it was mine, from pass 1

I ruled that inlining the stylesheet would make `AC-F41-03` checkable in the
export's artefact, because the size lived only in CSS. Measured:

| | live `/dossier/<id>` | the export's artefact, opened **as a file** |
|---|---|---|
| `riskiest-figure` | present, **40px**, sole element at the page maximum | **absent entirely** |
| distinct computed sizes | six | **two** (24/16px — browser defaults) |

So the artefact carries neither the size nor the element. **Inlining could not
have closed the gap it was ruled to close.**

**The error is older and deeper than styling, and it is mine, not
`code-agent`'s and not pass 21's.** Reading the criteria rather than my own
summary of them:

- **`AC-F41-03`** — *"**When the Review screen is rendered**, that element is
  rendered outside any collapsed or expandable region and appears ahead of the
  proposal's supporting narrative in the reading order."* `UX_KB` UX-4 scopes
  gate 5's strengthening the same way: *"first in DOM order **on Review** …
  at the largest computed font size **on the screen**."*
- **`AC-F41-04`** — *"the stored rendered view **for that approval**"*.

**These are two different screens.** The retained region is
`pages.approval_evidential_region`, composed for `/approvals/<proposal_id>`;
the risk band renders in `pages.review`, `pages.dossier` and the finding screen,
and **never on the approval screen at all.** §9.4 consequence 3 asserted a
Review-screen property was checkable in an approval-screen artefact, and that
was untrue on 2026-07-31, before styling entered the question. At gate 10 I then
reasoned from `.riskband .big` — a CSS rule that only ever applies to a
component this document does not contain. The gate-10 argument was internally
consistent and about the wrong document.

This is the §18.1 failure mode with me as the author rather than the reader: a
KB sentence asserting a property, believed downstream because it was in the KB,
which nobody could falsify without opening a browser. It cost `code-agent` a
declined work item and `test-agent` a verification pass. **The standard I
applied to §18.1 applies here: the sentence is struck where it stands (§9.4),
not quietly rewritten.**

#### 25.4bis.2 Ruling on `AC-F41-03` — option 3. It is a screen criterion, by its own text

**Ruled: `AC-F41-03` is a Review-screen criterion by design, and the retained
rendered view carries the evidence without the emphasis.** Recorded, not
worked around.

**Option 2 — importing the risk band into the retained region — is refused, on
three grounds, and pass 21's judgement is upheld rather than reopened.**

1. **It would put a fact in the artefact that the approver was not shown.** The
   approver on `/approvals/<proposal_id>` never sees the risk band. An artefact
   whose job is to reproduce *what was displayed at approval time* does not
   improve by gaining something that was not. `pages.py` already names this
   exact failure in the opposite direction — retaining the threshold without
   showing it would have been *"an artefact carrying a fact the approver was
   not shown, which is the same defect from the opposite direction."* Option 2
   commits that defect deliberately. **This is the decisive ground.**
2. **It is a typography decision driven by a criterion about evidence.** Pass
   21's recorded reason — the band carries the single largest type in the
   product and that size is a *per-screen uniqueness invariant* — is better
   architecture than the sentence of mine it contradicted. Importing it would
   put the product's largest type onto the screen that carries the **approve
   control**, changing what dominates the moment of decision. That is
   `ui-ux-designer`'s call and `UX_KB`'s invariant, and it must not be made as
   a side effect of an architecture ruling about file formats.
3. **Nothing evidential is missing.** The retained region already carries the
   amount, the finding, the four-period evidence table with the recurring
   wording, the threshold, the bundle version, the dataset version and as-of,
   the coverage figure and the exact journal lines. The risk band is a
   *ranking and emphasis of facts the artefact already contains in full*.
   Emphasis is the right thing for a screen to add and for an evidence record
   to omit.

**And the emphasis is not lost from the product.** `pages.dossier` — the
`/dossier/<id>` exhibit — renders `C.risk_band` **with the stylesheet inlined**,
measured at 40px and sole element at the page maximum. The composition that
carries the riskiest element at maximum size exists and is style-inlined; it is
simply not the same composition as the retained rendered view. Anyone reading
option 3 as "the emphasis went away" should read this paragraph.

**Owner of any spec consequence: `functional-design-agent`.** If `AC-F41-03`'s
screen scoping should be stated in `FUNCTIONAL_SPEC` rather than inferred from
its Given/When, that is their lane and their ID. I am not issuing it — the same
line I drew at §18.1, and the mechanism worked there.

#### 25.4bis.3 Ruling on inlining — option 1, on a reason that survives contact with the artefact

**Ruled: still inline it. The four constraints in §25.4 stand unchanged. The
reason is replaced.**

I opened the artefact rather than reasoning about it
(`test-evidence/ui-export-artefact-unstyled-1280-2026-08-06.png`). Unstyled,
every label is glued to its value:

```
Amount312,480.00
Authoragent.crossperiod-surveillance
Applicable threshold$150,000.00, inclusive
Guardrail bundlelev14 - 9f3a71c2
Coverage of this run70% - partial
Dataset versiongl_balances vFIXTURE-2026.06.03-a
```

The separation was carried by `.lbl`'s block display. Without the stylesheet it
is gone, on **133 elements at two computed sizes**.

**Why this justifies the work even though it looked uncovered by any criterion.**
`AC-F41-04` requires the retained view to *"reproduce what was displayed at
approval time, **including the figures, the threshold and the bundle version**."*
`Applicable threshold$150,000.00, inclusive` and `Guardrail bundlelev14 - 9f3a71c2`
are not reproductions of what was displayed — the label/value boundary was
displayed and is not reproduced, and those are two of the three things the
criterion names explicitly. So this sits **closer to criterion-covered than
"stylistic"**, and the honest statement is: it is my reading of `AC-F41-04`, and
whether the criterion reaches legibility is `functional-design-agent`'s to
confirm. The ruling does not depend on winning that argument.

What the ruling does depend on, and what I am willing to defend alone:

- **It is a correctness hazard, not an aesthetic one.** `Coverage of this
  run70% - partial` is one misparse from a wrong coverage figure, in a
  seven-year record, read by `AC-F1-04`'s party who has **no application login
  and no one to ask**. Wherever a label ends in text and a value begins with a
  digit, glued rendering is genuinely ambiguous. That is the wrong class of
  risk to leave in an S4 deliverable to save a stylesheet.
- **The cost is smaller than the number I ruled on, and that number was wrong
  twice.** The corrected count is **624**, not 1,248 — `approver_view` and
  `rendered_view` are the same bytes, and deliberately so:
  `test_the_rendered_view_and_the_approver_view_are_the_same_artefact` asserts
  they cannot diverge, because `approver_view` is `AC-F1-05`'s reconstruction
  field and `rendered_view` is `AC-F41-04`'s retained view. That duplication is
  designed and should stay. **`code-agent` re-measures the added bytes against
  the real stylesheet and the real dossier count before building** — I have now
  been handed a wrong figure twice and will not carry a third into the KB.

**§25.4's four constraints are unaffected** by this re-ruling, because none of
them rested on the falsified premise: per-dossier inlining rather than hoisting
(each view independently openable); byte-identical across dossiers with the
digest recorded once; **the retained SHA-256 must be of the shipped bytes**; and
`check_no_active_content` run post-inlining. Constraint 3 remains the one that
would create a worse defect if got wrong.

#### 25.4bis.4 What this does *not* fix, stated so it is not read as fixed

Inlining makes the artefact **legible**. It does not make `AC-F41-03` checkable
in it, and after §25.4bis.2 nothing is expected to. Any future test asserting
`AC-F41-03` against the export's artefact is asserting the wrong thing about the
wrong document and should fail review.

Separately: `test-agent`'s gate-11 smoke found the **pilot-provenance disclosure
missing from both artefacts**, which `code-agent` is already fixing. I did not
rule on it and it is not mine, but it is the more serious of the two findings
and I want the ordering recorded — an artefact that does not say it was built
from synthetic fixture data is a worse defect than one whose labels are glued.
The human declined claim prohibition 6 on 2026-08-06 **on the basis that the
substance is disclosed on the surfaces a reader meets**, which makes that fix
load-bearing for a decision that has already been taken.

---

### 25.5 IMPACT ANALYSIS — Architecture pass 2 (gate 10 rulings)

Mandatory per my contract, enumerating **every surface the project has** from
§19.1's register — not only the surfaces these rulings happen to touch. Six rows,
each reached or not, each with reasoning a reader can falsify. A surface omitted
without justification blocks this gate; none is omitted.

| # | Surface | Reached by pass 2? | Reasoning — falsifiable |
|---|---|---|---|
| **S1** | **Desktop web** | **NOT REACHED** | No ruling adds, removes or re-composes a screen. Ruling 4 changes the **export's** copy of the rendered view; the live `/dossier/<id>` exhibit and `/approvals/<proposal>` are already style-inlined via `chrome.page` and are **unchanged in both markup and CSS**. Ruling 1 is documentation of behaviour already built and rendering (`approval-blocked-by-data`). Rulings 2 and 3 touch no renderer. **Falsify by** finding any element of `pages.approval_detail` or `pages.approval_evidential_region` whose tree or class set changes as a consequence of §25.1–§25.4 — there should be none. |
| **S2** | **Backend HTTP API (`api` and `ges`)** | **REACHED — by ruling 3 only, and only as a future constraint** | Rulings 1, 2 and 4 change no route, request schema or response shape: ruling 1 documents an existing `/ges/decide` context resolution, ruling 2 changes only which tuple two already-registered primitives are named in (`REGISTERED` is untouched, so no detector run changes), ruling 4 is confined to the export writer. Ruling 3 reaches this surface because gates T1–T3 change **how the two processes are packaged and how the api reaches GES in a deployed topology** — no wire contract changes, but the transport that serves it does. Nothing lands in the pilot. **Falsify by** finding a route schema, status code or auth requirement altered by any of the four rulings. |
| **S3** | **Data / export pipeline (Oracle Journal Import file)** | **NOT REACHED** | The Journal Import file is produced by `ges/journal_export.py` under §10's FBDI column contract and contains **no rendered view and no HTML at all**. Ruling 4 is confined to `app/evidence/export.py`'s per-dossier `rendered_view` field in the **F1 auditor export**, which is a different artefact with a different consumer. **Falsify by** showing that the FBDI file's column set, source/category values, or reference-column stamping changes under any ruling here — it does not. |
| **S4** | **Evidential deliverables (F1 auditor export, dossiers, CUEC checklist, published obligations)** | **REACHED — this is the primary surface of ruling 4, and secondarily of ruling 2** | Ruling 4 changes **what the export file contains**: every per-dossier `rendered_view` (and the `approver_view` that is asserted identical to it) gains an inlined `<style>` block, and the integrity section gains a stylesheet digest. **The size figure is deliberately not stated here** — I was given 280 KB, then 624-vs-1,248 classes, and have been wrong once already; `code-agent` measures it against the real stylesheet and real dossier count before building (§25.4bis.3). What it does **not** change: the artefact still does not contain the risk band, and `AC-F41-03` is still not checkable in it (§25.4bis.2). Ruling 2 reaches it more narrowly — findings from primitives 12 and 13 flow into dossiers, and §7.3's new standing rule requires the calibration denial to be **on every emitted finding**, so a dossier carrying a `journal_attribute_outlier` finding must carry the denial with it. **Falsify by** finding an export or dossier whose bytes are unchanged after constraints 1–4 are built. |
| **S5** | **Mobile web** | **NOT REACHED** | Still no MVP1 build target, and more usefully: the two rulings that could plausibly constrain it are neutral for it. Ruling 4's inlined `<style>` is displayable verbatim by any browser including a mobile one — inlining **removes** a dependency (an external stylesheet fetch) rather than adding one, so it strictly widens where the artefact renders. Ruling 3's T1–T3 are deployment-topology gates on the server side and are invisible to any client. **Falsify by** showing an inlined declaration in `chrome.stylesheet()` that requires a desktop viewport to resolve, or a gate in §25.3.2 that assumes a client type. |
| **S6** | **Native mobile (F23 read/monitor, F24 approval)** | **NOT REACHED — and ruling 4 *strengthens* §18.2's constraint on it** | No MVP1 build target. F23 is unaffected for S5's reason: it inherits GES enforcement and retains nothing evidential. **F24 is made harder, not easier, and that is worth recording now**: §18.2 already found that a native client rendering its own approval screen produces a different artefact from the retained view. Ruling 4 makes the retained artefact's **styling** part of what must be reproduced, so "render the same JSON natively" now diverges on typography as well as structure. The only viable F24 remains a webview displaying the server-rendered artefact. **Falsifier corrected 2026-08-06** — it previously cited `.riskband .big`, which is not in this artefact at all (§25.4bis.1). The correct falsifier: design a native renderer that reproduces the artefact's **label/value separation** from the payload alone. It cannot — the payload carries `.lbl` class names, not layout, which is the same fact that makes the unstyled export illegible. |

#### 25.5.1 What must be re-tested, per reached surface

Concrete enough for `test-agent` and the suite owners to act on. **Surfaces whose
evidence the Test gate must show for this pass: S2 and S4.** S1, S3, S5 and S6
require no new evidence, for the reasons above; if any acquires a build target or
if ruling 3's T1–T3 land, this Impact Analysis is re-run first.

| Surface | Suite(s) | What must be shown |
|---|---|---|
| **S2 Backend API** | `architecture` (**mine**), `security` (`security-architect`) | **Nothing new until T1–T3 land in a deployment** — and that is the point of saying so rather than listing a placeholder. When they do: a check **in the api image** that `import ges` raises `ModuleNotFoundError`; a check that `backend/pilot_transport.py` is absent from that image; and **T3 — one complete approval driven end-to-end over `LoopbackHttp`**, which is the scenario that does not exist today. Until then, `ARCH_04`'s two topology scenarios are the whole of the evidence and §20.1 says exactly that. |
| **S4 Evidential deliverables** | `architecture` (**mine**, ARCH-16), `industry`, `functional` | **ARCH-16 must be written and executed** — it is currently unwritten (§20.1). It must assert, on a real export: (a) each per-dossier `rendered_view` contains a `<style>` block; (b) the block is **byte-identical** across every dossier in the export; (c) its SHA-256 matches the digest recorded in the export's integrity section; (d) **the retained view's recorded hash is the hash of the shipped bytes** — constraint 3, the one that would produce a worse defect if got wrong; (e) `check_no_active_content` passes on the post-inlining bytes; (f) determinism — same payload + template ⇒ byte-identical HTML, stylesheet included. Separately, for ruling 2: a dossier carrying a `journal_attribute_outlier` finding must carry the **calibration denial on the finding**, not only in the module header. |

---

### 25.6 What these rulings do to the deferred-substitution register

Stated for the orchestrator to record; **I do not edit `PROJECT_CONTEXT.md`.**

| Entry | Effect | Why |
|---|---|---|
| **19** — pilot transport collapses the trust boundary | **NARROWED, NOT CLOSED** | Ruled sufficient for the pilot on five standing conditions (§25.3.1), and the precondition for first tenant deployment is now written as three conjunctive gates T1–T3 (§25.3.2) rather than as an open residual. It closes when T1/T2 are verifiable in a deploy artefact and T3 executes — none of which is possible on a single-host pilot. Owners: `deploy-agent`, `code-agent`, `test-agent`. |
| **30** — `journal_attribute_outlier` threshold declared, not calibrated | **LEFT OPEN, and re-scoped upward** | Promoting the primitive into §7.3 does not calibrate it, and it must not be read as doing so. What changed is that the disclosure obligation is now an **architectural rule binding every future primitive** (§7.3), not a property of one module. Closing it still needs real close data — register 21/24. |
| **35** — style-inlining (opened at gate 10 from the §9.4 residual) | **RESTATED 2026-08-06, still open, still one work item** — see the row below, which supersedes this one | Ruled at gate 10: inline it, four constraints, `code-agent` + `test-agent` (§25.4). Not a pilot blocker; a precondition on the first real-auditor export. |
| **35 — as it now reads (supersedes the row above)** | **OPEN. Same remedy, different justification, and one thing it was thought to close that it does not.** | **Restated per §25.4bis.** *(i)* The remedy is unchanged: inline `chrome.stylesheet()` into each per-dossier retained view, under §25.4's four constraints. *(ii)* **The reason is now legibility, not `AC-F41-03`.** Unstyled, the artefact glues every label to its value (`Amount312,480.00`, `Coverage of this run70% - partial`) across 133 elements at two computed sizes — a misparse hazard in a seven-year record read by a party with no login and no one to ask, and arguably a failure of `AC-F41-04`'s own "reproduces … the figures, the threshold and the bundle version". *(iii)* **What entry 35 does NOT close, recorded so it is not read as closing it:** `AC-F41-03` is **not** made checkable in this artefact by inlining, because the risk band is absent from it entirely — the retained region derives from the approval screen and the band lives on Review. That is ruled correct and permanent (§25.4bis.2), not a gap. *(iv)* The byte cost is **unmeasured**; the two figures supplied so far were both wrong, and `code-agent` measures it before building. Owners: `code-agent` (build), `test-agent` (ARCH-16). |
| **1** — mTLS on loopback | **UNCHANGED, but re-linked** | §25.3.2 records it as T1–T3's peer: both are preconditions on the same event, and they should reach the human as one deployment gate rather than one at a time during onboarding. |
| **2** — SQLite triggers, no `SERIALIZABLE` | **UNCHANGED, and its test consequence is now disclosed** | §20.1 records that ARCH-06 (blast-radius concurrency under retry-on-serialization-failure) is unwritten *because* the transaction it would exercise is not built. Previously the suite was simply green without it. |
| **No new register entry is opened by these rulings.** | | Ruling 1 closes a stale KB assertion; ruling 2 ratifies what was already built and declared. Neither introduces a new gap between spec and build. |

---

## 24 · Change history

| Date | Version | Change | Approving decision |
|---|---|---|---|
| 2026-08-06 | 1.2.0 | **Gate 11 re-ruling of §25.4 / register 35 (§25.4bis), after `test-agent` falsified its premise in Chromium.** The export's artefact carries **neither** the riskiest-element size nor the element: `riskiest-figure` is absent, because the retained region derives from the **approval** screen while the risk band lives on **Review**. **The root error is mine and predates styling** — §9.4 consequence 3 (2026-07-31) asserted a Review-screen property was checkable in an approval-screen artefact; `AC-F41-03`'s own Given/When says *"when the Review screen is rendered"* and `UX_KB` UX-4 scopes the strengthening the same way. §9.4 consequence 3 is **struck where it stands**, not rewritten. **Rulings: (a) option 3 on `AC-F41-03`** — it is a screen criterion by design, the retained view carries the evidence without the emphasis; **option 2 (importing the risk band) is refused** because it would put in the artefact a fact the approver was never shown — the defect `pages.py` already names from the opposite direction — and because pass 21's per-screen-uniqueness typography judgement is upheld as better architecture than the sentence of mine it contradicted. The emphasis is not lost from the product: `pages.dossier` renders the band style-inlined at 40px. **(b) Option 1 on inlining — still inline, on a replaced reason**: legibility. Unstyled, 133 elements at two computed sizes with every label glued to its value (`Coverage of this run70% - partial`), a misparse hazard in an S4 deliverable read by a party with no login. §25.4's four constraints are unchanged; the byte cost is **unmeasured and to be measured by `code-agent`**, both figures supplied so far having been wrong. Corrected in the same sweep: §19.3's S1 row (which asserted `AC-F41-03` against the retained artefact), §25.5's S4 size claim and S6 falsifier. **Register 35: OPEN, restated — same remedy, different justification, and explicitly not closing `AC-F41-03`.** No `dev/` file modified. | Gate 11 smoke, `test-agent` verification 2026-08-06; routed back by the orchestrator rather than built on |
| 2026-08-05 | 1.1.0 | **Architecture pass 2 — gate 10 review-and-rule (§25).** Four items ruled. (1) **§18.1 was stale, not disclosed**, and is amended: supersession-by-data now has `AC-F41-14`/`-15`, is built in `ges/supersession.py`, is enforced by bundle rule `scope.no_bound_dataset_superseded_by_later_data` (`override_eligible: false`, context resolved server-side), and its **negative half is the rule's `non_firing` fixture**, so §8.2's compile-time fixture evaluation verifies it on every build. The consequential sweep also corrects **§20.1** (same defect) and **§18.3** (routing budget — superseded by `AC-F41-16`/`-17`). (2) **§7.3 grows from eleven primitives to thirteen**: `obligation_gap` (declaration-derived, not history-derived; stays **one** primitive over three closed obligation kinds) and `journal_attribute_outlier` (attribution, not a distance scalar) both join; neither is folded. New **standing calibration-denial rule** binding every future primitive. (3) **Register 19 / §3.2**: the pilot transport is ruled **sufficient for the pilot** on five standing conditions, and the precondition for first tenant deployment is stated as **three conjunctive gates T1–T3** — the `ges` package absent from the api image, `pilot_transport.py` absent from that image, and one full approval exercised over `LoopbackHttp`. Narrowed, not closed. A **gap in the override's claim-prohibition list** is raised for the human (§25.3.3). (4) **§9.4**: the export's per-dossier `rendered_view` **must be style-inlined** — the size emphasis exists only in the stylesheet, so `AC-F41-03` is unverifiable in the artefact the auditor actually receives; four constraints, `code-agent` + `test-agent`, precondition on the first real-auditor export, not a pilot blocker. **§20.1 execution status changed from `STATIC ONLY — NOT EXECUTED` to EXECUTED**: the suite was re-run for real per the standing commitment — 28 scenarios, 0 failures, exit 0 — and eleven §20.2 scenarios are now named as **not present**, including ARCH-06 and ARCH-16. **Impact Analysis §25.5** enumerates all six surfaces; S2 and S4 reached, S1/S3/S5/S6 not reached with falsifiable reasons. No `dev/` file was modified by this pass. | Gate 10 review, 2026-08-05; joint presentation with `security-architect` owed for §25.3.3 |
| 2026-07-31 | 1.0.0 | Initial Architecture pass for MVP1. Five-plane component model with the api↔GES process boundary as the single trust boundary (§3); warehouse-lag resolved via run pinning, close-clock staleness and Point-of-Action Revalidation (§5); certified semantic layer with SQL made unroutable rather than filtered (§6); detector runtime as manifests over eleven registered evaluator primitives (§7); guardrail broker with compiled hash-addressed bundles, compile-time predicate schema binding and transactionally co-committed blast-radius state (§8); evidence store as Postgres + hash chain + KMS-signed anchors + 7-year Object-Lock archive, with server-rendered self-contained rendered views (§9); export path and CUEC model (§10); coverage as a closed sum type (§11). Twelve judgement calls registered (§17). `PLAN` §9.3's per-action-vs-policy-cold question **decided** (§16). Two new findings raised (§18.1 supersession-by-data has no criterion; §18.2 F24 native mobile approval is incompatible with the rendered-view mechanism). **Impact Analysis §19** establishes a six-surface register; four surfaces reached, two not reached with falsifiable reasons. Architecture suite specified, **STATIC ONLY — NOT EXECUTED** (§20.1). Four items handed to `security-architect` for joint presentation (§22). | Standing authorization to build MVP1, `PROJECT_CONTEXT.md` Decisions Log 2026-07-31; gate 6 joint sign-off with `security-architect` pending |
