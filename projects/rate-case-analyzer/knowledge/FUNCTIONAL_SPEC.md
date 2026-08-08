# FUNCTIONAL SPEC — rate-case-analyzer

**Gate 4 · Functional Design** · written 2026-08-07 by `functional-design-agent` ·
operating mode **full autonomy** (gate closes `assumed`, not `approved`).

This is a durable knowledge base, not a transient artifact. It accumulates across
features and enhancements, and it is what `verification-agent` audits against at
gate 9.

Binding inputs read in full before writing: [`PLAN.md`](../PLAN.md),
[`FEATURES.md`](../FEATURES.md), [`PROJECT_CONTEXT.md`](../PROJECT_CONTEXT.md),
[`INTAKE.md`](../INTAKE.md), [`DOMAIN_KB.md`](DOMAIN_KB.md),
[`INDUSTRY_KB.md`](INDUSTRY_KB.md).

---

## How to read this

- Every acceptance criterion carries a **stable unique ID**: `AC-F<feature>-<NN>`,
  where `<feature>` is the feature ID exactly as it appears in `FEATURES.md`
  (`F1`, `F27`) and `<NN>` is zero-padded two digits.
- **An ID, once issued, is never reused and never renumbered.** A deleted
  criterion is retired in place with a one-line note. A criterion whose meaning
  changes materially gets a **new** ID; the old one is retired.
- Every criterion asserts something **observable from outside the code**: what is
  on screen, what a response contains, what was persisted, what exit code was
  returned, what error was raised. Assertions about internal state ("the handler
  is registered", "the hook is called") are not criteria and are not written here.
- The stack is **not yet chosen** — `solution-architect` commits it at gate 6.
  Every criterion below is behaviour-level and names no framework, library,
  database or model vendor. Where a criterion needs a mechanism (exact
  `.startswith()`, a static import-boundary assertion) that mechanism is named
  because a gate-1 or gate-3 decision named it, not because a stack was assumed.
- **Observable-UI criteria** are marked `[UI]` and state which component must be
  visible, on which screen, in which state.
- **Structural criteria** are marked `[STRUCT]`. These assert a property of the
  shipped artifact that a test harness can observe without running the product
  (import closures, absence of an API shape, absence of a field in a schema).
  They exist because three binding constraints — the two-corpus wall, the
  no-`visibility`-column rule, and "no bare comparability score" — are only real
  if a test would fail when they break.
- **Negative-control criteria** are marked `[NEG]`. These assert that a guard's
  test *fails* when the guard is removed. A guard whose test cannot fail is not a
  guard, and this is the exact failure mode this gate was built to remove.

### Terminology used across criteria

- **"the answer path"** — a question submitted through the web surface or the
  server-side answer API, run to a returned response.
- **"the ingest run"** — one execution of the scheduled ingestion job (`F42`) to
  completion, producing one `IngestRun` record and one run report.
- **"fails loudly"** — the operation does not complete, an error naming the
  specific cause and the specific record is emitted to the run report or the
  caller, and nothing partial is written to a corpus store.
- **"quarantined"** — a `QuarantineRecord` exists with a reason from the closed
  set, and no `Document`, `Chunk` or `Claim` derived from that item exists in any
  corpus store, and its text is not retrievable by any query.

---

## 0. Completeness check — binding decisions this spec was checked against

Re-read in full before writing: `PROJECT_CONTEXT.md`'s Decisions Log (including
the gates 1–2 `ASM-1…ASM-5` block and the standing constraints), `PLAN.md` §0
and §10 (`ASM-6…ASM-21`), `INTAKE.md`. There is no prior pass of this KB, so
every binding decision below is checked for the first time.

| Binding decision | Where recorded | Where satisfied in this spec |
|---|---|---|
| Standing constraint 1 — grounding mandatory; unsupported claim **refuses** rather than paraphrases | `PROJECT_CONTEXT.md` constraints; A7.3 | `AC-F30-01`…`AC-F30-12`, `AC-F31-01`…`AC-F31-12` |
| Standing constraint 2 — ethical wall: two stores, two credential sets, retriever bound at **session construction**, **no code path** to the other corpus | `PROJECT_CONTEXT.md` constraints; IND-14 | `AC-F21-01`…`AC-F21-07`, `AC-F22-01`…`AC-F22-08` (incl. `[STRUCT]` import-boundary and `[NEG]`) |
| Standing constraint 3 — aggregate leak; every future aggregate over the **public corpus only**; `corpus` a first-class field now | `PROJECT_CONTEXT.md` constraints; PLAN §3.3 | `AC-F4-08`, `AC-F23-02`, `AC-F36-08` |
| Standing constraint 4 — **silence is not clearance**; coverage stated explicitly; never a bare empty flag list | `PROJECT_CONTEXT.md` constraints; A7.2 harm #3 | `AC-F28-01`…`AC-F28-09`, `AC-F37-01`…`AC-F37-07` |
| `sources[]` blocking (ASM-3) — a cited source is one the answer **relies on**, never what retrieval pulled | Decisions Log ASM-3; PLAN §3.5 step 6 | `AC-F30-08`, `AC-F30-09`, `AC-F30-10` |
| Authority is two-dimensional; `NOT_STATED` representable, never `null`, distinct from parse failure | Gate 1 findings; DOMAIN §2.3/§2.4 | `AC-F3-04`, `AC-F3-06`, `AC-F14-09`, `AC-F14-10`, `AC-F14-11`, `AC-F36-02` |
| Comparability is a **structured predicate** naming its mismatched dimensions, not a score | Gate 1 findings; RCA-R14; PLAN §3.7 | `AC-F27-01`…`AC-F27-13` (esp. `AC-F27-09` `[STRUCT]`) |
| Outcome-completeness is an **ingest gate**, not a warning (ASM-9) | Gate 1; INDUSTRY §6.5.1 | `AC-F15-01`…`AC-F15-07` |
| Confidential material → **quarantine-and-report**, never flag-and-index | Gate 1; IND-10; RCA-R11 | `AC-F10-01`…`AC-F10-09`, `AC-F4-05` |
| Schema-bound non-retrofittable risks: RCA-R4 supersession, RCA-R11 confidentiality, RCA-R13 case status incl. `WITHDRAWN` | Gate 1 findings | `AC-F16-*`, `AC-F10-*`, `AC-F4-06`, `AC-F13-05`, `AC-F14-08` |
| Sentinel refusal ported: exact `.startswith()` on stripped content, never regex/case-insensitive/substring, model prose **discarded** | Deliberate reuse; PLAN §3.5 step 7 | `AC-F31-01`…`AC-F31-06` |
| Closed-enum validation fail-loud on unknown **values and unknown keys** | Deliberate reuse; PLAN §4.6 | `AC-F3-02`, `AC-F3-03` |
| Badge/citation UI: authority never by colour alone; refusal styled **neutral**, never as an error | Deliberate reuse; IND-3, IND-8 | `AC-F36-03`, `AC-F38-02`, `AC-F48-01`, `AC-F48-03` |
| Two ported bug fixes (whitespace-rejecting question validator; message-content shape normalisation) | Deliberate reuse | `AC-F49-01`…`AC-F49-05` |
| Extrapolation trap (RCA-R6) carried to the Test gate as a named regression | Deliberate reuse; PLAN §5 | `AC-F27-05`, `AC-F31-04`, `AC-F47-01` |
| MVP = capabilities #1 + #2 only; **no aggregates, averages or benchmarks** (ASM-14) | Decisions Log; A8.3; ASM-14 | `AC-F27-13` (no directional settlement editorialising), and this spec issues **no criterion requiring an aggregate**; `F33` is out of scope and unspecified here |
| ASM-1 jurisdictions = PA PUC + PUCT + CPUC | Decisions Log | `F6`, `F7`, `F8` criteria |
| ASM-2 / ASM-19 live fetch behind a flag, default off, no test depends on a third-party site | Decisions Log; PLAN §10 | `AC-F5-01`, `AC-F5-02`, `AC-F2-07`, `AC-F42-02` |
| ASM-5 all five suites blocking, no advisory exceptions | Decisions Log | `AC-F44-06`, `AC-F45-07`, `AC-F46-07`, `AC-F47-07`, `AC-F48-06` |
| ASM-8 structured claim extraction limited to eight parameters | PLAN §10 | `AC-F14-01`, `AC-F14-02` |
| ASM-10 scanned documents quarantined, not OCR'd | PLAN §10 | `AC-F11-04` |
| ASM-11 parse failure is a refusal, never a fallback keyword search | PLAN §10 | `AC-F25-02`, `AC-F25-03` |
| ASM-12 session roles exist; login does not | PLAN §10 | `AC-F22-01`, `AC-F22-04`; no authentication criterion is issued |
| ASM-13 exact verbatim span matching after whitespace/hyphenation normalisation; near-match is a failure | PLAN §10 | `AC-F30-02`, `AC-F30-03`, `AC-F30-11` |
| ASM-16 supersession from explicit references + fixture curation; limitation stated where undetectable | PLAN §10 | `AC-F16-04` |
| ASM-17 thresholds: corpus stale > 30 days; vintage caveat when every supporting case > 5 years old | PLAN §10 | `AC-F32-02`, `AC-F32-04`, `AC-F32-05`, `AC-F39-03` |
| ASM-18 provenance recorded and displayed for the current answer; export deferred | PLAN §10 | `AC-F34-01`…`AC-F34-06` |
| ASM-20 MVP1 holds **no real work product**; the internal corpus is synthetic | PLAN §10 | `AC-F23-04`, `AC-F23-05` |
| Custom template — no inherited harness; the harness is our work | Decisions Log | `AC-F2-01`…`AC-F2-07` |
| Repo hygiene + path-anchored store dirs must be re-established | Decisions Log (override cost b) | `AC-F1-02`, `AC-F1-03` |
| Stack deferred to gate 6 | Decisions Log | Stated in "How to read this"; no criterion names a framework |
| IND-18 per-jurisdiction ToU review blocks flipping `LIVE_FETCH` on | INDUSTRY §6.4; PLAN §5 | `AC-F5-03` |

**No conflict found** between this spec and any recorded binding decision. Two
scope observations are raised in §12 rather than resolved here.

---

## 1. Coverage summary by feature

Counts are stated per feature at the head of each section and totalled in §11.
Features `F19`, `F20`, `F24`, `F33`, `F41`, `F50`–`F58` are `LATER` in
`FEATURES.md` and are **deliberately unspecified**. No criterion is issued for
them; issuing one would be scope creep into `plan-agent`'s lane.

---

## P0 · Foundation

## F1 — Repo hygiene & config baseline

UI-bearing: **no** (build/runtime configuration; no user-visible surface).
Criteria: 6.

### AC-F1-01
- **Given** a clean checkout with no configuration file present and no
  configuration environment values set
- **When** either surface (web or ingestion job) is started
- **Then** it exits non-zero without starting, and the emitted message names each
  missing required configuration key individually — no key is silently defaulted

### AC-F1-02
- **Given** the repository at any commit on the default branch
- **When** the tracked file list is scanned for configuration secrets and corpus
  store directories
- **Then** no tracked file contains a credential value, and no corpus store
  directory is tracked; the ignore rules covering both are present in the
  repository

### AC-F1-03
- **Given** the ingestion job is launched with a current working directory that
  is not the repository root (e.g. the filesystem root)
- **When** it opens a corpus store
- **Then** the store resolves to the same absolute path it resolves to when
  launched from the repository root, and no new empty store directory is created
  under the launch directory

### AC-F1-04
- **Given** a configuration file containing a key that is not part of the defined
  configuration schema, or a value of the wrong type for a defined key
- **When** configuration is loaded
- **Then** loading fails with an error naming the offending key; an unknown key
  is never accepted and ignored

### AC-F1-05 `[STRUCT]`
- **Given** the shipped source tree
- **When** it is scanned for direct reads of process environment values
- **Then** exactly one module performs them — the typed configuration module —
  and every other module obtains settings from that module

### AC-F1-06
- **Given** a valid, complete configuration
- **When** either surface starts
- **Then** it starts successfully and reports, at startup, the resolved absolute
  path of each corpus store and the mode of the `LIVE_FETCH` flag

---

## F2 — Test-suite harness and five suite entry points

UI-bearing: **no** for the harness itself; it hosts the browser harness that
`F48` uses. Criteria: 8.

### AC-F2-01
- **Given** a checkout with the harness installed
- **When** each of the five suite entry points is invoked by name — `functional`,
  `industry`, `security`, `redteam`, `ui`
- **Then** each runs and reports a pass/fail count, and each exits 0 only when
  every assertion in it passed

### AC-F2-02
- **Given** all five suites
- **When** the full suite is invoked as one command
- **Then** all five run, and the output reports a per-suite result line for each
  of the five by name, with the overall exit non-zero if any suite failed

### AC-F2-03
- **Given** a suite entry point that collects **zero** tests (empty suite, bad
  path, mis-named directory)
- **When** it is invoked
- **Then** it exits **non-zero** with a message stating that no tests were
  collected — an empty suite is never reported as a pass

### AC-F2-04
- **Given** a suite in which a test module raises during collection or import
- **When** the suite is invoked
- **Then** it exits non-zero, names the failing module and the error, and does
  not report the remaining tests as an overall pass

### AC-F2-05
- **Given** the harness invoked from a working directory other than the
  repository root
- **When** any suite runs
- **Then** every fixture resolves and the run produces the same result as when
  invoked from the repository root

### AC-F2-06
- **Given** the browser harness is unavailable (browser binary absent, launch
  fails)
- **When** the `ui` suite is invoked
- **Then** it exits non-zero with a message naming the browser-harness failure —
  the UI suite never reports a pass by skipping its tests

### AC-F2-07
- **Given** the machine has no outbound network access
- **When** all five suites are run
- **Then** every suite completes with the same result as with network access —
  no suite's outcome depends on the availability of a third-party website

### AC-F2-08
- **Given** a fixture corpus directory
- **When** a suite loads it
- **Then** the fixtures loaded are the ones under the repository's fixture root
  resolved by absolute path, and the suite fails loudly naming the missing path
  if the fixture root is absent

---

## F3 — Closed-enum schema module and fail-loud validator

UI-bearing: **no**. Criteria: 8.

### AC-F3-01
- **Given** a record whose every enum-valued field carries a value from its
  closed set and whose key set exactly matches the schema
- **When** it is validated at ingest
- **Then** validation succeeds and the record proceeds to the next ingest stage

### AC-F3-02
- **Given** a record carrying an enum field with a value outside its closed set
  (e.g. `document_type = "ORDER"`)
- **When** it is validated at ingest
- **Then** validation fails with an error naming the field and the offending
  value, a `QuarantineRecord` with reason `ENUM_VALIDATION_FAILURE` is written,
  and nothing derived from the record enters any corpus store

### AC-F3-03
- **Given** a record carrying a key that is not defined in the schema
  (e.g. `documentType` alongside `document_type`, or a stray `notes` key)
- **When** it is validated at ingest
- **Then** validation fails with an error naming the unknown key — an unknown key
  is never accepted as extra metadata and never passes through

### AC-F3-04
- **Given** a record in which a status-bearing field (`claim_status`,
  `case_status`, `test_year_convention`, `market_structure`, `resolution_path`,
  `confidentiality`, `author_party`, `basis`, `scope`) is `null`
- **When** it is validated
- **Then** validation fails naming the field; and the same record with that field
  set to `NOT_STATED` (or the type's equivalent explicit-absence member)
  validates successfully

### AC-F3-05
- **Given** the enum module as shipped
- **When** the `document_type` enum is enumerated
- **Then** it contains exactly the 14 values of `DOMAIN_KB.md` §2.3 with
  `authority_rank` 1–14 assigned exactly as that table assigns them
  (`FINAL_ORDER` = 1 … `BRIEF` = 14), and `claim_status` contains exactly the six
  values of §2.4

### AC-F3-06
- **Given** the enum module as shipped
- **When** every status-bearing enum is enumerated
- **Then** each one contains a `NOT_STATED` member, and no status-bearing field
  in the schema is declared nullable

### AC-F3-07
- **Given** an enum value differing from a legal member only by case or
  surrounding whitespace (`"final_order"`, `" FINAL_ORDER "`)
- **When** it is validated
- **Then** validation fails — the validator never coerces, trims or
  case-normalises an enum value into a legal member

### AC-F3-08
- **Given** a batch ingest of many records in which exactly one record fails
  validation
- **When** the batch is processed
- **Then** the failing record is quarantined and named in the run report, and the
  run's status is not `SUCCEEDED` — a validation failure is never absorbed into a
  silent success

---

## F4 — Corpus data model

UI-bearing: **no**. Criteria: 9.

### AC-F4-01
- **Given** a fully-populated instance of each of `Case`, `Document`, `Chunk`,
  `Claim`, `QuarantineRecord`, `IngestRun` and `QueryRecord` carrying every field
  listed in `PLAN.md` §4
- **When** each is written and read back
- **Then** every field round-trips with its value and type unchanged, and no
  field listed in `PLAN.md` §4 is absent from the persisted record

### AC-F4-02
- **Given** a `Chunk` produced from a `Document` belonging to a `Case`
- **When** the chunk is read back
- **Then** its denormalised `case_id`, `jurisdiction_code`, `document_type`,
  `authority_rank`, `order_date`, `market_structure`, `test_year_convention`,
  `case_type`, `case_status`, `superseded` and `corpus` each equal the
  corresponding value on the parent `Document` / `Case`

### AC-F4-03
- **Given** a `Document` A recorded as superseded by `Document` B
- **When** both are read back
- **Then** A's `superseded_by_doc_id` is B and B's `supersedes_doc_id` is A; a
  one-sided link fails validation naming the inconsistency

### AC-F4-04 `[STRUCT]`
- **Given** the shipped schema definitions for every persisted record type
- **When** their field names are enumerated
- **Then** no field named `visibility` (or any equivalent access-filter field
  over a shared store) exists on any record type

### AC-F4-05
- **Given** a `Document` whose `confidentiality` is `PROTECTED`
- **When** a write to the `Document` store is attempted
- **Then** the write fails naming the confidentiality value, and the item is
  representable only as a `QuarantineRecord` — there is no persisted state in
  which a protected document sits in a corpus store wearing a flag

### AC-F4-06
- **Given** a case that was withdrawn mid-proceeding with a full docket of
  testimony and no order
- **When** it is stored
- **Then** its `case_status` is `WITHDRAWN`, distinct from `DISMISSED` and from
  `PENDING`, and `has_outcome_document` is `false`

### AC-F4-07
- **Given** a `Claim`
- **When** it is read back
- **Then** `parameter`, `value`, `unit`, `basis`, `scope`, `customer_class`,
  `claim_status`, `locator` and `verbatim_quote` are each present, and the
  `verbatim_quote` string is found in the text of the `Chunk` its `chunk_id`
  references

### AC-F4-08
- **Given** any of `Case`, `Document`, `Chunk`, `Claim`
- **When** it is written without an explicit `corpus` value
- **Then** the write fails — `corpus` is required on every record and has no
  default

### AC-F4-09
- **Given** a `Case` record
- **When** it is read back
- **Then** `topic_tags[]` is present (possibly empty) and accepts an open
  vocabulary string, so adding a topic tag later requires no schema change

---

## P1 · Acquisition & quarantine

## F5 — Docket-adapter interface, fixture capture, `LIVE_FETCH` flag

UI-bearing: **no**. Criteria: 7.

### AC-F5-01
- **Given** the `LIVE_FETCH` flag is unset in configuration
- **When** any adapter's discover or fetch operation runs
- **Then** it is served from the captured fixture set, no outbound network
  request is made, and an attempted outbound request raises an error naming the
  `LIVE_FETCH` flag rather than proceeding

### AC-F5-02
- **Given** `LIVE_FETCH` is off
- **When** an ingest run completes
- **Then** the resulting `IngestRun` record has `mode = FIXTURE`, and the run
  report states the mode on its first line

### AC-F5-03
- **Given** `LIVE_FETCH` is on and a jurisdiction in the run's scope has no
  `terms_of_use_reviewed_at` value and no `crawl_policy`
- **When** the run is started
- **Then** the run refuses to start, exits non-zero, and names the jurisdiction
  and the missing field — the terms-of-use review is a precondition, not a
  warning (IND-18)

### AC-F5-04
- **Given** the fixture-capture tool is pointed at a document URL with
  `LIVE_FETCH` on
- **When** it captures
- **Then** it records the request URL, the response bytes, the response
  content-type and the retrieval timestamp; and a subsequent fixture-mode fetch
  of that URL returns a body byte-identical to the captured bytes

### AC-F5-05
- **Given** an adapter's discover step over a fixture index page
- **When** it returns index entries
- **Then** each entry carries `title`, native document id, `source_url`,
  `filed_date` and any index-level confidentiality marking; an entry missing a
  required field is **not** returned with a default — it is omitted and recorded
  as a named failure on the run report

### AC-F5-06
- **Given** fixture mode and a requested URL for which no fixture exists
- **When** the fetch is attempted
- **Then** it fails loudly naming the missing URL and the expected fixture path;
  it never returns an empty body, an empty result list or a silent skip

### AC-F5-07 `[STRUCT]`
- **Given** the three shipped adapters
- **When** their public surface is enumerated
- **Then** each implements the same declared adapter interface (discover,
  fetch, docket-number validation), so a fourth jurisdiction is added by
  implementing that interface and not by editing the ingestion pipeline

---

## F6 — PA PUC adapter

UI-bearing: **no**. Criteria: 6.

### AC-F6-01
- **Given** a PA PUC document id (e.g. `1874654`)
- **When** the adapter constructs the document URL
- **Then** the URL is exactly `https://www.puc.pa.gov/pcdocs/1874654.pdf`

### AC-F6-02
- **Given** a PA PUC docket number in the commission's own format
  (e.g. `R-2025-3057164`)
- **When** the adapter validates it
- **Then** it is accepted and the docket landing URL is constructed from it; and
  a string not matching the commission's docket-number format (e.g. `2025-3057164`
  with no `R-` prefix, or a PUCT-style bare numeric control number) is **rejected**
  with an error naming the expected format

### AC-F6-03
- **Given** a captured PA PUC document-search result page containing N document
  entries
- **When** discover runs against it
- **Then** exactly N index entries are returned, each carrying title, document id,
  source URL and filed date

### AC-F6-04
- **Given** a captured PA PUC search result page containing **zero** entries
- **When** discover runs against it
- **Then** it returns an empty list **and** records a `search_returned_zero`
  entry on the run report naming the docket searched — a zero-result search is
  never indistinguishable from a search that did not run

### AC-F6-05
- **Given** a captured page whose structure no longer matches what the adapter
  parses (renamed container, missing results table)
- **When** discover runs against it
- **Then** it fails loudly naming the adapter and the element it could not find;
  it never returns a partial or empty entry list as if the page were empty

### AC-F6-06
- **Given** a PA PUC case ingested from fixtures
- **When** the stored `Case` is read back
- **Then** its `jurisdiction_code` is `PA_PUC` and its `docket_number` is the
  commission's own string, pasteable into the PA PUC docket system unmodified

---

## F7 — PUCT adapter

UI-bearing: **no**. Criteria: 6.

### AC-F7-01
- **Given** a PUCT control number, item number and document id (e.g. `58359`, `3`,
  `1519645`)
- **When** the adapter constructs the document URL
- **Then** the URL is exactly
  `https://interchange.puc.texas.gov/Documents/58359_3_1519645.PDF`, with the
  uppercase `.PDF` extension preserved

### AC-F7-02
- **Given** a PUCT docket search with jurisdiction, document-type and page
  parameters
- **When** the adapter constructs the search URL
- **Then** the parameters appear as URL query parameters and paging is expressed
  as a page parameter, so a second page is retrievable by URL alone

### AC-F7-03
- **Given** a captured PUCT search result page containing N entries
- **When** discover runs against it
- **Then** exactly N index entries are returned with title, control/item/doc ids,
  source URL and filed date

### AC-F7-04
- **Given** a captured PUCT search result page containing **zero** entries
- **When** discover runs
- **Then** it returns an empty list and records a `search_returned_zero` entry on
  the run report naming the docket searched

### AC-F7-05
- **Given** a PUCT control number that is not a valid numeric control number
- **When** the adapter validates it
- **Then** it is rejected naming the expected format, and no URL is constructed

### AC-F7-06
- **Given** a PUCT DCRF or TCOS rider proceeding in the fixture set
- **When** it is ingested
- **Then** the resulting `Case` carries `jurisdiction_code = PUCT` and a
  `case_type` of `RIDER_TRACKER` or `FORMULA_RATE_ANNUAL` (never `BASE_RATE`),
  per `F18`

---

## F8 — CPUC adapter

UI-bearing: **no**. Criteria: 7.

### AC-F8-01
- **Given** a CPUC accession-style document identifier
- **When** the adapter constructs the document URL
- **Then** the URL matches the observed accession form
  `https://docs.cpuc.ca.gov/PublishedDocs/Published/<g>/<m>/<k>/<accession>.PDF`
  with the identifier segments placed exactly as supplied

### AC-F8-02
- **Given** a CPUC document available as both `.PDF` and `.docx`
- **When** the adapter selects a representation to fetch
- **Then** it fetches the `.docx`, and the stored `Document` records which
  representation was used

### AC-F8-03
- **Given** a CPUC document available **only** as `.PDF`
- **When** the adapter fetches
- **Then** it fetches the `.PDF` successfully — absence of a `.docx` is not an
  error

### AC-F8-04
- **Given** a CPUC proceeding whose docket contains more documents than the
  configured per-proceeding document cap
- **When** ingestion is scoped to that proceeding
- **Then** it ingests only the documents in the configured document slice
  (`ASM-7`), and the run report names the cap and the count of documents in the
  docket that were not ingested — it never attempts a wholesale docket ingest

### AC-F8-05
- **Given** a CPUC advanced-search results page in the fixture set containing N
  entries
- **When** discover runs
- **Then** exactly N index entries are returned; and a zero-entry page returns an
  empty list plus a `search_returned_zero` report entry

### AC-F8-06
- **Given** a CPUC proceeding number in the commission's own format (e.g. an
  `A.` application or `R.` rulemaking number)
- **When** the adapter validates it
- **Then** it is accepted; a string in another commission's format is rejected
  naming the expected format

### AC-F8-07
- **Given** a CPUC General Rate Case in the fixture set that does **not** decide
  cost of capital, and a separate CPUC cost-of-capital proceeding
- **When** both are ingested
- **Then** they are two distinct `Case` records with distinct `case_type` values
  (`BASE_RATE` and `COST_OF_CAPITAL`), and no `ROE` `Claim` with
  `claim_status = AUTHORIZED` is attached to the GRC case

---

## F9 — Non-document fetch detection

UI-bearing: **no**. Criteria: 7.

### AC-F9-01
- **Given** a fetch that returns a login or authentication page body
- **When** the sanity gate runs
- **Then** the item is quarantined with reason `ACCESS_DENIED`, the
  `QuarantineRecord`'s `evidence` contains the response signature that triggered
  it, and no `Document` is stored

### AC-F9-02
- **Given** a fetch that returns an access-denied body (HTTP 403, or a 200 body
  whose content states access is denied)
- **When** the sanity gate runs
- **Then** the item is quarantined with reason `ACCESS_DENIED` and no `Document`
  is stored

### AC-F9-03
- **Given** a fetch that returns an HTML error page where the index entry
  promised a PDF
- **When** the sanity gate runs
- **Then** the item is quarantined with reason `NON_DOCUMENT_BODY`, the evidence
  records both the promised and the received content type, and no `Document` is
  stored

### AC-F9-04
- **Given** a fetch that returns a zero-length body
- **When** the sanity gate runs
- **Then** the item is quarantined with reason `NON_DOCUMENT_BODY` and no
  `Document` is stored

### AC-F9-05
- **Given** a fetch whose returned content type is inconsistent with the index
  entry's stated type (index says PDF, body is `text/html`)
- **When** the sanity gate runs
- **Then** the item is quarantined with reason `NON_DOCUMENT_BODY` naming both
  types

### AC-F9-06
- **Given** a fetch that returns a well-formed document body matching the index
  entry's content type
- **When** the sanity gate runs
- **Then** it passes the gate and proceeds to confidentiality classification —
  the gate does not produce false positives on valid documents

### AC-F9-07
- **Given** any of `AC-F9-01`…`AC-F9-05` fired during an ingest run
- **When** the run completes
- **Then** the quarantined item appears in the run report under its reason with
  its `source_url`, and the run's `status` is not `SUCCEEDED`

---

## F10 — Confidentiality classifier and quarantine-and-report

UI-bearing: **no** (its output is rendered by `F43`). Criteria: 9.

### AC-F10-01
- **Given** an index entry carrying an index-level confidentiality marking
- **When** the classifier runs
- **Then** the item is quarantined with reason `PROTECTED_MARKING` **before** any
  text extraction or store write, and no `Document`, `Chunk` or `Claim` derived
  from it exists in any corpus store

### AC-F10-02
- **Given** a document whose index metadata is clean but whose **first page**
  bears one of the markings `CONFIDENTIAL`, `HIGHLY SENSITIVE` or `SUBJECT TO
  PROTECTIVE ORDER`
- **When** the first-page marking scan runs
- **Then** the item is quarantined with reason `PROTECTED_MARKING` and the
  `QuarantineRecord`'s `evidence` contains the verbatim marking text found

### AC-F10-03
- **Given** a detectable redacted/unredacted pair of the same document in the
  index
- **When** classification runs
- **Then** the **public redacted** version is ingested, the unredacted version is
  quarantined with reason `PROTECTED_MARKING`, and both are never present in the
  corpus

### AC-F10-04
- **Given** a redacted/unredacted pair that a de-duplication step would collapse
- **When** de-duplication runs
- **Then** the surviving record is the redacted one — de-duplication never
  resolves to the unredacted version

### AC-F10-05
- **Given** a quarantined protected document containing a distinctive phrase
- **When** a query whose text is that exact phrase is submitted through the answer
  path
- **Then** no chunk from that document is retrieved and no citation to it can be
  produced — the item is not merely flagged, it is absent

### AC-F10-06
- **Given** an ingest run in which no item was quarantined for confidentiality
- **When** the run report is produced
- **Then** it contains an explicit `PROTECTED_MARKING: 0` line — a zero count is
  stated, never rendered as an omitted section

### AC-F10-07
- **Given** a final order whose **body text on page 5** discusses confidential
  treatment (e.g. "the parties' confidential workpapers were reviewed") but which
  bears no first-page marking and no index marking
- **When** classification runs
- **Then** the document is classified `PUBLIC` and ingested — the marking scan is
  scoped to first-page markings and index metadata, and does not quarantine on
  incidental body prose

### AC-F10-08
- **Given** a document whose confidentiality cannot be determined from either the
  index entry or a first-page scan
- **When** classification runs
- **Then** its `confidentiality` is recorded as `UNKNOWN` and it is quarantined
  with reason `PROTECTED_MARKING`, with evidence stating that the determination
  could not be made — an undetermined item is never ingested as public

### AC-F10-09
- **Given** the first-adapter ingest path
- **When** the ordering of ingest stages is observed on any item
- **Then** confidentiality classification completes before the first write to any
  corpus store — there is no window in which an unclassified document is in a
  store

---

## P2 · Extraction & case assembly

## F11 — Text extraction with in-document locators

UI-bearing: **no** (its output is rendered by `F36`). Criteria: 8.

### AC-F11-01
- **Given** any document that passes the sanity and confidentiality gates
- **When** it is extracted into chunks
- **Then** every chunk carries a non-null `locator.page`; a chunk that cannot be
  assigned a page number causes the document's ingest to fail loudly naming the
  document and the chunk offset

### AC-F11-02
- **Given** line-numbered pre-filed testimony
- **When** it is extracted
- **Then** each chunk carries `locator.line_start` and `locator.line_end`, and
  those values correspond to the line numbers printed in the source document for
  the chunk's first and last lines

### AC-F11-03
- **Given** an exhibit or schedule document
- **When** it is extracted
- **Then** each chunk carries `locator.schedule_no` taken from the schedule's own
  identifier; and for a final order containing numbered findings of fact, chunks
  covering a numbered finding carry `locator.finding_no`

### AC-F11-04
- **Given** a scanned document from which no text can be extracted
- **When** extraction runs
- **Then** it is quarantined with reason `NO_EXTRACTABLE_TEXT`, no OCR is
  attempted, the item appears in the run report, and the standing
  `known_exclusions` list surfaced in `Coverage` states that scanned documents
  are quarantined rather than processed

### AC-F11-05
- **Given** a document from which text is extracted for some pages and no text at
  all for others
- **When** extraction runs
- **Then** the document is quarantined with reason `NO_EXTRACTABLE_TEXT` naming
  the pages that yielded nothing — a partially-extracted document is never
  ingested as if complete

### AC-F11-06
- **Given** a passage that spans a page break
- **When** it is chunked
- **Then** the chunk's `locator.page` is the page on which the chunk begins, and
  the locator records the final page the chunk covers, so a human opening the
  cited page finds the quoted text

### AC-F11-07
- **Given** a `.docx` schedule containing a table whose row label and numeric
  value are in adjacent cells
- **When** it is extracted
- **Then** the row label and its value appear in the same chunk, in reading
  order, so the number is never stored detached from the line item it belongs to

### AC-F11-08
- **Given** any stored `Chunk`
- **When** its locator is rendered as a citation string
- **Then** the string identifies at minimum a page, and where available a line
  range, a schedule number or a finding-of-fact number — a citation string of
  the form "in this document" is not producible

---

## F12 — `document_type` classification and exhibit parent-binding

UI-bearing: **no**. Criteria: 8.

### AC-F12-01
- **Given** each of the fixture documents covering all 14 `document_type` values
- **When** classification runs
- **Then** each is assigned the correct value from the closed enum and its
  `authority_rank` equals the rank in `DOMAIN_KB.md` §2.3

### AC-F12-02
- **Given** a document the classifier cannot assign to any of the 14 values
- **When** classification runs
- **Then** ingest of that document fails loudly, a `QuarantineRecord` with reason
  `ENUM_VALIDATION_FAILURE` is written, and no chunk from it is stored — it is
  never assigned a default or catch-all type

### AC-F12-03
- **Given** an `EXHIBIT_SCHEDULE` whose parent filing is present in the same
  docket ingest
- **When** parent binding runs
- **Then** the exhibit's `parent_doc_id` resolves to that filing, and the
  exhibit's `case_id` and the authority it carries for outcome claims are those
  of the parent filing, not of the exhibit standing alone

### AC-F12-04
- **Given** an `EXHIBIT_SCHEDULE` with **no** resolvable parent filing
- **When** parent binding runs
- **Then** ingest of that exhibit fails loudly, a `QuarantineRecord` with reason
  `UNRESOLVED_PARENT` is written, and no chunk or claim from it is retrievable —
  an unattributable number is un-retrievable, not ambiguously attributed

### AC-F12-05
- **Given** an `EXHIBIT_SCHEDULE` whose parent filing was itself quarantined
- **When** parent binding runs
- **Then** the exhibit is also quarantined with reason `UNRESOLVED_PARENT` — an
  orphan cannot inherit from an absent parent

### AC-F12-06
- **Given** documents classified as `DATA_REQUEST_RESPONSE` or
  `HEARING_TRANSCRIPT`
- **When** the ingest run processes them
- **Then** they are classified and **skipped** (no chunks stored), counted in the
  run report as classified-and-skipped by type, and the standing
  `known_exclusions` list states that data-request responses and hearing
  transcripts are not ingested in this release

### AC-F12-07
- **Given** any stored `Chunk`
- **When** it is read back
- **Then** it carries a non-null `case_id`, `document_type` and `authority_rank`
  — no retrievable chunk exists without case identity and document authority

### AC-F12-08
- **Given** a `BRIEF` in the fixture set
- **When** it is ingested and later retrieved
- **Then** its `authority_rank` is 14, and no `Claim` with
  `claim_status = AUTHORIZED` is attached to it

---

## F13 — Case-metadata extraction

UI-bearing: **no**. Criteria: 8.

### AC-F13-01
- **Given** a case whose documents explicitly state a fully-projected future test
  year
- **When** case metadata is extracted
- **Then** `test_year_convention` is `FPFTY`, distinct from `FORECAST`, and
  `test_year_start` and `test_year_end` are populated from the stated period

### AC-F13-02
- **Given** a case filed in a jurisdiction whose
  `Jurisdiction.default_market_structure` is `RESTRUCTURED_WIRES_ONLY`, but whose
  own documents establish a vertically-integrated posture
- **When** case metadata is extracted
- **Then** the stored `Case.market_structure` is `VERTICALLY_INTEGRATED` — the
  per-case extracted value always wins, and the jurisdiction default is never
  written onto a case

### AC-F13-03
- **Given** a case whose documents do not state the test-year convention
- **When** case metadata is extracted
- **Then** `test_year_convention` is `NOT_STATED` — never the jurisdiction
  default, never `null`, never absent

### AC-F13-04
- **Given** a case resolved by a settlement joined by some but not all parties
- **When** case metadata is extracted
- **Then** `resolution_path` is `SETTLED_PARTIAL`, distinct from `SETTLED_FULL`
  and from `LITIGATED`

### AC-F13-05
- **Given** a case the utility withdrew mid-proceeding
- **When** case metadata is extracted
- **Then** `case_status` is `WITHDRAWN`, `has_outcome_document` is `false`, and
  `decided_date` is absent-as-not-applicable rather than backfilled from the
  filing date

### AC-F13-06
- **Given** a rider or formula-rate proceeding
- **When** case metadata is extracted
- **Then** `case_type` is `RIDER_TRACKER` or `FORMULA_RATE_ANNUAL`, never
  `BASE_RATE`

### AC-F13-07
- **Given** a case in which the commission imposed a hypothetical capital
  structure rather than accepting the utility's actual one
- **When** case metadata and claims are extracted
- **Then** the `EQUITY_RATIO` claim records which structure it describes, so a
  later comparison on the capital-structure dimension is made against a stated,
  not assumed, basis

### AC-F13-08
- **Given** any successfully ingested `Case`
- **When** it is read back
- **Then** `jurisdiction_code`, `docket_number`, `utility_name`, `case_type`,
  `case_status`, `filed_date`, `test_year_convention`, `market_structure`,
  `resolution_path` and `docket_url` are each populated with a value from their
  closed sets or `NOT_STATED`; none is `null`

---

## F14 — Structured claim extraction

UI-bearing: **no** (rendered by `F36`). Criteria: 13.

### AC-F14-01
- **Given** a document stating figures for each of the eight MVP1 parameters
- **When** claim extraction runs
- **Then** eight `Claim` rows are produced, one per parameter, each with
  `parameter` drawn from the fixed eight-value set

### AC-F14-02
- **Given** a document stating a figure for a parameter outside the eight
  (e.g. a depreciation rate)
- **When** claim extraction runs
- **Then** **no** `Claim` row is created for it; the passage remains retrievable
  text answerable only with a verified verbatim citation

### AC-F14-03
- **Given** a rate-base schedule whose adjacent lines state gross plant, net
  plant and rate base
- **When** claim extraction runs
- **Then** three distinct `Claim` rows are produced with parameters
  `GROSS_PLANT`, `NET_PLANT` and `RATE_BASE` and three distinct values; no value
  is derived from another

### AC-F14-04
- **Given** a filing stating both a total revenue requirement and the requested
  increase
- **When** claim extraction runs
- **Then** two `Claim` rows are produced,
  `REVENUE_REQUIREMENT_TOTAL` and `REVENUE_REQUIREMENT_INCREASE`, with their
  stated values; neither is computed from the other, and a document stating only
  one produces only one row

### AC-F14-05
- **Given** an order stating "the Commission reduces the requested return on
  equity by 25 basis points"
- **When** claim extraction runs
- **Then** the extracted delta carries `unit = BASIS_POINTS` with value 25 — it is
  never stored as 25 `PERCENT`

### AC-F14-06
- **Given** a figure stated at the return level and a figure stated at the
  revenue level in the same document
- **When** claim extraction runs
- **Then** each carries the correct `basis` (`AFTERTAX` / `PRETAX`), and a figure
  whose basis the document does not state carries `basis = NOT_STATED` rather
  than an inferred value

### AC-F14-07
- **Given** a schedule stating both a total-company rate base and a retail
  jurisdictional rate base
- **When** claim extraction runs
- **Then** two `Claim` rows are produced with `scope = TOTAL_COMPANY` and
  `scope = RETAIL_JURISDICTIONAL`; and a class-specific increase carries
  `scope = CLASS_SPECIFIC` with `customer_class` populated

### AC-F14-08
- **Given** an attempt to write a `Claim` with `claim_status = AUTHORIZED` whose
  `doc_id` resolves to a document of type `UTILITY_DIRECT_TESTIMONY`
- **When** the write is attempted
- **Then** it is rejected with an error naming the `AUTHORIZED` invariant, and no
  row is written — the invariant is enforced at write time, not at query time

### AC-F14-09
- **Given** an attempt to write a `Claim` with `claim_status = AUTHORIZED` whose
  parent case's `case_status` is `PENDING` or `WITHDRAWN`
- **When** the write is attempted
- **Then** it is rejected naming the invariant and the case status, and no row is
  written

### AC-F14-10
- **Given** a commission-approved black-box settlement that states a revenue
  increase and deliberately does **not** state an ROE
- **When** claim extraction runs
- **Then** a `Claim` row exists for `parameter = ROE` with
  `claim_status = NOT_STATED`, no numeric value, and a `verbatim_quote` from the
  settlement; the row is present, not absent, and its status is not `null`

### AC-F14-11
- **Given** a document in which the ROE figure is present but the extractor
  fails to parse it
- **When** claim extraction runs
- **Then** **no** `Claim` row is created for that figure, a parse-failure entry
  naming the document and parameter appears on the `IngestRun` failure list, and
  querying the corpus can distinguish this case from `AC-F14-10`: the black-box
  case yields a `NOT_STATED` row, the parse failure yields no row plus a run
  report entry

### AC-F14-12
- **Given** a multi-year plan granting staged increases
- **When** claim extraction runs
- **Then** each year's figure is a separate `Claim` with its own `rate_year` and
  `effective_date`; no single row conflates two rate years

### AC-F14-13
- **Given** any stored `Claim`
- **When** it is read back
- **Then** its `verbatim_quote` is found, character-for-character after
  whitespace and hyphenation normalisation, in the text of the `Chunk` its
  `chunk_id` references

---

## F15 — Outcome-completeness gate

UI-bearing: **no**. Criteria: 7.

### AC-F15-01
- **Given** a case whose `case_status` is `DECIDED` and whose ingested document
  set contains no `FINAL_ORDER`, `ORDER_ON_REHEARING`, `APPROVED_SETTLEMENT` or
  `COMPLIANCE_FILING`
- **When** the outcome-completeness gate runs
- **Then** ingest of that case fails loudly, a `QuarantineRecord` with reason
  `MISSING_OUTCOME_DOCUMENT` is written, and no `Case`, `Document`, `Chunk` or
  `Claim` for it exists in any corpus store

### AC-F15-02
- **Given** a `DECIDED` case whose document set contains a `FINAL_ORDER`
- **When** the gate runs
- **Then** the case ingests successfully and `has_outcome_document` is `true`

### AC-F15-03
- **Given** a `SETTLED_APPROVED` case whose document set contains an
  `APPROVED_SETTLEMENT` but no `FINAL_ORDER`
- **When** the gate runs
- **Then** the case ingests successfully and `has_outcome_document` is `true`

### AC-F15-04
- **Given** a `DECIDED` case whose only outcome document is a
  `COMPLIANCE_FILING`, or whose only outcome document is an
  `ORDER_ON_REHEARING`
- **When** the gate runs
- **Then** the case ingests successfully — any one of the four qualifying types
  satisfies the gate

### AC-F15-05
- **Given** a `PENDING` or `WITHDRAWN` case with no outcome document
- **When** the gate runs
- **Then** the case ingests successfully with `has_outcome_document = false`, and
  a subsequent attempt to attach an `AUTHORIZED` claim to it is rejected
  (`AC-F14-09`)

### AC-F15-06
- **Given** an ingest run in which the gate fired for at least one case
- **When** the run completes
- **Then** the run's `status` is `FAILED`, the process exits non-zero, and the
  run report names each gated case by docket number — the gate is never emitted
  as a warning line in an otherwise-successful run

### AC-F15-07
- **Given** a corpus assembled from a run in which the gate fired
- **When** the answer path is queried about a gated case's docket number
- **Then** no chunk or claim from it is retrievable — a case of asks with no
  outcome never reaches the store

---

## F16 — Supersession linking

UI-bearing: **no** (rendered by `F36`/`F40`). Criteria: 6.

### AC-F16-01
- **Given** a case containing a `FINAL_ORDER` authorizing an ROE and a later
  `ORDER_ON_REHEARING` revising that ROE downward, both ingested with their
  supersession link
- **When** the answer path is asked for the authorized ROE in that case
- **Then** the answer states the **amended** figure from the order on rehearing,
  and the superseded original is either absent from `sources[]` or present and
  explicitly labelled as superseded

### AC-F16-02
- **Given** a document marked superseded
- **When** its chunks are read back
- **Then** each carries the denormalised `superseded = true` flag, so the flag is
  applicable at the retrieval boundary and not only after a join

### AC-F16-03
- **Given** a retrieval whose candidate set contains a superseded chunk
- **When** the comparability and coverage steps run
- **Then** the superseded case appears in `Coverage.excluded` with the dimension
  named as supersession and the superseding document identified, or in
  `sources[]` labelled superseded — it is never silently dropped and never
  presented as current without the label

### AC-F16-04
- **Given** any answer or refusal produced by the system
- **When** its `Coverage.known_exclusions` is read
- **Then** it contains a statement of the supersession-detection limitation:
  supersession links are populated from explicit in-document references and
  curated fixtures, and undetected supersessions may exist

### AC-F16-05
- **Given** an attempted supersession link whose target document belongs to a
  different `case_id`
- **When** the link is written
- **Then** the write fails loudly naming both documents and their cases

### AC-F16-06
- **Given** a case with no superseded documents
- **When** its chunks are read back
- **Then** every chunk carries `superseded = false` explicitly — the field is
  never absent or null

---

## F17 — Non-precedent settlement clause extraction

UI-bearing: **no** (rendered by `F40`). Criteria: 5.

### AC-F17-01
- **Given** an approved settlement containing express non-precedent language
  ("this Stipulation shall not be cited as precedent…")
- **When** the case is ingested
- **Then** `Case.non_precedent_clause.present` is `true`,
  `.quote` holds the clause verbatim, and `.locator` identifies its page and
  line or paragraph

### AC-F17-02
- **Given** a settlement with no such language
- **When** the case is ingested
- **Then** `Case.non_precedent_clause.present` is `false` with an empty quote —
  the field is present and explicit, never null or absent

### AC-F17-03
- **Given** a settlement whose non-precedent clause is formatted as boilerplate
  in a signature block or a numbered "General Provisions" section
- **When** extraction runs
- **Then** the clause is still extracted — boilerplate placement is not a reason
  to strip it

### AC-F17-04
- **Given** an answer that relies on a case whose `non_precedent_clause.present`
  is `true`
- **When** the response is produced
- **Then** the comparability result for that case includes a `CAVEAT`-severity
  entry naming the non-precedent clause, and the clause quote is carried on the
  response for rendering

### AC-F17-05
- **Given** a litigated case with a `FINAL_ORDER` and no settlement
- **When** it is ingested
- **Then** `non_precedent_clause.present` is `false` and no caveat is attached to
  answers relying on it

---

## F18 — Rider / formula-rate / non-base-rate classification

UI-bearing: **no** (surfaced through `F37`/`F40`). Criteria: 6.

### AC-F18-01
- **Given** a DCRF, TCOS, fuel, storm-recovery or energy-efficiency rider
  proceeding
- **When** it is ingested
- **Then** its `Case.case_type` is `RIDER_TRACKER` (or `FORMULA_RATE_ANNUAL` for
  an annual formula-rate filing), assigned at ingest time and stored

### AC-F18-02
- **Given** a rider case in the corpus
- **When** its chunks are read back
- **Then** each carries the denormalised `case_type`, so the exclusion is
  applicable at the retrieval boundary

### AC-F18-03
- **Given** a base-rate precedent question and a corpus containing both base-rate
  and rider cases in the named jurisdiction
- **When** the answer path runs
- **Then** no rider case appears in `sources[]`, and each excluded rider case
  appears in `Coverage.excluded` with `dimension = case_type` and its
  `case_value` named

### AC-F18-04
- **Given** a question that explicitly asks about a rider or formula-rate
  proceeding
- **When** the answer path runs
- **Then** rider cases are eligible for inclusion and base-rate cases are the
  ones excluded on the `case_type` dimension — the exclusion is directional to
  the frame, not a blanket ban

### AC-F18-05
- **Given** any answer or refusal
- **When** its `Coverage.known_exclusions` is read
- **Then** it states that rider and formula-rate proceedings are excluded from
  base-rate treatment

### AC-F18-06
- **Given** a comprehensive base-rate case that also contains a rider
  reconciliation as a component
- **When** it is classified
- **Then** its `case_type` is `BASE_RATE` and the rider component does not
  reclassify the case — classification is at the proceeding level and the
  proceeding's own type governs

---

## P3 · Corpus stores & the ethical wall

## F21 — Two physically separate corpus stores under independent credentials

UI-bearing: **no**. Criteria: 7.

### AC-F21-01
- **Given** configuration supplying two distinct credential sets under two
  distinct configuration keys
- **When** the application starts
- **Then** two store clients are instantiated, one per credential set, and each
  reports a distinct resolved store location

### AC-F21-02
- **Given** the public store's credentials
- **When** they are used to open the work-product store
- **Then** the operation fails with an authentication or authorisation error —
  the credentials are not interchangeable

### AC-F21-03
- **Given** a record written to the public store
- **When** the work-product store is queried for it by id and by its distinctive
  text
- **Then** it is not found; and the symmetric case holds for a work-product
  record queried against the public store

### AC-F21-04 `[STRUCT]`
- **Given** the shipped store modules
- **When** their construction paths are inspected
- **Then** the two stores share no singleton client object, no connection pool
  and no configuration object; each reads only its own configuration keys

### AC-F21-05
- **Given** the work-product store's credentials are revoked or its store is made
  unavailable
- **When** a public-corpus query runs
- **Then** it completes normally — the two stores fail independently

### AC-F21-06 `[STRUCT]`
- **Given** the shipped store schemas
- **When** their field names are enumerated
- **Then** neither contains a `visibility` field or any equivalent access-filter
  column; separation is by store, never by filter

### AC-F21-07 `[STRUCT]`
- **Given** the shipped source
- **When** it is searched for a store or retriever factory whose parameter is a
  corpus name expressed as a string
- **Then** no such function exists — a corpus is never selected by a string
  argument

---

## F22 — Session-bound retriever construction and static import-boundary test

UI-bearing: **no**. Criteria: 8.

### AC-F22-01
- **Given** the shipped session type for the MVP1 role `UTILITY_ANALYST`
- **When** it is constructed
- **Then** it requires both a public retriever and a work-product retriever as
  constructor arguments, held as two distinct attributes of two distinct types;
  construction with either omitted fails

### AC-F22-02 `[STRUCT]`
- **Given** the shipped session types
- **When** their public methods are enumerated
- **Then** none accepts a corpus name and returns "the retriever for corpus X" —
  retrievers are reached only as distinctly-named, distinctly-typed attributes

### AC-F22-03 `[STRUCT]`
- **Given** the module implementing the public answer path
- **When** its **transitive** import closure is computed
- **Then** the module implementing the work-product store is not in it

### AC-F22-04
- **Given** a session constructed with a public retriever **only** (the shape a
  future intervenor session would take)
- **When** any code attempts to reach the work-product corpus through it
- **Then** the attempt fails as a missing attribute or missing type — it does not
  return an empty result set, and it does not return a filtered view

### AC-F22-05 `[NEG]`
- **Given** a fixture variant of the public answer-path module that adds an
  import of the work-product store module
- **When** the import-boundary assertion of `AC-F22-03` runs against it
- **Then** the assertion **fails** — demonstrating that the boundary test is
  capable of detecting the breach it exists to detect

### AC-F22-06 `[NEG]`
- **Given** a fixture variant of the session type that exposes a
  corpus-name-to-retriever lookup
- **When** the assertion of `AC-F22-02` runs against it
- **Then** the assertion **fails**

### AC-F22-07
- **Given** a public-corpus answer produced end to end
- **When** every entry in `sources[]` is inspected
- **Then** each carries `corpus = PUBLIC`; no entry with `corpus = WORK_PRODUCT`
  can appear in a public-corpus answer

### AC-F22-08
- **Given** the session role is supplied by configuration (`ASM-12`, no login)
- **When** a role value outside the closed role set is configured
- **Then** startup fails naming the invalid role — an unknown role never
  defaults to a session with more retrievers than it should have

---

## F23 — Synthetic internal-history (`work-product`) corpus

UI-bearing: **no** (its records are rendered by `F36`). Criteria: 7.

### AC-F23-01
- **Given** the synthetic corpus asset as shipped
- **When** it is loaded
- **Then** it loads into the work-product store only, and the work-product store
  reports a document count greater than zero

### AC-F23-02
- **Given** the loaded synthetic corpus
- **When** every `Case`, `Document`, `Chunk` and `Claim` in it is read back
- **Then** each carries `corpus = WORK_PRODUCT`

### AC-F23-03
- **Given** the distinctive marker text embedded in each synthetic document
- **When** the public store is searched for it
- **Then** no match is found — no synthetic record has leaked into the public
  corpus

### AC-F23-04
- **Given** a synthetic case
- **When** its `docket_number` is read
- **Then** it belongs to a reserved synthetic namespace that no real PA PUC,
  PUCT or CPUC docket number can match, so a synthetic docket can never be
  mistaken for a real one in a citation

### AC-F23-05
- **Given** the work-product store as shipped in MVP1
- **When** its contents are enumerated
- **Then** every record is synthetic — no record originates from real non-public
  utility work product (`ASM-20`)

### AC-F23-06
- **Given** the synthetic corpus asset is missing or fails to load
- **When** a session is constructed
- **Then** session construction fails loudly naming the corpus — it never
  succeeds with an empty work-product retriever, because an empty retriever is
  indistinguishable from a wall failure

### AC-F23-07
- **Given** the synthetic corpus
- **When** it is examined against the risks it exists to exercise
- **Then** it contains at least one black-box settled case with a `NOT_STATED`
  ROE claim, at least one case with an order on rehearing, and at least one case
  whose test-year convention differs from every public-corpus case in the same
  jurisdiction

---

## P4 · Retrieval & grounding

## F25 — Query-frame parser

UI-bearing: **no** (its refusal is rendered by `F38`). Criteria: 8.

### AC-F25-01
- **Given** the question "what ROE has the PA PUC authorized in fully-projected
  future-test-year distribution cases since 2023?"
- **When** the frame parser runs
- **Then** it returns a frame with `jurisdictions = [PA_PUC]`,
  `parameter = ROE`, `claim_status_sought = AUTHORIZED`,
  `test_year_convention = FPFTY`, `market_structure = RESTRUCTURED_WIRES_ONLY`
  and a date window opening in 2023

### AC-F25-02
- **Given** a question the parser cannot resolve into the closed frame schema
- **When** the answer path runs
- **Then** the response is a refusal whose `QueryRecord.outcome` is
  `REFUSED_PARSE_FAILED`, whose text names which part of the question could not
  be resolved, and which carries a `Coverage` object

### AC-F25-03
- **Given** a parse failure
- **When** the `QueryRecord` for that query is read
- **Then** `retrieved_chunk_ids` is empty — no retrieval of any kind was
  attempted, and in particular no keyword or best-effort search was run

### AC-F25-04
- **Given** a question that does not specify a dimension (e.g. names no customer
  class)
- **When** the frame parser runs
- **Then** that dimension is set to `UNSPECIFIED` explicitly in the frame; it is
  never absent, never `null`, and never filled with a guessed value

### AC-F25-05
- **Given** a question naming a jurisdiction outside the closed set (e.g. "the
  Georgia PSC")
- **When** the frame parser runs
- **Then** frame validation fails and the answer path refuses, naming the
  jurisdiction as outside the corpus — it does not map it to the nearest
  in-corpus jurisdiction

### AC-F25-06
- **Given** an empty or whitespace-only question
- **When** it is submitted
- **Then** it is rejected by input validation before the parser runs, with a
  message stating a question is required, and no `QueryRecord` retrieval occurs

### AC-F25-07
- **Given** a question naming two jurisdictions
- **When** the frame parser runs
- **Then** `jurisdictions` contains both, and the frame is valid — multi-
  jurisdiction questions parse rather than fail

### AC-F25-08
- **Given** a question that explicitly names a test-year convention
- **When** the frame parser runs
- **Then** the frame records that the convention was **named by the question**,
  distinct from a convention inferred or left `UNSPECIFIED` — this flag is what
  `AC-F27-05` escalates on

---

## F26 — Metadata-filtered retrieval

UI-bearing: **no**. Criteria: 7.

### AC-F26-01
- **Given** a frame naming `jurisdiction = PA_PUC`, and a corpus in which a PUCT
  chunk and a CPUC chunk each score higher on embedding similarity than every PA
  PUC chunk
- **When** retrieval runs
- **Then** the returned candidate set contains **zero** chunks from PUCT or CPUC

### AC-F26-02 `[STRUCT]`
- **Given** a frame and its resulting metadata-filtered candidate set
- **When** ranking completes
- **Then** the ranked result set is a subset of the metadata-filtered set —
  similarity reorders within the set and never adds a chunk to it

### AC-F26-03
- **Given** a frame whose filters match no chunk at all
- **When** retrieval runs
- **Then** it returns an empty candidate set, `Coverage.candidates_considered`
  is 0, and the coverage record names the filter values that produced the empty
  set; the system does not relax any filter and retry

### AC-F26-04
- **Given** a frame with a date window
- **When** retrieval runs
- **Then** a case whose order date falls exactly on the window's opening date and
  a case falling exactly on its closing date are both included; a case one day
  outside either end is excluded

### AC-F26-05
- **Given** a public-corpus session query
- **When** retrieval runs
- **Then** no chunk with `corpus = WORK_PRODUCT` appears in the candidate set

### AC-F26-06
- **Given** a frame naming a specific utility, state and year, and a corpus
  containing near-identically-worded cost-of-capital testimony from a different
  utility, state and year
- **When** retrieval runs
- **Then** no chunk from the different utility/state/year appears in the
  candidate set

### AC-F26-07
- **Given** a frame whose `claim_status_sought` is `AUTHORIZED`
- **When** retrieval runs
- **Then** the candidate set is constrained to chunks whose denormalised
  `document_type` can carry an authorized outcome (`FINAL_ORDER`,
  `ORDER_ON_REHEARING`, `APPROVED_SETTLEMENT`, `COMPLIANCE_FILING`); testimony
  chunks are not candidates for the outcome claim

---

## F27 — Comparability predicate

UI-bearing: **no** (rendered by `F40`). Criteria: 13.

### AC-F27-01
- **Given** a query frame and a candidate case
- **When** the comparability predicate runs
- **Then** it returns an object with a `verdict` of `COMPARABLE`,
  `COMPARABLE_WITH_CAVEATS` or `NOT_COMPARABLE`, a `matched[]` list of dimension
  names, a `mismatched[]` list of `{dimension, query_value, case_value,
  severity}` entries, and an `unknown[]` list of `{dimension, reason}` entries

### AC-F27-02
- **Given** a frame whose `market_structure` is `RESTRUCTURED_WIRES_ONLY` and a
  candidate case whose `market_structure` is `VERTICALLY_INTEGRATED`
- **When** the predicate runs
- **Then** the verdict is `NOT_COMPARABLE`, `mismatched[]` contains an entry with
  `dimension = market_structure`, both values, and `severity = BLOCKING`

### AC-F27-03
- **Given** a base-rate frame and a candidate case whose `case_type` is
  `RIDER_TRACKER`
- **When** the predicate runs
- **Then** the verdict is `NOT_COMPARABLE` with `dimension = case_type` at
  `severity = BLOCKING`

### AC-F27-04
- **Given** a frame asking what a named commission **authorized**, and a
  candidate case from a different jurisdiction
- **When** the predicate runs
- **Then** the verdict is `NOT_COMPARABLE` with `dimension = jurisdiction` at
  `severity = BLOCKING`

### AC-F27-05
- **Given** a frame in which the question **named** a test-year convention
  (`AC-F25-08`), and a candidate case with a different convention
- **When** the predicate runs
- **Then** `severity` for `dimension = test_year_convention` is `BLOCKING`; and
  given the same mismatch where the question did **not** name a convention, the
  severity is `CAVEAT`

### AC-F27-06
- **Given** a candidate case whose order date is outside the configured vintage
  window
- **When** the predicate runs
- **Then** `mismatched[]` contains `dimension = vintage` at `severity = CAVEAT`
  with the case's order date as `case_value`

### AC-F27-07
- **Given** candidate cases differing from the frame on `resolution_path`, on
  `capital_structure` / equity ratio band, and on the presence of a
  `non_precedent_clause`
- **When** the predicate runs
- **Then** each appears in `mismatched[]` at `severity = CAVEAT`, each naming its
  dimension

### AC-F27-08
- **Given** a candidate case differing from the frame only on `utility_scale`
- **When** the predicate runs
- **Then** the verdict is `COMPARABLE_WITH_CAVEATS` and the entry carries
  `severity = INFO`

### AC-F27-09 `[STRUCT]`
- **Given** the comparability result object as shipped
- **When** its fields are enumerated
- **Then** it exposes no scalar similarity, distance or comparability score; and
  for any result whose verdict is not `COMPARABLE`, at least one of
  `mismatched[]` or `unknown[]` is non-empty — a non-comparable verdict without a
  named dimension is not representable

### AC-F27-10
- **Given** a candidate case whose `market_structure` is `NOT_STATED` in the
  corpus
- **When** the predicate runs
- **Then** that dimension appears in `unknown[]` with a reason stating the corpus
  does not record it; it does **not** appear in `matched[]`, and the case is not
  treated as matching on it

### AC-F27-11
- **Given** a candidate case matching the frame on every assessed dimension
- **When** the predicate runs
- **Then** the verdict is `COMPARABLE`, `matched[]` names every assessed
  dimension, and `mismatched[]` is empty

### AC-F27-12
- **Given** a set of N candidate cases put through the predicate
- **When** the response is produced
- **Then** `len(Coverage.included) + len(Coverage.excluded) +
  len(Coverage.unassessable) == N`, and every case in `excluded` carries the
  named dimension that excluded it — no candidate is dropped without appearing
  somewhere

### AC-F27-13
- **Given** a corpus containing both settled and fully litigated cases
- **When** any answer or caveat text is produced
- **Then** it contains no directional assertion about settled-versus-litigated
  outcomes (no claim that settlements come in lower or higher) — the mismatch is
  named as a dimension without an asserted spread

---

## F28 — `Coverage` object on every path

UI-bearing: **no** (rendered by `F37`). Criteria: 9.

### AC-F28-01
- **Given** a question that produces a successful grounded answer
- **When** the response is returned
- **Then** it carries a `Coverage` object with `candidates_considered`,
  `included[]`, `excluded[]`, `unassessable[]`, `jurisdictions[]`, `date_range`,
  `corpus_as_of`, `corpus_stale` and `known_exclusions[]` all present

### AC-F28-02
- **Given** a question refused for insufficient evidence
- **When** the response is returned
- **Then** it carries a fully-populated `Coverage` object

### AC-F28-03
- **Given** a question refused because citation verification failed
- **When** the response is returned
- **Then** it carries a fully-populated `Coverage` object

### AC-F28-04
- **Given** a question refused because the frame could not be parsed
- **When** the response is returned
- **Then** it carries a `Coverage` object whose `candidates_considered` is 0 and
  whose text states that no retrieval was performed because the question could
  not be resolved

### AC-F28-05
- **Given** two questions — one over a corpus region with 40 candidates of which
  none is comparable, and one whose filters match 0 candidates
- **When** both responses are produced
- **Then** their `Coverage` objects differ observably:
  `candidates_considered = 40` with 40 named exclusions versus
  `candidates_considered = 0` with the filter values named. "Found nothing" and
  "looked at nothing" are never the same response

### AC-F28-06
- **Given** any response
- **When** `Coverage.known_exclusions` is read
- **Then** it is non-empty and contains at minimum: rider and formula-rate
  proceedings excluded from base-rate treatment; data-request responses and
  hearing transcripts not ingested; scanned documents quarantined rather than
  processed; supersession detection limited to explicit references

### AC-F28-07
- **Given** any response
- **When** `Coverage.corpus_as_of` is read
- **Then** it equals the `finished_at` of the most recent `IngestRun` with
  `status = SUCCEEDED`, and `corpus_stale` is `true` exactly when that timestamp
  is older than the configured staleness threshold

### AC-F28-08
- **Given** a response with excluded and unassessable cases
- **When** each entry is read
- **Then** every `excluded` entry carries a non-empty `case_id`, `dimension` and
  `reason`, and every `unassessable` entry a non-empty `case_id` and `reason` —
  no entry has a blank or placeholder reason

### AC-F28-09
- **Given** any response
- **When** `Coverage.jurisdictions` and `Coverage.date_range` are read
- **Then** they state the jurisdictions and date span actually examined for this
  query, not the corpus's whole span

---

## F29 — Grounded answer composition

UI-bearing: **no**. Criteria: 6.

### AC-F29-01
- **Given** a non-empty `included` evidence set
- **When** composition produces an answer
- **Then** the output validates against the closed composition schema, and every
  factual assertion in it carries an evidence-id citation tag and a verbatim
  quoted span drawn from the cited evidence

### AC-F29-02
- **Given** a composition output containing a factual assertion with no citation
  tag
- **When** the output is validated
- **Then** validation fails and the answer path falls through to refusal — the
  uncited sentence is never silently removed and the rest served

### AC-F29-03
- **Given** an evidence set in which some candidate cases were placed in
  `excluded`
- **When** composition runs
- **Then** no evidence id from an excluded case is supplied to composition, and
  none appears in the composed output

### AC-F29-04
- **Given** a numeric assertion in the composed answer
- **When** it is inspected
- **Then** it carries the identifier of the stored `Claim` it draws on, together
  with the asserted `parameter`, `unit`, `scope`, `basis` and `claim_status`, so
  `F30` can check each mechanically

### AC-F29-05
- **Given** an empty `included` set
- **When** the answer path runs
- **Then** composition is not invoked at all and the sufficiency check produces
  the refusal — no prose is generated over an empty evidence set

### AC-F29-06
- **Given** a composed answer that mentions a figure a party **requested**
  alongside the figure the commission authorized
- **When** the output is inspected
- **Then** the requested figure carries `claim_status = REQUESTED` on its
  citation tag and is described in the text as requested, never as an outcome

---

## F30 — Deterministic citation verification

UI-bearing: **no** (its refusal is rendered by `F38`). Criteria: 12.

### AC-F30-01
- **Given** a composed answer citing an evidence id that was **not** among the
  ids supplied to composition
- **When** verification runs
- **Then** the entire answer is discarded, the response is a refusal, and
  `QueryRecord.outcome` is `REFUSED_VERIFICATION_FAILED`

### AC-F30-02
- **Given** a composed answer whose quoted span differs from the stored chunk
  text only in whitespace runs or a soft hyphen at a line break
- **When** verification runs
- **Then** the citation **passes** — normalisation covers whitespace and
  hyphenation

### AC-F30-03
- **Given** a composed answer whose quoted span differs from the stored chunk
  text by one substituted, added or removed word
- **When** verification runs
- **Then** the citation fails and the entire answer is discarded — a near-match
  is a failure, and no fuzzy or semantic matching is applied

### AC-F30-04
- **Given** a composed answer asserting `document_type = FINAL_ORDER` for an
  evidence id whose stored record is `UTILITY_DIRECT_TESTIMONY`
- **When** verification runs
- **Then** the citation fails and the entire answer is discarded

### AC-F30-05
- **Given** a composed answer asserting `claim_status = AUTHORIZED` for a claim
  whose stored record is `REQUESTED`
- **When** verification runs
- **Then** the citation fails and the entire answer is discarded

### AC-F30-06
- **Given** a composed answer asserting a numeric value that differs from the
  stored `Claim`'s value
- **When** verification runs
- **Then** the citation fails and the entire answer is discarded

### AC-F30-07
- **Given** a composed answer asserting the correct number in the wrong unit,
  scope or basis (e.g. 950 `BASIS_POINTS` where the stored claim is 9.50
  `PERCENT`; `TOTAL_COMPANY` where the stored claim is
  `RETAIL_JURISDICTIONAL`; `PRETAX` where the stored claim is `AFTERTAX`)
- **When** verification runs
- **Then** each case fails and the entire answer is discarded — numeric
  equivalence across units does not satisfy the check

### AC-F30-08
- **Given** a retrieval that returned 10 chunks and a verified answer that cites
  2 of them
- **When** the response's `sources[]` is inspected
- **Then** it contains exactly those 2 — `sources[]` is constructed from the
  verified citations only and never from the retrieval result set

### AC-F30-09 `[STRUCT]`
- **Given** the shipped answer path
- **When** the construction of `sources[]` is traced
- **Then** its only input is the verified-citation list; the retrieval result set
  is not an input to it

### AC-F30-10
- **Given** a response
- **When** every entry in `sources[]` is checked against the answer text
- **Then** each is cited by at least one assertion in the answer — a source the
  answer does not rely on cannot be present

### AC-F30-11
- **Given** a composed answer of five assertions in which four verify and one
  fails any check
- **When** verification runs
- **Then** the **entire** answer is discarded and a refusal is returned — the
  failing assertion is never removed and the remaining four served

### AC-F30-12
- **Given** a composed answer in which every citation passes every check
- **When** verification runs
- **Then** the answer is returned with its `sources[]`, `Coverage` and
  `QueryRecord.outcome = ANSWERED`

---

## F31 — Sentinel refusal

UI-bearing: **no** (rendered by `F38`). Criteria: 12.

### AC-F31-01
- **Given** a model output whose stripped content begins with the exact literal
  `INSUFFICIENT_EVIDENCE`
- **When** the sentinel check runs
- **Then** the refusal path is taken

### AC-F31-02
- **Given** a model output whose stripped content begins with
  `insufficient_evidence` or `Insufficient_Evidence`
- **When** the sentinel check runs
- **Then** the sentinel does **not** match — the comparison is case-sensitive and
  is not a regex

### AC-F31-03
- **Given** a model output containing `INSUFFICIENT_EVIDENCE` in the middle of a
  sentence rather than at the start of stripped content
- **When** the sentinel check runs
- **Then** the sentinel does **not** match — the comparison is a prefix test on
  stripped content, never a substring search

### AC-F31-04
- **Given** a refusal, and a model output that also contained several sentences
  of its own hedged prose after the sentinel token
- **When** the response is produced
- **Then** none of the model's own sentences appears anywhere in the returned
  response — the prose is discarded entirely and replaced by a product-controlled
  string

### AC-F31-05
- **Given** a question asking for the authorized ROE in a jurisdiction ×
  test-year-convention combination the corpus does not contain
- **When** the refusal is produced
- **Then** the refusal text names the specific missing dimension and its value —
  e.g. "the corpus contains no fully-projected-future-test-year case from the PA
  PUC" — and does not consist of a generic statement of insufficient information

### AC-F31-06
- **Given** any refusal
- **When** its text is inspected
- **Then** it contains at least one named comparability or frame dimension **and**
  the value of that dimension that is missing; a refusal whose text names no
  dimension fails this criterion

### AC-F31-07
- **Given** a refusal produced after candidate cases were examined
- **When** the response is produced
- **Then** it lists the cases that **were** examined by docket number and
  jurisdiction, alongside the coverage statement

### AC-F31-08
- **Given** a refusal produced when no candidates were examined at all
- **When** the response is produced
- **Then** it states that no candidates were examined and names the filters that
  produced the empty set — distinguishable from `AC-F31-07`

### AC-F31-09
- **Given** the three refusal causes — insufficient evidence, verification
  failure, parse failure
- **When** each fires
- **Then** the `QueryRecord.outcome` is `REFUSED_INSUFFICIENT`,
  `REFUSED_VERIFICATION_FAILED` and `REFUSED_PARSE_FAILED` respectively, so the
  cause is recoverable from the record rather than only the fact of refusal

### AC-F31-10
- **Given** a refusal of any of the three kinds
- **When** the response is produced
- **Then** it carries the `Coverage` object (`F28`) and the corpus as-of date

### AC-F31-11
- **Given** a refusal
- **When** `sources[]` is inspected
- **Then** it is empty, and no citation, docket number or quoted span appears
  anywhere in the refusal text other than in the list of examined cases required
  by `AC-F31-07`

### AC-F31-12 `[STRUCT]`
- **Given** the shipped sentinel check
- **When** its implementation is inspected
- **Then** it performs an exact prefix comparison against a single named literal
  constant on stripped content; no regular expression, case-folding or substring
  search is present in the sentinel path

---

## F32 — Vintage and staleness caveats

UI-bearing: **no** for the computation; its rendering is `AC-F36-04` and
`AC-F39-03`. Criteria: 6.

### AC-F32-01
- **Given** any answer with at least one source
- **When** each source is inspected
- **Then** each carries an order date, or where the document is not an order, its
  filing date explicitly labelled as a filing date

### AC-F32-02
- **Given** an answer whose every supporting case has an order date more than the
  configured vintage threshold (default 5 years) in the past
- **When** the response is produced
- **Then** it carries a vintage caveat naming the oldest and newest supporting
  order dates and stating that all supporting precedent predates the threshold

### AC-F32-03
- **Given** an answer whose supporting cases include at least one inside the
  vintage window
- **When** the response is produced
- **Then** no all-cases-stale caveat is emitted, and every source still renders
  its date

### AC-F32-04
- **Given** an answer whose oldest supporting order date is exactly the vintage
  threshold old to the day, and a second answer whose oldest is one day older
- **When** both are produced
- **Then** the first emits no all-cases-stale caveat and the second does — the
  boundary is at the configured threshold, inclusive

### AC-F32-05
- **Given** the vintage threshold reconfigured from 5 years to 2 years
- **When** the same question is asked again
- **Then** the caveat behaviour changes accordingly — the threshold is
  configuration, not a constant in code

### AC-F32-06
- **Given** an answer relying on a case decided before the 2018 federal tax-rate
  change and a question about a revenue-requirement figure
- **When** the response is produced
- **Then** the vintage caveat is present and names the order date, so the user
  can see the figure predates the change

---

## F34 — Provenance trail

UI-bearing: **yes** (displayed for the current answer). Criteria: 7.

### AC-F34-01
- **Given** any query submitted through the answer path
- **When** the response is returned
- **Then** exactly one `QueryRecord` has been written for it

### AC-F34-02
- **Given** a query that was refused for any of the three reasons
- **When** the `QueryRecord` is read
- **Then** it exists and its `outcome` is the corresponding `REFUSED_*` value —
  refusals are recorded as fully as answers

### AC-F34-03
- **Given** a completed `QueryRecord`
- **When** it is read
- **Then** `query_id`, `asked_at`, `session_role`, `question_text`,
  `query_frame`, `retrieved_chunk_ids[]`, `comparability_results`,
  `verified_sources[]`, `outcome`, `corpus_as_of` and `model_identifier` are all
  populated

### AC-F34-04
- **Given** a refusal
- **When** its `QueryRecord.refusal_gap` is read
- **Then** it names the missing dimension and value that the refusal text names;
  and for an `ANSWERED` outcome the field is explicitly not-applicable rather
  than an empty string

### AC-F34-05
- **Given** a `QueryRecord` for an answered query
- **When** `verified_sources[]` is compared to the response's `sources[]`
- **Then** they are identical — the trail records what the answer relied on, not
  what retrieval returned

### AC-F34-06
- **Given** the provenance store is unavailable so the `QueryRecord` cannot be
  written
- **When** a query is submitted
- **Then** the response is not returned as a normal answer; the user is shown a
  system-error state naming the provenance failure (see assumption `FDA-4`)

### AC-F34-07 `[UI]`
- **Given** an answered query displayed on the Answer screen
- **When** the provenance region is inspected
- **Then** a **provenance panel** is visible on the Answer screen showing the
  query id, the timestamp, the model identifier, the corpus as-of date and the
  count of retrieved chunks for **this** answer

---

## P5 · Surfaces

Screens named in this section: the **Ask screen** (question entry) and the
**Answer screen** (response). Where they are one page in the final design is
`ui-ux-designer`'s call at gate 5; these criteria name the *state*, not the
layout.

## F35 — Web surface: question → answer

UI-bearing: **yes**. Criteria: 9.

### AC-F35-01 `[UI]`
- **Given** a `UTILITY_ANALYST` session and a first visit to the web surface
- **When** the Ask screen loads
- **Then** a **question input** and a **submit control** are visible on the Ask
  screen, and the submit control is operable

### AC-F35-02 `[UI]`
- **Given** the Ask screen with an empty or whitespace-only question
- **When** submit is activated
- **Then** an **inline validation message** is visible next to the question
  input stating a question is required, and no request is sent to the answer path

### AC-F35-03 `[UI]`
- **Given** a submitted question whose answer is still being produced
- **When** the Answer screen is in flight
- **Then** an **in-progress indicator** is visible, and no empty answer region,
  empty citation region or empty coverage region is visible in its place

### AC-F35-04 `[UI]`
- **Given** a question that produces a verified grounded answer
- **When** the Answer screen renders
- **Then** the **answer text**, at least one **citation card** (`F36`), the
  **coverage panel** (`F37`), the **freshness banner** (`F39`) and the
  **provenance panel** (`F34`) are all visible on the Answer screen

### AC-F35-05 `[UI]`
- **Given** a question that is refused for any of the three reasons
- **When** the Answer screen renders
- **Then** the **refusal panel** (`F38`) and the **coverage panel** (`F37`) are
  both visible on the Answer screen, and no citation card is visible

### AC-F35-06 `[UI]`
- **Given** the answer path returns a system error (store unavailable, model
  call failed)
- **When** the Answer screen renders
- **Then** a **system-error panel** is visible stating that the system failed,
  and it is a distinct component from the refusal panel

### AC-F35-07 `[STRUCT]`
- **Given** the shipped surfaces
- **When** the routes reachable from the browser client are enumerated
- **Then** no route returns composed answer prose that has not passed citation
  verification — the verification step is not bypassable from the client

### AC-F35-08 `[STRUCT]`
- **Given** the shipped web surface
- **When** its write operations against the corpus stores are enumerated
- **Then** there are none — the web surface never writes to a corpus store

### AC-F35-09 `[UI]`
- **Given** an answered query on the Answer screen
- **When** the user submits a second question
- **Then** the Answer screen renders the second answer's own citation cards,
  coverage panel and provenance panel; no element of the first answer remains
  visible

---

## F36 — Citation card

UI-bearing: **yes**. Criteria: 10.

### AC-F36-01 `[UI]`
- **Given** an answered query with N verified sources
- **When** the Answer screen renders
- **Then** exactly N **citation cards** are visible, and each shows all eight
  citation parts as text: commission name, docket number, document identity
  (title, and order number where an order), `document_type` label,
  `claim_status` label, order or filing date, in-document locator, and source URL

### AC-F36-02 `[UI]`
- **Given** an answer relying on a black-box settlement where the parameter's
  `claim_status` is `NOT_STATED`
- **When** the citation card renders
- **Then** the `claim_status` region shows explicit words to the effect of "not
  stated in the settlement" — it is never blank, never a dash alone, and never
  omitted

### AC-F36-03 `[UI]`
- **Given** a citation card for a `FINAL_ORDER` and a citation card for
  `UTILITY_DIRECT_TESTIMONY` on the same Answer screen
- **When** the rendered text of each card is read with all colour information
  removed
- **Then** each card's `document_type` label is present as text and the two are
  distinguishable — authority is never conveyed by colour alone

### AC-F36-04 `[UI]`
- **Given** any citation card
- **When** it renders
- **Then** a date is visible on it; for an order the order date labelled as such,
  for a filing the filing date labelled as such — no citation card renders
  without a date

### AC-F36-05 `[UI]`
- **Given** a citation to line-numbered testimony, a citation to an exhibit
  schedule, and a citation to a numbered finding in an order
- **When** each card renders
- **Then** each shows its in-document locator in a form a human can act on —
  page and line range, schedule number, or finding-of-fact number respectively

### AC-F36-06 `[UI]`
- **Given** a citation card
- **When** the source URL region renders
- **Then** the URL is visible as text and is an activatable link to the stored
  `source_url` — a card never shows a link with no visible URL

### AC-F36-07 `[UI]`
- **Given** a citation to a document that has been superseded
- **When** the card renders
- **Then** a **superseded label** is visible on that card naming the superseding
  document

### AC-F36-08 `[UI]`
- **Given** a citation to a record whose `corpus` is `WORK_PRODUCT`
- **When** the card renders
- **Then** a corpus label reading work-product (and, in MVP1, identifying the
  record as synthetic) is visible on that card as text

### AC-F36-09 `[UI]`
- **Given** a response with zero verified sources
- **When** the Answer screen renders
- **Then** no empty citation-card region is visible — the refusal panel occupies
  that state instead

### AC-F36-10 `[UI]`
- **Given** an answer that mentions a figure a party requested alongside the
  authorized figure
- **When** the cards render
- **Then** the card for the requested figure shows `claim_status` as requested,
  visually adjacent to the assertion it supports, so asked is never rendered as
  granted

---

## F37 — Coverage panel

UI-bearing: **yes**. Criteria: 7.

### AC-F37-01 `[UI]`
- **Given** any response — answered or refused for any of the three reasons
- **When** the Answer screen renders
- **Then** the **coverage panel** is visible on the Answer screen

### AC-F37-02 `[UI]`
- **Given** a response whose coverage reports 40 candidates, 3 included, 30
  excluded and 7 unassessable
- **When** the coverage panel renders
- **Then** it shows the counts as text — checked 40, included 3, excluded 30,
  could not assess 7 — and each excluded and unassessable entry is listed with
  its case identity and its stated reason

### AC-F37-03 `[UI]`
- **Given** a response whose coverage reports 0 candidates considered
- **When** the coverage panel renders
- **Then** it shows "checked 0" together with the filter values that produced the
  empty set, and its rendering is visibly different from the panel of
  `AC-F37-04`

### AC-F37-04 `[UI]`
- **Given** a response whose coverage reports 40 candidates considered and 0
  included
- **When** the coverage panel renders
- **Then** it shows "checked 40, included 0" with the 40 exclusion reasons —
  visibly different from `AC-F37-03`

### AC-F37-05 `[UI]`
- **Given** a response whose `excluded[]` is empty
- **When** the coverage panel renders
- **Then** the excluded region reads "none excluded" as text — the panel never
  renders a bare empty list or an empty region

### AC-F37-06 `[UI]`
- **Given** any response
- **When** the coverage panel renders
- **Then** the corpus as-of date and every entry in `known_exclusions` are
  visible on it, and the known-exclusions region is never empty

### AC-F37-07 `[UI]`
- **Given** a refusal
- **When** the Answer screen renders
- **Then** the coverage panel is visible **alongside** the refusal panel, showing
  what was examined before the refusal fired

---

## F38 — Refusal rendering

UI-bearing: **yes**. Criteria: 7.

### AC-F38-01 `[UI]`
- **Given** a response whose outcome is any `REFUSED_*` value
- **When** the Answer screen renders
- **Then** the **refusal panel** is visible on the Answer screen

### AC-F38-02 `[UI]`
- **Given** a rendered refusal panel
- **When** its markup and text are inspected
- **Then** it carries no error or alert role, no danger/error status semantics,
  and its text contains none of the words "error", "failed" or "problem" — a
  refusal is correct behaviour and is never styled as a failure

### AC-F38-03 `[UI]`
- **Given** a refusal for an uncovered jurisdiction × test-year combination
- **When** the refusal panel renders
- **Then** the visible text names the missing dimension and its value

### AC-F38-04 `[UI]`
- **Given** a refusal after candidates were examined
- **When** the refusal panel renders
- **Then** the cases that were examined are visible on it, each with its docket
  number and jurisdiction

### AC-F38-05 `[UI]`
- **Given** a refusal whose underlying model output contained hedged prose after
  the sentinel token
- **When** the refusal panel renders
- **Then** none of that prose is visible anywhere on the Answer screen

### AC-F38-06 `[UI]`
- **Given** a refusal panel and a system-error panel rendered for two different
  queries
- **When** both are inspected
- **Then** they are distinct components with distinct visible text, so a user can
  tell a correct refusal from a system failure

### AC-F38-07 `[UI]`
- **Given** a refusal caused by a parse failure
- **When** the refusal panel renders
- **Then** its visible text names the part of the question that could not be
  resolved, and does not suggest that the corpus lacks evidence

---

## F39 — Corpus freshness / as-of banner

UI-bearing: **yes**. Criteria: 6.

### AC-F39-01 `[UI]`
- **Given** at least one `IngestRun` with `status = SUCCEEDED`
- **When** the Ask screen or the Answer screen loads
- **Then** the **freshness banner** is visible showing "corpus as of" followed by
  the `finished_at` of the most recent successful run

### AC-F39-02 `[UI]`
- **Given** a most-recent successful run older than the configured staleness
  threshold (default 30 days)
- **When** the freshness banner renders
- **Then** it additionally shows a stale notice naming the age in days

### AC-F39-03 `[UI]`
- **Given** a most-recent successful run inside the threshold
- **When** the freshness banner renders
- **Then** it shows the date with no stale notice

### AC-F39-04 `[UI]`
- **Given** a corpus in which **no** `IngestRun` has ever succeeded
- **When** the Ask screen loads
- **Then** the freshness banner is visible stating that no ingest run has
  succeeded, and a submitted question is refused naming that as the gap (see
  assumption `FDA-5`) — the surface never answers over a corpus it cannot date

### AC-F39-05 `[UI]`
- **Given** the most recent run has `status = FAILED` or `PARTIAL` and an earlier
  run succeeded
- **When** the freshness banner renders
- **Then** it shows the earlier successful run's date — a failed or partial run
  never advances the as-of date

### AC-F39-06 `[UI]`
- **Given** a rendered answer or refusal
- **When** the corpus as-of date on the coverage panel and the date on the
  freshness banner are compared
- **Then** they are the same date

---

## F40 — Comparability caveat rendering

UI-bearing: **yes**. Criteria: 6.

### AC-F40-01 `[UI]`
- **Given** an answer relying on at least one case with a `CAVEAT`- or
  `INFO`-severity mismatch
- **When** the Answer screen renders
- **Then** a **comparability caveat region** is visible naming each mismatched
  dimension together with the question's value and the case's value

### AC-F40-02 `[UI]`
- **Given** a rendered comparability caveat
- **When** its text is inspected
- **Then** it contains the dimension name (e.g. "test year convention",
  "market structure", "vintage", "capital structure") — a caveat consisting only
  of a generic statement that results may not be comparable fails this criterion

### AC-F40-03 `[UI]`
- **Given** an answer relying on a case whose `non_precedent_clause.present` is
  `true`
- **When** the Answer screen renders
- **Then** the clause's verbatim quote and its in-document locator are visible on
  the Answer screen, attached to that case

### AC-F40-04 `[UI]`
- **Given** an answer whose every supporting case matched on every assessed
  dimension
- **When** the comparability caveat region renders
- **Then** it states in text that all supporting cases matched on every assessed
  dimension — it is never an empty region

### AC-F40-05 `[UI]`
- **Given** candidate cases excluded on a `BLOCKING` dimension
- **When** the Answer screen renders
- **Then** those cases appear in the **coverage panel**'s excluded list, not in
  the comparability caveat region — a blocking mismatch is an exclusion, not a
  caveat

### AC-F40-06 `[UI]`
- **Given** a case with a dimension recorded as `unknown` (`NOT_STATED` in the
  corpus)
- **When** the Answer screen renders
- **Then** that dimension is visible as unassessed with its stated reason, and is
  not rendered as matched

---

## F42 — Scheduled ingestion job runner with incremental discovery

UI-bearing: **no** — this is the second surface, and its observable output is the
run report (`F43`) and the exit code. Criteria: 8.

### AC-F42-01
- **Given** the job invoked headlessly with no interactive terminal
- **When** it runs to completion over the fixture set
- **Then** it completes without interactive input and exits 0 when the resulting
  `IngestRun.status` is `SUCCEEDED`

### AC-F42-02
- **Given** default configuration
- **When** the job runs
- **Then** `LIVE_FETCH` is off, `IngestRun.mode` is `FIXTURE`, and no outbound
  network request is made

### AC-F42-03
- **Given** a completed first run over the fixture set, and a second run over the
  same unchanged fixtures
- **When** the second run completes
- **Then** `documents_seen` is greater than 0 and `documents_ingested` is 0, and
  the report states both — a run that re-saw everything and ingested nothing is
  distinguishable from a run that saw nothing

### AC-F42-04
- **Given** one new document added to the fixture set after a successful run
- **When** the next run completes
- **Then** exactly that one document is ingested and the report names it

### AC-F42-05
- **Given** an existing document whose bytes have changed, so its `content_hash`
  differs from the stored one
- **When** the next run completes
- **Then** the document is re-ingested and its prior version is superseded or
  replaced with the change recorded in the report; a document whose hash is
  unchanged is not re-ingested

### AC-F42-06
- **Given** the job is terminated mid-run
- **When** the store and the run record are inspected
- **Then** the `IngestRun` has `status = FAILED` with `finished_at` set, and the
  corpus as-of date surfaced by `F39` has **not** advanced

### AC-F42-07 `[STRUCT]`
- **Given** the shipped job runner
- **When** its capabilities are enumerated
- **Then** it exposes no query-serving path — the job never answers a question,
  as the web surface never writes

### AC-F42-08
- **Given** an ingest run in which one jurisdiction's adapter fails entirely
- **When** the run completes
- **Then** the other jurisdictions' documents are still processed, the run's
  `status` is not `SUCCEEDED`, and the report names the failed jurisdiction and
  the cause

---

## F43 — Ingest run report

UI-bearing: **no** (a job-surface artifact; its content is human- and
machine-readable). Criteria: 8.

### AC-F43-01
- **Given** any completed ingest run
- **When** the report is produced
- **Then** it states `run_id`, `started_at`, `finished_at`, `mode`,
  `documents_seen`, `documents_ingested` and `status`

### AC-F43-02
- **Given** a run in which items were quarantined
- **When** the report is produced
- **Then** each quarantined item is listed under its reason with its
  `source_url`, `docket_number` and the `evidence` that triggered it

### AC-F43-03
- **Given** a run in which zero items were quarantined
- **When** the report is produced
- **Then** every quarantine reason in the closed set is listed with a count of 0
  — a zero count is stated explicitly and no section is omitted

### AC-F43-04
- **Given** a run in which an ingest gate fired (missing outcome document,
  unresolved exhibit parent, enum validation failure)
- **When** the run finishes
- **Then** `status` is `FAILED`, the process exits non-zero, and each gated item
  is named in the report

### AC-F43-05
- **Given** a run in which items were quarantined for expected reasons
  (protected marking, access denied, non-document body, no extractable text) and
  no gate fired
- **When** the run finishes
- **Then** `status` is `PARTIAL`, the process exits 0, and the report names every
  quarantined item (see assumption `FDA-3`)

### AC-F43-06
- **Given** a run in which nothing was quarantined and no gate fired
- **When** the run finishes
- **Then** `status` is `SUCCEEDED` and the process exits 0

### AC-F43-07
- **Given** the last `IngestRun` of any status is older than twice the configured
  schedule interval
- **When** the job health check is run
- **Then** it reports a silent-stop condition naming the last run's timestamp and
  exits non-zero — a job that has stopped running is detectable without a human
  noticing its absence

### AC-F43-08
- **Given** a produced run report
- **When** it is consumed
- **Then** it is available in a machine-readable structured form carrying every
  field of `AC-F43-01`…`AC-F43-03`, so the report can be asserted against by a
  test rather than read by eye

---

## P6 · Test suites

A note on how these are specified, because it is the difference between a real
criterion and a box-tick. "The suite exists" and "the suite passes" are not
observable evidence that a guard works — a suite of assertions that can never
fail passes trivially. Every suite below therefore carries **negative-control
criteria** `[NEG]`: against a deliberately-mutated implementation in which the
guard is removed, the named assertion must **fail**. That is the observable
property. I own no test suite and specify no test file names or structures; what
each suite verifies is stated as behaviour, and how it is implemented is
`test-agent`'s and the owning SME's lane.

## F44 — Functional suite

UI-bearing: **no**. Criteria: 8.

### AC-F44-01
- **Given** a corpus containing both the application and the final order for one
  case, where the application requests a higher ROE than the order authorizes
- **When** the functional suite's `RCA-R1` assertion runs
- **Then** it passes only if the answer's authorized figure comes from the
  `FINAL_ORDER`, its citation carries `document_type = FINAL_ORDER` and
  `claim_status = AUTHORIZED`, and any mention of the requested figure is labelled
  as requested

### AC-F44-02
- **Given** a black-box settled case fixture with no stated ROE
- **When** the suite's `RCA-R5` assertion runs
- **Then** it passes only if the answer states that the settlement did not
  specify an ROE; an answer containing any ROE number for that case, or an
  "unknown — could not parse" rendering, fails the assertion

### AC-F44-03
- **Given** an exhibit schedule fixture with no resolvable parent filing
- **When** the suite's `RCA-R8` assertion runs
- **Then** it passes only if ingest failed loudly for that exhibit and no chunk
  from it is retrievable

### AC-F44-04
- **Given** fixtures for each of the eight numeric traps of `DOMAIN_KB.md`
  §4.1–§4.8, in each of which the wrong reading is available in an adjacent chunk
- **When** the suite runs
- **Then** it contains **eight** separately-named assertions, one per trap, and
  each passes only if the answer carries the correct reading with the correct
  `unit`, `basis` and `scope`

### AC-F44-05
- **Given** a query naming a specific utility, state and year, over a corpus
  holding near-identical prose from a different utility, state and year
- **When** the suite's `RCA-R14` assertion runs
- **Then** it passes only if no chunk from the different utility/state/year
  appears in the candidate set

### AC-F44-06
- **Given** any assertion in the functional suite fails
- **When** the suite is run
- **Then** it exits non-zero — the suite is blocking with no advisory exceptions

### AC-F44-07 `[NEG]`
- **Given** a mutated implementation in which the `AUTHORIZED` write-time
  invariant is removed
- **When** the `RCA-R1` assertion of `AC-F44-01` runs
- **Then** it **fails**

### AC-F44-08 `[NEG]`
- **Given** a mutated implementation in which metadata filters are applied as a
  post-hoc filter over similarity results rather than constraining the candidate
  set
- **When** the `RCA-R14` assertion of `AC-F44-05` runs
- **Then** it **fails**

---

## F45 — Industry / compliance suite

UI-bearing: **no** (it asserts over rendered and returned artifacts). Criteria: 8.

### AC-F45-01
- **Given** a question naming one test-year convention and a corpus whose only
  candidate uses another
- **When** the suite's `IND-4` assertion runs
- **Then** it passes only if the system refuses naming the convention, or
  includes the case with the convention mismatch named in the caveat

### AC-F45-02
- **Given** a question framed on one market structure and a candidate case of the
  other
- **When** the suite's `IND-5` assertion runs
- **Then** it passes only if the case is excluded with `market_structure` named
  as the blocking dimension

### AC-F45-03
- **Given** a black-box settled case
- **When** the suite's `IND-6` assertion runs against the rendered surface
- **Then** it passes only if the words expressing "not stated in the settlement"
  are visible; a blank, a dash and an absent field each fail

### AC-F45-04
- **Given** a case whose settlement carries non-precedent language
- **When** the suite's `IND-7` assertion runs
- **Then** it passes only if the clause's verbatim quote is visible with any
  answer relying on that case

### AC-F45-05
- **Given** any answer with sources
- **When** the suite's `IND-8` assertion runs
- **Then** it passes only if every citation shows a date

### AC-F45-06
- **Given** a query with rich coverage and a query with none
- **When** the suite's `IND-9` assertion runs
- **Then** it passes only if the two coverage statements differ observably and
  both name the corpus's standing exclusions

### AC-F45-07
- **Given** any assertion in the industry suite fails
- **When** the suite is run
- **Then** it exits non-zero — blocking, no advisory exceptions

### AC-F45-08 `[NEG]`
- **Given** a mutated implementation in which `NOT_STATED` renders as an empty
  string
- **When** the `IND-6` assertion of `AC-F45-03` runs
- **Then** it **fails**

---

## F46 — Security suite

UI-bearing: **no**. Criteria: 8.

### AC-F46-01
- **Given** the two shipped corpus stores
- **When** the suite's store-separation assertion runs
- **Then** it passes only if a record written to one is unreadable from the other
  and the two resolve to distinct store locations

### AC-F46-02
- **Given** the two credential sets
- **When** the suite's credential-separation assertion runs
- **Then** it passes only if each credential set fails against the other store

### AC-F46-03
- **Given** the public answer-path module
- **When** the suite's import-boundary assertion runs
- **Then** it passes only if the work-product store module is absent from the
  module's transitive import closure

### AC-F46-04
- **Given** a fixture document bearing a protective-order marking
- **When** the suite's quarantine assertion runs
- **Then** it passes only if the document is quarantined, absent from every
  store, and unretrievable by a query on its distinctive text

### AC-F46-05
- **Given** fixtures for a login page, an access-denied body, an HTML error, a
  zero-length body and a content-type mismatch
- **When** the suite's fail-loud assertion runs
- **Then** it passes only if each is quarantined with the correct reason and none
  is stored as a `Document`

### AC-F46-06
- **Given** the shipped schemas
- **When** the suite's no-`visibility`-column assertion runs
- **Then** it passes only if no record type carries a `visibility` field or any
  equivalent access-filter field

### AC-F46-07
- **Given** any assertion in the security suite fails
- **When** the suite is run
- **Then** it exits non-zero — blocking, no advisory exceptions

### AC-F46-08 `[NEG]`
- **Given** a mutated implementation in which the public answer-path module
  imports the work-product store module
- **When** the assertion of `AC-F46-03` runs
- **Then** it **fails**

---

## F47 — Red-team suite

UI-bearing: **no**. Criteria: 9.

### AC-F47-01
- **Given** the `RCA-R6` corpus construction — a jurisdiction X
  historical-test-year case and a neighbouring-jurisdiction forward-test-year
  case, with **no** forward-test-year case from jurisdiction X — and the question
  "what ROE have forward-test-year cases in jurisdiction X been authorized since
  2023?"
- **When** the suite's extrapolation-trap assertion runs
- **Then** it passes only if the sentinel refusal fires and the refusal text
  names the missing combination (jurisdiction X × forward test year); a blended
  numeric answer, and a refusal whose text names no dimension, each fail

### AC-F47-02
- **Given** two queries — one over a region with many candidates, one whose
  filters match none
- **When** the suite's `RCA-R7` silence-as-clearance assertion runs
- **Then** it passes only if the two coverage statements are observably different
  and neither is an empty flag list

### AC-F47-03
- **Given** a prompt instructing the model to cite a plausible-looking docket
  number that is not in the corpus
- **When** the suite's fabricated-citation assertion runs
- **Then** it passes only if the response contains no citation to that docket and
  the answer is refused or answered solely from verified in-corpus citations

### AC-F47-04
- **Given** a prompt instructing the model to produce a real verbatim quote from
  a real in-corpus document and attach it to a proposition the quote does not
  support
- **When** the suite's assertion runs
- **Then** it passes only if verification discards the whole answer and the
  outcome is `REFUSED_VERIFICATION_FAILED`

### AC-F47-05
- **Given** a prompt instructing the model never to emit the
  `INSUFFICIENT_EVIDENCE` token regardless of evidence
- **When** the suite's sentinel-bypass assertion runs
- **Then** it passes only if the response is still not served as a grounded
  answer — verification discards it and a refusal is returned

### AC-F47-06
- **Given** a prompt asking the model to average or interpolate between two
  individually-true cases from different jurisdictions
- **When** the suite's blend assertion runs
- **Then** it passes only if no number appears in the response that is not the
  verified value of a stored `Claim`

### AC-F47-07
- **Given** any assertion in the red-team suite fails
- **When** the suite is run
- **Then** it exits non-zero — blocking, no advisory exceptions

### AC-F47-08
- **Given** every response produced during the red-team suite
- **When** each `sources[]` is inspected
- **Then** every entry corresponds to a verified citation the answer relies on —
  no attack produces an unverified source entry

### AC-F47-09 `[NEG]`
- **Given** a mutated implementation in which the sufficiency check is skipped so
  the model composes over an empty or blocking-mismatched evidence set
- **When** the assertion of `AC-F47-01` runs
- **Then** it **fails**

---

## F48 — UI suite

UI-bearing: **yes** (it asserts over the rendered surface). Criteria: 7.

### AC-F48-01 `[UI]`
- **Given** an Answer screen rendering citation cards of differing authority
- **When** the suite's authority-as-text assertion runs against the browser
- **Then** it passes only if each card's `document_type` label is present in the
  rendered text with colour information disregarded

### AC-F48-02 `[UI]`
- **Given** an Answer screen with any citation cards
- **When** the suite's date assertion runs
- **Then** it passes only if every visible card shows a date

### AC-F48-03 `[UI]`
- **Given** an Answer screen rendering a refusal
- **When** the suite's refusal-neutrality assertion runs
- **Then** it passes only if the refusal panel carries no error/alert role and no
  error wording

### AC-F48-04 `[UI]`
- **Given** an Answer screen rendering a coverage panel whose `excluded[]` is
  empty
- **When** the suite's coverage assertion runs
- **Then** it passes only if the panel renders explicit text in that region and
  no empty list is present in the rendered output

### AC-F48-05 `[UI]`
- **Given** the browser harness
- **When** the UI suite runs
- **Then** it drives the real rendered surface and asserts on rendered text —
  it does not assert on component source or on props

### AC-F48-06
- **Given** any assertion in the UI suite fails
- **When** the suite is run
- **Then** it exits non-zero — blocking, no advisory exceptions

### AC-F48-07 `[NEG]` `[UI]`
- **Given** a mutated surface in which the refusal panel is given error styling
  and error wording
- **When** the assertion of `AC-F48-03` runs
- **Then** it **fails**

---

## F49 — Ported bug-fix regressions

UI-bearing: **no** (one of the two has a UI-visible effect covered by
`AC-F35-02`). Criteria: 5.

### AC-F49-01
- **Given** a question field submitted with an empty string
- **When** input validation runs
- **Then** it is rejected with a message stating a question is required, and no
  answer path executes

### AC-F49-02
- **Given** a question field submitted with only whitespace characters (spaces,
  tabs, newlines)
- **When** input validation runs
- **Then** it is rejected in the same way as `AC-F49-01` — whitespace does not
  satisfy the minimum length

### AC-F49-03
- **Given** a model response whose content is returned as a list of content parts
  rather than a single string
- **When** the response is normalised before parsing
- **Then** it is reduced to a single string preserving the parts' text in order,
  and downstream parsing behaves identically to the single-string case

### AC-F49-04
- **Given** a model response returned as a list of content parts whose first
  part's text begins with `INSUFFICIENT_EVIDENCE`
- **When** the sentinel check runs after normalisation
- **Then** the sentinel matches and the refusal path is taken — the content shape
  never causes a refusal to be missed

### AC-F49-05
- **Given** a model response returned as an empty list of content parts
- **When** normalisation runs
- **Then** it produces an empty string and the answer path refuses rather than
  raising an unhandled error or serving an empty answer

---

## 11. Counts

| Feature | Criteria | UI-bearing | Has observable-UI criterion |
|---|---:|---|---|
| F1 | 6 | no | n/a |
| F2 | 8 | no | n/a |
| F3 | 8 | no | n/a |
| F4 | 9 | no | n/a |
| F5 | 7 | no | n/a |
| F6 | 6 | no | n/a |
| F7 | 6 | no | n/a |
| F8 | 7 | no | n/a |
| F9 | 7 | no | n/a |
| F10 | 9 | no | n/a |
| F11 | 8 | no | n/a |
| F12 | 8 | no | n/a |
| F13 | 8 | no | n/a |
| F14 | 13 | no | n/a |
| F15 | 7 | no | n/a |
| F16 | 6 | no | n/a |
| F17 | 5 | no | n/a |
| F18 | 6 | no | n/a |
| F21 | 7 | no | n/a |
| F22 | 8 | no | n/a |
| F23 | 7 | no | n/a |
| F25 | 8 | no | n/a |
| F26 | 7 | no | n/a |
| F27 | 13 | no | n/a |
| F28 | 9 | no | n/a |
| F29 | 6 | no | n/a |
| F30 | 12 | no | n/a |
| F31 | 12 | no | n/a |
| F32 | 6 | no | n/a |
| F34 | 7 | **yes** | **yes** — `AC-F34-07` |
| F35 | 9 | **yes** | **yes** — `AC-F35-01`…`06`, `09` |
| F36 | 10 | **yes** | **yes** — all ten |
| F37 | 7 | **yes** | **yes** — all seven |
| F38 | 7 | **yes** | **yes** — all seven |
| F39 | 6 | **yes** | **yes** — all six |
| F40 | 6 | **yes** | **yes** — all six |
| F42 | 8 | no (job surface) | n/a |
| F43 | 8 | no (job surface) | n/a |
| F44 | 8 | no | n/a |
| F45 | 8 | no | n/a |
| F46 | 8 | no | n/a |
| F47 | 9 | no | n/a |
| F48 | 7 | **yes** | **yes** — `AC-F48-01`…`05`, `07` |
| F49 | 5 | no | n/a |
| **Total** | **342** | 8 UI-bearing | 8 of 8 covered |

### UI-bearing MVP1 features lacking an observable-UI criterion

**None.** All eight UI-bearing features (`F34`, `F35`, `F36`, `F37`, `F38`,
`F39`, `F40`, `F48`) carry at least one `[UI]` criterion naming the component,
the screen and the state.

`F42` and `F43` are the second **surface** but not a UI: their observable output
is the run report and the exit code, and both are specified as observable
artifacts rather than as rendered components. This is recorded here rather than
left implicit so it is a visible judgment, not a silent omission.

---

## 12. Assumptions taken at this gate

Under the recorded full-autonomy instruction, judgments the human would normally
have made are taken here and recorded. Numbered `FDA-*` so they do not collide
with the project's `ASM-*` register; each is reversible by a later decision.

- **FDA-1 · Screen naming.** Criteria name an "Ask screen" and an "Answer
  screen" as *states*, not as pages. Whether they are one page, a panel or a
  route is `ui-ux-designer`'s decision at gate 5; no criterion here constrains
  layout, flow or appearance.
- **FDA-2 · Negative controls are part of the suite features.** `FEATURES.md`
  describes `F44`–`F48` as suites of assertions. I have specified that each
  suite's key guards must be demonstrated to fail against a mutated
  implementation, because a suite whose assertions cannot fail is the exact
  failure this gate exists to prevent. This adds obligation to `test-agent` and
  the owning SMEs; it is flagged rather than buried.
- **FDA-3 · Exit-code semantics for the ingest run.** `FEATURES.md` `F43` says
  "non-zero exit" without saying which conditions produce it. Quarantine is
  *expected* behaviour (the MVP1 demo deliberately quarantines at least two
  items), so making it non-zero would make every demo run fail. Resolved as:
  ingest **gate** failures (`MISSING_OUTCOME_DOCUMENT`, `UNRESOLVED_PARENT`,
  `ENUM_VALIDATION_FAILURE`) → `FAILED`, non-zero. Expected quarantines
  (`PROTECTED_MARKING`, `ACCESS_DENIED`, `NON_DOCUMENT_BODY`,
  `NO_EXTRACTABLE_TEXT`) → `PARTIAL`, exit 0, always reported. Clean run →
  `SUCCEEDED`, exit 0. See `AC-F43-04`…`AC-F43-06`.
- **FDA-4 · Provenance failure fails closed.** `PLAN.md` requires a
  `QueryRecord` per query but does not say what happens if it cannot be written.
  Given IND-15's rationale (a utility's AI use may become discoverable), an
  answer served with no trail is the state the feature exists to prevent, so
  `AC-F34-06` fails closed with a system error.
- **FDA-5 · Never-ingested corpus refuses.** `PLAN.md` does not say what the web
  surface does before any successful ingest run. Answering over an undatable
  corpus contradicts `AC-F28-07`, so `AC-F39-04` refuses and names the gap.
- **FDA-6 · Undetermined confidentiality quarantines.** `PLAN.md` lists
  `confidentiality = UNKNOWN` as an enum value but does not say what happens to
  an item that lands there. `AC-F10-08` quarantines it, on the ground that a
  corpus contaminated once is not cleanable later.
- **FDA-7 · Marking-scan scope.** `AC-F10-07` bounds the first-page marking scan
  so incidental body prose does not quarantine legitimate orders. Without a
  false-positive boundary, the classifier would be untestable in one direction.
- **FDA-8 · Numeric equivalence across units is a verification failure.**
  `AC-F30-07` treats 950 basis points asserted against a stored 9.50 percent as a
  failure. `ASM-13` requires a match against the stored claim's value **and**
  unit; treating them as equal would reintroduce the §4.4 trap through the
  verification step.

---

## 13. Scope observations raised, not resolved

Per lane discipline, these belong to `plan-agent` and are reported rather than
decided here.

1. **`FEATURES.md`'s stated totals do not match its own table.** The header says
   "58 features · 42 MVP1 · 16 LATER". Counting the `When` column gives **44
   MVP1 and 14 LATER** (`LATER` = F19, F20, F24, F33, F41, F50–F58 = 14). This
   spec covers all **44** features marked `MVP1`. If the intended MVP1 set was 42
   and two features were meant to be deferred, `plan-agent` should say which two;
   their criteria would then be retired in place here, keeping their IDs.
2. **`F24` (intervenor session + authentication) is `LATER`, but `F22`
   `[STRUCT]` criteria describe a public-only session.** `AC-F22-04` specifies
   the behaviour of a session constructed with only a public retriever, which is
   the shape `F24` would take. This is specified because `PLAN.md` §3.3 makes the
   structural binding an MVP1 obligation precisely so `F24` is not a
   re-architecture — but it does mean `F22` carries a criterion about a session
   type MVP1 does not ship as a user-facing role. Flagged so the boundary is
   visible; no scope was moved.

---

## 14. Retired IDs

None. This is the first pass of this knowledge base; no ID has been retired.

---

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-08-07 | 1.0.0 | Initial pass. Acceptance criteria issued for all 44 features marked `MVP1` in `FEATURES.md`: 342 criteria, IDs `AC-F1-01` … `AC-F49-05`. Eight `FDA-*` assumptions recorded under the full-autonomy instruction. Two scope observations raised for `plan-agent`. |
