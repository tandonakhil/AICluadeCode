# UX Knowledge Base — `conclave-finance-studio`

Owner: `ui-ux-designer` · Gate 5 · Experience Design
Created 2026-07-31 · **Status: proposed under standing authorization
(`batch_authorized`), rendered artefact available, awaiting human review**

**Rendered mockup (this is what approval is given from, not this file):**
`projects/conclave-finance-studio/design-review/index.html` — self-contained,
light and dark, seventeen sections covering every screen in
`FUNCTIONAL_SPEC` §23.

**Write set for this pass, declared:**
1. `projects/conclave-finance-studio/design-review/index.html` — created (new file)
2. `projects/conclave-finance-studio/knowledge/UX_KB.md` — this file (new)

Nothing else was created or modified. `PROJECT_CONTEXT.md`, `PLAN.md`,
`FEATURES.md`, `FUNCTIONAL_SPEC.md` and `pipeline-state.json` are untouched —
the Decisions Log line for this gate is owed by the orchestrator, and the one
criterion I want *added* (§9.1 below) is `functional-design-agent`'s to issue.

**Inputs read in full for this pass:** `knowledge/FUNCTIONAL_SPEC.md` (all 186
criteria, §23 observable-UI map, §24 edge/empty/error map, §25 open
ambiguities), `PLAN.md` §6.2 (routes and module structure), §7 (full backlog,
build-now / deferred / refused), §8 (phase 2), §9.2 (reversible assumptions),
`knowledge/DOMAIN_KB.md` §6.2, §7.2, §10.2–§10.7, `knowledge/INDUSTRY_KB.md`
§14, §15.4, and `PROJECT_CONTEXT.md`'s **full** Decisions Log including the
entries recorded after the request that triggered this invocation.

This file has two parts, and it is meant to keep both for the life of the
product:

- **Part A — design intent**: what I proposed and why. Written now.
- **Part B — observed post-deploy behaviour**: how the design actually
  performed once real people used it. Empty until there is production usage,
  and explicitly marked as empty rather than omitted.

---
---

# PART A — DESIGN INTENT

## 1 · The brief, restated so it cannot drift

The product is a set of month-end close agents sitting on Oracle ERP Cloud data
in a warehouse. **It is not the GL.** It detects and resolves close anomalies
and can trigger postings into Oracle. Three personas: staff accountant (does),
controller (supervises and signs), FP&A analyst (explains). MVP1 is **desktop
web only** and **ERP-data-only**. The surface is a natural-language,
skill-based interface: select datasets, ask an agent to act under guardrails.

### 1.1 The design problem is not the one it looks like

`INDUSTRY_KB` §15.4 carries an anti-recommendation that inverts the intuitive
design:

> Reviewers given **clearer** AI explanations **defer more, not less.**

So the 11pm-on-day-3 approval problem **cannot** be solved by presenting the
agent's reasoning beautifully. Doing so makes the control *weaker*.
`FUNCTIONAL_SPEC` §12 carries a matching standing exclusion — no criterion
asserts explanation quality and none may be added — and I have not read its
absence as a gap.

`DOMAIN_KB` §7.2 sharpens it: you cannot make a fortieth approval at 11pm
meaningful by improving its layout, because the constraint is **attention
budget**, which is fixed, small, and already spent. And **uniform approval
undifferentiated by risk is the same as no scrutiny** — if a $0.00 no-activity
account and a $4M judgemental accrual both present as one click, the design has
actively destroyed the risk signal the accountant needs.

### 1.2 The design principle everything below descends from

> **Design for a depleted reviewer, not an attentive one.** Reduce what reaches
> them, differentiate what does by risk, give the page to the riskiest element,
> and demote the explanation.

Four mechanisms, all of which the criteria already support:

| Mechanism | Where it lands | Criteria |
|---|---|---|
| **Volume reduction, made visible** | N detected → M routed is the masthead of Exceptions | `AC-F41-09` |
| **Effort scales with risk** | Highest band requires typed, unlistable input; lowest is a single resolution click | `AC-F35-05` (as a floor, not a ceiling) |
| **Riskiest element, not clearest narrative** | Review's first band, largest type, never collapsible | `AC-F41-03` |
| **Override-rate + probe monitoring** | Monitors — override rate per agent and per user; probe outcomes **aggregate only**, never per named person | `AC-F41-07`, ~~`AC-F12-08`~~ → `AC-F12-10` (RETIRED 2026-07-31 — see §5.9's editorial marker), `AC-F41-08` |

---

## 2 · The inversion: the explanation is the collapsed element

**The agent's supporting narrative is last in the reading order on the Review
screen and closed by default. The risk band is first and uncollapsible.**

This is the single most consequential decision in the design and it is a
deliberate inversion of the intuitive layout, in which the AI's reasoning is
the hero. Three arguments for it:

1. **§15.4 directly.** Clearer explanations increase deference. An explanation
   that is prominent, formatted and open is *more* persuasive, and persuasion
   is what we are trying to reduce.
2. **It makes `AC-F12-03` carry information.** The criterion requires the
   capture record to name which evidence elements the reviewer expanded and
   which they left collapsed. If the narrative is expanded by default, that
   label is a constant across every reviewer and every item and its information
   content is **zero** — F12's ground-truth factory produces a column of
   identical values. Collapsing it turns "did this person open the reasoning?"
   into a real per-item, per-reviewer signal the controller can read on
   Monitors. **The design decision and the measurement decision are the same
   decision**, and this is the strongest argument I have.
3. **It puts evidence before commentary.** The Review screen's second block is
   the raw four-period residual table — the data, before anyone's reasoning
   about it. A reviewer who reads the data first and the narrative second (or
   never) is doing the job. The reverse order is how the self-justifying
   reconciling item of `DOMAIN_KB` §6.2 survives twelve periods.

**What I explicitly did not build:** no confidence score rendered as a
reassuring bar, no "explanation quality" component, no summary-of-the-reasoning
hero, no agent avatar or conversational framing on the approval surface. The
Ask screen is conversational; the Review screen is a working paper.

---

## 3 · Visual language

### 3.1 What this should feel like

An **evidence instrument**, not an analytics product. Reference points: a
working paper, a bank statement, a legal exhibit. The audience is a controller
and a staff accountant in an energy utility, and the downstream reader is an
external auditor holding a greyscale printout inside a workpaper. High
information density is correct — finance users read dense tables fluently and a
sparse, airy consumer layout reads as *unserious* to this audience.

Contrast this deliberately with a consumer-facing billing chatbot: same
industry, opposite visual register. This product should look like something
that gets filed.

### 3.2 The palette rule: there is no green

**Green does not appear anywhere in this product.** Not for a clean result, not
for a passed check, not for a met prediction.

Green means "fine, move on." That is precisely the affect a depleted reviewer
must not be handed, and `PLAN` §2b already warns that a control which cannot
fail trains its reviewer that the dashboard cannot fail. A clean result renders
in **neutral ink**, as a sentence carrying its coverage, with no colour at all.
The strongest result this product can produce — no exceptions at 100% coverage
— still does not get a tick.

Colour is reserved for exactly three jobs:

| Job | Treatment | Tokens (light / dark) |
|---|---|---|
| **Risk** — three ordinal steps, one hue family | Structural left bar on rows; band border on Review | `#B45309` / `#D9932F` · `#B42318` / `#E8695A` · `#7A1214` / `#FF8C7C` |
| **Permanence of refusal** | Slate, solid, heavy left rule — deliberately *not* red, because a refusal is not an error | `#334155` / `#94A3B8` |
| **Interactivity** | One restrained ink blue, controls only, never data | `#1D4ED8` / `#7AA2F7` |

Everything else is ink and rule on paper: base `#F6F6F3` / `#0E1013`, surface
`#FFFFFF` / `#16191F`, ink `#14161A` / `#E7E9ED`.

Two supporting rules:

- **Risk is a three-step ordinal ramp in one hue family, not a rainbow**, so
  "worse" is legible without a legend and survives print. Desaturated
  deliberately — saturated red at close volume becomes wallpaper by item ten.
- **Uncertified / non-evidential state is carried by a hatch pattern *plus* a
  sentence, never by hue alone.** It must survive greyscale, colour-vision
  deficiency and PDF export into a workpaper. Colour-as-sole-carrier is an
  accessibility failure and here it is also a control failure.

Dark mode is a first-class theme, not a courtesy — this product is used at 11pm
on day 3. Dark keeps the risk ramp getting *brighter* with rank so the ordinal
reading survives inversion; it is not a hue rotation of the light theme, because
a desaturated dark red on a dark ground would be the least visible element on
the page, which is the opposite of what the risk band is for.

### 3.3 Typography and numerals

- System sans for prose.
- **Tabular lining numerals for every figure, without exception.** Proportional
  digits in a finance product are a defect, not a preference — column
  comparison is the primary reading act.
- Monospace for amounts, account codes, periods, hashes, decision IDs and
  dataset versions, so a bundle hash and a dollar figure are never confusable
  with body prose.
- Amounts right-aligned, account codes left, always.
- Designed at 1440×900. **No responsive breakpoint below tablet in the product
  design** — see §10.4 on the surfaces discrepancy.

---

## 4 · Information architecture

Nine screens, named by `FUNCTIONAL_SPEC` §23 and routed by `PLAN` §6.2. I keep
every name and every route. I group them three ways:

| Group | Screens | Whose job |
|---|---|---|
| **Work** | Ask · Exceptions · Review · Dispositions | The staff accountant's night |
| **Govern** | Monitors · Catalogue · Inventory | The controller's week |
| **Evidence** | Audit · Refusals | What leaves the building |

> **Editorial marker (gate 10).** A2.2 proposes an IA that replaces this
> section, and the 2026-08-02 change-history row calls §4 *superseded*. That is
> true of the **proposal** and not of the **product**: the shipped pilot's nav
> groups are **Work / Govern / Evidence — this section's grouping**, filled with
> A2.2's demotions and merges. A2.2's flat four-item shape is not built. See
> A2.2a for the full reconciliation. Neither grouping is human-approved.

**Refusals sits under Evidence, at top level, not in a settings drawer.** It is
an artefact a controller takes to an audit committee. Burying it makes a
refusal look like an omission — the exact failure `AC-REFUSAL-02` exists to
prevent.

**Nav badges are the volume control, expressed in the chrome.** The badge on
Review is the number routed to *this person tonight*, not the number detected.
A reviewer who sees "3" before clicking is budgeting attention correctly; one
who opens a screen and discovers 40 has already lost.

Entity, period and close day sit permanently under the product name, because
every figure here is meaningless without them and `AC-F38-11` requires
staleness relative to the close clock on the same surface as the figure.

---

## 5 · Screen-by-screen design intent

### 5.1 Ask — dataset selection inverted into a declared-population panel

`INDUSTRY_KB` §14 is unambiguous: dataset selection is a **control failure, not
user error**, and **under-selection is the failure that bites** because it is
invisible. A 70% scan returns a clean result pixel-identical to a 100% scan.

**So I inverted the selector. The user does not pick tables from a list.** The
skill declares the population it needs, and the screen shows each declared
segment as covered or not covered, **by name**. Under-selection stops being an
absence the user cannot perceive and becomes a list of named unmet segments
they have to look at. A multi-select dropdown structurally cannot do this; a
declared-population panel does it by construction.

Second consequence: **the coverage read-out is not a progress bar.** A bar
filling toward the right reads as "70% good". It is a **population strip with
the gaps drawn in and labelled** — the missing segments are the graphic, not
the absence of graphic, and they are hatched so they read as gaps in
greyscale.

Also on Ask:

- The resolved certified query name, its version and the bound parameters are
  shown **before submit is available** (`AC-F39-01`) — the user approves the
  interpretation, not just the answer.
- The submit control **states the coverage in its own label**: "Run over 897
  accounts — partial, 70%". There is no unqualified "Run" button.
- Ambiguity forks are explicit (`AC-F39-07`). "Unusual movement in clearing
  accounts" maps equally to a present-anomaly detector and a cross-period
  accumulation detector. Those answer materially different questions; a silent
  pick hands the user the wrong one with no signal. Both are named, the user
  chooses, submit is unavailable until they do.
- Uncertified datasets remain freely selectable in the exploration tier and
  carry a permanent hatch and the sentence *"not certified — cannot support a
  posting or a no-exceptions conclusion."* The state follows the dataset onto
  every derived result and **no affordance dismisses it** (`AC-F38-10`).

### 5.2 Exceptions — volume reduction as the masthead

`AC-F41-09` requires N and M both visible. **I made the ratio the masthead**,
because it is the only object on the screen that tells a reviewer whether the
system is working for them or dumping on them. A product whose N/M ratio
degrades is failing at its actual job even when every individual finding is
correct.

The mockup shows 214 detections → 9 routed, with the disposition of the other
205 stated (168 by cold-approved policy, 31 as unexpired prior-period R1, 6 as
duplicates) and all 205 reachable. **Nothing is hidden; things are ranked.**

- Rows are **ordered and banded by risk**, with a structural left bar rather
  than a dot or a coloured word — at close volume a legend-dependent signal is
  not read.
- Omission findings and present-anomaly findings carry **visually distinct
  labels** (`AC-F29-12`, `AC-F42-08`): omission is a solid heavier pill,
  present-anomaly a dashed one. These are the two sides of the wedge test and
  they must never be confusable.
- The five boundary checks each render an individual result, and **"not run"
  renders in risk colour, not neutral**. Silence is never a pass (`AC-F28-07`,
  convention C2). A check that could not run is closer in meaning to a failure
  than to a pass, and colouring it neutral would be the single most dangerous
  small decision on this screen.
- Coding findings render their backtest precision and recall **with the bias
  label adjacent at equal weight** — *"recall is measured against caught errors
  only"* (`AC-F33-07`). Schema, not footnote. A precision figure with a silent
  caveat is how a measurement becomes a claim.

### 5.3 Coverage states — coverage changes the grammar of the conclusion

`AC-F38-07` was the criterion I designed hardest against: a 70% clean run and a
100% clean run must be textually different on screen, in the dossier and in the
export.

**My answer is that coverage is not a status line near the conclusion — it
changes the grammar of the conclusion itself.**

| Coverage | Rendered conclusion |
|---|---|
| **100%** | "No exceptions across the full declared population. All 1,284 declared accounts were scanned (100%). Nothing was excluded." — universal quantifier, neutral ink, no colour |
| **70%** | "No exceptions *in the 897 accounts scanned*. 387 accounts were not scanned: Intercompany — NGH-CA-200 (312) and FX revaluation subledger (75). **This run cannot support a no-exceptions conclusion for June 2026.**" — bounded quantifier, names the bound, risk-coloured border |
| **0%** | The findings region is **absent, not empty**: "Nothing was scanned. No findings conclusion has been produced." (`AC-F38-08`) |

**Build consequence for `code-agent`:** the conclusion component must be
*structurally incapable* of emitting the strings "clean", "no exceptions" or an
unqualified all-clear when coverage < 100%. Not validated out — unreachable in
that state. An empty findings list at 0% coverage is the most misreadable state
this product could render, so 0% removes the region entirely.

The partial-run banner is **non-dismissable and inline in the result**, not a
toast. There is no "don't show again".

### 5.4 Review — the 11pm screen

Reading order, top to bottom, fixed:

> **risk → evidence → resolution → narrative (collapsed)**

**There is no "Approve" button on this screen for a finding.** The terminal
action is *record a resolution*. Approval exists only where a posting artefact
exists (§5.5). This is a direct answer to `DOMAIN_KB` §10.2: if the UI makes
posting the default terminal state, the safe answer becomes harder to record
than the risky one. `AC-F41-13` requires only that approve not be the *only*
visible terminal action; I have gone further and removed it from the generic
case entirely.

> **Editorial marker (gate 7, pass 23) — `AC-F41-13` is RETIRED.** Retired
> 2026-08-03, body preserved, replaced by `AC-F41-22`/`-23`/`-24`; see
> `FUNCTIONAL_SPEC` §28.1 (and §20). The reasoning above stands and is
> `ui-ux-designer`'s — only the ID's tense is corrected here, because a
> live-tense reference to a retired ID is how a retired ID gets re-adopted.
> The clause this paragraph relies on is now `AC-F41-24`.

**Resolution typing (`AC-F35-09`, `AC-F35-05`).** All six types are one row of
six **equal-sized, equal-weight** buttons, fixed order R1–R6, none
pre-selected. R2 (data-side fix) and R5 (handoff) — the majority outcome per
`DOMAIN_KB` §10.2, and the two no competitor models as first-class — sit in the
middle of the row at identical visual rank to R3/R4. Only R3 and R4 carry a
small "Posts" flag, in risk colour, below the label.

Interaction counts to completion, stated explicitly so `code-agent` and
`test-agent` can check them rather than eyeball them:

| Type | Steps to completion |
|---|---|
| **R2** data-side fix | select R2 → expected clearing period → save = **3** |
| **R5** handoff | select R5 → owner + due date → clearing period → save = **4** |
| **R1** accepted & explained | select R1 → expiry → typed explanation → clearing period → save = **5** |
| **R3** reclass | select R3 → review journal lines → approve lines → clearing period → save = **5** |
| **R4** correcting journal | select R4 → review journal lines → approve lines → clearing period → save = **5** |
| **R6** control-state change | select R6 → confirm the state change → clearing period → save = **4** |

**The safe outcomes are never more effortful than the posting ones.** That
satisfies `AC-F35-05` by construction rather than by inspection.

**In force at approval time** (`AC-F41-05`, `AC-F36-18`): threshold with its
inclusivity stated, guardrail bundle version and hash, decision ID, dataset
version, data as-of relative to the close clock, agent version, and the run's
coverage. All in one panel, all always visible.

**A structural constraint `AC-F41-04` imposes on the design, which I want on
the record because it is easy to violate accidentally: nothing on the Review
screen may be reachable only by hover, only by a live query, or only by lazy
load.** The retained rendered view has to reproduce what the approver saw, so a
tooltip-only fact is a fact that vanishes from the audit record. No tooltips
carrying data, no on-scroll fetches, no numbers that refresh under the reader.

**Structured rejection (`AC-F41-06`)** uses a closed list of six reasons, none
pre-selected, with optional free text *underneath* rather than instead. Free
text alone is unaggregatable and therefore never becomes a control signal —
and rejection reasons are among the highest-value labels this product
manufactures. A closed list turns "the reviewer disagreed" into "reason 3 is
40% of rejections against this agent this period", which a controller can act
on.

**A friction I am keeping on purpose.** `DOMAIN_KB` §7.2.2 predicts the
designer will object to deliberate friction on judgemental items. **I do not
object — I am asking for it.** For the highest risk band, both the reject path
and the R1-accept path require the reviewer to *type* a sentence that is not
selectable from any list. It is slow on purpose. Every other mechanism in this
design reduces work; this specific case is where the work belongs, and removing
the friction here would undo the point of grading risk at all.

**Superseded runs (`AC-F41-12`).** The action area is **structurally replaced**,
not decorated with a warning. A toast saying "this run is stale" is dismissed
by a tired reviewer in under a second and the approve button is still there.
The approve control is **absent, not disabled** — a disabled approve button
still tells a tired reviewer that approving was the expected act. The only
forward action is to open the superseding run, named with its completion time.

### 5.5 The one screen with an approve button — reclass export

Approval is scoped to the artefact that leaves the building. The exact journal
lines are visible **before** the export control is usable (`AC-F40-11`), and
that same rendering is what is retained as the evidential rendered view.

The button reads **"Approve these 2 lines for export"** and the screen states
in plain words: *this does not post to Oracle; it produces a Journal Import
file for a human to load.* "Approve" alone would let a user believe they had
posted (`AC-F40-02` — MVP1 exports, it does not post).

The two-key model is rendered as three named roles: preparer, in-product
approver (the evidence-bearing leg we own), and the Oracle-side poster (outside
this product). CUEC verification date is shown.

### 5.6 Probes — invisible before, revealed immediately after

The criteria require only that a probe be indistinguishable from a genuine
proposal by anything rendered **before** disposition (`AC-F41-08`,
`AC-F12-05`). They are silent on afterwards.

**My call: reveal it the instant the disposition is submitted, with the correct
answer.** Argument: the stated purpose of injected probes in `INDUSTRY_KB`
§15.4 is *to keep attention live*. A probe never revealed is a measurement
instrument only — it measures decay without arresting it. A probe revealed at
the moment of disposition is a measurement *and* a calibration signal delivered
at the one moment the reviewer still holds the item in their head. It is also
the fairest option for the staff accountant, who is otherwise silently scored —
and `DOMAIN_KB` §6.3 is emphatic that the staff accountant is harmed first and
worst by this product's failure modes.

**The cost I accept and want recorded:** reviewers will learn the probe rate
and may recalibrate against it. Mitigation is to vary the rate. I judge this
smaller than the alternative. `responsible-ai-architect` should have a view
before it is built — logged in §9.3 as an open question.

**Build consequence:** no component may render probe status anywhere before
disposition — not a badge, not a distinguishing class name in the DOM, not a
differing skeleton height. That is testable and I want the UX suite to assert
it (§8.2).

### 5.7 Dispositions — making the forward prediction not feel like a tax

`AC-F32-01` makes a disposition **unsaveable** without an expected clearing
period, at every permission level, as a hard save failure and not a warning
that can be acknowledged. It is the most retrofit-hostile item in the backlog
and the one most likely to feel like bureaucracy. Three design moves:

1. **It is not a field, it is the sentence you are already writing.** The
   composer reads *"This clears by ▾"*, and the save control reads *"Record —
   clears by 2026-07"*. Until the period is set the button reads *"Record —
   clears by …"* and does nothing. **The prediction is the shape of the action,
   not a validation error that appears after you thought you were done.** That
   is the whole difference between a control and a tax.
2. **Never pre-filled** — a defaulted prediction is a manufactured one and
   would poison the hit rate that makes the control worth having — but the
   three most common answers (P+1, P+2, P+3) are one tap.
3. **Framed as a promise the product makes to you**, not a hoop: *"We will
   check in 2026-07 and tell you if it did not. If it did not, this account's
   risk grade rises and auto-pass is revoked."* Micro-copy converts an
   obligation into a service, and it also states the R6 consequence up front so
   it is not a surprise next period.

The user's own running hit rate ("31 of 38 met") sits beside the field.

**A risk I want on the record rather than designed around:** showing a user
their own hit rate may push people toward conservative, easily-met predictions,
inflating the measure. I still recommend showing it — an invisible score is
worse, and `DOMAIN_KB` §6.3 argues the reviewer should see what is being
recorded about them. But the controller's view should watch for **horizon
drift** (predictions bunching at the far end of the permitted range), and I
want that watched in the first production period rather than assumed away. It
is the first entry in Part B's watch list.

On the list itself: missed predictions are visibly distinguished from
within-horizon ones (`AC-F32-09`), a missed prediction is a **state change**
and not a notification (`AC-F32-03`), and a lapsed R1 re-enters the exception
queue **carrying its original explanation attached** so the next reviewer sees
what was promised last time (`AC-F35-06`).

### 5.8 Catalogue

All nine certification attributes on one row (`AC-F38-01`). Two design points
worth stating:

- **Staleness is expressed relative to the close clock**, not as an absolute
  timestamp — "2 days behind close clock" is the fact a close professional acts
  on; "01 Jul 22:40" is not.
- **The empty state explains what is consequently impossible**, not that a list
  is empty: "No datasets have been certified in this tenant. Action-capable and
  assurance-emitting skills cannot run." (`AC-F38-13`)

A failed ERP tie-out shows with its date and the action-capable refusal names
it (`AC-F38-12`).

### 5.9 Monitors — the product marking its own homework

**The forward-disposition hit rate is the masthead, not a tile** (`AC-F32-10`).
It is the product's own falsifiability measure, displayed whether good or bad.
The mockup shows 64% — 27 of 42 — deliberately, because a mockup that shows a
flattering number is designing for the demo. Everything else on this screen
measures the agents and the reviewers; this one measures *us*, and putting it
anywhere but first would be a tell.

**No metric on this screen is coloured good or bad.** A high override rate
could mean a reviewer is catching things or that an agent is misfiring; a low
one could mean the agent is right or that nobody is reading. Colouring it
asserts an interpretation the data does not support — and a green dashboard is
exactly the artefact that teaches a controller their controls cannot fail.
Figures are ink. Only *escalations* take risk colour.

Zero override rates render as an **explicit `0.0%` with its denominator**,
never omitted and never blank (`AC-F36-19`).

The per-user table (`AC-F41-07`, `AC-F12-10`) is designed to make one pattern
readable without pre-judging it: 48 items at 38 seconds each, narrative opened
9% of the time. **No colour is applied to that row.** The controller reads it and
makes the judgement; the product does not pre-judge a colleague in a system
whose audit trail is already, per `DOMAIN_KB` §6.3, a liability-allocation
device pointed at the most junior person in the chain. But the row is
*readable*, which it is not in any product on the market today.

Probe outcomes are **not** in that row. They render aggregated by queue, agent,
account and queue-load only, with the G-PROBE-3 note stated on the screen.

> **Editorial marker (gate 10) — `AC-F12-08` is RETIRED, and one clause of the
> original design intent above was overridden, not merely re-numbered.**
>
> Retired 2026-07-31 (pass 2), replaced by `AC-F12-10`;
> `FUNCTIONAL_SPEC` §8 (`AC-F12-08` body, struck) and §27.6 (`AC-F12-10`).
>
> **What I originally designed, preserved here because it was a real intent and
> deleting it would hide why the current screen looks as it does.** This
> paragraph read *"1 of 3 probes caught"* as a column of the per-named-user
> table. The intent was continuous with the rest of §5.9: a controller who can
> see that a reviewer's probe misses cluster in the last hour of a 48-item night
> is reading a **routing and workload** fact, and my argument was that the
> uncoloured, un-pre-judged presentation defended against the misreading —
> exactly the §5.9 argument for showing an unflattering hit rate rather than
> hiding it.
>
> **Why it does not survive.** `RESPONSIBLE_AI_KB` §1.3 G-PROBE-3 prohibits *any*
> per-named-person probe score, ranking or trend exposed to anyone in that
> person's management chain — and the Monitors screen is definitionally a
> management-chain surface, so presentation discipline cannot rescue it. The
> orchestrator's 2026-07-31 gate-6 ruling 4 settles it the same way: aggregate
> only. `RESPONSIBLE_AI_KB` §8 disagreement D1 is where this was argued out, and
> `responsible-ai-agent` won it. I record that as a **correct override of my
> design**, not a technicality: the harm G-PROBE-3 prevents does not depend on
> whether the number is coloured.
>
> **What survives unchanged.** Override rate per agent, per user and per period —
> that was never the contested part, and it lives on in `AC-F12-10` and
> `AC-F41-07`. The uncoloured-figures rule, the explicit-zero rule and the
> hit-rate masthead are all untouched.
>
> **The build is on the correct side of this already** — `pages._probe_panel` is
> aggregate-only over a closed key list and renders the G-PROBE-3 note. This
> marker corrects the *record*, which cited a retired ID in the live tense three
> times and described a per-user probe column the product does not and must not
> have. A live-tense reference to a retired ID is how a retired ID gets
> re-adopted; a live-tense description of a prohibited surface is worse, because
> a future implementer could build it from this file in good faith.

Cross-period escalations (`AC-F9-08`) show which leg raised them, and a
**narrative-only escalation is a first-class row**, not a sub-property of the
numeric one — `DOMAIN_KB` §9 predicts leg (ii) will otherwise be quietly
dropped, and it is the *earlier* signal.

### 5.10 Audit and Inventory

Audit shows the full version tuple on the dossier detail (`AC-F2-07`), the
retained rendered view as an openable exhibit, a period export consumable
without an application login (`AC-F1-09`), and **refusal events as audit
records** (`AC-REFUSAL-04`). The rendered view is framed as the staff
accountant's defence as much as the auditor's evidence — it shows what they
were given, not only what they clicked.

Inventory (`AC-F5-07`) lists agents as named principals with versions,
entitlements and lineage, and **a retired agent's lineage remains enumerable**.
An unanswerable blast-radius question converts a contained error into a
scope-wide material weakness.

### 5.11 Refusals — the contrast is the design

Refused-permanently and deferred appear **on the same screen, adjacent**,
because if a user only ever sees one treatment they cannot learn to tell them
apart.

| | Refused by design | Not in this release |
|---|---|---|
| **Card** | Solid slate border, heavy 6px left rule, filled ground | Dashed amber outline, no fill |
| **Header word** | "Refused — by design, permanently" | "Not in this release" |
| **Closing line** | "This will not be built. It is not on a roadmap and it is not awaiting prioritisation." | "Deferred, not refused. Planned." |
| **Colour** | Slate — deliberately *not* red; a refusal is not an error | Amber, outline only |

The distinction is carried **in the wording alone with all styling stripped**,
so it survives a screen reader and a greyscale print (`AC-REFUSAL-02`,
`AC-REFUSAL-06`). A19–A22 each appear by name with their reason
(`AC-REFUSAL-01`), and the three outright refusals — auto-post below a
threshold, agent-review substituting for human approval, free-form NL-to-SQL —
are listed alongside (`AC-REFUSAL-07`).

---

## 6 · Traceability — every observable-UI criterion has a place in the design

| Screen | Criteria | Where it lives in the mockup |
|---|---|---|
| **Ask** | `AC-F38-14`, `AC-F39-09`, `AC-REFUSAL-03` | §3 coverage meter + declared-population panel + NL input + resolved query; §4 inline A19 refusal |
| **Exceptions** | `AC-F26-10`, `AC-F28-10`, `AC-F29-12`, `AC-F33-12`, `AC-F42-08`, `AC-F41-09`, `AC-F41-10`, `AC-F38-15` | §5 queue with per-type labels, five-check table, backtest panel; §6 zero-pending state |
| **Review** | `AC-F35-09`, `AC-F36-18`, `AC-F40-11`, `AC-F41-01`–`06`, ~~`AC-F41-13`~~ (RETIRED 2026-08-03 — `FUNCTIONAL_SPEC` §28.1; now `AC-F41-22`/`-23`/`-24`) | §7 risk band, in-force panel, six-button resolution row, structured reject; §9 journal lines |
| **Dispositions** | `AC-F32-09`, `AC-F35-07` | §12 open-items table with missed vs within-horizon; zero-open state |
| **Catalogue** | `AC-F38-01`, `AC-F38-12`, `AC-F38-13` | §13 full-attribute table, failed tie-out row, no-certified-datasets state |
| **Monitors** | `AC-F9-08`, ~~`AC-F12-08`~~ (RETIRED 2026-07-31 — `FUNCTIONAL_SPEC` §8/§27.6; now `AC-F12-10`), `AC-F32-10`, `AC-F36-19`, `AC-F41-07` | §14 hit-rate masthead, tiles incl. explicit zero, per-user **override-rate** table, **aggregate-only** probe panel, escalations |
| **Inventory** | `AC-F5-07` | §15 agent table incl. retired agent lineage |
| **Audit** | `AC-F1-09`, `AC-F2-07`, `AC-REFUSAL-04` | §15 dossier detail, export controls, refusal event log |
| **Refusals** | `AC-REFUSAL-01`, `AC-REFUSAL-02` | §16 four A-cards plus the deferred contrast |

Empty, error and boundary states from `FUNCTIONAL_SPEC` §24 that are designed
explicitly rather than left to `code-agent`: 0% coverage, 70% vs 100% pairing,
zero pending items, zero open dispositions, no certified datasets, check not
run, superseded run, failed tie-out, lapsed R1, uncertified dataset in
exploration, ambiguity fork, unanswerable-from-certified-layer.

---

## 7 · What I deliberately did **not** design

Recorded so their absence is a decision and not an oversight.

1. **Any explanation-quality surface.** No confidence bar, no reasoning
   summary hero, no "why the agent thinks this" as a headline. §12's standing
   exclusion is binding and its absence is not a gap.
2. **Any bulk-action affordance anywhere**, including for administrators —
   not a select-all checkbox, not a multi-row toolbar, not a keyboard shortcut
   (`AC-F41-01`, `AC-F12-09`). The component simply does not exist in the
   library.
3. **Any green state.** §3.2.
4. **Any mobile or tablet layout.** §10.4.
5. **A skill-builder / authoring surface.** F16 is deferred (`PLAN` §7.5). I
   have designed nothing that assumes skills are a fixed set — the Ask screen's
   skill resolution is data-driven — so F16 can be added without redesign.
6. **A flux / FP&A analytical surface.** F45 is deferred; FP&A persona coverage
   in MVP1 is F39's NL inquiry only. This is `PLAN` §7.7's open conflict and I
   have carried it forward, not re-decided it.

---

## 8 · Notes for the gates downstream

### 8.1 For `solution-architect` and `code-agent`

- The conclusion component must be **structurally incapable** of emitting
  "clean" / "no exceptions" below 100% coverage — unreachable, not validated
  out (§5.3).
- Nothing on Review may be **hover-only, lazy-loaded or live-refreshing**;
  `AC-F41-04`'s retained rendered view depends on the screen being static and
  self-contained at approval time (§5.4).
- `components/review/` contains **no bulk-approve component by
  construction** (`PLAN` §6.2 already says this; the design does not
  reintroduce it).
- Probe status must not be present in the DOM before disposition in any form
  (§5.6).
- Risk grading is **ordinal with exactly three steps**. Do not add a fourth or
  a numeric score — a five-step scale reintroduces the undifferentiated
  scrutiny problem it exists to solve.

### 8.2 For the UX suite I own at the Test gate

Scenarios I intend to write against `dev/tests/suites/ux/run.sh` once it
exists. **The entry point does not exist yet** — there is no `dev/` directory
in this project as of 2026-07-31 — so none of these has been executed and none
may be reported as passing.

| # | Scenario | Kind |
|---|---|---|
| UX-1 | Contrast ratio ≥ 4.5:1 for all text and ≥ 3:1 for all non-text state indicators, in **both** themes | Accessibility |
| UX-2 | No state is carried by hue alone — every risk/certification state has a non-colour carrier (text, hatch, border style) | Accessibility |
| UX-3 | Semantic structure: one `h1` per screen, correct heading order, tables with real `th` scope, form controls with labels | Accessibility |
| UX-4 | The riskiest element is first in DOM order on Review, outside any collapsed region, and at the largest computed font size on the screen | Flow + `AC-F41-03` (+ proposed §9.1) |
| UX-5 | The agent narrative is collapsed on first render of Review | Flow |
| UX-6 | A 70% run and a 100% run produce non-identical result text on screen | Flow + `AC-F38-07` |
| UX-7 | The string "no exceptions" unqualified is unrenderable below 100% coverage | Flow |
| UX-8 | R2 completes in ≤ the interaction count of R3, measured as real clicks | Flow + `AC-F35-05` |
| UX-9 | A disposition cannot be saved without an expected clearing period, at every permission level | Flow + `AC-F32-01` |
| UX-10 | No bulk-action control is reachable on any screen at any permission level, including by keyboard | Flow + `AC-F41-01` |
| UX-11 | Probe status is absent from the DOM before disposition | Flow |
| UX-12 | Refused and deferred responses differ in text with all CSS disabled | Flow + `AC-REFUSAL-06` |
| UX-13 | End-to-end journey: staff accountant asks → sees coverage → runs partial → opens an exception → records R5 with owner, due date and clearing period → item leaves the queue | Journey |
| UX-14 | End-to-end journey: controller opens Monitors → reads hit rate, override rate incl. an explicit zero, probe results → opens a cross-period escalation | Journey |

Evidence goes to `projects/conclave-finance-studio/test-evidence/` per
`test-agent`'s convention, with screenshots as the evidence field for the
visual checks.

---

## 9 · Open questions for the human and for other gates

### 9.1 `AC-F41-03` — I am not asking for it to be relaxed, I am asking for it to be strengthened

`FUNCTIONAL_SPEC` §25.3 offers to renegotiate the riskiest-element criterion at
this gate if I judge it to trespass on design. **It does not trespass.** Reading
order and non-collapsibility are exactly the right level of specification —
behavioural, testable, silent on pixels. `functional-design-agent` drew that
line correctly.

But they are **insufficient**. An element can be first in the DOM and
uncollapsed and still be visually recessive — which would satisfy the criterion
and defeat its purpose. I would like one more behavioural clause, issued as a
**new ID by `functional-design-agent`** rather than assumed by me:

> *Given a proposal for which the system has ranked one element as the
> riskiest; when the Review screen is rendered; then that element renders at
> the largest type size present on that screen, and no other element on that
> screen renders at an equal or larger size.*

Checkable by comparing computed font sizes. Fixes no number, no colour, no
position beyond what `AC-F41-03` already fixes.

### 9.2 A design intent with no criterion behind it — a routing budget

Volume reduction is the mechanism the research supports, and `AC-F41-09` makes
volume **visible** — but nothing in the 186 criteria makes it **bounded**. I
would like a configured per-reviewer per-night routing budget: when a run would
exceed it, the run says so, and a controller must either raise the cap
(recorded as a control event) or split the queue. That turns volume reduction
from an aspiration into a structural limit, and it is the one mechanism that
would actually prevent a fortieth approval at 11pm rather than merely making it
better-designed.

**I am proposing it, not adding it.** New scope is `plan-agent`'s lane and it
would need a criterion from `functional-design-agent`. If it is not taken, the
11pm problem is *mitigated* by this design but not *bounded* by it, and that
should be a recorded choice rather than an oversight.

### 9.3 Probe reveal timing — `responsible-ai-architect` should weigh in

§5.6. The criteria permit immediate post-disposition reveal and are silent on
it. It has a real cost. I have made the call; it should be reviewed, not
inherited.

### 9.4 Persona coverage carried forward, not re-decided

`PLAN` §7.7's conflict stands: FP&A is served in MVP1 only by F39's NL inquiry,
because F45 is deferred. I have designed the Ask screen to be a genuine FP&A
surface — provenance-stamped, version-stated answers over certified metrics —
but I have not invented a flux surface to close the gap. That is `plan-agent`'s
call.

---

## 10 · Recorded requirements this pass does and does not cover

Per my contract I re-read `PROJECT_CONTEXT.md`'s **full** Decisions Log, not
only the request that triggered this invocation.

### 10.1 Covered

| Recorded decision | How this design honours it |
|---|---|
| Scope correction — not the GL, do not imitate GL | No matching UI, no certification workspace, no statement ingestion, no period-close mechanics. F40 terminates at an export file and says so in the button label. |
| NL, skill-based, datasets selected, action under guardrails | §5.1 in full. NL parameterises a named certified query; the resolution is shown before submit. |
| MVP1 ERP-data-only | Catalogue shows Oracle-sourced datasets only; "non-Oracle data sources" appears on the **deferred** side of the Refusals screen, so the boundary is a stated product property rather than a silent absence. |
| Write-back with per-action approval — "the defining decision" | No bulk affordance anywhere at any permission level; approval attaches to one artefact; the rendered view is retained. |
| Three personas | Staff accountant: Ask, Exceptions, Review, Dispositions. Controller: Monitors, Catalogue, Audit. FP&A: Ask's inquiry leg — **partial, and flagged in §9.4.** |
| A7.2 worst harm delegated to SMEs | The §6.2 self-justifying residual is the worked example on the Review screen and the top row of Exceptions, deliberately: the design's hardest case is the product's worst harm. |
| Refusals A19–A22 as a shipped surface | §5.11, top-level nav. |
| §15.4 anti-recommendation binding on F41 | §2 — the inversion. |
| Standing authorization; make the calls | Calls made, not returned. §9 lists only the four that genuinely are not mine. |

### 10.2 Assumption I made under the standing authorization

**Assumption U1.** I designed the Exceptions screen so that detections *not*
routed to a human (205 of 214 in the mockup) are **listed and reachable rather
than merely counted**. No criterion requires this — `AC-F41-09` requires only
that N and M be visible. I judged that a system which reduces volume without
letting anyone inspect what it suppressed is asking for exactly the trust it
should be earning, and an auditor will ask for the 205 on day one. It is
cheap. If `plan-agent` disagrees it should be cut explicitly.

### 10.3 Assumption I made about the F42/F29 wedge pairing

**Assumption U2.** `AC-F29-08` / `AC-F42-04` require the wedge comparison to be
produced as a **single reportable result**. I have not designed a customer-facing
screen for it, because I read it as a **test-evidence artefact**, not a product
surface — it is the demonstration that the wedge is real, addressed to us and
to an evaluator, not to a staff accountant at close. What the product surface
does carry is the consequence: omission findings and present-anomaly findings
are visually distinct classes on Exceptions (§5.2). If the pairing is meant to
be user-visible, this needs a second pass.

### 10.4 **Not covered — a recorded requirement this design does not satisfy**

`PROJECT_CONTEXT.md`'s header still reads:

> **Surfaces**: desktop web · mobile web · native mobile (**multi-surface**)

while the Decisions Log, `PLAN` §9.2 A2 and `FUNCTIONAL_SPEC` §21 all scope
MVP1 to **one surface, desktop web**, with F23 deferred and F24 (approving from
native mobile) marked **RECOMMEND REJECT** on control grounds.

**I have designed desktop web only.** There is no mobile layout in the mockup
and no responsive breakpoint below tablet in the product design. I am flagging
the header rather than silently satisfying the narrower reading.

If multi-surface is still binding, this gate needs a second pass — and F24 needs
re-deciding first, because mobile is the lowest-scrutiny approval surface that
exists and 11pm on day 3 is exactly when it would be used. Designing a mobile
approval flow before that decision is made would be designing the thing the
plan recommends against.

### 10.5 Tooling note

**`DesignSync` was not available in this runtime invocation**, so no Claude
Design component-library project was created or updated for
`conclave-finance-studio` on this pass. My contract's change history records it
as confirmed present on 2026-07-26; it was not in the tool set I was given
today. The rendered review artefact — which is what approval actually depends
on — exists and is complete. The component library push is outstanding and
should be picked up on the next invocation if the tool returns. Stating it
rather than quietly omitting it.

---
---

# PART A2 — NAVIGATION & JOURNEY REDESIGN (2026-08-02)

**Trigger.** The human opened the running pilot and said *"UI/UX in the link you
gave me is really bad. I just cannot follow anything,"* then asked for a
parallel design thread producing journey maps and an end-to-end navigation
model per use case. This section is that pass. It does **not** supersede Part A:
the visual language, palette, risk grammar, coverage strip, abstention
treatment and narrative behaviour in §§2–3 and §5 all survive intact and are
reused verbatim. What is added is the layer above them.

Rendered prototype: `design-review/redesign-2026-08-02/index.html`.
The gate-5 approved record at `design-review/index.html` is untouched.

## A2.1 · What I found by using the pilot, and what §4 got wrong

§4 of this file claimed an information architecture: nine screens, three groups
(Work / Govern / Evidence). **The build shipped twelve screens in two groups.**
Evidence was dissolved into Govern; `/readiness` and `/my-probe-history` were
added at top level with no design pass. The IA degraded after approval with no
gate watching it. That is the first lesson: **§4 was a paragraph, not a checked
artefact, and a paragraph does not survive contact with 262 acceptance
criteria.**

Three findings from actually walking the running build:

1. **The navigation graph has no edges.** Eight of twelve screens contain zero
   outbound links other than the global nav — `/dispositions`, `/readiness`,
   `/monitors`, `/refusals`, `/catalogue`, `/inventory`, `/my-probe-history`.
   Exactly three screens produce forward motion. Every journey is
   *nav → screen → dead end → nav*. It is worse inside the objects: a finding
   cannot reach the run that produced it, the agent that authored it, or the
   dataset it was computed over — all three render as dead text.

2. **The deeper defect is composition, not location.** `/exceptions` renders
   3,483px tall and stacks seven unrelated analytical modules; the six-row work
   queue is ~250px of it, about 7%. The mechanism: a criterion says "X must be
   visible on screen Y", and the cheapest way to satisfy 262 of those is to
   append X to Y. Each screen became **the union of every criterion that named
   it**. A perfect IA would not fix this, because the problem is inside the page.

3. **The item page is good; everything above it is not.** `/review/ITEM-…` is
   well composed and is Part A working as designed. This is a
   navigation-and-composition problem sitting on a sound design system — which
   makes the fix additive rather than a restyle.

Also recorded: `/review` (the controller's primary surface) is a bare bulleted
list of six hyperlinks with no risk, amount, age, state, sort or filter, behind
a ~300px probe-programme essay; the item page's `<h1>` is **"Not approved"**,
naming a workflow state rather than the object the user clicked; and
`/readiness` is a permanent nav slot hard-bound to a single agent with no
selector, making every other agent's readiness unreachable by any means.

## A2.2 · Design intent — the IA that replaces §4

> **STATUS MARKER (gate 10). This section is a design proposal. It is not a
> description of the shipped pilot, and two of its destinations do not exist.**
>
> Every row below now carries a **Shipped?** cell. Read those before reading
> anything else here: a reader who takes A2.2 for a map of the running build will
> go looking for a **Close** landing screen and a **Period record**, and neither
> string appears anywhere in `dev/`. `PROJECT_CONTEXT.md` briefly recorded
> "Part A2 built"; the orchestrator has corrected that to *partially built*, with
> **J3 and J4 unwalkable in the shipped pilot**. This marker makes the design
> record say the same thing, so the two cannot drift apart again.
>
> This is a status marker, not a redesign. Nothing below is withdrawn: the
> unshipped items remain the proposal, and A2.6 already carries them as
> **severity A — blocks a whole journey**.

**Organising principle: the close period is the object, the queue is the verb,
and everything else is evidence reached from a thing rather than from a menu.**

Primary navigation, four items, task-ordered:

| # | Item | Answers | Shipped? |
|---|---|---|---|
| 1 | **Close** (new) | "Where is this close and what does it need from me tonight?" Default landing, per-persona call-list. Replaces landing on Ask — a doer does not begin the night by writing a query. | **NOT BUILT.** No such route, screen or nav entry in `dev/`. The pilot has no per-persona landing and no close cockpit. A2.6 severity **A** (large). |
| 2 | **My queue** | "What am I working?" Merges the work half of Exceptions with all of Review. | **BUILT**, as `/queue`, under the nav group **Work**. `/exceptions` and `/review` still resolve to it, deliberately, because many criteria name those addresses. |
| 3 | **Approvals** (new) | "What awaits my deliberate act, and what does approving actually do?" | **BUILT**, as `/approvals`, under **Work**. |
| 4 | **Ask** | Detect mode (staff) and Inquire mode (FP&A). | **PARTIALLY BUILT.** `/ask` ships under **Work**; Detect mode only. **Inquire mode and the FP&A persona are not built** — J4 remains net-new scope awaiting a ruling, not a design decision (A2.3, A2.6 severity **A**). |
| — | **Evidence** (section) | Period record · Runs & dossiers · Agents & datasets · What we refuse to do. | **PARTIALLY BUILT.** Runs & dossiers (`/audit`), Agents & datasets (`/inventory`) and What we refuse to do (`/refusals`) ship under **Evidence**. **Period record is NOT BUILT** — no period-parameterised surface exists anywhere, which is exactly why A2.3 records J3 as *Unstartable*. A2.6 severity **A** (large). |

**The two destinations named here that do not exist are `Close` and
`Period record`.** Both were load-bearing to a journey, and both are still
open gaps rather than abandoned intent.

Demotions and dissolutions, with reasons:

| Screen | Becomes | Why | Shipped? |
|---|---|---|---|
| `/dispositions` | Dissolved — a queue filter, a Close row, a Period-record table | Its whole content is one row. A forward prediction is worth something when it *comes back*, so its home is where you stand when it does. | **PARTIALLY.** Off the top level and reachable from the queue and the item that carries it. The Close row and the Period-record table are **not built**, because neither destination exists. |
| `/readiness` | Deleted from nav — a property of an agent | One row of a table that should have many, promoted to a permanent slot. | **BUILT** — off the nav, reached from the agent object. |
| `/inventory`, `/catalogue`, `/monitors` | Under Evidence, plus in-context routes | Nobody navigates *to* an inventory; they arrive from a thing they were looking at. | **DIVERGED.** All three are off the primary task path as intended, but **`/catalogue` and `/monitors` ship under a third group, `Govern`, not under Evidence** — see the grouping note below. `/inventory` ships under Evidence as "Agents & datasets". |
| `/my-probe-history` | Identity menu | Per-person, private by design, empty most of the time. A permanent top-level slot also subtly advertises a surveillance affordance A24 refuses to have. | **BUILT** — identity block below the persona switch. |
| `/refusals` | **Kept in global nav**, under Evidence | §5.11's argument holds: burying a refusal makes it look like an omission. Evidence is not a settings drawer. | **BUILT**, under Evidence, as "What we refuse to do". |
| F26 fidelity, boundary checks, F33, backtest, second held-out period | `/evidence/run/<id>` | Properties of a **run**, not of my night's work. Give the run an object and the queue becomes a queue. | **NOT VERIFIED HERE.** The run object is A2.6 severity **B**; this row's status is `code-agent`'s to confirm, and I am not claiming it either way. |

**The single rule that removes most dead ends:** every object gets one canonical
page; every page names its object in its `<h1>`; every reference to an object is
a link to it. Objects: period, run, finding, dossier, agent, dataset,
resolution, approval.

### A2.2a · Which grouping the build actually has — §4's, not A2.2's

Recorded at gate 10 because pass 17's commit message credits *"the IA from
`UX_KB` A2.2: Work / Govern / Evidence"*, and **Work / Govern / Evidence is
§4's grouping — the one this section's own heading says it replaces.** A2.2
proposes no `Govern` group at all, and assigns Catalogue and Monitors to
Evidence. As the owner of this file, my adjudication:

| | §4 | A2.2 (this section) | **What `chrome.NAV` ships** |
|---|---|---|---|
| Groups | Work / Govern / Evidence | Four flat task-ordered items + an Evidence section. **No Govern group.** | **Work / Govern / Evidence** |
| Work | Ask · Exceptions · Review · Dispositions | — (Close · My queue · Approvals · Ask, flat) | queue · approvals · ask |
| Govern | Monitors · Catalogue · Inventory | — (no such group) | catalogue · monitors |
| Evidence | Audit · Refusals | Period record · Runs & dossiers · Agents & datasets · What we refuse to do | audit · inventory · refusals |

**The shipped container is §4's three-group shape. The shipped contents are
largely A2.2's decisions** — the Exceptions/Review merge into `/queue`, the new
`/approvals`, Ask demoted out of the landing slot, and `/readiness`,
`/my-probe-history` and `/dispositions` taken off the top level. So the honest
description is neither "A2.2 was built" nor "A2.2 was ignored": **A2.2's
demotions and merges shipped inside §4's grouping.** The commit message's
attribution is wrong on the grouping and right on the movements.

**Was the difference deliberate or simply not built?** Both, in separate parts,
and I am not going to blur them:

1. **The `Govern` group is not-built rather than rejected.** A2.2 folds
   Catalogue and Monitors into Evidence on the argument that nobody navigates
   *to* an inventory. The build keeps them as a distinct governance group. I find
   no design record — here, in a commit, or in the Decisions Log — that argues
   against A2.2's fold, so I record this as **A2.2 not carried through, not
   A2.2 overruled**.
2. **The flat four-item nav is not-built, necessarily, because `Close` is not
   built.** A2.2's flat shape is built around Close as the default landing. With
   Close absent there is no flat shape to ship, and grouping the three surviving
   items under a `Work` heading is a reasonable fallback rather than a rejection
   of A2.2. Build Close and the question genuinely reopens.
3. **Keeping Refusals in global nav is deliberate and agreed** — §4, A2.2 and
   the build all say the same thing, and `chrome.NAV`'s comment cites §5.11.

**My position, for whoever rules on it:** the shipped Work / Govern / Evidence
grouping is defensible and I am **not** asking for it to be unwound. The three
governance surfaces really are a different mode of use from the night's work,
and §4 had that right. What I still hold is the *Close-first, task-ordered*
claim — which cannot be evaluated until Close exists. Until then, **§4's
grouping is the accurate description of the product and A2.2's is an
unrealised proposal**, and this file should not be read the other way round.
Neither grouping is human-approved: see the change-history rows, which read
*"approval pending"* and are accurate.

## A2.3 · The four journeys

| # | Persona | Journey | State today |
|---|---|---|---|
| J1 | Staff accountant | Omission detected → investigate → resolve → leaves my queue | Walks, but **dead-ends at the last step**: saving produces no confirmation, no queue removal, no badge change, and the record it creates is linked from nowhere. Six times a night. |
| J2 | Controller | Approve a reclass → it becomes an export | **Unwalkable.** No approvals surface exists. |
| J3 | Controller | Was last period's close clean? | **Unstartable.** No period-parameterised surface anywhere. |
| J4 | FP&A analyst | Why did this account move? | **No surface, no persona button.** Confirmed by `PROJECT_CONTEXT.md` L2507. |

Full before/after step maps are rendered in the prototype's §2.

**J3's design claim, which is the most product-specific thing in this pass:**
the honest answer to "was it clean" is not yes or no. The Period record leads
with *"This is a record of what was examined and what was concluded. It is not a
statement that the period was clean"* and names A20/A21. This renders the
product's central refusal at the exact moment a user asks for the thing it
refuses — which is the strongest possible place for it to appear, and better
than a `/refusals` page nobody visits.

**J4 is net-new scope, flagged not claimed.** Proposed Inquire mode returns the
substantiable half (decomposition to the posting, certified metrics and joins,
population covered) and openly refuses the explanatory half under A22. The
claim worth arguing: an FP&A surface that hands over the decomposition and
refuses the narrative is *more* useful to an analyst defending a variance than
one that manufactures a plausible sentence — and it is the only FP&A surface
that can exist without breaching A19 or A22.

## A2.4 · The six binding constraints — tested, none is the cause

Tested individually against observed behaviour. **No green** (zero
contribution), **narrative collapsed and last** (right, and extended to the
probe essay), **coverage as a population strip** (best component in the
product, promoted to two more screens), **abstention structurally distinct**
(already implemented well, given a first-class count), **desktop-only MVP1**
(honoured) — none causes the unusability.

Two require a recorded note:

- **"No Approve button on the Review screen" was honoured *negatively*.** The
  button was removed; the separate deliberate act it implies must happen
  somewhere was never given a screen, an object or a state. J2 is therefore
  unwalkable. **This is a gap created by honouring a constraint only in its
  subtractive form, and it is the highest-value gap in the product.** The
  constraint is correct and stays.
- **"Guardrails at the broker, never the UI" is not a cause of unusability but
  is a cause of clutter, and I am not asking for it to be relaxed.** Because the
  UI may never disable, ineligible affordances render live and compete visually
  with eligible ones. Proposed change is **ordering, not enforcement**:
  ineligible options move below a rule, keep full contrast, stay clickable and
  submittable, and carry the broker's last-known reason inline. The UI still
  decides nothing.

**What actually causes the visual clutter belongs to no constraint:** the
provenance strip plus pilot strip occupy ~110px identically on all twelve
screens with no delta between visits — 12% of a 900px viewport, forever.
Proposed: one 30px context line always naming the staleness number, full
sentence behind a disclosure. `AC-F38-11` requires staleness on the *same
surface* as the figure, not in the same 110 pixels.

## A2.5 · Typography floor — a call I am making, and a criterion I am asking for

`test-agent` measured navigation at **10px** computed and the provenance strip
at **10.5–11.5px**, the smallest text on every screen. No criterion sets a
minimum, so nothing failed. **I am failing it**, on two grounds:

1. **Audience and hour.** Used at 11pm on close night by finance staff whose age
   distribution skews well above consumer software's.
2. **The inversion is a design contradiction, not a rounding error.** The
   smallest text on every screen is the provenance strip, which carries
   close-clock staleness — the datum that determines whether *any other figure
   on the screen* may be relied upon. The risk number renders at 42px. A product
   whose entire claim is that it does not assert what it cannot substantiate is
   rendering the qualifier at 10.5px and the assertion at 42px. That states the
   opposite of the thesis in the one language a tired reader actually processes.

**Proposed criterion**, for `plan-agent` to rule on and `test-agent` to assert:
no persistently-rendered or interactive text below **12px** computed; primary
navigation items **≥ 14px**; any text carrying a **reliability qualifier**
(staleness, coverage, tier, certification state, abstention, not-run, retention
non-enforcement) **≥ 13px**. Stated as a class, not a selector list, so it
survives new components. Applied throughout the prototype.

## A2.6 · Gaps this redesign needs, by blocking severity

**A — blocks a whole journey:** Approvals screen/object/state (J2, large);
Period record and period parameterisation (J3, large); FP&A inquiry mode and a
third persona (J4, large, **net-new scope requiring a ruling not a design
decision**); post-resolution confirmation + queue removal + undo + next-item
(J1's final step, small — smallest fix on the list, probably the largest felt
improvement).

**B — structural:** a run object; an agent object with readiness as a property;
the Close cockpit; eight missing object-graph edges; queue columns/sort/filter;
item `<h1>` naming the object; context-bar collapse; the typography criterion.

**C — deleted or demoted:** see the table in A2.2. **Nothing that satisfies an
acceptance criterion is deleted** — every module moves to an object that owns
it. Criteria of the form "X must be visible on screen Y" will need Y
re-pointed, which is precisely the point: those criteria built the 3,483px page.

## A2.7 · Visual pass — "Paper & Seal, at close" (2026-08-02, second turn)

Human request: *"make it look slick UI with Apple theme, Conclave Branding and
User experience for journey maps."*

**Brand source of truth: `projects/conclave-marketing/dev/app/static/css/site.css`**,
palette "Paper & Seal", human-approved 2026-07-19. Read directly, not from a
summary — which mattered, see below. Tokens lifted verbatim into
`design-review/redesign-2026-08-02/apple.css`.

**The brand already carries this product's semantics**, which is the finding
that made the pass easy: the marketing CSS defines `--gold` as *human
decisions*, `--rust` as *the honest rejection*, and `--cream` as *artifact
cards*. Those are precisely the meanings this product needs. Each is used for
that and nothing else: gold appears on exactly two things (the Approve control
and a forward prediction a person promised), rust on the severity ramp, cream
on evidence sets and dossiers.

### The green conflict — dropped entirely, and the brand loses nothing

I was told the brand contains `#78c48a` and that the product's no-green rule
wins. Both true, but the record is more specific and the resolution is cleaner
than "substitute it":

**The core Paper & Seal palette contains no green.** The only green in the
marketing CSS is `--c-ship` (`#1E7A46` light / `#6FCF8F` dark), one of six
*team-family accents* colour-coding agent families on the marketing `/who`
page. **It is not a status colour and has never meant "passed" anywhere in the
brand.** So it is dropped outright — there is no green token in `apple.css` in
either theme, and nothing needed recolouring to replace it, because it carried
no meaning this product uses. Verified by grep across the whole visual layer:
the only occurrence of the word is the comment recording its absence. The
conflict was an artefact of the summary, not of the brand.

### Apple *pro-app*, not Apple marketing page

The stated risk — a naive consumer treatment producing a beautiful page that
holds six rows — is real for this content, which is dense, evidential and
numeric. Reference points taken were Numbers, Xcode inspectors and Finder list
view. What that meant concretely:

- **Four colour families, one meaning each.** Rust = something is wrong (one
  hue, three weights); gold = a human decision; teal = navigation and action;
  slate = could not establish / refuse. Slate is the only cool hue in a warm
  palette, so "unknown" is structurally other before it is read.
- **Hairlines, not boxes** — `--hairline` is brand-reserved for rules that
  never carry text. Cards only where a real container exists.
- **A seven-size type scale** (12·13·15·17·21·28·40) against the pilot's
  eleven-plus, and one 28px alignment grid.
- **Density that reads as calm**: 14px row padding, hairline separation, 3px
  severity rail. Six rows fit above the fold; forty would still scan.
- **The serif has one job** — Georgia carries the product's own voice, on
  refusals and abstentions only, because "this is not a statement that the
  close is clean" is the system speaking about its own limits and that is a
  different register from a data label.
- **Light-on-warm-paper is the primary treatment**, not a light-theme
  afterthought.

### The typography ruling, built rather than proposed

| Element | Pilot | Now |
|---|---|---|
| **Close-clock staleness value** | **10.5px — smallest text on every screen** | **15px semibold, rust** |
| All reliability qualifiers | 10.5–11.5px | 15px |
| Primary navigation | 10px computed | 15px |
| Micro-labels / table headers | 10–10.5px | 12px (the floor) |
| The risk figure | 42px | 40px |
| **Qualifier-to-assertion ratio** | **4.0×** | **2.7×** |

The ratio is the substance. A product whose claim is that it does not assert
what it cannot substantiate cannot render the assertion four times the size of
the substantiation.

### Journey maps as designed artefacts

`v2-journeys.html` — four maps on the brand's cream artifact ground, each with
persona initial, role, the question in brand serif, trigger/stakes/frequency,
a verdict pill, and two lanes (today / proposed) of connected step cards.
Steps are clickable and navigate into the prototype. Dead ends render in the
severity ramp; proposed steps in dashed teal.

### Scope of the visual pass — stated, not glossed

**Four screens carry the treatment** (`v2-close`, `v2-queue`, `v2-item`,
`v2-approvals`) plus the journey maps. The other fifteen prototype screens
remain on the first-pass stylesheet and should be read for structure, not
finish. **Contrast is designed, not measured** — every brand pair used was
already verified computationally at AA by the marketing site, but my two
additions (the rust severity ramp, the slate family) have not been run through
a checker. That is the UX suite's job at the Test gate and is not claimed here.
No motion. Desktop only.

## A2.8 · Identity carried forward — logo, hero, motifs (2026-08-03)

Human request: *"please make sure we have conclave branding and design
language from the Conclave-marketing project carried forward. Logos, heros
etc."* A2.7 carried the brand's **tokens**; this carries its **identity**.
Delivered as `brand.css` (a layer over `apple.css`) plus `brand-assets.html`
(the asset sheet `code-agent` copies from).

### The logo is a wordmark plus the Council Mark

Source: `templates/base.html`, `templates/index.html`, `templates/how.html`,
`static/css/site.css`. There is **no SVG logotype** — the wordmark is a type
treatment (`.wordmark`: 17px / 700 / `.02em` / ink), carried verbatim.

The **Council Mark** is six teal threads converging on a neutral core with a
single gold pull-line above: the six SDLC disciplines, the Conclave core, and
the human. It carries one hard colour law, quoted from `site.css`: **"GOLD IS
USED ONLY FOR THE PULL-LINE + ITS TERMINUS DOT — never the core, never the
threads."**

**A2.7 broke that law** — it invented a gold filled disc as an app icon.
Corrected: the real geometry, core in `--neutral-core` (the one token
`apple.css` had not carried).

Marketing defines three tiers. Product usage:

| Tier | Marketing use | Product use |
|---|---|---|
| 1 (full labelled) | `/who` lead-in | **Not used** |
| 2 (440px hero glyph) | home hero | **Left behind** — illegible small, pure cost large |
| 3 (`.sig3`, 34px signature) | human-decision beats on `/how`, `/what` | **Carried verbatim** — the Approve control and recorded decisions |
| 4 (28px lockup) | — | **NEW, but a reduction**: three threads + core for sidebar chrome |

**Tier 3 transfers with zero reinterpretation**, which is the find of this
pass: marketing already pairs it with `.sealrow`/`.seal` — gold seal
"Approved", **rust seal "Sent back"** — and this product records exactly those
acts. Both variants already existed. I added one: **dashed slate, "Not
concluded"** — the state marketing has no beat for, because the system
abstained and no human decision was ever offered. Dashed because it is the
absence of a decision, not a decision.

### The hero: carried as rhythm, not as height

Marketing opens a page with serif headline (one phrase gold-underlined) → lede
→ stat strip → CTA → Council Mark: ~520px before content. **Carried**: the
order, the stat strip, `.goldline`, the closing hairline. **Dropped**: the
full-bleed height, the Tier-2 glyph, the `.cta` button — the call-list *is*
this product's call to action. Result ~150px.

**The opening is graded by visit frequency** — the density adaptation as a
rule:

| Screen | Visits per night | Opening |
|---|---|---|
| Close | once | Full: icon, serif headline, answer, 4-stat strip |
| Approvals | a few | Full, 3-stat strip |
| Finding | six | Icon, **sans** title, one answer line |
| Queue | after every item | Shortest: icon, title, one line, rule |

`.stat-strip` was the most directly reusable marketing component — already the
right shape for "6 routed / 1 abstention / 70% coverage". Two adaptations:
figures **mono not serif** (ledger quantities must align in a column), and a
figure may take a severity colour so **70%** reads as the partial-coverage
warning it is rather than an achievement in teal.

### The serif: deliberately narrower, and it is the same rule

Marketing uses Georgia for almost everything with a voice (`h1.q`/`h2.q` — the
site is built as questions — home headline, panel headings, pull-quotes, stat
figures, all of `.artifact`). The product uses far less. **The rule is not
"headings are serif"; it is: the serif carries Conclave's voice, the sans
carries the evidence.** On marketing nearly everything is voice; in this
product nearly everything is evidence, so the identical rule yields a much
smaller footprint.

Two A2.7 errors corrected:
- **The artifact card.** Marketing's `.artifact` is serif on cream; mine was
  sans on cream. Now the kind label and the statement are serif, the table
  inside stays sans/mono — serif tabular figures do not align in a column.
- **Page-opening headlines.** Close and Approvals now open in Georgia because
  they are the product speaking. The finding screen deliberately stays sans:
  "18300 Deferred Storm Restoration Costs" is a ledger account, not a voice.
  That contrast is the rule made visible and is worth preserving.

### Section icons: carried verbatim, mapped 1:1, no new glyph drawn

`si-seal` → approvals · `si-record` → dossier/period record · `si-gate` →
boundary checks/guardrails · `si-flask` → run report/backtest · `si-door` →
refusals · `si-build` → agents/datasets.

### Left behind, on purpose

`#conclaveNet` (the site-wide ambient drifting-node canvas) — a continuously
animating background behind a queue scanned at 11pm is the clearest case of a
marketing treatment that would actively hurt the work. `motion.css` draw-in —
noise on a screen visited forty times a night. `.cta` button. The six `/who`
family accents including `--c-ship`. **Nothing ported depends on any green**;
verified by grep — the only occurrences of the word across the visual layer are
the comments recording its absence.

### What cannot come across at all

**The question-and-answer spine.** Marketing is a chain of questions —
`h1.q`, `.answer`, a `chain-nav` walking Why → What → How → Who. It is a
rhetorical structure and the best thing about that site. A close queue has no
rhetoric, only a task order. The **tone** transfers — plain, unhedged, willing
to state what it will not do, which is why the refusal blocks read as they do.
The **structure** cannot. Also capped: `.goldline` marks one phrase per page on
marketing; in a product with forty findings a night it would become decoration
within a week, so it is limited to one per page-opening and unavailable in
lists.

### Build-safety

`brand.css` is a layer, not a restructure: loads after `apple.css`, adds one
token, and every selector is new. It changes no layout rule `code-agent`'s
pass-17 work touches (IA, eight graph edges, Approvals, composition split,
typography floors). Applying it is four mechanical steps: link the stylesheet,
paste the glyph `<defs>` once into the base template, swap the sidebar block
for `.lockup`, wrap each page head in `.opening`.

## A2.9 · Not covered by this pass, stated rather than omitted

- **`DesignSync` is still unavailable in the runtime** — same finding as §10.5
  at gate 5, re-confirmed 2026-08-02: it is not in this agent's tool grant and
  there is no MCP configuration providing it. **No component-library push
  happened.** The deliverable is rendered HTML on disk instead, which satisfies
  the standing "a rendered artefact, never a text summary" rule but does *not*
  satisfy the contract's DesignSync obligation. Flagged for the orchestrator.
- **Mobile and native surfaces** — out of scope per desktop-only MVP1, as at
  gate 5. Nothing in this IA forecloses a later mobile pass; the four-item
  primary nav is materially easier to carry to a small surface than eleven.
- **Dark theme** — the prototype renders light only. The dark tokens are
  untouched and the new components use the same variables, so dark is expected
  to work, but it is **not verified** in this pass.
- **No accessibility execution.** This is a design pass, not a Test-gate pass;
  the typography call is a design judgement, not a suite result.

---
---

# PART A3 — THE CLOSE COCKPIT, AND EVERY DESTINATION IN A DRAWER (2026-08-08)

**Trigger.** The human, having used the running pilot: *"based on the user who logs there
should be a simple home page. showing close tracker. Showing KPIs based action items for
that user. move all the menu items to a hamburger menu."*

Rendered prototype: `design-review/close-cockpit-2026-08-08/index.html`. Both earlier
artefacts — `design-review/index.html` (gate-5 record) and `redesign-2026-08-02/` — are
untouched. `apple.css` and `brand.css` are reused by reference; `cockpit.css` is an additive
layer adding two components and no token.

## A3.1 · This is A2.2's Close cockpit, built — with one thing changed

A2.2 row 1 already specified this screen: **Close**, the default landing, *"where is this
close and what does it need from me tonight?"*, a per-persona call-list, replacing landing on
Ask. A2.3 records **J3 as Unstartable** without it and A2.6 carries it under **A — blocks a
whole journey**. The human has arrived independently at the screen already specified. That
design stands and is reused; this section does not restart it.

**What has moved since, and why.** A2.2 assumed the cockpit sat *beside* a persistent
four-item nav. The human has now removed that nav. So the call-list is no longer a courtesy
on top of navigation — **it is the navigation for the night's work**. Two consequences,
both designed against rather than inherited:

1. **Every row points at a specific object, never at a section.** A2.2's rows could afford to
   say "go to the queue" because the queue was one click away regardless. They cannot now.
2. **A2.2's own "flat four-item nav" question is closed, not reopened.** A2.2a said building
   Close would reopen it. It does not: with all destinations in a drawer there is no primary
   nav to be flat or grouped, and the drawer carries **A2.2a's shipped Work / Govern /
   Evidence grouping unchanged**, plus a *This close* entry and a *You* group.

## A3.2 · The hamburger: what the decision costs, and the one cost I cannot absorb

The human was offered keeping Queue and Approvals persistent and chose everything in the
drawer. That is their call and it stands. The accounting, on the record:

| Cost | Answer |
|---|---|
| **Nav badges go dark.** §4 made them the volume control expressed in the chrome. | **Fully answered.** Every badge's number is on the home page, larger, with a destination and a qualifier. While standing on home, chrome badges were always redundant. |
| **Refusals loses its standing rebuke.** §5.11 keeps it in global nav so a refusal does not read as an omission. | **Answered by content, not position.** The refusal block is on all three home pages, in the serif voice, at the moment the user is most likely to want the thing it refuses — a *stronger* placement than a nav row nobody clicked. |
| **The return path lengthens.** Six items a night × (open drawer → find queue → click), paid at the moment attention is already spent. | **Partly answered, and this is the live risk — A3.3.** |

The return path is answered by **one non-hamburger control in the top bar**: *"Close — 2026-06
· 4 left"* — one control, to one screen, carrying the one badge that matters mid-flow. **This
is not navigation smuggled back in**, and the distinction is worth stating precisely because
it would be easy to erode: it addresses exactly one destination, the screen the human asked
to carry the work. A second such control is a sidebar with extra steps and should be refused.

The drawer buys one thing and I have spent it: **a drawer is entered deliberately, so it can
afford a 13px descriptor per row** saying what each destination answers. A 15px sidebar row
could not.

## A3.3 · The one problem I cannot design around, stated as a condition

**The return path only works if the post-resolution step exists, and it does not.** A2.6
already lists it as an open severity-A gap: J1's final step produces no confirmation, no
queue removal, no badge change, no next-item. With a persistent sidebar that was an
irritation. **With everything in a drawer it becomes the dominant interaction of the night**:
save an item, land nowhere, open the drawer, find the queue, and count which rows you have
already done because nothing removed them.

So: **designable around, conditional on one build item.** After a resolution is recorded the
product must land the user on the next routed item, or back on the cockpit with the count
decremented. This was A2.6's *smallest* listed fix; the hamburger decision makes it
**load-bearing**. My recommendation is not that the decision be reversed — it is that this
item ships *with* the drawer rather than after it. Shipping the drawer over a dead end would
cost more than the clutter it removes.

## A3.4 · The close tracker — drawn from the declared calendar, and its four states

Drawn from `common/close_calendar.py`'s declared calendar `close.pilot_2026_06@1`: **five**
checkpoints at 08:00 UTC on close days 1–5, refresh due by the day-2 cut-off, and
`AC-F26-05`/`AC-F38-11`'s arithmetic against them. Nothing invented.

**Correction to A2.7's prototype:** `v2-close.html` renders *"day 3 of 8"*. The declared
calendar has five checkpoints, so the honest figure is **day 3 of 5**. A tracker that
disagrees with the calendar it is computed from is worse than no tracker.

**The graphic is the gap, not the progress.** A passed checkpoint is **filled neutral ink,
never green** — a cut-off that has gone by is a fact, not an achievement, and "fine, move on"
is precisely the affect §3.2 exists to withhold. What renders in severity colour is the
**bracket** between the checkpoint the refresh was *due* by and the one it *landed* in; the
15px semibold rust staleness sentence is that bracket's label, not a second assertion beside
it. This is the coverage strip's rhetorical move applied to time.

Four states, and the fourth is what makes it honest:

| State | Rendering |
|---|---|
| On calendar, N days behind | Five stops, bracket drawn, staleness sentence as its label |
| Refreshed after the last checkpoint | Marker past day 5; *"arrived after the books closed"* — a different fact from "just in time for day 5", never folded into it |
| **No refresh observed** | Tracker still drawn (position comes from the calendar, not the data); the marker is **absent** and an abstention block says so. Not "zero close days behind" — zero is an answer |
| **No calendar declared** | The tracker is **absent, not empty**, in serif voice, naming `AC-F38-11` unmet and register 6. Five grey stops would look like a close that had not started — a claim nobody made |

## A3.5 · KPIs as action items — the rule, made structural

The rule: a figure earns a place on a home page only if it has **(a)** a number, **(b)** a
reliability qualifier at **≥13px**, and **(c)** a destination that is a **specific object**,
not a section.

**Enforced by the component, not by editorial discipline.** `.act` is an `<a>` and has no
variant without a `.q` qualifier: a tile with no destination and a tile with no qualifier are
inexpressible. Same move §5.3 makes for the conclusion string — unreachable, not validated
out. A2.1's lesson is that a paragraph does not survive contact with 262 criteria.

**The floor changed a design decision, which is the evidence it is doing work.** Coverage was
going into the stat strip, whose labels sit at the 12px micro-label floor. A coverage
percentage is a reliability qualifier, so it could not live under a 12px label; it moved to
its own tile with a 13px qualifier and the population strip beneath it.

### What each persona sees, and why

**Staff accountant (A. Reyes).** Six items routed, rendered as **"five findings and one the
system could not settle"** — the queue badge is 6 and the page must never call 6 "findings",
which would convert an abstention into a finding in the one place a tired reader takes the
number at face value. The severity ramp draws the five, then a gap, then the dashed
abstention swatch outside it. Then: the abstention's own row; a forward prediction come due
(gold); three accounts nothing has scanned; one boundary check that could not run. The
**routing cap is a qualifier, not a tile** — 6 against a cap of 12 does not bind, so it
implies no act tonight.

**Controller (D. Okafor).** One proposal awaiting the act only they can complete; two
cross-period escalations split by leg with the narrative-only leg as a first-class row; one
abstention **not yet assessed** (counts, never a rate); **an agent acting tonight that is not
ready**; **zero routing caps raised**, with its denominator; one forward prediction missed on
the team. Plus a panel naming the four real figures deliberately *not* here.

> **The row I would defend hardest, because nobody would have specified it.** The pilot's
> `readiness_report` for `crossperiod-surveillance` has **P2 unmet — "one F32 forward
> disposition missed in 2026-05 and not yet explained"**. That is **the same miss** on the
> staff accountant's page tonight. The two personas' cockpits are looking at one fact from
> two ends, and there was no surface in the product on which that was visible. It is
> computed, real, and it is the argument that per-persona composition is worth more than a
> shared dashboard filtered by role.

**FP&A analyst.** The honest one, and it required refusing the obvious page. **There is no
FP&A persona in the build** — `state.PERSONAS` carries two — and nothing in this product
routes to one. So the temptation was to fill the page with coverage, detections and dwell:
figures that are real and imply no act. Instead the **abstention grammar is applied to a whole
persona**: *"Nothing is routed to you, and that is a fact about this product, not about this
close."* Then the three things genuinely obtainable from the period today — the 7 accounts
with a quotable decomposition (stamped with certified query, version and dataset version,
which is what makes it defensible in a variance meeting), the 3 accounts nothing has scanned
(the figure most worth knowing *before* the meeting), and the 1 abstention. Then **refused
(A22, solid slate, filled) and deferred (Inquire mode, dashed outline, no fill) side by
side**, because a user who only ever sees one treatment cannot learn to tell them apart.

### What was refused a place, and why

| Fact | Why not | Where it belongs |
|---|---|---|
| Override rate per agent / per user | A high rate could mean a reviewer is catching things or an agent is misfiring. It does not name the act, and colouring it would assert an interpretation the data does not support | Monitors |
| Median dwell time | Same, and a per-person figure at glance-read cadence on a management-chain surface is the wrong pressure | Monitors |
| Forward-disposition hit rate (64%, 27 of 42) | It is the product marking its own homework and is the Monitors **masthead** by design. Demoting it to a home tile among action items makes it look like one more number about *you* rather than the one about *us* | Monitors masthead |
| Probe aggregates | Aggregate-only by G-PROBE-3, no act implied tonight, and a home-page probe figure is one hop from a per-person one | Monitors, aggregate only |
| Total detections (214) as a tile | A number with no destination is the definition of the vanity metric this pass exists to keep out. It survives only as the qualifier that makes 6 legible as a *reduction* | Qualifier on the queue tile |

## A3.6 · A build consequence that only appears once counts share a page

**Queue counts include probes; coverage figures exclude them — and they must not be made to
agree.** The build is already right: `state.conclusion` excludes probes from the coverage
population under `AC-F12-16` (a coverage statement is a claim about the customer's ledger; a
probe is one we manufactured), while `nav_badges["queue"]` counts every admitted item because
a probe must be indistinguishable. Putting both on one page for the first time creates the
opportunity to "tidy" them into consistency. A "5 findings" figure computed by subtracting the
probe would make the probe **detectable by arithmetic** — the one thing `AC-F41-08` forbids.
Recorded here because it is invisible until a home page exists.

## A3.7 · Gaps, and two criteria I am asking for

**Blocking:** the post-resolution landing (A3.3) — `code-agent`, already on A2.6's list,
now load-bearing.

**Open:** an FP&A persona in `state.PERSONAS` (`plan-agent`, net-new scope);
per-user forward-disposition hit rate — `disposition_store.hit_rate()` is period-wide and the
staff tile quotes "31 of 38 met", which is **dropped rather than faked** if it is not
computable (`code-agent` to confirm); the Period record (A2.6 severity A, still unbuilt, so
J3 stays unstartable); a route and screen id for this page — suggested `/close` with `/`
re-pointed to it from `/queue`, which is an IA change several criteria's screen references
need re-checking against (`solution-architect`).

**Two criteria requested from `functional-design-agent`:**

1. A2.5's typography floor as an actual criterion. It is still a design ruling. This pass
   makes it structural in one component; nothing stops the next component omitting it.
2. *Given a figure rendered on the close cockpit; then it is inside an element that is a link
   to a specific object, and it carries a qualifier rendered at ≥13px.* Checkable from the
   DOM. Without it, "action items only" is a paragraph — and A2.1 records what happens to
   those.

## A3.8 · Not covered by this pass, stated rather than omitted

- **`DesignSync` is still not in this agent's tool grant** — re-confirmed 2026-08-08, the
  third consecutive pass (§10.5, A2.9). **No component-library push happened.** A Figma MCP
  server is present in this runtime but is not part of this agent's grant and no Figma file
  was created; rendered HTML is the deliverable.
- **No accessibility execution.** Contrast is designed, not measured. Two new pairings — the
  neutral-ink checkpoint dot on surface, and the dashed slate abstention-tile border — have
  not been through a checker. `dev/tests/suites/ux/run.sh` now exists, so this is executable
  at the Test gate and must be executed rather than statically reviewed.
- **Desktop only**, as at gate 5. `PROJECT_CONTEXT.md`'s header still reads *multi-surface*
  while every ruling scopes MVP1 to desktop web; flagged again rather than silently
  satisfying the narrower reading.
- **Two illustrative figures are unconfirmed** and are named as such rather than presented as
  established: the per-user hit rate, and the escalation split as 1 numeric + 1
  narrative-only.

---
---

# PART B — OBSERVED POST-DEPLOY BEHAVIOUR

**Status: empty. This project has not been built or deployed.**

Recorded as explicitly empty rather than omitted, because an absent section
reads as "we did not look" and this file is meant to be a living record of how
the design actually performed, not only what was intended.

## B.1 What to watch in the first production close

Written now, while the reasoning is fresh, so the first period of real usage is
measured rather than merely survived. Each item names the design decision it
would falsify.

| # | Watch | Falsifies |
|---|---|---|
| **W1** | **Horizon drift** in forward dispositions — do predicted clearing periods bunch at the far end of the permitted range over time? | §5.7's decision to show the user their own hit rate |
| **W2** | **Narrative expansion rate** — if it converges toward 0% or 100% across all reviewers, the collapsed-by-default decision has stopped producing a signal | §2's core argument |
| **W3** | **N/M ratio trend across periods** — does routed volume grow as the catalogue grows? | The whole volume-reduction thesis |
| **W4** | **Dwell time at item 20+ versus item 1–5** within a session — does the risk grading actually hold attention late, or does dwell collapse uniformly? | §1.2's "effort scales with risk" |
| **W5** | **Probe catch rate before vs after a reviewer has seen ~10 probes** — does immediate reveal train calibration, or does it teach the probe rate? | §5.6's judgement call |
| **W6** | **R2/R5 share of dispositions** — if postings (R3/R4) dominate, the equal-weight resolution row failed to counteract the pull toward posting | §5.4's interaction-count argument |
| **W7** | **Partial-run frequency** — how often do users run below 100% coverage, and do they add the missing datasets when prompted or proceed anyway? | §5.1's declared-population inversion |
| **W8** | **Refusal comprehension** — do users re-ask a refused capability in a later period? Re-asking suggests "refused" is being read as "not yet" | §5.11's two-vocabulary design |

## B.2 Observation log

_(no entries — no production usage)_

| Date | Period observed | What was observed | Design decision affected | Action taken |
|---|---|---|---|---|
| _(none)_ | | | | |

---

## Change history

| Date | Version | Change | Approving decision |
|---|---|---|---|
| 2026-08-08 | 1.4.0 | MINOR — **Part A3, the close cockpit and the hamburger.** Builds A2.2's unbuilt **Close** row rather than restarting it, and records the one thing that changed since: with the persistent nav removed the call-list *is* the navigation, so every row points at a specific object. Adds the close tracker drawn from the declared calendar (`close.pilot_2026_06@1`, five checkpoints) in **four** states including the two absences, and corrects A2.7's "day 3 of 8" to **day 3 of 5**. Adds the KPI rule — number + ≥13px qualifier + object destination — enforced by the component rather than editorially, and records which computed facts were refused a place and why. Per-persona content for staff, controller and FP&A, the last of which applies abstention grammar to a whole persona because no FP&A persona exists in the build. Records **one cost of the hamburger decision that cannot be absorbed** (A3.3, post-resolution landing) as a condition on shipping it, and one build hazard (A3.6, probe counts vs coverage counts must not be reconciled). Rendered prototype at `design-review/close-cockpit-2026-08-08/index.html`; gate-5 record and `redesign-2026-08-02/` untouched. `DesignSync` unavailable for the third consecutive pass — no library push. | Human request, 2026-08-08; approval pending |
| 2026-08-05 | 1.3.1 | PATCH — **gate-10 record correction, no design change.** E2: `AC-F12-08` was cited live in three places (§1.2 mechanisms table, §5.9, §6 traceability) though retired 2026-07-31 and replaced by `AC-F12-10`; corrected, with a §5.9 editorial marker that **preserves rather than deletes** the original per-user probe-column intent and records `RESPONSIBLE_AI_KB` G-PROBE-3 / gate-6 ruling 4 as a correct override of it. The per-user *probe* figure is removed from the design record; per-user *override rate* is untouched. The build was already aggregate-only — this was a documentation defect, not a product one. E3: A2.2 gains a status marker and a **Shipped?** column per row, naming **Close** and **Period record** as NOT BUILT; new **A2.2a** reconciles the grouping — what shipped is **§4's** Work/Govern/Evidence, not A2.2's flat four, with A2.2's demotions and merges inside it — and §4 gains a matching marker. Nothing in `dev/`, `design-review/`, `FUNCTIONAL_SPEC.md` or `PROJECT_CONTEXT.md` touched. **The Part A2 approval-pending rows below are unchanged and remain accurate.** | `review-agent` gate-10 escalations E2/E3, adjudicated by this file's owner; no new human approval sought or implied |
| 2026-08-03 | 1.3.0 | MINOR — **A2.8, identity carried forward.** Logo (wordmark + Council Mark, incl. the Tier-3 signature and seal row reused for their original meaning), page-opening pattern graded by visit frequency, six section icons mapped 1:1, artifact card, gold underline. Corrects two A2.7 errors: the invented gold-disc app icon broke the Council Mark's own colour law, and the artifact card was sans where marketing is serif. New `brand.css` + `brand-assets.html`; applied to the four branded screens. Records what was left behind (`#conclaveNet`, `motion.css`, Tier-2 glyph, `.cta`, all six `/who` accents incl. the green) and what cannot come across (the question-and-answer spine). | Human request, 2026-08-03; approval pending |
| 2026-08-02 | 1.2.0 | MINOR — **A2.7, visual pass "Paper & Seal, at close".** Conclave brand (read from `conclave-marketing/dev/.../site.css`, not a summary) + Apple pro-app discipline, in a new `apple.css`. Records that the **brand's green is not a status colour** — it is one of six team-family accents on the marketing `/who` page — and is therefore **dropped entirely rather than substituted**, with the no-green rule intact. Applies the typography ruling as built fact: staleness 10.5px → 15px, nav 10px → 15px, qualifier-to-assertion ratio 4.0× → 2.7×. Journey maps redrawn as designed artefacts. Four screens restyled, fifteen not — disclosed. | Human request, 2026-08-02; approval pending |
| 2026-08-02 | 1.1.0 | MINOR — **Part A2, navigation & journey redesign.** Parallel design thread requested by the human after using the running pilot. Adds: four end-to-end journey maps (J1–J4, two of them currently unwalkable and one unstartable); a four-item task-ordered IA replacing §4's eleven-item flat nav, with demotions for `/readiness`, `/inventory`, `/catalogue`, `/monitors`, `/my-probe-history` and dissolution of `/dispositions`; a verdict that none of the six binding constraints causes the unusability, with the "no Approve button" constraint's unbuilt positive half identified as the highest-value gap; a **FAIL** call on the 10px navigation / 10.5px provenance typography with a proposed floor criterion; and a gap list. §4 is superseded by A2.2 but retained for the record. Rendered clickable prototype at `design-review/redesign-2026-08-02/index.html`; gate-5 record untouched. `DesignSync` re-confirmed unavailable — no library push. | Human request, 2026-08-02; approval pending |
| 2026-07-31 | 1.0.0 | Initial Experience Design pass. Visual language, IA and nine screens designed against all 186 acceptance criteria; rendered mockup at `design-review/index.html`. Four items escalated (§9), two assumptions recorded (§10.2, §10.3), one recorded requirement flagged as **not covered** (§10.4, multi-surface header vs desktop-only MVP1), one tooling gap recorded (§10.5, `DesignSync` unavailable). | Standing authorization to build MVP1, `PROJECT_CONTEXT.md` Decisions Log 2026-07-31; gate 5 human review pending |
