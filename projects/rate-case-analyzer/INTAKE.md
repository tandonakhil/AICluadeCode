# Intake — rate-case-analyzer

**Completed**: 2026-08-07 · **Path**: A (new project) · **Form**:
`admin/templates/INTAKE_FORM.md`

Answers marked *(pre-filled)* were inferred from the request or from earlier
answers and shown to the human rather than asked. Answers marked *(open)* were
recorded as "not yet known" and are carried as known risks, per the form's rule
that an unanswered question is only acceptable when it was actually asked.

---

## Q0 · Path

**A — new project.** Confirmed by the human 2026-08-07 against the recommendation.

The close call was `policy-lookup-assistant`, a deployed `rag-knowledge-base`
project whose own Intake recorded its domain as *utility regulatory/compliance
policy lookup* in the *Utilities/Energy* industry — overlapping capability #2
(grounded Q&A) almost exactly. Split anyway because two of the three named
capabilities fall outside that product's purpose: a **filings-acquisition
pipeline** against external commission dockets, and a **judgment-generating
approval-likelihood analysis** with a materially different harm profile and
roster. The form's standing rule (when unsure, prefer enhancement) was stated
explicitly and the human chose the split knowingly.

**Deliberate reuse, not a fresh start**: `policy-lookup-assistant` already
proved the grounded-refusal + authority-labeled-citation pattern in this exact
industry. Its `DOMAIN_KB.md`, `SECURITY_KB.md` and sentinel-refusal design are
inputs to this project's Architecture gate, not things to rediscover.

---

## A1 · Identity

| # | Answer |
|---|---|
| A1.1 | `rate-case-analyzer` |
| A1.2 | An agentic AI sidekick for preparing rate case analysis for power utilities |
| A1.3 | *(pre-filled)* The human in session holds approval authority at every gate. No separate named business owner recorded. |

Three capabilities named in the original request, in the human's own order:

1. Intake historical rate cases; access publicly submitted rate cases for other
   utilities.
2. Build a RAG model to answer any questions.
3. Provide competitive analysis on likelihood of approvals / questions, etc.

---

## A2 · Problem

| # | Answer |
|---|---|
| A2.1 | *(pre-filled)* Rate case preparation depends on precedent — what peer utilities asked for, what commissions actually authorized, and what got challenged. That precedent is public but scattered across per-state docket systems in long PDFs, so it is searched manually or not at all. |
| A2.2 | **All four personas selected** — see below. |
| A2.3 | *(pre-filled)* Manual docket search and analyst reading, plus institutional memory and consultants' private precedent files. |
| A2.4 | *(pre-filled)* Status quo persists: precedent research stays expensive and shallow, and asks are set from memory rather than evidence. |

### A2.2 — primary users (all four selected)

- Regulatory affairs analyst (utility-side) — assembles the filing
- Rate case strategy lead / director of regulatory — sets the ask
- External consultant / advisory firm — works across utilities and jurisdictions
- Commission staff / intervenor — reviews filings adversarially

### Conflict-of-interest finding — raised at A2.2, resolved at A8.2

Serving utility-side users **and** intervenor/commission-staff users in one
product is a conflict-of-interest surface, not merely a persona list. If the
system ever holds non-public utility work product (draft testimony, internal
cost positions) alongside intervenor users, the failure mode is disclosure to
an opposing party in a live proceeding.

**Recommendation given and accepted** — treat it as an *ethical wall*, not an
access-control problem. Permissions are a filter over a shared thing, and a
dropped filter is a silent breach:

1. **Two corpora that are never siblings.** Classify at ingestion, not query.
   `public` (filings, orders, testimony as filed) and `work-product` (drafts,
   internal positions) get separate stores and separate credentials — never one
   store with a `visibility` column.
2. **Bind the corpus at session construction, not at retrieval.** The user's
   role determines which retriever object *exists*. An intervenor session must
   have no code path to the work-product retriever — not a path returning empty.
   Handed to `solution-architect` as a non-negotiable at the Architecture gate.
3. **The aggregate leak.** Capability #3 is a statistical view over the corpus,
   so a benchmark learned from non-public material is a disclosure channel even
   though no document crossed. **Every number in the competitive-analysis
   feature is computed over the public corpus only** — testable, and owned by
   `responsible-ai-architect` as a red-team case.
4. **Deployment separation** per party or per engagement for any real
   adverse-party production use; shared-instance multi-tenancy between
   litigation adversaries is a posture that must be defended, and "we had good
   RBAC" has not historically been a successful defence.

**Recorded scope decision**: intervenor/commission-staff use is **in the
product's persona set but out of MVP scope**. MVP serves utility-side only. The
wall is designed in from the start rather than retrofitted, because retrofitting
it means re-architecting retrieval. `security-architect` ratifies or amends at
the Architecture gate.

---

## A3 · Users and context

| # | Answer |
|---|---|
| A3.1 | *(pre-filled)* Desk work. Long-form, deadline-bound, over months of filing preparation — not a glance-and-go tool. |
| A3.2 | *(pre-filled)* Deliberate and analytical, but under filing-deadline pressure; output is expected to withstand scrutiny by a regulator. |
| A3.3 | *(open)* Not asked — recorded as unknown. Scale is not a binding constraint on the MVP; revisit before any shared deployment. |

---

## A4 · Domain and industry *(both unconditional)*

| # | Answer | Owner |
|---|---|---|
| A4.1 | Utility rate-case preparation / regulatory economics — revenue requirement, ROE, rate base, capital structure, test year, settlement vs. litigated outcomes | `functional-agent` |
| A4.2 | Regulated power utilities (electric; gas adjacency not excluded) | `industry-expert` |

Both agents write their initial KBs at the Intake gate regardless of the final
roster.

---

## A5 · Surfaces — **not skipped**

| # | Answer |
|---|---|
| A5.1 | **Two surfaces: desktop web + scheduled ingestion job.** |
| A5.2 | *(pre-filled)* Exportable deliverables (analysis memo, comparison workbook) are a plausible later surface — `deliverables-agent` territory. Mobile explicitly not anticipated. |
| A5.3 | Yes — the ingestion job and the web app share a backend and a corpus store. |

> **Consequence, applied**: more than one surface, so `solution-architect`
> moves into the core non-droppable set and its Impact Analysis is mandatory.
> The surface count is stated plainly at Team Composition so the human can
> correct the count rather than only the roster.
>
> The ingestion job counts as a surface because it ships and fails
> independently of the UI: a silently-broken scraper produces a stale corpus,
> and a stale corpus produces confident wrong answers with no UI symptom.

---

## A6 · Data

| # | Answer |
|---|---|
| A6.1 | **Public state commission dockets** + **the utility's own historical rate cases**. For this project, the internal corpus is **synthetic data mocked up from public rate cases** — no real work product is ever held. |
| A6.1b | **Two or three jurisdictions, chosen for contrast** (e.g. a restructured market vs. a vertically-integrated state) so cross-jurisdiction comparison works from day one. **Which commissions is deliberately unresolved here** — `industry-expert` researches and recommends named dockets at the Intake gate on both contrast value and public-access tractability, for human confirmation. Not chosen by orchestrator intuition. |
| A6.2 | Ingested filings and derived artifacts: parsed documents, chunk embeddings, extracted case metadata, and query/answer history. |
| A6.3 | **No real PII, health or children's data.** The regulated-data exposure is different in kind: public regulatory filings are non-sensitive, but the *work-product* class is confidential and adversarially contested. Because the internal corpus is synthetic for this project, the sensitivity is **simulated but designed for**. `security-architect` is retained on this basis. |
| A6.4 | *(open)* Retention not specified. Recorded as a known risk; a real deployment holding genuine work product needs an answer before it holds anything. |

---

## A7 · AI behaviour

| # | Answer |
|---|---|
| A7.1 | *(pre-filled, accepted)* Never invent a citation, docket number, order number or quoted finding. Never present a likelihood estimate as a commitment or a legal opinion. Never let work-product content reach a public-corpus answer. |
| A7.2 | **All four harms selected** — see below. |
| A7.3 | **Yes — grounding is mandatory.** Every claim about precedent carries a resolvable docket citation; an unsupported claim refuses rather than paraphrases. Follows directly from harm #2. |
| A7.4 | *(pre-filled)* The human filer is accountable, always. The tool is decision-support; its output is never signed and never filed unreviewed. |

### A7.2 — worst plausible harm (all four selected)

1. **Bad strategic ask, real money lost** — a wrong precedent read ("peers got
   10.2% ROE in comparable cases") drives an ask the commission cuts. Tens of
   millions per year over the rate period, and the error is invisible because
   the output looked well-sourced.
2. **Fabricated precedent in a filed document** — an invented or misattributed
   citation reaches testimony actually filed. A credibility event with the
   regulator, potentially sanctionable, damaging every future case rather than
   just this one.
3. **False confidence — missed challenge** — the analysis says an item is
   uncontroversial; intervenors attack it and the utility is unprepared. The
   harm is asymmetric: silence is read as clearance.
4. **Ratepayer-facing harm** — errors flowing through to customers, either an
   unjustified cost recovery raising bills or a needed safety/reliability
   investment dropped because the tool predicted it would not survive review.

**Consequences applied:**

- `responsible-ai-architect` becomes **non-droppable** (harms #2 and #3 are
  squarely its lane).
- Grounding/refusal is mandatory, not a preference (A7.3).
- **Harm #3 is an interface problem, not a model problem.** A tool that speaks
  only when it finds something teaches users to read silence as clearance. It
  must state coverage explicitly — *"checked 40 comparable cases, flagged 3,
  could not assess 5 for these reasons"* — rather than showing a flag list that
  is empty both when nothing is wrong and when nothing was examined. Carried to
  Functional Design as a **required acceptance criterion**, not left to
  designer discretion.

---

## A8 · Success and scope

| # | Answer |
|---|---|
| A8.1 | *(pre-filled)* A strategy lead can ask a precedent question and get an answer whose every citation resolves to a real filing, and the system refuses rather than guesses when the corpus does not support an answer. Observable and testable; sharpened into acceptance criteria at Functional Design. |
| A8.2 | **Out of MVP scope**: capability #3 (approval-likelihood / competitive analysis); intervenor and commission-staff use; real (non-synthetic) internal work product; mobile surfaces; exportable Office deliverables. |
| A8.3 | **MVP = capabilities #1 + #2** — ingestion of 2–3 jurisdictions plus the synthetic internal history, and grounded Q&A with hard citations and honest refusal. |

**Why #3 is deferred** (stated at the gate, accepted): capability #3's value is
entirely parasitic on corpus quality. An approval-likelihood estimate over a
thin or mis-parsed corpus *is* harm #1, delivered confidently and with a number
attached. It becomes the first `/enhance-project` once the corpus is proven.

---

## A9 · Constraints

| # | Answer |
|---|---|
| A9.1 | No deadline. |
| A9.2 | **No hard budget — build it properly.** `usage-monitor` still tracks per-stage spend into `USAGE.md` and still produces the pre-work estimate at Team Composition; no soft ceiling is enforced. Rationale accepted: given the A7.2 harm profile, guardrail and grounding work is where the cost goes and is not the place to economize. |
| A9.3 | *(open)* No formal compliance or audit obligation named. Regulatory-filing accuracy is the binding quality constraint rather than a named compliance regime. |
| A9.4 | *(pre-filled)* Nothing mandated for reuse, but `policy-lookup-assistant`'s grounded-refusal and authority-labeled-citation design is a deliberate, recorded input. |

---

## A10 · Template

Not asked as a menu, per the `/new-project` procedure. `plan-agent` reads every
`TEMPLATE_MANIFEST.md` and recommends against the described need; the human
confirms or overrides a single recommendation. Recorded in
`PROJECT_CONTEXT.md`'s Decisions Log.

---

## Open questions carried forward as known risks

| # | Question | Status |
|---|---|---|
| A3.3 | How many users? | Not binding for MVP; revisit before shared deployment |
| A6.1b | Which named commissions? | `industry-expert` recommends at Intake gate, human confirms |
| A6.4 | Retention — how long, who can delete? | Must be answered before any real work product is held |
| A9.3 | Compliance/audit obligations | None named; revisit if the tool's output enters filed material |
