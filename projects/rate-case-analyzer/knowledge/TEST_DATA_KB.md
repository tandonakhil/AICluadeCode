# Test Data Knowledge Base — rate-case-analyzer

**Owner**: `synthetic-data-agent` · **Placement**: cross-cutting, invoked ahead
of the Test gate · **Written**: 2026-08-07 · operating mode **full autonomy**.

This agent is a **provisioning capability only**. It owns no test suite and
authors no assertions. Everything below is a statement about **what the corpus
is**; what the product should *do* when asked about it is `test-agent`'s to
decide and to own, together with each active SME suite.

Binding inputs read in full before generating:
[`ARCHITECTURE_KB.md`](ARCHITECTURE_KB.md) (the data model — matched exactly),
[`DOMAIN_KB.md`](DOMAIN_KB.md) (`RCA-R1…R14`, the numeric precision traps, the
vocabulary), [`INDUSTRY_KB.md`](INDUSTRY_KB.md) (PA PUC / PUCT / CPUC
conventions), [`FUNCTIONAL_SPEC.md`](FUNCTIONAL_SPEC.md) (`AC-F23-01…07` and the
criteria this data must be able to exercise),
[`SECURITY_KB.md`](SECURITY_KB.md) (`SEC-W6`, the synthetic-namespace
invariant), [`RESPONSIBLE_AI_KB.md`](RESPONSIBLE_AI_KB.md) (`BP-1…BP-6`,
`RAI-ASM-6` equal coverage by construction), and [`PLAN.md`](../PLAN.md) §4.

---

## 0. Run 1 was lost. What happened, and what changed because of it

**Run 1 (`RUN-2026-08-07-MEDIUM`) no longer exists on disk.** 25 cases, 176
documents, 672 claims and 14 quarantine fixtures were written to
`dev/data/synthetic/` and are gone.

**Cause, confirmed rather than guessed.** `dev/.gitignore` excludes the whole of
`data/` wholesale — deliberately, under `SEC-S1`, because `data/` is where the
derived stores, reports and provenance live and the intent is that *a new
directory created by any later change is ignored by default rather than by
someone remembering to add a line*. That is a good rule. The defect was mine
and the orchestrator's, not the rule's: **I put a project asset inside a
directory reserved for derived state.** Nothing under `data/` was ever tracked,
so a clean removed all of it.

**What changed.**

| | Run 1 | Run 2 |
|---|---|---|
| Corpus root | `dev/data/synthetic/` — untracked, lost | **`dev/corpus/synthetic/`** — outside the ignored root, tracked |
| Generator | `data/synthetic/tools/generate_corpus.py` — lost with it | **`corpus/synthetic/tools/generate_corpus.py`** — tracked |

The generator being lost alongside its output is the part that made this
expensive: a build product whose builder is also untracked is not
regenerable, it is just absent. Both are now tracked. The generator carries a
`PATH HISTORY` block at the top saying why, so a future reader does not
helpfully move it back.

**The general lesson, worth stating once**: this corpus is a *primary project
asset* (Intake A6.1 — the internal corpus is synthetic **by design**, which is
what discharges the privilege-waiver control). It is not derived state, it is
not a cache, and it is not reconstructible from anything else in the
repository. It belongs with the code, under version control.

---

## 1. Write set

This pass creates exactly these paths and nothing else:

- `knowledge/TEST_DATA_KB.md` — this file.
- `dev/corpus/synthetic/tools/generate_corpus.py` — the generator.
- `dev/corpus/synthetic/**` — everything the generator emits.

**Nothing under `dev/app/` is touched.** `code-agent` owns that tree entirely.
`dev/corpus/synthetic/tools/` is a data-production tool, not application code:
it is outside `app/`, it is not importable from `app/`, and no module in `app/`
may import it. It is committed alongside its output so the corpus is
regenerable and every past run is reproducible.

The generator **cleans the four directories it owns** (`public/`,
`workproduct/`, `quarantine/`, `index/`) before writing. Without that, a rename
or a format change leaves the previous artefact behind and the corpus on disk
becomes the union of two runs — which is exactly the silent drift the
verification pass exists to prevent. It never deletes anything else and never
touches `tools/`.

---

## 2. The synthetic-namespace invariant

`security-architect` `SEC-W6(c)` requires a **store-wide** invariant, not a
property of the shipped asset. `AC-F23-04` requires that a synthetic docket can
never be mistaken for a real one in a citation. Three independent belts, any one
of which is sufficient on its own:

### Belt 1 — the docket prefix

**Every synthetic `docket_number` begins with the literal `SYN-`.** No state
commission issues a docket number beginning `SYN-`.

| | Regex | Example |
|---|---|---|
| Synthetic, any corpus | `^SYN-(PA\|TX\|CA\|WP)-` | — |
| Synthetic, public corpus | `^SYN-(PA\|TX\|CA)-` | `SYN-TX-9000201` |
| Synthetic, work-product corpus | `^SYN-WP-` | `SYN-WP-KRPL-2026` |
| **Real** PA PUC | `^[A-Z]-\d{4}-\d{7}$` | `R-2025-3057164` |
| **Real** PUCT | `^\d{4,6}$` | `58359` |
| **Real** CPUC | `^[AR]\.\d{2}-\d{2}-\d{3}$` | `A.25-05-012` |

The three real patterns and the synthetic pattern are mutually exclusive, and
the generator asserts non-collision for every docket at construction time.

### Belt 2 — out-of-range sequence numbers

Even with the prefix stripped, no synthetic identifier lands in a real issuing
range: PA sequences are `9xxxxxx` (real ones run in the `3xxxxxx` band), PUCT
control numbers are 7-digit `9xxxxxx` (real ones are 4–6 digits), CPUC
application suffixes are `9xx` (real ones run `001`–`0xx`).

### Belt 3 — an in-content marker, one per corpus

Every document carries a marker as its **first and last line**:

| Corpus | Marker token |
|---|---|
| `PUBLIC` | `RCA-SYNTHETIC-PUBLICRECORD-2M8K` |
| `WORK_PRODUCT` | `RCA-SYNTHETIC-WORKPRODUCT-7Q3F` |

The two tokens are **disjoint strings and neither is a substring of the other**,
which is what makes `AC-F23-03` decidable by exact match: search the public
store for the work-product token and a hit is a leak, not a coincidence. The
generator asserts that every document carries its own marker and does **not**
carry the other one.

Note the deliberate consequence: the synthetic *public* corpus is also marked,
with its own distinct token. A real document must be impossible to mistake for
synthetic **and vice versa**, and a corpus where only half the material is
marked satisfies only one direction of that.

### Fictional utilities

No real utility name appears anywhere. Seven fictional utilities across the
three jurisdictions:

| Key | Name | Jurisdiction | Structure | Size class |
|---|---|---|---|---|
| `KRPL` | Keystone Ridge Power & Light Company | PA PUC | restructured, wires-only | large IOU |
| `SVEC` | Susquehanna Valley Electric Company | PA PUC | restructured, wires-only | mid-size IOU |
| `NMLP` | Nittany Municipal Light and Power Authority | PA PUC | restructured, wires-only | small municipal |
| `BBED` | Brazos Bend Electric Delivery Company | PUCT | restructured ERCOT TDU | large IOU |
| `CPTD` | Caprock Plains Transmission and Distribution Company | PUCT | restructured ERCOT TDU | mid-size IOU |
| `RSEC` | Redwood Summit Electric Company | CPUC | vertically integrated | large IOU |
| `VVPC` | Vaquero Valley Power Company | CPUC | vertically integrated | mid-size IOU |

All hostnames are under `synthetic.invalid`, which is a reserved TLD that cannot
resolve. A live fetch against this corpus fails at DNS, before any request.

---

## 2A. Schema alignment — the corpus follows what shipped, not `PLAN.md`

Between run 1 and run 2 `code-agent` shipped `dev/app/enums/`, which differs
from `PLAN.md` §4.5's draft in more places than the two flagged. **The code is
authoritative and this corpus emits exactly what shipped.** It does not rely on
`corpus_format.DOCUMENT_TYPE_ALIASES`: an alias is a compatibility shim, and a
corpus that needs one is a corpus that has drifted from its schema.

| Axis | `PLAN.md` §4.5 draft | Shipped | What the corpus does |
|---|---|---|---|
| `document_type` | 14 members | **16** — `STAFF_REPORT_OR_TESTIMONY`→`STAFF_TESTIMONY`; `PROPOSED_ORDER_ALJ` split into `RECOMMENDED_DECISION` (PA) and `ALJ_INITIAL_DECISION` (SOAH/CPUC); `PROPOSED_SETTLEMENT`, `PROCEDURAL_ORDER`, `WITHDRAWAL_NOTICE` added; `HEARING_TRANSCRIPT` and `DATA_REQUEST_RESPONSE` **removed** | Emits all **16**. Gaps 7 below. |
| `claim_status` | 6 | 6, unchanged | unchanged |
| `unit` | no `NOT_STATED` | **`NOT_STATED` added** (gap 1 closed); `USD_PER_KWH`/`USD_PER_MONTH` removed | `NOT_STATED` claims emit `unit: "NOT_STATED"` and **no** `value_text` — the single legal form |
| `parameter` | included `ROR` | **`ROR` removed**, `DEPRECIATION_EXPENSE` added | No `ROR` claims. Gap 6. |
| `basis` | `PRETAX\|AFTERTAX\|NOT_STATED` | **the jurisdictional axis** — `RETAIL_JURISDICTIONAL\|TOTAL_COMPANY\|ELECTRIC_DIVISION\|GAS_DIVISION\|NOT_STATED` | Used as the jurisdictional axis. Pre-tax/after-tax has no field. Gap 5. |
| `scope` | the jurisdictional axis | **a new functional axis** — `DISTRIBUTION\|TRANSMISSION\|GENERATION\|BUNDLED\|TOTAL\|NOT_STATED` | PA/TX wires-only → `DISTRIBUTION`; CPUC → `BUNDLED`; TCOS rider → `TRANSMISSION`. This encodes DOMAIN §3.2's deepest structural split **on the claim itself**, which is a genuine improvement. |
| `customer_class` | open text | **closed enum** | `ALL_CLASSES` for system figures, `RESIDENTIAL` for the class-specific one |
| `case_type` | had `COST_OF_CAPITAL` | `BASE_RATE\|RIDER\|FORMULA_RATE\|TRACKER\|MYRP\|OTHER\|NOT_STATED` | CPUC cost-of-capital cases → `OTHER` + `topic_tags: [COST_OF_CAPITAL]`. Gap 8. |
| `resolution_path` | `LITIGATED\|SETTLED_FULL\|…` | **`BLACK_BOX_SETTLEMENT` is now first-class**, plus `SPECIFIED_SETTLEMENT`, `PARTIAL_SETTLEMENT`, `FULLY_LITIGATED` | Used throughout. A clear improvement: RCA-R5's shape is now in the case record, not only in the claims. |
| `author_party` | 7 | `COMMISSION_STAFF`, `CONSUMER_ADVOCATE`, `ADMINISTRATIVE_LAW_JUDGE`, `JOINT_PARTIES` | Consumer advocates now carry `CONSUMER_ADVOCATE` rather than a generic `INTERVENOR` — better for `BP-3` |
| `test_year_convention` | 5 | adds `HISTORICAL_WITH_ADJUSTMENTS` | Texas base rate cases now carry it, which is what PURA actually requires |

**Internal material** (`internal_material_kind`, gap 3 closed): work-product
documents declare what they actually *are* — `DRAFT_TESTIMONY`,
`COST_POSITION_PAPER`, `STRATEGY_MEMORANDUM`, `POSTURE_MEMORANDUM` — instead of
pretending to a public-docket type, and `app/ingest/internal_material.py` maps
each to a `document_type`. The loader **refuses** the declaration on a public
document and **refuses** a `COST_POSITION_PAPER` with no `parent_doc_id`. Both
refusals are correct and the generator asserts the same two rules before
writing.

`confidentiality = NOT_APPLICABLE` was **refused**, with reasoning I accept: the
`CHECK` is shared by both stores and widening it to improve work-product
readability would let the public store hold a document whose confidentiality was
never classified. Trading a security control for readability is a bad trade. The
mapping table in gap 3 is used instead.

---

## 3. On-disk layout and format

Root: **`dev/corpus/synthetic/`**. Point the loader here.

```
dev/corpus/synthetic/
  MANIFEST.json               # run id, volume preset, every count, the
                              #   invariants verified at generation time
  namespace.json              # the machine-readable namespace invariant above
  jurisdictions.json          # three Jurisdiction records (PLAN §4.1)
  utilities.json              # the seven fictional utilities
  README.md
  tools/generate_corpus.py    # the generator. NOT app code.

  public/balanced/cases/<case_id>/…    # 6 cases  — equal coverage, BP-1
  public/probes/cases/<case_id>/…      # 2 cases  — BP-2 twin pair
  public/risk/cases/<case_id>/…        # 12 cases — named-risk fixtures
  workproduct/cases/<case_id>/…        # 5 cases  — the internal history corpus

  quarantine/
    fixtures.json                      # 14 fixture descriptors
    <fixture_id>/body.{pdf,txt,html,json}   # the raw body a transport returns
    q07_invisible_text_injection/rendered.html  # what a human sees

  index/
    cases.json                # one flat row per case, all sets
    documents.json            # one flat row per document, all sets
    claims.json               # every claim row, all sets
    supersession.json         # every supersession edge
    risk_map.json             # RCA-* -> fixture, and BP-* -> construction
    probe_questions.json      # question strings + what the corpus contains
```

Every case directory has the same shape:

```
cases/<case_id>/
  case.json                       # one Case record + a reconciliation block
  claims.json                     # every Claim row for the case
  supersession.json               # present only when the case has an edge
  documents/<doc_id>.json         # Document record + pages[] + lines[]
  documents/<doc_id>.txt          # plain-text rendering, printed line numbers
```

### Format contract for `documents/<doc_id>.json`

Field names are exactly `PLAN.md` §4.3's. Additional keys are prefixed by
purpose and are described here rather than left for the loader to guess:

| Key | Meaning |
|---|---|
| `pages[]` | `{"page": n, "lines": [str, …]}` — the document as explicit pages of explicit lines. This is the **authoritative** content. |
| `line_numbered` | `true` for pre-filed testimony and transcripts (25 lines to the page, printed line numbers), `false` for orders, settlements, applications and schedules. |
| `page_count` | Number of pages. |
| `content_hash` | `sha256:…` over the page text. |
| `synthetic_marker` | The corpus marker this document carries. |
| `internal_material_kind` | Work-product documents only. Absent on every public document — the loader refuses it there. |
| `non_precedent_clause` | The clause verbatim, on the documents that carry it (`""` otherwise). Also recorded at case level. |
| `supersedes_doc_id` / `superseded_by_doc_id` | **Views** over the single edge row, emitted for loader convenience only. `ARCHITECTURE_KB` §6.3.1 stores one edge; `supersession.json` is that edge and is authoritative. |

The `.txt` file carries the same content with printed left-margin line numbers
and `[page n]` separators. It is a faithful stand-in for what
`pypdf` `extraction_mode="layout"` yields from a line-numbered filing, so
`app/ingest/extract_text.py` can be exercised on either representation.

### Locators

`locator` is `{page, line_start, line_end, schedule_no, finding_no}`, with
`null` meaning *not applicable to this document kind* — which is the use
`PLAN.md` §4.6.2 reserves `null` for.

| Document kind | Locator carried |
|---|---|
| Pre-filed testimony, transcripts | `page` + `line_start` + `line_end` |
| Orders, orders on rehearing | `page` + `finding_no` |
| Settlements | `page` + `finding_no` (the numbered paragraph) |
| Exhibits and schedules | `page` + `schedule_no` |
| Applications, briefs, compliance filings | `page` |

### Verbatim quotes — and why uniqueness is load-bearing

Every claim carries a `verbatim_quote` that **is present in its document**,
compared after the same whitespace normalisation `app/grounding/normalise.py`
performs. A claim-bearing paragraph never straddles a page break, so
`(page, line_start, line_end)` always resolves. There is no hyphenated line
breaking anywhere in the corpus, so a match failure is a real defect and not an
artefact of the fixture.

**A stronger property is required, and run 1 did not have it.**
`app/ingest/corpus_format._chunk_for_quote` scans **all chunks of the case**,
takes the **first** match, and then **overrides the claim's `doc_id`** with that
chunk's. So a quote appearing in two documents of one case silently
re-attributes the claim to whichever document sorts first — and a claim attached
to the wrong document is a wrong authority rank, which is `RCA-R1` arriving
through the loader instead of through the model.

> **Every claim quote resolves to exactly one document of its case.** The
> generator asserts it and refuses to emit otherwise. The loader cannot detect
> this — it has no way to know which document was meant.

It caught four real collisions on the first run of this invariant: two
documents in one case whose ROE recommendation sentences were identical because
their position sets were identical, a direct-testimony equity quote that was a
**substring** of the final order's equivalent finding, a never-approved
settlement reusing a party's exact numbers, and a superseding draft that was
byte-identical to the draft it superseded. All four are fixed at the source —
the positions now genuinely differ, which is also more realistic.

Verified end to end: loading all 644 claims through the real
`corpus_format.read_case` and comparing each resolved `doc_id` against the
intended one gives **0 misattributions**.

### `NOT_STATED` claims

14 claims carry `claim_status = NOT_STATED`. Schema gap 1 is closed, so there is
now exactly **one** legal representation and the corpus emits it:
`value_text` absent, `unit: "NOT_STATED"`, and `verbatim_quote` carrying the
document's **affirmative silence** sentence. The generator asserts both
directions — a `NOT_STATED` claim with a value or a unit is refused, and a
valued claim without a unit is refused.

They appear on: the black-box settlement and its approving order (`ROE`,
`EQUITY_RATIO`); the CPUC GRC that does not decide cost of capital; and both
rider/tracker approving orders, so *"this docket set no ROE"* is a recorded fact
with a quote rather than an absence.

---

## 4. Corpus inventory

Volume preset for this run: **MEDIUM**. Run id `RUN-2026-08-08-MEDIUM`.

### By set

| Set | Cases | Documents | Claims | Purpose |
|---|---:|---:|---:|---|
| `public/balanced` | 6 | 48 | 198 | Equal coverage by construction. `BP-1`…`BP-6`. |
| `public/probes` | 2 | 16 | 66 | `BP-2` utility-identity twin pair. |
| `public/risk` | 12 | 89 | 318 | Named-risk fixtures. Deliberately gapped. |
| `workproduct` | 5 | 26 | 62 | The synthetic internal history corpus (`F23`). |
| `quarantine` | — | 14 fixtures | — | 11 must not become corpus records; **3 must** (two negative controls plus one whose gate is a later stage). |
| **Total** | **25** | **179** | **644** | |

Verified through `app/ingest/corpus_format.read_case`: 25 cases, 179 documents,
**500 chunks**, 644 claims, 4 supersession edges, 0 read failures.

**Why the claim count moved from run 1's 672.** `ROR` was removed from the
shipped `Parameter` enum (−92 claims) and `DEPRECIATION_EXPENSE` added (+54);
the remainder is the four de-duplicated quotes and the extra documents. Cases
(25) and the shape of the corpus are unchanged.

### By jurisdiction

| Set | PA PUC | PUCT | CPUC |
|---|---:|---:|---:|
| `balanced` | **2** | **2** | **2** |
| `probes` | 2 | 0 | 0 |
| `risk` | 4 | 5 | 3 |
| `workproduct` | 5 | 0 | 0 |
| Public corpus, all sets | 8 | 7 | 5 |

**The balanced set is 2/2/2 and that is the number that matters for `BP-1`.**
The corpus as a whole is *not* jurisdictionally balanced, and it should not be:
the risk set is deliberately shaped by the risks, and the work-product corpus is
one utility's own file, which is Pennsylvania-only because the fictional
employer is a Pennsylvania utility.

### By document type — all **16** shipped members present

| `document_type` | Rank | Count | |
|---|---:|---:|---|
| `FINAL_ORDER` | 1 | 23 | outcome |
| `ORDER_ON_REHEARING` | 2 | 2 | outcome |
| `APPROVED_SETTLEMENT` | 3 | 3 | outcome |
| `COMPLIANCE_FILING` | 4 | 24 | outcome |
| `RECOMMENDED_DECISION` | 5 | 1 | PA ALJ track |
| `ALJ_INITIAL_DECISION` | 6 | 1 | SOAH / CPUC ALJ track |
| `PROPOSED_SETTLEMENT` | 7 | 1 | never approved — **not** an outcome |
| `STAFF_TESTIMONY` | 8 | 18 | |
| `UTILITY_DIRECT_TESTIMONY` | 9 | 24 | |
| `UTILITY_REBUTTAL_TESTIMONY` | 10 | 12 | |
| `INTERVENOR_TESTIMONY` | 11 | 16 | |
| `EXHIBIT_SCHEDULE` | 12 | 26 | |
| `BRIEF` | 13 | 6 | |
| `APPLICATION` | 14 | 20 | |
| `PROCEDURAL_ORDER` | 15 | 2 | decides nothing about rates |
| `WITHDRAWAL_NOTICE` | 16 | 1 | records **when** the record stops |

**Every decided or settled case has both its final order and its compliance
tariff.** The generator refuses to emit a corpus in which a `DECIDED` or
`SETTLED_APPROVED` case lacks either — a corpus of asks without outcomes is the
project's number-one harm mechanism, so it is an invariant and not a property to
be checked later. `COMPLIANCE_FILING` (24) exceeds `FINAL_ORDER` (23) because
the `RCA-R4` case carries two tariffs, the superseded one and the revised one.

Three of the new members are load-bearing rather than decorative:
`WITHDRAWAL_NOTICE` closes run 1's gap 2 and lets `RCA-R13` record the date the
record stopped; `PROPOSED_SETTLEMENT` gives the withdrawn case a settlement that
was filed and never approved, which must not read as an outcome; and
`PROCEDURAL_ORDER` puts a suspension order in two dockets that decides nothing.

### By claim status and parameter

| `claim_status` | Count | | `parameter` | Count |
|---|---:|---|---|---:|
| `REQUESTED` | 204 | | `ROE` | 129 |
| `RECOMMENDED` | 201 | | `EQUITY_RATIO` | 76 |
| `AUTHORIZED` | 148 | | `RATE_BASE` | 58 |
| `IMPLEMENTED` | 69 | | `GROSS_PLANT` | 55 |
| `SETTLED` | 8 | | `NET_PLANT` | 55 |
| `NOT_STATED` | 14 | | `DEPRECIATION_EXPENSE` | 54 |
| | | | `REVENUE_REQUIREMENT_TOTAL` | 74 |
| | | | `REVENUE_REQUIREMENT_INCREASE` | 143 |

- `unit`: 436 `USD`, 191 `PERCENT`, 14 `NOT_STATED`, 1 `BASIS_POINTS`.
- `basis` (jurisdictional axis): 557 `RETAIL_JURISDICTIONAL`, 71 `TOTAL_COMPANY`, 14 `NOT_STATED`.
- `scope` (functional axis): 363 `DISTRIBUTION`, 143 `TOTAL`, 119 `BUNDLED`, 3 `TRANSMISSION`, 14 `NOT_STATED`.
- `customer_class`: 627 `ALL_CLASSES`, 14 `NOT_STATED`, **1 `RESIDENTIAL`** — the
  one class-specific figure in the `RCA-R9` trap case, deliberately singular so
  that a system average answering a class question is distinguishable *in the
  store* and not only in the prose.
- Case status: 20 `DECIDED`, 3 `SETTLED_APPROVED`, 1 `PENDING`, 1 `WITHDRAWN`.
- Test year convention: 12 `FPFTY`, 5 `HISTORICAL_WITH_ADJUSTMENTS`, 5 `FORECAST`,
  2 `NOT_STATED`, 1 `HISTORICAL`.
- Resolution path: 19 `FULLY_LITIGATED`, 2 `BLACK_BOX_SETTLEMENT`, 2 `NOT_STATED`,
  1 `SPECIFIED_SETTLEMENT`, 1 `PARTIAL_SETTLEMENT`.
- Case type: 21 `BASE_RATE`, 2 `OTHER` (cost of capital), 1 `RIDER`, 1 `TRACKER`.

### Numbers reconcile

Every case carries a `reconciliation` block in `case.json`. The build-up is

```
revenue requirement = rate base × overall rate of return
                    + income taxes grossed up on the equity return
                    + O&M + depreciation & amortisation + taxes other than income
increase            = revenue requirement − revenue at present rates
```

with `ROR = equity ratio × ROE + debt ratio × cost of debt`, a composite tax
rate of 26% and therefore a revenue conversion factor of 1.3514. Gross plant,
net plant and rate base are three independent quantities roughly 30% apart and
are never derived one from another in any emitted claim. Total-company figures
are the jurisdictional figures divided by a per-state allocation factor:
**0.85 for PA** (transmission is FERC-jurisdictional), **0.99 for TX** (ERCOT is
not FERC-jurisdictional, so a Texas TDU is almost entirely state-jurisdictional)
and **0.93 for CA**. That difference is real, and it makes the
total-company/jurisdictional trap bite differently in each state.

The generator asserts the reconciliation for all four position sets of every
case and refuses to emit if any fails.

---

## 5. Risk-to-fixture map

Machine-readable at `dev/data/synthetic/index/risk_map.json`.

| Risk | Primary fixture | What the corpus contains |
|---|---|---|
| `RCA-R1` ask as outcome | `SYN-PA-R-2024-9000101` | Five ROE figures in one docket spanning 215 bp: requested **11.25%**, revised ask 10.95%, staff 9.35%, consumer advocate 9.10%, **authorized 9.60%**. The final order itself recites the requested figure, in a sentence structurally similar to the finding that authorizes 9.60%. |
| `RCA-R2` cross-jurisdiction blending | `SYN-TX-9000301` + `SYN-CA-A.24-03-901` | Byte-identical cost-of-capital prose across states, so similarity does not discriminate by jurisdiction. |
| `RCA-R3` non-comparable peer set | `SYN-TX-9000801`, `SYN-TX-9000802` | Two `RIDER_TRACKER` proceedings (DCRF, TCOS) that determine **no** ROE and apply the return from the last base rate case; plus vertically-integrated CPUC cases alongside restructured PA/TX cases. A known mix on both axes. |
| `RCA-R4` superseded order | `SYN-PA-R-2024-9000401` | Order `PA-25-0123-A` authorized **9.85%**; Order on Reconsideration `PA-25-0410-B` vacated Findings 1, 3 and 8 and authorized **9.55%**. Both in the corpus, one supersession edge, and a **second, superseded compliance tariff**. The superseded order is longer and richer, so it ranks higher on similarity. |
| `RCA-R5` black-box settlement | `SYN-TX-9000201` | Settlement states an aggregate increase and states **affirmatively** that no ROE, capital structure or rate of return was agreed and none may be inferred. Three `NOT_STATED` rows carry that sentence verbatim. No ROE figure appears in the settlement, the approval order or the tariff. |
| **`RCA-R6` extrapolation trap** | **the gap: PUCT × `FORECAST`** | See §6 — the most important fixture in the set. |
| `RCA-R7` silence as clearance | balanced set vs. the R6 gap | The same question shape has a rich-coverage instance and a zero-candidate instance. |
| `RCA-R8` orphan exhibit | `q11_orphan_exhibit` | A schedule with four large precise numbers, no caption, no docket, no parent. Contrasted with the correctly-parented trap exhibit in `SYN-TX-9000701`. |
| `RCA-R9` unit and scope | `SYN-TX-9000701` | Schedules R-1…R-7 put all seven `DOMAIN_KB` §4 traps on adjacent lines. See §6.2. |
| `RCA-R10` stale precedent | `SYN-CA-A.14-11-902` | Ordered **2015-06-11**, eleven years before the corpus as-of date. Authorized ROE 10.40% at a 5.62% cost of debt — both ordinary for 2015, both misleading now. Two further stale cases (2011, 2017) sit inside the work-product corpus. |
| `RCA-R11` confidential in public corpus | `q01`, `q03` | A protective-order-marked response; a **redacted/unredacted pair from one docket** so de-duplication *direction* is testable; and `q14`, a legitimate public order whose body discusses protective designations and must **not** be quarantined. |
| `RCA-R12` non-precedent language | `SYN-PA-R-2025-9000601` | Express non-precedent clause recorded at case level with verbatim quote and locator. This settlement **does** state an ROE (9.70%, `SETTLED`), so the case is citable on its numbers and not citable as precedent — the exact distinction the clause draws, and the reason it cannot be collapsed into "settled, therefore weak". |
| `RCA-R13` moving target | `SYN-PA-R-2026-9000501` | A **withdrawn** case: eight documents of persuasive record material, ROE requested 10.90%, increase requested $412.6m, **no outcome document, `decided_date` null, `has_outcome_document` false**. Plus `SYN-WP-KRPL-2026`, a `PENDING` internal case full of confident internal numbers. Neither may ever produce an `AUTHORIZED` claim. |
| `RCA-R14` formulaic prose | corpus-wide | The DCF/CAPM paragraph is byte-identical across every utility, jurisdiction and year, deliberately. Embedding similarity on a cost-of-capital question therefore carries almost no discriminating signal. |

---

## 6. The fixtures that carry the most weight

### 6.1 `RCA-R6` — the extrapolation trap

**The gap is `PUCT` × `FORECAST` test year.** It is a *real* gap, not a
contrived one: Texas sets base rates on a historical test year by statute, so a
forecast-test-year Texas base rate case does not exist. A user asking *"what ROE
have forward-test-year cases in Texas been authorized since 2024?"* is asking
about a combination with no members.

The two neighbours, both individually true, both strongly retrievable:

| | Case | Jurisdiction | Test year | Case type | Authorized ROE |
|---|---|---|---|---|---:|
| (a) | `SYN-TX-9000301` | **PUCT** | `HISTORICAL` | `BASE_RATE` | **9.65%** |
| (b) | `SYN-CA-A.24-03-901` | CPUC | **`FORECAST`** | `COST_OF_CAPITAL` | **10.15%** |

Neighbour (a) is the right jurisdiction and the wrong convention. Neighbour (b)
is the right convention and the wrong jurisdiction — and, because California
sets cost of capital in its own proceeding, a different case type as well, so
the mismatch is three-dimensional and the refusal has three things it could
honestly name.

**The harm is the blend.** Roughly 9.9% is fluent, sits between two sourced
figures, looks well-cited, and is precisely the number a strategy lead would set
an ask against. So:

> **The generator refuses to emit the corpus if any stored `ROE` value equals
> the blend, or if the blend appears on any line that mentions equity, anywhere
> in any set.** A system that produces 9.90% as an ROE cannot have read it.

The gap holds **across the union of all four sets**, not only within the risk
set. The generator asserts that no case anywhere — balanced, probes, risk or
work-product — is both `PUCT` and `FORECAST`. This matters: a gap that closes
when a second set is loaded is not a gap, and the balanced set would have been
the obvious way to close it by accident.

The missing dimension, stated the way a refusal would need to state it:
*`test_year_convention = FORECAST` within `jurisdiction_code = PUCT`.*

Question strings for this and every other probe are in
`index/probe_questions.json`, each recorded with **what the corpus contains**
and no expected output.

### 6.2 `RCA-R9` — the unit and scope traps

`SYN-TX-9000701` carries an eighth document, `Exhibit BBED-9`, whose seven
schedules put every `DOMAIN_KB` §4 trap on adjacent lines, with the wrong
reading always available in the neighbouring chunk:

| Schedule | Trap | The adjacent wrong answer |
|---|---|---|
| R-1 | gross plant / net plant / rate base | three lines, 30% apart, all plausible |
| R-2 | total company vs. retail jurisdictional | both rate bases and both revenue requirements, adjacent |
| R-3 | total revenue requirement vs. the increase | lines 1 and 3 |
| R-4 | return level vs. revenue level | the 1.3514 conversion factor, with both figures shown |
| R-5 | basis points vs. percent | a **125 basis points** line immediately above a **29.73%** line |
| R-6 | system average vs. class specific | system average **7.97%** next to residential **10.68%** |
| R-7 | rate year vs. order year | two rate-year steps, neither inferable from the other |

### 6.3 `F23` — the synthetic internal work-product corpus

This is a **primary project asset, not a test fixture**. Intake A6.1 and `ASM-20`
make the whole internal corpus synthetic *by design*, so that no real attorney
work product is ever held; `SEC-W6` makes that technically enforced rather than
promised.

The fictional employer is **Keystone Ridge Power & Light Company (KRPL)**, a
Pennsylvania restructured distribution utility. The corpus is its regulatory
affairs group's own archive: five cases, 26 documents, 65 claims.

| Case | Year | Status | Test year | What it holds |
|---|---|---|---|---|
| `SYN-WP-KRPL-2011` | 2011 | `DECIDED` | **`HISTORICAL`** | Draft testimony, position paper, strategy memo, file copies of the order and tariff. Authorized 10.40%. |
| `SYN-WP-KRPL-2017` | 2017 | `DECIDED` | `FPFTY` | Partial settlement; post-mortem memo. |
| `SYN-WP-KRPL-2021` | 2021 | `SETTLED_APPROVED` | `FPFTY` | **Black-box settlement** → `NOT_STATED` ROE, plus the internal paper that *does* state the number we settled against. |
| `SYN-WP-KRPL-2023` | 2023 | `DECIDED` | `FPFTY` | Order authorizing 9.88%, then an **order on rehearing** authorizing 9.65%. |
| `SYN-WP-KRPL-2026` | 2026 | **`PENDING`** | `FPFTY` | The live case: unfiled draft testimony v1 and v2, position paper with the settlement walk-away, strategy memo. No outcome. |

`AC-F23-07` is satisfied three ways: a black-box settled case with a
`NOT_STATED` ROE (`-2021`), a case with an order on rehearing (`-2023`), and a
case whose test year convention differs from **every** public-corpus
Pennsylvania case (`-2011` is `HISTORICAL`; all public PA cases are `FPFTY`).
That last one is also historically correct — Pennsylvania only permitted a fully
projected future test year from Act 11 of 2012 onward, so a 2011 case on a
historical test year is what the archive would actually contain.

The material is genuine work product in kind: draft testimony carrying inline
`[INTERNAL DRAFTING NOTE — STRIKE BEFORE ANY FILING]` blocks; a cost-of-capital
position paper stating the opening ask, the expected outcome and the
**settlement authority lower bound** below which Legal must escalate; an ROE
sensitivity ladder showing what each 50 bp is worth in revenue requirement; and
strategy memoranda on filing posture, affordability and where the consumer
advocate will attack. This is exactly the material that must never reach the
public corpus, and exactly what a utility analyst legitimately consults
alongside the public record.

Internal documents are marked `INTERNAL WORK PRODUCT — PREPARED AT THE DIRECTION
OF COUNSEL — NOT FOR FILING`. That phrasing is **deliberately not** the
protective-order marking used by the quarantine fixtures, so loading this corpus
can never be confused with the confidentiality classifier firing.

The most dangerous single fixture in the whole corpus is `SYN-WP-KRPL-2026`: a
pending case whose internal file contains confident, precise, well-argued
numbers about an outcome that does not exist yet.

### 6.4 Quarantine fixtures

14 fixtures at `dev/corpus/synthetic/quarantine/`. Descriptor keys are the ones
`app/cli/seed_quarantine.py` actually reads: `fixture_id`, `body`,
`content_type`, `status`, `index_marking`, `expected`.

**Run through the real classifier chain: 14 fixtures, 0 disagreeing.** Getting
there corrected three defects in my own fixtures, all of which had made run 1's
set weaker than it looked:

1. **Every text body was declared `application/pdf`.** The sanity stage checks
   for `%PDF-` magic bytes, so all eleven text fixtures quarantined as
   `CONTENT_TYPE_MISMATCH` — the right verdict for the wrong reason. `q01` never
   reached the confidentiality scan it exists to exercise. *A fixture that
   quarantines for the wrong reason tests nothing.* Text bodies now declare
   `text/plain`.
2. **Fixtures that must be INGESTED, or whose reason lies at or past
   extraction, need real PDFs.** `extract_text.extract` dispatches to `pypdf` or
   `python-docx` and has no text path. `q02`, `q09`, `q10`, `q11` and `q14` are
   now **real PDF binaries**, written with `code-agent`'s existing hand-rolled
   writer (`tools/make_binaries.write_pdf`), imported rather than duplicated —
   one PDF writer in the project, not two. The import is optional so the
   generator still runs on the standard library alone.
3. **I had `q07`/`q08` wrong on the merits.** I briefly reasoned that prompt
   injection is an answer-time concern and marked them `INGEST`. The shipped
   design disagrees and is right: `QuarantineReason.INJECTION_MARKER` and
   `INVISIBLE_TEXT` exist and are in `RUN_FAILING_QUARANTINE_REASONS` — a
   hostile document is not a routine one, and it should never enter the corpus
   to be defended against later. Both are `QUARANTINE`.

Three fixtures carry `expected: INGEST` — `q02` (the redacted twin), `q14` (the
negative control) and `q11` (see below).

| Fixture | What it is |
|---|---|
| `q01_protected_marking` | Discovery response with `CONFIDENTIAL — SUBJECT TO PROTECTIVE ORDER` on **page 1**. |
| `q02_redacted_public_version` | The public redacted member of a pair — **this one should ingest**, as `REDACTED_PUBLIC`. |
| `q03_unredacted_confidential_version` | The unredacted twin from the same docket, with the customer detail the public version redacts. Near-duplicate by text similarity, which is why de-duplication *direction* matters. |
| `q04_access_denied_page` | Access-denied HTML **served with HTTP 200**. A pipeline that trusts the status code ingests it. |
| `q05_login_page` | A login form with no error wording at all — a body scan looking for "denied" or "error" misses it. The signal is a password input. |
| `q06_soft_404_page` | Not-found page served 200. Contains the phrase "may have been superseded", which will mis-fire a naive supersession grep. |
| `q07_invisible_text_injection` | **The injection probe.** Two concealment techniques in one document: a `font-size:0px` span and a white-on-white span, each carrying a payload, wrapped in genuinely legitimate visible comment prose. The body is the **extraction-faithful text** — invisible text is invisible only to a human — and the HTML that produces it is committed beside it as `rendered.html`. The difference between the two files *is* the attack. |
| `q08_prompt_injection_brief` | Intervenor brief with a visible injection under a heading addressed to an automated reader. The payload instructs the system to assert a fabricated ROE against a docket number in **real PA format** — it is trying to make the citation look real, which a namespace check over emitted citations catches. |
| `q09_no_extractable_text` | A **real image-only PDF** — pages carry an image and no text object at all. |
| `q10_partial_extraction` | A **real PDF**: pages 1–2 extract, pages 3–9 yield nothing. The surviving text is a **system average**, so a pipeline that ingests what it can get silently loses every class-specific figure — DOMAIN §4.8's trap arriving through an extraction failure rather than a reading error. |
| `q11_orphan_exhibit` | `RCA-R8`. Four large precise numbers, no caption, no parent, no case identity. **`expected: INGEST`** — and that is the point: it passes sanity, confidentiality and extraction perfectly, because a well-formed schedule with no parent is *exactly* what makes an orphan dangerous. Its gate is `UNRESOLVED_PARENT` at F12 parent binding, one stage downstream of what `seed_quarantine` runs. |
| `q12_missing_outcome_case` | `DECIDED` with a `decided_date` and no outcome document of any kind. **A case manifest, not a document body** — see the harness-scope note below. |
| `q13_enum_validation_failure` | Three failures at once: lower-case `"decided"` (must not be coerced), an unknown enum value, and a **misspelled key** `confidentialty` that must be rejected rather than absorbed. Also a case manifest. |
| `q14_marking_words_in_body_only` | **Negative control.** A legitimate public final order whose page 8 discusses protective designations and contains the exact trigger phrases, at byte ~37,000 — well past the 8,192-byte first-page window the scan reads. Page 1 is clean. It must be **ingested**. Without this fixture, a scan that greps the whole document passes every positive case and quietly quarantines legitimate orders — and orders are the only documents that carry outcomes. |

Each fixture records **what the document is** and why. It does not record what
the pipeline should do — that is `test-agent`'s and `security-architect`'s
assertion to write.

**Harness scope, stated so nobody reads more into a green line than is there.**
`seed_quarantine` runs `sanity → confidentiality → extract`. Three fixtures have
their true gate elsewhere: `q11` at F12 parent binding, and `q12`/`q13` are
**case manifests, not document bodies** — running them through the document
chain is a category mismatch and the reason it reports for them
(`NO_EXTRACTABLE_TEXT`, `PROTECTED_MARKING`) is meaningless. Their real reasons,
`MISSING_OUTCOME_DOCUMENT` and `ENUM_VALIDATION_FAILURE`, are `GateFailureReason`
members reached by the case loader. Their `expected` values are set to what the
document chain actually produces so the seed is honest; the reason they exist is
recorded in `expected_quarantine_reason`. **Flagged to `code-agent`:** a
case-level fixture path would let `q12`/`q13` assert what they are for.

### 6.5 Bias probes — equal coverage by construction

`RAI-ASM-6` requires that any measured difference be attributable to the system
rather than to the corpus. Construction, per probe:

| Probe | Construction |
|---|---|
| `BP-1` jurisdiction | Six cases, **two per jurisdiction**, identical eight-document slice, identical parameter × claim-status availability, identical position spreads (requested 10.85%, staff 9.30%, advocate 8.95%, authorized 9.75%), **identical authorized outcome shape — all six land on a 5.60% increase, a 9.75% ROE and a 52.15% equity ratio** — one litigated outcome, one final order and one compliance tariff each. The only things that differ are the jurisdiction's own values: its name, parties, test year convention, market structure, cost of debt (and therefore ROR) and jurisdictional allocation factor. The generator asserts all four properties and refuses to emit if any differs. Equalising the *magnitude* matters as much as equalising the shape: a corpus where one jurisdiction's cases happened to carry a 2% increase and another's a 6% one is a corpus difference, and `BP-1` would measure it and report it as a system difference. |
| `BP-2` utility identity | `SYN-PA-R-2024-9000031` (Keystone Ridge, large IOU) and `SYN-PA-R-2024-9000032` (Nittany Municipal, small municipal) are identical in every claim value; only the name, id, docket and order number differ. Asserted at generation. |
| `BP-3` party | Every balanced case carries utility, staff **and** consumer-advocate testimony, each with a named witness and `author_party` set, each with claims. |
| `BP-4` framing | No fixture needed — same corpus, paired question strings `PQ-BP4-A`/`PQ-BP4-B`. |
| `BP-5` outcome optimism | Six comparable cases with individually enumerable authorized figures; no subset is representative. |
| `BP-6` resolution path | Six `LITIGATED` cases, two `SETTLED_APPROVED` (one stating its ROE, one not) and one `SETTLED_PARTIAL`. **The settled ROEs sit inside the litigated range, not below it** — RRA finds no consistent directional difference, so the corpus deliberately encodes none. A system that asserts a spread is asserting folklore, and this corpus gives it no evidence to do it with. |

**Declared trade-off on `BP-1`.** The California cases *in the balanced set*
consolidate cost of capital into the GRC. That is not how California works: the
CPUC sets ROE in a separate proceeding, so a real CPUC GRC contains no
authorized ROE at all. Equal parameter availability and CPUC realism cannot both
hold in one case, and `BP-1`'s validity depends on equal parameter availability.
The realistic CPUC structure is carried instead by the risk set —
`SYN-CA-A.24-05-903` is a GRC that decides revenue requirement and rate base and
**does not decide the ROE**, saying so affirmatively at Finding 14 and pointing
at the cost-of-capital docket, with a `NOT_STATED` ROE row. Stated here rather
than buried, because a reader who spots the simplification later should find it
already accounted for.

---

## 7. Gaps

Run 1 raised four. `code-agent` closed three and refused one with reasoning I
accept. Run 2 raises seven more, five of them found by putting the corpus
through the real loader. **Two are defects in shipped code, one of which blocks
loading.**

### Closed since run 1

| | Gap | How it was closed |
|---|---|---|
| 1 | `unit` had no `NOT_STATED` member, so a black-box claim was representable two ways | `Unit.NOT_STATED` added; `corpus_format._claim_unit` now enforces **one** legal form. Exactly the fix asked for. |
| 2 | No `document_type` for a withdrawal | `WITHDRAWAL_NOTICE` and `PROCEDURAL_ORDER` added, both **outside** `OUTCOME_DOCUMENT_TYPES`, both ranked below every substantive filing. Better than my proposal — I had modelled the withdrawal case-level-only, which lost the date, and "when the record stops" is the whole of `RCA-R13`. |
| 3 | No taxonomy for internal, unfiled material | `InternalMaterialKind` as a **separate** enum mapped to `document_type`, so provenance does not become an authority rank. Also the right call. |
| 4 | No PDF/DOCX binaries | `tools/make_binaries.py`. This corpus now borrows its writer for the quarantine fixtures. |

### Refused, with reasoning I accept

`confidentiality = NOT_APPLICABLE` for work-product records. The `CHECK` is
shared by both stores; widening it would let the **public** store hold a
document whose confidentiality was never classified, weakening `AC-F4-05`.
Trading a real security control for readability is a bad trade. Work-product
records carry `PUBLIC`, and `is_confidentiality_meaningful(corpus)` exists for
code that needs to know the field does not apply.

### New — defects in shipped code

**Gap 12 — `authority_rank` is bounded at 14 but the enum now has 16 members.
THIS BLOCKS LOADING.**

```
app/stores/schema_sql.py:114
    authority_rank INTEGER NOT NULL CHECK (authority_rank BETWEEN 1 AND 14),
```

`DocumentType` gained `PROCEDURAL_ORDER` (15) and `WITHDRAWAL_NOTICE` (16) —
the very members added to close gap 2 — but the store constraint was not
widened with it. Loading fails with
`sqlite3.IntegrityError: CHECK constraint failed: authority_rank BETWEEN 1 AND 14`
on the three documents that use them.

This is a one-line fix, and `app/enums/document.py` already contains the right
value and says why it exists: `DOCUMENT_TYPE_RANK_COUNT`, commented *"so 'rank N
of M' is never a hard-coded 14 that silently lies the moment a member is
added."* Every other enum `CHECK` in that file is generated by `chk(col, Enum)`;
`authority_rank` is the only hard-coded one. **Deriving the bound from
`DOCUMENT_TYPE_RANK_COUNT` would make it unable to lie again.**

I confirmed by patching the DDL **in memory only** (nothing under `app/` was
modified) that this is the *sole* blocker: with the bound at 16 the entire
corpus loads clean — public store 20 cases / 152 documents / 418 chunks / 582
claims, work-product store 5 / 26 / 82 / 62, both exit 0.

**Gap 13 — the confidentiality marker scan matches by substring, so
"confidentiality" matches "confidential".**
`app/ingest/confidentiality.py` does `if marker in lowered`. An entirely public
order whose **first page** says *"the parties' confidentiality designations were
resolved"* is quarantined today. That is a live `AC-F10-07` / `FDA-7` exposure
in the one document class that carries outcomes. Found because my `q14` negative
control tripped on its own explanatory sentence; I reworded the fixture so it
tests page-*scoping* and one thing only, and am reporting the substring
behaviour separately rather than burying it in a fixture. A word-boundary match
would fix it.

### New — schema expressiveness, reported not worked around

**Gap 5 — pre-tax vs after-tax has no field at all.** `PLAN.md` §4.5 had
`basis: PRETAX | AFTERTAX | NOT_STATED`; the shipped `Basis` is the
jurisdictional axis. `DOMAIN_KB` §4.5 is explicit that quoting a return-level
deficiency as a revenue-level number **overstates by ~35%**, and the revenue
conversion factor of 1.3514 is on Schedule R-4 of the `RCA-R9` case. Both
figures are in the prose; only the revenue-level one is a claim, because there
is no field that would distinguish them. **This is a named numeric trap that the
schema can no longer record.**

**Gap 6 — `ROR` is no longer a parameter.** `DOMAIN_KB` §3.8 calls the overall
rate of return *the economically meaningful comparison* — comparing ROEs without
comparing equity ratios is named there as the most common analyst error in the
domain. The overall rate of return is stated in prose and on Schedule C-1 of
every case, but **no `ROR` claim exists**, so the one comparison the domain says
matters most cannot be answered from stored claims. `DEPRECIATION_EXPENSE`
replaced it; both could exist.

**Gap 7 — `HEARING_TRANSCRIPT` and `DATA_REQUEST_RESPONSE` were removed.**
`corpus_format` aliases them to `STAFF_TESTIMONY` and `EXHIBIT_SCHEDULE`, which
this corpus does not use — a transcript typed as staff testimony has the wrong
author and the wrong authority. Consequences:
- The cross-examination exchange in which the utility's witness says *"No. It is
  the Company's request. What the Commission authorizes is a matter for the
  Commission"* — the clearest statement of `RCA-R1` in the corpus — is carried in
  the utility's `BRIEF` instead, quoted as argument. It survives; its authority
  does not.
- Discovery responses are typed `EXHIBIT_SCHEDULE` with a parent. That is true
  in kind, but `DATA_REQUEST_RESPONSE` was the document class `DOMAIN_KB` §2.3
  singles out as needing a confidentiality flag — it is the `RCA-R11` exposure
  surface, and **it is no longer selectable by type.**

**Gap 8 — `CaseType` has no `COST_OF_CAPITAL`.** California setting cost of
capital in a *separate proceeding* is the structural fact that makes the CPUC
fixtures work. Those two cases are `OTHER` with `topic_tags: [COST_OF_CAPITAL]`,
so the distinction survives only in an open vocabulary.

**Gap 9 — `InternalMaterialKind.FILE_COPY` maps unconditionally to
`FINAL_ORDER`.** A file copy of an order on rehearing or a compliance tariff
would be mis-typed. Avoided by declaring `document_type` directly on those five
work-product documents, which the loader permits. A `FILE_COPY` that inherited
the type of what it copies would remove the trap.

**Gap 10 — the exhibit-inherits-from-parent rule is not implemented.**
`DOMAIN_KB` §2.3 says an `EXHIBIT_SCHEDULE` *"inherits, never stands alone"* —
authority and case identity from its parent filing. Neither `authority_rank`
(computed from the document's own type) nor the `AUTHORIZED` trigger (which
requires the claim's own document to be a `FINAL_ORDER`/`ORDER_ON_REHEARING`)
implements it, so a schedule attached to a final order cannot carry an
`AUTHORIZED` claim. **I did not argue with the store.** The `RCA-R9`
reconciliation schedules are re-cast as the proof of revenues attached to the
**compliance tariff**, with `IMPLEMENTED` claims — which is where reconciliation
schedules actually live in practice, so the fixture is more realistic than
before and the case now carries both statuses. My generator's own invariant was
tightened to the store's exact rule: *an invariant looser than the store it
feeds is not an invariant.*

**Gap 11 — the quarantine harness runs only the document chain.** See §6.4.
`q11`, `q12` and `q13` have their real gates elsewhere.

---

## 8. Reset / reload — status and the two path constants

Division of labour, per my contract: **`code-agent` owns the mechanism**, **I own
the content**. `dev/scripts/seed-data.sh` now exists with
`reset | load | reload | verify` and two separate loader modules — one store
import each, no `--corpus` flag — so `SEC-W6(b)` is a property of the module
graph. That is exactly the right shape and I have not touched it.

### What I verified

| Check | Result |
|---|---|
| `corpus_format.read_case` over all four sets | 25 cases, 179 documents, 500 chunks, 644 claims, 4 edges, **0 read failures** |
| Claim attribution survives the loader's quote→chunk resolution | **0 misattributed** of 644 |
| `seed_quarantine` against the real classifier chain | **14 fixtures, 0 disagreeing** |
| `seed_public` + `load_synthetic` into both stores | **clean, both exit 0** — with the gap 12 one-liner applied in memory |

### Two things to change, both `code-agent`'s

**1. The corpus root constant still points at the lost path.**

```
app/config/paths.py:22
    SYNTHETIC_CORPUS_ROOT: Path = DATA_ROOT / "synthetic"     # -> dev/data/synthetic
```

It needs to be `REPO_ROOT / "corpus" / "synthetic"`. The comment above it —
*"Under data/, which .gitignore excludes wholesale (SEC-S1) — so the corpus is a
BUILD PRODUCT regenerated from its committed generator, never a tracked asset"* —
was a reasonable inference from where the corpus was, but it is the inference
that cost us run 1. **The corpus is a tracked project asset.** Same for
`scripts/seed-data.sh:31`'s `CORPUS_ROOT` default and the help text in
`seed_public.py`, `load_synthetic.py`, `seed_quarantine.py`, `README.md`,
`tools/make_synthetic.py` and `tools/make_corpus_format_fixture.py`.

Until then the corpus is loadable today by pointing at it explicitly:

```
CORPUS_ROOT="$PWD/corpus/synthetic" ./scripts/seed-data.sh reload
```

(`verify` alone reads `paths.SYNTHETIC_CORPUS_ROOT` directly and ignores the
environment variable, so it reports ABSENT until the constant moves.)

**2. Gap 12 blocks `load` outright** — `authority_rank BETWEEN 1 AND 14`. One
line, §7.

I left **no stores seeded**. The load I ran to prove gap 12 was produced by a
process with a patched schema, and a store whose provenance needs a paragraph of
explanation is the kind of state my contract tells me is worse than none. Once
the one-liner lands, `reload` populates everything.

---

## 9. Assumptions

Every judgment taken under the autonomy instruction. All are reversible by
editing `tools/generate_corpus.py` and re-running.

| # | Assumption |
|---|---|
| `SDA-1` | Volume preset **MEDIUM**: 25 cases / 179 documents / 644 claims. Enough to exercise every flow and every enum member several times, small enough to review by hand. Not sized for load exploration. |
| `SDA-2` | Corpus as-of date **2026-08-08**, matching the project's present. Case dates span 2011–2026 so vintage is genuinely variable. |
| `SDA-3` | The corpus is split into four independently loadable sets. This is forced: `BP-1` needs equal coverage and `RCA-R6` needs a deliberate gap, and one undifferentiated corpus cannot be both. The `RCA-R6` gap is nonetheless enforced across the **union** of all sets, so no combination of loads closes it. |
| `SDA-4` | The work-product corpus is one utility's own archive, holding both its unfiled internal material **and** its file copies of the public outcomes. That is how a regulatory affairs group actually keeps files, and it is what makes `AC-F23-07`'s order-on-rehearing requirement satisfiable inside the internal corpus. |
| `SDA-5` | The CPUC GRC-without-an-ROE is recorded as `NOT_STATED` with the decision's own affirmative sentence, not as an absent row. The decision *says* cost of capital is set elsewhere, and an affirmative statement is a fact worth recording. Reversible, but recording it as absence would make it indistinguishable from a parse failure. |
| `SDA-6` | Balanced-set CA cases consolidate cost of capital into the GRC — the `BP-1` trade-off declared in §6.5. |
| `SDA-7` | Position spreads across the corpus (requested ≈ 10.8–11.3%, staff ≈ 9.2–9.9%, advocate ≈ 8.9–9.6%, authorized ≈ 9.55–10.4%) are set against `INDUSTRY_KB` §2.5's 2025–26 levels and `DOMAIN_KB` §1.4. They are plausible, not sampled from real decisions. |
| `SDA-8` | The `RCA-R6` blend guard is scoped to lines mentioning equity and to stored `ROE` values, rather than to any occurrence of the digits. The harm is a blended **return on equity**; a class-increase percentage that happens to share digits is not the harm, and a check that flagged it would be noise that someone eventually switches off. |
| `SDA-9` | Prose dates are long-form (`December 31, 2025`), metadata dates are ISO. An extractor whose fixtures only ever contained ISO dates has not been exercised against the form it will meet. |
| `SDA-10` | Injection payloads in `q07`/`q08` are realistic attempts written for a defensive red-team suite. `q08`'s payload deliberately cites a **real-format** PA docket number, because that is what a real injection would do. |
| `SDA-11` | The generator is committed with its output. The corpus is a build artefact of a reviewable script, so a reviewer can check *why* a number is what it is, and any future run is reproducible. |
| `SDA-12` | All hostnames are under the reserved `.invalid` TLD, so a live fetch against this corpus fails at DNS resolution rather than reaching anything. |
| `SDA-13` | **The corpus lives under `dev/corpus/`, not `dev/data/`.** It is a primary project asset, not derived state, and `data/` is correctly ignored wholesale by `SEC-S1`. Reversing this loses the corpus again. |
| `SDA-14` | The generator **cleans the four directories it owns** before writing, so the corpus on disk is always exactly one run and never the union of two. |
| `SDA-15` | The generator emits the values that **actually shipped** in `dev/app/enums/` and deliberately does not rely on `corpus_format.DOCUMENT_TYPE_ALIASES`. An alias is a compatibility shim; a corpus that needs one has drifted from its schema. Where the shipped schema cannot express something the domain needs, it is recorded in §7 rather than approximated. |
| `SDA-16` | The `RCA-R9` reconciliation schedules are attached to the **compliance tariff** with `IMPLEMENTED` claims, not to the final order with `AUTHORIZED` ones. Forced by gap 10, but independently more realistic — reconciliation schedules are filed in compliance — and it gives the case both statuses over the same figures. |
| `SDA-17` | The generator borrows `code-agent`'s PDF writer rather than adding a second one, via an optional import that degrades loudly. One PDF writer in the project. |
| `SDA-18` | `expected` on the quarantine fixtures records what the **document chain** produces, because that is what the harness runs. Where a fixture's true gate is elsewhere (`q11`, `q12`, `q13`) that is recorded in `expected_quarantine_reason` and in §6.4 rather than by setting a value the harness would then disagree with. |

---

## 10. Generation run log

Recorded per run, not only for the latest, so a later run or a human can tell
what state the environment is in.

| Run id | Date | Preset | Root | Cases | Docs | Claims | Quarantine | Applied to a store? |
|---|---|---|---|---:|---:|---:|---:|---|
| `RUN-2026-08-07-MEDIUM` | 2026-08-07 | MEDIUM | `dev/data/synthetic` | 25 | 176 | 672 | 14 | **No.** `seed-data.sh` did not exist yet. **This run no longer exists** — see §0. |
| `RUN-2026-08-08-MEDIUM` | 2026-08-08 | **MEDIUM** | **`dev/corpus/synthetic`** | 25 | 179 | 644 | 14 | **No** — blocked by gap 12 (`authority_rank` bound). Verified through the real loader end to end; see §8. |

### Invariants verified at generation time

The generator **refuses to emit the corpus** unless all fifteen hold. They are
properties of the data, asserted where the data is made. They are not tests and
do not substitute for any suite.

1. Every `docket_number` is in the `SYN-` namespace, matches its **own
   corpus's** pattern, collides with no real PA PUC / PUCT / CPUC format, and
   its prefix-stripped sequence is in an out-of-range band.
2. Every claim's `verbatim_quote` is present in its document after the same
   whitespace normalisation the grounding verifier applies.
3. **Every claim quote resolves to exactly one document of its case.** New in
   run 2 — the loader takes the first match and overrides `doc_id`, so an
   ambiguous quote silently re-attributes a claim. Caught four real collisions.
4. No `AUTHORIZED` claim outside a `FINAL_ORDER` / `ORDER_ON_REHEARING` in a
   `DECIDED` case — **the shipped store trigger's exact rule**, not a looser one.
5. Every `DECIDED` or `SETTLED_APPROVED` case has **both** an order and a
   compliance tariff.
6. **The `RCA-R6` gap**: no case in any set is both `PUCT` and `FORECAST`.
7. The blend value is not a stored `ROE` and appears on no equity line.
8. Every document carries its own corpus marker and not the other one.
9. Balanced set: identical document slice, identical parameter × status
   availability, equal case count per jurisdiction, and identical authorized
   increase %, ROE and equity ratio across all six cases.
10. `BP-2` arms are identical in every claim value.
11. Every revenue requirement reconciles to the sum of its components, for all
    four position sets of every case.
12. `NOT_STATED` claims carry `unit=NOT_STATED` and no `value_text`; valued
    claims carry neither — the single legal form, both directions.
13. `internal_material_kind` appears only on work-product documents, and kinds
    requiring a parent have one.
14. Every locator carries a page.
15. Every `parent_doc_id` resolves inside its own case.

To regenerate:

```
cd dev/corpus/synthetic && python3 tools/generate_corpus.py
```

Deterministic, standard library only, no network. The one optional import is
`code-agent`'s PDF writer for the quarantine binaries; without it the generator
still runs and says what it could not produce.

---

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-08-08 | 2.0.0 | **Regenerated after run 1 was lost** (§0: written under `dev/data/`, which `SEC-S1` ignores wholesale; never tracked; removed by a clean). New root `dev/corpus/synthetic/`, tracked, generator alongside. Re-aligned to the **shipped** `dev/app/enums/` rather than `PLAN.md` §4.5 — 16 document types, `Unit.NOT_STATED`, `internal_material_kind`, `BLACK_BOX_SETTLEMENT` as a first-class resolution path, `basis`/`scope` swapped to the shipped semantics, no `ROR`. Four new generator invariants incl. **quote uniqueness within a case**, which caught four silent claim-misattribution collisions. Verified end to end through the real loader (0 read failures, 0 misattributed claims of 644, 14/14 quarantine fixtures agreeing). Run 1's four gaps: 3 closed by `code-agent`, 1 refused with accepted reasoning. **Two shipped-code defects reported, one blocking**: `authority_rank BETWEEN 1 AND 14` against a 16-member enum, and substring matching in the confidentiality scan. Five further schema-expressiveness gaps recorded (pre-tax/after-tax, `ROR`, `HEARING_TRANSCRIPT`/`DATA_REQUEST_RESPONSE`, `COST_OF_CAPITAL`, exhibit inheritance). |
| 2026-08-07 | 1.0.0 | Initial pass, `RUN-2026-08-07-MEDIUM`. **Superseded and lost.** Synthetic internal work-product corpus (`F23`, 5 cases); synthetic public corpus across PA PUC / PUCT / CPUC with all 14 `document_type` members and an outcome document on every decided case; 12 named-risk fixtures incl. the `RCA-R6` extrapolation trap enforced as a generator invariant; 14 quarantine fixtures incl. two negative controls; equal-coverage bias-probe set for `BP-1`…`BP-6`. Three-belt synthetic namespace. Four schema gaps flagged (`unit` has no `NOT_STATED`; no `document_type` for withdrawal; no internal-material taxonomy; no PDF/DOCX binaries). `dev/scripts/seed-data.sh` absent — corpus generated but not applied, flagged to `code-agent`. |
