# FEATURES — rate-case-analyzer

**Gate 3 · Plan & Backlog** · written 2026-08-07 by `plan-agent`.
Companion to [`PLAN.md`](PLAN.md), which carries the reasoning, the data model
and the numbered assumptions. This file is the itemized backlog.

**Downstream gates build exactly the `MVP1` set.** Anything marked `LATER` is
out of scope for this build, and is listed here *with its reasoning* rather than
deleted — the human can pull any deferred item forward at any point.

## How to read this

- **ID** — stable. Referenced by `PLAN.md`, and by every downstream gate.
- **When** — `MVP1` (build now) or `LATER` (deferred, with reason stated).
- **Size** — `S` (hours), `M` (a day-ish), `L` (multi-day, or the genuinely
  hard part). Honest, not flattering.
- **Discharges** — the `RCA-*` / `IND-*` risk or the Intake/PROJECT_CONTEXT
  constraint this item exists to satisfy. An item discharging nothing is an
  item to question.

## Note on the approval protocol (ASM-21)

The `plan-agent` contract requires every feature to be an individually
approvable item with the split presented as a *recommendation*, never a
decision, and deferred items always shown. Under the recorded full-autonomy
instruction ("make all assumptions, don't ask any questions") the approval
*question* is suppressed — the *record* is not. Every feature below is listed
individually with its own reasoning, including every deferred one, so nothing
was filtered out before the human saw it.

**Totals: 58 features · 44 MVP1 · 14 LATER.**

> Corrected 2026-08-07 (ASM-22). This header previously read "42 MVP1 · 16
> LATER", contradicting the per-feature `When` column below, which yields 44/14.
> `functional-design-agent` found the discrepancy at gate 4 and specified all 44
> rather than guessing which two to drop. **The per-feature column is
> authoritative** — it is where the reasoning lives and was written item by item;
> this header is a derived summary, so a derived total contradicting its own
> source is an arithmetic slip, not a scope decision. `LATER` is exactly F19,
> F20, F24, F33, F41, F50–F58 = 14.

---

## P0 · Foundation

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F1** | Repo hygiene & config baseline — `.env` / `.gitignore` discipline, path-anchored store directories, single typed config module | MVP1 | S | The custom-template override means the template's already-debugged hygiene fixes are not inherited and must be re-established. The relative-path store bug is known and would otherwise recur. | Decisions Log 2026-08-07 (override cost b); `PLAN.md` §7.11 |
| **F2** | Test-suite harness built from scratch — runner structure, fixture layout, and five suite entry points (`functional`, `industry`, `security`, `redteam`, `ui`) including the browser harness | MVP1 | **L** | **The single largest item the override created.** There is no inherited `tests/suites/` scaffold. `responsible-ai-architect` is non-droppable and owns a red-team suite, so the runner it needs must exist. Listed as real work, not assumed — it is the item most likely to be under-estimated. | Decisions Log (override cost a); ASM-5; ASM-15 |
| **F3** | Closed-enum schema module + fail-loud validator, rejecting unknown **values and unknown keys** | MVP1 | M | The two-dimensional authority model is only real if it is enforced. Closes the malformed-keys gap that `policy-lookup-assistant`'s KB identified and deferred — tolerable for two hand-written entries, not for a machine-populated multi-jurisdiction corpus. | Constraint 3; IND-1, IND-2, IND-4, IND-5; RCA-R9; `PLAN.md` §4.6 |
| **F4** | Corpus data model — `Case` / `Document` / `Chunk` / `Claim` / `QuarantineRecord` / `IngestRun` / `QueryRecord`, incl. supersession links, confidentiality, case status | MVP1 | **L** | Carries all three gate-1 non-retrofittable risks. Building these fields later means re-ingesting the corpus, which is the expensive thing. | RCA-R4, RCA-R11, RCA-R13; constraint 9; `PLAN.md` §4 |

## P1 · Acquisition & quarantine

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F5** | Docket-adapter interface + fixture-capture tooling + `LIVE_FETCH` flag | MVP1 | M | ASM-2 made concrete. Adapters are real code against real URL shapes; the flag bounds *when* the network is touched, not *whether* the integration is genuine. The capture tool is what makes fixtures reproducible rather than hand-pasted. | ASM-2, ASM-19; IND-18 |
| **F6** | **PA PUC** adapter — flat numeric document URLs (`puc.pa.gov/pcdocs/<id>.pdf`), semantic docket numbers (`R-*`), HTML document search | MVP1 | M | ASM-1. Restructured wires-only + FPFTY + settlement-dominant. Best-observed URL tractability of the three. | ASM-1; IND-4 (FPFTY stress test) |
| **F7** | **PUCT** adapter — predictable `interchange.puc.texas.gov/Documents/<c>_<i>_<d>.PDF`, URL-parameter docket search | MVP1 | M | ASM-1. Restructured but reached the opposite way from PA: historical test year, statutory four-year cycle, rider-heavy. Best structural contrast partner and best tractability. | ASM-1; IND-6, IND-9 |
| **F8** | **CPUC** adapter — accession-style URLs, `.docx` as well as PDF, advanced search parameters | MVP1 | **L** | ASM-1, and the only vertically-integrated / generation-in-rate-base source. Sized `L` honestly: CPUC GRCs run to tens of thousands of pages, so this adapter must scope **by proceeding**, never ingest a docket wholesale. The `.docx` availability is a real advantage — native Word extracts far more reliably and tables survive. | ASM-1; IND-5; DOMAIN §3.2 |
| **F9** | Non-document fetch detection — fail loud on login page, access-denied body, HTML error, zero-length, content-type mismatch | MVP1 | S | Cheap, and catches a mundane bug with a serious signature: an access-denied HTML body stored as a "document" and later retrieved as precedent. | IND-11; RCA-R11 |
| **F10** | Confidentiality classifier + **quarantine-and-report** — index metadata *plus* first-page marking scan; prefer public redacted version; never ingest both; never index a protected item | MVP1 | M | Constraint 8. Must ship **with** the first adapter, not after: a corpus contaminated once is not cleanable by a later feature, and improperly-redacted PDFs mean the utility running the tool becomes the party in possession. | IND-10; RCA-R11; INDUSTRY §4.5 |

## P2 · Extraction & case assembly

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F11** | Text extraction with in-document locators — page, line range, schedule number, finding-of-fact number | MVP1 | **L** | "Somewhere in a 400-page order" is not a citation. Rate case testimony is line-numbered *specifically so it can be cited this way*; a sponsoring witness cannot attest to a claim they cannot check. | IND-12; DOMAIN §6.4; INDUSTRY §4.1 |
| **F12** | `document_type` classification + exhibit parent-binding (an `EXHIBIT_SCHEDULE` with no resolvable parent **fails ingest**) | MVP1 | M | Schedules hold the numbers, chunk beautifully, and carry almost no context. A free-floating schedule chunk is an unattributable number and must be un-retrievable rather than ambiguously attributed. | RCA-R8; IND-1; DOMAIN §2.3 |
| **F13** | Case-metadata extraction — test-year convention, market structure, resolution path, case status, case type | MVP1 | **L** | These are the inputs to the comparability predicate. Extracted **per case**, never inferred from the state: DOMAIN §1.3 is explicit that convention varies per-case, not just per-jurisdiction. | IND-4, IND-5; RCA-R2, RCA-R3 |
| **F14** | Structured claim extraction with `claim_status`, `unit`, `basis`, `scope`, `customer_class` over the eight-parameter MVP1 set | MVP1 | **L** | The heart of "asked is never rendered as granted." Includes the `AUTHORIZED` write-time invariant and the black-box `NOT_STATED` row. | RCA-R1, RCA-R5, RCA-R9; IND-2, IND-6; constraint 3 |
| **F15** | Outcome-completeness **gate** — a `DECIDED`/`SETTLED_APPROVED` case with no order, settlement or compliance filing fails ingest | MVP1 | S | Constraint 7 / ASM-9. A corpus of asks without outcomes is a machine for producing harm #1. A warning would be ignored; a gate cannot be. | Constraint 7; INDUSTRY §6.5.1; RCA-R1 |
| **F16** | Supersession linking — `supersedes` / `superseded_by`, denormalised `superseded` flag on chunks; limitation stated where undetectable | MVP1 | M | Schema-bound: cannot be fixed at query time. An order on rehearing that revised ROE downward, with the original still ranking higher on similarity, is a confident wrong answer. | RCA-R4; IND-17; constraint 9 |
| **F17** | Non-precedent settlement clause extraction ("this stipulation shall not be cited as precedent") | MVP1 | S | Cheap, and the document itself disclaims the claim the tool would otherwise make. Stripping it as boilerplate is the failure. | RCA-R12; IND-7 |
| **F18** | Rider / formula-rate / non-base-rate case classification and exclusion tagging | MVP1 | S | An ingestion-time classification, not a query-time filter (standard RRA practice). Ingesting rider cases unflagged corrupts every future benchmark, and Texas is precisely where the money moves through riders. | RCA-R3; IND-9; DOMAIN §3.4 |
| **F19** | OCR for scanned filings | **LATER** | M | ASM-10. OCR error inside a numeric table produces a fluent, wrong number — exactly the harm. A scanned document quarantined as `NO_EXTRACTABLE_TEXT` and reported in `known_exclusions` is safe; a silently mis-OCR'd rate base is not. Pull forward only if the curated corpus turns out to be materially scanned. | ASM-10 |
| **F20** | Data-request-response and hearing-transcript ingestion | **LATER** | M | ASM-7. Discovery volume is enormous and is where confidential material concentrates, so it is the worst value-per-risk slice to ingest first. Both stay in the `document_type` enum and are classified-and-skipped, so adding them later is a pipeline change, **not** a schema change. | ASM-7; IND-10 |

## P3 · Corpus stores & the ethical wall

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F21** | Two **physically separate** corpus stores under independent credentials — no shared client, pool or config object | MVP1 | M | Constraint 2. Not two collections in one database and not a `visibility` column: permissions are a filter over a shared thing, and a dropped filter is a silent breach. | Constraint 2; IND-14 |
| **F22** | Session-bound retriever construction + **static import-boundary test** | MVP1 | M | The binding must be structural, not conventional. A public-only session must have **no code path** to the work-product store, not a path returning empty. Enforcement is a shipped test, not a review note. | Constraint 2; IND-14; `PLAN.md` §3.3 |
| **F23** | Synthetic internal-history corpus (`work-product`) — mocked from public rate cases | MVP1 | **L** | A **primary project asset**, not test fixtures: the entire internal-history capability is synthetic by design (A6.1), and per INDUSTRY §4.3 the synthetic-only decision is a privilege-waiver *compliance control*. Owned by `synthetic-data-agent`. | A6.1; ASM-20; IND-14 |
| **F24** | Intervenor / commission-staff session role + authentication | **LATER** | M | Recorded scope decision: intervenor use is in the persona set but out of MVP scope. The *wall* is built now (`F22`) because retrofitting it means re-architecting retrieval; the *login* is not, because MVP1 serves one role. Note that adverse-party production use also needs deployment separation, not just this feature. | A8.2; Intake COI finding #4 |

## P4 · Retrieval & grounding

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F25** | Query-frame parser — closed output schema; **parse failure refuses**, never falls back to keyword search | MVP1 | M | ASM-11. A best-effort search over a corpus of near-identical formulaic prose *is* the cross-jurisdiction blending risk. | ASM-11; RCA-R2, RCA-R14 |
| **F26** | Metadata-filtered retrieval — filters constrain the candidate set, similarity only ranks within it | MVP1 | M | RCA-R14 directly. Embedding similarity will rank a 2011 Georgia vertically-integrated case as "similar" to a 2025 Massachusetts distribution-only settlement, because the prose really is near-identical. Similarity must never widen the set. | RCA-R14; RCA-R2 |
| **F27** | **Comparability predicate** — structured, over extracted metadata, with mismatched dimensions **named** and severity-ranked (BLOCKING / CAVEAT / INFO) | MVP1 | **L** | The crux, and the gate-1 finding that binds Architecture. If this is built as a similarity score, the product *is* harm #1. Severity table is specified in `PLAN.md` §3.7 so `code-agent` implements rather than invents. | Constraint 6; RCA-R2, RCA-R3, RCA-R6; IND-4, IND-5 |
| **F28** | `Coverage` object returned on **every** path, including every refusal | MVP1 | M | Constraint 4 made concrete. There must be no state in which "found nothing" and "looked at nothing" are the same response. | Constraint 4; RCA-R7; IND-9, IND-17 |
| **F29** | Grounded answer composition with evidence-id citation tags and verbatim quoted spans | MVP1 | M | The model must attach checkable claims; step 6 then checks them. Constrained/structured output, not free prose. | Constraint 1; A7.3 |
| **F30** | **Deterministic citation verification** — evidence id supplied, verbatim span present, `document_type`/`claim_status` match, numeric matches the stored `Claim`; **any failure discards the whole answer** | MVP1 | **L** | ASM-3, escalated from open item to blocking at gate 1. The most dangerous hallucination kind is a real quote from a real source that does not support the proposition — not caught by verifying the docket exists. `sources[]` is built from verified citations only, never from the retrieval set. **The largest deliberate deviation from `policy-lookup-assistant`.** | ASM-3; RCA-R8; IND-13; DOMAIN §6.8(c) |
| **F31** | Sentinel refusal — exact `.startswith()` on stripped content, model prose **discarded**, product-controlled string that **names the gap** | MVP1 | M | Ported mechanism, with a stricter requirement: the refusal must say *what* is missing. "I don't have enough information" sends the user off to guess, which reproduces the harm outside the tool. Never regex, never case-insensitive, never substring. | Constraint 1; RCA-R6; IND-13 |
| **F32** | Vintage and staleness caveats — order date on every claim; all-supporting-cases-older-than-threshold caveat | MVP1 | S | A pre-2018 tax gross-up is not merely dated, it is computed under a different statutory rate. Cheap and directly harm-reducing. | RCA-R10; IND-8; INDUSTRY §2.4 |
| **F33** | Peer-aggregate / benchmark / statistics engine | **LATER** | **L** | ASM-14, and the sharpest scope call in the plan. An aggregate is the *delivery mechanism* of harm #1 and is the substance of capability #3, which is the recorded MVP boundary. MVP1 answers with **named cases and their individual figures** instead. Deferring this also removes the surface RCA-R3 needs. When built: public corpus only, rider cases excluded, never averaged across the vertically-integrated/restructured split. | ASM-14; A8.2; constraint 3; RCA-R3 |
| **F34** | Provenance trail — `QueryRecord` written per query, displayed for the current answer | MVP1 | S | A utility's use of AI in preparing a filing may itself become discoverable or commentable (Arizona Corporation Commission opened the first state inquiry into utility AI governance in early 2026). Cheap now, unreconstructable later. | IND-15; INDUSTRY §3.3, §4.6 |

## P5 · Surfaces

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F35** | Web surface — question → answer page | MVP1 | M | Surface 1 of 2. | A5.1 |
| **F36** | Citation card — authority label **as text**, `claim_status`, order date, commission, docket number, in-document locator, source URL | MVP1 | M | The eight-part citation bar from DOMAIN §6, rendered. Authority never by colour alone; `NOT_STATED` rendered as text, never as blank. | IND-3, IND-6, IND-8, IND-12; DOMAIN §6 |
| **F37** | Coverage panel — "checked N, included K, excluded M because…, could not assess J because…" | MVP1 | S | Constraint 4 at the surface. The UI must be structurally unable to render a bare empty list. | Constraint 4; RCA-R7; IND-9 |
| **F38** | Refusal rendering — **neutral, never styled as an error** | MVP1 | S | Refusal is correct behaviour. Styling it as a failure teaches users to route around it, which converts a working guardrail into a nuisance. | Ported UI pattern; constraint 1 |
| **F39** | Corpus freshness / as-of banner, driven by the last successful `IngestRun` | MVP1 | S | The independent-failure argument for treating ingestion as a surface: a silently-stopped scraper yields a stale corpus, and a stale corpus yields confident wrong answers with **no UI symptom** — unless this exists. | RCA-R13; Decisions Log (two surfaces) |
| **F40** | Comparability caveat rendering — named mismatched dimensions, and the non-precedent clause where present | MVP1 | S | Naming the dimension is the whole value; a generic "results may not be comparable" is not a mitigation. | Constraint 6; RCA-R12; IND-7 |
| **F41** | Saved queries / workspace / provenance-trail export | **LATER** | M | ASM-18. The non-reconstructable half (recording the trail) ships in `F34`; export is a convenience over data we will already have. | ASM-18; A8.2 |
| **F42** | Scheduled ingestion job runner with incremental discovery | MVP1 | M | Surface 2 of 2. Runs against fixtures by default (ASM-19), which proves the job works without making the suite depend on three third-party websites. CPUC's official email-subscription service is the sanctioned, polite way to drive incremental runs when live fetch is enabled. | A5.1; ASM-19; IND-18 |
| **F43** | Ingest run report — quarantine report, failure list, non-zero exit, silent-stop detection | MVP1 | S | Quarantine without a visible report is quarantine nobody reads. Pairs with `F39`. | IND-10, IND-11; RCA-R13 |

## P6 · Test suites (all blocking, ASM-5)

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F44** | **Functional suite** — ask-vs-outcome (RCA-R1), black box `NOT_STATED` (RCA-R5), orphan exhibit (RCA-R8), one assertion per numeric trap in DOMAIN §4.1–§4.8 (RCA-R9), metadata-before-similarity (RCA-R14) | MVP1 | **L** | Owned by `functional-agent`, which authored the register. Each `RCA-*` was written to become a test case; this is where that is cashed in. | RCA-R1, R5, R8, R9, R14 |
| **F45** | **Industry / compliance suite** — test-year and market-structure caveats (IND-4/5), black-box display (IND-6), non-precedent clause surfacing (IND-7), order date always present (IND-8), coverage boundaries (IND-9) | MVP1 | M | Owned by `industry-expert`, which authored the `IND-*` register. | IND-4…IND-9, IND-17 |
| **F46** | **Security suite** — store separation, credential separation, import-boundary assertion, quarantine of protected material, fail-loud on non-document fetch | MVP1 | M | Owned by `security-architect`. The wall is only real if a test would fail when it breaks. | Constraint 2; IND-10, IND-11, IND-14; RCA-R11 |
| **F47** | **Red-team suite** — the extrapolation trap (RCA-R6) as the named regression, silence-as-clearance (RCA-R7), fabricated-citation attempts modelled on the 2026 sanctions record (IND-13), sentinel-bypass attempts, blend-two-neighbouring-cases attacks | MVP1 | **L** | Owned by `responsible-ai-architect`, non-droppable, and **must be built** rather than inherited per the override. The RCA-R6 case is near-identical in structure to `policy-lookup-assistant`'s risk #5 and is the single most important test in the project: a plausible blend of two individually-true cases is fluent, well-sourced-looking, and *is* the catastrophic harm. | RCA-R6, RCA-R7; IND-13; A7.2 harms #2, #3 |
| **F48** | **UI suite** — four rendering invariants: authority label as text not colour; order date always present; refusal neutral not error; coverage never an empty list | MVP1 | M | ASM-15. Deliberately narrow: a broad UI suite over an MVP UI is cost without signal, and these four are the ones that carry harm. Requires the browser harness from `F2`. | IND-3, IND-8; constraint 4 |
| **F49** | Ported bug-fix regressions — `min_length=1` + whitespace-rejecting question validator; `AIMessage.content: str \| list[...]` shape normalisation | MVP1 | S | Both were found by real suite runs in `policy-lookup-assistant`, not by review. Porting them on day one is free; rediscovering them is not. | Deliberate reuse |

## Deferred — corpus and capability extensions

| ID | Feature | When | Size | Reasoning | Discharges |
|---|---|---|---|---|---|
| **F50** | **FERC Form 1 + eLibrary structured companion** | **LATER** | **L** | The single highest-leverage post-MVP addition, and the strongest deferred item in this list. `data.ferc.gov` is the **only** candidate with a documented official public API, and Form 1 is the **only** source of genuinely cross-state-comparable rate base / capital structure / O&M data — which is exactly what state dockets cannot give and what `F33` would need. Rejected as an MVP *jurisdiction* for a substantive reason: FERC does not set state retail base rates, so it answers none of the product's core questions and would blur `market_structure` (transmission formula rate proceedings look superficially like rate cases and are not). | ASM-1; IND-5; INDUSTRY §6.5 |
| **F51** | **Capability #3 — approval likelihood / competitive analysis** | **LATER** | **L** | The recorded first `/enhance-project`. Its value is entirely parasitic on corpus quality: an approval-likelihood estimate over a thin or mis-parsed corpus *is* harm #1, delivered confidently with a number attached. Its standing constraints are **already written**, in `PLAN.md` §9 — political context is out-of-corpus, settlement erases the outcome variable, public corpus only, no settled-vs-litigated editorialising. | A8.2; IND-16; constraint 3 |
| **F52** | Illinois ICC as a fourth jurisdiction (MYRP / PBR precedent) | **LATER** | M | Brings the one thing PA/TX/CA do not: a four-year multi-year rate plan with statutory performance metrics under CEJA. Not in MVP1 because it is *also* restructured — PA + TX + IL would give three wires-only states and no generation rate base anywhere, which is why CPUC took the third slot. Promote over `F7` only if PBR/MYRP precedent is the human's real interest. | ASM-1; INDUSTRY §6.3 |
| **F53** | Michigan MPSC as a jurisdiction | **LATER** | **L** | Analytically attractive (10-month statutory deadline, self-implementation at 6 months, projected test year, large 2026 cases) and its e-filed PDFs are required to be OCR-searchable. Rejected for MVP because E-Dockets runs on a JavaScript Salesforce portal with no stable document URLs — a headless browser needed for *discovery*, not just fetching, at disproportionate cost for one jurisdiction. Also considered and deferred: **NY DPS** — excellent analytically, but opaque non-derivable GUID document URLs; worth a 30-minute check for a NY Open Data route before dismissing. | ASM-1; INDUSTRY §6.4 |
| **F54** | Retention & deletion policy implementation | **LATER** | M | **Gating, not merely deferred.** A6.4 was recorded as an open question and is non-blocking *only* because the internal corpus is synthetic. Any real work product requires this first, and the synthetic-only decision must be treated as a compliance control rather than a convenience. | A6.4; ASM-20; IND-14 |
| **F55** | Exportable deliverables — analysis memo, comparison workbook | **LATER** | M | Named at Intake as a plausible later surface and explicitly out of MVP scope. `deliverables-agent` territory. | A5.2, A8.2 |
| **F56** | Gas utility adjacency | **LATER** | M | A4.2 records gas as not excluded but not in scope. The schema does not assume electric, so this is corpus work rather than a rebuild. | A4.2 |
| **F57** | Multi-year rate plan / PBR modelling — per-year ROE bands, annual reconciliation, metric reports | **LATER** | M | Seventeen states plus DC have formalised PBR and nine are actively evolving it in 2026, so this matters. MVP1's schema does not *assume* one-case-one-ROE (`Claim` carries `rate_year` and `effective_date`), so this is additive. Pairs naturally with `F52`. | INDUSTRY §2.6; DOMAIN §1.2 |
| **F58** | Large-load / data-center tariff as a tracked document class | **LATER** | S | The fastest-moving live issue in 2026 and where a strategy lead's questions will actually concentrate — `industry-expert` ranked it #6 in its own advisory backlog. Deferred only because there is essentially **no useful pre-2023 precedent**, so a 12-case corpus supports it thinly and would answer from analogy — which is the extrapolation trap. `Case.topic_tags[]` exists in the MVP1 schema specifically so this is a tagging pass, not a migration. | INDUSTRY §2.1; RCA-R6 |

---

## What MVP1 demonstrably does when it is done

Not a feature list — the end-to-end demo, so the Test gate and `review-agent`
have a single shared picture of "done":

1. The scheduled job runs against captured fixtures for PA PUC, PUCT and CPUC,
   ingests 12 curated real cases **each with its outcome document**, quarantines
   at least one protected-marked document and one non-document fetch, and emits
   a run report showing exactly that.
2. `synthetic-data-agent`'s internal-history corpus loads into a **separate
   store under separate credentials**, and a test proves the public answer path
   has no import route to it.
3. A strategy lead asks *"what ROE has the PA PUC authorized in fully-projected
   future-test-year distribution cases since 2023?"* and gets named cases with
   authorized figures, each citation carrying commission, docket number,
   document identity, page/line locator, `document_type`, `claim_status`, order
   date and verbatim support — every one of which resolves.
4. They ask the same question for a jurisdiction × test-year combination the
   corpus does not cover, and the system **refuses while naming the missing
   dimension** — not "insufficient information."
5. They ask for the authorized ROE in a black-box settled case and are told
   *the settlement did not specify one* — not a back-solved number, not a
   parse-failure `null`.
6. They ask a question about a case whose order was superseded on rehearing and
   get the amended figure, with the superseded document labelled.
7. Every one of those six responses — including both refusals — carries a
   coverage statement naming what was checked, what was excluded and why, what
   could not be assessed, and the corpus as-of date.
8. All five suites are green, and all five are blocking.
