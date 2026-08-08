# Domain Knowledge Base: Utility Rate Case Preparation / Regulatory Economics

Owner: `functional-agent` (standing SME + devil's advocate)
Domain question answered at Intake (A4.1): **utility rate-case preparation /
regulatory economics** — revenue requirement, ROE, rate base, capital structure,
test year, settlement vs. litigated outcomes.
Industry (A4.2, `industry-expert`'s lane, not restated here): regulated US power
utilities.
Scope of this KB: what an engineer with **no utility background** needs in order
to build correct data structures, a correct authority model, and correct test
cases for the MVP (capabilities #1 + #2 — ingestion of 2–3 public commission
dockets plus a synthetic internal corpus, and grounded Q&A with hard citations
and honest refusal).

Written at the Intake gate. Sections 2 (document taxonomy / authority enum) and
3 (comparability) are the two that Architecture cannot be done correctly
without.

---

## 1. Domain Overview — the mechanics and the vocabulary

### 1.1 What a rate case actually is

A regulated utility is a legal monopoly. It cannot set its own prices. To change
what it charges customers, it files a **rate case** (formally, an *application*
or *petition* for a general rate increase) with its state public utility
commission — a quasi-judicial administrative proceeding with parties, evidence,
discovery, hearings and a written decision. It typically runs 7–12 months and
produces hundreds to thousands of documents in a numbered **docket**.

The whole proceeding exists to settle one number and then divide it up:

> **Revenue Requirement** = the total dollars per year the utility is allowed to
> collect from customers.

The canonical formula (NARUC's own formulation):

```
RR = r × RB + O&M + D + T
```

- `r`  — authorized **rate of return** (weighted cost of capital)
- `RB` — **rate base**
- `O&M` — operating & maintenance expense
- `D` — depreciation & amortization
- `T` — taxes

Two structural consequences an engineer must internalise:

1. **The formula is multiplicative in its most contested term.** `r × RB` means
   a 50-basis-point error in ROE on a $10B rate base is roughly $50M/yr of
   pre-tax revenue requirement, before gross-up. This is exactly harm #1 in
   `INTAKE.md` A7.2, and it is why numeric precision (§4) is not a nicety.
2. **Every one of these five terms is separately litigated**, each by different
   witnesses, in different testimony, with different exhibits. A "rate case
   answer" is almost never a single document.

### 1.2 Core vocabulary — define these precisely; they become fields

| Term | Precise meaning | Data-structure implication |
|---|---|---|
| **Revenue requirement** | Total annual revenue the utility is authorized to collect. Distinct from the *increase*. | Two separate numeric fields, never one. See §4.3. |
| **Rate base** | Net original-cost investment in plant used to serve customers: gross plant − accumulated depreciation − accumulated deferred income taxes (ADIT) + working capital + regulatory assets. | Store **gross plant**, **net plant** and **rate base** as distinct fields. They differ by billions. See §4.2. |
| **Rate of return (ROR)** | Weighted average cost of capital allowed on rate base = Σ (component weight × component cost). | Composite; store components too. |
| **Return on equity (ROE)** | The equity component's allowed return, in percent. The single most-cited number in the domain. | Must carry a *status* (requested / recommended / settled / authorized) — see §2.4. |
| **Capital structure** | The debt/equity/preferred split used to weight the ROR. May be the utility's **actual** structure or a commission-imposed **hypothetical** one. | Flag `actual` vs `hypothetical`. A 10.0% ROE on 54% equity ≠ 10.0% ROE on 48% equity. |
| **Test year** | The 12-month period of cost and revenue data used as the baseline. | Enum + explicit start/end dates. See §1.3. |
| **Cost of service study (COSS)** | Study allocating the total revenue requirement to functions (production/transmission/distribution/customer) and then to customer classes. | A document type *and* a set of allocator choices. |
| **Class cost allocation** | Assigning costs to residential / commercial / industrial / lighting classes. Demand allocators (1CP, 4CP, 12CP, NCP, Average-and-Excess) shift **millions** between classes. | Store the allocator method as a first-class field; two cases with the same revenue requirement can hit residential customers very differently. |
| **Rate design** | Converting each class's allocated revenue into actual tariff components — customer charge, energy charge (¢/kWh), demand charge ($/kW), TOU periods. | Separate from revenue requirement. A case can grant a small increase with a large residential fixed-charge shift. |
| **Rider / tracker / surcharge** | A mechanism recovering a specific cost category **outside** a general rate case, usually with an annual true-up (fuel, purchased gas, storm, energy efficiency, infrastructure replacement, decoupling). | **Critical**: rider proceedings are *also* rate cases in the docket sense, and RRA-style datasets normally **exclude rider cases** from average-ROE statistics. Ingesting them unflagged corrupts every benchmark. |
| **Decoupling** | Mechanism severing revenue from sales volume; authorized revenue is fixed and periodically trued-up against actual. | Presence/absence materially changes what a given ROE *means* in risk terms. Comparability field. |
| **Formula rate plan / multi-year rate plan / PBR** | Alternative ratemaking that sets rates by formula or over a multi-year term rather than one test year. | Breaks the one-case-one-ROE assumption; a multi-year plan may have different ROEs or an ROE band per year. |
| **Regulatory lag** | Gap between when a utility incurs a cost and when rates reflect it. The motivation for forward test years and riders. | Explains *why* test-year convention differs by state. |
| **Prudence review** | Retrospective examination of whether an investment/expense decision was reasonable **judged on what was known at the time it was made**, not with hindsight. Costs found imprudent are **disallowed** — excluded from recovery. | A case outcome can include a disallowance that reduces rate base without changing the authorized ROE. Distinct field. |
| **Used and useful** | The standard that customers pay only for plant actually in service serving them. | Gates what enters rate base. |
| **CWIP** (Construction Work in Progress) | Plant under construction. Traditionally **excluded** from rate base because not yet used and useful; some states permit CWIP in rate base (which shifts financing cost to current customers) or permit it only for specified projects. | A yes/no comparability flag with large money attached. |
| **AFUDC** | Allowance for Funds Used During Construction — the non-cash capitalised carrying cost accrued *instead* of CWIP-in-rate-base. The two are alternatives: CWIP in rate base means current recovery; AFUDC means deferred recovery with a return. | If a system compares a CWIP-in-rate-base utility to an AFUDC utility on "rate base growth" it is comparing different things. |
| **Deferred accounting / regulatory asset** | Commission authorisation to defer a cost to a balance-sheet regulatory asset for later recovery rather than expensing it now. | Explains costs that appear in a later case with no obvious current driver. |
| **ADIT** | Accumulated deferred income taxes — a *reduction* to rate base (customer-supplied cost-free capital). | Sign errors here are common and large. |
| **Revenue conversion factor / gross-up** | Multiplier converting an after-tax return deficiency into pre-tax revenue requirement (~1.3–1.4×). | A number quoted "at the return level" vs "at the revenue level" differ by ~35%. |
| **Settlement / stipulation** | Negotiated resolution among some or all parties, requiring commission approval to take effect. | See §2.4 and §4.1 — the black-box problem. |
| **Fully litigated** | Case decided by the commission after hearings without a comprehensive settlement. | Comparability flag; see §3.6. |

### 1.3 Test year — the single most under-appreciated comparability field

A **test year** is the 12 months of cost/revenue data used to set rates. Three
conventions:

- **Historical test year (HTY)** — an actual, completed 12-month period ending
  before the filing. Sometimes with limited "known and measurable" adjustments.
- **Future / forecast test year (FTY)** — a projected 12-month period that
  begins at or after the date new rates take effect. Reduces regulatory lag.
- **Hybrid** — historical base period plus a forecast adjustment period, or a
  partially-forecast year.

State practice varies and is not uniform: Illinois codified a future test year
(83 Ill. Adm. Code 287); Indiana's SEA 560 (2013) lets a utility elect historic,
future, or hybrid; Oregon has a long history of future test periods; other
states allow FTY only case-by-case, or not at all. **This is a per-state, and
sometimes per-case, attribute — it must be extracted per case, never inferred
from the state.**

Why it matters for this product: a forecast-test-year case and a
historical-test-year case are answering different questions about cost. An ROE
authorized alongside a forward test year carries less regulatory-lag risk than
the same ROE with a historical test year and no rider coverage. Treating those
two 9.7% ROEs as the same data point is the mechanism of harm #1.

### 1.4 Grounding numbers (as of mid-2026, from RRA/S&P Global Regulatory Focus)

These are useful as sanity bounds and as fixtures for tests. They are **not** to
be served to users as answers — they are not in the corpus and have no docket
citation.

- Average authorized electric ROE, **excluding rider cases**: **9.68%** in
  H1 2025; **9.64%** for the first nine months of 2025; **9.78%** full-year 2024.
- Vertically integrated electric: **9.47%** vs. distribution-only: **9.13%** in
  cases decided in H1 2022 — a ~34 bp structural spread. (§3.2)
- RRA reports **no discernible pattern** between settled and fully-litigated
  average authorized ROEs — in some years litigated is higher, in others settled.
  A system that asserts "settlements come in lower" is asserting folklore. (§3.6)

Practical consequence: nearly every authorized electric ROE in the modern era
sits in a narrow ~9.0–10.5% band. **The discriminating information is almost
never the headline ROE — it is the capital structure, the test year, the rider
package and the rate base adjustments around it.** A system that retrieves ROEs
well and everything else poorly will look accurate and be useless, or worse.

---

## 2. Document taxonomy of a rate case docket — and the authority model

This is the section the closed, ranked authority enum comes from
(`PROJECT_CONTEXT.md` names this as `functional-agent`/`industry-expert`
territory and notes that `policy-lookup-assistant`'s four-value taxonomy does
**not** transfer).

### 2.1 The documents, in roughly filing order

| Document | What it is | Filed by |
|---|---|---|
| **Application / petition** | The formal ask. Opens the docket. States the requested revenue requirement increase, ROE, capital structure, test year. | Utility |
| **Direct testimony** | Pre-filed written witness testimony supporting the application, by topic (revenue requirement, cost of capital, cost of service, rate design, depreciation, specific projects). | Utility |
| **Exhibits / schedules / workpapers** | The numbers themselves. Standardised schedules (rate base, income statement, cost of capital, COSS, bill impacts). Where the authoritative arithmetic lives. | Utility, then all parties |
| **Data requests (DRs) / interrogatories and responses** | Discovery. Written Q&A between parties. Often the only place a specific assumption is explained. Frequently filed under **confidential/protective-order** treatment. | All parties |
| **Staff report / staff testimony** | The commission's own technical staff's independent analysis and recommendation. Staff is a *party*, not the decision-maker. | Commission staff |
| **Intervenor testimony** | Consumer advocate, industrial customer group, environmental intervenor positions and their own recommended ROE/revenue requirement. | Intervenors |
| **Rebuttal testimony** | Utility's response to staff/intervenor direct testimony. Often revises the ask downward. | Utility |
| **Surrebuttal (and sometimes rejoinder)** | Response to rebuttal. | Staff/intervenors, then utility |
| **Hearing transcripts** | Live cross-examination. | Commission |
| **Briefs (initial / reply)** | Legal argument, post-hearing. | All parties |
| **Settlement agreement / stipulation** | Negotiated resolution. **Not effective until approved.** | Signatory parties |
| **ALJ proposed order / recommended decision / proposal for decision** | A hearing officer's recommendation. **Not binding.** Commissions modify or reject them. | ALJ / hearing examiner |
| **Final order** | The commission's decision. **This is the law of the case.** | Commission |
| **Order on rehearing / reconsideration; errata** | Amends the final order. | Commission |
| **Compliance filing / approved tariff sheets** | The tariffs actually implementing the order. What customers actually get billed. | Utility, commission-accepted |

### 2.2 The load-bearing distinction: *asked* vs. *granted*

Everything above the settlement row, except staff reports, is **advocacy**. A
utility's direct testimony requesting a 10.9% ROE is a true statement about what
was requested and a **false** statement about the jurisdiction's ROE. The
requested-vs-authorized gap is routinely 75–150 basis points.

**The catastrophic-harm mechanism is a retrieval hit on direct testimony
presented as an outcome.** It will read beautifully — direct testimony is
written to be persuasive — and it will be wrong.

Only two document classes are authoritative for "what was actually granted":

1. **Final order** (as amended by any order on rehearing).
2. **Commission-approved settlement**, and only to the extent the settlement
   itself states the parameter (§4.1, black box).

**Compliance filings / approved tariffs** are authoritative for "what rates
actually took effect," which is a *third* question and occasionally differs from
the order's illustrative figures.

### 2.3 Proposed enum A — `document_type` (closed, ranked)

Ranked by authority for outcome claims, 1 = highest. Recommended as a closed
enum enforced at ingestion with fail-loud on any unmapped value (per the
manifest-driven pattern inherited from `policy-lookup-assistant`).

| Rank | Value | Authoritative for |
|---|---|---|
| 1 | `FINAL_ORDER` | What was granted. Top authority. |
| 2 | `ORDER_ON_REHEARING` | Supersedes/amends rank 1 — must be linked, see §5 risk 4 |
| 3 | `APPROVED_SETTLEMENT` | What was granted, **only for parameters it states** |
| 4 | `COMPLIANCE_FILING` | Rates actually implemented |
| 5 | `PROPOSED_ORDER_ALJ` | A recommendation only. **Never an outcome.** |
| 6 | `STAFF_REPORT_OR_TESTIMONY` | Staff's position |
| 7 | `INTERVENOR_TESTIMONY` | An intervenor's position |
| 8 | `UTILITY_REBUTTAL_TESTIMONY` | The utility's revised ask |
| 9 | `UTILITY_DIRECT_TESTIMONY` | The original ask |
| 10 | `APPLICATION` | The original ask |
| 11 | `EXHIBIT_SCHEDULE` | Whatever its parent filing is authoritative for — **inherits, never stands alone** |
| 12 | `DATA_REQUEST_RESPONSE` | A factual assertion by the responding party, discovery-scoped |
| 13 | `HEARING_TRANSCRIPT` | What a witness said under examination |
| 14 | `BRIEF` | Legal argument. Never a fact source. |

Two notes the architect should not skip:

- **`EXHIBIT_SCHEDULE` is the trap.** Schedules are where the numbers are, they
  chunk beautifully (they are tables), and they carry almost no context. An
  exhibit must inherit `document_type` authority and case identity from its
  parent filing at ingestion time; a free-floating schedule chunk is an
  unattributable number and should be un-retrievable rather than
  ambiguously-attributed.
- **`DATA_REQUEST_RESPONSE` needs a confidentiality flag.** Discovery responses
  are commonly filed under protective order with public redacted versions. The
  ethical wall (`PROJECT_CONTEXT.md` standing constraint 2) is about internal
  work product, but confidential discovery is a *second*, structurally similar
  exposure inside what looks like "the public corpus." Flag it at ingestion; do
  not assume "it was on the commission website" means "it is public."

#### Addendum, 2026-08-08 — the table above is the original proposal; shipped code has drifted from it

**This is a record-reconciliation addendum, not a rewrite.** The table above
is preserved as originally proposed at Intake. `review-agent` found at the
Review gate (finding E-1) that `AC-F3-05` — the acceptance criterion binding
the shipped `document_type` enum to this table — was false of the code as
built, and escalated rather than adjudicating which was right. The
orchestrator ruled the shipped enum authoritative and corrected `AC-F3-05` to
match it (see `FUNCTIONAL_SPEC.md` §AC-F3-05). This addendum records exactly
how the two diverged, so the divergence is visible rather than silently
absorbed into a bumped count.

**Shipped `document_type` (16 values, `app/enums/document.py`):**

| Rank | Value | Relationship to the original proposal |
|---|---|---|
| 1 | `FINAL_ORDER` | unchanged |
| 2 | `ORDER_ON_REHEARING` | unchanged |
| 3 | `APPROVED_SETTLEMENT` | unchanged |
| 4 | `COMPLIANCE_FILING` | unchanged |
| 5 | `RECOMMENDED_DECISION` | **replaces** `PROPOSED_ORDER_ALJ`, split into two |
| 6 | `ALJ_INITIAL_DECISION` | **replaces** `PROPOSED_ORDER_ALJ`, split into two |
| 7 | `PROPOSED_SETTLEMENT` | **new** — a settlement filed but not yet approved, distinct from `APPROVED_SETTLEMENT` |
| 8 | `STAFF_TESTIMONY` | renamed from `STAFF_REPORT_OR_TESTIMONY` |
| 9 | `UTILITY_DIRECT_TESTIMONY` | unchanged (rank unchanged too, coincidentally) |
| 10 | `UTILITY_REBUTTAL_TESTIMONY` | unchanged value, rank moved 8→10 |
| 11 | `INTERVENOR_TESTIMONY` | unchanged value, rank moved 7→11 |
| 12 | `EXHIBIT_SCHEDULE` | unchanged value, rank moved 11→12 |
| 13 | `BRIEF` | unchanged value, rank moved 14→13 |
| 14 | `APPLICATION` | unchanged value, rank moved 10→14 |
| 15 | `PROCEDURAL_ORDER` | **new** — deliberate, documented (`RCA-R13`, gap 2) |
| 16 | `WITHDRAWAL_NOTICE` | **new** — deliberate, documented (`RCA-R13`, gap 2) |

**Dropped from the original proposal, present in this table but absent from
shipped code**: `DATA_REQUEST_RESPONSE` (rank 12 above) and
`HEARING_TRANSCRIPT` (rank 13 above). Both losses were already surfaced —
`TEST_DATA_KB.md` §7 flagged the missing `DATA_REQUEST_RESPONSE` member and
`synthetic-data-agent` worked around it by typing the one discovery-response
fixture as `EXHIBIT_SCHEDULE`, parented to the testimony it supports (true in
kind, but loses the ability to select the discovery-response document class
specifically — the confidentiality-flag note above cannot be fully acted on
without it). Neither drop is adjudicated here; both are recorded as known
gaps, in the same spirit as `ASM-29`'s deferred claim-schema gaps —
candidates for a future enhancement pass, not a Code-gate fix forced under
time pressure.

**Why `RECOMMENDED_DECISION`/`ALJ_INITIAL_DECISION`/`PROPOSED_SETTLEMENT`
happened without a KB update**: unknown — no commit message or KB note from
the Code gate's early passes explains the split. Recorded honestly rather
than guessed at; `functional-agent` should evaluate at the next enhancement
whether the three-way split is domain-correct (it plausibly is — a
recommended decision, an ALJ's initial decision, and a not-yet-approved
settlement are genuinely distinct documents the original single
`PROPOSED_ORDER_ALJ` value conflated) or whether it should be reconciled back.

### 2.4 Proposed enum B — `claim_status` (orthogonal, and the real fix)

Document type alone is not enough, because a *final order* recites what was
requested, and *rebuttal testimony* quotes the order in a prior case. Authority
is two-dimensional. Every extracted numeric claim should carry:

| Value | Meaning |
|---|---|
| `REQUESTED` | What a party asked for |
| `RECOMMENDED` | What staff or an intervenor proposed |
| `SETTLED` | Agreed in an approved settlement |
| `AUTHORIZED` | Granted by commission order |
| `IMPLEMENTED` | In effect per compliance filing/tariff |
| `NOT_STATED` | Explicitly present-but-unspecified — the black-box case (§4.1) |

`NOT_STATED` must be a *representable value*, not an absent field. "The
settlement did not state an ROE" and "we failed to parse the ROE" are different
facts, and collapsing them into `null` destroys the system's ability to refuse
honestly. This is the single highest-leverage schema recommendation in this KB.

---

## 3. The comparability problem — the crux

`INTAKE.md` A7.2 names the catastrophic harm as *a confident answer built on
non-comparable precedent*. Here is what actually makes two rate cases
non-comparable. Each of these should be a stored, extracted field and a
displayed caveat, not an implicit assumption.

**3.1 Jurisdiction.** Commissions differ in statute, precedent, elected vs.
appointed commissioners, political climate, and permitted ratemaking mechanisms.
An ROE authorized in one state is weak evidence about another. Cross-state
comparison is legitimate as *context* and illegitimate as *precedent* — utility
witnesses cite out-of-state ROEs as market evidence, never as controlling
authority, and the system's language must preserve that distinction.

**3.2 Vertically integrated vs. restructured/distribution-only.** In restructured
retail-choice states the utility's rate case covers distribution (and billing and
customer service) only; generation is competitive and out of rate base. In
vertically integrated states the case covers generation, transmission and
distribution. These are different risk profiles and the market prices them
differently — **9.47% vs. 9.13% in H1 2022 electric cases**, a ~34 bp structural
gap that has nothing to do with the merits of either case. A benchmark that
averages across this split is producing a number that describes no real utility.

**3.3 Test-year convention** (§1.3). HTY vs. FTY vs. hybrid changes what the cost
data means and how much regulatory-lag risk the ROE has to compensate.

**3.4 Rider/tracker coverage and decoupling.** A utility recovering fuel, storm,
infrastructure replacement and energy efficiency through riders, with revenue
decoupling on top, bears far less volumetric and cost risk than one recovering
everything in base rates. Same authorized ROE, materially different earned
return and risk. **Also: rider-only cases must be excluded from base-rate ROE
statistics** — this is standard RRA practice and it is an ingestion-time
classification, not a query-time filter.

**3.5 Vintage.** Cost of capital is a function of contemporaneous interest rates
and market conditions. A 2013 authorized ROE and a 2025 authorized ROE are not
peers. Any precedent claim needs the order date visible; a stale precedent
presented without its date is a §6 grounding failure.

**3.6 Settlement vs. fully litigated.** A settled outcome is a negotiated package
where parameters trade against each other; the stated ROE may be a plug that
makes a bargained revenue requirement arithmetically work. A litigated outcome
is a commission's reasoned finding and carries precedential weight a settlement
usually does not (settlements frequently include express non-precedent
language — *"this stipulation shall not be cited as precedent"* — which the
system should extract and honour). Note also, against intuition: RRA finds **no
consistent directional difference** in average authorized ROE between settled and
litigated cases, so the system must not editorialise a spread that the data does
not support.

**3.7 Utility size, credit rating, and capital program.** A small utility with a
modest capital plan and an A-rated giant mid-nuclear-build are not peers on
either ROE or equity ratio.

**3.8 Capital structure.** Comparing ROEs without comparing equity ratios is the
most common analyst error in this domain. The economically meaningful comparison
is the overall ROR, or ROE-at-a-common-equity-ratio.

**Design consequence.** Comparability is not a similarity score over embeddings.
Embedding similarity will happily rank a 2011 Georgia vertically-integrated
litigated case as "similar" to a 2025 Massachusetts distribution-only settlement
because the prose is near-identical — rate case testimony is highly formulaic.
**Comparability must be a structured, explicit predicate over extracted metadata,
surfaced to the user, with the non-matching dimensions named.** If the
architecture treats this as a retrieval-ranking problem, it has built harm #1.

---

## 4. Numeric precision traps

Each of these is a place where a fluent, confident, wrong number is easy to
produce. Each should become a test case.

**4.1 Requested vs. authorized vs. settled ROE.** Three different numbers in the
same docket, typically spanning 150+ bp, all appearing in documents that use
nearly identical sentences. Plus a fourth state: **the black-box settlement**,
where the parties agree on a revenue increase and deliberately **do not specify**
an ROE or the underlying parameters. Some states preclude black-box treatment and
require the values to be stated; many do not. For a black-box case the correct
answer to "what ROE was authorized?" is *"the settlement did not specify one"* —
**never** a number back-solved from the revenue requirement, and never a number
borrowed from the utility's request. This is `claim_status = NOT_STATED` (§2.4)
and it is a first-class refusal path, not an error.

**4.2 Gross vs. net rate base.** Gross plant, net plant (after accumulated
depreciation), and rate base (after ADIT, plus working capital and regulatory
assets) can differ by 30–50%. All three appear on adjacent lines of the same
schedule. Also: **total company vs. jurisdictional** rate base (§4.6), and
**test-year-end vs. average** rate base — states differ on which they use, and
the difference is real money for a utility with a large capital program.

**4.3 Total revenue requirement vs. incremental increase.** "A $2.1 billion rate
case" almost always means the *increase*, while "$2.1 billion revenue
requirement" means the total. Press coverage and executive summaries blur these
constantly. Store both, never derive one silently. Also watch: increases stated
as a **percentage** (of what base?), as a **residential bill impact** ($/month at
some assumed usage), and as **$/kWh** — four different numbers describing one
outcome.

**4.4 Percentages vs. basis points.** "The commission reduced ROE by 25" is
25 bp = 0.25%, not 25%. Also "a 0.5% increase in ROE" (ambiguous: 50 bp, or a
relative 0.5%?). Any extracted delta needs an explicit unit field.

**4.5 Nominal vs. real; and pre-tax vs. after-tax.** ROE is nominal and
after-tax. The revenue requirement is pre-tax, reached via a revenue conversion
factor of roughly 1.3–1.4×. Quoting a return-level deficiency as a revenue-level
number overstates by ~35%. Depreciation studies and escalation factors introduce
real-vs-nominal confusion separately.

**4.6 Jurisdictional vs. total-company allocation.** Under the Federal Power Act,
FERC has jurisdiction over wholesale sales and interstate transmission; states
have retail rates. A utility's total-company revenue requirement is split, and a
state rate case concerns only the **retail jurisdictional** portion. Multi-state
utilities split further by state. A total-company number answered to a
"what did [state] authorize" question can be wrong by a factor of two or more,
and it will look entirely plausible.

**4.7 Rate-year vs. calendar-year, and multi-year steps.** Multi-year plans grant
staged increases (year 1 / year 2 / year 3). "The 2024 increase" is ambiguous
between the year of the order and the rate year. Store effective dates.

**4.8 The one-number-many-classes trap.** A "9.5% increase" is a system-average.
The residential increase, the industrial increase and the change in the
residential fixed customer charge are all different, and rate design is where
the political heat is. Never let a class-specific question be answered with the
system average.

---

## 5. Risk register

Numbered so downstream agents (`solution-architect`,
`responsible-ai-architect`, `test-agent`, `synthetic-data-agent`) can cite them.
Each is phrased to become a test case.

**RCA-R1 — The ask presented as the outcome.**
Retrieval hits utility direct testimony requesting 10.9% ROE; the system answers
"the authorized ROE was 10.9%." *Test:* ask for the authorized ROE in a case
whose corpus contains both the application and the final order, and assert the
answer comes from the order and cites `document_type = FINAL_ORDER`. Assert also
that the requested figure, if mentioned, is explicitly labelled as requested.

**RCA-R2 — Cross-jurisdiction blending.**
Question about state A; the system answers using cases from states B and C
because the prose is similar. *Test:* ask a jurisdiction-scoped question where
the corpus holds cases only from other jurisdictions; require either refusal or
an answer that names the jurisdictional mismatch in the answer body, not only in
a badge.

**RCA-R3 — Structurally non-comparable peer set.**
The system builds a "peer average ROE" mixing vertically-integrated and
distribution-only cases (the ~34 bp structural gap of §3.2), or mixing rider
cases into base-rate statistics. *Test:* a corpus with a known mix; assert any
aggregate names its inclusion criteria and excludes rider-only proceedings.

**RCA-R4 — Superseded order treated as current.**
An order on rehearing revised the authorized ROE downward; the original order is
still in the corpus and ranks higher on similarity. *Test:* ingest an order plus
its order on rehearing; assert the answer reflects the amended figure and that
the superseded document is either suppressed or explicitly labelled superseded.
This requires a supersession link in the schema — it cannot be fixed at query
time.

**RCA-R5 — Black-box settlement back-solved.**
Asked for the authorized ROE in a black-box settled case, the system produces a
number by inference from the revenue requirement, or silently substitutes the
requested ROE. *Test:* a synthetic settled case with no stated ROE; the only
passing answer states that the settlement did not specify one. A `null` that
renders as "unknown — parse failure" also fails; the required state is
`NOT_STATED`.

**RCA-R6 — The extrapolation trap (rate-case analogue of
`policy-lookup-assistant` DOMAIN_KB risk #6; named as a required regression test
in `PROJECT_CONTEXT.md`).**
The user asks for the authorized ROE for a **jurisdiction × test-year-convention
combination the corpus does not contain** — e.g. "what ROE have forward-test-year
cases in [state X] been authorized since 2023?" where the corpus holds (a) a
[state X] *historical*-test-year case and (b) a *forward*-test-year case from a
neighbouring state. Both retrieve strongly. Both are individually true. A
plausible blend — "around 9.7%" — is fluent, well-sourced-looking, defensible-
sounding, and **is the catastrophic harm**, because it is precisely the number a
strategy lead would set an ask against.
*Test:* construct exactly this corpus gap and assert the sentinel refusal fires,
with the refusal naming the missing dimension ("the corpus contains no
forward-test-year case from [state X]") rather than a generic "insufficient
information." A refusal that does not say *what* is missing sends the user to
guess, which reproduces the harm outside the tool.

**RCA-R7 — Silence read as clearance.**
The system reports no comparable precedent risk because it examined nothing, and
the UI is identical to the case where it examined 40 cases and found nothing.
Directly the A7.2 harm #3 and `PROJECT_CONTEXT.md` standing constraint 4.
*Test:* two queries — one with rich coverage, one with none — must produce
visibly different coverage statements ("checked N, flagged M, could not assess K
because…"), not two empty flag lists.

**RCA-R8 — Orphan exhibit number.**
A number extracted from a schedule chunk that lost its parent filing's identity,
attributed to the wrong case or the wrong claim status. *Test:* assert every
retrievable chunk carries case identity, document type and claim status
inherited at ingestion; assert an exhibit with no resolvable parent fails ingest
loudly rather than entering the store.

**RCA-R9 — Unit and scope confusion.**
Basis points as percent; total revenue requirement as the increase; total-company
as jurisdictional; system-average increase as the residential increase (§4).
*Test:* one assertion per trap in §4.1–§4.8, each with a fixture where the wrong
reading is available in an adjacent chunk.

**RCA-R10 — Stale precedent, no vintage.**
A 2012 authorized ROE offered as current market evidence. *Test:* every precedent
claim renders an order date; assert an answer whose supporting cases are all
older than a configured threshold says so.

**RCA-R11 — Confidential discovery in the "public" corpus.**
A protected-version data-request response, or a document filed under protective
order, ingested as public because it was reachable on the commission's site.
Distinct from the work-product wall and not covered by it.
*Test:* assert ingestion classifies and can exclude protected-treatment
documents; assert a confidential-flagged document is not retrievable in a
public-corpus session.

**RCA-R12 — Non-precedent settlement language ignored.**
A settlement expressly stating it shall not be cited as precedent is cited as
precedent. *Test:* fixture with the clause; assert the caveat surfaces with any
answer relying on that case.

**RCA-R13 — The docket is a moving target.**
A case cited as an outcome is still pending; or the scheduled ingestion job
silently stops and the corpus goes stale while answers stay confident (the
independent-failure argument for treating ingestion as a surface, per
`PROJECT_CONTEXT.md`). *Test:* assert case status (`pending` / `decided` /
`withdrawn`) is stored and that a pending case cannot produce an `AUTHORIZED`
claim; assert corpus as-of dates are surfaced and a stale corpus is visible.
Note that cases can be **withdrawn** mid-stream — PECO withdrew rate cases in
Pennsylvania in 2026 — leaving a full docket of persuasive testimony and **no
outcome at all**. A withdrawn case is a live source of RCA-R1.

**RCA-R14 — Formulaic prose defeats retrieval.**
Rate case testimony is highly templated; a DCF cost-of-capital section reads
nearly identically across utilities and decades. High embedding similarity
therefore carries little discriminating signal. *Test:* assert that a query
naming a specific utility/state/year does not return top-ranked chunks from a
different utility/state/year without metadata filtering.

---

## 6. What "grounded" must mean here

`INTAKE.md` A7.3 makes grounding mandatory. In this domain a citation is
defensible in filed testimony only if it resolves to **all** of the following.
This is the acceptance bar, and it is stricter than
`policy-lookup-assistant`'s.

A rate-case citation must resolve to:

1. **Commission** — the specific state commission (or FERC).
2. **Docket number** — in that commission's own format, the identifier a human
   can paste into the commission's docket system.
3. **Document identity** — which filing within the docket, and, for orders, the
   order number and date; for testimony, the witness name.
4. **A locator inside the document** — page/line, schedule number, or finding-of-
   fact number. Rate case testimony is line-numbered *specifically so it can be
   cited this way*, and orders contain numbered findings for the same reason.
   "Somewhere in a 400-page order" is not a citation.
5. **`document_type`** from the §2.3 enum, displayed as label text (never colour
   alone, per the inherited UI pattern).
6. **`claim_status`** from the §2.4 enum — whether the number was requested,
   recommended, settled, authorized, implemented, or not stated.
7. **Date** — order date or filing date, so vintage (§3.5) is visible.
8. **Verbatim support** — the quoted or extracted text must actually contain the
   claim. Note the taxonomy from the 2025 legal-sanctions literature: three
   distinct failure kinds are (a) citation to a nonexistent source, (b)
   fabricated citation to a real source, and (c) **a real quote from a real
   source that does not support the proposition**. Only (a) is caught by
   checking that the docket exists. (c) is the one that will reach filed
   testimony.

Consequences to carry into Architecture:

- **Citation resolvability must be mechanically verifiable, not asserted.** A
  citation that cannot be round-tripped against ingested corpus metadata should
  fail closed. `PROJECT_CONTEXT.md` already flags as an open item that
  `policy-lookup-assistant`'s `sources[] = what retrieval pulled` trade-off is
  **not** inherited here. I agree, and I'd put it more strongly: given point 8(c)
  above, showing retrieval hits beside a claim is not merely imprecise, it
  actively manufactures the appearance of support. It should be treated as a
  blocking design question at Architecture, not a nice-to-have.
- **Refusal must name the gap.** Per RCA-R6, "I don't have enough information"
  is a weak refusal in a domain where the user will then guess. The refusal
  should state which dimension of the question the corpus does not cover.
- **The stakes are documented, not hypothetical.** Roughly 712 judicial decisions
  worldwide have now addressed hallucinated citations, about 90% of them in 2025;
  sanctions in 2025 included attorney disqualification and bar referral
  (*Johnson v. Dunn*, N.D. Ala.), following *Mata v. Avianca* (S.D.N.Y. 2023).
  Regulatory commissions are quasi-judicial bodies with the same intolerance for
  fabricated authority, and a utility's credibility with its commission is a
  multi-decade asset. That is A7.2 harm #2, and it is why the sentinel-refusal
  mechanism's property of **discarding the model's prose entirely on refusal**
  matters more here than it did in `policy-lookup-assistant`.

---

## 7. Sources

- NARUC, Ratemaking Fundamentals and Principles (Commissioner's Desk Reference) — https://www.naruc.org/commissioners-desk-reference-manual/3-ratemaking-fundamentals-and-principles/
- NARUC, Revenue Requirements, Rate Base and Cost of Capital — https://pubs.naruc.org/pub.cfm?id=53739F56-2354-D714-519C-4F8320738A03
- NARUC, Methodology of Cost Allocation (Kliethermes) — https://pubs.naruc.org/pub.cfm?id=538103FD-2354-D714-5105-6C8824D830B9
- NARUC, Ratemaking in the U.S. (Bryant, PUC of Texas) — https://pubs.naruc.org/pub.cfm?id=53768A01-2354-D714-517A-DC3B4EC72920
- NARUC, Future Test Years: Evidence from State Utility Commissions — https://pubs.naruc.org/pub/FA86C105-05F5-9766-BC78-29829AC50361
- Jamison (PURC, Univ. of Florida), Rate of Return Regulation — https://bear.warrington.ufl.edu/centers/purc/docs/papers/0528_jamison_rate_of_return.pdf
- Regulatory Assistance Project, "Dividing the Pie: Cost Allocation, the First Step in the Rate Design Process" — https://www.raponline.org/wp-content/uploads/2023/09/appendix-a-smart-rate-design-2015-aug-31.pdf
- RAP, Decoupling Design: Customizing Revenue Regulation to Your State's Priorities — https://www.raponline.org/knowledge-center/decoupling-design-customizing-revenue-regulation-state-priorities/
- ACEEE, A Decade of Decoupling for US Energy Utilities — https://www.aceee.org/files/pdf/collaborative-reports/decade-of-decoupling.pdf
- RMI Electricity Affordability Toolkit, Revenue Decoupling — https://affordability-toolkit.rmi.org/policies/revenue-decoupling
- NY DPS, Major Rate Case Process Overview — https://dps.ny.gov/major-rate-case-process-overview
- Indiana URC, Rate Case Overview and Process — https://www.in.gov/iurc/about-us/rate-case-overview-and-process/
- SC Office of Regulatory Staff, Rate Case Process Definitions — https://ors.sc.gov/consumers/how-rate-case-process-works/definitions
- RRA / S&P Global Regulatory Focus, quarterly decided-rate-case updates (2025 ROE averages; settled vs. litigated comparison) — https://psc.ky.gov/pscecf/2025-00114/kyle.j.smith124.civ@army.mil/09232025013307/MPG_Copyright_Protected_WP_27.pdf and https://efis.psc.mo.gov/Document/Display/53586
- S&P Global Market Intelligence, "Electric beats gas in exceeding authorized equity returns over past 15 years" (black-box settlements) — https://www.spglobal.com/market-intelligence/en/news-insights/research/electric-beats-gas-in-exceeding-authorized-equity-returns-over-past-15-years
- S&P Global Market Intelligence, "PECO withdraws rate cases as Pa. regulators begin to consider other new filings" — https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/05/peco-withdraws-rate-cases-as-pa-regulators-begin-to-consider-other-new-filings
- Wikipedia, Used and Useful Principle — https://en.wikipedia.org/wiki/Used_and_Useful_Principle
- PwC Viewpoint, Utilities & Power accounting guide, ch. 18 (utility plant, CWIP, AFUDC) — https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/utilities_and_power_/utilities_and_power__US/chapter_18_regulated_US/183_allowance_for_fu_US.html
- Manhattan Institute, "The Hidden Tax on Your Power Bill: Construction Work in Progress" — https://manhattan.institute/article/the-hidden-tax-on-your-power-bill-construction-work-in-progress
- National Law Review, "Is the Future Test Year History?" — https://natlawreview.com/article/future-test-year-history
- MOST Policy Initiative, Future Test Year science note — https://mostpolicyinitiative.org/science-note/future-test-year/
- US DOE, Federal-State Jurisdictional Split — https://www.energy.gov/sites/prod/files/2017/01/f34/Federal%20State%20Jurisdictional%20Split--Implications%20for%20Emerging%20Electricity%20Technologies.pdf
- EPA, Power Market Structure (restructured vs. vertically integrated) — https://www.epa.gov/green-power-markets/power-market-structure
- Wilkinson Barker Knauer, The Vertically Integrated Utility (white paper) — https://www.wbklaw.com/wp-content/uploads/2020/10/Vertically-Integrated-Utility-White-Paper-10.26.20.pdf
- SD PUC docket EL22-017, Guide to the Electric Class Cost of Service Study — https://puc.sd.gov/commission/dockets/electric/2022/el22-017/Vol2/CJBSch2.pdf
- Sterne Kessler, "AI Hallucinations in Court Filings and Orders: A 2025 Review of Sanctions" — https://www.sternekessler.com/news-insights/insights/ai-ip-year-in-reviewai-hallucinations-in-court-filings-and-orders-a-2025-review-of-sanctions-across-the-courts-and-rule-proposals/
- Damien Charlotin, AI Hallucination Cases Database — https://www.damiencharlotin.com/hallucinations/
- Bloomberg Law, "AI-Faked Cases Become Core Issue Irritating Overworked Judges" — https://news.bloomberglaw.com/legal-ops-and-tech/ai-faked-cases-become-core-issue-irritating-overworked-judges
