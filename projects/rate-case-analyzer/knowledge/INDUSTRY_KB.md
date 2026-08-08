# Industry Knowledge Base: US Regulated Electric Power Utilities & State Public Utility Commissions

Owner: `industry-expert`
Industry answered at Intake (A4.2): **Regulated power utilities (electric; gas
adjacency not excluded)** — and, inseparably, the **state public utility
commissions** that regulate them. Written at the Intake gate, 2026-08-07.

Scope: this KB covers industry/business-sector context — how the regulatory
market actually works, what is moving in it right now, what AI adoption in
regulatory affairs genuinely looks like, and the compliance/professional-conduct
obligations that bear on a tool whose output may end up inside filed testimony.
It is the companion to `functional-agent`'s `DOMAIN_KB.md`, which owns the
*domain mechanics* (revenue requirement, rate base, capital structure, test-year
math). Read both before Plan & Backlog.

A second, decision-forcing deliverable lives in **Section 6: Jurisdiction
Recommendation** — the named commissions to ingest, left deliberately
unresolved at Intake (A6.1b) for this agent to research.

---

## 1. The regulatory landscape

### 1.1 What a rate case is, structurally

A utility asks its state commission to approve (a) the total dollars it needs to
run the system — the **revenue requirement** — and (b) how those dollars are
collected across customer classes — **rate design**. The proceeding is run much
like a court case: formal intervention, written testimony, discovery, hearings
with cross-examination, briefs, and a written order. The commission's own staff
of economists, engineers and accountants reviews the filing independently of the
commissioners. ([Red Clay industry primer](https://redclay.com/industry-101-regulation-in-the-electricity-industry-rate-case-process/);
[Colorado PUC, Electric Rate Cases](https://puc.colorado.gov/electric-rate-cases))

**Why this matters to the product**: a rate case docket is not a document
collection, it is an *adversarial record*. The same number — say a proposed ROE
of 10.4% — appears in the utility's direct testimony as a request, in staff
testimony as a rebutted claim, in an intervenor brief as an attack, in a
settlement as a possibly-unstated compromise, and in the final order as an
authorization. Treating these as interchangeable "sources about ROE" is the
mechanism of harm #1 in `INTAKE.md`. The corpus needs a **document-role**
dimension (as-filed / rebuttal / staff / intervenor / settlement / order) and a
**posture** dimension (requested / recommended / stipulated / authorized) or the
grounded-Q&A layer will confidently cite a request as an outcome.

### 1.2 The standing participants

Nearly every US electric rate case has the same cast, and each has a predictable
institutional position that a precedent tool should surface rather than flatten:

| Participant | Role | Predictable posture |
|---|---|---|
| **The utility** | Applicant, carries burden of proof (e.g. 66 Pa.C.S. § 315 places it on the utility) | Maximal defensible ask; future test year where allowed |
| **Commission staff / trial staff** | Independent technical review; in some states a formal litigating party, in others advisory to commissioners | Cuts to O&M, rate base disallowances, lower ROE |
| **Consumer advocate** | Statutory ratepayer representative (PA Office of Consumer Advocate, CA Public Advocates Office, TX Office of Public Utility Counsel, NY Utility Intervention Unit) | Residential bill impact, ROE and capital structure |
| **Industrial / large-customer intervenors** | Manufacturers' and large-load coalitions | Cost allocation and class cost-of-service — they fight about *who pays*, not only *how much* |
| **Environmental / clean-energy intervenors** | NRDC, Sierra Club, Earthjustice, state equivalents | Prudence of fossil capital, decoupling, DER and rate-design terms |
| **Municipal / low-income / faith coalitions** | Increasingly active as affordability politics sharpen (Section 2.8) | Disconnection policy, low-income tariffs, affordability |

Consequence for retrieval: an intervenor brief is *advocacy*, not authority. The
authority enum that `PROJECT_CONTEXT.md` says must be built fresh for this corpus
should be **ranked**, with commission order at the top and intervenor brief near
the bottom — and the ranking must be visible in the UI, because an
authoritative-looking citation to a losing party's brief is exactly harm #2.

### 1.3 Lifecycle and typical timeline

A generic fully-litigated case runs roughly **9–12 months** from filing to order,
though statutory clocks vary sharply by state (this variation is itself a reason
to pick contrasting jurisdictions):

1. **Pre-filing** — internal case development, sometimes a required notice period.
2. **Filing / suspension** — utility files; commission suspends the proposed
   tariff. Statutory suspension periods are the real clock: Pennsylvania's is
   effectively 9 months (7-month suspension after a 60-day notice); Michigan's
   statute imposes a 10-month deadline with utility self-implementation
   permitted after 6 months.
3. **Discovery / data requests** — months of interrogatories. Volume here is
   enormous and is where confidential material concentrates (Section 4).
4. **Staff and intervenor direct testimony** (roughly months 5–7), then utility
   rebuttal, then surrebuttal.
5. **Evidentiary hearings** before an ALJ or the commission, with cross-examination.
6. **Settlement negotiation** — runs in parallel, not sequentially, and can
   land at almost any point up to and sometimes after briefing.
7. **Briefing** — initial and reply briefs; ALJ recommended decision or
   proposed decision.
8. **Commission deliberation and final order** at a public meeting.
9. **Compliance filing** — tariffs implementing the order. In the PPL Electric
   2026 case, compliance tariffs implemented approved rates for service on and
   after July 1, 2026 following a five-business-day settlement withdrawal window.
   ([PA PUC](https://www.puc.pa.gov/press-release/2026/puc-issues-decision-in-ppl-electric-rate-proceeding-06042026))
10. **Rehearing / appeal** — rare but real; an order on appeal is not settled law.

**Ingestion consequence**: step 9 is where the *actual authorized numbers* often
live in usable tabular form, and step 10 means an order can be superseded. A
corpus with no notion of procedural stage will happily answer a 2026 question
with a document that was later vacated.

### 1.4 Settlements dominate — and they hide the numbers

This is the single most important structural fact for capability #3 (deferred)
and a serious one for capability #2 (in MVP).

Settlements have been the dominant resolution path in many states for years, and
a large share of them are **"black box" settlements** that state a total revenue
increase without specifying ROE, capital structure, or the individual issue
resolutions that produced it. A partial black box settles some terms and leaves
others explicit. Examples: SPS/PUCT Staff/intervenors filed a black box
settlement in December 2023 with a $65M base rate increase effective back to
July 2023; an earlier 2020 SPS settlement was similarly unopposed and black box.
([SEC filings via search; Xcel/SPS 8-Ks](https://www.sec.gov/Archives/edgar/data/72903/000007290324000092/xcelearningsreleaseq12024.htm))

Recent 2026 evidence that settlement is the norm, not the exception:

- **PPL Electric (PA, 2026)** — settled at **$275M**, about **23% below** the
  $356.3M originally sought, and the settlement bundled a data-center tariff
  and raised storm expense recovered in base rates from $20M to $32M annually.
  ([Utility Dive](https://www.utilitydive.com/news/ppl-electric-rate-case-settlement-data-center-tariff/814760/))
- **Dakota Electric (MN)** — settlement approved by the Minnesota PUC.
  ([Grand Rapids Herald-Review](https://www.grandrapidsmn.com/business/minnesota-public-utilities-commission-approves-settlement-for-dakota-electric-rate-case/article_2a71c967-1ac4-4f38-9792-dd29ca93dbe8.html))
- **Florida Power & Light (Nov 2025)** — 10.95% ROE via **settlement**, among
  the highest recent authorizations.

**Three hard implications, and they are product requirements, not trivia:**

1. **A black box settlement has no extractable ROE.** Any pipeline that expects
   an ROE per case will either drop these cases silently or, worse, impute one.
   The correct behaviour is an explicit `not stated in settlement` value that
   propagates to the UI — this is the concrete form of the Intake standing
   constraint "silence is not clearance."
2. **Settlement outcomes are not precedent in the legal sense.** Most settlement
   approvals recite that the settlement is approved without the commission
   adopting any party's position or establishing precedent. A tool that reports
   "the commission approved a 9.8% ROE in the X settlement" as precedent is
   making a claim the document itself disclaims. **This disclaimer language
   should be extracted and surfaced**, not stripped as boilerplate.
3. **Settlement rates are a jurisdiction attribute, not a global constant.**
   Contrast on settlement culture is a legitimate axis for jurisdiction
   selection (Section 6). *Note: I found abundant case-level evidence of
   settlement dominance but did not find a citable, current published
   settled-vs-litigated percentage — RRA/S&P holds that data behind a paywall.
   Do not let any downstream artifact state a percentage as fact.*

### 1.5 Test year: the convention that makes cross-jurisdiction comparison hard

Three broad conventions, and they are not comparable without adjustment:

- **Historical test year** — actual costs from a completed 12-month period,
  sometimes with limited known-and-measurable adjustments (Texas TDUs).
- **Forecast / future test year** — projected costs for the period rates will be
  in effect (California GRC, many others).
- **Fully projected future test year (FPFTY)** — Pennsylvania's, authorized by
  Act 11 of 2012, projecting revenues, expenses and capex for the 12 months
  beginning when new rates take effect. The PA PUC finalized FPFTY filing
  requirements in a Final Form Rulemaking Order released January 8, 2025.
  ([Morgan Lewis](https://www.morganlewis.com/pubs/2025/05/pa-public-utility-commissions-fully-projected-future-test-year-filing-requirements-advance-at-irrc);
  [PA PUC](https://www.puc.pa.gov/press-release/2017/puc-seeks-comments-on-proposed-procedures-and-filing-requirements-for-utilities-using-a-fully-projected-future-test-year))

**This is a first-class metadata field.** "Peer utilities got X" is meaningless
across a historical/FPFTY boundary without saying so. Recommend test-year
convention be a required, closed-enum ingestion field with fail-loud behaviour,
exactly like the authority enum.

### 1.6 Vertically integrated vs. restructured — the deepest structural split

- **Vertically integrated** (most of the Southeast, West, and Midwest): the
  utility owns generation, transmission and distribution; the rate case covers
  all of it, plus fuel/purchased-power via a separate adjustment clause.
- **Restructured / retail choice** (Texas ERCOT, Pennsylvania, Illinois, Ohio,
  most of the Northeast): generation is competitive; the regulated utility is a
  **wires-only** distribution (and sometimes transmission) company. Its base
  rate case has **no generation rate base and no fuel** — the revenue
  requirement is structurally smaller and composed differently.

A precedent question like "what O&M-to-rate-base ratio did peers get approved"
is meaningless across this boundary. Cross-jurisdiction comparison is the
product's core value, so **the corpus must carry this attribute and the answer
layer must refuse or caveat comparisons that cross it.** This is the strongest
single argument for the contrast-based jurisdiction selection Intake asked for.

### 1.7 Between-case mechanisms — where the money increasingly moves

Base rate cases are no longer the only, or in some states even the main, event:

- **Riders / trackers / interim adjustments** — Texas DCRF lets a utility adjust
  for distribution capital between comprehensive base-rate proceedings, no more
  than four times between them (16 TAC § 25.243); TCOS does the analogous job
  for transmission. ([Texas Administrative Code](http://txrules.elaws.us/rule/title16_chapter25_sec.25.243))
- **Formula rate plans** — Louisiana, Mississippi and Alabama adjust rates
  annually against a formula rather than through a full case. Alabama Power's
  **RSE** sets authorized ROE off 30-year Treasury yields plus 6%, adjusts to
  hold actual ROE within 0.5% of authorized, and caps residential increases at
  2.5%/year.
- **Multi-year rate plans (MYRP) and performance-based regulation (PBR)** —
  see Section 2.6.

**Product consequence**: a jurisdiction where the action lives in riders will
look deceptively quiet if you only ingest base rate cases. That is a coverage
gap the tool must *state*, not silently exhibit.

---

## 2. Current trends shaping rate cases in 2025–2026

This section exists to answer one question: **why is a 2018 precedent dangerous
to cite in 2026?** Because nearly every driver of the revenue requirement, and
the politics around it, has changed direction since then.

### 2.1 Data-center load growth is the dominant story

After ~two decades of flat load, demand forecasts have inverted. S&P Global puts
US utility capex near **$1.3 trillion for 2026–30** on surging demand, and other
2026 trackers put the AI-data-center-driven figure at **$1.4T with a ~27% capex
surge**. ([S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/surging-energy-demand-puts-us-utility-capex-forecast-near-1-3t-in-2026-30);
[tech-insider](https://tech-insider.org/us-utility-1-4-trillion-ai-data-center-energy-2026/))

The rate-case-visible consequence is a genuinely new document class: **large-load
/ data-center tariffs**, with minimum-take provisions, contract terms, exit fees
and collateral requirements designed to stop cost-shifting onto residential
customers. PPL's 2026 settlement included one. In March 2026 Amazon, Google,
Meta, Microsoft, Oracle, OpenAI and xAI signed a "ratepayer protection pledge"
committing that data-center growth would not raise household bills. Utilities
themselves are visibly divided on data centers even as affordability pressure
mounts. ([Utility Dive Q1 2026 roundup](https://www.utilitydive.com/news/2026-q1-earnings-utilities-data-centers-affordability/820079/);
[E3 analysis](https://www.ethree.com/wp-content/uploads/2026/05/Understanding-the-Drivers-of-Rising-Electricity-Rates-and-the-Role-of-Data-Centers_E3-2026.pdf))

**Staleness implication**: there is essentially no useful pre-2023 precedent on
large-load tariff design. A corpus weighted to older cases will answer
large-load questions from nothing, or from analogy — the extrapolation trap that
`PROJECT_CONTEXT.md` already flags for porting as a regression test.

### 2.2 Grid hardening and wildfire mitigation

Wildfire has moved from a Western anomaly to a central cost-recovery and
liability question. Notably, **California's regulatory ranking improved in 2026,
reflecting constructive treatment of incremental wildfire liabilities** — i.e.
the regulatory *risk* signal on wildfire has been moving, not static. Undergrounding,
covered conductor, PSPS operations and vegetation management are now large,
contested capital and O&M line items with their own prudence standards.

### 2.3 Storm cost recovery

Increasingly a named, separately-tracked component rather than buried in O&M.
The PPL 2026 settlement raised reportable-storm expense recovered in base rates
from **$20M to $32M annually**. Securitization of extraordinary storm costs
(post-Uri Texas, post-hurricane Gulf states) is now routine and creates
documents that look like rate cases but are financing orders — a document-type
classification hazard for ingestion.

### 2.4 Tax: normalization and post-IRA effects

- **Normalization** rules require matching tax effects to rate recovery via
  ADIT; flow-through of accelerated-depreciation benefits to ratepayers violates
  them and puts the utility's ability to claim accelerated depreciation at risk.
  ([PwC Viewpoint 19.3](https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/utilities_and_power_/utilities_and_power__US/chapter_19_regulated_US/193_normalization_US.html))
- **Excess ADIT** from the TCJA rate cut (35% → 21%) is still being amortized
  back to customers under **Rev. Proc. 2020-39** conventions — a recurring,
  case-specific revenue-requirement reduction.
  ([Rev. Proc. 2020-39](https://www.irs.gov/pub/irs-drop/rp-20-39.pdf);
  [Lucasys](https://www.lucasys.com/blog/revenue-procedure-2020-39-and-the-future-of-edit))
- **IRA's Corporate Alternative Minimum Tax** — 15% on adjusted financial
  statement income for corporations averaging over $1B AFSI, for tax years
  beginning after Dec 31, 2022 — plus transferable/direct-pay credits, change
  the effective tax rate and cash-tax position embedded in the revenue
  requirement. ([IRS](https://www.irs.gov/inflation-reduction-act-of-2022/corporate-alternative-minimum-tax);
  [CRS R47328](https://www.congress.gov/crs-product/R47328))

**This is the cleanest example of the staleness thesis**: a tax gross-up or
income-tax expense figure from a pre-2018 case is not merely dated, it is
computed under a different statutory rate. Any comparison feature that does not
carry the order date prominently is manufacturing errors.

### 2.5 ROE: the numbers, and the direction of travel

Grounded figures worth carrying (with dates attached — never quote these
without the date):

- Average authorized electric ROE has sat around **9.5–9.7%** in 2024–2025.
- RRA reported **9.60% average for cases decided in 2023**, up from **9.54% in 2022**.
- **January 2026**: five proceedings ranged **9.40% (New York) to 10.00% (Missouri)**.
- **Nov 2025**: FPL **10.95%** (settlement); Dominion Virginia biennial 2026–27 **9.80%**;
  Northern Illinois Gas and AEE-Illinois **9.60%**.
- **March 2026**: FERC cut New England transmission owners' allowed ROE to
  **9.57%**, down from 10.57% set in 2014.
- **Dec 2025 / March 2026**: California reduced ROEs for all major electric and
  gas utilities, and cut Liberty Utilities by 25bp to **9.75%**.
- A 2026 Aii report argues both requested and authorized ROEs have trended
  **downward over two decades** and are not a driver of bill increases —
  a contested, advocacy-adjacent claim, flagged as such.
  ([PR Newswire / Aii](https://www.prnewswire.com/news-releases/new-aii-report-finds-utility-roes-have-trended-downward-over-two-decades-challenging-claims-that-returns-are-driving-electricity-bills-302818942.html);
  [S&P Global ROE analysis](https://www.spglobal.com/market-intelligence/en/news-insights/research/underearning-spread-widens-for-gas-electric-utilities-in-roe-analysis))

The important nuance is not the level but the **decoupling from interest rates**:
ROEs drifted down through a period of *rising* rates, so the naive
"rates went up, so ROE should go up" argument does not match the record, and
affordability politics is now actively pushing authorized ROE down
([Utility Dive: utility profits in the crosshairs](https://www.utilitydive.com/news/utility-profits-in-the-crosshairs-amid-affordability-concerns/825610/)).
S&P also reports a **widening underearning spread** — the gap between authorized
and actually-earned ROE — which is precisely the kind of thing a precedent tool
should let a strategy lead see, and precisely the kind of thing it must not
invent when the corpus lacks it.

### 2.6 Performance-based regulation and multi-year rate plans

**Seventeen states plus DC** have some formalized PBR, with roughly a dozen more
exploring it; **nine states are actively evolving or initiating PBR in 2026** —
Colorado, Hawaii, Illinois, Michigan, Minnesota, New York, Vermont, Virginia and
Washington. Illinois' Public Act 102-0662 (CEJA) lets ComEd and Ameren Illinois
file **four-year multi-year rate plans** with performance metrics; Ameren's
metrics for 2025–2027 include SAIDI and demand-response targets.
([EQ Research](https://eq-research.com/eq-publications/performance-based-regulation-states-to-watch/);
[RMI Affordability Toolkit](https://affordability-toolkit.rmi.org/policies/multi-year-rate-plans);
[LBNL](https://eta.lbl.gov/publications/state-performance-based-regulation);
[ICC Ameren 2024 metrics report](https://icc.illinois.gov/api/web-management/documents/downloads/public/Ameren2024PerfMetricsEvaluationReport.pdf))

**Product consequence**: in a MYRP state the "rate case" is a *plan* with
annual reconciliation and metric reports. A schema built only around
single-year revenue requirements will mis-model these badly.

### 2.7 Formula rate plans

See 1.7. The practical point for jurisdiction selection: a formula-rate state
generates thin, annual, highly structured filings rather than fat litigated
records — excellent for structured extraction, poor for testimony-style
precedent, and a genuinely different shape of corpus.

### 2.8 Affordability politics — the trend that changes what "winnable" means

This is the most under-modelled variable in any historical precedent set.

- Electricity rates are a live **2026 midterm** issue; Democrats won 2025
  gubernatorial races in Virginia and New Jersey partly on utility affordability
  messaging. ([Brookings](https://www.brookings.edu/articles/how-rising-electric-rates-could-affect-the-2026-midterms/);
  [E&E News](https://www.eenews.net/articles/electricity-rates-a-potent-political-issue-ahead-of-2026-midterms-2/))
- Normally-invisible **utility commissioner elections** are drawing unusual
  attention and money. ([US News](https://www.usnews.com/news/us/articles/2026-04-06/low-voltage-utility-elections-face-surge-of-attention-as-electricity-bills-rise))
- Protesters disrupted a Las Vegas conference of investor-owned utility
  executives in 2026; some regions have seen annual increases above 25%.
- Legislatures are intervening in **procedure**, not just outcomes: New York
  S.5593 would let the PSC extend rate case suspension to **fourteen months** to
  give the PSC and intervenors more scrutiny time.
  ([NY Senate](https://www.nysenate.gov/newsroom/press-releases/2026/state-senate-advances-legislation-stand-utility-corporations-lower))
- Michigan's 2026 cases (Consumers ~11%; DTE $574M / +$13.50 average monthly
  bill) land in a gubernatorial and Senate election year.

**The honest framing for the deferred capability #3**: approval likelihood is
partly a function of the *political* moment, which is not in the document corpus
at all. A model trained only on 2015–2022 filings will systematically
over-predict approval in 2026. This should be written into capability #3's
enhancement brief now, while it is cheap, rather than discovered later.

---

## 3. How AI is actually used in regulatory affairs today — real vs. marketing

### 3.1 What is genuinely deployed

- **HData** is the clearest real, named incumbent in this exact space: a
  regulatory intelligence platform for regulated energy, built around FERC
  Forms 1/2/6 and EIA data from 2011 forward with real-time ingestion of new
  FERC filings, serving utilities, regulators, advocates and advisory firms.
  There is a documented customer case of **witness preparation and
  cross-examination anticipation for rate cases** (John Cogburn, Southern
  Company Gas), and an announced **HData–Southern Company AI pilot**.
  Systrends acquired HData's compliance solution.
  ([HData](https://www.hdata.com/);
  [witness prep case study](https://blog.hdata.com/customer-story-witness-preparation-regulatory-ai);
  [Systrends acquisition](https://blog.hdata.com/press-releases/systrends-acquires-compliance-solution);
  [Southern Co. pilot](https://www.stocktitan.net/news/SO/h-data-and-southern-company-announce-ai-pilot-program-to-ck3crtrhqwbv.html))
  Read HData's founder's claim of having "no competitors" as vendor positioning,
  not a market fact — but the *FERC-data-first* orientation is real and is
  itself informative: the tractable structured data is federal, not state.
- **SAP "Rate Case Normalizer"** — cited in `policy-lookup-assistant`'s
  INDUSTRY_KB for automating cross-referencing of rate case filings against
  current requirements. Vendor-sourced claim; treat the time-savings number
  as marketing.
- **Commission-side AI** is emerging, not just utility-side: commissions are
  implementing configurable case management with AI-assisted document review,
  structured citizen intake, natural-language public-comment interfaces and
  high-impact-filing dashboards. A March 2026 brief for the California State
  Senate Energy Committee describes rate applications that "bury regulators in
  paper and deadlines," with a single GRC generating **tens of thousands of
  pages** of testimony and data requests.
  ([Speridian](https://www.speridian.com/blogs/regulatory-compliance-software-for-public-utility-commissions-managing-utility-regulation-in-ai-era/))
- **Horizontal legal AI** has arrived in this workflow by default — research,
  summarisation and drafting tools are in use by regulatory counsel whether or
  not anyone procured them for that purpose.

### 3.2 What is marketing

- "AI predicts your rate case outcome." No credible public evidence exists of a
  validated approval-likelihood model in this space. This is exactly the
  capability Intake deferred (A8.2), and the deferral looks well-judged: the
  outcome variable is dominated by settlement (which erases the numbers,
  Section 1.4) and by political conditions absent from the corpus (Section 2.8).
- Percentage time-savings claims (e.g. "35% faster regulatory analysis") come
  from consulting and vendor collateral, not controlled study.
- "Regulatory copilot that drafts your testimony." Drafting assistance is real;
  *unreviewed* drafting into a filed document is the sanction scenario in
  Section 4.2.

### 3.3 The regulator is now regulating AI, including the utility's own use

The **Arizona Corporation Commission opened the first formal state-level inquiry
into utility AI governance in early 2026**, covering rate base treatment,
cybersecurity and algorithmic transparency — a docket likely to be the template
others adapt. Combined with NYU CSMAP's "hidden regulators" finding that PUCs are
active AI watchers, the realistic expectation is that **a utility's use of AI in
preparing a filing may itself become a discoverable, commentable subject.**
That is an argument for the tool keeping a defensible provenance trail from day
one, not as a nice-to-have.

### 3.4 The honest read for this project

The niche this product occupies — **cross-jurisdiction state-level precedent
retrieval with hard citations** — is genuinely underserved, because the
incumbents optimise for federal structured data (FERC forms) where the data is
clean, and state docket PDFs are messy. That is a real opportunity and also a
warning: the reason it is underserved is that the ingestion is hard. Corpus
quality *is* the product, which is precisely why Intake sequenced #1 + #2 first.

---

## 4. Compliance and professional-conduct obligations

None of these is a named regulatory regime like HIPAA (consistent with Intake
A9.3 recording no formal compliance obligation). They are professional-conduct
and proceeding-level obligations, and they bite hard because the output can
enter filed testimony.

### 4.1 Verification and attestation of filed material

Filed testimony and applications generally carry a **verification or affidavit**
by the sponsoring witness attesting to truth and accuracy under penalty, and
counsel signs pleadings. The accountability chain is human and personal —
consistent with Intake A7.4. The design consequence: the tool must make
verification *possible*, which means every asserted fact must be traceable to a
retrievable source document with a citable location, not just a document-level
citation. A sponsoring witness cannot attest to a claim they cannot check.

### 4.2 AI-hallucinated citations are now a documented sanctions category

This is no longer hypothetical and the numbers are large. As of May 2026 a public
tracker recorded roughly **1,490 court decisions worldwide (1,000+ in the US)**
where a party relied on AI-hallucinated material and the court responded; by
June 2026 the tracker stood at **1,598**. Representative consequences:

- Nebraska, April 2026: an Omaha attorney **suspended** after a February 2026
  brief in which **57 of 63 citations were defective**, including 20 hallucinated
  cases and three fabricated decisions.
- Oregon: 15 fake citations and 8 fabricated quotations across three summary
  judgment briefs drew roughly **$109,700** in combined sanctions, fines and
  opposing fees.
- Seventh Circuit, March 30, 2026: addressed counsel's obligations and the
  *opposing* party's obligations on receiving such a pleading.
- The consistent finding across the tracker: **the cover-up draws the harsher
  penalty** than the original error.

([GC AI tracker](https://gc.ai/blog/ai-hallucination-legal-cases);
[Norton Rose Fulbright](https://www.nortonrosefulbright.com/en-us/knowledge/publications/792d8bf3/ai-in-litigation-update-on-gen-ai-sanctions-in-2026);
[Law.com — PA attorney suspended](https://www.law.com/thelegalintelligencer/2026/06/22/fed-court-suspends-pa-attorney-for-aihallucinated-citations/);
[NYSBA](https://nysba.org/beyond-the-mirage-beware-of-generative-ai-and-hallucinations/))

These are courts, not PUCs, but ALJ-run commission proceedings apply materially
the same candour expectations, and a commission is a repeat-player regulator
where credibility damage compounds across every future case — as Intake harm #2
already states. **This is the single strongest external justification for the
mandatory grounding and sentinel-refusal design.**

### 4.3 Attorney work product and privilege

Rate case preparation is typically conducted **under counsel's direction**
precisely so that draft analyses, strategy memos and consultant work fall within
attorney work-product protection. Two consequences:

- Ingesting real internal drafts into a shared system with any external or
  adverse access risks **waiver of protection** — a harm that is invisible until
  it is catastrophic. This is the legal underpinning of the ethical wall in
  `PROJECT_CONTEXT.md` standing constraint #2, and it is why "we had good RBAC"
  is a weak answer: waiver analysis asks who *could* have accessed, not who did.
- The project's decision to hold **only synthetic** internal history (A6.1)
  neutralises this for the MVP. That decision should be treated as a compliance
  control, not a convenience, and re-examined at any gate that proposes real
  work product.

### 4.4 Ex parte rules

Most commissions prohibit or strictly regulate substantive off-the-record
communication with decisionmakers in a contested proceeding, often with mandatory
disclosure filings for permitted contacts. Relevance to this tool:

- If the intervenor/commission-staff personas are ever brought in scope
  (currently out of MVP per A8.2), a shared system where parties can see each
  other's queries or a decisionmaker can see a party's material is an ex parte
  hazard in a new form. Deployment separation per party (Intake finding #4) is
  the mitigation.
- Ex parte *disclosure filings* are themselves a document type in the docket and
  will be swept up by an undiscriminating scraper. They are procedural, not
  substantive precedent, and should be classified out rather than retrieved as
  authority.

### 4.5 Protective orders and confidential material inside public dockets — a real ingestion hazard

**This is the most concrete technical compliance risk in the project and it
deserves explicit engineering attention.**

Commission protective orders let parties designate discovery and testimony as
confidential — typically trade secret or confidential commercial/research
information — with a good-faith obligation to designate only the qualifying
portions, and a challenge procedure where the designating party bears the burden.
Many orders have **two or more tiers**, with "Highly Sensitive Protected
Material" restricted to outside counsel, outside consultants under counsel's
direction, and specified employees authorised by the presiding officer.
([Oregon PUC Order 14-150](https://apps.puc.state.or.us/orders/2014ords/14-150.pdf);
[Texas PUCT protective order example](https://interchange.puc.texas.gov/Documents/32436_12_505126.PDF);
[PA PUC](https://www.puc.pa.gov/pcdocs/1874654.pdf))

Why it is a hazard *here specifically*:

1. **Confidential material lives inside otherwise-public dockets.** The docket is
   public; individual items in it are not. A crawler that treats "the docket is
   public" as a per-document permission is wrong, and being wrong is not a
   theoretical foul — it may breach a protective order that binds the parties,
   and it can put confidential competitor data into a utility's own system.
2. **The public/confidential pairing is a naming and versioning problem.** The
   normal pattern is a **public redacted version** and a **confidential
   unredacted version** of the same document. Ingestion must prefer the redacted
   public version and must not silently ingest both, or worse, dedupe to the
   confidential one.
3. **Redacted PDFs are unreliable.** Improper redaction — black rectangles over
   still-extractable text — is a recurring real-world failure. A text-extraction
   pipeline can surface content that the redaction was meant to remove, and the
   utility running the tool becomes the party in possession.
4. **Access-restricted items may still be listed.** A docket index may show an
   item whose file is not publicly retrievable. The pipeline must fail loud on
   a fetch that returns an access-denied or login page rather than storing the
   HTML error body as a document — a mundane bug with a serious signature.
5. **Terms of use and state records law** vary. Pennsylvania's Office of Open
   Records has directed the PA PUC to disclose documents in at least one
   dispute, which shows the public/non-public line there is contested and
   moving, not fixed. ([Buchanan Ingersoll & Rooney](https://www.bipc.com/no-secrets-office-of-open-records-directs-papuc-to-disclose-documents))

**Recommended control**: a confidentiality classification at ingestion, from
document-title/index metadata *and* first-page text scanning for protective-order
markings ("CONFIDENTIAL", "HIGHLY SENSITIVE", "SUBJECT TO PROTECTIVE ORDER"),
with **quarantine-and-report** rather than "flag and index." This belongs to
`security-architect` at Architecture; I am raising it as an industry-sourced
requirement, advisory as always.

### 4.6 Regulator-facing AI disclosure

Carried forward from `policy-lookup-assistant`'s INDUSTRY_KB and still current:
state AI-disclosure laws are proliferating and PUCs are active AI watchers
(NYU CSMAP). For *this* product the relevant question is narrower and sharper:
if AI-assisted analysis materially shaped filed testimony, is that disclosable
or discoverable? There is no settled answer as of August 2026. The defensible
posture is a retained provenance trail plus human attestation, which the design
already implies.

---

## 5. Obligation and constraint register

Numbered for downstream citation. Format: **IND-n**. Each is advisory from this
agent; the named gate owner rules.

| # | Obligation / constraint | Rationale (section) | Suggested owner |
|---|---|---|---|
| **IND-1** | Every retrievable unit carries **document role** (as-filed direct / rebuttal / staff / intervenor / settlement / order / compliance tariff / ex parte notice) as a closed enum, fail-loud on unknown. | 1.1, 1.3, 4.4 | `solution-architect` |
| **IND-2** | Every extracted numeric carries **posture**: requested / recommended / stipulated / **authorized**. A requested figure must never be rendered as an outcome. | 1.1 | `functional-agent`, `responsible-ai-architect` |
| **IND-3** | Authority enum is **ranked** with commission order highest and intervenor brief low, and the rank is visible in the UI (label text, never colour alone). | 1.2 | `experience-designer` |
| **IND-4** | **Test-year convention** (historical / forecast / FPFTY) is a required closed-enum field; comparisons across conventions must be caveated or refused. | 1.5 | `functional-agent` |
| **IND-5** | **Market structure** (vertically integrated / restructured wires-only) is a required field; cross-structure comparisons of revenue requirement composition must be caveated or refused. | 1.6 | `functional-agent` |
| **IND-6** | Black box settlements must yield an explicit **"not stated in settlement"** value that reaches the UI. Never impute, never omit silently. | 1.4 | `code-agent`, `responsible-ai-architect` |
| **IND-7** | Settlement **non-precedential disclaimer language** is extracted and surfaced alongside any settlement-derived figure. | 1.4 | `functional-agent` |
| **IND-8** | **Order date is mandatory and always displayed** with any figure. Tax-law, ROE-trend and load-forecast regime changes make undated figures actively misleading. | 2.4, 2.5 | `experience-designer` |
| **IND-9** | The corpus states its **coverage boundaries explicitly** — jurisdictions, date range, document types, and known exclusions such as rider/formula-rate proceedings — and the answer layer reports coverage per query ("checked N comparable cases…"). Direct implementation of Intake standing constraint #4. | 1.7, 2.6, 2.7 | `functional-agent`, `experience-designer` |
| **IND-10** | **Confidential-material quarantine**: classify at ingestion from index metadata plus first-page marking scan; prefer public redacted versions; never ingest an item marked CONFIDENTIAL / HIGHLY SENSITIVE / SUBJECT TO PROTECTIVE ORDER. Quarantine and report, do not index. | 4.5 | `security-architect` |
| **IND-11** | **Fail loud on non-document fetches.** An access-denied page, login redirect or error body must never be stored as a document. | 4.5 | `code-agent`, `test-agent` |
| **IND-12** | **Citations must be verifiable by a human at the point of use** — stable source URL plus in-document location — because a sponsoring witness must be able to check what they attest to. | 4.1 | `solution-architect` |
| **IND-13** | **No fabricated citation, ever**, enforced by the ported sentinel-refusal mechanism, with a red-team case explicitly modelled on the 2026 hallucinated-citation sanctions record. | 4.2 | `responsible-ai-architect` |
| **IND-14** | **Work-product isolation is a privilege-waiver control**, not merely access control. Retriever bound at session construction. The synthetic-only internal corpus is a compliance control and any proposal to hold real work product reopens this gate. | 4.3 | `security-architect` |
| **IND-15** | **Provenance trail retained** for any analysis that could inform filed material — which sources, which retrieval, when — anticipating that a utility's AI use may itself become discoverable or commentable (Arizona docket precedent). | 3.3, 4.6 | `solution-architect` |
| **IND-16** | **Political/affordability context is out-of-corpus.** Any future approval-likelihood feature must state this limitation prominently; a model fit on 2015–2022 filings will over-predict approval in 2026. Written into capability #3's enhancement brief now. | 2.8 | `plan-agent` (at enhancement) |
| **IND-17** | **Superseded-order awareness**: rehearing, appeal and subsequent orders can vacate or modify. Where detectable, later proceedings referencing an order should be surfaced; where not detectable, the limitation is stated. | 1.3 | `functional-agent` |
| **IND-18** | **Per-jurisdiction terms-of-use and rate-limit review before the scraper runs**, with polite crawl settings and identifiable user agent. Access posture is not verified for any candidate below and must be checked at Architecture. | 6.4 | `solution-architect`, `security-architect` |

---

## 6. Jurisdiction recommendation (Intake A6.1b)

**The ask**: 2–3 named commissions chosen for contrast *and* public-access
tractability, for human confirmation.

### 6.0 An honesty note on method

Everything below about URL shapes and document formats comes from **URL patterns
and documents observed in web search results**, plus official help pages. I did
**not** fetch, crawl or benchmark any commission system — my `Bash` grant is
scoped to running my own test suite only, and I will not exceed it to satisfy a
research question. Every tractability claim is therefore labelled
**OBSERVED** (a real URL or official statement seen in results),
**STATED** (the agency says so), or **UNVERIFIED** (inference).
Anything marked UNVERIFIED needs a one-hour ingestion spike before commitment —
which is the correct place to spend that hour, at the Architecture gate, not now.

### 6.1 Primary recommendation — ranked

#### 1. Pennsylvania Public Utility Commission (PA PUC) — *strongest overall*

**Contrast value**
- **Restructured / wires-only** distribution base rate cases — no generation
  rate base, no fuel. Structurally the cleanest contrast partner for a
  vertically-integrated state.
- **FPFTY** test year under Act 11 of 2012, with new filing requirements
  finalised in the January 8, 2025 Final Form Rulemaking Order — the most
  aggressive test-year convention in the country and a perfect stress test for
  IND-4.
- **Settlement-dominant culture** with a formal ALJ track, and 2026 evidence in
  hand (PPL: $275M settled vs. $356.3M sought — a 23% cut, plus a data-center
  tariff and storm-cost step-up in the same document). One case exercises
  Sections 1.4, 2.1 and 2.3 at once.
- Tight ~9-month statutory clock, and litigated outcomes still occur (PAWC's
  ~$74M / 9.55% ROE split-vote decision) — so the corpus contains both paths.

**Tractability**
- **OBSERVED**: a flat, numeric, directly-addressable document URL scheme —
  `https://www.puc.pa.gov/pcdocs/<id>.pdf` (e.g. `1641744.pdf`, `1869661.pdf`,
  `1874654.pdf`, `1890426.pdf`), seen repeatedly across independent searches.
  This is close to the best case: stable, citable, no session state, trivially
  storable as a source URL for IND-12.
- **OBSERVED**: per-docket landing pages at `puc.pa.gov/docket/<docket-number>`
  (e.g. `R-2025-3057164`) — docket numbers are semantic (`R-` = rate).
- **STATED**: an official Document Search at `puc.pa.gov/search/document-search/`,
  plus Daily Action Search and e-filing.
- **UNVERIFIED**: no public API found; assume HTML search-result scraping to
  discover document IDs. Text-native vs. scanned PDFs unverified, but modern
  e-filed testimony is very likely text-native.
- **Caveat**: the PA public/non-public line has been litigated (Office of Open
  Records directing disclosure), so apply IND-10 with care.

#### 2. Public Utility Commission of Texas (PUCT) — *strongest contrast partner, near-best tractability*

**Contrast value**
- **Restructured ERCOT wires-only TDUs**, but reached by a completely different
  route than Pennsylvania: **historical test year**, a **statutory comprehensive
  base-rate proceeding every four years**, and heavy reliance on **interim
  riders** (DCRF up to four times between base rate cases per 16 TAC § 25.243;
  TCOS for transmission). This makes it the best available test of IND-9's
  coverage-boundary honesty: ingesting only base rate cases in Texas
  *systematically misses* where the money moves.
- Documented **black box settlement** practice (SPS 2020, 2023) — direct
  exercise of IND-6 and IND-7.
- ERCOT-only, no FERC wholesale overlay for most of the state: an unusual and
  clarifying structural feature.

**Tractability — the best of the state candidates**
- **OBSERVED**: fully predictable document URLs —
  `https://interchange.puc.texas.gov/Documents/<control>_<item>_<docid>.PDF`
  (e.g. `32436_12_505126.PDF`, `58359_3_1519645.PDF`). Uppercase `.PDF`,
  numeric triple. Excellent for stable citation.
- **OBSERVED**: docket search with **URL-encoded query parameters** —
  `interchange.puc.texas.gov/search/dockets/?UtilityType=E&DocumentType=ALL&SortBy=FilingCount&Page=8`
  — i.e. filterable and paginable by URL, which is most of what an API would
  give you. Also a Daily Filing Search at `/search/daily/`.
- **STATED**: PUCT publishes **no official developer API**; Interchange is
  designed for browser access. A third-party (Parse.bot) sells structured access
  to the same data — evidence the surface is scrapable, and *not* a reason to
  buy it.
- **STATED**: Central Records support contact published for document-access help.
- **UNVERIFIED**: rate limits, terms of use, and how far back documents are
  text-native rather than scanned. Older filings (pre-2010) are likelier scanned.

#### 3. California Public Utilities Commission (CPUC) — *the vertically-integrated, forecast-test-year contrast*

**Contrast value** — this is the one that makes the set genuinely three-way:
- **Vertically integrated IOUs** (with CCA load departure as a complication),
  so generation rate base and procurement are *in* the case — the exact material
  absent from PA and TX. Without a state of this type, the corpus cannot answer
  most generation-related precedent questions at all.
- **Forecast test year on a three-year GRC cycle** with attrition-year
  escalation, and **cost of capital set in a separate proceeding** — a third
  distinct test-year regime, and a structural reason ROE will not be found in
  the GRC at all. A superb negative test for IND-2/IND-9: the honest answer to
  "what ROE did the CPUC authorize in this GRC" is *"not decided here, see the
  cost of capital proceeding."*
- **Wildfire cost recovery and liability** — the defining Western issue, with
  2026 evidence that CPUC's treatment is being read as more constructive.
- **Litigation-heavy with ALJ proposed decisions** and an unusually strong
  intervenor ecosystem (Cal Advocates, TURN) — the richest available source of
  adversarial documents for IND-3.
- Recent **ROE reductions across all major electric and gas utilities**
  (Dec 2025) and Liberty −25bp to 9.75% (Mar 2026) — live affordability-driven
  movement (Section 2.8) inside the corpus window.

**Tractability**
- **OBSERVED**: stable accession-style document URLs —
  `https://docs.cpuc.ca.gov/PublishedDocs/Published/G000/M564/K904/564904268.PDF`
  — **and the same document served as `.docx`**. That second point is a real
  advantage: a native Word document extracts far more reliably than any PDF, and
  tables survive.
- **STATED**: advanced search at `docs.cpuc.ca.gov/advancedsearchform.aspx`,
  results at `SearchRes.aspx` with URL parameters (`?doctypeid=1&daysearch=30`
  observed), docket cards at `cpuc.ca.gov/Docket`, and coverage of decisions,
  resolutions and rulings **from June 2000 onward**.
- **STATED**: an official free **email subscription service** for newly published
  documents matching criteria — the sanctioned, polite way to drive the
  scheduled ingestion job's incremental runs instead of re-crawling.
- **STATED**: no bulk-download API was found; CPUC's own "Order A Document" page
  exists for material not online.
- **Real cost, stated plainly**: CPUC GRCs are **enormous** — the March 2026
  California Senate brief describes a single GRC generating tens of thousands of
  pages. This is the highest-volume, highest-parse-cost candidate of the three.
  If ingestion budget is the binding constraint, this is the one to scope by
  proceeding rather than ingest wholesale.

### 6.2 If only two: **Pennsylvania + California**

They contrast on every axis at once — restructured vs. vertically integrated,
FPFTY vs. forecast, settlement-dominant vs. litigation-heavy, East vs. West,
storm vs. wildfire — and both have observed stable document URLs. Texas is the
better *third* than either is a substitute for the other.

### 6.3 Alternate: Illinois Commerce Commission (ICC)

Worth naming because it brings the one thing none of the three above does: a
**four-year multi-year rate plan with statutory performance metrics** under
Public Act 102-0662 (CEJA), i.e. genuine PBR (Section 2.6). If the human's real
interest is PBR/MYRP precedent, promote Illinois over Texas.

Tractability: **OBSERVED** — documents served from a stable, directly-fetchable
path (`icc.illinois.gov/api/web-management/documents/downloads/public/<file>.pdf`,
observed for Ameren's 2024 performance metrics report). Note honestly: the word
`api` in that path is a **CMS internal route, not a public API** — do not report
it to anyone as an API. **STATED**: e-Docket search at `icc.illinois.gov/e-docket/`
and `icc.illinois.gov/docket/search/documents`, searchable by case type, service
type, company and date range. The drawback for this specific set is redundancy:
Illinois is also restructured, so PA + TX + IL gives three wires-only states and
no generation rate base anywhere.

### 6.4 Candidates I would actively avoid for the MVP

- **Michigan MPSC — avoid, despite excellent contrast.** Michigan is analytically
  attractive (10-month statutory deadline, self-implementation after 6 months,
  projected test year, and headline 2026 cases at Consumers ~11% and DTE $574M).
  But **OBSERVED**: E-Dockets is hosted on Salesforce Experience Cloud at
  `mi-psc.my.site.com/s/` — a JavaScript-rendered Lightning portal. These are
  among the hardest public systems to ingest reliably: no stable document URLs
  in the page source, dynamic component endpoints that change without notice,
  and a high likelihood of needing a headless browser for *discovery*, not just
  fetching. That is a disproportionate share of the ingestion budget for one
  jurisdiction. **The genuine consolation**: Michigan **STATES** that e-filed
  PDFs must be OCR-searchable and copy-pasteable, and ≤100MB — so the documents
  themselves are ideal once you can find them. Revisit post-MVP.
- **New York DPS — defer, not avoid.** Analytically excellent (joint proposals,
  multi-year plans, 9.40% Jan 2026 ROE, live legislative pressure via S.5593).
  But **OBSERVED**: document URLs are opaque GUIDs —
  `documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId={D0670790-0000-CE19-894E-7AA79D5FE1CB}`.
  Stable and citable, but **not derivable** — every document requires an index
  crawl first, and GUID URLs are brittle to log and diff. A New York Open Data
  (Socrata) route for DPS matter/document metadata is plausible and would change
  this assessment entirely, but I **could not verify** such a dataset exists.
  Worth a 30-minute check before dismissing.
- **Formula-rate states (Louisiana, Alabama, Mississippi) — avoid for MVP.**
  The FRP model produces thin annual formula filings rather than the fat
  litigated records the product is built to read, and LPSC document access is
  the weakest of the candidates considered (**UNVERIFIED**, and that uncertainty
  is itself the reason to skip). Alabama's RSE is fascinating as a *contrast
  concept* and can be described in the KB without being ingested.

### 6.5 FERC eLibrary — explicitly considered, and **rejected as a jurisdiction; accepted as a narrow supplement**

**Rejected as one of the 2–3, for a substantive reason, not a technical one.**
FERC does not set **state retail base rates**. Its rate jurisdiction is wholesale
sales and **transmission** — transmission formula rates, transmission ROE and
incentives, RTO/ISO tariffs. Spending one of three precious jurisdiction slots on
FERC would buy no answers to "what did the commission authorize for my peer's
distribution revenue requirement," which is the product's core question. It would
also blur the corpus's structural metadata (IND-5), because FERC transmission
formula rate proceedings look superficially like rate cases and are not.

**But its tractability is the best of anything considered, and it should be
recorded as the named phase-2 addition:**
- **STATED**: `data.ferc.gov` publishes an **official public API with
  documentation and API-key signup** — the only *documented official API* found
  among all candidates. ([FERC developer docs](https://data.ferc.gov/developer/gettingstarted/))
- **STATED**: eLibrary is FERC's official document repository, covering documents
  submitted and issued **since 1981**, recently modernised with better search and
  download. **OBSERVED**: stable accession-number document URLs
  (`elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20110714-0015`).
- **OBSERVED**: a **community** API wrapper exists on GitHub
  (`4very/ferc-elibrary-api`) — a third-party convenience, not official support,
  and should not be treated as a stability guarantee.
- **The genuinely high-value FERC asset is Form 1**, the standardised annual
  financial/operational filing that makes peer-utility rate base, capital
  structure and O&M **comparable across states** — the one thing state dockets
  cannot give you. It is exactly what HData built on (Section 3.1), which is
  strong external evidence of its value. Adding FERC Form 1 as a *structured
  companion* to the state document corpus is likely the highest-leverage single
  enhancement after MVP, and it is the natural feeder for the deferred
  capability #3.

**Recommendation**: reject FERC for the MVP jurisdiction slots; record FERC Form 1
plus eLibrary as the first post-MVP corpus extension in the enhancement backlog.

### 6.5.1 One thing NOT to skip regardless of choice

Whichever jurisdictions are picked, **each ingested case needs its final order
and its compliance tariff**, not just the application and testimony. The
authorized numbers (IND-2) frequently only exist in those two documents, and a
corpus of asks without outcomes is a machine for producing harm #1.

### 6.6 The recommendation, stated as a confirm

> **Ingest three: Pennsylvania PUC, Public Utility Commission of Texas, and
> California PUC.** PA and TX are both restructured wires-only but reached by
> opposite routes (FPFTY + settlement-dominant vs. historical test year +
> statutory four-year cycle + riders); California supplies the
> vertically-integrated, forecast-test-year, generation-in-rate-base case that
> neither can. All three have **observed stable, citable document URLs**, and
> California additionally serves many documents as `.docx` as well as PDF.
> **Alternate**: swap Texas for the Illinois Commerce Commission if
> multi-year-rate-plan / performance-based-regulation precedent matters more
> than rider mechanics. **Drop to two** by cutting Texas, keeping PA + CA, if
> ingestion budget bites. **Avoid Michigan MPSC** for the MVP — its E-Dockets
> runs on a JavaScript Salesforce portal with no stable document URLs, which
> would consume a disproportionate share of the ingestion budget.
> **FERC is rejected** as a jurisdiction (it does not set state retail base
> rates) and **recorded as the first post-MVP corpus extension**, because
> `data.ferc.gov` is the only candidate with a documented official public API
> and FERC Form 1 is the only source of genuinely cross-state-comparable
> financial data.

---

## 7. Proposed feature backlog (industry-informed) — for Plan & Backlog

Advisory; the human folds these in alongside their own must-haves. Ordered by
how directly each follows from the research above.

1. **Posture-and-role-aware citation rendering** — every figure shown as
   *requested / recommended / stipulated / authorized*, with document role and
   order date on the badge (IND-1, IND-2, IND-3, IND-8). This is the single
   highest-value feature in the list; without it the corpus is actively
   dangerous.
2. **Coverage statement per query** — "checked N cases across 3 jurisdictions,
   2016–2026; 4 excluded as black box settlements; rider proceedings not
   ingested" (IND-9). Implements Intake standing constraint #4 concretely.
3. **Confidential-material quarantine in the ingestion job**, with a visible
   quarantine report per run (IND-10, IND-11). Cheap now, unbuildable later
   once the corpus is contaminated.
4. **Structural-comparability guardrail** — refuse or hard-caveat comparisons
   that cross the restructured/vertically-integrated or test-year boundary
   (IND-4, IND-5). Directly targets the extrapolation trap already slated for
   regression testing.
5. **Black box settlement handling** as a first-class case, including extraction
   and display of the non-precedential disclaimer (IND-6, IND-7).
6. **Large-load / data-center tariff as a tracked document class** (Section 2.1)
   — the fastest-moving live issue and where a strategy lead's questions will
   actually concentrate in 2026.
7. **Order-supersession signal** where detectable, and an explicit limitation
   statement where not (IND-17).
8. **Provenance trail export** for any analysis feeding filed material
   (IND-12, IND-15) — the artifact that makes witness verification and any
   future AI-use inquiry survivable.
9. **FERC Form 1 structured companion** — post-MVP, named now so it is designed
   for rather than bolted on (Section 6.5).

---

## Sources

**Rate case process and structure**
- Red Clay, Industry 101: Regulation in the Electricity Industry — Rate Case Process — https://redclay.com/industry-101-regulation-in-the-electricity-industry-rate-case-process/
- Colorado PUC, Electric Rate Cases — https://puc.colorado.gov/electric-rate-cases
- Atlas Buildings Hub, Rate cases explained (Oct 2025) — https://atlasbuildingshub.com/2025/10/21/rate-cases-explained-how-commissions-set-prices-and-why-energy-bills-are-rising/
- 66 Pa.C.S. § 315, Burden of Proof — https://law.onecle.com/pennsylvania/title-66/315.html
- NYS Focus, Lawmakers Scrutinize Secretive Process Behind Energy Bill Hikes — https://nysfocus.com/2025/10/02/energy-bill-price-rate-case-new-york

**Settlements and 2025–26 outcomes**
- Utility Dive, PPL Electric reaches $275M rate case settlement, including data center tariff — https://www.utilitydive.com/news/ppl-electric-rate-case-settlement-data-center-tariff/814760/
- PA PUC, PUC Issues Decision in PPL Electric Rate Proceeding (June 2026) — https://www.puc.pa.gov/press-release/2026/puc-issues-decision-in-ppl-electric-rate-proceeding-06042026
- Grand Rapids Herald-Review, Minnesota PUC approves settlement for Dakota Electric — https://www.grandrapidsmn.com/business/minnesota-public-utilities-commission-approves-settlement-for-dakota-electric-rate-case/article_2a71c967-1ac4-4f38-9792-dd29ca93dbe8.html
- Xcel Energy 8-K (SPS black box settlements) — https://www.sec.gov/Archives/edgar/data/72903/000007290324000092/xcelearningsreleaseq12024.htm
- Daily Energy Insider, PA PUC cuts PAWC request to ~$74M, sets 9.55% ROE — https://dailyenergyinsider.com/hearing-summaries/53051-pennsylvania-puc-cuts-pawc-rate-request-to-roughly-74m-sets-9-55-roe-in-split-vote/

**Test year / Pennsylvania FPFTY**
- Morgan Lewis, PA PUC's Fully Projected Future Test Year Filing Requirements Advance at IRRC — https://www.morganlewis.com/pubs/2025/05/pa-public-utility-commissions-fully-projected-future-test-year-filing-requirements-advance-at-irrc
- PA PUC, Comments on FPFTY procedures and filing requirements — https://www.puc.pa.gov/press-release/2017/puc-seeks-comments-on-proposed-procedures-and-filing-requirements-for-utilities-using-a-fully-projected-future-test-year

**Load growth, capex, data centers**
- S&P Global, Surging energy demand puts US utility capex near $1.3T in 2026–30 — https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/04/surging-energy-demand-puts-us-utility-capex-forecast-near-1-3t-in-2026-30
- Utility Dive, 2026 Q1 roundup: Utilities divided on data centers as affordability looms large — https://www.utilitydive.com/news/2026-q1-earnings-utilities-data-centers-affordability/820079/
- E3, Understanding the Drivers of Rising Electricity Rates and the Role of Data Centers (2026) — https://www.ethree.com/wp-content/uploads/2026/05/Understanding-the-Drivers-of-Rising-Electricity-Rates-and-the-Role-of-Data-Centers_E3-2026.pdf
- tech-insider, US Utilities Plan $1.4T for AI Data Centers — https://tech-insider.org/us-utility-1-4-trillion-ai-data-center-energy-2026/

**ROE**
- S&P Global, Underearning spread widens for gas, electric utilities in ROE analysis — https://www.spglobal.com/market-intelligence/en/news-insights/research/underearning-spread-widens-for-gas-electric-utilities-in-roe-analysis
- S&P Global, Regulatory risk levels warrant monitoring in 8 jurisdictions (June 2026) — https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/06/regulatory-risk-levels-warrant-monitoring-in-8-jurisdictions
- PR Newswire / Aii, New Aii Report Finds Utility ROEs Have Trended Downward Over Two Decades — https://www.prnewswire.com/news-releases/new-aii-report-finds-utility-roes-have-trended-downward-over-two-decades-challenging-claims-that-returns-are-driving-electricity-bills-302818942.html
- Gabelli, Utilities — U.S. Outlook — https://gabelli.com/research/utilities-u-s-outlook/
- RRA, Major Energy Rate Case Decisions (example filing copy) — https://pscdocs.utah.gov/electric/24docs/2403504/336109DPUExhbt3.14MjrEnrgyRtCsDcsns10-17-2024.pdf

**PBR / MYRP / formula rates**
- EQ Research, Performance-Based Regulation: States to Watch — https://eq-research.com/eq-publications/performance-based-regulation-states-to-watch/
- RMI Electricity Affordability Toolkit, Multi-Year Rate Plans — https://affordability-toolkit.rmi.org/policies/multi-year-rate-plans
- LBNL, State Performance-Based Regulation Using Multiyear Rate Plans for U.S. Electric Utilities — https://eta.lbl.gov/publications/state-performance-based-regulation
- Illinois ICC, Ameren 2024 Performance Metrics Evaluation Report (MYRP) — https://icc.illinois.gov/api/web-management/documents/downloads/public/Ameren2024PerfMetricsEvaluationReport.pdf
- Brattle, Performance Based Regulation Plans: Goals, Incentives and Alignment — https://www.brattle.com/wp-content/uploads/2021/05/14487_2017_12_06_-_brown_et_al_-_pbr_plans_goals_incentives_and_alignment_-_for_dte.pdf

**Tax**
- IRS, Corporate Alternative Minimum Tax — https://www.irs.gov/inflation-reduction-act-of-2022/corporate-alternative-minimum-tax
- CRS R47328, The 15% Corporate Alternative Minimum Tax — https://www.congress.gov/crs-product/R47328
- PwC Viewpoint 19.3, Normalization — https://viewpoint.pwc.com/dt/us/en/pwc/accounting_guides/utilities_and_power_/utilities_and_power__US/chapter_19_regulated_US/193_normalization_US.html
- IRS Rev. Proc. 2020-39 — https://www.irs.gov/pub/irs-drop/rp-20-39.pdf
- Federal Register, Accounting and Ratemaking Treatment of ADIT — https://www.federalregister.gov/documents/2018/11/23/2018-25372/accounting-and-ratemaking-treatment-of-accumulated-deferred-income-taxes-and-treatment-following-the

**Affordability politics**
- Brookings, How rising electric rates could affect the 2026 midterms — https://www.brookings.edu/articles/how-rising-electric-rates-could-affect-the-2026-midterms/
- E&E News/POLITICO, Electricity rates a potent political issue ahead of 2026 midterms — https://www.eenews.net/articles/electricity-rates-a-potent-political-issue-ahead-of-2026-midterms-2/
- Utility Dive, Utility profits in the crosshairs amid affordability concerns — https://www.utilitydive.com/news/utility-profits-in-the-crosshairs-amid-affordability-concerns/825610/
- US News, Low-Voltage Utility Elections Face Surge of Attention as Electricity Bills Rise — https://www.usnews.com/news/us/articles/2026-04-06/low-voltage-utility-elections-face-surge-of-attention-as-electricity-bills-rise
- NY Senate, State Senate Advances Legislation to Stand Up to Utility Corporations, Lower Rates — https://www.nysenate.gov/newsroom/press-releases/2026/state-senate-advances-legislation-stand-utility-corporations-lower

**AI in regulatory affairs**
- HData, Regulatory Intelligence Platform — https://www.hdata.com/
- HData blog, Customer Story: Witness Preparation with Regulatory AI — https://blog.hdata.com/customer-story-witness-preparation-regulatory-ai
- HData blog, How to Leverage FERC Data for Utility Benchmarking — https://blog.hdata.com/how-to-leverage-ferc-data-for-utility-benchmarking
- HData/Systrends, Systrends Acquires HData Compliance Solution — https://blog.hdata.com/press-releases/systrends-acquires-compliance-solution
- StockTitan, HData and Southern Company announce AI pilot program — https://www.stocktitan.net/news/SO/h-data-and-southern-company-announce-ai-pilot-program-to-ck3crtrhqwbv.html
- Hydro Leader, Hudson Hollister of HData — https://hydroleadermagazine.com/hudson-hollister-of-hdata-automating-compliance-and-business-intelligence-for-ferc-licensees/
- Speridian, Regulatory Compliance Software for Public Utility Commissions in the AI Era — https://www.speridian.com/blogs/regulatory-compliance-software-for-public-utility-commissions-managing-utility-regulation-in-ai-era/
- Glean, How AI enhances regulatory readiness in utilities — https://www.glean.com/perspectives/how-ai-enhances-regulatory-readiness-in-utilities
- Logic20/20, Two clocks, one grid: Designing utility AI for the rate case — https://logic2020.com/insight/designing-utility-ai-rate-case-not-just-pilot/
- NewGen Strategies & Solutions, The AI Transition for Utilities: A Strategic Guide for 2026 — https://www.newgenstrategies.net/stories/utility-ai-transition-full-report.html

**AI hallucination sanctions / professional conduct**
- GC AI, AI Hallucination Legal Cases: A Sanctions Tracker (2026) — https://gc.ai/blog/ai-hallucination-legal-cases
- Norton Rose Fulbright, AI in litigation: Update on Gen AI sanctions in 2026 — https://www.nortonrosefulbright.com/en-us/knowledge/publications/792d8bf3/ai-in-litigation-update-on-gen-ai-sanctions-in-2026
- National Law Review, Seventh Circuit Addresses Sanctions for Attorney Citing AI-Generated Hallucinations — https://natlawreview.com/article/seventh-circuit-addresses-counsels-obligations-when-ai-generated-hallucinations
- Law.com, Fed. Court Suspends Pa. Attorney for AI-Hallucinated Citations — https://www.law.com/thelegalintelligencer/2026/06/22/fed-court-suspends-pa-attorney-for-aihallucinated-citations/
- NYSBA, Beyond the Mirage: Beware of Generative AI and Hallucinations — https://nysba.org/beyond-the-mirage-beware-of-generative-ai-and-hallucinations/

**Protective orders / confidentiality**
- Oregon PUC Order No. 14-150 (protective order, UM 1689) — https://apps.puc.state.or.us/orders/2014ords/14-150.pdf
- Oregon PUC Order No. 15-416 — https://apps.puc.state.or.us/orders/2015ords/15-416.pdf
- Texas PUCT, protective order document (Control 32436) — https://interchange.puc.texas.gov/Documents/32436_12_505126.PDF
- PA PUC document (protective-order related) — https://www.puc.pa.gov/pcdocs/1874654.pdf
- Buchanan Ingersoll & Rooney, No Secrets: Office of Open Records Directs PaPUC to Disclose Documents — https://www.bipc.com/no-secrets-office-of-open-records-directs-papuc-to-disclose-documents

**Docket system access (tractability evidence)**
- PA PUC Document Search — https://www.puc.pa.gov/search/document-search/
- PA PUC Docket example R-2025-3057164 — https://www.puc.pa.gov/docket/R-2025-3057164
- PA PUC Filing & Resources — https://www.puc.pa.gov/filing-resources/
- PUCT Interchange, Docket Search — https://interchange.puc.texas.gov/search/dockets
- PUCT Interchange, Daily Filing Search — https://interchange.puc.texas.gov/search/daily/
- PUCT, Instructions and FAQ for Interchange Filing Search — https://www.puc.texas.gov/industry/filings/retrievalfaq/
- 16 TAC § 25.243, Distribution Cost Recovery Factor — http://txrules.elaws.us/rule/title16_chapter25_sec.25.243
- CPUC Online Documents — https://docs.cpuc.ca.gov/
- CPUC Advanced Search Form — https://docs.cpuc.ca.gov/advancedsearchform.aspx
- CPUC Locate Documents — https://www.cpuc.ca.gov/proceedings-and-rulemaking/locate-documents
- CPUC Docket Card — https://www.cpuc.ca.gov/Docket
- CPUC, Tracking Issues of Interest (subscription service) — https://www.cpuc.ca.gov/about-cpuc/divisions/news-and-public-information-office/public-advisors-office/tracking-issues-of-interest
- Illinois ICC e-Docket — https://icc.illinois.gov/e-docket/
- Illinois ICC document search — https://icc.illinois.gov/docket/search/documents
- Michigan MPSC E-Dockets — https://mi-psc.my.site.com/s/
- Michigan MPSC E-Dockets Instruction Manual — https://www.michigan.gov/-/media/Project/Websites/mpsc/activity/MPSC-E-Dockets-Instruction-Manual.pdf
- Michigan MPSC, Case & Hearing Information — https://www.michigan.gov/mpsc/commission/case-hearing-info
- NY DPS document example (GUID URL scheme) — https://documents.dps.ny.gov/public/Common/ViewDoc.aspx?DocRefId=%7BD0670790-0000-CE19-894E-7AA79D5FE1CB%7D

**FERC**
- FERC eLibrary — https://ferc.gov/ferc-online/elibrary
- FERC eLibrary Quick Help — https://www.ferc.gov/elibrary-quick-help
- data.ferc.gov, Getting Started (official public API) — https://data.ferc.gov/developer/gettingstarted/
- FERC eLibrary document info example — https://elibrary.ferc.gov/eLibrary/docinfo?accession_Number=20110714-0015
- GitHub, 4very/ferc-elibrary-api (community wrapper, unofficial) — https://github.com/4very/ferc-elibrary-api
- JD Supra, eLibrary is Now FERC's Official Document Repository — https://www.jdsupra.com/legalnews/elibrary-is-now-ferc-s-official-78523/
