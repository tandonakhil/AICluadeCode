# UX Knowledge Base: policy-lookup-assistant

Owner: ui-ux-designer
Gate: Experience Design (first pass — covers PLAN.md's first feature:
grounded-refusal + authority-labeled citations)

This file has two sections per the ui-ux-designer role definition: **Design
Intent** (what was proposed and why, written before code exists) and
**Observed Post-Deploy Behavior** (a running log filled in once the feature
is live and has real usage — empty at this stage since nothing has shipped
yet).

---

## 1. Design Intent

### 1.1 Audience framing (read before anything else here)

Per `PROJECT_CONTEXT.md`, `FEATURES.md`, and `INDUSTRY_KB.md` section 1.3/3.6,
this is an **internal utility-staff tool**, not a public/customer-facing
chatbot — the OPG "ChatOPG" precedent (technicians and compliance/CS reps
retrieving policy in real time) is the direct comparable, not a consumer
support widget. That framing drives every choice below:

- No onboarding flow, marketing chrome, avatars, or conversational
  personality — staff already know what this tool is for and will use it
  repeatedly, not once.
- Design optimizes for **fast trust-checking by someone who already knows
  the domain**, not for delighting a first-time consumer. A compliance
  officer or field-adjacent staffer needs to see the authority level and
  as-of date at a glance, because (per DOMAIN_KB risk #1 and #8, and the
  Moffatt v. Air Canada precedent) an answer without visible provenance is
  actively worse than no answer — it invites unverified reliance.
- Density over whitespace-heavy consumer polish: this is closer to an
  internal admin/ops tool (think: a compliance dashboard, not a chat app
  landing page) in visual register.

### 1.2 End-to-end user flow

Single-screen flow, no multi-page navigation needed for this first feature:

1. **Empty state** — user lands on the page, sees a question input, a short
   scope statement ("Answers are grounded only in ingested utility
   maintenance and incentive documents — ask about those topics"), and
   nothing else. No example prompts carousel, no illustration — this is a
   utility, not a product demo.
2. **Asking state** — user submits a question. Input disables, a compact
   inline loading indicator appears where the answer will render (not a
   full-page spinner/skeleton screen — keep prior state, e.g. the previous
   Q&A pair, visible above so the user isn't staring at a blank page for a
   query that takes a few seconds).
3. **Answered state** (`sufficient_evidence: true`) — renders:
   - The answer text, with exact quoted figures preserved as returned by
     the API (no client-side reformatting of numbers).
   - One **authority badge** per unique source in `sources[]`, each showing
     `label` (e.g. "Internal Policy," "FAQ — Informal Guidance") and
     `as_of` date, visually distinct by authority level (see color scheme
     below).
   - The document filename as a citation, associated with its badge (not a
     generic "Sources: a.txt, b.txt" list detached from which claim came
     from which document).
   - A persistent, non-dismissible microcopy line under every answer:
     "AI-generated answer — verify against the linked source document."
     (This anticipates FEATURES.md item 3, which is explicitly deferred as
     a build item, but the design should reserve the layout slot now so
     item 3 is a copy/data change, not a new layout pass — flagging this
     as intentional forward-compat, not scope creep on this pass.)
4. **Refused state** (`sufficient_evidence: false`) — visually and
   structurally *distinct* from the answered state, not just an answer box
   with different text. This is the highest-leverage visual decision in
   this whole proposal, because DOMAIN_KB risk #5/#6 and the Test gate's
   acceptance criteria depend on refusal being unmistakable, not a hedge
   buried in prose the user might skim past:
   - Different container treatment (bordered/tinted card, not the plain
     answer box), a neutral "not answered" icon (e.g. an outlined
     circle-slash or info glyph — explicitly *not* a red error/alert icon,
     since this is correct, expected behavior, not a system failure), and
     the fixed product-controlled refusal sentence from `rag.py`.
   - No authority badges rendered in this state (there's nothing to cite),
     but the scope statement from the empty state reappears here as a
     reminder of what the corpus does cover, so the user isn't left
     wondering whether to rephrase or give up.
5. Both answered and refused states leave the input active immediately for
   the next question — this is a lookup tool used many times per session,
   not a one-shot form.

### 1.3 Key screen states (summary table)

| State | Trigger | Key elements | Visual treatment |
|---|---|---|---|
| Empty | Page load | Question input, scope statement | Neutral, minimal |
| Asking | Submit pressed | Disabled input, inline loading indicator, prior Q&A retained above | Neutral, low-motion |
| Answered | `sufficient_evidence: true` | Answer text, per-source authority badge(s), as-of date(s), filename citation(s), persistent verify-disclosure line | Calm, information-dense, badge color coded by authority |
| Refused | `sufficient_evidence: false` | Fixed refusal sentence, scope reminder, no badges | Visually distinct container (bordered/tinted), neutral (non-error) iconography |

### 1.4 Component list

For DesignSync (component-library) purposes, the following reusable
components cover this feature:

1. **`QuestionInput`** — text input + submit button/enter-to-submit, with a
   disabled/loading variant.
2. **`ScopeStatement`** — small static text block describing corpus scope;
   reused in both empty state and refused state.
3. **`AnswerCard`** — container for a successful answer: renders answer
   text as children, hosts `SourceBadgeList` and `DisclosureNote`.
4. **`SourceBadge`** — single badge: authority label + as-of date + source
   filename, color-coded by `authority` enum
   (`regulation | guidance | internal_policy | faq`). This is the
   highest-reuse, highest-importance component in the set — it is the
   direct UI expression of DOMAIN_KB risk #1.
5. **`SourceBadgeList`** — lays out one or more `SourceBadge`s under an
   answer (dedup'd by filename, matching the API's `sources[]` shape).
6. **`RefusalCard`** — container for the refused state: fixed refusal
   sentence, neutral icon, reuses `ScopeStatement`.
7. **`DisclosureNote`** — the persistent "AI-generated — verify against
   source" line; a standalone component now so item 3 (FEATURES.md) only
   ever touches this one component's copy, not layout.
8. **`LoadingIndicator`** — inline (not full-page) loading state for the
   asking transition.
9. **`QAHistoryItem`** — wraps one past question + its `AnswerCard` or
   `RefusalCard`, stacked so a user can scroll back through the session.

### 1.5 Color scheme rationale

Design goal: **an internal trust-critical tool signals authority and
certainty/uncertainty through color, not brand personality.** Consumer chat
products lean on a single accent color and friendly gradients; this tool
instead uses color as a *functional* channel, matching how compliance/ops
dashboards typically work (status colors carry meaning, not mood).

- **Base palette: neutral, low-saturation grays** for all chrome (page
  background, input, text) — this keeps the interface calm and keeps the
  functional colors (below) legible and un-competed-with. No dark-mode
  personality gradient, no illustration/brand color wash — utility staff
  scanning this repeatedly during a shift should not be visually fatigued
  by high-chroma UI.
- **Authority badges use a 4-step color-coded scale mapped to the closed
  `authority` enum**, ordered by binding weight (per DOMAIN_KB section 1's
  regulation > guidance > internal_policy > faq taxonomy):
  - `regulation` — strongest/most saturated treatment (e.g., a deep
    blue/navy) — reserved for legally binding content. Not used by either
    current sample doc, but the visual slot exists now per PLAN.md decision
    #3 (closed enum modeled ahead of corpus growth).
  - `guidance` — a distinct, slightly less saturated hue (e.g., teal) —
    also unused today, same forward-compat reasoning.
  - `internal_policy` — a muted amber/gold — signals "the utility's own
    rule, not government-mandated." Applies to
    `grid_maintenance_policy.txt`.
  - `faq` — the most muted/desaturated treatment (e.g., gray-blue) —
    signals lowest authority, matching DOMAIN_KB's explicit callout that
    FAQs are "often the least authoritative, fastest to go stale."
    Applies to `renewable_incentives_faq.txt`.
  - Rationale for a 4-step *ordered* scale rather than 4 arbitrary colors:
    a staffer scanning multiple badges should be able to eyeball relative
    authority at a glance (darker/more saturated = more binding) even
    before reading the label text — this is a redundant, non-color-only
    encoding requirement too (see accessibility note below), but the
    ordering itself is deliberate design, not decoration.
  - Every badge always pairs color with the text label (e.g., "Internal
    Policy") — color is never the sole carrier of authority information,
    both because color-blind users must be able to distinguish the four
    levels and because this is exactly the kind of high-stakes distinction
    (DOMAIN_KB risk #1) that must not silently degrade if colors are
    misread or the badge is screen-read aloud.
- **Refusal state uses a neutral/informational treatment (blue-gray or
  slate), explicitly *not* red/error styling.** A refusal is the system
  working correctly (declining to extrapolate, per FEATURES.md item 1),
  not a failure state — coloring it as an error would train staff to see
  correct, trustworthy behavior as something to distrust or dismiss, which
  is the opposite of what this feature exists to build. Iconography
  follows the same logic (info/neutral glyph, not a warning triangle or
  X).
- **No use of green for "success"/"answered."** An answered state is not
  inherently more trustworthy than a refusal — green would wrongly imply
  "good outcome" vs "bad outcome" framing onto what should read as
  "answer with evidence" vs "no evidence, correctly declined." Answered
  state uses the same neutral chrome as the rest of the page; only the
  authority badges carry color.
- **Accessibility baseline**: all color pairings (badge-on-background,
  text-on-container) target WCAG AA contrast at minimum, given this is a
  work tool used for extended periods, and every color-coded element has a
  text-label fallback so the interface remains fully usable at a glance
  under grayscale/color-blind viewing or when screen-read.

### 1.6 Explicit non-goals for this pass

- No chat-bubble/avatar visual metaphor — a Q&A ledger/list reads better
  for a lookup tool where provenance matters more than conversational feel.
- No dark mode / theming system in this pass — single, accessible light
  theme only; can be added later without touching the component contracts
  above.
- No mobile-first layout — internal staff usage (per INDUSTRY_KB's
  precedent of desk-based compliance/CS reps and technician workstations)
  is assumed primarily desktop/tablet; responsive behavior should not break
  but is not the design driver.
- Frontend implementation itself (React/Next.js component code) is
  code-agent's job once this proposal is approved — this document specifies
  flow, states, components, and visual language, not markup.

---

## 2. DesignSync Status

**Status: not pushed — DesignSync is unavailable in this execution
environment.**

Attempted `DesignSync.list_projects` in this run; it returned:

> "DesignSync needs design-system authorization, but /design-login requires
> an interactive terminal and is not available in this environment."

This is a known gap in this subagent context (no claude.ai/design login
available here), not a decision to skip the tool. **This proposal has not
yet been pushed to a Claude Design component-library project.**

When DesignSync access is available (e.g., run from an interactive session
with `/design-login` completed, or via Claude Design's "Send to Claude Code
Web"), the push should proceed incrementally as follows — this is the exact
plan a human or a future run should execute, not a placeholder:

1. `list_projects` — check whether a `policy-lookup-assistant` design-system
   project already exists; `create_project` (name:
   `policy-lookup-assistant`) if not.
2. `finalize_plan` with `writes` covering one file per component listed in
   section 1.4 above (9 components: `QuestionInput`, `ScopeStatement`,
   `AnswerCard`, `SourceBadge`, `SourceBadgeList`, `RefusalCard`,
   `DisclosureNote`, `LoadingIndicator`, `QAHistoryItem`), plus a
   foundational `colors`/`authority-scale` spec file documenting the
   4-step badge palette from section 1.5.
3. `write_files` — push each component as a preview/spec file (HTML or the
   project's preview format), starting with `SourceBadge` and `RefusalCard`
   first since those are the highest-stakes, most reused components in this
   feature (they directly encode DOMAIN_KB risk #1 and #5/#6 mitigations).
4. Never a wholesale replace of the project's files — incremental
   component-by-component pushes only, per the tool's own guidance, so a
   future revision (e.g., adding FEATURES.md item 3's disclosure copy
   changes, or item 6's staleness badge) touches only the affected
   component file(s).
5. Present the resulting Claude Design project link for human review
   alongside this KB file before Architecture designs the technical
   implementation.

**Action needed from a human or a future run with tool access:** run the
above push once `/design-login` (or equivalent) is available, then update
this section with the resulting `projectId` and a link.

---

## 3. Observed Post-Deploy Behavior

_None yet — this feature has not been built or deployed. This section will
be populated once the frontend implementing this design intent is live and
real usage (or Test-gate UX/accessibility runs) produces observations._
