# Architecture Knowledge Base — rate-case-analyzer

**Owner**: `solution-architect` · **Gate**: 6 · Architecture (joint owner with
`security-architect`) · **Written**: 2026-08-07 · operating mode **full
autonomy** (gate closes `assumed`, not `approved`).

**Non-droppable on this project** — two surfaces (desktop web + scheduled
ingestion job), recorded in `PROJECT_CONTEXT.md`'s Decisions Log 2026-08-07.
The **Impact Analysis** in §12 is mandatory and is a gate-blocking artifact.

Binding inputs read in full before writing: [`PLAN.md`](../PLAN.md) (esp. §7,
addressed to this agent), [`FEATURES.md`](../FEATURES.md),
[`FUNCTIONAL_SPEC.md`](FUNCTIONAL_SPEC.md) (342 criteria),
[`UX_KB.md`](UX_KB.md), [`DOMAIN_KB.md`](DOMAIN_KB.md),
[`INDUSTRY_KB.md`](INDUSTRY_KB.md), [`PROJECT_CONTEXT.md`](../PROJECT_CONTEXT.md),
[`INTAKE.md`](../INTAKE.md), and
`projects/policy-lookup-assistant/knowledge/ARCHITECTURE_KB.md` (proven patterns
in the same industry).

**No open items are left for the human.** Where `policy-lookup-assistant` left
an open item (the `sources[]` trade-off, the malformed-manifest-key gap), this
document decides. Every judgment taken under the autonomy instruction is
numbered `ASA-*` in §14 and is reversible.

---

## 0. Completeness check — binding decisions this design was checked against

Re-read in full immediately before writing: `PROJECT_CONTEXT.md`'s Decisions Log
(standing constraints 1–4, gates 1–2 `ASM-1…ASM-5`, `ASM-22`), `PLAN.md` §0/§7/§10
(`ASM-6…ASM-21`), `FUNCTIONAL_SPEC.md` §0 and §12 (`FDA-1…FDA-8`), `UX_KB.md` §9.3
(`ASM-UX-1…11`) and §9.4 (four open items, one addressed to me). There is no
prior pass of this KB, so every binding decision is checked here for the first
time.

| Binding decision | Where recorded | How this design satisfies it |
|---|---|---|
| Standing constraint 1 — grounding mandatory; unsupported claim refuses | Decisions Log; A7.3 | §7 answer path; §7.4 deterministic verification is a pure function that fails closed; §7.5 sentinel. `Answer` has a private constructor reachable only from the verifier (§7.4). |
| Standing constraint 2 — two stores, two credential sets, retriever bound at **session construction**, **no code path** to the other corpus | Decisions Log; IND-14 | §4 in full. Physical separation (§4.1), credential gate (§4.2), typed session binding (§4.4), statically-checked import boundaries with negative controls (§4.5–§4.6). |
| Standing constraint 3 — aggregate leak; public corpus only; `corpus` first-class now | Decisions Log; PLAN §3.3 | §6.2 `corpus` is a **required, defaulted-nowhere** column on `case`/`document`/`chunk`/`claim`, and `Source` subtypes carry it as a read-only class property (§7.4) so a public path cannot emit a work-product source. |
| Standing constraint 4 — silence is not clearance; coverage on every path | Decisions Log; A7.2 harm #3 | §8 `CoverageLedger.seal()`; `Coverage` has no public constructor and cannot be built violating the partition arithmetic. Both `Answer` and `Refusal` require it. |
| ASM-3 — `sources[]` from what the answer **relies on** | Decisions Log; gate 1 | §7.4. `build_sources()` takes exactly **one** parameter, of type `VerifiedCitations`; the retrieval result set is not in its scope. This is the escalated open item from `policy-lookup-assistant`, now closed. |
| Authority two-dimensional; `NOT_STATED` representable, distinct from parse failure | Gate 1; DOMAIN §2.3/§2.4 | §6.3. `claim_status` is a `CHECK`-constrained closed enum with `NOT_STATED` a member; parse failure writes **no row** and one `IngestRun.failures[]` entry, in a different database (§6.1). |
| Comparability a structured predicate, never a score | Gate 1; RCA-R14 | §8.1 — a **tagged union of three types**, `NonEmpty[...]` on the non-comparable arms, no float field permitted anywhere in `app/comparability/` (statically checked). |
| Outcome-completeness is an ingest **gate** | ASM-9; INDUSTRY §6.5.1 | §5.3 stage 6; a gate failure returns `GateFailure`, which has no constructor path to `IngestableCase`, which is the only type `store.write_case()` accepts. |
| Confidential material → quarantine-and-report, never flag-and-index | Gate 1; IND-10; RCA-R11 | §5.2/§5.3. `document.confidentiality` carries a SQL `CHECK <> 'PROTECTED'`, so a protected row is **unrepresentable in the store**, not merely unwritten. |
| Schema-bound risks RCA-R4 / R11 / R13 | Gate 1 findings | §6.3 — supersession as a single edge row with a same-case `CHECK` (one-sided links unrepresentable); `confidentiality`; `case_status` incl. `WITHDRAWN` with the `AUTHORIZED` trigger. |
| Sentinel ported: exact `.startswith()`, prose discarded | Deliberate reuse; PLAN §3.5 step 7 | §7.5 — the sentinel path is **two zero-`import` modules**, which is what makes `AC-F31-12` statically checkable rather than reviewed. |
| Closed-enum validation, fail-loud on unknown values **and unknown keys** | Deliberate reuse; PLAN §4.6 | §6.2 — `pydantic` `extra="forbid"` + `StrEnum` + SQL `CHECK`. Closes the gap `policy-lookup-assistant` identified and deferred. |
| Badge/citation UI: authority as text; refusal neutral | IND-3/IND-8; UX §5, §7.1 | §9 — templates adopt `design-review/` markup and `rca.css` unchanged; the enum-gloss rule of `UX_KB` §7.1 is implemented as a render-boundary filter (§9.2). |
| Two ported bug fixes | Deliberate reuse | §10.2 — `app/model/content.py` (content-shape normaliser, ours not a vendor's) and the whitespace-rejecting question validator in `app/web/forms.py` + `app/grounding/question.py`. |
| MVP = #1 + #2; **no aggregates** (ASM-14) | Decisions Log; A8.3 | No aggregate, average or statistics module exists in §3's layout. Deliberate: there is nothing to reach for when `F33` is proposed. |
| ASM-1 jurisdictions PA PUC + PUCT + CPUC | Decisions Log | §5.1 three adapters behind one `DocketAdapter` protocol. |
| ASM-2 / ASM-19 live fetch behind a flag, default off | Decisions Log | §5.1 — `FixtureTransport` is the default and its import closure **excludes every HTTP client**, which is why `AC-F5-01` is structural rather than conditional. |
| ASM-5 all suites blocking | Decisions Log | §11 — seven entry points, all blocking, empty collection exits non-zero. |
| ASM-8 eight parameters; ASM-13 exact verbatim matching | PLAN §10 | §6.3 `claim.parameter` `CHECK`ed against the eight; §7.4 normalisation covers whitespace + hyphenation only, and contains no unit-conversion symbol (FDA-8). |
| ASM-11 parse failure refuses, no fallback search | PLAN §10 | §7.1 — the frame parser returns `QueryFrame | ParseFailure`; retrieval accepts only `QueryFrame`. No keyword-search module exists. |
| ASM-12 role binding ships, login does not | PLAN §10 | §4.4 — two session types, role from a `CHECK`ed config enum, no auth module. |
| ASM-17 thresholds configurable | PLAN §10 | §6.5 — both in the typed config module; no literal in code (`AC-F32-05`). |
| ASM-20 no real work product | PLAN §10 | §4.3 — the work-product store is loaded only by `app/cli/load_synthetic.py` from `synthetic-data-agent`'s asset; no ingestion adapter writes to it. |
| Custom template — harness is our work | Decisions Log | §11, built from scratch, sized as real work. |
| Repo hygiene + path-anchored store dirs | Decisions Log (override cost b) | §3.3 — `REPO_ROOT` from `Path(__file__).resolve()`, never `cwd`; one env-reading module, statically checked. |
| **Stack deferred to gate 6** | Decisions Log 2026-08-07 | §2 — decided here, against `PLAN.md` §7's twelve requirements, one by one, in §2.4. |
| `FDA-3` ingest exit-code semantics | FUNCTIONAL_SPEC §12 | §10.1 — the exit code is a total function of `IngestRun.status`, and `status` is computed from the quarantine/gate split, not set by hand. |
| `FDA-4` provenance fails closed | FUNCTIONAL_SPEC §12 | §7.6 — the `QueryRecord` write happens **before** the response is handed to the renderer; a write failure raises `SystemError`, a third response type. |
| `FDA-8` unit equivalence is a failure | FUNCTIONAL_SPEC §12 | §7.4 — comparison is exact tuple equality over `(Decimal(value_text), unit, scope, basis)`; no converter exists in `app/`. |
| `ASM-UX-6` — the MVP1 session's corpus binding is **my call** | `UX_KB` §9.4 item 1 | **Decided in §4.4**: MVP1 ships `UtilityAnalystSession` bound to **both** retrievers. The app-bar chip "public + internal corpora" stands and the work-product citation-card variant is reachable. |
| `ASM-UX-2` no session history; `ASM-UX-11` no chart component | `UX_KB` §9.3 | §9 — one answer per render, and no chart/aggregate template partial exists. |

**No conflict found** with any recorded binding decision. Three refinements of
`PLAN.md` §4's *storage shape* (never its field names or semantics) are declared
openly in §6.3 and §6.4 rather than made silently; each strengthens an invariant
`PLAN.md` asked for.

---

## 1. Write set and resumability

This pass creates exactly one file: `knowledge/ARCHITECTURE_KB.md`. Nothing under
`dev/`, `PROJECT_CONTEXT.md`, `SECURITY_KB.md` or `RESPONSIBLE_AI_KB.md` is
touched — `security-architect` and `responsible-ai-architect` are running
concurrently on their own KBs and the orchestrator owns the context file.

No reference in this document points at a file that does not exist, **except**
the `dev/` paths in §3, §11 and §13, which are the design `code-agent` is being
asked to create and are marked as such at the head of §3.

---

## 2. The stack — the headline decision

### 2.1 What is chosen

| Layer | Choice | Version floor |
|---|---|---|
| Language / runtime | **Python 3.12** (`StrEnum`, `match`, PEP 695 generics available) | 3.12 |
| Web surface | **FastAPI + Jinja2, server-rendered HTML**. No SPA, no node, no build step. | fastapi ≥0.115, jinja2 ≥3.1 |
| Client JS | **~40 lines of hand-written vanilla JS**, one file, progressive enhancement only (in-flight indicator, client-side empty-question guard) | — |
| Types / validation | **pydantic v2**, `extra="forbid"`, `frozen=True`, `StrEnum` | ≥2.8 |
| Corpus stores | **Two independent SQLite databases**, one per corpus, `STRICT` tables, `PRAGMA foreign_keys=ON`, opened through a credential gate (§4.2) | stdlib `sqlite3` |
| Operations store | **A third SQLite database** (`ops`) for `IngestRun`, `QuarantineRecord`, `QueryRecord` | stdlib |
| Vectors | **Float32 blobs in the corpus DB + exact cosine ranking in `numpy` over the already-filtered candidate set.** No vector database. | numpy ≥1.26 |
| Embeddings | **OpenAI `text-embedding-3-small`** at ingest; **deterministic local hashing embedder** (`EMBEDDINGS_PROVIDER=hash`, stdlib) for all suites and offline runs | openai ≥1.40 |
| Chat model | **Anthropic `claude-sonnet-4-5` via the `anthropic` SDK directly** (no LangChain), forced tool-use for structured output | anthropic ≥0.40 |
| Document extraction | **`pypdf`** (`extraction_mode="layout"`) for PDF, **`python-docx`** for CPUC `.docx` | pypdf ≥5, python-docx ≥1.1 |
| HTTP (live fetch only) | **`httpx`**, imported only by `app/acquisition/live_transport.py` | ≥0.27 |
| Job scheduling | **`python -m app.jobs.ingest`** + a `launchd` plist template; no daemon of our own | — |
| Tests | **pytest** + **Playwright** (`pytest-playwright`) for the UI suite; per-suite `run.sh` | — |

**No LangChain. No Chroma. No node toolchain. No Docker. No cloud service of any
kind.** Total runtime dependency count: nine.

### 2.2 Why — the four decisions that carry the weight

**(a) Server-rendered FastAPI + Jinja2, not FastAPI + Next.js.**
`policy-lookup-assistant` shipped a separate SPA; `conclave-finance-studio` and
`conclave-dashboard` shipped server-rendered and both went well. Three specific
reasons decide it here, beyond the portfolio precedent:

1. **The UX deliverable is already the implementation.** `design-review/` is
   twelve static HTML pages plus one 27 KB `rca.css` with a stable, nameable
   class contract (`UX_KB` §9.1 says so explicitly: *"they are a component
   library, in the target technology"*). Server-rendered Jinja2 adopts that
   markup with near-zero translation. An SPA would re-express every one of those
   classes in JSX and then need `AC-F48-*` to assert against the *re-expression*.
   That translation step is exactly where a rendering invariant like "the refusal
   panel carries no error semantics" goes quietly missing.
2. **`AC-F35-07` — the verification step must not be bypassable from the
   client.** With server rendering, the browser never receives composition
   output at all; the only thing crossing the wire is finished HTML. The
   criterion becomes *structurally* true rather than defended by an API design.
   A JSON API for an SPA is, by construction, a third surface with its own
   contract, its own drift and its own review obligation — and I would then be
   obliged to carry it in every future Impact Analysis. Not adding it is the
   cheapest thing this design does.
3. **Build speed is a recorded human priority.** Two toolchains, two dependency
   trees, two failure surfaces and a Playwright harness that must wait on a dev
   server *and* an API server is the single largest schedule risk available here,
   over 44 features and 342 criteria.

The cost, stated: rich client interactivity later (`F41` saved queries, `F51`
capability #3) will want more than 40 lines of JS. Mitigation is that the answer
region is rendered from one template tree, so an incremental island (htmx or a
single web component) can be introduced without a rewrite. `ASA-1`.

**(b) SQLite as *both* the relational store and the vector store — and no vector
database.** This is the least obvious choice and the one that buys the most.

`PLAN.md` §7.2 requires metadata filtering **at the vector-search boundary, not
as a post-hoc join**, and §3.4 requires that similarity *never widens the
candidate set*. A vector database satisfies §7.2 with a `where` clause, but the
ordering guarantee then lives inside a third-party query planner where no test
of ours can see it. Doing it the other way round makes the guarantee structural:

```python
candidate_ids = store.filter_chunks(predicate)          # SQL. metadata only.
ranked        = rank_within(candidate_ids, query_vec, k) # numpy. ranks a set it was handed.
```

`rank_within` cannot return a chunk that was not passed to it, because it never
touches the store. `AC-F26-02` ("the ranked set is a subset of the filtered set")
stops being an assertion about behaviour and becomes an assertion about a
function signature. `AC-F44-08`'s negative control (rank-then-filter) is then
simulated by substituting a mutant ranker, with no edit to `app/`.

Secondary reasons: ASM-6 caps the corpus at 12 curated cases plus a synthetic
set — brute-force cosine over a filtered subset of a few thousand chunks is
sub-millisecond and *exact*, so there is no ANN recall to reason about; SQLite
gives `PLAN.md` §7.3's relational-quality querying, joins and write-time `CHECK`
constraints in the same engine; two databases are two files, which is the most
literal reading of "physically separate stores" available (§4.1); and it removes
the `chroma_db` relative-path bug class entirely, which the Decisions Log records
as override cost (b).

The cost, stated: this design does not scale to a corpus where the filtered
candidate set is routinely six figures. That is well beyond MVP1 and beyond
`F50`/`F52`; the migration path is to keep `filter_chunks` and swap `rank_within`
for an ANN index over the same blobs, which is one module. `ASA-2`.

**(c) No LangChain.** We use no LangChain retriever, vector store, loader,
chain or agent — every one of those is replaced above by something the design
requires to be inspectable. What would remain is a chat wrapper, and that
wrapper is the source of the `AIMessage.content: str | list` shape bug `F49`
exists to regress against. Calling the Anthropic SDK directly means the
content-shape normaliser is **ours**, in one named module, and `AC-F49-03/04/05`
test our own code rather than asserting a vendor's behaviour we cannot fix.
`ASA-3`.

**(d) Determinism over generation wherever the harm lives.** Fully argued in
§10; the short form is that this project's named harms are *generation* harms,
so the model is confined to two places (question → frame, evidence → prose),
both with forced-schema output, both fail-closed, and **all extraction is
deterministic**.

### 2.3 Explicitly considered and rejected

| Option | Why rejected |
|---|---|
| **Chroma** (as in `policy-lookup-assistant`) | Would satisfy §7.2 with `where`, but hides the metadata-before-similarity ordering inside a dependency; brings back the relative-path store bug the override already cost us once; and gives no relational joins for `case`/`document`/`claim` (§7.3), so we would need SQLite anyway and would then own *two* store technologies per corpus — four stores, four credential paths. |
| **PostgreSQL + pgvector** | Genuine credential separation (roles) and good filtering. Rejected: needs a server process on macOS for a local-dev target, and two databases in one cluster is one engine, one connection pool and one config surface — the exact shape `PLAN.md` §7.1 forbids. Two clusters would be two servers `deploy-agent` must start and keep alive. |
| **Next.js / React frontend** | §2.2(a). |
| **LangChain / LlamaIndex** | §2.2(c). |
| **An LLM extraction pipeline for `F13`/`F14`** | §10.1. Its failure mode is a confident wrong number; the rule-based extractor's failure mode is a *reported gap*, and the product already has a first-class channel for reported gaps (`AC-F14-11`). |
| **SQLCipher for at-rest encryption** | Wanted, but needs a compiled wheel, and the target is "must actually start on macOS". Deferred behind an unchanged interface (§4.2) and handed to `security-architect` as a named item, not silently dropped. |
| **A JSON API surface alongside the web pages** | Would create a third surface with an independent contract and a permanent Impact-Analysis obligation, for no MVP1 consumer. `AC-F43-08`'s machine-readable run report is a file, not an endpoint. |

### 2.4 `PLAN.md` §7 — the twelve requirements, one by one

| # | Requirement | How this stack satisfies it | Verified by |
|---|---|---|---|
| 1 | Two physically separable stores, independent credentials, no shared singleton/pool/config | Two SQLite **files** in two directories; `PublicStore` and `WorkProductStore` are distinct classes in distinct modules, each reading **only** its own config section (`PublicStoreConfig` / `WorkProductStoreConfig` — two types, no shared object); each opens its own `sqlite3.Connection`; there is no module-level connection, no pool, no cache. §4.1–§4.3 | `AC-F21-01/04/05`, security suite |
| 2 | Metadata filtering **at** the vector-search boundary, not post-hoc | Filtering *is* the boundary: SQL predicate produces the candidate id set, and the ranker is a pure function of that set. §7.2 | `AC-F26-01/02/06`, `AC-F44-08` `[NEG]` |
| 3 | Relational-quality querying; enums enforced at write time | SQLite `STRICT` tables, FKs on, `CHECK (col IN (...))` per enum column, plus triggers for the `AUTHORIZED` invariant and the supersession same-case rule. §6.2–§6.4 | `AC-F3-*`, `AC-F14-08/09`, `AC-F16-05` |
| 4 | Closed-enum validation, fail-loud on unknown **values and keys** | pydantic `extra="forbid"` rejects unknown keys; `StrEnum` members reject unknown/case-variant values with no coercion; SQL `CHECK` is the second line. §6.2 | `AC-F3-02/03/07` |
| 5 | Deterministic verbatim span matching with whitespace/hyphenation normalisation | `app/grounding/normalise.py` — NFKC, whitespace-run collapse, soft-hyphen and line-break-hyphen removal. **No case folding, no punctuation stripping, no fuzzy matcher, no unit converter.** §7.4 | `AC-F30-02/03`, `AC-F30-07` (FDA-8) |
| 6 | Text extraction preserving page and line numbers, plus table structure | `pypdf` layout mode preserves left-margin line numbers as text (testimony is line-numbered precisely so it can be cited); `python-docx` preserves CPUC table structure so a row label and its value land in one chunk. §5.4 | `AC-F11-01/02/03/07` |
| 7 | Server-side answer path, not reachable or bypassable from the client | Server-rendered HTML; the browser has no route that returns composition output. `app/web/**`'s import closure **excludes** `app/grounding/compose.py`; `Answer` is constructible only inside the verifier. §4.6, §7.4, §9 | `AC-F35-07` `[STRUCT]` |
| 8 | Schedulable job runner, headless, structured report, non-zero exit | `python -m app.jobs.ingest`; `IngestRun` → JSON report + exit code as a total function of status. `launchd` plist template; no daemon of ours. §10.1 | `AC-F42-01`, `AC-F43-04/05/06/08` |
| 9 | Browser-testable UI | Playwright against the real rendered pages; the `ui` suite exits non-zero if the browser binary is missing rather than skipping. §11 | `AC-F2-06`, `AC-F48-05` |
| 10 | Structured/constrained model output validated against a closed schema | Anthropic **forced tool use** for the frame parser and the composer; the tool schema *is* the closed schema; output is re-validated by pydantic. Neither call is parsed from free prose. §10.2 | `AC-F25-01/02`, `AC-F29-01/02` |
| 11 | Path-anchored store directories | `app/config/paths.py`: `REPO_ROOT = Path(__file__).resolve().parents[2]`. `cwd` is read nowhere; `os.environ` is read in exactly one module, statically asserted. §3.3 | `AC-F1-03/05`, `AC-F2-05/08` |
| 12 | Local-dev target; no test depends on a third-party site | `LIVE_FETCH` off by default and `FixtureTransport`'s closure contains no HTTP client at all; `LIVE_MODEL` off by default with a transcript-replay model client; `EMBEDDINGS_PROVIDER=hash` offline. Every suite runs with the network cable out. §5.1, §10.3 | `AC-F2-07`, `AC-F5-01`, `AC-F42-02` |

All twelve satisfied; none violated; none reinterpreted.

---

## 3. Module layout

> Everything under `dev/` in this section is **design to be created by
> `code-agent`**. As of this writing `dev/` contains only `README.md` and
> `.gitignore`.

### 3.1 The tree

```
dev/
  pyproject.toml            # deps + the seven suite entry points
  .env.example              # every required key, no values
  app/
    __init__.py
    config/
      paths.py              # REPO_ROOT, store dirs, fixture root — all absolute
      settings.py           # THE ONLY MODULE THAT READS os.environ  (AC-F1-05)
      schema.py             # typed config models; unknown key => startup failure
    enums/
      document.py           # DocumentType (14, ranked), AuthorParty, Confidentiality
      claim.py              # ClaimStatus (6), Parameter (8), Unit, Basis, Scope
      case.py               # CaseType, CaseStatus, TestYearConvention,
                            #   MarketStructure, ResolutionPath, JurisdictionCode
      corpus.py             # Corpus (PUBLIC | WORK_PRODUCT) — a LABEL, never a selector
      quarantine.py         # QuarantineReason, IngestStatus, QueryOutcome
      validate.py           # fail-loud validator: unknown value AND unknown key
    model/                  # pure records. imports no store, no adapter, no model client
      records.py            # Case, Document, Chunk, Claim, Jurisdiction
      ops.py                # QuarantineRecord, IngestRun, QueryRecord
      locator.py            # Locator(page, line_start, line_end, schedule_no, finding_no)
      source.py             # PublicSource / WorkProductSource (distinct types)
      content.py            # model content-shape normaliser (F49). ZERO imports.
    stores/
      sqlite_engine.py      # generic engine: open, migrate, credential gate. NO corpus arg.
      schema_sql.py         # DDL: STRICT tables, CHECKs, triggers, views
      credentials.py        # StoreCredential, fingerprint verify, StoreAuthenticationError
      public_store.py       # class PublicStore  — reads ONLY PublicStoreConfig
      workproduct_store.py  # class WorkProductStore — reads ONLY WorkProductStoreConfig
      ops_store.py          # class OpsStore — runs, quarantine, provenance
    retrieval/
      protocol.py           # EvidenceSource Protocol. imports neither store.
      filters.py            # QueryFrame -> SQL predicate (metadata only)
      rank.py               # rank_within(candidate_ids, query_vec, k) — pure, numpy
      public_retriever.py       # class PublicRetriever(PublicStore)
      workproduct_retriever.py  # class WorkProductRetriever(WorkProductStore)
    comparability/
      dimensions.py         # the nine dimensions + severities from PLAN §3.7
      types.py              # Comparable | ComparableWithCaveats | NotComparable
      predicate.py          # assess(frame, case) -> one of the three. no floats.
    coverage/
      ledger.py             # CoverageLedger -> Coverage.seal(); private constructor
      standing.py           # STANDING_EXCLUSIONS (non-empty, asserted at import)
    grounding/
      question.py           # whitespace-rejecting question validator (F49)
      frame.py              # QueryFrame | ParseFailure  (model call #1)
      prompts.py            # system prompts; imports the sentinel CONSTANT, never retypes it
      compose.py            # Composition (model call #2). imports no store, no retriever.
      normalise.py          # NFKC + whitespace + hyphenation. No case fold. No units.
      verify.py             # VerifiedCitations | VerificationFailure. pure.
      sentinel.py           # ZERO imports. one literal. one .startswith().
      refuse.py             # product-controlled refusal strings that NAME THE GAP
      vintage.py            # F32 caveats, thresholds from config
    answer/
      pipeline.py           # corpus-agnostic: contributions -> compose -> verify -> Response
      public_path.py        # PublicRetriever -> CorpusContribution(PUBLIC)
      workproduct_path.py   # WorkProductRetriever -> CorpusContribution(WORK_PRODUCT)
      response.py           # Answer | Refusal | SystemError. private constructors.
    session/
      public_only.py        # PublicOnlySession        — .public only
      utility_analyst.py    # UtilityAnalystSession    — .public AND .work_product
    acquisition/
      protocol.py           # DocketAdapter Protocol, Transport Protocol, IndexEntry
      fixture_transport.py  # default. closure contains NO http client.
      live_transport.py     # httpx. constructed only when LIVE_FETCH is on.
      capture.py            # fixture-capture tool (F5)
      pa_puc.py  puct.py  cpuc.py
    ingest/
      stages.py             # the typed stage chain (§5.3)
      sanity.py             # F9  non-document detection
      confidentiality.py    # F10 classify + quarantine
      extract_text.py       # F11 locators
      classify_doc.py       # F12 document_type + parent binding
      case_meta.py          # F13
      claims.py             # F14 deterministic claim extraction
      outcome_gate.py       # F15
      supersession.py       # F16
      clauses.py            # F17 non-precedent clause
      case_type.py          # F18 rider / formula-rate classification
      writer.py             # the ONLY module that calls store.write_case()
    jobs/
      ingest.py             # surface 2. no query path.
      healthcheck.py        # AC-F43-07 silent-stop detection
      report.py             # F43 run report: JSON + human-readable
    web/
      main.py               # FastAPI app. no store writes.
      routes.py             # GET / , POST /ask
      forms.py              # request validation (F49)
      render.py             # Response -> template context; the enum-gloss boundary
      templates/            # ask.html answer.html + partials mirroring rca.css classes
      static/rca.css        # adopted verbatim from design-review/assets/
      static/app.js         # ~40 lines. in-flight indicator + empty-question guard.
    cli/
      init_stores.py  load_synthetic.py  show_config.py
    wiring/
      compose_root.py       # THE ONLY MODULE THAT IMPORTS BOTH STORES
    boundaries.py           # the machine-readable import-boundary manifest (§4.6)
  tools/
    structural_checks/      # AST closure checker + shape rules. Used by 2 suites.
    propose_claims.py       # OFFLINE curation aid. Not importable from app/.
  fixtures/
    http/<sha256>.json      # byte-identical captured responses
    corpus/                 # the 12 curated cases' expected records (frozen baselines)
    transcripts/            # recorded model exchanges for offline suites
    synthetic/              # synthetic-data-agent's work-product asset
  tests/
    run_all.sh
    suites/{functional,industry,security,redteam,ui,architecture,unit}/run.sh
    suites/ux/run.sh        # shim -> ../ui/run.sh  (see §11.1)
    negative_controls/
  deploy/
    com.rca.ingest.plist.template
  data/                     # gitignored
    corpus_public/public.sqlite3
    corpus_workproduct/workproduct.sqlite3
    ops/ops.sqlite3
```

### 3.2 The dependency rule, in one sentence

**`enums` → `model` → (`stores` | `retrieval` | `comparability` | `coverage` |
`grounding`) → `answer` → `session` → (`web` | `jobs`) → `wiring`**, and nothing
points back up. `model/` imports no store; `grounding/` imports no store and no
retriever; `answer/pipeline.py` imports no concrete store. This is not a
convention — six of these arrows are entries in the boundary manifest (§4.6) and
fail a suite when broken.

### 3.3 Configuration and path anchoring (`F1`)

`app/config/paths.py`:

```python
REPO_ROOT = Path(__file__).resolve().parents[2]   # config -> app -> dev
PUBLIC_STORE_DIR      = REPO_ROOT / "data" / "corpus_public"
WORKPRODUCT_STORE_DIR = REPO_ROOT / "data" / "corpus_workproduct"
OPS_STORE_DIR         = REPO_ROOT / "data" / "ops"
FIXTURE_ROOT          = REPO_ROOT / "fixtures"
```

`os.getcwd()`, `Path(".")` and relative store paths appear nowhere; the
structural checker asserts it (`AC-F1-03`, `AC-F2-05/08`). `os.environ` is read
in `app/config/settings.py` and nowhere else (`AC-F1-05`, checker rule kind 2).
Config is a pydantic model with `extra="forbid"`, so an unknown key fails
startup naming the key (`AC-F1-04`), and every missing required key is listed
individually rather than the first one aborting (`AC-F1-01`). Startup prints the
resolved absolute store paths and the `LIVE_FETCH` mode (`AC-F1-06`).

---

## 4. The two-corpus ethical wall — the most important design in the project

Four independent mechanisms, deliberately layered so that no single one is the
wall. In order of strength: **separate databases** → **separate credentials** →
**separate types** → **statically-checked import closure with negative
controls**.

### 4.1 Physical separation

Two SQLite database files, in two directories, with two schemas created by two
calls, containing no cross-database references and no `ATTACH` anywhere in the
codebase (checker rule: the literal `ATTACH` may not appear in `app/`). Not two
tables, not two collections, not one file with a `visibility` column — there is
no `visibility` column, and `AC-F4-04`/`AC-F21-06` are checked twice: statically
over the schema module, and dynamically over `PRAGMA table_info` for every table
in both stores.

`OpsStore` is a **third** database and is deliberately not a corpus store: it
holds `IngestRun`, `QuarantineRecord` and `QueryRecord`. Rationale — a
`QuarantineRecord` for a protected document carries `evidence` (the marking text
that triggered it), and `AC-F10-01` requires nothing derived from that document
to exist in **any corpus store**. Putting quarantine records in a corpus store
would put a protected document's own text inside the corpus, which is the exact
state quarantine exists to prevent. Two constraints follow and are handed to
`security-architect` in §15: `QuarantineRecord.evidence` is capped at 512
characters and holds only the marking text or the response signature, never a
document body; and `QueryRecord.verified_sources[]` stores work-product entries
as `(corpus, doc_id, locator)` **references only**, never title or quote.

### 4.2 Credential separation

```python
class StoreCredential:            # opaque; __repr__ redacts; never logged
    def fingerprint(self, salt: bytes) -> bytes: ...   # HMAC-SHA256

def open_store(db_path: Path, credential: StoreCredential) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    row = conn.execute("SELECT salt, fingerprint FROM store_identity").fetchone()
    if row is None or not hmac.compare_digest(credential.fingerprint(row.salt), row.fingerprint):
        conn.close()
        raise StoreAuthenticationError(f"credential does not authenticate {db_path.name}")
    return conn
```

Each store file carries a `store_identity` row written at `init-stores` time from
its own credential. Using the public credential against the work-product store
raises `StoreAuthenticationError` before any usable handle exists — `AC-F21-02`
observably satisfied. The two credentials come from two distinct config keys
(`RCA_PUBLIC_STORE_SECRET`, `RCA_WORKPRODUCT_STORE_SECRET`) held in two distinct
typed config objects; there is no config object that holds both, and
`compose_root.py` is the only module that sees both (§4.5).

**Honest limitation, stated rather than buried.** This is an *application-level*
credential gate, not at-rest encryption: a process with filesystem access can
open the file with plain `sqlite3` and bypass it. The threat model this MVP1
actually faces is a code path taken in error, not an attacker with local disk
access — and `ASM-20` puts nothing but synthetic data in the work-product store.
So the control matches the threat, and the gap is named rather than implied.
`SQLCipher` is the drop-in upgrade behind the unchanged `open_store` signature
and is recorded in §15 as a **precondition of `F54`** (any real work product),
alongside `chmod 0700` on both store directories at `init-stores`.
`security-architect` may amend or harden this at the joint gate; if we disagree,
the disagreement is surfaced to the human rather than resolved between us.
`ASA-4`.

### 4.3 Type separation — no string-keyed anything (`AC-F21-07`)

`PublicStore` and `WorkProductStore` are two classes in two modules, each
constructed from **its own config type**:

```python
class PublicStore:
    def __init__(self, config: PublicStoreConfig) -> None: ...
class WorkProductStore:
    def __init__(self, config: WorkProductStoreConfig) -> None: ...
```

There is no `get_store(corpus)`, no `STORES: dict[str, Store]`, no
`store_for(corpus: Corpus)`. The `Corpus` enum exists **only** as a label on
records and on `Source` subtypes; it is never a selector. Three checker rules
enforce this (§4.6, rule kind 3):

- no function in `app/stores/` or `app/retrieval/` may take a parameter
  annotated `str`, `Corpus`, or named `corpus`/`corpus_name`/`store_name`;
- no dict literal anywhere in `app/` may have a store or retriever class as a
  value;
- no `getattr(` call in `app/session/` or `app/answer/`.

Negative control `AC-F22-06`: a fixture session exposing
`retriever_for(corpus: str)` must make the rule fail.

### 4.4 Session binding — construction, not selection (`ASM-UX-6` decided here)

```python
class PublicOnlySession:                       # the shape F24 will take
    def __init__(self, public: PublicRetriever) -> None:
        self.public = public
    # there is no .work_product attribute, and no method that could produce one

class UtilityAnalystSession:                   # the ONLY role MVP1 ships
    def __init__(self, public: PublicRetriever, work_product: WorkProductRetriever) -> None:
        if work_product.document_count() == 0:
            raise WorkProductCorpusMissingError(...)   # AC-F23-06
        self.public = public
        self.work_product = work_product
```

**Decision on `UX_KB` §9.4 item 1 (`ASM-UX-6`): MVP1's session is bound to both
corpora.** `PLAN.md` §3.3 is explicit that the wall is not between a utility
analyst and their own historical files, and `AC-F36-08` requires a work-product
citation card to be reachable. So the app-bar chip reading *"public + internal
corpora"* stands as designed, and the work-product card variant is a live code
path, not a spare part. `ui-ux-designer`'s open item is closed by this
paragraph; nothing in `design-review/` needs to change.

Neither session type has a method that takes a corpus name and returns a
retriever (`AC-F22-02`). Reaching the work-product corpus through a
`PublicOnlySession` fails as `AttributeError` — not an empty result, not a
filtered view (`AC-F22-04`). The role comes from a `CHECK`ed config enum, and an
unknown role fails startup rather than defaulting (`AC-F22-08`).

### 4.5 The composition root — the one place both corpora meet

`app/wiring/compose_root.py` is the **only** module in the codebase whose import
closure contains both stores. It constructs both credentials from both config
sections, both stores, both retrievers, and the session. Everything else takes
what it is given. This is what makes the boundary assertions below meaningful:
they are not "nobody happens to import that", they are "the graph has exactly
one join, and it is named."

### 4.6 The static import-boundary assertion (`AC-F22-03`, `AC-F22-05`)

The requirement is a **static** assertion over the **transitive** import closure.
Design:

`app/boundaries.py` is a machine-readable manifest — data, not code — with three
rule kinds:

```python
BOUNDARIES = (
    Boundary(
        name="public-answer-path",
        roots=("app.answer.public_path", "app.answer.pipeline", "app.session.public_only"),
        forbidden_modules=("app.stores.workproduct_store",
                           "app.retrieval.workproduct_retriever",
                           "app.stores.sqlite_engine"),          # reached only via a store
    ),
    Boundary(name="grounding-is-store-free",
             roots=("app.grounding.compose", "app.grounding.verify"),
             forbidden_modules=("app.stores.*", "app.retrieval.*")),
    Boundary(name="web-never-writes",
             roots=("app.web.main",),
             forbidden_modules=("app.ingest.writer", "app.grounding.compose")),   # AC-F35-08, AC-F35-07
    Boundary(name="job-never-answers",
             roots=("app.jobs.ingest",),
             forbidden_modules=("app.answer.*", "app.grounding.compose", "app.web.*")),  # AC-F42-07
    Boundary(name="fixture-transport-is-offline",
             roots=("app.acquisition.fixture_transport",),
             forbidden_modules=("httpx", "urllib.request", "http.client", "requests",
                                "app.acquisition.live_transport")),               # AC-F5-01
    Boundary(name="sentinel-path-is-bare",
             roots=("app.grounding.sentinel", "app.model.content"),
             forbidden_modules=("*",),                                            # zero imports
             forbidden_symbols=("re", "lower", "upper", "casefold", "find",
                                "index", "match", "search", "fullmatch", "sub")), # AC-F31-12
    Boundary(name="env-read-once",
             roots=("app",), forbidden_symbols=("os.environ", "os.getenv"),
             except_modules=("app.config.settings",)),                            # AC-F1-05
)
```

The checker (`tools/structural_checks/closure.py`):

1. **Parses, never imports.** `ast.parse` on each file; resolves `Import` and
   `ImportFrom` (including relative) to files inside the package; recurses to a
   fixed point. Importing to inspect would execute module bodies and would make a
   *runtime* check out of something the criterion requires to be static.
2. **Closes the dynamic-import escape hatch.** A static closure can be evaded by
   `importlib.import_module("app.stores.workproduct_store")`. So the checker also
   fails if any module in a boundary's closure references `importlib`,
   `__import__`, `eval`, `exec`, or subscripts `globals()`/`sys.modules`. A
   static boundary check that ignores dynamic imports is a boundary check with a
   hole in it, and this is where that hole gets closed.
3. **Is a pure function of a package root path**:
   `check(package_root: Path, boundaries) -> tuple[Violation, ...]`. This is the
   design decision that makes the negative control cheap and non-destructive:
   `AC-F22-05` points the same function at
   `tests/negative_controls/wall_breach/` — a tree containing a mutated copy of
   `public_path.py` that imports the work-product store — and asserts the
   function returns a violation. **No mutation ever touches `app/`.**
4. Reports violations as a **path through the graph**
   (`app.answer.public_path → app.retrieval.x → app.stores.workproduct_store`),
   because a boundary failure that does not say *how* the module was reached is a
   failure someone will paper over with an unrelated edit.

**Ownership, stated so two agents do not assert the same thing twice.** The
checker *library* is shipped code (`code-agent`). The *wall assertions* belong to
the **security suite** (`F46`, `security-architect`) — `AC-F46-03`, `AC-F46-08`.
My **architecture suite** asserts the layer beneath: that the manifest covers
every boundary this KB claims, that the checker detects a breach in each of the
seven boundaries (seven negative controls, not one), and that the dynamic-import
hatch is closed. The security suite tests the wall; I test the instrument.

---

## 5. Ingestion — seven stages, and why the ordering is a type, not a convention

### 5.1 Acquisition, adapters and the `LIVE_FETCH` flag

```python
class Transport(Protocol):
    def get(self, url: str) -> RawResponse: ...

class DocketAdapter(Protocol):
    jurisdiction: JurisdictionCode
    def validate_docket_number(self, raw: str) -> DocketNumber: ...   # rejects other formats
    def discover(self, docket: DocketNumber) -> tuple[IndexEntry, ...]
    def fetch(self, entry: IndexEntry) -> RawResponse
```

Three adapters (`pa_puc`, `puct`, `cpuc`) implement it identically, so a fourth
jurisdiction is a new module and a registry entry, never an edit to the pipeline
(`AC-F5-07`). Transport is **injected**, and the default is `FixtureTransport`,
whose import closure contains no HTTP client at all (§4.6). That is why
`AC-F5-01` — "an attempted outbound request raises an error naming the
`LIVE_FETCH` flag" — is structural: with the flag off there is no HTTP client in
the process to make a request with.

`LiveTransport.__init__` requires, per jurisdiction in scope, a non-null
`terms_of_use_reviewed_at` **and** `crawl_policy`, and raises naming the
jurisdiction and the missing field otherwise (`AC-F5-03`, IND-18) — the ToU
review is a construction precondition, not a warning.

Fixtures: `fixtures/http/<sha256(url)>.json` carrying
`{url, status, content_type, retrieved_at, body_b64}`; replay is byte-identical
(`AC-F5-04`); a missing fixture raises naming the URL **and** the expected
fixture path, never an empty body (`AC-F5-06`).

### 5.2 Quarantine is a return type, not a flag

Every stage returns a **union**:

```python
StageResult = Ok[T] | Quarantined | GateFailure
```

`Quarantined` carries a `QuarantineReason` from the closed set plus capped
`evidence`; `GateFailure` is the subset of reasons that make the whole run
`FAILED` (§10.1). Neither has any constructor path towards the next stage's
input type, so a quarantined item cannot continue by omission — only by someone
writing a conversion that does not exist.

### 5.3 The typed stage chain — `AC-F10-09` as a type-level property

```
IndexEntry
  ─fetch/sanity─▶  SaneDocument          (F9  : login page / 403 / HTML error / zero-length / type mismatch)
  ─classify────▶  ClassifiedDocument     (F10 : index marking + first-page scan; UNKNOWN quarantines, FDA-6)
  ─extract─────▶  ExtractedDocument      (F11 : page always; lines / schedule / finding where present)
  ─doc type────▶  TypedDocument          (F12 : 14-value enum + exhibit parent binding)
  ─case meta───▶  AssembledCase          (F13 : per-case extraction; never the jurisdiction default)
  ─outcome gate▶  GatedCase              (F15 : DECIDED/SETTLED_APPROVED with no outcome doc => GateFailure)
  ─claims──────▶  IngestableCase         (F14/F16/F17/F18)
                        │
                        ▼
              writer.write_case(case: IngestableCase)     ← the ONLY store-write call site
```

`ClassifiedDocument` is constructible only with
`confidentiality ∈ {PUBLIC, REDACTED_PUBLIC}`, and every later type requires a
`ClassifiedDocument` upstream. `write_case` accepts **only** `IngestableCase`.
Therefore "confidentiality classification completes before the first write to any
corpus store" is enforced by the type graph, not by the order of lines in a
function — which is the strongest available answer to `AC-F10-09`, and it stays
true when someone later reorders the pipeline.

Redacted/unredacted pairs: the classifier prefers the redacted member and
quarantines the unredacted one; de-duplication is defined to resolve **toward
the redacted record**, never away from it (`AC-F10-03/04`). The first-page
marking scan is scoped to page 1 and index metadata, so incidental body prose on
page 5 does not quarantine a legitimate order (`AC-F10-07`, FDA-7).

### 5.4 Extraction and locators (`F11`)

PDF via `pypdf` in `extraction_mode="layout"`, which preserves horizontal
position so the left-margin printed line numbers of pre-filed testimony survive
as text. Line-numbering is *detected* (a page is line-numbered when ≥80% of its
physical lines begin with a monotonically increasing small integer); when
detection fails the document is page-located only, which is exactly what
`AC-F11-02` requires ("where the document is line-numbered"). CPUC `.docx` via
`python-docx`, which preserves table structure so a row label and its numeric
value land in the same chunk in reading order (`AC-F11-07`) — this is the real
advantage `PLAN.md` §7.6 and INDUSTRY §6.1 flagged, and the CPUC adapter prefers
`.docx` when both representations exist (`AC-F8-02`).

A document yielding no text anywhere, **or text for some pages and none for
others**, is quarantined `NO_EXTRACTABLE_TEXT` and never OCR'd (`AC-F11-04/05`,
ASM-10). If `pypdf` layout mode proves insufficient on the curated corpus, the
named fallback is `pdfplumber` — and per my own contract that is a gap
`code-agent` **reports**, not one it swaps in silently.

### 5.5 Deterministic claim extraction (`F14`) — no model in the ingest path

`app/ingest/claims.py` is a rule-based extractor over a curated
`ClaimPattern` registry: per `parameter`, a set of anchored regexes plus a
required unit cue, a status cue, and a scope cue, each pattern carrying the
capture group that becomes `verbatim_quote` **and its character offsets in the
chunk**. Consequences:

- A claim always carries the span it came from, so `AC-F14-13` / `AC-F4-07`
  ("the quote is found in the chunk") is true by construction rather than by
  luck.
- `GROSS_PLANT`, `NET_PLANT` and `RATE_BASE` have three distinct pattern sets and
  no derivation between them; the same for `REVENUE_REQUIREMENT_TOTAL` vs
  `_INCREASE` (`AC-F14-03/04`, DOMAIN §4.2–§4.3).
- "reduced ROE by 25 basis points" requires the `BASIS_POINTS` cue to be present
  in the matched span; without an explicit unit cue **no row is written**
  (`AC-F14-05`, DOMAIN §4.4).
- Anything outside the eight parameters produces no row and remains retrievable
  text (`AC-F14-02`, ASM-8).
- **A pattern that does not resolve writes no row and one
  `IngestRun.failures[]` entry naming the document and parameter** — the third
  state (`AC-F14-11`), structurally distinct from the black-box `NOT_STATED` row
  (`AC-F14-10`), which is written from an *affirmative* silence pattern in the
  settlement text and carries the settlement's own quote.

Where the rules cannot reach, curation does: `fixtures/corpus/<case>/claims.yaml`
carries hand-verified rows (ASM-6's "verified against the source by hand once and
frozen"). **Curated rows are not privileged**: every one is re-verified at ingest
against the extracted chunk text, and a curated row whose quote is not found
fails ingest. So even hand-entered data cannot introduce an unsupported number.

`tools/propose_claims.py` is an **offline** curation aid that may call a model to
draft candidate rows for a human to review and commit. It is not importable from
`app/` (checker rule), never runs in the job, and its output is reviewed data,
not extraction. `ASA-5`.

---

## 6. Data model and storage

### 6.1 Which database holds what

| Records | Store | Why |
|---|---|---|
| `Case`, `Document`, `Chunk`, `Claim`, `Jurisdiction` | `public.sqlite3` **or** `workproduct.sqlite3` | The corpora. Never both; the `corpus` column is a label, not a filter (§4.1). |
| `QuarantineRecord`, `IngestRun`, `QueryRecord` | `ops.sqlite3` | §4.1 — quarantine evidence must not live inside a corpus, and provenance spans both. |

### 6.2 Record types and enum enforcement

Records are pydantic v2 models, `frozen=True`, `extra="forbid"`, every
status-bearing field a `StrEnum` with a `NOT_STATED` member and **no**
`Optional[...]` (`AC-F3-04/06`). `extra="forbid"` is what closes the
malformed-key gap `policy-lookup-assistant`'s KB identified and deferred — with a
machine-populated multi-jurisdiction corpus, an unknown key silently becoming
extra metadata is not an acceptable trade (`AC-F3-03`). Enum members are matched
exactly: `"final_order"` and `" FINAL_ORDER "` both fail, with no trimming or
case-normalising anywhere in the validator (`AC-F3-07`).

Every enum column additionally carries a SQL `CHECK (col IN (...))` generated
from the same Python enum, so the constraint holds against any writer, including
a future migration script.

### 6.3 Three storage-shape refinements — declared, not slipped in

`PLAN.md` §4 prescribes field **names**, and storage technology is explicitly my
call. Three places where I store the same facts in a shape that makes a
`PLAN.md` invariant unrepresentable rather than merely validated. Field names and
semantics are unchanged; the model layer exposes exactly what §4 names.

1. **Supersession is one edge row, not two mirrored columns.**
   `supersession(superseded_doc_id, superseding_doc_id)` with `UNIQUE` on both
   columns and `CHECK` that both resolve to the same `case_id` (`AC-F16-05`).
   `Document.supersedes_doc_id` and `.superseded_by_doc_id` are **views** over
   that edge. A one-sided link is therefore not a validation failure — it is not
   expressible (`AC-F4-03`). `chunk.superseded` stays denormalised and explicit
   `false` (`AC-F16-02/06`).
2. **`document.confidentiality` carries `CHECK (confidentiality <> 'PROTECTED')`.**
   The enum member exists so a `QuarantineRecord` can state a reason; the store
   cannot hold a protected row wearing a flag (`AC-F4-05`).
3. **The `AUTHORIZED` invariant is a trigger as well as a Python gate.**
   ```sql
   CREATE TRIGGER claim_authorized_guard BEFORE INSERT ON claim
   WHEN NEW.claim_status = 'AUTHORIZED' AND NOT EXISTS (
     SELECT 1 FROM document d JOIN "case" c ON c.case_id = d.case_id
     WHERE d.doc_id = NEW.doc_id
       AND d.document_type IN ('FINAL_ORDER','ORDER_ON_REHEARING')
       AND c.case_status = 'DECIDED')
   BEGIN SELECT RAISE(ABORT, 'AUTHORIZED invariant: ...'); END;
   ```
   The Python gate gives the error message `AC-F14-08` asks for ("naming the
   invariant"); the trigger makes the invariant a property of the *store*
   regardless of which code path writes. `RCA-R1` becomes unrepresentable rather
   than tested-for (`AC-F14-08/09`, `AC-F15-05`).

### 6.4 Numbers are stored as text

`claim.value_text TEXT` (the decimal exactly as stated) plus
`claim.value_num REAL` **for range filtering only**. Every equality comparison —
extraction round-trip, citation verification — uses `Decimal(value_text)`.
Floating-point equality has no place anywhere near `AC-F30-06/07`, and storing
the stated form also preserves "9.50" vs "9.5" for verbatim rendering. The
`(value, unit, scope, basis)` tuple is compared as a unit; there is no code path
that compares value alone.

### 6.5 Configuration-bound thresholds

`corpus_stale_days` (default 30) and `vintage_years` (default 5) live in config,
never as literals (`AC-F32-05`, `AC-F39-02`, ASM-17). `max_evidence_per_corpus`
(default 6) and the CPUC per-proceeding document cap (`AC-F8-04`) likewise.

---

## 7. The answer path

### 7.1 Steps, and where each can refuse

```
question ──▶ question.validate()            empty/whitespace ──▶ rejected before anything runs (F49)
         ──▶ frame.parse()   [MODEL #1]     ParseFailure     ──▶ REFUSED_PARSE_FAILED   (no retrieval at all)
         ──▶ per-corpus path: filter ──▶ rank ──▶ comparability ──▶ CoverageLedger
         ──▶ sufficiency (deterministic)    empty included   ──▶ REFUSED_INSUFFICIENT   (names the dimension)
         ──▶ compose()      [MODEL #2]      sentinel / schema ─▶ REFUSED_INSUFFICIENT / _VERIFICATION_FAILED
         ──▶ verify()       (pure)          any check fails  ──▶ REFUSED_VERIFICATION_FAILED (whole answer discarded)
         ──▶ QueryRecord write             failure           ──▶ SystemError (FDA-4)
         ──▶ Answer
```

`frame.parse()` returns `QueryFrame | ParseFailure`, and `retrieve()` accepts
only `QueryFrame` — so "a parse failure falls back to a keyword search" is not
expressible, and `AC-F25-03` (`retrieved_chunk_ids` empty) holds because
retrieval was never reachable. No keyword-search module exists in §3.1 at all.

### 7.2 Retrieval (`F26`) — metadata first, similarity second

```python
candidate_ids = store.filter_chunks(predicate_from(frame))   # SQL over denormalised chunk columns
ranked        = rank_within(candidate_ids, embed(question), k)
```

`filter_chunks` is called **exactly once** per query; there is no retry loop and
no relaxation path (`AC-F26-03`; checker rule: no loop in `app/retrieval/` may
contain a call to `filter_chunks`). Denormalised chunk columns (`case_id`,
`jurisdiction_code`, `document_type`, `authority_rank`, `order_date`,
`market_structure`, `test_year_convention`, `case_type`, `case_status`,
`superseded`, `corpus`) are what make the filter applicable at the boundary
rather than as a post-hoc join (`AC-F4-02`). A frame seeking `AUTHORIZED`
constrains `document_type` to the four outcome types before ranking
(`AC-F26-07`). Date-window bounds are inclusive at both ends (`AC-F26-04`).

### 7.3 Evidence identity — the model never sees a real id

Retrieved evidence is packed into an `EvidenceBundle` that maps **ordinals**
(`E1…En`) to typed `EvidenceId(corpus, chunk_id)`. The model is shown only the
ordinals. Two consequences: a fabricated evidence id cannot accidentally resolve
to a real record, and `AC-F30-01` ("cited an id not supplied") reduces to an
integer set-membership test. Work-product and public evidence are ordinally
indistinguishable to the model, which is correct — the analyst legitimately uses
both, and the corpus label is stamped by the path (§7.4), not chosen by the
model.

### 7.4 Deterministic citation verification (`F30`) — the ASM-3 step

```python
def verify(composition: Composition,
           supplied: EvidenceBundle,
           claims: ClaimLookup) -> VerifiedCitations | VerificationFailure
```

A **pure function**: no store handle, no model client, no network. All record
reads happen upstream into `EvidenceBundle`/`ClaimLookup`, which is what makes
the whole of `F30` unit-testable without a corpus and makes `AC-F30-09`
provable — because:

```python
def build_sources(verified: VerifiedCitations) -> tuple[Source, ...]
```

takes **exactly one parameter**, and the retrieval result set is not in its
scope. That signature is the entire content of the deviation from
`policy-lookup-assistant`, whose accepted trade-off was `sources[] = what
retrieval pulled`. Per DOMAIN §6.8(c) the most dangerous hallucination kind is a
real quote from a real source that does not support the proposition; showing
retrieval hits beside a claim manufactures the appearance of support. Closed
here, structurally, in a function signature a checker can read.

Checks, in order, all-or-nothing:

| Check | Mechanism | Criterion |
|---|---|---|
| (a) evidence id was supplied | ordinal ∈ bundle | `AC-F30-01` |
| (b) quoted span verbatim in that chunk | `normalise()` both sides, then `in` | `AC-F30-02/03` |
| (c) asserted `document_type`/`claim_status` match the stored record | enum equality | `AC-F30-04/05` |
| (d) numeric assertion matches the stored `Claim` | exact tuple equality on `(Decimal(value_text), unit, scope, basis)` | `AC-F30-06/07` |

`normalise()` performs NFKC, whitespace-run collapse, soft-hyphen removal and
line-break-hyphen joining — **and nothing else**. No case folding, no punctuation
stripping, no stemming, no fuzzy or semantic matcher, and **no unit converter
exists anywhere in `app/`** (checker rule: the symbols `convert`, `to_percent`,
`to_basis_points` may not appear in `app/grounding/`). FDA-8's 950 bp asserted
against a stored 9.50 % therefore fails, because nothing in the process knows how
to make them equal.

**Any single failure discards the entire answer** (`AC-F30-11`) — verification
returns a `VerificationFailure` and there is no code path that removes an
assertion and serves the rest, because `Answer` is constructible only from a
complete `VerifiedCitations`. `Answer.__init__` is private (guarded by a module
sentinel) and reachable only from `verify.build_answer`, which is also how
`AC-F35-07` is satisfied: no route can render prose that did not pass.

Sources are typed per corpus — `PublicSource` and `WorkProductSource`, with
`corpus` a read-only class property. `public_path.py` can emit only
`PublicSource`, so `AC-F22-07` holds by construction and a mislabelled record in
the store cannot spoof a corpus label.

### 7.5 The sentinel (`F31`) — a module with no imports

```python
# app/grounding/sentinel.py   — zero imports, one literal, one operation
INSUFFICIENT_EVIDENCE = "INSUFFICIENT_EVIDENCE"

def is_refusal(content: str) -> bool:
    return content.strip().startswith(INSUFFICIENT_EVIDENCE)
```

`AC-F31-12` requires that **no regex, case-fold or substring operation exists
anywhere in the sentinel path**, statically. That is achievable only if the path
is small enough to close: the boundary manifest declares the sentinel path to be
exactly `{app.grounding.sentinel, app.model.content}`, both with an empty import
closure and neither containing any of `re`, `lower`, `upper`, `casefold`, `find`,
`index`, `match`, `search`, `sub`, or an `in` test against the literal. `content`
is in the path because `AC-F49-04` requires the sentinel to survive a
list-shaped model response, so the normaliser runs first and must be held to the
same standard; it joins content parts in order and returns `""` for an empty list
(`AC-F49-05`) using nothing but `str.join`.

The prompt module imports the constant rather than retyping the literal, so
there is exactly one occurrence of the token in `app/` outside the prompt text
it is interpolated into.

On refusal the model's prose is **discarded entirely** and replaced by a
product-controlled string from `app/grounding/refuse.py` composed of: the named
gap, the coverage statement, and the resolvable cases that *were* examined
(`AC-F31-04/05/06/07/08`). `Refusal` has **no `sources` field at all**, so
`AC-F31-11` ("`sources[]` is empty") is not a runtime check — there is nothing to
populate.

The deterministic sufficiency check runs **before** composition (`AC-F29-05`), so
the sentinel is a second line of defence covering the case where the model judges
supplied evidence insufficient, not the primary gate. Saying which is primary
matters: the primary refusal decision is ours and deterministic.

### 7.6 Provenance (`F34`) fails closed

The `QueryRecord` is written to the ops store **before** the response is handed
to the renderer. A write failure produces `SystemError` — the third response type
— rendered by the one `role="alert"` component in the product (`UX_KB` §7.1), and
visibly distinct from a refusal (`AC-F34-06`, `AC-F35-06`, `AC-F38-06`, FDA-4).
`verified_sources[]` is written from the same `VerifiedCitations` the response
carries, so `AC-F34-05` (trail == response) is one value used twice, not two
computations that must agree.

---

## 8. Comparability and coverage — invariants that are unrepresentable when violated

### 8.1 Comparability (`F27`) — a tagged union, not a record with a verdict field

`AC-F27-09` requires that a non-`COMPARABLE` verdict with empty `mismatched[]`
**and** empty `unknown[]` be unrepresentable, and that no scalar score field
exist. A single record with a `verdict` string and three lists cannot deliver
that — validation could be skipped. So the type is three types:

```python
NonEmpty[T]   # frozen wrapper; __post_init__ raises on len == 0

@frozen class Comparable:            matched: tuple[Dimension, ...]
                                     # NO mismatched field exists on this arm
@frozen class ComparableWithCaveats: matched: tuple[Dimension, ...]
                                     caveats: NonEmpty[Mismatch | Unknown]
@frozen class NotComparable:         matched: tuple[Dimension, ...]
                                     blocking: NonEmpty[Mismatch]   # each severity is BLOCKING
                                     caveats: tuple[Mismatch | Unknown, ...]

Comparability = Comparable | ComparableWithCaveats | NotComparable
```

The only way to obtain a non-`COMPARABLE` value is to hand the constructor at
least one **named** dimension; `NonEmpty` raises otherwise. `.verdict`,
`.mismatched` and `.unknown` are read-only properties so the serialised shape
`AC-F27-01` describes is unchanged for the renderer and the tests.

**No score, anywhere**: a checker rule forbids any `float`/`Decimal`-annotated
field and any field named `score`, `similarity`, `distance` or `confidence` in
`app/comparability/`. The similarity value from ranking never leaves
`app/retrieval/rank.py` — it is an ordering key, not a datum, and is not carried
on any evidence or comparability object. That is the design answer to the gate-1
finding: *if the architecture treats comparability as a retrieval-ranking
problem, it has built harm #1.*

Dimensions and severities are implemented exactly as `PLAN.md` §3.7's table
states, in `app/comparability/dimensions.py`, including the two behaviours that
are easy to lose: `test_year_convention` escalates `CAVEAT → BLOCKING` when the
frame records that the question **named** a convention (`AC-F25-08` →
`AC-F27-05`), and a dimension the corpus records as `NOT_STATED` goes to
`unknown[]` and is **never** counted as matched (`AC-F27-10`). No text produced
anywhere asserts a settled-vs-litigated direction (`AC-F27-13`) — there is no
such string in `refuse.py` or in any template, and the industry suite scans for
it.

### 8.2 Coverage (`F28`) — a ledger that must balance before it can be sealed

`Coverage` has **no public constructor**. The only way to obtain one:

```python
ledger = CoverageLedger(candidates)          # immutable candidate tuple, fixed at construction
ledger.include(case_id)
ledger.exclude(case_id, dimension, reason)   # both NonEmptyStr
ledger.unassessable(case_id, reason)         # NonEmptyStr
coverage = ledger.seal()                     # raises unless every candidate is dispositioned exactly once
```

`seal()` raises `CoverageNotBalanced` if any candidate is undispositioned or
dispositioned twice, so `included + excluded + unassessable == candidates`
(`AC-F27-12`, `AC-F28-*`) cannot be false of any `Coverage` that exists. The
`NonEmptyStr` types make `AC-F28-08` ("no blank or placeholder reason")
structural. `UX_KB` §6.1's on-screen arithmetic reconciliation line therefore
displays an invariant, not a hope.

Merging across corpora: `Coverage.merge()` operates on two sealed objects over
**disjoint** candidate sets and re-runs the balance check, so the merge cannot
lose a candidate either.

`candidates_considered == 0` is a distinct state carried on the object, and the
renderer selects `.coverage-none` (the dashed, hatched band) rather than a
zero-length bar — `UX_KB` §6.1 calls this the single most important pixel-level
decision in the proposal, and it is the difference between `AC-F37-03` and
`AC-F37-04`. `STANDING_EXCLUSIONS` is a module constant asserted non-empty at
import, so `known_exclusions` cannot regress to empty (`AC-F28-06`,
`AC-F37-06`).

Both `Answer` and `Refusal` require `coverage: Coverage` — a refusal without
coverage is not constructible (`AC-F28-02/03/04`, `AC-F31-10`).

---

## 9. The web surface (surface 1)

### 9.1 Shape

Two routes. `GET /` renders the Ask screen; `POST /ask` runs the answer path and
renders the Answer screen. Nothing else is reachable from a browser. There is no
JSON endpoint, no `/api`, no partial-render endpoint — which is what makes
`AC-F35-07` structural rather than a matter of route discipline.

`app/web/**`'s import closure excludes `app/ingest/writer.py` (`AC-F35-08`: the
web surface performs no corpus write) and `app/grounding/compose.py`
(`AC-F35-07`: nothing but a verified `Response` reaches a template). Both are
boundary-manifest entries (§4.6).

### 9.2 Templates adopt `design-review/` directly

`design-review/assets/rca.css` is copied to `app/web/static/rca.css` **unchanged**
and the Jinja2 partials reproduce the class contract exactly: `.rca-appbar`,
`.rca-freshness[--stale|--never]`, `.rca-columns`, `.panel.answer-panel`,
`.coverage-strip`, `.coverage-bar`, `.coverage-none`, `.coverage-empty-note`,
`.citation-card[--position|--absent]`, `.authority-spine`, `.status-chip`,
`.dim-table`, `.refusal-panel`, `.refusal-gap`, `.syserror-panel`,
`.provenance-panel`, `.known-exclusions`. One partial per component, named for
its class. `code-agent` reads the twelve rendered pages as the reference; no
translation layer exists to lose an invariant in.

**The enum-gloss rule at the render boundary** (`UX_KB` §7.1, open item 2, a real
defect found at gate 5, not a hypothetical): `app/web/render.py` is the single
place enum values become display text, via an explicit `GLOSS` mapping. Any enum
literal containing "error", "failed" or "problem" — `IngestStatus.FAILED`,
`QueryOutcome.REFUSED_VERIFICATION_FAILED` — is glossed before it can reach a
template. The industry/UI suites scan the rendered refusal-panel subtree for those
three words, so an un-glossed enum fails a blocking suite. `AC-F38-02`.

### 9.3 Client JS

One file, ~40 lines, no framework, no build step: show the in-flight indicator on
submit (`AC-F35-03`) and block submission of an empty or whitespace-only question
(`AC-F35-02`, which requires that *no request is sent*). The server enforces the
same rule independently (`AC-F49-01/02`) — the client check exists to satisfy the
"no request" wording, the server check is the actual guard. With JS disabled the
form still posts and the server still refuses; nothing about correctness depends
on the browser.

No session history is rendered (`ASM-UX-2`); a second question replaces the first
answer entirely (`AC-F35-09`) — trivially true when each answer is a fresh page
render. There is **no chart or aggregate partial in the template set**
(`ASM-UX-11`), deliberately, so `F33` cannot be built by reaching for one that is
already there.

---

## 10. The scheduled job (surface 2), and the model/determinism split

### 10.1 The job is a genuine second surface

`python -m app.jobs.ingest` — headless, non-interactive, no server, no daemon.
It shares the §6 data model and `app/enums/` with the web surface **and nothing
else**: `app.jobs.ingest`'s import closure excludes `app/answer/**`,
`app/grounding/compose.py` and `app/web/**` (`AC-F42-07`), which is the mirror of
`AC-F35-08`. That pair of boundaries is what makes `PLAN.md` §3.1's claim — the
job runs to completion with no web surface, the web surface is testable with no
job — a checked property rather than a description.

**Exit-code semantics (FDA-3), as a total function of `IngestRun.status`**, which
is itself computed from the quarantine/gate split rather than assigned by hand:

| Condition | `status` | Exit |
|---|---|---|
| Any `GateFailure` — `MISSING_OUTCOME_DOCUMENT`, `UNRESOLVED_PARENT`, `ENUM_VALIDATION_FAILURE` | `FAILED` | non-zero |
| Only expected quarantines — `PROTECTED_MARKING`, `ACCESS_DENIED`, `NON_DOCUMENT_BODY`, `NO_EXTRACTABLE_TEXT` | `PARTIAL` | 0 |
| Nothing quarantined, no gate fired | `SUCCEEDED` | 0 |
| Terminated mid-run | `FAILED` with `finished_at` set; as-of date does not advance (`AC-F42-06`) | non-zero |

The run report is emitted twice from one structure: a JSON artifact for tests
(`AC-F43-08`) and a human-readable rendering matching `design-review/11-run-report.html`.
Zero counts are printed explicitly for **every** reason in the closed set — a zero
is stated, never an omitted section (`AC-F10-06`, `AC-F43-03`). One adapter failing
does not stop the others, and the run is then not `SUCCEEDED` (`AC-F42-08`).

`corpus_as_of` is the `finished_at` of the most recent `SUCCEEDED` run, read by
the web surface from the ops store; a `FAILED` or `PARTIAL` run never advances it
(`AC-F39-05`). `python -m app.jobs.healthcheck` reports a silent-stop condition
and exits non-zero when the last run of **any** status is older than twice the
schedule interval (`AC-F43-07`). Scheduling is `launchd` via
`deploy/com.rca.ingest.plist.template` — we ship a template and a command, not a
process of our own; process lifecycle belongs to `deploy-agent`.

Before any successful run, the web surface refuses and names that as the gap
(`AC-F39-04`, FDA-5) — the surface never answers over a corpus it cannot date.

### 10.2 Where the model is allowed, and where it is not

**The model is used in exactly two places, and this project's harms are
generation harms, so everywhere else is deterministic code.**

| Concern | Mechanism | Why |
|---|---|---|
| Question → `QueryFrame` (`F25`) | **Model**, forced tool use, closed schema | Natural-language understanding is genuinely what this is. Failure → `REFUSED_PARSE_FAILED`, never a fallback search. |
| Evidence → prose with citation tags (`F29`) | **Model**, forced tool use, closed schema | Writing readable prose over a *fixed* evidence set. The set is chosen before the call and cannot be widened by it. |
| Claim / case-metadata / doc-type extraction | **Deterministic** rules + curated frozen fixtures (§5.5) | An LLM extractor's failure mode is a confident wrong number in a numeric table; a rule extractor's failure mode is a *reported gap*, and `AC-F14-11` already gives that gap a first-class home. This is the single most consequential determinism call in the design. |
| Confidentiality classification (`F10`) | **Deterministic** marking scan | A probabilistic classifier here means a probabilistic privilege control. |
| Comparability (`F27`) | **Deterministic** predicate | Gate-1 binding finding. |
| Coverage (`F28`) | **Deterministic** ledger | An arithmetic invariant cannot be delegated. |
| Citation verification (`F30`) | **Deterministic**, pure | A verifier that can be talked out of a verdict is not a verifier. |
| Sentinel (`F31`) | **Deterministic**, two bare modules | `AC-F31-12`. |
| Retrieval filtering (`F26`) | **Deterministic** SQL | Similarity must never widen the set. |

Both model calls use Anthropic **forced tool use**, so output arrives as a
validated structure rather than prose to be parsed (`PLAN.md` §7.10). Failure
mapping, decided here because `PLAN.md` does not state it (`ASA-6`): a frame call
returning no tool use, or a schema-invalid frame → `REFUSED_PARSE_FAILED`; a
composition call returning neither the sentinel nor a schema-valid composition →
`REFUSED_VERIFICATION_FAILED`, because a malformed model response is not evidence
of an insufficient corpus and must not be reported to the user as one.

Model and embedding identities are configuration and are recorded on every
`QueryRecord.model_identifier` (`AC-F34-03`). Defaults: chat
`claude-sonnet-4-5`; embeddings `text-embedding-3-small` (1536-d, float32 blobs).
Embedding choice is deliberately low-stakes: because embeddings only *rank within*
an already-correct candidate set, embedding quality is an ordering concern, never
a correctness one — which is why swapping to the offline hashing embedder does
not change any correctness assertion.

### 10.3 Every suite runs offline (`AC-F2-07`)

Three flags, all default-off, each with a deterministic stand-in:

| Flag | Default | Off behaviour |
|---|---|---|
| `LIVE_FETCH` | off | `FixtureTransport`; no HTTP client is even imported (§4.6) |
| `LIVE_MODEL` | off | `TranscriptModelClient` replays recorded exchanges from `fixtures/transcripts/` |
| `EMBEDDINGS_PROVIDER` | `hash` | Deterministic stdlib hashing embedder; no API key needed |

`ModelClient` is a Protocol; the transcript client is the default in every suite.
This matters most for the **red-team suite**: scripting a model that emits a
fabricated docket number, a real quote attached to a false proposition, or a
refusal to emit the sentinel is *stronger* coverage than hoping a live model
misbehaves on the day, and it is reproducible. `LIVE_MODEL=1` remains available
for exploratory adversarial runs, which is where genuinely novel attacks come
from; both modes exist and neither is a substitute for the other. `ASA-7`.

---

## 11. Test harness layout (`F2`) — built from scratch

### 11.1 Entry points

`FUNCTIONAL_SPEC` `AC-F2-01` names five blocking suites by name. This design
ships **seven** entry points; the extra two are additive, blocking, and reported
by name in the aggregate run (`AC-F2-02`):

```
tests/suites/functional/run.sh    F44  — functional-agent
tests/suites/industry/run.sh      F45  — industry-expert
tests/suites/security/run.sh      F46  — security-architect
tests/suites/redteam/run.sh       F47  — responsible-ai-architect
tests/suites/ui/run.sh            F48  — ui-ux-designer (Playwright)
tests/suites/ux/run.sh                 — two-line shim: exec ../ui/run.sh
tests/suites/architecture/run.sh       — solution-architect (this agent)
tests/suites/unit/run.sh               — code-agent
tests/run_all.sh                       — per-suite result line; non-zero if any failed
```

The `ux` shim exists because `FUNCTIONAL_SPEC` binds the name `ui` while the
`ui-ux-designer` contract and `UX_KB` §10 name `dev/tests/suites/ux/run.sh`. Both
paths must resolve to the same run; a second, divergent UI suite is exactly the
kind of drift a second surface produces. `ASA-8`.

Harness properties that are themselves criteria: zero tests collected → non-zero
exit with a message (`AC-F2-03`); a collection/import error → non-zero, naming
the module (`AC-F2-04`); fixtures resolved by absolute path from `REPO_ROOT` so
the working directory is irrelevant (`AC-F2-05/08`); the `ui` suite exits
non-zero when the browser binary is absent rather than skipping (`AC-F2-06`).

### 11.2 Negative controls (FDA-2) — a design constraint on `code-agent`

Every guard must be removable **by substitution**, never by editing `app/`. Two
patterns, and no third:

1. **Static guards** (import boundaries, shape rules): the checker is a pure
   function of a package root, so a mutated fixture tree under
   `tests/negative_controls/<name>/` is checked without touching `app/`
   (`AC-F22-05`, `AC-F22-06`, `AC-F46-08`).
2. **Runtime guards** (the `AUTHORIZED` invariant, the metadata-first ranker, the
   sufficiency check, the `NOT_STATED` renderer): each is an injectable
   collaborator or a pure function, so a mutant is substituted at test time
   (`AC-F44-07/08`, `AC-F45-08`, `AC-F47-09`, `AC-F48-07`).

This is a real constraint on implementation, stated here so it is designed in
rather than discovered at the Test gate: **a guard implemented as an inline
conditional inside a large function cannot be negative-controlled, and is
therefore not an acceptable implementation of a guard.**

### 11.3 The architecture suite — what I own and execute

`dev/tests/suites/architecture/run.sh`, scoped to contract tests between
components and design-conformance checks over what was actually designed here:

| Scenario | Asserts |
|---|---|
| `ARCH-01` boundary-manifest completeness | Every boundary claimed in §4.6 exists in `app/boundaries.py`; no boundary in this KB is unmanifested |
| `ARCH-02` checker detects each breach | Seven negative-control trees, one per boundary; each must produce a violation |
| `ARCH-03` dynamic-import hatch closed | A fixture using `importlib.import_module` to reach the work-product store is detected |
| `ARCH-04` stage-chain contract | `writer.write_case` accepts only `IngestableCase`; no stage type is constructible from a `Quarantined`/`GateFailure` |
| `ARCH-05` `build_sources` arity | Exactly one parameter, typed `VerifiedCitations` (`AC-F30-09`) |
| `ARCH-06` comparability shape | No float field, no score-named field, `NonEmpty` enforced on both non-comparable arms |
| `ARCH-07` coverage ledger | `Coverage` has no public constructor; `seal()` rejects an unbalanced ledger |
| `ARCH-08` no string-keyed store/retriever factory | `AC-F21-07` shape rules |
| `ARCH-09` sentinel path is bare | Zero imports, zero forbidden symbols across both path modules |
| `ARCH-10` surface separation | `web` ⊅ writer/composer; `jobs` ⊅ answer/web |
| `ARCH-11` retriever/store protocol conformance | Both retrievers satisfy `EvidenceSource`; neither accepts a corpus argument |
| `ARCH-12` config/path anchoring | `os.environ` read in one module; no `cwd`-relative store path |
| `ARCH-13` scale/design conformance | Ranking is called with a bounded candidate set; `filter_chunks` called once per query, in no loop |

Evidence is written as structured per-scenario records under
`projects/rate-case-analyzer/test-evidence/` per `test-agent`'s documented
convention.

**Status of my suite as at 2026-08-07: `dev/tests/suites/architecture/run.sh`
does not exist** — `F2` builds the harness from scratch under the custom-template
override, and `dev/` holds only `README.md` and `.gitignore`. Nothing in this
document is a test result. When the entry point lands, every scenario above is
**run for real**; none is waved through on the strength of this design pass.

---

## 12. Impact Analysis — MVP1 initial build

**Mandatory on this project** (two surfaces). This enumerates the surfaces the
*project* has, not the ones this change happens to touch. Because MVP1 is the
initial build, most rows are "reached" — the value of the section here is the
baseline: it fixes the surface list every later enhancement must enumerate
against, so a surface can never be omitted later by never having been listed.

### 12.1 Surfaces this project has

| # | Surface | Reached by MVP1? | Justification |
|---|---|---|---|
| S1 | **Desktop web** (`app/web`, Ask + Answer screens, twelve designed states) | **REACHED** | `F35`–`F40`, `F34`'s provenance panel. Every rendering invariant in `UX_KB` §5–§7 is implemented here for the first time. |
| S2 | **Scheduled ingestion job** (`app/jobs`, run report, exit codes, health check) | **REACHED** | `F42`, `F43`. Ships and fails independently of S1; owns `corpus_as_of`, which is S1's only symptom of a silently-stopped job. |
| S3 | **Public API / integration surface** | **NOT REACHED — and deliberately does not exist.** | The web surface is server-rendered; there is no JSON route, no `/api`, no partial-render endpoint (§9.1). `AC-F43-08`'s machine-readable run report is a **file**, not an endpoint, so it creates no network contract. Falsifiable: enumerate the routes registered on the FastAPI app — if any returns JSON to a client, this row is wrong and a third surface exists. Adding one later is a **surface addition** requiring a new Architecture pass, not a feature. |
| S4 | **Corpus data stores** (`public.sqlite3`, `workproduct.sqlite3`, `ops.sqlite3` + the frozen fixture corpus) | **REACHED** | `F3`, `F4`, `F21`, `F23`. Schema, credential gate, triggers, and the 12-case curated baseline all originate here. Any later schema change reaches this surface and requires re-ingestion, which is precisely why `PLAN.md` put RCA-R4/R11/R13 in the MVP1 schema. |
| S5 | **Deliverables** — `design-review/`'s twelve pages + `rca.css`, and the KB set (`ARCHITECTURE_KB`, `UX_KB`, `FUNCTIONAL_SPEC`, `PLAN`, `FEATURES`) | **REACHED** | `rca.css` is **copied into the running product** (§9.2), so `design-review/` stops being a mockup and becomes a source artifact with a live consumer. That is a drift risk with a name: if a template diverges from the design-review page it was derived from, the deliverable silently starts describing a product that no longer exists — the F18 failure this contract's rule was written after. Mitigation in §12.3. |
| S6 | **Mobile** | **NOT REACHED — no mobile surface exists.** | `PROJECT_CONTEXT.md` puts mobile out of MVP scope and `FEATURES.md` carries no mobile item; `UX_KB` §4 designs desktop-only and says so. Nothing in this design emits a mobile artifact, and the CSS degrades in a narrow window without that being claimed as a design target. Falsifiable: if a responsive layout or a mobile client is ever added, this row becomes a reached surface and this analysis is stale. |

Six rows, six justifications. No surface is left implicit, and the two "not
reached" rows carry the reason they are not reached rather than the word
"unaffected".

### 12.2 What must be re-tested, per reached surface

Concretely enough for `test-agent` and the suite owners to act on. Because this
is the initial build, "re-test" means "the Test gate must show evidence from
each of these, and the gate does not close on a subset."

| Surface | Evidence the Test gate must show |
|---|---|
| **S1 desktop web** | `ui` suite (`F48`) green on the **real rendered surface** via Playwright — the four invariants plus `AC-F48-07`'s negative control. Additionally the `industry` suite's rendered-surface assertions (`AC-F45-03` `NOT_STATED` visible as words; `AC-F45-04` non-precedent quote visible; `AC-F45-05` date on every citation). **A UI suite that passes by skipping when the browser binary is missing is a failed gate** (`AC-F2-06`). |
| **S2 ingestion job** | An end-to-end fixture run producing all three statuses: a clean `SUCCEEDED`/0, a `PARTIAL`/0 with at least one protected-marking and one non-document quarantine, and a `FAILED`/non-zero from a gate. Plus incremental behaviour (`AC-F42-03/04/05`), mid-run termination (`AC-F42-06`), one-adapter-fails (`AC-F42-08`), and the silent-stop health check (`AC-F43-07`). Exit codes asserted, not just report text. |
| **S4 data stores** | `security` suite store/credential separation (`AC-F46-01/02`) and the no-`visibility` scan run **dynamically over `PRAGMA table_info` of both live stores**, not only statically over the schema module. Plus write-time invariants exercised against the real database: `AUTHORIZED` trigger (`AC-F14-08/09`), protected-document `CHECK` (`AC-F4-05`), supersession same-case `CHECK` (`AC-F16-05`), round-trip of every field (`AC-F4-01`). |
| **S5 deliverables** | A **drift check**: the class names used by the shipped Jinja2 partials are a subset of those defined in `app/web/static/rca.css`, and that file is byte-identical to `design-review/assets/rca.css`. Owned by the `architecture` suite (`ARCH-14`, added below). Plus: `UX_KB` §10 and this KB's change history must be updated in the same pass as any change to the rendered states — a deliverable fifteen days stale describing a product that has moved is the defect this rule exists to stop. |
| **Cross-surface** | The two surface-separation boundaries (`AC-F35-08`, `AC-F42-07`) are the contract *between* S1 and S2 and are asserted in the `architecture` suite (`ARCH-10`), because neither surface's own owner is well placed to notice the other's encroachment. |

`ARCH-14` (`design-review/` ↔ `static/rca.css` byte-identity and class-subset
check) is added to §11.3's scenario list by this section; the two lists are one
list.

### 12.3 The drift risk this design deliberately creates, and its control

Copying `rca.css` into the product makes S5 a live dependency of S1. That is a
real coupling and I am choosing it knowingly, because the alternative —
re-expressing the design in a second technology — loses invariants in
translation, which is a worse failure than staleness. The control is `ARCH-14`:
byte-identity, checked by a blocking suite, so the two copies cannot drift
silently. If a designer changes `design-review/`, the suite fails until the
product copy is updated, and vice versa. The coupling is made noisy on purpose.

---

## 13. Run commands for `deploy-agent` (local, macOS, no cloud)

From `projects/rate-case-analyzer/dev/`:

```bash
# 1. environment (once)
python3.12 -m venv .venv
.venv/bin/pip install -e ".[dev]"
.venv/bin/python -m playwright install chromium      # UI suite only

# 2. configuration
cp .env.example .env         # then fill: two store secrets, optional model keys
.venv/bin/python -m app.cli.show_config              # prints resolved absolute store paths + LIVE_FETCH mode

# 3. stores (once; creates both corpus DBs, the ops DB, chmod 0700 on store dirs)
.venv/bin/python -m app.cli.init_stores

# 4. corpora
.venv/bin/python -m app.jobs.ingest                  # fixture mode by default; exit code per FDA-3
.venv/bin/python -m app.cli.load_synthetic           # work-product store only

# 5. web surface  (LONG-LIVED — deploy-agent / orchestrator only, never a subagent turn)
.venv/bin/uvicorn app.web.main:app --host 127.0.0.1 --port 8420

# 6. operations
.venv/bin/python -m app.jobs.healthcheck             # non-zero on silent stop
bash tests/run_all.sh                                # all seven suites, blocking
```

No network access is required for steps 1–4, 6 (`pip install` excepted) with the
default flags. No Docker, no database server, no cloud credential, no node.
Scheduling, when wanted:
`cp deploy/com.rca.ingest.plist.template ~/Library/LaunchAgents/com.rca.ingest.plist`
with paths substituted, then `launchctl load`.

Per my own contract I have started no process and run no suite in this pass;
step 5 is long-lived and belongs to `deploy-agent`.

---

## 14. Assumptions taken at this gate

Numbered `ASA-*` so they do not collide with `ASM-*` (project), `FDA-*`
(functional design) or `ASM-UX-*` (experience design). Each is a judgment the
human would normally have made, taken under the recorded full-autonomy
instruction, and each is reversible.

- **ASA-1 · Server-rendered, no SPA.** §2.2(a). Cost: richer client
  interactivity for `F41`/`F51` will need more than 40 lines of JS; the mitigation
  is that an incremental island can be added without a rewrite.
- **ASA-2 · SQLite + numpy, no vector database.** §2.2(b). Cost: does not scale to
  six-figure filtered candidate sets; migration is one module (`rank_within`).
- **ASA-3 · No LangChain; direct Anthropic SDK.** §2.2(c). Cost: we own retry,
  timeout and content-shape handling — which `F49` says we should own anyway.
- **ASA-4 · Application-level store credentials, not at-rest encryption, in
  MVP1.** §4.2. Matches the threat model given `ASM-20` (synthetic work product
  only). SQLCipher recorded as a `F54` precondition. `security-architect` may
  amend at the joint gate; a disagreement is surfaced to the human, not settled
  between us.
- **ASA-5 · Deterministic extraction; the model may assist curation offline
  only.** §5.5, §10.2. The extractor's failure mode becomes a reported gap rather
  than a confident wrong number.
- **ASA-6 · Malformed model output maps to `REFUSED_VERIFICATION_FAILED`, not
  `REFUSED_INSUFFICIENT`.** §10.2. A broken response is not evidence that the
  corpus lacks material, and telling the user it is would be a false statement
  about the corpus.
- **ASA-7 · Suites drive a transcript-replay model client by default;
  `LIVE_MODEL=1` is available for exploratory red-teaming.** §10.3. Scripted
  worst-case model behaviour is reproducible and stronger; live runs remain the
  source of novel attacks. Both exist; neither replaces the other.
- **ASA-8 · Seven suite entry points, not five**, with `suites/ux/run.sh` as a
  shim over `suites/ui/run.sh`. §11.1. Reconciles `FUNCTIONAL_SPEC`'s binding name
  with `ui-ux-designer`'s contract path without shipping two divergent UI suites.
- **ASA-9 · A third (`ops`) database.** §4.1. Quarantine evidence and provenance
  must not live inside a corpus store; this is a consequence of `AC-F10-01`, not a
  convenience.
- **ASA-10 · Three storage-shape refinements** (supersession edge row;
  `PROTECTED` `CHECK`; `AUTHORIZED` trigger). §6.3. Field names and semantics from
  `PLAN.md` §4 are preserved exactly; only the persisted shape differs, and each
  refinement converts a validated rule into an unrepresentable state.
- **ASA-11 · Values stored as decimal text; comparisons via `Decimal`.** §6.4.
  No float equality anywhere near citation verification.
- **ASA-12 · `UX_KB` `ASM-UX-6` resolved as both-corpora binding for MVP1.**
  §4.4. Closes `UX_KB` §9.4 item 1.
- **ASA-13 · `rca.css` is copied into the product byte-identically and the copy
  is drift-checked by a blocking suite** (`ARCH-14`). §9.2, §12.3.

---

## 15. Items handed to other gate owners — none requiring human resolution

Per the operating mode, nothing here is an open question for the human. These are
items that belong to another owner's lane and are stated so they are not lost.

**To `security-architect` (joint owner of this gate).** Four items, each with my
position stated so a disagreement is visible rather than negotiated away:

1. **Store credential model** (§4.2) — application-level gate, no at-rest
   encryption in MVP1; SQLCipher deferred behind an unchanged `open_store`
   signature and named as an `F54` precondition. If you assess that MVP1 needs
   encryption at rest despite `ASM-20`'s synthetic-only corpus, that is a
   legitimate disagreement and it goes to the human, not into a quiet compromise.
2. **`QuarantineRecord.evidence` is capped at 512 characters** and holds only the
   marking text or response signature — never a document body (§4.1). Confirm or
   tighten.
3. **`QueryRecord.verified_sources[]` stores work-product entries as
   `(corpus, doc_id, locator)` references only** — no title, no quote — so the
   ops store never accumulates work-product text (§4.1).
4. **The wall assertions (`AC-F46-03`, `AC-F46-08`) are yours**; the checker
   library is shipped code and my suite tests the instrument (§4.6). Two owners
   for one assertion is how an assertion ends up owned by neither.

**To `responsible-ai-architect`.** `ASM-UX-8` (alternative questions offered on
refusal panels) is unchanged by this design and remains the item most worth
red-teaming — the extrapolation trap's natural human response is to ask the two
halves separately and blend them by hand, and the design's only defence is a
sentence of copy. Also: §10.3's transcript-replay default is the substrate your
`F47` suite will be written against; if you want live-model adversarial runs to
be blocking rather than exploratory, say so at the joint gate.

**To `code-agent`.** (a) The negative-control constraint in §11.2 — a guard
implemented as an inline conditional inside a large function cannot be
negative-controlled and is not an acceptable implementation of a guard. (b) The
enum-gloss rule at the render boundary (§9.2), which was a real gate-5 defect.
(c) If `pypdf` layout mode cannot recover printed line numbers on the curated
corpus, **report it** — `pdfplumber` is the named fallback and swapping silently
is not in scope for implementation.

**To `plan-agent`.** No new scope observation. `FUNCTIONAL_SPEC` §13's two
observations are already resolved (`ASM-22` ruled MVP1 at 44; `F24`'s
public-only session shape is shipped as a type in MVP1 per §4.4, which is what
`AC-F22-04` asserts).

---

## 16. Change history

| Date | Version | Change |
|---|---|---|
| 2026-08-07 | 1.0.0 | Initial pass. Gate 6 · Architecture, written under the recorded full-autonomy instruction. **Stack committed**: Python 3.12 · FastAPI + Jinja2 server-rendered · pydantic v2 · two SQLite corpus stores + one ops store · numpy exact ranking, no vector DB · Anthropic SDK direct (no LangChain) · OpenAI embeddings with an offline deterministic fallback · pypdf/python-docx · Playwright. All twelve `PLAN.md` §7 requirements addressed individually (§2.4). Two-corpus wall designed as four layers with a seven-boundary static import manifest, a dynamic-import hatch closure, and seven negative controls (§4). Comparability and coverage invariants made unrepresentable-when-violated by type construction (§8). Deterministic-vs-generative split decided: the model is used in exactly two places (§10.2). Mandatory Impact Analysis over six enumerated surfaces, two of them justified as not reached (§12). Thirteen `ASA-*` assumptions; `ASM-UX-6` resolved; no open item left for the human. |

