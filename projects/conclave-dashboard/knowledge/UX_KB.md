# UX Knowledge Base — `conclave-dashboard`

Owner: `ui-ux-designer` · Gate 5 · Experience Design
Created 2026-07-29 · **Status: proposed, awaiting human approval**

Inputs read: `projects/conclave-dashboard/INTAKE.md` (incl. addendum R1–R6),
`admin/PIPELINE.md` (§1–§4), `admin/PORTFOLIO_STATUS.md`,
`projects/little-milestones/PIPELINE_LOG.md`, `admin/kb-server/DESIGN_SPEC.md`,
`admin/kb-server/templates/index.html`.

> **Note on gate order.** This project has no `PROJECT_CONTEXT.md`, no
> `PLAN.md` and no `FEATURES.md` on disk yet; `PIPELINE_LOG.md` records the run
> as sitting at gate 2. Experience Design has therefore been invoked **ahead of
> gates 3 and 4**, so this document designs against the *intake requirements*
> (A1–A10 + R1–R6) rather than against an approved backlog. That is a deviation
> worth recording, not absorbing silently: the acceptance criteria this design
> should have been handed at gate 4 do not exist, so every "AC" reference below
> is a design intent I am proposing, not one I was given. If gate 3/4 later
> change scope, this section is the loop-back target.

---

## 1. What this thing actually is

Not a dashboard in the analytics sense. It is a **status report that redraws
itself** — the artefact a delivery lead reads before a steering meeting,
rendered from state instead of typed. Everything downstream follows from that
sentence:

- It is read in **seconds, not minutes**. Scanning, not reading (A3.2).
- It is read **cold**, between sessions, with no memory of what was true
  yesterday. So it must say when it last knew anything.
- Its most dangerous failure is not being ugly or slow. It is **being wrong and
  believed** (A7.2). Every design decision below is downstream of that.

### The one-line design principle

> **A status surface earns its authority by being visibly honest about the
> limits of what it knows.** Anything it cannot currently establish must render
> as a *state*, never as an absence, and never as green.

---

## 2. The central problem: RAG vs. the real state space

The brief asks me to reconcile "scannable in one second" with "never lies by
omission." Here is my answer, argued.

### 2.1 The state space we actually have

| Axis | States |
|---|---|
| Gate | `done` `active` `looped` `warn` `pending` `skipped` |
| Approval | `hdone` `hwait` `hpend` `hskip` `hnone` |
| Reason a gate is `⊘` | `not_applicable` · `gate_did_not_exist` · `skipped_without_exception` |
| Runtime | (proposed, §5) `up` `degraded` `down` `unreachable` `never_deployed` `unknown` `stale` |

That is not three things. Any mapping onto three colours is lossy, and this
platform has already paid for exactly that loss: `⊘ not applicable` and
`⊘ skipped without exception` rendered identically for weeks, which is how
little-milestones' Review gate stayed invisible.

**And it is still happening, right now, in `admin/PORTFOLIO_STATUS.md`.** Every
one of the five projects renders `G4["⊘ 4 Functional"] --> H4{"✋ n/a"}`. But
the prose above the graphs says those gates *did not exist yet* — a coverage
gap the file itself calls "a real coverage gap, not a formatting artefact."
Meanwhile `load-alert-agent`'s `G5` renders **identically** and is genuinely
not-applicable-by-template. Two different facts, one glyph, one label, today,
in the source of truth. This dashboard's first job is to stop rendering them
the same.

### 2.2 Why I am not rejecting RAG

RAG earns its place for one reason only: it answers a question the full state
space cannot answer quickly — **"is there anything here I need to do something
about?"** That question is not derivable at a glance from eleven glyphs. RAG is
a good *index*. It is a terrible *record*.

### 2.3 The resolution — two layers, one derivation rule

**RAG is an index into the facts, never a summary that replaces them.**

- **Layer 1 · Attention.** One chip per project (and one per KPI tile). Its job
  is triage and nothing else.
- **Layer 2 · Fact.** Every gate, approval and runtime probe keeps its own
  glyph, label and class exactly as `admin/PIPELINE.md` §3 defines it. Layer 1
  never overwrites, recolours or hides Layer 2.

Four binding rules make this safe:

**Rule 1 — RAG has four states here, not three.** The fourth is
**`? UNKNOWN` (slate)**. Classic RAG's fatal flaw for us is that it has no way
to say *I could not establish this*, so absence of evidence silently becomes
green. Unknown is a first-class, visually distinct, non-green state. This is the
direct mechanical answer to A7.2.

**Rule 2 — a chip must be able to enumerate its reasons, or it degrades.** Every
non-green chip carries the count of the facts that produced it
(`AMBER · 3 findings`) and those facts are reachable in the same visual unit —
one disclosure, no navigation. **A chip that cannot enumerate its reasons
renders `? UNKNOWN`, never green.** Green is only ever emitted by a positive
assertion over a complete fact set; it is never a default and never a fallback.

**Rule 3 — colour is the second channel, never the first.** Every state carries
a glyph and a word. Colour only ever intensifies a distinction that is already
legible in monochrome. Test: print the page greyscale — no fact may be lost.
This is also the accessibility position (§7).

**Rule 4 — the amber/red derivation is published on the page.** A rule the
reader cannot inspect is a rule the reader cannot distrust, and a status board
you cannot distrust is one you cannot check. The legend screen states the
derivation explicitly.

### 2.4 The proposed derivation (illustrative, to be ratified at gate 4)

| Colour | Emitted when |
|---|---|
| `● RED` | any `hnone` (approval owed, never asked) · any `skipped_without_exception` · runtime `down` on a project recorded as deployed |
| `▲ AMBER` | any `warn` gate · any open loop-back · runtime `degraded` · any source older than the staleness threshold · any `gate_did_not_exist` (a coverage gap, per `PORTFOLIO_STATUS.md`'s own words) · any `hwait` |
| `? UNKNOWN` | any input unreadable, any probe inconclusive, or any chip whose reason set cannot be enumerated |
| `✓ GREEN` | **only** when every gate is `done`/legitimately `n/a`, every approval `hdone`/`hskip`, runtime `up` or `never_deployed`-by-design, and all sources fresh |

Note the asymmetry, deliberately: red and amber are *unions* (any one finding
trips them), green is an *intersection* (everything must hold). Uncertainty
falls to Unknown, never to Green.

**Precedence: `RED` → `UNKNOWN` → `AMBER` → `GREEN`.** Unknown outranks amber
and green but not red — an unreadable input can never be outranked into green by
good news elsewhere, and a known-red fact is not softened by an unrelated
unreadable file. A count that cannot be established renders `?`, never `0`,
because `0` is an assertion.

### 2.5 The three flavours of `⊘` get three distinct marks

Not one glyph plus a tooltip. A tooltip is not a rendering; it is a thing you
have to already suspect before you go looking.

| Fact | Mark | Border | Word on the face |
|---|---|---|---|
| `not_applicable` | `⊘` | dashed grey | `n/a · by template` |
| `gate_did_not_exist` | `⊘` on a **hatched** field | dashed grey + 45° hatch | `pre-gate · did not exist` |
| `skipped_without_exception` | `⊘` in **red**, solid heavy border | solid red | `SKIPPED · no exception` |

The third is not a quiet grey box. It is the second-loudest element the page can
produce, after `✋ NOT ASKED`.

---

## 3. Layout — the template, and why (R2, R4)

### 3.1 Template: PRINCE2 **Highlight Report**, section order preserved

R4 asks for an established status-report template rather than an invention. The
Highlight Report is the right one because it is *already* built around the
distinction this project cares about: routine progress vs. **exceptions**. It
has a named, ordered section list, which is what "follow a template" has to mean
if it means anything checkable.

| Highlight Report section | Region on this dashboard |
|---|---|
| Report header — project, period, date | **Header**: selector, "as of", source freshness |
| Overall status + status by area | **KPI tile row** (Layer 1) |
| **Exceptions / issues needing attention** | **Callouts band** (R3) |
| Milestone / schedule status | **Gate strip** + canonical graph |
| Products delivered this period | **Gate ledger** table |
| Risks, issues and change log | **Loop-backs · Exceptions · Route changes** |
| Next actions / decisions required | **"Waiting on you"** (folded into callouts) |

Overlaid on the **inverted pyramid**: 5–7 KPI tiles at the top where attention
lands, exceptions immediately under, full detail below, drill-down on demand.
Nothing below the fold is required to reach a correct conclusion about whether
something is wrong — that is the acceptance test for the layout.

### 3.2 Vertical order (project view), top to bottom

1. **Header** — selector rail · overall chip · `as of` · freshness strip
2. **KPI row** — 6 tiles (§4.2)
3. **Callouts** — 0..n cards; if zero, an explicit *"No findings — derived from
   N sources, all fresh"* card. Silence is never left ambiguous.
4. **Gate strip** — 11 gates + 11 approvals, the analytical layer
5. **Canonical graph** — the verbatim mermaid render (§6)
6. **Gate ledger** — the table from `PIPELINE_LOG.md`
7. **Loop-backs / Exceptions / Route changes**
8. **Runtime detail** — endpoints, probe results, check ages
9. **Provenance footer** — every source file, its mtime, its read status

### 3.3 Grid

Single column, max content width **1280px**, 12-column grid, 24px gutters.
Desktop only (A5.1) — no responsive breakpoints below 1024px are designed;
below that the page shows a plain "designed for desktop" notice rather than
degrading into a phone layout it was never tested at. KPI tiles: 6 across at
≥1280, 3×2 at 1024–1279.

---

## 4. Flows and controls

### 4.1 R1 — the project selector, and where I disagree with the requirement

R1 asks for **a dropdown**. I am proposing something else, and here is the
argument rather than silent compliance.

**A dropdown is the wrong control for this data, at this cardinality, for this
user.** Three reasons:

1. **A closed dropdown cannot carry state.** Its whole job is to hide the
   options. On a status board that means: while you are reading project A, a
   red project B is invisible *by design*. That is the same class of failure as
   the `⊘` conflation — a real fact rendered as nothing.
2. **Cardinality is ~6.** Dropdowns start paying off around 10–12 items. Below
   that they cost a click and buy nothing.
3. **It defeats comparison.** "Is this project unusually bad, or are they all
   like this?" is a question a status reader asks constantly, and a dropdown
   makes it a serial memory task.

**What I propose instead — and it still satisfies R1's intent**
("switch between projects, not five stacked graphs"):

- **A project rail**: a persistent horizontal segmented selector, one segment
  per project, each carrying its own attention chip and runtime dot in the
  segment itself. One click to switch. No project's red state can hide behind a
  collapsed control.
- **Plus a portfolio view as the default landing**, which is *one table*, not
  five stacked graphs — it satisfies the letter of R1 as well as its intent.
  Graphs appear only in a project view, one at a time.
- **The rail degrades to a `<select>` above ~8 projects.** At that point the
  rail's advantages invert and R1's original instinct becomes correct. The
  control is a function of cardinality, not a fixed choice.

If the human prefers the literal dropdown, it drops straight in — the rail and
the select are the same state, differently rendered, and I have rendered the
`<select>` fallback in the mockup so both can be judged side by side. **The one
thing I would push back hard on is a dropdown with no always-visible portfolio
row**, because that recreates "the bad news is one interaction away."

### 4.2 The KPI row — 6 tiles

Chosen to be six because five to seven is where a tile row is still scanned as a
row rather than read as a list, and because each of these answers a *different*
question. None of them is a count of things that "look fine."

| # | Tile | Answers |
|---|---|---|
| 1 | **Overall** | RAG+Unknown chip, with reason count |
| 2 | **Position** | current gate, name, and whether running / awaiting / blocked |
| 3 | **Approvals owed** | how many `hwait` + how many `hnone` — the two never merged |
| 4 | **Gates not run** | broken out by the three `⊘` flavours, never one number |
| 5 | **Runtime** | state word + check age |
| 6 | **Freshness** | oldest source mtime + read status |

**Tile 4 is the whole thesis in one component.** "3 gates not run" is exactly the
sentence that hid the Review skip. The tile renders `1 n/a · 2 pre-gate ·
1 no-exception` and the last segment is red whenever it is non-zero. A single
summed number is forbidden here, and that prohibition is an acceptance
criterion, not a preference.

**No tile ever shows a hardcoded denominator.** Not "7 of 11" as literal copy —
the 11 comes from the pipeline definition at render time (A7.3). If the pipeline
gains a gate, the tile changes with it and nothing in the design needs editing.

### 4.3 Callouts (R3), and the harm they carry (A7.2)

A callout is the most authoritative element on the page, so it is the most
dangerous. Rules:

- **A callout always names its evidence**: which file, which row, read at what
  time. No callout is a bare assertion.
- **Callouts are ordered by severity, then by age of the underlying fact.**
- **The empty state is a positive statement, not blankness**: *"No findings.
  Derived from N sources, all read successfully, newest 4m old."* A quiet page
  and a broken reader must never look alike.
- **An "all clear" callout is never rendered when any input failed to read.** In
  that case the band renders `? UNKNOWN — n of m sources unreadable` and lists
  them. This is the single most important rule in the document.
- **Callouts never aggregate across kinds.** "3 issues" is not a callout;
  "Review closed without the approval it owed" is.

### 4.4 Flows

**F-A · Between-session check (the dominant flow, target: under 10 seconds).**
Open `/status` → land on Portfolio → scan the attention column → either close
the tab, or click one project.
*Design consequence*: the portfolio table must be complete above the fold, and
must carry the freshness strip. If it can't be complete, it says so at the top.

**F-B · Mid-run "where are we?" (during an active gate).**
Open → the active project is pre-selected (state says which run is in flight) →
Position tile + `✋ YOU / approve?` are the loudest things on the page.
*Design consequence*: `hwait` gets the heaviest treatment in the whole visual
system, matching `admin/PIPELINE.md`'s "loudest thing in the graph."

**F-C · "Is the app actually up?"**
Open → Runtime tile → runtime detail for endpoint, status, latency, check age.
*Design consequence*: probes are **on page load**, and the check age is rendered
next to every verdict, always, even when it is 2 seconds old.

**F-D · Audit / "what was skipped?"**
Project view → gate strip → the three `⊘` flavours are distinguishable without
interaction → ledger row gives the reason text.

**Out of scope and staying out** (A8.2): no editing, no approving, no advancing
a gate, no trend charts, no notifications. **There are no write affordances
anywhere in this design** — no buttons that look actionable other than
selection, disclosure and theme. A read-only surface that looks like it can act
invites exactly one bad afternoon.

---

## 5. Runtime status — honest degradation

Seven states, all visually distinct, none of them collapsible into "up/down":

| State | Glyph | Colour | Rendered as |
|---|---|---|---|
| `up` | `●` | green | `UP · 200 · 8ms · checked 3s ago` |
| `degraded` | `◐` | amber | `RESPONDING · 404 at / · checked 3s ago` |
| `down` | `○` | red | `DOWN · connection refused` |
| `unreachable` | `⊗` | red | `UNREACHABLE · timeout after 2s` |
| `never_deployed` | `—` | slate | `NOT DEPLOYED · no endpoint recorded` |
| `unknown` | `?` | slate | `UNKNOWN · no probe result this session` |
| `stale` | `◌` | slate | `LAST KNOWN UP · 41m ago · not re-checked` |

`degraded` exists because of a real observation made while designing this: at
render time `little-milestones`' backend on `:8000` answered, but answered
**404 at `/`**. A naive probe calls that UP (something answered) or DOWN
(non-2xx) and both are lies. It is a server that is running and not serving what
we expected — which is precisely the shape of failure a status board exists to
surface. Recording it here so the probe design at gate 6 can't quietly pick
one of the two lies.

`stale` is a **decay**, not a separate reading: any verdict older than the
threshold visibly demotes to slate and prefixes with `LAST KNOWN`. Green never
survives its own freshness window. **Nothing on this page stays green by
inertia.**

---

## 6. Reconcile or supersede: "The Signal Path"

**Call: reconcile the identity, supersede four specific decisions.** Not a
clean-sheet redesign — `admin/kb-server/` is migrating into this project's
`dev/` (O2), one app, two routes, and two routes of one app should not look like
two products.

### Kept (this is the same family)

- The neutral scaffolding: `--void / --floor / --surface / --surface2`, the
  hairline system (`--hair`, `--hair-hi`), `--ink / --ink-dim / --ink-faint`.
- The **mono eyebrow with leading rule**, 0.28em tracking, uppercase — it
  becomes the section header of every report block, which is exactly what a
  status report wants.
- `tabular-nums` everywhere numeric; `text-wrap: balance`; `::selection` tint.
- **The aperture/slit motif for gates.** This one is not decoration — a gate
  *is* an aperture in the Signal Path's own vocabulary, and the gate strip is
  eleven apertures the work passes through. Kept literally: each gate node is a
  slit-marked cell, and the "signal" is the fill progress along the strip.
- The **iris** for agents, at small size, in the ledger's participants column.
- Grain, at reduced opacity (0.03).

### Superseded, with reasons

1. **"Commit to dark-only. Delete the light theme and the toggle." — superseded.**
   The brief requires both themes and it is right to: a status console is read
   at a desk in daylight, and — decisively — **the canonical mermaid palette in
   `admin/PIPELINE.md` §3 is a light palette** (`fill:#eef6ef`, `#fff8e6`,
   `#fdf0ec`). A dark-only surface cannot host the verbatim graph honestly.
   Default theme follows the OS.

2. **Theatrical display type (`clamp(3.6rem, 10vw, 8.2rem)`, ghost numerals at
   11rem, `padding: clamp(96px,14vh,180px)`) — superseded.** That scale is a
   marketing instrument: it makes one idea unmissable by making everything else
   wait. A status report is *dense by requirement* — many facts, none of which
   may be given up. Largest type here is the KPI numeral at 32px/600. The
   Signal Path's "≥1 element over 3rem type per viewport" test is explicitly
   waived for `/status` and I am recording the waiver rather than quietly
   failing the test.

3. **Ambient animation — the particle beam, ignition, scroll-driven signal fill,
   the blinking cursor — superseded, and this is the strongest of the four.**
   **Motion connotes liveness.** On a page whose entire purpose is to be honest
   about how old its knowledge is, a permanently animated surface asserts
   "live" with every frame, including when the underlying data is 18 days
   stale. That is A7.2 committed in the motion layer. Motion on this surface is
   restricted to: (a) state-change transitions under 200ms, (b) an explicit
   in-flight indicator *while a probe is actually running*. Nothing loops.
   Nothing idles. Everything honours `prefers-reduced-motion`.

4. **Ember as the accent — superseded; the accent becomes arc blue.** Ember
   `#f5a83c` is within a hair of the `warn` amber in the canonical `classDef`
   block (`stroke:#8a6410`, `fill:#fff8e6`). A brand accent that reads as
   "attention" makes a healthy page look mildly alarming and, worse, makes a
   genuinely amber page look normal. **Status hues are reserved exclusively for
   status; the accent is reserved exclusively for navigation, selection and
   focus.** No exceptions — a chart or chip may not borrow the accent, and a
   button may not borrow a status hue.

### Also carried forward: the cautionary tale

`DESIGN_SPEC.md` hardcoded *"Eighteen agents. / Nine gates."* into the **design
document**, so the wrongness was upstream of the code and would have shipped
through any implementation. Consequences adopted here, binding on gate 6/7:

- **No count, gate name, agent name or project name appears in this design as
  copy.** Every such string in the mockup is sample data and is labelled as such
  in the rendering itself.
- The gate strip is **generated by iterating the pipeline definition** — it has
  no fixed number of cells. If the pipeline becomes 12 gates, the strip is 12
  cells with no design change and no copy change.
- The page carries the pipeline's own version/mtime in the provenance footer, so
  "which pipeline shape is this drawn against?" is answerable on the page.

---

## 7. Colour and type

### 7.1 The status palette is the graph's palette

Non-negotiable, and it is what makes §6's reconciliation work: the dashboard's
status hues are **taken from `admin/PIPELINE.md` §3's `classDef` block**, so a
tile and the graph beside it can never disagree about what green means.

**Light theme (canonical — identical to the classDef values):**

| Role | Fill | Stroke | Text |
|---|---|---|---|
| done / GREEN | `#eef6ef` | `#2f6f43` | `#123021` |
| active / warn / AMBER | `#fff8e6` | `#8a6410` | `#3d2c04` |
| looped / RED | `#fdf0ec` | `#a3341f` | `#3d1109` |
| pending / skipped / UNKNOWN | `#f4f5f7` | `#b8bfc9` | `#767f8d` |
| approval given (`hdone`) | `#dcefe2` | `#2f6f43` | `#123021` |
| **awaiting you (`hwait`)** | `#ffe9a8` | `#8a6410` @4px | `#3d2c04` |
| **NOT ASKED (`hnone`)** | `#f8ded7` | `#a3341f` @3px | `#3d1109` |

**Dark theme** lifts the same *hues* for contrast on `--void #030405` — greens
to `#3fd68f`, ambers to `#e8b93f`, reds to `#f2645e`, slate to `#8b93a3` (these
three already exist in `kb-server`'s `:root` as `--good/--warn/--crit`, so the
two routes stay one family). Fills become 12% alpha washes of the same hue.
Hue relationships are preserved exactly; only luminance changes.

**Accent** (navigation/selection/focus only): `#1d4d8f` light, `#6fb4ff` dark.

**Contrast targets**: body and all status text ≥ 4.5:1; the `hnone` and
`skipped_without_exception` treatments ≥ 7:1 — the loudest facts get the
highest legibility floor, not just the strongest colour. Focus ring: 2px accent
+ 2px offset, never removed.

### 7.2 Type

| Role | Spec |
|---|---|
| Section eyebrow | mono · 11px · uppercase · 0.28em · leading rule (kept from Signal Path) |
| Page/section title | sans · 20px · 650 · -0.01em |
| KPI numeral | sans · 32px · 600 · `tabular-nums` (**not** 200-weight ultralight — a 5rem hairline numeral is the least legible element on most dashboards) |
| KPI label | mono · 11px · uppercase · 0.16em · `--ink-dim` |
| Body / table | sans · 13.5px · 1.55 |
| Data, IDs, paths, timestamps, glyphs | mono · 12.5px · `tabular-nums` |
| State word on a chip | mono · 11px · uppercase · 700 · 0.08em |

Rule: **anything the machine produced is mono; anything a human wrote is sans.**
Provenance made typographic — you can tell at a glance which parts of the page
are derived and which are quoted.

### 7.3 Palette variants — the "heavy on the eyes" pass (2026-07-29)

Human feedback on the approved mockup: *"I like the rendered mockup, can you
give some different color themes, it looks very heavy on eyes."* Structure,
the RAG-with-UNKNOWN resolution and the information design were approved in
substance; this was a colour/visual-weight pass only. Nothing was restructured.

**What I measured before changing anything.** The mockup now computes its own
contrast at render time (the audit panel under the switcher), so these are
measurements rather than claims:

| Finding | Measured | Verdict |
|---|---|---|
| Ground ladder is **non-monotonic** — `--void #f2f3f5` is *lighter* than `--floor #e9ebee` | void↔surface ≈ **1.06:1** | Defect. The page ground reads as sitting above the card it contains, so the eye re-hunts for every edge. |
| `--ink #141922` on white | ≈ **17.4:1** | ~2.5× the AAA floor. Correct for an audit, tiring to re-scan. |
| `--ink-faint` on surface | **3.05:1** light / **3.74:1** dark | **Fails 4.5:1** while carrying small mono metadata. A real accessibility failure missed at the first pass. |
| Saturated fills at tile scale (the hypothesis put to me) | `#fff8e6` ≈ 97% L, `#fdf0ec` ≈ 94% L | **Largely not the cause.** The canonical fills are already near-white and carry very little weight against the surface. |

**So where is the weight actually coming from?** Not the canonical hue values —
their *usage*: dark saturated `--*-line` strokes at 2–4px, six of them stacked
down the callout column; whole paragraphs set in `--r-text #3d1109` /
`--a-text #3d2c04`; and ~20 bold-uppercase-mono chips per screen. All of that is
chrome-adjacent or rule-level, and all of it is fixable without touching
`admin/PIPELINE.md`.

**Chrome-only vs. canonical — the split.** Variants override chrome tokens only
(`--void --floor --surface --surface2 --hair --hair-hi --ink --ink-dim
--ink-faint --accent --accent-soft --shadow`). §7.1's guarantee survives intact:
`--*-line` and `--*-text` stay byte-identical to the `classDef` block and the
canonical graph panel is untouched, so a tile and the graph beside it still
agree about what green means.

| # | Variant | Scope | One line | Greyscale test |
|---|---|---|---|---|
| 1 | **Canonical** (baseline) | — | As approved; kept so the comparison is fair | Passes |
| 2 | **Quiet Ledger** | Chrome-only | Ink off near-black; monotonic ladder at ~3.5× the plane separation | Passes |
| 3 | **Paper** | Chrome-only | Warm cream ground, brown-black ink, near-zero blue — print, not screen | Passes |
| 4 | **Low Light** | Chrome-only | Cool and dim, dark-first; floor raised off `#030405`, ink to ~10.6:1 | Passes |
| 5 | **Chartroom** | Chrome **+ colour area** | Colour rationed, not desaturated: hues stay canonical, their *area* shrinks | Passes — least colour-dependent of the five |

All four variants fix both baseline defects (monotonic ladder; `--ink-faint`
raised to pass 4.5:1). All keep §7.1, and all preserve the greyscale acceptance
test in §8 — no variant makes any fact colour-dependent, because glyph + word
were already carrying every state.

Variant-specific notes worth keeping:

- **Paper** is the one variant where a canonical change would genuinely help —
  the amber fill `#fff8e6` nearly disappears against a cream surface. Amber
  still survives on line + glyph + word, but the "colour intensifies" layer is
  weakest here. Not proposed: the price is 15+ regenerated graphs to rescue a
  variant I am not recommending. Its accent stays blue deliberately; a warm
  accent would collide with canonical amber, which §6 forbids.
- **Low Light** adjusts dark fill **alpha only** (.12 → .16) because the ground
  it composites onto is lighter. Hue unchanged.
- **Chartroom** softens `*-fill` only, and deliberately keeps `--hwait-fill` and
  `--hnone-fill` at *full* canonical strength — §4.2 calls `hwait` the loudest
  element in the system, so if colour is rationed those two keep all of it. It
  also returns callout prose to neutral ink, retaining the status hue on glyph,
  border and chip where it *identifies* the state. Its risk: §7.1 agreement is
  preserved by hue but weakened by area.

**Recommendation: variant 2, Quiet Ledger, chrome-only.** It is the smallest
change that addresses the cause the measurements point at, it costs nothing
outside this project, and it fixes the two defects. **No change to
`admin/PIPELINE.md` §3 is recommended or required.** If the human wants colour
to recede further after living with it, Chartroom (5) is the next step and is
*still* a project-local change.

**Deliberately not fixed, flagged instead.** The canonical graph panel is
hardcoded `#ffffff` in every theme by design (§7.1 — the palette is part of the
artefact). In a dim theme it is a bright rectangle. Dimming a reproduced
artefact makes it a different artefact, so it stays verbatim; **open question
for gate 6**, added to §9.

---

## 8. Accessibility

- **Greyscale test is the acceptance test.** Print any screen greyscale: no fact
  may be lost. Glyph + word carry every state; colour only intensifies.
- Semantic structure: one `h1`, `h2` per report section, real `<table>` with
  `<caption>` and `<th scope>` for the ledger, `<nav>` for the rail with
  `role="tablist"` / `aria-selected`, `<time datetime>` for every timestamp.
- Disclosures are `<details>`/`<summary>` or `aria-expanded` buttons — never
  hover-only. **No fact is reachable only by hover**, which also makes the page
  screenshot-able as evidence.
- Probe results announce via a single `aria-live="polite"` region, not one per
  row.
- `prefers-reduced-motion` removes the only two permitted motions.
- Full keyboard path: rail (arrow keys) → tiles → callouts → strip → ledger.

---

## 9. Open questions for gates 4 and 6

1. **Staleness threshold** — what age demotes a runtime verdict to `stale`, and
   what age turns the freshness tile amber? Proposed 5 min / 24 h. Human's call.
2. **Probe timing** — on load only, or a manual "re-check" button? A button is
   a write-shaped affordance on a read-only page; I lean on-load-only, with the
   check age doing the work. Needs a decision at gate 4.
3. **Drift detection** — the dashboard can compare `pipeline-state.json`'s mtime
   against the generated `PIPELINE_LOG.md`/`PORTFOLIO_STATUS.md` and flag
   disagreement. That directly attacks A2.1 (drift is the platform's most
   persistent failure) but is arguably scope beyond A8.3. Recommend in, as a
   callout kind. Human's call.
4. **Does `conclave-dashboard` appear in its own portfolio?** I say yes — it is
   the only project that can demonstrate `▶ active` and `✋ YOU approve?`, and a
   status board that omits itself has a blind spot at exactly its own location.
5. **The canonical graph panel in a dark or dim theme** (raised by §7.3). §7.1
   requires the panel to reproduce `admin/PIPELINE.md §3` verbatim, palette
   included, so it is hardcoded `#ffffff` in every theme — a bright rectangle in
   a dark UI. Dimming it makes it a different artefact; the alternatives are (a)
   leave it and accept the glare, (b) mat it in a wider recessed frame so it
   reads as a quoted document rather than a panel, or (c) collapse it behind a
   `<details>` in dark themes only — which §8 disallows if any fact lives only
   there. Left verbatim for now. **Decide at gate 6.**
6. **Which palette variant ships** (raised by §7.3). Five are rendered in the
   mockup's switcher; my recommendation is variant 2, Quiet Ledger, chrome-only.
   Human's call, and it is a project-local decision either way.

---

## 10. Deliverables produced at this gate

| Artifact | Path |
|---|---|
| This document | `projects/conclave-dashboard/knowledge/UX_KB.md` |
| Rendered mockup (all screens · 5 palette variants × light/dark · live contrast audit · greyscale-test toggle) | `projects/conclave-dashboard/design-review/index.html` |

**DesignSync**: not available in this invocation's tool grant, so no component
library was pushed. Recorded rather than silently omitted; the mockup's
component sheet (screen 5) is the push-ready inventory when it is available.

---

## 11. Observed post-deploy behaviour

*Empty — nothing is deployed. This section is the running log of how the design
actually performed once the human uses it, per this agent's contract. First
entry lands after gate 11.*

| Date | Observation | Design response |
|---|---|---|
| — | — | — |
