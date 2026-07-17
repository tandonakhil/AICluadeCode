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
