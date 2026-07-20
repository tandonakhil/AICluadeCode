# PLAN: conclave-marketing — Multi-page marketing site (Plan & Backlog gate)

**Date**: 2026-07-17 | **Author**: plan-agent | **Status**: awaiting human approval
**Design seed**: `dev/design-reference/microsite-v5-seed.html` — approved direction; **extend, don't reimagine**.

## 1. Goal & audience (honest framing)

Today this is a **local-dev showcase/demo site** for the Conclave platform: no
deployment target, no external customers, placeholder contact address
(`hello@conclave.example` — flagged until the human replaces it). Copy and CTAs
must remain truthful if the site is later shared externally: the "conversion"
is routing a visitor to the Contact page (mailto — no fake form), and the
strongest honest proof is that the site was **built by Conclave itself**.
Imagined audience: energy-sector AI-software buying committees (product,
operations, compliance/security, IT) — the site must survive being forwarded
to skeptics. No customer-shaped language, ever.

## 2. Template & why

**Template: none** (human-approved deviation, recorded at Intake). No existing
template (`genai-chatbot`, `agentic-workflow`, `rag-knowledge-base`) fits a
marketing website; project scaffolded template-less with its own `dev/` repo.
**FastAPI + multi-page structure are human decisions** — not open questions.

## 3. Site architecture

Small FastAPI app (uvicorn) serving Jinja2 templates + static assets. No
database, no auth, no forms that post anywhere. **Zero external network
requests**; all fonts/CSS/JS/images self-contained.

```
dev/
  app/
    main.py               # FastAPI app: routes /, /solutions, /contact; 404 handler
    templates/
      base.html           # shared shell: head (per-page title/meta/canonical), header nav, footer brand block
      home.html           # numbered sections 01–0N (thesis → how → proof → personas → CTA)
      solutions.html      # deep-dive: 3 use cases, governance, platform/stack tabs
      contact.html        # one action (mailto), response expectation, no dead form
      404.html
    static/
      css/site.css        # extracted/organized from v5 seed styles
      js/site.js          # constellation, animations, tabs, marquee; reduced-motion aware
      img/                # SVG assets
  content/
    CITATIONS.md          # claims-substantiation manifest: claim → source → year → verified date
  tests/
    test_routes.py        # unit/integration (pytest + httpx TestClient)
    test_content.py       # citation-manifest sync, internal-link, banned-phrase checks
  design-reference/microsite-v5-seed.html   # frozen seed, never served
  requirements.txt
  README.md               # run instructions (uvicorn, port)
```

Routes: `GET /`, `/solutions`, `/contact`, static mount, custom 404. Each page:
distinct `<title>`, meta description, canonical URL, semantic landmarks,
correct heading order. Shared header (3-item nav) and THRED-style footer brand
block on every page; every page ends with the giant typographic closing CTA
routing to Contact.

## 4. Proposed feature backlog

Priority order. Size: S ≈ under half a session, M ≈ half–one, L ≈ 1+.

**MVP scope** (the v5 seed already contains most Home content — MVP =
restructure into multi-page + components the human explicitly asked for +
claims manifest):

- **F1 — FastAPI multi-page scaffold** (M): app, base template, three routes,
  404, static pipeline; port seed's shared chrome (nav → real links, footer,
  theme, ambient layers). *feature*
- **F2 — Home page restructure** (M): re-slot seed's numbered sections into
  `home.html`; compress deep-dive content (moves to Solutions); bigger
  Conclave branding (larger wordmark/headline type, per human intent);
  narrative order per DOMAIN_KB: problem → thesis → how → proof → personas →
  closing CTA; one primary CTA. *feature*
- **F3 — Always-moving hero: looping council animation + marquee** (M):
  continuous-loop council/pipeline diagram as hero explanation; marquee strip.
  Both freeze (not remove) under `prefers-reduced-motion`; marquee gets a
  pause affordance (WCAG 2.2.2). *feature*
- **F4 — Tabbed value-by-role module** (M): THRED CxO-style tabs for the four
  utility buying-committee roles from the seed. Each tab a genuinely distinct
  value story + role-specific proof artifact; if we can't write four distinct
  stories, cut to fewer (DOMAIN_KB rule). Keyboard + ARIA tablist. *feature*
- **F5 — Solutions deep-dive page** (L): structured by the three portfolio use
  cases (chatbot / agentic workflow / RAG) anchored to real utility pains
  (INDUSTRY_KB §6.1); gate-by-gate outage-chatbot walkthrough as canonical
  narrative; platform/stack tab module with detail cells (human intent);
  "governance, on the record" content — decision-record/test-evidence
  renderings, accurate framework language ("aligned with the expectations
  of," never "certified"). *feature*
- **F6 — Contact page + giant typographic closing CTA** (S): closing CTA
  component ("Convene the Conclave.") with grow-on-hover underline links
  (visible focus states) reused site-wide; Contact = one mailto action with
  response expectation; placeholder-address warning rendered in dev. *feature*
- **F7 — Claims-substantiation manifest** (S): `content/CITATIONS.md` mapping
  every stat/claim → source → year → verified date; verified Gartner 2024/2025
  stats carried over verbatim; hedged phrasing applied ("by design, nothing
  advances without approval" instead of "0 lines/100%" as outcome metrics);
  counts synced to `admin/MAS_REGISTRY.md`. Test gate checks page copy against
  the manifest. *feature*
- **F8 — Accessibility & reduced-motion hardening pass** (M): WCAG 2.2 AA
  sweep across all pages — copper-on-dark contrast (4.5:1 / 3:1), reduced-
  motion parity for every moving component, keyboard nav, landmarks, mobile
  behavior for marquee/tabs/giant type. *feature* (ui-ux-designer-led)

**Deferred** (post-MVP enhancements):

- **F9 — Verified-stats strip** (S): Gartner + optional Itron 81%/43% with
  inline source+year (house rule: number never without adjacent source).
- **F10 — "Built by Conclave" proof section strengthened** (M): faithful
  renderings of registry/gate/test artifacts; state the no-tracking/no-external-
  requests constraint as a trust point.
- **F11 — "Evaluation-ready" resource block** (M): RFP-shaped one-pager
  framing, reference-architecture diagram, stack-portability statement (ship
  only after verifying the "provider switchable by config" claim per template).
- **F12 — Additional THRED components** (M): any remaining reference
  components ranked by messaging value, not ported wholesale.
- **F13 — Real contact address swap + external-sharing checklist** (S):
  human-owned; blocks any external distribution.

## 5. Hard rules (apply to every feature)

1. Real citations only; every stat traces to `content/CITATIONS.md`, checked
   at Test. Unverifiable claim → cut.
2. No fabricated customers, testimonials, logos, or traction-implying copy.
3. Reduced-motion parity (freeze, not remove) for every always-moving
   component; looping motion always has a pause/reduce path.
4. WCAG 2.2 AA target on all pages (contrast, keyboard, ARIA, landmarks).
5. "0 lines / 100%" claims phrased as design guarantees, not audited outcome
   metrics (INDUSTRY_KB §5); no "NERC CIP compliant" / "ISO 42001 certified."
6. `hello@conclave.example` stays visibly flagged (code comment + README +
   F13) until the human replaces it.
7. Zero external network requests; assets self-contained.

## 6. Classification, tests, deploy

- **Semver**: all backlog items are *features* (minor bumps). F2's move of
  content off the single page is not breaking (no published URLs exist).
  First release = 0.1.0 on MVP (F1–F8).
- **Test expectations per feature**:
  - F1: pytest unit/integration (route status, template render, 404, static
    serving, per-page title/meta, no external URLs in rendered HTML).
  - F2, F5, F6: integration (content present, internal links resolve, one
    primary CTA per page) + citation checks (F7 manifest sync).
  - F3, F4, F8: UX/accessibility suite owned by **ui-ux-designer** —
    reduced-motion behavior, ARIA/keyboard on tabs, contrast, focus states.
  - F7: dedicated citation test — every stat in rendered pages appears in
    manifest with source+year; banned-phrase check (customer-shaped language,
    "certified," unhedged 0-lines/100% phrasing).
  - All active suites blocking per approved Test Policy.
- **Deploy**: local uvicorn (`uvicorn app.main:app --port <TBD>`); port chosen
  at Architecture gate — **8000 and 3000 are occupied by little-milestones**
  (propose 8100-range). README documents run/stop. No prod promotion until
  F13 (real address) at minimum.

## 7. Risks (top 5)

1. **Design-revision cost spiral** (flagged by usage-monitor as biggest cost
   risk). *Mitigation*: seed = approved direction; extend, don't reimagine;
   visual changes limited to what a feature explicitly requires.
2. **"Replicate every THRED component" scope magnet.** *Mitigation*: MVP fixed
   to F1–F8; remaining components live in F12, ranked by messaging value with
   an accessibility budget each — human re-approves before any are built.
3. **Overclaiming / marketing–product drift** (FTC Operation AI Comply in
   scope). *Mitigation*: F7 manifest + banned-phrase tests; counts sourced
   from `admin/MAS_REGISTRY.md` at build and re-verified at Test;
   responsible-ai-architect claims review before Deploy.
4. **Accessibility debt from always-moving components** — self-refuting for a
   governance product. *Mitigation*: reduced-motion parity is an acceptance
   criterion inside F3/F4, not deferred to F8; F8 is the sweep, not the fix.
5. **Persona tabs with thin, near-duplicate copy** — worse than no tabs.
   *Mitigation*: F4 acceptance requires distinct value story + proof artifact
   per tab; fall back to fewer tabs rather than pad.

## 8. Acceptance criteria (Test gate checks MVP against these)

- Three routes serve with correct titles/meta/canonical; 404 handled; zero
  external requests in any rendered page.
- Every stat on any page exists in `CITATIONS.md` with source + year; hedged
  phrasings in place; no customer-shaped or certification language.
- Every moving component freezes under `prefers-reduced-motion`; marquee
  pausable; tab modules keyboard-operable with correct ARIA.
- Contrast passes 4.5:1 body / 3:1 large on copper-on-dark.
- One primary CTA per page; every page ends with the closing-CTA component
  routing to Contact.
- Placeholder address flagged in README and page source; app runs via uvicorn
  on the Architecture-chosen port with documented start command.

---

## Rebuild v2 — Show Your Work (2026-07-19)

**Author**: plan-agent | **Status**: awaiting human approval (per-feature checklist)
**Supersedes**: the v1 site above (F1–F12, deployed 2026-07-17). Kept for history;
v2 replaces its pages, palette, motion, and information architecture wholesale.

### Context

The human rejected the v1 site ("very confusing for a visitor, does not tell me
what it does in one line") and approved a full redesign from the rendered
mockup `design-review/show-your-work-mockup.html`: **"Show Your Work"** — five
pages forming a question chain, each page answering its title question in its
first sentence and ending with the next question as a forward link. Formal
human decisions bound into this plan:

- **Industry-agnostic** — zero energy/utility framing anywhere; generic
  examples (customer-support chatbot, automated workflows, knowledge
  assistants). Any energy-anchored stat or copy from v1 is retired, not ported.
- **Palette "Paper & Seal"** — light: Paper `#F7F5F0`, Ink `#1D1C1A`, Deep Teal
  `#0B6B60`, Human Gold `#8A5A17`, Artifact Cream `#FBF3E4`, Rework Rust
  `#A8432F`; dark: `#161513` / `#EDEAE2` / `#3FC9B9` / `#E0A94E` / `#242019` /
  `#E07A5F`. Typography: Georgia-stack serif for question headlines + artifact
  cards; system sans for body/UI.
- **Signature motion**: gold seal stamp (scale-and-settle) at every human
  decision; grow-underline links; page-entrance rises; card cascades. Nothing
  loops or autoplays; everything static under `prefers-reduced-motion`.
- **Human additions at approval** (explicit features below, not afterthoughts):
  (a) substantive content depth per page — F2.4/F2.7/F2.8; (b) more intuitive
  pipeline animation on `/how` — F2.5; (c) `/who` as a connected hierarchy
  visualization, not word-heavy cards — F2.6.

**The question chain** (routes replace v1's `/`, `/solutions`, `/contact`):

1. `/` — "What is Conclave?" (one viewport, no below-fold)
2. `/how` — "How does it work?" (the nine-gate build replay)
3. `/who` — "Who does the work?" (the roster hierarchy)
4. `/what` — "What can it build?" (three app types)
5. `/why` — "Why trust it?" (evidence + contact)

**Carry-forward constraints (non-negotiable, from v1 hard rules)**: zero
external network requests; WCAG AA contrast in both themes; 100% original
content; every stat mapped in `content/CITATIONS.md` and enforced by
`tests/test_content.py`; honest claims only (no invented customers); FastAPI +
Jinja2 + vanilla CSS/JS; extend the existing test-suite pattern; real contact
address remains deferred and human-owned (F13).

### Target structure (delta from §3)

```
dev/app/
  main.py                 # routes /, /how, /who, /what, /why; 404; legacy redirects
  templates/
    base.html             # rewritten shell: question-chain nav, theme toggle, footer
    index.html  how.html  who.html  what.html  why.html  404.html
  static/
    css/site.css          # Paper & Seal tokens (light+dark), serif/sans scale
    css/motion.css        # seal stamp, rises, cascades, underlines, reduced-motion
    js/replay.js          # /how stepper engine
    js/roster.js          # /who hierarchy interaction
    js/site.js            # theme toggle, entrance observers, shared utilities
    img/                  # inline-able SVG assets (seal, rail, hierarchy)
content/
  CITATIONS.md            # rewritten for v2 copy (industry-agnostic)
  replay/                 # optional: per-gate artifact excerpts as data (see F2.4)
tests/
  test_routes.py  test_content.py   # extended for 5 routes + chain invariants
```

### Feature backlog v2

Sizes: S ≈ under half a session, M ≈ half–one, L ≈ 1+.

- **F2.1 — Paper & Seal foundation** (M): new `base.html` shell, five routes +
  404 in `main.py`, full light/dark token system, serif/sans typography scale,
  question-chain top nav, theme toggle, footer.
  *Accepts when*: all 5 routes serve with correct title/meta/canonical; both
  themes render from CSS custom properties only; every token pair used for
  text meets 4.5:1 (body) / 3:1 (large) in both themes; nav marks the active
  question; zero external requests.
- **F2.2 — Signature motion system** (M): shared motion layer — gold-seal
  stamp (scale-and-settle), grow-underline links, page-entrance rise,
  card cascade, word-by-word headline utility; one reusable CSS/JS vocabulary,
  not per-page one-offs.
  *Accepts when*: each primitive exists once and is consumed by pages, not
  duplicated; nothing loops or autoplays; under `prefers-reduced-motion` every
  primitive renders its final static state (element present, no transform/
  opacity animation); links keep visible focus states.
- **F2.3 — `/` "What is Conclave?"** (S): single-viewport page, no below-fold
  content at common desktop sizes. Headline exactly: "Conclave is a team of AI
  agents that builds AI applications — and a human approves every step." with
  word-by-word entrance and gold underline drawing under "human"; CTA "Build
  one with us" (→ `/why` contact block); forward link "How does it actually
  work? Watch one get built →" (→ `/how`).
  *Accepts when*: headline text matches verbatim and is the page's first
  sentence; page fits one viewport (no vertical scroll at ≥ 1280×800 and a
  sane mobile treatment); both links resolve; reduced-motion shows the full
  headline + underline statically.
- **F2.4 — `/how` replay engine + nine gates fully written** (L): the
  centerpiece. Stepper through all NINE gates (Intake, Team Composition,
  Plan & Backlog, Experience Design, Architecture, Code, Test, Review, Deploy)
  of a canonical customer-support-chatbot build. Per step: agent chips,
  artifact card (rendered excerpt in serif on Artifact Cream — a real-shaped
  artifact: intake brief, backlog checklist, design spec, code diff, test run,
  review notes, deploy record), human decision as gold seal; **step 7 (Test)
  is an honest "Sent back" in Rework Rust**, followed by the fix and re-pass.
  Next/Back buttons, fully keyboard-operable, no autoplay; gate-progress rail
  shows position. Content is substantive per the human's addition: every gate
  gets a genuinely distinct, fully written artifact excerpt — no placeholder
  or near-duplicate steps. All excerpts are original, honest, industry-
  agnostic ("a canonical build," not a fake customer).
  *Accepts when*: 9 steps, each with distinct agent chips + distinct written
  artifact + a decision; step 7 renders the rust "Sent back" path; stepper
  operable by keyboard alone (buttons focusable, Enter/Space, arrow keys);
  no timer-driven advancement; the page's first sentence answers "How does it
  work?"; forward link to `/who` present.
- **F2.5 — `/how` intuitive pipeline motion** (M): the human's "more intuitive
  animation" addition, layered on F2.4. Concrete proposal: (1) *hand-off
  flow* — on step entry, a teal pulse travels a drawn connector from the
  active agent chip(s) into the artifact card, then the card rises in, then
  the gold seal stamps: agent → artifact → decision reads as one continuous
  motion; (2) *advancing rail* — on approval, the rail's current node fills
  gold and a line visibly draws forward to the next node before the step
  transitions; (3) *send-back reversal* — at step 7, the rail line draws
  BACKWARD in rust from Test to Code, then re-advances on the fix; (4)
  *directional transitions* — Next slides content forward (exit left / enter
  right), Back reverses, so direction always matches pipeline motion. All
  sequences are triggered only by user action, never looped, and collapse to
  static final states under reduced motion.
  *Accepts when*: the four behaviors above are present and per-interaction
  (not ambient); total per-step sequence stays under ~1.2s so repeat stepping
  never feels slow; reduced-motion shows completed rail/connector states with
  no animation; keyboard-triggered steps get the identical sequence.
- **F2.6 — `/who` connected hierarchy visualization** (L): replaces card
  lists entirely. SVG-based diagram: human at top → orchestrator → specialist
  agents, with gate-ownership connections; connections draw in on entrance
  (once, no loop). Interactive nodes: hover/focus/click reveals that node's
  detail (role, gate owned, what it produces) in an adjacent panel — detail
  lives in the panel, keeping the diagram itself sparse. Every node keyboard-
  focusable in a logical order with visible focus rings; detail panel is a
  live region or linked via `aria-expanded`/`aria-controls`. Roster and gate
  ownership synced from `admin/MAS_REGISTRY.md` at build time (counted, not
  guessed — v1's "eight vs six" lesson). Responsive: reflows or pans sensibly
  on mobile rather than shrinking to illegibility.
  *Accepts when*: hierarchy renders human → orchestrator → agents with
  visible gate connections; every node operable by mouse AND keyboard with
  the same revealed detail; no word-heavy card grid anywhere on the page;
  roster contents match the registry; reduced-motion shows fully drawn
  connections statically; first sentence answers "Who does the work?";
  forward link to `/what`.
- **F2.7 — `/what` "What can it build?"** (M): three app types — support
  chatbots, automated workflows, knowledge assistants — each with a full
  treatment (what it is, what a build produces, what the human approves along
  the way, an honest "what it is not"), not a three-tile teaser. Industry-
  agnostic examples only. Card-cascade entrance from F2.2.
  *Accepts when*: three genuinely distinct treatments (no shared boilerplate
  sentences between types); no capability claim beyond what the templates
  catalog actually supports; no industry framing; first sentence answers the
  title; forward link to `/why`.
- **F2.8 — `/why` "Why trust it?" evidence page** (L): the chain's terminus.
  Contents: (1) decision-log excerpts rendered as artifact cards (real-shaped,
  original); (2) test evidence including the failure — the honest "sent back"
  record; (3) the two Gartner citations with inline source + year (30% GenAI
  PoC abandonment, 2024; 40%+ agentic canceled by 2027, 2025); (4) the FULL
  claims-to-source table rendered on-page from the same facts as
  `content/CITATIONS.md`; (5) "this site was built by Conclave itself" proof
  block; (6) contact block with the CTA — one mailto action, placeholder
  address still flagged (F13 unchanged, blocks external sharing).
  *Accepts when*: all six blocks present; every on-page claim row matches a
  CITATIONS.md row; the failure evidence is real-shaped and rust-styled; the
  contact block is the site's conversion endpoint (the `/` CTA lands here);
  first sentence answers "Why trust it?"; the chain terminates (closing link
  loops to `/`, "Start again — What is Conclave? →" or equivalent).
- **F2.9 — Citations manifest v2 + industry-agnostic content sweep** (S):
  rewrite `content/CITATIONS.md` for v2 copy — keep only the two Gartner rows
  and Conclave-self-referential rows; retire all energy-anchored rows
  (Deloitte outlook, EPRI, Itron, NERC) with a "retired 2026-07-19,
  industry-agnostic pivot" note rather than silent deletion; keep the "claims
  deliberately NOT made" section. Add an industry-framing banned-term list
  (utility/utilities, energy, grid, outage, NERC, meter, etc.) to the content
  rules.
  *Accepts when*: every stat rendered anywhere in v2 has a manifest row;
  no retired stat appears in any template; hedged 0/100% phrasing preserved
  wherever those design guarantees are stated.
- **F2.10 — Test-suite extension** (M): extend `test_routes.py` +
  `test_content.py` for v2, same pattern: 5 routes + 404 + legacy redirects;
  per-page title/meta/canonical; zero external URLs; stat↔CITATIONS sync;
  banned phrases now including the industry-term list and customer-shaped
  language; **question-chain invariants** (each page's `<h1>` is its
  question; each page contains its forward link to the next route; `/` links
  to `/how`, chain ends at `/why`); structural a11y checks (one `<h1>`,
  landmarks present, no heading-order skips, stepper/nodes have real button
  semantics). ui-ux-designer owns the interactive/contrast/reduced-motion
  audit at the Test gate as before.
  *Accepts when*: suite passes green on the finished v2 build; deliberately
  breaking a chain link or reintroducing a banned term fails a test.
- **F2.11 — Legacy route retirement** (S): `/solutions` → 308 redirect to
  `/what`, `/contact` → 308 to `/why`; old templates/CSS/JS removed from
  `app/` (v1 remains in git history and the frozen design seed stays in
  `design-reference/`); README rewritten for v2 (run command, port 8100,
  route map, F13 flag).
  *Accepts when*: both legacy paths redirect (tested); no dead v1 template,
  style block, or script ships in the served app; README current.

### Suggested build order

1. **F2.1** foundation → 2. **F2.2** motion system (everything else consumes
these two) → 3. **F2.3** `/` (smallest page; proves foundation + motion end to
end and gives the human an early visual checkpoint) → 4. **F2.4** replay
engine + content → 5. **F2.5** pipeline motion (layers on a working replay) →
6. **F2.6** `/who` hierarchy → 7. **F2.7** `/what` → 8. **F2.8** `/why` →
9. **F2.9** citations sweep (needs final copy from all pages) → 10. **F2.10**
test extension → 11. **F2.11** legacy retirement + README. Semver: v2 ships as
**0.2.0** on completion of F2.1–F2.11; F13 unchanged, still blocking external
sharing.

### Risks (v2-specific)

1. **/how content thinness** — nine distinct, well-written artifact excerpts
   is the largest writing task in the plan; padding would gut the concept.
   *Mitigation*: F2.4 acceptance requires distinct artifacts per gate; model
   them on this project's own real gate outputs (reshaped, original).
2. **Hierarchy visualization accessibility** — interactive SVG is the easiest
   place to strand keyboard/screen-reader users. *Mitigation*: keyboard parity
   and panel semantics are F2.6 acceptance criteria, not a later sweep.
3. **Motion-layer creep on /how** — "more intuitive" must not become "always
   moving" (would violate the no-loop rule and v1's own lesson). *Mitigation*:
   F2.5 caps sequences at ~1.2s, everything user-triggered.
4. **Industry framing leaking back in** via reused v1 copy. *Mitigation*:
   v2 copy written fresh; F2.9 banned-term list enforced by F2.10 tests.
5. **One-viewport home regressing** as copy is added later. *Mitigation*:
   F2.3's no-below-fold rule is a standing test-gate check, not a one-time one.
