# UX Knowledge Base — rate-case-analyzer

**Owner**: `ui-ux-designer`
**Gate**: 5 · Experience Design
**Written**: 2026-08-07
**Designs against**: `knowledge/FUNCTIONAL_SPEC.md` (342 acceptance criteria),
`FEATURES.md` (44 MVP1 features), `PLAN.md`, `PROJECT_CONTEXT.md`,
`knowledge/DOMAIN_KB.md`, `knowledge/INDUSTRY_KB.md`.

**Rendered proposal**: [`../design-review/index.html`](../design-review/index.html)
— twelve self-contained static pages covering every significant state. This
file is the reasoning; that is the artefact a human can actually look at. Under
the standing requirement recorded in `PROJECT_CONTEXT.md` and in the platform's
memory, a design proposal is not reviewable from spec text alone, and this gate
was not closed on text.

This file has three sections per the `ui-ux-designer` contract: **Design
Intent** (§1–§8), **Environment constraints and what was not done** (§9), and
**Observed post-deploy behaviour** (§10, empty until there is real usage).

---

## 1. Audience framing — read this before anything else

Two facts about the reader drive every decision below.

**The user is a utility strategy lead or rate-case analyst preparing material
that may be filed with a commission.** They already know what a test year is.
They are not being onboarded, delighted or converted. They are checking whether
a number is safe to put in front of a regulator whose good opinion is a
multi-decade asset. The design optimises for *fast trust-checking by someone
who already knows the domain* — the same framing that worked in
`policy-lookup-assistant`, carried forward deliberately.

**But the failure mode here is the opposite of that project's.** This is a
dense, high-stakes analytical tool over regulatory filings, and the gravitational
pull of the material is toward an interface that *looks like a regulatory
filing* — grey tables, twelve-point everything, no hierarchy, every fact
equally weighted, nothing scannable. The human's brief was explicit and is
treated as a hard requirement: *"I want to make sure the UI is easy and
designed… It needs to be easy clean and intuitive."*

The two pull against each other, and the resolution is the single most
important framing decision in this document:

> **Density is earned, never assumed. The interface starts nearly empty and
> adds information only as the user's own question justifies it.**

The Ask screen is one field and a scope statement. The Answer screen is dense —
but every dense region on it exists because the user asked a question that
made it relevant. Nothing is dense *ahead of* the user. There is no dashboard,
no corpus browser, no saved-query sidebar, no navigation. This is what makes a
tool that must show a forty-item exclusion list still read as calm.

`ASM-UX-1` · *Assumption*: a single-purpose, no-navigation surface is correct
for MVP1. Capability #3 (`F51`) and export (`F41`) will both want more surface
area; the layout reserves the right rail and a full-width main column so
neither requires a new layout pass.

---

## 2. End-to-end user flows

### 2.1 The primary flow — ask a precedent question

There is one flow, and its defining property is that **it has two equally
first-class endings**.

```
  Ask screen (empty)
        │  types a question
        ▼
  Validation ──── whitespace/empty ──▶ inline message, nothing sent  [screen 02]
        │
        ▼
  Frame parse ─── unresolvable ──────▶ REFUSAL · parse             [screen 08]
        │
        ▼
  Metadata-filtered retrieval
        │
        ├── 0 candidates ────────────▶ REFUSAL · nothing examined  [screen 07]
        │
        ▼
  Comparability predicate
        │
        ├── 0 comparable ────────────▶ REFUSAL · none comparable   [screen 06]
        │
        ▼
  Composition → deterministic citation verification
        │
        ├── any check not passed ────▶ REFUSAL · verification      [screen 09]
        │
        ▼
  ANSWER  ─ grounded [03] · with caveats [04] · NOT_STATED [05]
```

Every terminal state on that diagram renders a **coverage panel**. Every
terminal state writes a **provenance record**. A provenance write that does not
succeed produces the one genuine error state (screen 09), which is not on this
diagram because it is not an outcome of the reasoning — it is the system
breaking.

**Design consequence stated plainly:** four of the seven endings are refusals.
A design that treats refusal as an edge case would spend its craft on one
seventh of the product. The refusal screens here got *more* design attention
than the answer screens, not less.

### 2.2 The re-ask loop

Both answers and refusals leave the question field active and empty at the top
of the screen. A second question **replaces** the first answer entirely — no
element of the previous answer remains visible (`AC-F35-09`).

`ASM-UX-2` · *Assumption*: **no session history / Q&A ledger in MVP1.**
`policy-lookup-assistant` stacked past Q&A pairs; that does not carry over here.
The reason is specific rather than aesthetic: two answers stacked on one page,
each with its own coverage panel, creates an ambient risk that a coverage
statement is read against the wrong answer. Given that the entire product exists
to prevent a coverage statement being misread, one answer on screen at a time is
the safer default. The provenance record preserves the history; `F41` (saved
queries, deferred) is where a reviewable ledger belongs, and it can be designed
with the adjacency problem in mind.

### 2.3 The second surface — the ingestion job

No interactive flow. The job runs headlessly, and its human-readable output is
the **run report** (screen 11). It is given the same visual language as the web
surface so the two read as one system, and it links back to the web surface's
freshness banner conceptually: a run that fails is the reason the analyst sees
a stale or never-dated banner.

---

## 3. Screen and state inventory

Thirteen renders, twelve screen/state pages plus the index. Screen numbers here
match the file names in `design-review/`.

| # | Screen / state | Trigger | Key components | Criteria |
|---|---|---|---|---|
| 01 | **Ask — first run** | page load | question form, scope statement, freshness banner, example questions | `AC-F35-01`, `AC-F39-01`, `AC-F39-03` |
| 02 | **Ask — in flight** + **empty-question validation** | submit | in-progress indicator with named pipeline stages; inline validation | `AC-F35-03`, `AC-F35-02` |
| 03 | **Answer — grounded** | verified answer | answer panel, coverage strip, 3 citation cards, comparability all-matched, coverage panel, provenance | `AC-F35-04`, `F36` all, `AC-F37-01/02`, `AC-F40-04`, `AC-F34-07` |
| 04 | **Answer — caveats, stale precedent, superseded order, work-product source** | `COMPARABLE_WITH_CAVEATS` | comparability table with CAVEAT/INFO/UNASSESSED rows, vintage caveat, non-precedent quote, superseded flag, work-product flags | `AC-F40-01/02/03/06`, `AC-F36-07/08`, `AC-F27-06/07/08/10`, `AC-F32-02/03` |
| 05 | **Answer — `NOT_STATED` black box** + the parse-failure contrast | black-box settlement | citation card `--absent`, evidence-of-silence quote; side-by-side with extraction gap | `AC-F36-02`, `AC-F14-10`, `AC-F14-11`, `RCA-R5` |
| 06 | **Refusal — 40 checked, none comparable** | `REFUSED_INSUFFICIENT`, rich coverage | refusal panel, refusal gap block, examined list (40), coverage panel with full-width excluded bar | `AC-F37-04`, `AC-F31-05/06/07`, `AC-F38-01…04`, `RCA-R6` |
| 07 | **Refusal — nothing examined** | `REFUSED_INSUFFICIENT`, 0 candidates | refusal panel, **`.coverage-none` band** (not a bar), filter values | `AC-F37-03`, `AC-F31-08`, `AC-F28-05`, `RCA-R7` |
| 08 | **Refusal — question unresolvable** | `REFUSED_PARSE_FAILED` | refusal panel, slot-by-slot resolved/unresolved block | `AC-F38-07`, `AC-F28-04`, `ASM-11` |
| 09 | **System failure** + **verification-failure refusal** + side-by-side | provenance store unavailable / `REFUSED_VERIFICATION_FAILED` | `.syserror-panel` (the only red), refusal panel | `AC-F35-06`, `AC-F38-06`, `AC-F34-06`, `AC-F28-03` |
| 10 | **Freshness banner — 4 states** | ingest-run state | `.rca-freshness` default / `--stale` / `--never`, plus the never-dated refusal | `AC-F39-01…06`, `RCA-R13` |
| 11 | **Ingest run report** + gate-failure variant — **headless, no browser route ships**; `AC-F43-*` is satisfied by `app/jobs/report.py`'s JSON/text output, not by an HTTP screen | job completion | run status, run stats, quarantine table with explicit zeros, quarantined items with evidence, extraction gaps, health check | `AC-F43-01…08`, `IND-10/11`, `RCA-R11` |
| 12 | **System sheet** | — | the 16×6 encoding, greyscale proof, colour tokens with ratios, type scale, component inventory, accessibility rules | `AC-F36-03`, `AC-F48-01…05` |

**Coverage of UI-bearing MVP1 features**: `F34` (03–08), `F35` (01–09), `F36`
(03, 04, 05, 12), `F37` (03–08), `F38` (06–10), `F39` (01–11), `F40` (03, 04),
`F48` (12, as the assertion targets). All eight rendered.

---

## 4. Layout

**Desktop web, single surface.** `PROJECT_CONTEXT.md` records mobile as out of
MVP scope; there is no responsive-web decision in the Decisions Log that would
require a designed mobile layout, unlike some other projects on this platform.
The layout degrades gracefully in a narrow window (the rail stacks beneath the
main column) but a narrow window is not a design target and is not claimed as
one.

```
┌──────────────────────────────────────────────────────────────────────┐
│ APP BAR (sticky)   wordmark · session chip · FRESHNESS BANNER        │
├──────────────────────────────────────────────────────────────────────┤
│  question form (full width)                                          │
│                                                                       │
│  ┌────────────────────────────────────┐  ┌────────────────────────┐  │
│  │ ANSWER  or  REFUSAL  or  ERROR     │  │ COVERAGE PANEL         │  │
│  │                                    │  │  (sticky, always       │  │
│  │ COVERAGE STRIP  ← above the fold   │  │   expanded)            │  │
│  │                                    │  │                        │  │
│  │ CITATION CARDS                     │  │ PROVENANCE PANEL       │  │
│  │                                    │  │                        │  │
│  │ COMPARABILITY                      │  └────────────────────────┘  │
│  └────────────────────────────────────┘                              │
└──────────────────────────────────────────────────────────────────────┘
   main column: minmax(0,1fr)              rail: 384px, ≥1080px
```

Three layout decisions carry weight:

1. **Coverage appears twice, deliberately.** A one-line *coverage strip*
   (arithmetic sentence + bar) sits in the main column directly beneath the
   answer, above the fold, before any citation. The *full coverage panel* lives
   in the persistent right rail. The strip guarantees the user cannot read the
   answer without reading how much of the corpus stands behind it; the panel
   guarantees the detail is never more than a glance away. See §6.
2. **The right rail is sticky and never collapsed.** No disclosure triangles
   anywhere on coverage, comparability or provenance. A collapsed coverage
   panel is a hidden coverage panel, and a hidden coverage panel is the
   silence-is-clearance failure with extra steps.
3. **The freshness banner is in the app bar, on every screen, including the
   empty first-run screen.** It is the only symptom a silently-stopped
   ingestion job produces. Putting it on the answer screen only would mean the
   user learns the corpus is two months old *after* forming an impression of
   the answer.

---

## 5. The hard problem #1 — encoding `document_type` (14) × `claim_status` (6)

**The constraint.** `PROJECT_CONTEXT.md` is explicit that
`policy-lookup-assistant`'s four-value authority taxonomy does **not** transfer.
Authority here is two-dimensional: a final order *recites* what was requested,
and rebuttal testimony *quotes* prior orders. So the card must carry both axes
simultaneously — 84 combinations. A design with 84 treatments is not a design,
it is a legend nobody reads. A design with one colour ramp over 16 values is
worse: it fails greyscale, fails colour-blind users, and fails the
non-negotiable rule that authority is never carried by colour alone.

**The resolution: collapse each axis into a small number of visual weights,
carry the full precision as text on every instance.**

### 5.1 Axis 1 — `document_type` → 4 tiers, rendered as a countable spine

The sixteen values are already ranked 1–16 in `DOMAIN_KB` §2.3 (widened from the original 14 at the Code gate to add `PROCEDURAL_ORDER`/`WITHDRAWAL_NOTICE`, both appended at the bottom of the rank so no existing rank changed). What an analyst
is actually scanning for is a four-way question: *is this an outcome, a
recommendation, an ask, or argument?* So the ranking is bucketed:

| Tier | Rendered as | `document_type` values | Meaning |
|---|---|---|---|
| **4 of 4** | 4 filled segments | 1 `FINAL_ORDER`, 2 `ORDER_ON_REHEARING`, 3 `APPROVED_SETTLEMENT`, 4 `COMPLIANCE_FILING` | **Outcome documents** — what was granted or implemented |
| **3 of 4** | 3 filled | 5 `PROPOSED_ORDER_ALJ`, 6 `STAFF_REPORT_OR_TESTIMONY`, 7 `INTERVENOR_TESTIMONY` | **Recommendations** — someone with standing proposed it |
| **2 of 4** | 2 filled | 8 `UTILITY_REBUTTAL_TESTIMONY`, 9 `UTILITY_DIRECT_TESTIMONY`, 10 `APPLICATION`, 11 `EXHIBIT_SCHEDULE` | **Party filings / the ask** |
| **1 of 4** | 1 filled | 12 `DATA_REQUEST_RESPONSE`, 13 `HEARING_TRANSCRIPT`, 14 `BRIEF` | **Record & argument** — never a fact source for an outcome |

The **authority spine** is a vertical stack of four small blocks on the card's
left edge with N filled. It is:

- **countable** — no legend needed, more filled = more authoritative;
- **greyscale-safe** — no hue involved at all;
- **screen-reader-safe** — `role="img"` with `aria-label="Authority tier 4 of
  4: outcome document."`;
- **stable under the deferred features** — tier 1 exists now even though
  `F19`/`F20` are deferred, so adding transcripts later is a pipeline change,
  not a design change.

The exact enum value and its numeric rank are always printed as text on the
card (`Final Order` · `document_type rank 1 of 16 · outcome document`), so the
bucketing loses nothing (`AC-F36-03`, `AC-F48-01`).

`ASM-UX-3` · *Assumption*: **not all sixteen types need equal visual weight**,
and the four-way bucketing is the right cut. It follows the enum's own
authority ranking rather than inventing a taxonomy, and the tier boundaries
land exactly where the schema invariants already are — tier 4 is precisely the
set of documents from which an `AUTHORIZED` claim may be written.

### 5.2 Axis 2 — `claim_status` → 3 chip families

The distinction that carries the project's **named worst harm** is not six-way,
it is three-way: *granted, merely proposed, or absent.* So:

| Family | Construction | Values | Gloss printed on every chip |
|---|---|---|---|
| **OUTCOME** | solid fill, highest contrast | `AUTHORIZED`, `SETTLED`, `IMPLEMENTED` | "— granted by commission order" / "— agreed in an approved settlement" / "— in effect per compliance tariff" |
| **POSITION** | hatched outline, **never filled** | `REQUESTED`, `RECOMMENDED` | "— what the utility asked for; **not granted**" / "— proposed by staff or an intervenor; not granted" |
| **ABSENT** | dashed outline, no fill | `NOT_STATED` | "— the document does not state this figure" |

Four redundant channels carry the same fact, and colour is the *last* of them:
(1) the family word, (2) the exact enum value, (3) the plain-English gloss,
(4) the chip's construction — fill vs. hatch vs. dash. Amber is applied to the
POSITION family, and it is the fourth channel, never the first.

**The hatch is doing real work.** A hatched chip reads as provisional at a
glance and never resolves into the solid outcome chip at any size, contrast or
viewing distance. Screen 12 shows the greyscale proof: with all colour removed,
`AUTHORIZED — granted by commission order` and `REQUESTED — what the utility
asked for; not granted` remain instantly distinguishable.

Additionally, on any answer that shows both, the requested card carries an
explicit reconciliation line pointing at the outcome — *"This figure was
requested, not authorized. The commission authorized 9.60% — see citation
[2]"* — placed adjacent to the assertion it supports (`AC-F36-10`).

### 5.3 The combined space

4 tiers × 3 families = **12 legible states**, of which four are structurally
unreachable because the schema forbids them (an `AUTHORIZED` claim requires a
tier-4 document and a `DECIDED` case, enforced at write time). Screen 12
renders the full matrix. The unreachable cells are shown as unreachable, which
turns a schema invariant into something a reviewer can see.

`ASM-UX-4` · *Assumption*: `IMPLEMENTED` is treated as an OUTCOME-family value
even though a compliance filing is a lower-ranked document than a final order.
Rationale: `IMPLEMENTED` means "in effect", which is a stronger claim about the
world than `AUTHORIZED`, not a weaker one. The two axes are genuinely
orthogonal and the design must not let the document tier quietly demote the
claim status.

---

## 6. The hard problem #2 — the coverage panel, and "silence is not clearance"

This is the hardest design problem in the project, and it has a precise
statement. The UI must make these two responses **visibly, structurally,
un-confusably different**:

- **A**: "I checked 40 comparable cases and none of them was comparable."
- **B**: "I checked nothing."

Both produce a refusal. Both, in a naïve design, produce an empty flag list.
If they look alike, the product has a silence-is-clearance failure
(`RCA-R7`, standing constraint 4, A7.2 harm #3) and every other guarantee in
the system is decoration.

### 6.1 The five mechanisms

**1. Coverage is never optional and never collapsed.** It renders on every
terminal state including all four refusals (`AC-F37-01`, `AC-F37-07`). There
is no disclosure control on it.

**2. The headline is arithmetic, in words, above the fold.**
*"Checked 40 candidate cases · included 0 · excluded 40 · could not assess 0."*
Followed by an explicit reconciliation line: *"40 = 0 + 40 + 0 — every
candidate is accounted for."* This is deliberate pedantry. It makes the
invariant `included + excluded + unassessable == candidates_considered`
(`AC-F27-12`) visible to the user rather than only to a test, and it means a
future bug that drops a candidate silently becomes a visible arithmetic
mismatch on screen.

**3. The zero case is a different element, not an empty one.** This is the core
move. When `candidates_considered == 0` the coverage bar is **not rendered at
all**. It is replaced by `.coverage-none`: a dashed, hatched band, headed
**"Nothing was examined"**, with the filter values that produced the empty set
printed inside it as a definition list.

   A zero-length bar, or a bar rendered empty, scans at a glance as "all
   clear". A dashed hatched band with no bar geometry cannot be scanned that
   way — there is nothing in it that looks like a measurement. This is the
   single most important pixel-level decision in the proposal, and screens 06
   and 07 exist next to each other so it can be judged rather than asserted.
   Screen 07 ends with the two panels side by side.

**4. Every empty region renders explicit text, never a bare empty list**
(`AC-F37-05`, `AC-F48-04`). `.coverage-empty-note` — a dashed inset box with a
sentence — is used for every zero region, and the sentence is *specific to why
it is zero*:
   - "None excluded — no candidate was removed on any dimension." (nothing was
     wrong)
   - "None excluded — no candidate reached the comparability stage to be
     excluded from it." (nothing was examined)
   Two zeros, two different sentences. The count alone is never the message.

**5. `known_exclusions` is a permanent section titled "Standing limits of this
corpus"**, present on every response and never empty (`AC-F37-06`,
`AC-F28-06`). It carries the four standing limits — riders excluded, discovery
and transcripts not ingested, scanned filings quarantined, supersession
detected only from explicit references. This is the part of "what we didn't
look at" that is true of *every* query, and separating it from the per-query
exclusions is what stops it being read as a per-query finding.

### 6.2 The bar

Where candidates exist, a single stacked bar shows included / excluded /
unassessable. The three segments are differentiated by **fill pattern as well
as tone** — solid, diagonal hatch, flat light — so the bar survives greyscale.
It carries `role="img"` with an `aria-label` restating the counts, and a text
key beneath it. The bar is decorative reinforcement of the sentence above it;
removing it loses nothing, which is the correct dependency direction.

### 6.3 Exclusions name their dimension

Every excluded entry carries case identity, the **named dimension** that
excluded it, and a plain-language reason (`AC-F28-08`). On screen 06, forty
exclusions are grouped by dimension with every case id enumerated and the
reason stated once per group — the reason is *why that dimension is
disqualifying*, not a restatement of the value. "You asked about vertically
integrated utilities; these are restructured wires-only. The composition of the
revenue requirement differs in kind, and the structural spread is unrelated to
case merits."

`ASM-UX-5` · *Assumption*: grouping long exclusion lists by dimension is
permitted, provided every case identity is individually visible and no entry is
truncated. A flat list of forty is unreadable and would defeat the purpose. If
the corpus grows past a few hundred candidates, the panel virtualises the list
but **never** truncates without stating the count and never hides a dimension
group.

---

## 7. The other required resolutions

### 7.1 Refusal is never styled as an error

Carried directly from `policy-lookup-assistant` and hardened by `AC-F38-02`.

- **No red, no warning triangle, no alert role, no error/danger semantics.**
- **The words "error", "failed" and "problem" appear nowhere in the refusal
  panel.** This is enforceable and was checked mechanically across all twelve
  pages. One real instance was found and fixed during this pass: on screen 10
  the refusal panel had printed the raw run-status enum `FAILED` inside a
  definition list. It is now glossed as *"did not complete"*. **Note for
  `code-agent`: the rendering rule is about visible text, not stored values —
  any enum value whose literal contains a forbidden word must be glossed at the
  render boundary.**
- **A refusal has the same visual weight as an answer.** Same panel, same
  padding, same type scale. It is distinguished by a dashed left rule and a
  neutral pill reading *"No answer given"* — not by being smaller, greyer or
  apologetic. Making a refusal look like a lesser outcome teaches users to
  route around it, which converts a working guardrail into a nuisance.
- **The only red in the entire product is the system-failure panel**, which
  carries `role="alert"` and is the only component that does. Screen 09 puts
  the two side by side, because the correct user response differs completely:
  rephrase, versus tell someone.

### 7.2 Every refusal names the gap

`AC-F31-05/06`, `AC-F38-03`. "I don't have enough information" sends the user
off to guess, which reproduces the harm outside the tool. So the refusal panel
carries a structured **`.refusal-gap`** block — not a sentence, a definition
list:

```
Missing dimension   test_year_convention × market_structure (in combination)
You asked for       FPFTY · VERTICALLY_INTEGRATED · since 2023-01-01
Corpus holds        FPFTY only for RESTRUCTURED_WIRES_ONLY (PA PUC)
Corpus holds        VERTICALLY_INTEGRATED only with FORECAST test years (CPUC)
```

A structured block rather than prose because the gap is the actionable content
and prose buries it. Below it, refusals offer **"Questions this corpus can
answer instead"** — narrower questions, explicitly framed as *not workarounds*,
with a line stating that the system will not combine their answers if both are
asked. That last sentence exists because the extrapolation trap's natural human
response is to ask the two halves separately and blend them by hand.

### 7.3 `NOT_STATED` vs. parse failure

`AC-F14-10` / `AC-F14-11`, `RCA-R5`. Different facts, therefore different
components, different wording, different next action:

| | **`NOT_STATED`** | **Extraction gap (parse failure)** |
|---|---|---|
| The fact | The document is silent | The figure is there; we could not read it |
| Data | A `Claim` row exists, `claim_status = NOT_STATED`, no value, verbatim quote | **No `Claim` row.** An entry on the ingest run's extraction-gap list |
| Rendered as | An **answer**, with a citation card (`--absent`, dashed) | A **refusal**, plus a run-report entry |
| The evidence | The settlement's own black-box language, quoted | The document and parameter named on the run report |
| Wording | "The settlement did not specify a return on common equity." | "The ROE could not be read from the ingested document. This is a gap in extraction, not a statement that the decision is silent." |
| User's next action | Nothing. This *is* the answer. | Open the source document; the gap is reported so it can be closed |

Screen 05 renders both side by side. The rule that makes it work: **the system
never asserts a document is silent unless it has a quote proving the silence.**

### 7.4 Vintage and staleness

Two distinct components, because "one of these is old" and "all of this is old"
are different findings (`AC-F32-02` vs `AC-F32-03`):

- **Per-case vintage caveat** — a row in the comparability table at severity
  `CAVEAT`, naming the case's order date against the configured window, plus a
  `.card-flag` on the citation card itself.
- **All-cases-stale caveat** — an answer-level `.vintage-caveat` block naming
  the oldest and newest supporting order dates. Screen 04 renders both, the
  second as a labelled variant.

Every citation card shows a date, always labelled as an **order date** or a
**filing date** (`AC-F36-04`, `AC-F48-02`). There is no card layout in which
the date is optional — it is a required row in `.citation-meta`, not a
conditional flourish.

### 7.5 Corpus freshness banner

Four states, screen 10. `default` / `--stale` / `--never`, plus the
did-not-complete case which reuses `--stale`.

- Stale states state the **age in days**, not only the date. "2 June" does not
  compute to "over two months" at a glance mid-task; "66 days old" does.
- A **failed** run (or an unfinished one) never advances the as-of date
  (`AC-F39-05`, amended `ASM-26`). A **`PARTIAL`** run *does* advance it — the
  literal original reading (partial withholds too) made the corpus
  permanently undateable, since a real corpus quarantines something on
  essentially every run. The banner reports the last `SUCCEEDED`-or-`PARTIAL`
  run and mentions a newer `FAILED` one separately.
- The never-succeeded state is dashed and hatched so it does not read as a date
  at all, and it is **load-bearing**: the surface refuses to answer over a
  corpus it cannot date (`AC-F39-04`, `FDA-5`), and that refusal is rendered.
- The date in the banner and the date on the coverage panel are the same value
  (`AC-F39-06`). One fact, one value, two places.

### 7.6 Comparability — named dimensions, never a score

`AC-F27-09` forbids a scalar score being representable at all, so the UI has no
component that could render one. Comparability is a **table**, one row per
dimension, with four columns: dimension name, the question's value, the case's
value, and a severity word.

- Severity is a **word** — `MATCHED` / `CAVEAT` / `INFO` / `UNASSESSED` — with
  colour redundant. There is no gauge, no percentage, no star rating, no
  "87% similar".
- A dimension the corpus does not record renders `UNASSESSED` with its reason
  and is **not** counted as matched (`AC-F40-06`, `AC-F27-10`). Screen 04 makes
  this explicit in prose beneath the table, because "unassessed" quietly
  collapsing into "fine" is exactly the drift this project cannot afford.
- **Blocking mismatches never appear here.** They are exclusions, and they
  appear in the coverage panel's excluded list (`AC-F40-05`). Caveat region and
  exclusion list are disjoint by construction.
- Where everything matched, the region states so in words —
  `.all-matched-note` — and is never empty (`AC-F40-04`).
- The non-precedent clause is rendered as a **verbatim quote with its locator**
  (`AC-F40-03`), not a summary. The document's own sentence disclaiming
  precedential use is more persuasive than any paraphrase of it.
- **No directional claim about settled vs. litigated outcomes appears
  anywhere** (`AC-F27-13`). The dimension is named; no spread is asserted.

---

## 8. Visual language

### 8.1 Colour

**Warm paper, cool ink, one accent, and functional colour in exactly three
places.** Full token table with contrast ratios on screen 12.

| Token | Light | Role | Contrast |
|---|---|---|---|
| `--paper` | `#FBFAF9` | page background | — |
| `--surface` | `#FFFFFF` | panels | — |
| `--ink` | `#16191D` | primary text | 16.2:1 |
| `--ink-2` | `#464C54` | secondary text | 8.4:1 |
| `--ink-3` | `#62696F` | tertiary / labels | 5.6:1 |
| `--accent` | `#1F4A7A` | links and focus **only** | 8.0:1 |
| `--outcome-bg` | `#2B3138` | filled chips, spine, bar | 12:1 on white text |
| `--position-*` | `#FBF3E2` / `#6F4600` | POSITION family and caveats | 7.3:1 |
| `--error-*` | `#FBEEEC` / `#8A2418` | **system failure only** | 7.6:1 |

Rationale for each choice worth defending:

- **Warm paper rather than cold white.** This is a document tool. A very
  slightly warm ground reduces the clinical-database feel that the material
  pulls toward, at zero cost to contrast, and makes the white citation cards
  read as *pieces of paper on a desk* rather than *rows in a table*. This is
  most of what makes screen 03 feel calm despite carrying a great deal of
  information.
- **One accent, used for links and focus only.** Not for headings, not for
  emphasis, not for the submit button. Accent-as-decoration is what makes dense
  tools noisy.
- **No green anywhere.** An answer is not a "success" and a refusal is not a
  "failure". Green/red framing would teach analysts that a refusal is a bad
  outcome to be worked around — the precise behaviour that converts a working
  guardrail into a nuisance.
- **No gradients, no shadows beyond a 1px lift on the ask form.** Nothing is
  decorated to look modern. The one thing this interface must project is that
  it is not embellishing anything.
- **Amber does double duty** — POSITION status and CAVEAT severity — because
  they are the same idea: *provisional, handle with care*. Reusing the hue
  reduces the palette rather than overloading it.
- **Red appears exactly once in the product**, on `.syserror-panel`. Its
  scarcity is what gives it meaning.

**Dark theme ships**, via `prefers-color-scheme`. It is a token swap that
preserves every contrast ratio and every non-colour channel; the spine, hatch
and dash constructions are hue-independent by design so nothing about the
encoding changes between themes.

### 8.2 Typography

**Three system stacks, no web fonts.** Nothing to download, nothing to fail, no
layout shift, no CDN call from a tool handling regulatory material.

- **UI stack** (`ui-sans-serif`/`-apple-system`/`Segoe UI`) — all chrome, labels
  and answer body.
- **Serif stack** (`ui-serif`/Georgia) — the echoed question and every
  **verbatim quote**. The serif is a semantic signal, not decoration: serif on
  this surface means *these are the document's own words, not ours*. It is used
  nowhere else.
- **Mono stack** with `font-variant-numeric: tabular-nums` set globally —
  docket numbers, locators, dates, enum values, and every figure. Columns of
  ROE figures align; `R-2024-3042569` never wraps mid-identifier.

Scale: 28 / 20 / 17 / 15 / 13 / 11px, line-height 1.55 body and 1.25 headings,
body measure capped at 68 characters. Dense reference material lives in tables
and cards, not in long prose — the longest paragraph on any answer screen is
three lines.

The **eyebrow** (11px, 700, 0.09em, uppercase) is the workhorse that makes
density readable: it labels every region so a returning user can jump to
"Standing limits of this corpus" without reading anything above it.

### 8.3 Motion

Effectively none. A single low-amplitude in-flight indicator. No transitions on
answer render — an answer that fades in invites reading it before the coverage
strip has arrived.

---

## 9. Environment constraints, and what was deliberately not done

### 9.1 No Figma, no DesignSync push — stated honestly

**No design-system push was made, and none was faked.**

The available Figma account is a **Starter plan with a View seat**: six MCP
tool calls per month and **no write access**. Figma writes and a Claude Design
`DesignSync` push are therefore unavailable in this environment. Per the
instruction for this gate they were not attempted, and per the precedent set by
`policy-lookup-assistant`'s `UX_KB.md` §2 — which recorded its DesignSync auth
failure rather than pretending — the gap is recorded here rather than papered
over.

This is the second project on this platform to hit a design-system tooling
wall, from a different cause. That is now a pattern worth naming rather than a
one-off:

> **`ui-ux-designer`'s design-system push has never once succeeded on this
> platform.** Twice the contract's step 2 has been unexecutable for
> environmental reasons. The contract treats the push as a normal step and the
> rendered `design-review/` pages as the reviewable artefact; in practice the
> rendered pages have been the *only* artefact both times. This is queued as
> feedback for `admin/LESSONS.md`: either the environment gains a working
> path, or the contract should stop presenting the push as routine.

**What we have instead is arguably better for this project.** The
`design-review/` pages are not mockups of a component library — they *are* a
component library, in the target technology, with a stable class contract
(§8, screen 12). `code-agent` can read the markup directly rather than
translating from a design tool. The component inventory on screen 12 is the
handoff.

**If DesignSync access ever becomes available**, the push order should be:
`.citation-card` (with all three variants and the authority spine) and
`.coverage-panel` (with the `.coverage-none` band) **first**, since those two
directly encode `RCA-R1` and `RCA-R7`; then `.refusal-panel`, `.status-chip`,
`.dim-table`, `.rca-freshness`; then the rest. Incremental, component by
component, never a wholesale replace.

### 9.2 Explicit non-goals for this pass

- **No mobile layout.** Out of MVP scope per `PROJECT_CONTEXT.md`. Not silently
  omitted — stated.
- **No session history / Q&A ledger** (`ASM-UX-2`).
- **No aggregate, benchmark, distribution or peer-comparison visual of any
  kind.** `ASM-14` defers `F33`, and there is deliberately **no chart component
  in this design system at all**. A bar chart of authorized ROEs across cases
  is one CSS class away from being an implied average, and an average is the
  delivery mechanism of the project's worst harm. When `F33` lands, the chart
  is a design decision to be taken deliberately, not a component already
  sitting in the kit.
- **No export, print stylesheet or PDF view.** `F41` deferred. Worth flagging:
  an analyst *will* copy figures out of this tool into filed material, and the
  citation card is currently optimised for reading rather than for copying. A
  copy-with-citation affordance is the highest-value small addition once export
  is on the table.
- **No login/authentication UI.** `ASM-12` ships role binding, not login. The
  session role is displayed as a standing chip in the app bar.
- **No frontend implementation.** `code-agent` builds this. The
  `design-review/` markup is a reference, not the application.

### 9.3 Full assumption register from this gate

| ID | Assumption |
|---|---|
| `ASM-UX-1` | Single-purpose, no-navigation surface for MVP1; rail and full-width column reserved for `F51`/`F41`. |
| `ASM-UX-2` | No session history in MVP1 — two coverage panels on one page risk a coverage statement being read against the wrong answer. |
| `ASM-UX-3` | The 14 `document_type` values bucket into 4 authority tiers along the enum's own ranking; tier boundaries coincide with existing schema invariants. |
| `ASM-UX-4` | `IMPLEMENTED` belongs to the OUTCOME chip family despite `COMPLIANCE_FILING` ranking below `FINAL_ORDER` — the axes are orthogonal and status must not be demoted by document tier. |
| `ASM-UX-5` | Long exclusion lists may be grouped by dimension provided every case identity remains individually visible and nothing is truncated. |
| `ASM-UX-6` | The session chip reads "public + internal corpora" — MVP1 serves one utility-side role that can see work-product records, which is why `AC-F36-08` needs a work-product card at all. **The actual retriever binding is `solution-architect`'s call at gate 6**; if the binding turns out to be public-only in MVP1, the work-product card variant stays in the kit unused and the chip text changes. Flagged rather than assumed silently. |
| `ASM-UX-7` | Coverage appears twice (strip + panel) rather than once. Costs vertical space; buys the guarantee that coverage is above the fold on every answer. |
| `ASM-UX-8` | Refusal panels offer alternative questions. There is a real risk this reads as "here's how to get the number anyway", so each instance carries an explicit line stating the system will not combine the answers. If red-teaming shows users treating these as workarounds, **remove them** — the guarantee outranks the convenience. |
| `ASM-UX-9` | The in-flight indicator names pipeline stages. This exposes internal architecture to the user, which is unusual; justified because it makes the metadata-before-similarity ordering (`RCA-R14`) visible, and because a skeleton screen is a rendered empty coverage panel. |
| `ASM-UX-10` | All content in `design-review/` is illustrative. Docket-number **formats** and URL **shapes** are the real ones per commission, because those are what the citation card must render; the values are not represented as real filings. |
| `ASM-UX-11` | No chart or aggregate visual component exists in the design system, deliberately, so that `F33` cannot be built by reaching for one that is already there. |

### 9.4 Open items for downstream gates

1. **`solution-architect` (gate 6)** — confirm the MVP1 session's corpus
   binding, which determines the app-bar session chip and whether the
   work-product citation-card variant is reachable (`ASM-UX-6`).
2. **`code-agent`** — the enum-gloss rule at the render boundary (§7.1). Any
   status or reason enum whose literal contains "error", "failed" or "problem"
   must be glossed before it reaches the refusal panel. This was a real defect
   found and fixed in this pass, not a hypothetical.
3. **`test-agent` / this agent at gate 8** — the UI suite's four invariants
   (`F48`) map to: the greyscale/text assertion on §5, the date-always-present
   row in `.citation-meta`, the refusal-neutrality scan of §7.1, and the
   `.coverage-empty-note` assertion of §6.1. All four are mechanically checkable
   against the rendered surface, and the refusal-neutrality scan should be run
   against the *whole* refusal panel subtree, which is how the screen-10 defect
   was caught.
4. **`responsible-ai-architect`** — `ASM-UX-8` (alternative questions on
   refusals) is the one decision here most worth red-teaming.

---

## 10. Observed post-deploy behaviour

_Empty. Nothing has been built or deployed. This section is a running log, not
a spec section, and will be populated with:_

- _UX/accessibility suite results once `dev/tests/suites/ux/run.sh` exists (it
  does not yet — `F2` builds the harness from scratch per the custom-template
  override)._
- _Flow-test evidence once a real UI exists, per `test-agent`'s per-scenario
  evidence convention in `projects/rate-case-analyzer/test-evidence/`._
- _Real usage observations: in particular, whether analysts read the coverage
  strip, whether refusals are treated as answers or as obstacles, and whether
  the alternative-questions block of `ASM-UX-8` is being used as a workaround._

**Status of this agent's test suite as at 2026-08-07: `dev/tests/suites/ux/run.sh`
does not exist.** No UX or accessibility suite has been executed for this
project. Nothing in this document should be read as a passing accessibility
result — the contrast ratios in §8.1 are computed design targets, and the
greyscale and refusal-neutrality properties in §5 and §7.1 were verified by
static inspection of the `design-review/` markup, not by a suite run. When the
harness lands, all of it is re-run for real.

---

## Change history

| Date | Version | Change |
|---|---|---|
| 2026-08-07 | 1.0.0 | Initial pass. Gate 5 · Experience Design, written under the recorded full-autonomy instruction. Twelve rendered screens at `design-review/`, eleven numbered assumptions, four open items. No DesignSync/Figma push — recorded as an environment constraint in §9.1, not skipped silently. |
