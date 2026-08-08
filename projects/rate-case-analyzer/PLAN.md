# PLAN — rate-case-analyzer · MVP1

**Gate 3 · Plan & Backlog** · written 2026-08-07 by `plan-agent` ·
operating mode **full autonomy** (gate closes `assumed`, not `approved`).

Companion artifact: [`FEATURES.md`](FEATURES.md) — the itemized backlog with
stable IDs. This file is the *why* and the *shape*; that file is the *what*.

Binding inputs read in full before writing: [`INTAKE.md`](INTAKE.md),
[`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md),
[`knowledge/DOMAIN_KB.md`](knowledge/DOMAIN_KB.md),
[`knowledge/INDUSTRY_KB.md`](knowledge/INDUSTRY_KB.md).

---

## 0. Completeness check — binding decisions this plan was checked against

Per the `plan-agent` contract, every binding decision recorded in
`PROJECT_CONTEXT.md`'s Decisions Log and in the two KBs, with how this plan
satisfies it. Nothing below is silently dropped.

| Binding decision | Where recorded | How this plan satisfies it |
|---|---|---|
| MVP = capabilities **#1 + #2** only; #3 deferred | Decisions Log 2026-08-07; A8.3 | §1 goals / §2 non-goals. Peer-aggregate/statistics engine explicitly **out** (`F33`), which is the load-bearing half of #3. |
| Two surfaces: desktop web + scheduled ingestion job, shared backend and corpus store | Decisions Log; A5.1/A5.3 | §3.1 shape; `F35`–`F40` (web), `F42`–`F43` (job), sharing §4 data model and §3.4 answer path. |
| Grounding mandatory; unsupported claim refuses rather than paraphrases | Standing constraint 1; A7.3 | §3.5 grounding pipeline; sentinel refusal `F31`; deterministic citation verification `F30` fails **closed**. |
| Ethical wall: two corpora, separate stores, separate credentials, retriever bound at **session construction** | Standing constraint 2; IND-14 | §3.3; `F21`, `F22`. No `visibility` column anywhere in §4. Import-boundary test is a shipped artifact, not a review note. |
| Aggregate leak: every number in the future competitive-analysis feature computed over the **public corpus only** | Standing constraint 3 | §3.3 — `corpus` is a first-class field on every `Source` in MVP1 **even though no aggregate exists yet**, so the rule is enforceable when `F33` lands rather than retrofitted. |
| Silence is not clearance — coverage stated explicitly, never an empty flag list | Standing constraint 4; RCA-R7; IND-9 | §3.6 `Coverage` object is returned on **every** answer path including refusal; `F28`, `F37`. |
| Template `custom` — no inherited test harness; building it is our work | Decisions Log 2026-08-07 | §6 phase P0; `F2` (harness + five runners), `F44`–`F49`. Treated as real work with real size, not assumed. |
| `.env`/`.gitignore` hygiene + path-anchored store dirs must be re-established | Decisions Log (override cost b) | `F1`. |
| Stack deferred to gate 6 (`solution-architect`) | Decisions Log 2026-08-07 | §7 states **requirements the stack must satisfy** and names no library, framework, database or model vendor. |
| **ASM-1** jurisdictions = PA PUC + PUCT + CPUC | Decisions Log | `F6`, `F7`, `F8`. Michigan/FERC/Illinois appear in the backlog as deferred items with their recorded reasoning, not deleted. |
| **ASM-2** live fetch behind a flag; correctness proven on fixtures + synthetic corpus | Decisions Log | §3.2; `F5` (flag + fixture capture tooling), ASM-19. |
| **ASM-3** `sources[]` blocking — cited source must be one the answer relies on | Decisions Log | §3.5 step 6 and `F30`. This is the single largest deviation from `policy-lookup-assistant`. |
| **ASM-4** full 14-agent roster, nothing dropped | Decisions Log | §8 maps every backlog item to an owning agent; no agent is left without an obligation. |
| **ASM-5** all suites blocking, no advisory exceptions | Decisions Log | `F44`–`F49` all MVP1; §6 P6 gates on them. |
| Authority is **two-dimensional**: `document_type` (14 ranked) × `claim_status` (6); `NOT_STATED` representable, never `null` | Gate 1 findings; DOMAIN §2.3/§2.4 | §4.2/§4.5. `NOT_STATED` is a required enum member on every status-bearing field; §4.6 states the no-nullable-enum rule as a schema invariant. |
| Comparability is a **structured predicate** over extracted metadata with mismatches **named** — not an embedding score | Gate 1 findings; RCA-R14; DOMAIN §3 | §3.7, `F27`. Embeddings are used only *inside* an already metadata-filtered candidate set (`F26`). |
| Confidential material in public dockets → **quarantine-and-report**, never flag-and-index | Gate 1 findings; IND-10; RCA-R11 | §3.2 stage 2; `F10`. Quarantined items never reach a store, so there is no "flagged but present" state to leak. |
| Every ingested case needs its **final order / compliance tariff** | Gate 1 findings; INDUSTRY §6.5.1 | §3.2 stage 6 outcome-completeness gate; `F15`. A `DECIDED` case with no outcome document **fails ingest loudly**. |
| Schema-bound risks that cannot be retrofitted: RCA-R4 supersession, RCA-R11 confidentiality, RCA-R13 case status incl. withdrawn | Gate 1 findings | §4.2/§4.3 fields; `F16`, `F10`, `F4`. All three are in the MVP1 schema even where the *behaviour* they enable is thin. |
| Sentinel-token refusal ported: exact `.startswith()` on stripped content, model prose **discarded** on refusal | Deliberate reuse | §3.5 step 7; `F31`. No regex, no case-insensitivity, no substring match. |
| Manifest-driven ingest-time authority validation, fail-loud; **close** the malformed-key gap with a closed-enum schema check | Deliberate reuse | `F3` — closed-enum validator rejecting unknown *keys* as well as unknown *values*. |
| Badge/citation UI: authority never by colour alone; refusal styled neutral, never as an error | Deliberate reuse; IND-3, IND-8 | `F36`, `F38`, `F48`. |
| Two ported bug fixes (whitespace-rejecting question validator; `AIMessage.content: str \| list` normalisation) | Deliberate reuse | `F49`, ported on day one as regressions, not rediscovered. |
| Extrapolation-trap regression test carried to Test gate | Deliberate reuse; RCA-R6 | `F47` red-team suite, named case. |
| **NOT** reused: `policy-lookup-assistant`'s no-authn/no-authz decision | Deliberate reuse §"Explicitly NOT reused" | §3.3 / ASM-12 — session **role binding** exists in MVP1; a *login* does not. These are separated deliberately. |
| IND-16: political/affordability context is out-of-corpus and must be written into capability #3's brief **now** | INDUSTRY §2.8, IND-16, owner `plan-agent` | §9 — discharged here, in this document, at the time it was cheap. This is my own named obligation and it is closed in this pass. |

Open questions carried from Intake and **still open** (none blocks MVP1):
A3.3 user count; A6.4 retention (`F54` — blocking before any real work product);
A9.3 compliance obligations. All three are restated in §5 as live risks, not
silently retired.

---

## 1. Goals — what MVP1 must be able to do

MVP1 is capabilities **#1 + #2**, and nothing else. Stated as observable
behaviour, because these become the Test gate's acceptance criteria:

**G1 · Corpus exists and is honest about itself.** A defined set of real public
rate cases from PA PUC, PUCT and CPUC — each with its **outcome** document, not
only its ask — plus a synthetic internal-history corpus, ingested with closed,
validated metadata. The corpus can state its own boundaries: which
jurisdictions, which date range, which document types, which known exclusions.

**G2 · A precedent question gets a grounded answer or an honest refusal.** A
strategy lead asks a precedent question and receives either (a) an answer in
which **every** citation resolves to commission + docket number + document
identity + in-document locator + `document_type` + `claim_status` + date +
verbatim supporting text, or (b) a refusal that **names the missing dimension**.
There is no third outcome. A partially-hedged paraphrase is not a permitted
output state.

**G3 · Asked is never rendered as granted.** A requested ROE cannot surface as
an authorized ROE. A black-box settlement yields `NOT_STATED`, never a
back-solved or borrowed number.

**G4 · Comparability is explicit and named.** Any answer drawing on a case that
differs from the question's frame on a comparability dimension **names the
dimension**. Non-comparability on a blocking dimension refuses rather than
caveats.

**G5 · Coverage is always stated.** Every answer, including every refusal,
reports what was examined and what could not be assessed and why. There is no
UI state in which "nothing found" and "nothing looked at" render identically.

**G6 · The wall holds structurally.** The public and work-product corpora live
in physically separate stores under separate credentials, and the retriever is
bound at session construction. A test proves there is no code path from a
public-only session to the work-product store — not a path returning empty.

**G7 · The ingestion job fails loudly.** A scheduled run that fetches a login
page, an access-denied body, a confidential-marked document, or a decided case
with no order, stops and reports. It never quietly stores the wrong thing, and
a job that has stopped running is visible on the web surface.

**G8 · The test suite exists.** Five blocking suites (functional, industry,
security, red-team, UI) with a runner structure built from scratch, because the
custom-template override means none was inherited.

---

## 2. Non-goals — explicitly out of MVP1

Each of these is in `FEATURES.md` as a deferred item with reasoning, **not
deleted**. The human can pull any of them forward.

- **Capability #3** — approval likelihood / competitive analysis, and with it
  any peer-average, benchmark or statistical aggregate over the corpus (`F33`,
  `F51`). This is the recorded MVP boundary, and §9 pre-writes its brief.
- **Intervenor / commission-staff sessions and authentication** (`F24`).
- **Real (non-synthetic) work product** (`F54` gates it).
- **Exports** — memo, workbook, provenance-trail export (`F41`, `F55`).
- **Mobile** (never anticipated; not in the backlog at all beyond this line).
- **OCR of scanned filings** (`F19`) — scanned documents quarantine rather than
  degrade silently.
- **Data-request responses and hearing transcripts as ingested content**
  (`F20`) — they stay in the `document_type` enum and are classified-and-skipped,
  so adding them later is not a schema change.
- **Additional jurisdictions** — FERC (`F50`), Illinois ICC (`F52`), Michigan
  MPSC (`F53`), gas (`F56`).
- **Multi-year rate plan / PBR modelling** (`F57`) — the schema does not assume
  one-case-one-ROE, but MYRP-specific behaviour is not built.

---

## 3. The shape of the system

Five parts. The two surfaces (web, scheduled job) sit at opposite ends of the
same spine, which is why they share a backend and a store (A5.3).

```
  [scheduled ingestion job]                    [desktop web surface]
            │                                            │
            ▼                                            ▼
  ┌──────────────────────┐                    ┌────────────────────────┐
  │ 1. ACQUISITION       │                    │ 5. ANSWER SURFACE      │
  │  docket adapters     │                    │  question → answer     │
  │  PA / TX / CA        │                    │  citation cards        │
  │  live-fetch FLAG     │                    │  coverage panel        │
  └──────────┬───────────┘                    │  refusal (neutral)     │
             ▼                                └───────────▲────────────┘
  ┌──────────────────────┐                                │
  │ 2. QUARANTINE GATE   │                    ┌───────────┴────────────┐
  │  non-document detect │                    │ 4. GROUNDING PIPELINE  │
  │  confidentiality     │                    │  frame → filter →      │
  │  → REPORT, not index │                    │  comparability →       │
  └──────────┬───────────┘                    │  compose → VERIFY →    │
             ▼                                │  refuse-or-answer      │
  ┌──────────────────────┐                    └───────────▲────────────┘
  │ 3. EXTRACTION        │                                │
  │  text + locators     │              ┌─────────────────┴──────────────┐
  │  doc-type + parent   │              │  SESSION-BOUND RETRIEVERS      │
  │  case metadata       │              │  (constructed, not selected)   │
  │  structured claims   │              └───▲────────────────────────▲───┘
  └──────────┬───────────┘                  │                        │
             ▼                    ┌─────────┴────────┐   ┌───────────┴──────────┐
             └───────────────────▶│ STORE: public    │   │ STORE: work-product  │
                                  │ own credentials  │   │ own credentials      │
                                  └──────────────────┘   └──────────────────────┘
                                        (no shared client, no shared config object)
```

### 3.1 Two surfaces, one spine

The web surface never writes to a store. The ingestion job never serves a query.
They share the §4 data model and the enum/validation module (`F3`), and nothing
else. This is deliberate: it is what makes G7 testable — the job can be run to
completion in a test with no web surface present, and the web surface can be
tested against a fixture corpus with no job running.

The job is treated as a first-class surface because it fails independently
(recorded rationale, Decisions Log). Concretely that means it owns its own run
report (`F43`) and its own failure signal, and the web surface reads corpus
freshness from a record the job writes (`F39`).

### 3.2 Ingestion pipeline — seven stages, each able to fail loudly

Ordering matters here and is a design decision, not an implementation detail:
**classification and quarantine happen before anything is written to a store.**
There is no state in which a confidential document is in the corpus wearing a
flag (constraint 8).

1. **Discover** — per-jurisdiction adapter enumerates candidate documents for a
   docket, returning index entries (title, native document id, source URL,
   filed date, any index-level confidentiality marking). Live network access is
   behind the `LIVE_FETCH` flag (ASM-2); default off, fixtures otherwise.
2. **Fetch & sanity-gate** — retrieve bytes. **Fail loud** if the response is a
   login page, an access-denied body, an HTML error, a zero-length body, or a
   content type inconsistent with the index entry (IND-11, `F9`). An HTML error
   body stored as a document is the mundane bug with the serious signature; it
   is caught here, once, rather than being detectable downstream.
3. **Confidentiality classify & quarantine** — from index metadata **and** a
   first-page marking scan (`CONFIDENTIAL`, `HIGHLY SENSITIVE`, `SUBJECT TO
   PROTECTIVE ORDER`). Prefer the public redacted version where a
   redacted/unredacted pair is detectable; never ingest both; never dedupe to
   the unredacted one. Quarantined items go to a quarantine record with a
   reason, and appear in the run report. They never enter a store (IND-10,
   RCA-R11, `F10`).
4. **Extract text with locators** — page number always; line numbers where the
   document is line-numbered (rate case testimony is line-numbered *precisely
   so it can be cited*); schedule number for exhibits; finding-of-fact number
   for orders. A document from which no text can be extracted is quarantined as
   `NO_EXTRACTABLE_TEXT` rather than OCR'd (ASM-10) — a scanned filing silently
   contributing nothing is worse than a scanned filing loudly contributing
   nothing. (`F11`)
5. **Classify document & bind parent** — assign `document_type` from the closed
   14-value enum. An `EXHIBIT_SCHEDULE` **must** resolve to a parent filing and
   inherit that parent's case identity and authority; an exhibit with no
   resolvable parent **fails ingest** rather than entering the store as an
   unattributable number (RCA-R8, `F12`).
6. **Assemble the case record & gate on outcome** — extract case-level metadata
   (§4.2). Then the **outcome-completeness gate**: a case whose `case_status` is
   `DECIDED` or `SETTLED_APPROVED` and which has no `FINAL_ORDER`,
   `ORDER_ON_REHEARING`, `APPROVED_SETTLEMENT` or `COMPLIANCE_FILING` document
   **fails ingest loudly**. `PENDING` and `WITHDRAWN` cases may be ingested with
   no outcome, but are then structurally barred from producing an `AUTHORIZED`
   claim (constraint 7, RCA-R13, `F15`).
7. **Extract structured claims & link** — the fixed MVP1 parameter set (§4.5,
   ASM-8) with `claim_status`, unit, scope and basis; supersession links
   (`F16`); non-precedent settlement clause (`F17`); rider/non-base-rate
   classification (`F18`). Then write to the store.

### 3.3 The two corpora and the wall

Two **physically separate** stores. Not two collections in one database, not one
store with a `visibility` column, not one client with two namespaces. Each has
its own credential set, loaded from its own configuration key, and there is no
factory function that takes a corpus name as a string argument — because a
string argument is exactly the thing that gets passed wrong.

Session construction, stated concretely enough that `code-agent` has no room to
improvise:

- `UtilityAnalystSession` is constructed with **both** a public retriever and a
  work-product retriever. A utility-side analyst legitimately needs their own
  historical cases; the wall is not between the analyst and their own files.
- `IntervenorSession` — **not built in MVP1** (`F24`) — would be constructed
  with the public retriever **only**. Its future existence is why the binding
  must be structural now.
- There is no `Session` base class method that returns "the retriever for
  corpus X." The retrievers are distinct constructor-injected attributes with
  distinct types.
- Every `Source` carries `corpus: PUBLIC | WORK_PRODUCT`. In MVP1 this drives
  UI labelling. Its real purpose is that when `F33` (aggregates) lands, the
  public-corpus-only rule (constraint 3) is a filter over a field that already
  exists on every historical record, rather than a retrofit over data that
  never distinguished them.
- **Enforcement is a test, not a convention**: `F22` includes a static
  import-boundary assertion that the module implementing the public answer path
  does not transitively import the work-product store module.

### 3.4 Retrieval — metadata first, embeddings second

RCA-R14 is the reason for the ordering. Rate case testimony is formulaic; a DCF
cost-of-capital section reads nearly identically across utilities and decades,
so embedding similarity carries little discriminating signal and will happily
rank a 2011 Georgia vertically-integrated case as "similar" to a 2025
Massachusetts distribution-only settlement.

Therefore: the query frame's hard dimensions (jurisdiction, utility, date
window, `document_type` class, `claim_status` sought, case type) are applied as
**metadata filters that constrain the candidate set**, and vector similarity
ranks only *within* that already-constrained set. Similarity never widens the
set. (`F26`)

### 3.5 Grounding — the answer path, in order

Seven steps. Steps 4, 6 and 7 are each independently capable of producing a
refusal, and a refusal at any of them discards the model's prose entirely.

1. **Parse the question into a query frame** (`F25`) — a closed-schema
   structured object: jurisdiction(s), utility, parameter, `claim_status`
   sought, test-year convention, market structure, date window, customer class.
   Dimensions the question does not specify are marked `UNSPECIFIED`
   explicitly. **A parse failure is a refusal, not a best-effort keyword
   search** (ASM-11) — a best-effort search over this corpus is the mechanism of
   RCA-R2.
2. **Filtered retrieval** within the session-bound retrievers (§3.4).
3. **Comparability predicate** over the candidate cases (§3.7) → an `included`
   set, an `excluded` set with per-case reasons, and an `unassessable` set with
   per-case reasons.
4. **Sufficiency check.** If the `included` set cannot support the frame — no
   case matches the jurisdiction, no case has the parameter at the requested
   `claim_status`, every candidate mismatches on a blocking dimension — emit the
   sentinel refusal **naming the specific missing dimension** (RCA-R6). "I don't
   have enough information" is an explicitly failing output; the refusal must
   say *what* is missing, because a user who is told only "no" will guess, and
   the guess reproduces the harm outside the tool.
5. **Compose** the answer, constrained to the `included` evidence, with the
   model required to attach an evidence-id citation tag and a verbatim quoted
   span to every factual assertion (`F29`).
6. **Deterministic citation verification — the ASM-3 step** (`F30`). For every
   citation the model emitted, mechanically check: (a) the evidence id was one
   actually supplied to the model; (b) the quoted span is verbatim present in
   that chunk under whitespace/hyphenation normalisation; (c) the asserted
   `document_type` and `claim_status` match the stored record; (d) for a numeric
   assertion, the number matches the stored `Claim` record's value, unit, scope
   and basis. **Any failure discards the entire answer and falls through to
   refusal.** `sources[]` is then constructed *from the verified citations only*
   — never from the retrieval result set.

   This is the deliberate break from `policy-lookup-assistant`. Its accepted
   trade-off was that `sources[]` reflected what retrieval pulled. Here that is
   not merely imprecise: per DOMAIN §6.8, the third and most dangerous
   hallucination kind is *a real quote from a real source that does not support
   the proposition*, and it is not caught by verifying the docket exists.
   Showing retrieval hits beside a claim manufactures the appearance of support.
7. **Sentinel refusal** (`F31`) — the model's own first line is a fixed
   `INSUFFICIENT_EVIDENCE` literal, parsed by exact `.startswith()` on stripped
   content. **Never** regex, never case-insensitive, never substring. On a
   refusal the model's prose is discarded entirely and replaced by a
   product-controlled string composed of: the named gap, the coverage statement,
   and the resolvable cases that *were* examined. Discarding the prose is what
   stops a partially-hedging paraphrase leaking through, and a partially-hedging
   paraphrase is the mechanism of the fabricated-precedent harm.

### 3.6 Coverage — returned on every path, including refusal

The `Coverage` object (§4.7, `F28`) is not an optional decoration on successful
answers. It is part of every response, and it is the direct implementation of
constraint 4 / RCA-R7 / IND-9.

There must be **no rendering in which an empty result and an unexamined corpus
look the same**. Concretely, the UI never shows a bare empty list; it shows
"checked N comparable cases across 3 jurisdictions (2019–2026); included K;
excluded M because …; could not assess J because …; corpus as of
<date>; rider and formula-rate proceedings are not ingested."

The `known_exclusions` field carries the standing corpus-level caveats — rider
proceedings excluded from base-rate treatment, data requests and transcripts not
ingested, scanned documents quarantined — so a coverage gap the product *has* is
a gap the product *states* (IND-9, INDUSTRY §1.7).

### 3.7 Comparability — a predicate, not a score

Per the gate 1 finding and RCA-R14, comparability is a structured predicate over
extracted metadata that **names** its mismatches. It returns:

```
Comparability {
  verdict:    COMPARABLE | COMPARABLE_WITH_CAVEATS | NOT_COMPARABLE
  matched:    [dimension]
  mismatched: [{ dimension, query_value, case_value, severity }]
  unknown:    [{ dimension, reason }]     # NOT_STATED in the corpus
}
```

Dimensions and severities — this table is the design decision, and it is what
`code-agent` implements rather than inventing:

| Dimension | Source | Severity when mismatched |
|---|---|---|
| `market_structure` (vertically integrated vs. restructured wires-only) | DOMAIN §3.2, IND-5 | **BLOCKING** — the ~34bp structural gap is unrelated to case merits; composition of the revenue requirement differs in kind |
| `case_type` — rider/formula-rate proceeding vs. base rate case | DOMAIN §3.4, IND-9 | **BLOCKING** for any base-rate question; standard RRA practice excludes rider cases, and this is an ingestion-time classification |
| `jurisdiction`, when the question asks what a commission *authorized* | DOMAIN §3.1, RCA-R2 | **BLOCKING** — out-of-state ROEs are market evidence, never controlling authority, and the answer language must preserve that distinction |
| `test_year_convention` (HTY / forecast / FPFTY / hybrid) | DOMAIN §1.3, IND-4 | **CAVEAT** (escalates to BLOCKING when the question names a convention — this is exactly RCA-R6) |
| `vintage` — order date outside the configured window | DOMAIN §3.5, RCA-R10, IND-8 | **CAVEAT** |
| `resolution_path` — settled vs. fully litigated | DOMAIN §3.6 | **CAVEAT**, and the system must **not** editorialise a directional spread: RRA finds no consistent difference, so asserting "settlements come in lower" is asserting folklore |
| `capital_structure` / equity ratio band | DOMAIN §3.8 | **CAVEAT** — comparing ROEs without equity ratios is the most common analyst error in the domain |
| `utility_scale` | DOMAIN §3.7 | **INFO** |
| `non_precedent_clause` present on the source settlement | RCA-R12, IND-7 | **CAVEAT**, always surfaced with any answer relying on that case |

`NOT_COMPARABLE` on a BLOCKING dimension removes the case from `included` and
puts it in `excluded` **with the dimension named**, where the coverage statement
reports it. It does not silently drop.

---

## 4. Data model

Stack-agnostic. Field names are prescriptive so `code-agent` is not inventing
them; storage technology is `solution-architect`'s call (§7).

### 4.1 `Jurisdiction`

`code` (`PA_PUC | PUCT | CPUC`), `name`, `docket_url_pattern`,
`document_url_pattern`, `default_market_structure` *(advisory only — never
authoritative for a case; DOMAIN §1.3 is explicit that convention is per-case,
sometimes, and must be extracted, never inferred from the state)*,
`terms_of_use_reviewed_at`, `crawl_policy` (IND-18).

### 4.2 `Case`

`case_id`, `jurisdiction_code`, `docket_number` *(the commission's own format —
the string a human can paste into the docket system)*, `utility_name`,
`utility_id`, `case_type` (`BASE_RATE | RIDER_TRACKER | COST_OF_CAPITAL |
SECURITIZATION | FORMULA_RATE_ANNUAL | MYRP | OTHER`), `case_status` (`PENDING |
DECIDED | SETTLED_APPROVED | WITHDRAWN | DISMISSED`), `filed_date`,
`decided_date`, `test_year_convention` (`HISTORICAL | FORECAST | FPFTY | HYBRID
| NOT_STATED`), `test_year_start`, `test_year_end`, `market_structure`
(`VERTICALLY_INTEGRATED | RESTRUCTURED_WIRES_ONLY | NOT_STATED`),
`resolution_path` (`LITIGATED | SETTLED_FULL | SETTLED_PARTIAL | NOT_STATED`),
`non_precedent_clause` (`present: bool`, `quote`, `locator`), `topic_tags[]`
*(open vocabulary — e.g. `LARGE_LOAD_TARIFF`, `WILDFIRE`, `STORM_RECOVERY`;
present in MVP1 so the deferred large-load feature `F58` is not a schema
change)*, `docket_url`, `has_outcome_document: bool`, `corpus`
(`PUBLIC | WORK_PRODUCT`), `ingested_at`, `as_of`.

Three fields here exist because of gate 1's non-retrofittable finding:
`case_status` including `WITHDRAWN` (RCA-R13 — PECO withdrew PA rate cases in
2026, leaving a full docket of persuasive testimony and **no outcome at all**,
which is a live source of RCA-R1), `has_outcome_document` (constraint 7), and
`non_precedent_clause` (RCA-R12).

### 4.3 `Document`

`doc_id`, `case_id`, `document_type` (the closed ranked 14-value enum, DOMAIN
§2.3), `authority_rank` (1–14, derived, stored for retrieval ordering),
`parent_doc_id` *(required for `EXHIBIT_SCHEDULE`; §3.2 stage 5)*, `title`,
`filed_date`, `order_number`, `order_date`, `author_party` (`UTILITY | STAFF |
INTERVENOR | ALJ | COMMISSION | JOINT | NOT_STATED`), `witness_name`,
`source_url` *(stable and citable — IND-12)*, `retrieved_at`, `content_hash`,
`confidentiality` (`PUBLIC | REDACTED_PUBLIC | PROTECTED | UNKNOWN`),
`supersedes_doc_id`, `superseded_by_doc_id` *(RCA-R4)*, `corpus`.

A document with `confidentiality = PROTECTED` **is not in this table** — it is a
quarantine record (§4.8). The enum value exists so a quarantine record can state
why, not so a protected document can sit in the corpus wearing a flag.

### 4.4 `Chunk`

`chunk_id`, `doc_id`, `text`, `embedding`, `locator` (`page`, `line_start`,
`line_end`, `schedule_no`, `finding_no`), plus **denormalised** `case_id`,
`jurisdiction_code`, `document_type`, `authority_rank`, `order_date`,
`market_structure`, `test_year_convention`, `case_type`, `case_status`,
`superseded: bool`, `corpus`.

The denormalisation is deliberate and is the mechanism of §3.4: filters must be
applicable at the vector-search boundary, not as a post-hoc join, or the
metadata-first ordering degrades into similarity-first with a filter bolted on.

### 4.5 `Claim` — the two-dimensional authority model in the data

One row per extracted numeric claim. This is where DOMAIN §4's precision traps
are made structurally unrepresentable rather than merely tested for.

`claim_id`, `case_id`, `doc_id`, `chunk_id`, `parameter`, `value`, `unit`,
`basis`, `scope`, `customer_class`, `claim_status`, `effective_date`,
`rate_year`, `locator`, `verbatim_quote`, `extraction_confidence`, `corpus`.

- `parameter` (MVP1 fixed set, ASM-8): `ROE`, `ROR`, `EQUITY_RATIO`,
  `RATE_BASE`, `GROSS_PLANT`, `NET_PLANT`, `REVENUE_REQUIREMENT_TOTAL`,
  `REVENUE_REQUIREMENT_INCREASE`. Note `GROSS_PLANT` / `NET_PLANT` / `RATE_BASE`
  are three distinct parameters, never one — they differ by 30–50% and appear on
  adjacent lines of the same schedule (DOMAIN §4.2). Likewise
  `REVENUE_REQUIREMENT_TOTAL` vs. `_INCREASE`, stored separately and never
  derived one from the other (DOMAIN §4.3).
- `unit`: `PERCENT | BASIS_POINTS | USD | USD_PER_KWH | USD_PER_MONTH | RATIO`.
  Explicit because "reduced ROE by 25" is 25bp, not 25% (DOMAIN §4.4).
- `basis`: `PRETAX | AFTERTAX | NOT_STATED` — the ~1.3–1.4× revenue conversion
  factor means a return-level figure quoted as a revenue-level figure overstates
  by ~35% (DOMAIN §4.5).
- `scope`: `TOTAL_COMPANY | RETAIL_JURISDICTIONAL | CLASS_SPECIFIC |
  SYSTEM_AVERAGE | NOT_STATED` — a total-company number answered to a "what did
  [state] authorize" question can be wrong by a factor of two and will look
  entirely plausible (DOMAIN §4.6); a system-average increase must never answer
  a class-specific question (DOMAIN §4.8).
- `claim_status`: `REQUESTED | RECOMMENDED | SETTLED | AUTHORIZED | IMPLEMENTED
  | NOT_STATED`.

**Invariant `AUTHORIZED`**: a claim may carry `claim_status = AUTHORIZED` only
if its `doc_id` resolves to a document of type `FINAL_ORDER` or
`ORDER_ON_REHEARING`, and only if the parent case's `case_status` is `DECIDED`.
A `PENDING` or `WITHDRAWN` case cannot produce an `AUTHORIZED` claim (RCA-R13).
This is enforced at write time, not query time — it is RCA-R1 made
unrepresentable.

**Invariant `SETTLED` / black box**: for a case with an `APPROVED_SETTLEMENT`
that does not state a parameter, the correct record is a `Claim` row with
`claim_status = NOT_STATED` — **not** an absent row, and **not** `null`. "The
settlement did not specify an ROE" and "we failed to parse the ROE" are
different facts, and collapsing them destroys the system's ability to refuse
honestly (DOMAIN §2.4, §4.1; IND-6; RCA-R5). A parse failure is a *third*
distinct state, recorded on the ingest run report, never in the `Claim` table.

### 4.6 Schema invariants

1. **Every enum is closed and validated at ingest**, fail-loud on an unmapped
   value **and on an unmapped key** — closing the malformed-keys-pass-through
   gap that `policy-lookup-assistant`'s KB identified and deferred. That gap was
   tolerable for two hand-written manifest entries; it is not tolerable for a
   machine-populated multi-jurisdiction corpus.
2. **No status-bearing field is nullable.** Where a value is genuinely absent
   from the source, the value is `NOT_STATED`. `null` is reserved for "not
   applicable to this record type" and is never rendered to a user as an answer.
3. **The query path never reads a manifest.** Metadata is validated once, at
   ingest, and travels with the data (ported pattern).
4. **No `visibility` column anywhere.** Corpus separation is physical (§3.3);
   the `corpus` field on records is for *labelling and later aggregate scoping*,
   never for access filtering.

### 4.7 `Coverage` (response-side, not stored)

`candidates_considered`, `included[]`, `excluded[{case_id, dimension, reason}]`,
`unassessable[{case_id, reason}]`, `jurisdictions[]`, `date_range`,
`corpus_as_of`, `corpus_stale: bool`, `known_exclusions[]`.

### 4.8 `QuarantineRecord` and `IngestRun`

`QuarantineRecord`: `source_url`, `jurisdiction_code`, `docket_number`, `title`,
`reason` (`PROTECTED_MARKING | ACCESS_DENIED | NON_DOCUMENT_BODY |
NO_EXTRACTABLE_TEXT | UNRESOLVED_PARENT | MISSING_OUTCOME_DOCUMENT |
ENUM_VALIDATION_FAILURE`), `detected_at`, `evidence` *(the marking text or
response signature that triggered it)*.

`IngestRun`: `run_id`, `started_at`, `finished_at`, `mode` (`LIVE | FIXTURE`),
`documents_seen`, `documents_ingested`, `quarantined[]`, `failures[]`,
`status` (`SUCCEEDED | FAILED | PARTIAL`). The web surface reads the latest
successful run's `finished_at` as `corpus_as_of` (`F39`) — which is how a
silently-stopped job becomes visible rather than producing confident answers
over a stale corpus (RCA-R13).

### 4.9 `QueryRecord` — the provenance trail (IND-15)

`query_id`, `asked_at`, `session_role`, `question_text`, `query_frame`,
`retrieved_chunk_ids[]`, `comparability_results`, `verified_sources[]`,
`outcome` (`ANSWERED | REFUSED_INSUFFICIENT | REFUSED_VERIFICATION_FAILED |
REFUSED_PARSE_FAILED`), `refusal_gap`, `corpus_as_of`, `model_identifier`.

Retained because a utility's use of AI in preparing a filing may itself become
discoverable or commentable — the Arizona Corporation Commission opened the
first formal state inquiry into utility AI governance in early 2026 (INDUSTRY
§3.3, §4.6). Building the trail is cheap now and unreconstructable later.
Note that `outcome` distinguishes the *three* refusal reasons, which is what
makes the red-team suite able to assert *why* a refusal fired rather than only
*that* it did.

---

## 5. Risks and mitigations

Every `RCA-*` and every `IND-*` is accounted for. Nothing is marked "accepted"
without a reason.

| Risk | Mitigation in this plan | Feature |
|---|---|---|
| **RCA-R1** ask presented as outcome | `AUTHORIZED` write-time invariant (§4.5); authority-ranked retrieval; `claim_status` on every rendered figure | `F3`,`F14`,`F36`,`F44` |
| **RCA-R2** cross-jurisdiction blending | Jurisdiction is a BLOCKING comparability dimension for authorization questions; frame-parse failure refuses rather than searches loosely | `F25`,`F27`,`F47` |
| **RCA-R3** non-comparable peer set | `market_structure` and rider `case_type` BLOCKING; **and** aggregates are out of MVP1 entirely (ASM-14), which removes the surface the risk needs | `F18`,`F27`,`F33`(deferred) |
| **RCA-R4** superseded order treated as current | `supersedes_doc_id`/`superseded_by_doc_id` in schema; `superseded` denormalised onto chunks; superseded documents suppressed or explicitly labelled | `F4`,`F16` |
| **RCA-R5** black box back-solved | `NOT_STATED` as a stored `Claim` row, never `null`, never absent; parse failure is a distinct third state on the run report | `F3`,`F14`,`F44` |
| **RCA-R6** extrapolation trap | Sufficiency check (step 4) refuses when the frame's dimension is uncovered, and the refusal **names the dimension**; test-year convention escalates to BLOCKING when the question names it | `F27`,`F31`,`F47` |
| **RCA-R7** silence read as clearance | `Coverage` returned on every path including refusal; UI cannot render an empty list | `F28`,`F37`,`F47` |
| **RCA-R8** orphan exhibit number | `EXHIBIT_SCHEDULE` must resolve a parent or fail ingest; every chunk carries denormalised case identity | `F12`,`F44` |
| **RCA-R9** unit/scope confusion | `unit`, `basis`, `scope`, `customer_class` as required fields; three distinct rate-base parameters; total vs. increase stored separately | `F3`,`F14`,`F44` |
| **RCA-R10** stale precedent, no vintage | `order_date` mandatory and always displayed; vintage CAVEAT dimension; all-supporting-cases-older-than-threshold caveat | `F32`,`F36` |
| **RCA-R11** confidential discovery in "public" corpus | Quarantine-and-report **before** any store write; redacted-version preference; never both | `F10`,`F46` |
| **RCA-R12** non-precedent settlement language ignored | Clause extracted at ingest; surfaced as a CAVEAT with any answer relying on the case | `F17`,`F45` |
| **RCA-R13** moving-target docket / silent staleness | `case_status` incl. `WITHDRAWN`; `AUTHORIZED` invariant; `IngestRun` drives the freshness banner | `F4`,`F15`,`F39`,`F43` |
| **RCA-R14** formulaic prose defeats retrieval | Metadata filters constrain the candidate set; similarity only ranks within it | `F26`,`F44` |
| **IND-1** document role closed enum, fail-loud | `document_type` + `author_party` | `F3`,`F12` |
| **IND-2** posture on every numeric | `claim_status` on every `Claim` | `F14` |
| **IND-3** ranked authority visible in UI as label text | `authority_rank` stored; citation card renders label, never colour alone | `F36`,`F48` |
| **IND-4** test-year convention required, comparisons caveated/refused | Required enum; CAVEAT→BLOCKING dimension | `F13`,`F27` |
| **IND-5** market structure required | Required enum; BLOCKING dimension | `F13`,`F27` |
| **IND-6** black box → explicit "not stated" reaching the UI | `NOT_STATED` rendered as text, not as blank | `F14`,`F36` |
| **IND-7** non-precedential disclaimer surfaced | Extracted and rendered | `F17`,`F40` |
| **IND-8** order date mandatory and always displayed | Citation card invariant, UI-tested | `F36`,`F48` |
| **IND-9** corpus states coverage boundaries | `Coverage.known_exclusions` + per-query statement | `F28`,`F37` |
| **IND-10** confidential-material quarantine | §3.2 stage 3 | `F10` |
| **IND-11** fail loud on non-document fetches | §3.2 stage 2 | `F9`,`F46` |
| **IND-12** human-verifiable citations | `source_url` + in-document `locator` on every citation | `F11`,`F36` |
| **IND-13** no fabricated citation, red-team enforced | Deterministic verification (step 6) + sentinel + red-team suite modelled on the 2026 sanctions record | `F30`,`F31`,`F47` |
| **IND-14** work-product isolation as privilege-waiver control | Physical separation + construction-time binding + import-boundary test | `F21`,`F22`,`F46` |
| **IND-15** provenance trail retained | `QueryRecord` | `F34` |
| **IND-16** political context out-of-corpus, write into #3's brief now | **Discharged in §9 of this document** | §9 |
| **IND-17** superseded-order awareness, or state the limitation | Links where detectable; `known_exclusions` states the limitation where not | `F16`,`F28` |
| **IND-18** per-jurisdiction ToU/rate-limit review before the scraper runs | `Jurisdiction.terms_of_use_reviewed_at` + `crawl_policy`; **blocks flipping `LIVE_FETCH` on**, not MVP1 fixture work | `F5` |

**Residual risks accepted, with reasons:**

- **Extraction accuracy on real PDFs is the largest unknown in the plan.** Every
  guardrail above assumes the extracted metadata is right. Mitigation is the
  narrow, curated MVP1 corpus (ASM-6/ASM-7) where each case's extracted record
  is verified against the source by hand once and frozen as a fixture — a
  correctness baseline the suite can regress against. This does not generalise
  to arbitrary new dockets, and that limitation is itself a `known_exclusion`.
- **`extraction_confidence` is recorded but does not gate answers in MVP1.**
  Gating on it would require a calibrated threshold we have no data to set.
  Recorded now so `F33` can use it.
- **A6.4 retention is unanswered.** Non-blocking only because the internal
  corpus is synthetic (A6.1) — which INDUSTRY §4.3 correctly reframes as a
  *compliance control*, not a convenience. `F54` blocks any move to real work
  product.
- **A3.3 user count and A9.3 compliance obligations remain open.** Neither binds
  a local-dev MVP1; both are restated here rather than retired.

---

## 6. Sequencing

Seven phases. The ordering constraint that matters: **the schema and the test
harness come before anything that would have to be migrated or retro-tested.**

| Phase | Contents | Why here |
|---|---|---|
| **P0 · Foundation** | `F1` repo hygiene, `F2` test harness + five runners, `F3` closed-enum module, `F4` data model | Nothing else can be tested before `F2` exists, and the custom-template override means it does not exist. `F3`/`F4` carry the three non-retrofittable schema risks. |
| **P1 · Acquisition & quarantine** | `F5` adapter interface + fixture capture, `F6`/`F7`/`F8` three adapters, `F9` non-document detection, `F10` quarantine | Quarantine ships *with* the first adapter, never after. A corpus contaminated once is not cleanable by a later feature. |
| **P2 · Extraction & case assembly** | `F11` locators, `F12` doc-type + parent binding, `F13` case metadata, `F14` claims, `F15` outcome gate, `F16` supersession, `F17` non-precedent clause, `F18` rider classification | Produces the first real corpus. `F15` is a gate, not a report: it changes what is *allowed* in. |
| **P3 · Stores & the wall** | `F21` two stores, `F22` session binding + import-boundary test, `F23` synthetic work-product corpus | Deliberately *after* extraction so the wall is built around a real schema, and deliberately *before* retrieval so no retrieval code is ever written against a single-store assumption. |
| **P4 · Grounding** | `F25` frame parser, `F26` filtered retrieval, `F27` comparability, `F28` coverage, `F29` composition, `F30` verification, `F31` sentinel refusal, `F32` vintage caveats, `F34` provenance | The product's core. `F30` before `F35` — the answer must be correct before it is pretty. |
| **P5 · Surfaces** | `F35`–`F40` web, `F42`–`F43` scheduled job | Both surfaces over a working spine. |
| **P6 · Suites complete & harden** | `F44`–`F49` all five suites populated, `F49` ported regressions | All blocking (ASM-5). Suites are *scaffolded* in P0 and *populated* throughout; P6 is where they must all be green. |

Suites are written alongside their features, not batched into P6. P6 is a gate,
not a phase where testing starts.

---

## 7. Requirements the stack must satisfy

This section deliberately names **no** framework, database, vendor or model.
Stack selection is `solution-architect`'s at gate 6 (Decisions Log 2026-08-07).
These are the constraints that selection must honour, derived from the design
above — an architect who satisfies all of them has not been pre-empted, and one
who violates any of them has broken a gate-1 or gate-3 decision.

1. **Two physically separable corpus stores** under independent credentials,
   instantiable as distinct client objects with no shared singleton, no shared
   connection pool and no shared configuration object (§3.3).
2. **Metadata filtering applied at the vector-search boundary**, not as a
   post-hoc join over similarity results (§3.4, RCA-R14).
3. **Relational-quality querying over case/document/claim metadata** — joins,
   multi-field predicates, and enum constraints enforced at write time.
4. **Closed-enum validation with fail-loud on unknown values and unknown keys**
   (§4.6).
5. **Deterministic verbatim span matching** over stored chunk text with
   whitespace/hyphenation normalisation (§3.5 step 6).
6. **Document text extraction preserving page and line numbers**, plus table
   structure sufficient to attribute a schedule line. Note CPUC serves many
   documents as `.docx` as well as PDF (INDUSTRY §6.1), which extracts far more
   reliably and preserves tables — a real advantage worth exploiting.
7. **A server-side answer path.** The grounding pipeline, and specifically the
   verification step, must not be reachable or bypassable from the client.
8. **A schedulable job runner** able to run to completion headlessly, emit a
   structured run report, and fail non-zero.
9. **A browser-testable UI** for the four rendering invariants (`F48`).
10. **Structured/constrained model output** for the frame parser (`F25`) and
    the citation-tagged composition (`F29`), validated against a closed schema
    rather than parsed from free prose.
11. **Path-anchored store directories** — the `chroma_db`-style
    relative-path bug already debugged into the template source must not recur
    (Decisions Log, override cost b).
12. **Local-dev target** (A6 target environment), with no dependency on a
    third-party site's availability for any test to pass (ASM-2).

---

## 8. Ownership map (ASM-4 full roster — every agent has a named obligation)

| Agent | Owns in MVP1 |
|---|---|
| `solution-architect` | Stack (§7); two-store design; session-binding mechanism; schema-bound risks RCA-R4/R11/R13; mandatory Impact Analysis |
| `responsible-ai-architect` | `F29`–`F31` guardrails; coverage requirement `F28`; red-team suite `F47`; the public-corpus-only aggregate rule as a standing constraint on `F33` |
| `security-architect` | `F21` credential separation; `F10` quarantine path; `F22` import-boundary enforcement; ratifies/amends the wall |
| `functional-agent` | `RCA-*` register; `F27` comparability table; functional suite `F44`; devil's advocate on this plan |
| `industry-expert` | `IND-*` register; jurisdiction adapter correctness `F6`–`F8`; industry/compliance suite `F45` |
| `synthetic-data-agent` | `F23` — a **primary project asset**, not test fixtures |
| `ui-ux-designer` | `F36`–`F40` rendering; the four invariants; refusal-as-neutral |
| `functional-design-agent` | Acceptance criteria from §1 goals; the coverage statement's wording |
| `code-agent` | Implementation across all phases |
| `test-agent` | `F2` harness; suite structure; ported regressions `F49` |
| `verification-agent`, `review-agent`, `deploy-agent` | Gates 9–11 |
| `plan-agent` | This document; IND-16 discharged in §9 |

---

## 9. IND-16 discharged — the capability #3 enhancement brief, written now

IND-16 assigns `plan-agent` the obligation to write the political-context
limitation into capability #3's brief *now, while it is cheap*. Doing it here
rather than at the enhancement gate:

**Capability #3 (approval likelihood / competitive analysis) — standing
constraints for whenever it is built:**

1. **Political and affordability context is not in the corpus at all.**
   Electricity rates are a live 2026 midterm issue; commissioner elections are
   drawing unusual money and attention; legislatures are intervening in
   *procedure* (NY S.5593 would extend rate case suspension to fourteen months).
   A model fit on 2015–2022 filings will **systematically over-predict
   approval** in 2026. This limitation must be stated prominently in the
   feature's own output, not in documentation.
2. **The outcome variable is erased by settlement.** Settlements dominate, and
   black-box settlements state a revenue increase without stating ROE or
   capital structure. A large share of the "outcomes" a likelihood model would
   train on are `NOT_STATED`. Excluding them biases the sample toward litigated
   cases; imputing them fabricates the target variable.
3. **Every number is computed over the `public` corpus only** (standing
   constraint 3). A benchmark learned from work-product material is a
   disclosure channel even though no document crossed. `Source.corpus` exists
   in MVP1 specifically to make this enforceable.
4. **Aggregates must exclude rider and formula-rate proceedings** and must not
   average across the vertically-integrated / restructured boundary (RCA-R3,
   DOMAIN §3.2). An average across that split describes no real utility.
5. **Do not editorialise a settled-vs-litigated spread.** RRA finds no
   consistent directional difference; asserting one is asserting folklore
   (DOMAIN §3.6).
6. **No credible public evidence exists of a validated approval-likelihood
   model in this space** (INDUSTRY §3.2). Whatever is built should be presented
   as descriptive statistics over named comparable cases before it is presented
   as a prediction — and never as a commitment or a legal opinion (A7.1).

---

## 10. Assumptions

Numbered continuing the project's existing `ASM-*` register (ASM-1…ASM-5 are in
`PROJECT_CONTEXT.md`), so there is one register, not two. Every one of these is
a judgment the human would normally have made, taken under the recorded
full-autonomy instruction, and every one is reversible by a later decision.

**ASM-6 · Corpus depth: 12 real public cases, four per jurisdiction.**
Spanning roughly 2019–2026, each selected to exercise a named risk: at least one
black-box settlement (RCA-R5), one fully litigated case (DOMAIN §3.6), one case
with an order on rehearing (RCA-R4), one withdrawn or pending case (RCA-R13),
one rider/DCRF proceeding to be classified-and-excluded (RCA-R3), and for CPUC
one cost-of-capital proceeding separate from a GRC (the honest answer to "what
ROE did the CPUC authorize in this GRC" is *"not decided here"* — a superb
negative test). Twelve is chosen to be demonstrable end-to-end rather than
impressive; the pipeline scales, the curation effort is what does not.

**ASM-7 · Document scope per case is a defined slice, not the whole docket.**
Ingest: application/petition, utility direct testimony (cost-of-capital and
revenue-requirement witnesses), staff and intervenor direct testimony where
available, settlement, final order, order on rehearing, compliance filing /
approved tariff. **Not** ingested in MVP1: data-request responses, hearing
transcripts, briefs, ex parte notices. They remain in the `document_type` enum
and are classified-and-skipped, so adding them later is a pipeline change and
not a schema change. Rationale: a CPUC GRC alone generates tens of thousands of
pages; ingesting everything is where an MVP dies.

**ASM-8 · Structured claim extraction is limited to eight parameters** (§4.5).
Anything outside that set is answerable only as retrieved text with a verified
verbatim citation, never as a structured numeric claim. This bounds the
extraction-accuracy risk to the parameters that actually carry the money.

**ASM-9 · Outcome-completeness is an ingest gate, not a warning.** A case with
`case_status = DECIDED` and no outcome document fails ingest loudly. Rationale:
INDUSTRY §6.5.1 and the gate-1 finding that a corpus of asks without outcomes is
a machine for producing harm #1. A warning would be ignored; a gate cannot be.

**ASM-10 · Scanned documents are quarantined, not OCR'd.** `NO_EXTRACTABLE_TEXT`
is a quarantine reason and appears in the run report and in
`Coverage.known_exclusions`. Rationale: OCR error in a numeric table is a
fluent-and-wrong number, which is precisely the harm; a stated gap is safe.

**ASM-11 · Question parsing failure is a refusal, not a fallback search.** If
the frame parser cannot resolve the question into the closed schema, the system
refuses and says which part it could not resolve. A best-effort keyword search
over this corpus *is* RCA-R2.

**ASM-12 · Session roles exist; login does not.** MVP1 ships exactly one role,
`UTILITY_ANALYST`, supplied by configuration. There is no authentication, no
user table and no `IntervenorSession`. This is **not** an inheritance of
`policy-lookup-assistant`'s no-authz decision (explicitly not reused): the
*structural binding* of retrievers at session construction is built now, because
retrofitting it means re-architecting retrieval. Only the *login* is deferred.

**ASM-13 · Citation verification uses exact verbatim span matching** after
whitespace and hyphenation normalisation, plus, for numerics, a match against
the stored `Claim` record's value, unit, scope and basis. No fuzzy or semantic
matching. A near-match is a failure and produces a refusal.

**ASM-14 · No aggregates, averages, benchmarks or peer statistics in MVP1.**
This is the sharpest scope call in the plan and the one most likely to be
questioned, so the reasoning is explicit: an aggregate is the *delivery
mechanism* of harm #1 and of capability #3, and the recorded MVP boundary
excludes #3. MVP1 answers a precedent question with **named cases and their
individual figures**, plus an enumerated comparable-case list. "Peers were
authorized 9.5%" is out; "in these three comparable cases the commission
authorized 9.45%, 9.60% and 9.55% — here they are, with citations" is in. This
also removes the surface RCA-R3 needs.

**ASM-15 · Five test suites, structure built from scratch, all blocking.**
functional, industry, security, redteam, ui. The UI suite uses a browser harness
but asserts only the four rendering invariants (authority label as text not
colour; order date always present; refusal styled neutral not error; coverage
never renders as an empty list). Rationale: a broad UI suite over an MVP UI is
cost without signal; those four are the ones that carry harm.

**ASM-16 · Supersession links are populated from explicit in-document
references plus fixture curation.** Where a supersession is not detectable, the
limitation is stated in `Coverage.known_exclusions` (IND-17). We do not claim
supersession coverage we do not have.

**ASM-17 · Thresholds, all configurable, with these defaults**: corpus stale if
the last successful ingest run is older than 30 days; vintage caveat if every
supporting case's order date is more than 5 years old. Both surfaced in the UI.

**ASM-18 · Provenance is recorded and displayed for the current answer; export
is deferred** (`F41`). Recording it now is the non-reconstructable half.

**ASM-19 · `LIVE_FETCH` defaults off, including for the scheduled job.** In
MVP1 the job runs against the fixture set on its schedule, which proves the job
*works* without making the test suite depend on three third-party websites. IND-18
(per-jurisdiction terms-of-use and rate-limit review) is a **precondition for
flipping the flag on**, and is therefore not an MVP1 blocker but is a blocker for
anything beyond MVP1.

**ASM-20 · MVP1 holds no real work product.** The `work-product` corpus contains
only `synthetic-data-agent`'s output. Per INDUSTRY §4.3 this is treated as a
compliance control (attorney work-product privilege waiver), not a convenience,
and any proposal to hold real material reopens gate 1 and requires `F54`.

**ASM-21 · Backlog split taken by `plan-agent`, not offered as a choice.** The
`plan-agent` contract normally requires every feature to be an individually
approvable checkbox item with deferred items always shown. Under the recorded
full-autonomy instruction the *approval question* is suppressed, not the
*record*: `FEATURES.md` still lists **every** feature individually, including
every deferred one with its reasoning, so the human can retrospectively pull any
of them forward. Nothing has been filtered out before being written down. This
assumption exists so that the deviation from the standing contract is visible
rather than silent.
