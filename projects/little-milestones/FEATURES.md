# Features: little-milestones

## In Development

### Approved MVP backlog (Plan & Backlog gate, 2026-07-10 — approved by human via itemized review)

Priority order. Each item traces to its source(s): the human's stated
must-haves, DOMAIN_KB risks (R1–R8), and INDUSTRY_KB's proposed backlog
(I1–I6). **The human reviewed the full itemized backlog and approved F1–F10
for this pipeline run** — a much larger scope than plan-agent's proposed
first slice (F1–F5). Only F11 remains in the later backlog. F7's compliance
preconditions (retention/delete policy, encryption at rest,
private-by-default, no face processing, no AI training on child photos) are
therefore pulled INTO this run's scope, and F10 forces a real auth decision
at the Architecture gate instead of deferring it. PLAN.md sequences F1–F10
into three internal build increments so dependencies land first and the
gates run per-increment.

#### This pipeline run (F1–F10, approved 2026-07-10, human-selected)

- **F1 — Kid profile creation (minimal fields).** Display name, DOB, and a
  prematurity question (full-term? if not, weeks of gestation) — the minimum
  needed to compute age correctly. Supports multiple child profiles (twins
  are disproportionately preterm). Includes profile deletion that actually
  purges data. Data-minimized by design: no last name, no gender, no
  demographics, no photos.
  _Source: human request (profile up front); DOMAIN_KB R4 (corrected age
  needs gestational status), R6 (data minimization, deletion); INDUSTRY_KB
  §2.1 (retention/delete as de-facto benchmark)._

- **F2 — Age computation service (chronological + corrected age).** Server-side
  age math from DOB at query time: completed months, CDC checklist-age
  bucketing (2/4/6/9/12/15/18/24/30/36 mo), corrected age for preterm
  children through 24 months, defined behavior for newborns (<2 mo) and
  out-of-range (>36 mo) instead of extrapolation. The LLM never computes age.
  _Source: DOMAIN_KB R4 (all edge cases); INDUSTRY_KB I1 (age-conditioned
  everything — content must "grow" with the kid, computed from DOB at query
  time, not a static FAQ bot)._

- **F3 — Age-aware milestone chat with safety guardrails.** Chat conditioned
  on the selected child's computed age. System prompt enforces: CDC-2022
  75th-percentile framing ("most children do X by Y — if not, worth
  mentioning to your pediatrician"), no "your child is behind," no "don't
  worry" on missed milestones (anxiety-aware, no false alarm AND no false
  reassurance), hard medical-question deflection (no diagnosis, dosing, or
  symptom triage; red-flag concerns always routed to the pediatrician and
  never minimized; corrected age never used to explain away regression or
  asymmetry).
  _Source: human request (interactive chat at each milestone); DOMAIN_KB R1,
  R2, R7; INDUSTRY_KB I1, I2._

- **F4 — Age-based activity suggestions + "what's coming next" preview.**
  Activities for the child's current stage, each with supervision/safety
  context and filtered by hard safety rules (safe sleep, no small parts <3y,
  no unsupervised tummy time, supervised water only), plus a short preview of
  the next stage window with 2–3 preparatory activities. The preview rides on
  the same age logic as F2 at near-zero extra cost and is the category's
  strongest re-open trigger.
  _Source: human request (best activities at each age); DOMAIN_KB R5
  (activity safety is liability, not polish); INDUSTRY_KB I1, I3._

- **F5 — Non-medical disclaimer, visible and machine-checked.** Plain-language
  disclaimer ("general parenting information, not medical or
  developmental-screening advice") present in the UI and carried in every
  chat/activities response payload so the Test gate can assert it. Cheap now,
  expensive to retrofit after an incident.
  _Source: DOMAIN_KB R2; INDUSTRY_KB I2, §2.4 (trust posture; protects
  against implied-healthcare positioning the human explicitly ruled out)._

- **F6 — Milestone memory log → life-journey timeline.** Parent-logged "first
  smile / first steps" moments (text entries; F7 photos attach to them)
  rendering as the timeline visualization the human asked for; the category's
  retention core. Depends on stored history (F1's store patterns), so it
  builds after the F1–F5 increment. Hard visual rule: the timeline must never
  plot the child "behind a line" or against an expected-vs-actual axis (R1 in
  visual form) — checklist ages appear only as neutral chapter markers.
  _Source: human request (life-journey view); INDUSTRY_KB I4; DOMAIN_KB R8._

- **F7 — Photo upload + storage.** Photos attach to F6 memories. Its
  compliance preconditions are now IN scope for this run: retention/deletion
  policy (data lives until the parent deletes it; delete actually purges the
  file bytes), encryption at rest (design owned by security-architect at the
  Architecture gate), private-by-default access (photos served only through
  authenticated/owned API routes, never a public static mount), no face
  detection or processing of any kind, and no AI training or LLM ingestion of
  child photos (enforced structurally — the photo pipeline has no code path
  into the LLM layer). Builds after F6 and on F1's delete/privacy machinery.
  _Source: human request; DOMAIN_KB R6, R8; INDUSTRY_KB §2.1–2.2 compliance
  flags._

- **F8 — Weekly prompt digest.** Strictly opt-in (default off, one-click
  opt-out) "Maya is 14 months this week" digest with typical milestones
  ("most children" framing only), activities, and a memory prompt. **Shipped
  in full**: content + in-app "this week" view (Increment 2), real delivery
  via Resend + in-process APScheduler with RFC 8058 one-click unsubscribe
  (Increment 3, per ARCHITECTURE_KB §5's human-overridden real-delivery
  design) — real sending stays gated off pending an unmet Resend
  sending-domain verification precondition, not a code gap. Per-caregiver
  email opt-in active with F10 accounts.
  _Source: INDUSTRY_KB I5._

- **F9 — Buying recommendations.** Age-staged, contextual-only (never
  behavioral-ad-driven), served from a curated product-category catalog with
  a CPSC recall/banned-category safety filter applied at serve time — never
  raw LLM product output. A recalled or banned category must never appear in
  a response, even if it erroneously enters the catalog.
  _Source: human request; DOMAIN_KB R8; INDUSTRY_KB §1.5, §2.3._

- **F10 — Multi-caregiver access.** Invite second parent/grandparent into a
  family; caregivers can view and log memories, only the owner can delete a
  child profile or photos. Forces the auth design decision at the
  Architecture gate NOW (account model, credential handling, sessions,
  family scoping) instead of deferring it; F1–F9 build behind a
  family-scoping seam so auth activation does not rewrite routes.
  _Source: INDUSTRY_KB I6._

**Open Architecture questions carried with this run (not decided here):**
R3 grounding (curated CDC-2022/AAP table vs. framing-rules-only generation —
functional-agent's KB actively contests ungrounded generation); auth design
(forced by F10); photo storage + encryption-at-rest design (forced by F7);
email/notification infrastructure choice (F8); and whether the expanded data
surface (profiles + users + memories + photo metadata) forces the storage
backend from JSON files to SQLite. See PLAN.md §6.

#### Later backlog (via /enhance-project — NOT in this run)

- **F11 — RAG-grounded answering mode (conditional).** Only if a vetted
  pediatric corpus (CDC/AAP) is introduced; never scraped parenting blogs.
  _Source: PROJECT_CONTEXT later-scope; DOMAIN_KB R8._

- **F12 — Hardened auth suite (conditional on SECURITY_KB §1.6's revisit
  triggers, added 2026-07-11 per human request).** F10 ships a deliberately
  right-sized baseline (local email+password, argon2id, server-side
  sessions, no MFA/OAuth/password-reset — see SECURITY_KB §1.1–§1.3 for the
  full reasoning). F12 is the future pass that goes beyond that baseline if
  and when the triggers SECURITY_KB §1.6 already names actually fire:
  - **Self-service password reset** — the accepted MVP gap (no reset flow
    ships with F10); this is the first thing that should build once email
    infrastructure is used for it (email infra itself already shipped for
    F8, but was deliberately not repurposed for reset tokens — see
    SECURITY_KB §1.3's note). Single-use, short-expiry, rate-limited reset
    tokens, same rigor as invite codes.
  - **MFA** (TOTP-based) — revisit if the threat model changes (e.g.
    monetization, third-party integration, or data export/sharing beyond
    the family unit — SECURITY_KB §1.6 trigger 3).
  - **OAuth/social login** — currently rejected on privacy grounds (routes
    a child-adjacent account signal through a third-party identity
    provider); revisit only if a concrete user-facing need emerges that
    argon2id+session hygiene doesn't already serve.
  - **Managed session store / higher-concurrency session infra** — revisit
    before any non-local (cloud-dev/cloud-prod) deployment, alongside
    confirming `Secure`/HTTPS enforcement end-to-end (SECURITY_KB §1.6
    trigger 1).
  **Not scheduled** — this is a tracked, named backlog item so the decision
  not to gold-plate auth now is visible and revisitable, not a commitment
  to build all four sub-items together. Each sub-item's own trigger
  (above) decides when it actually gets picked up.
  _Source: human request 2026-07-11; SECURITY_KB §1.3, §1.6._

- **F13 — Chat history + age/history-aware suggested prompts (added
  2026-07-11 per human request — "chat page is very dull").** Two related
  but distinct pieces, likely one `/enhance-project` pass since they touch
  the same screen:
  - **Historical chats**: persist and let a caregiver browse past `/chat`
    conversations, not just the current in-memory session. Needs a schema
    decision (a `chat_sessions`/`chat_messages` table, family+profile
    scoped, same hard-delete discipline as memories/photos) — currently
    `/chat` is stateless server-side (PLAN §4.1/ARCHITECTURE_KB §6.1: the
    client resends full history each turn, nothing persists). This is a
    real architecture decision, not a frontend-only change.
  - **Suggested prompts**: on opening chat, surface a handful of starter
    questions tailored to the child's current age bucket and — where
    available — their logged memory/milestone history (e.g. a prompt
    referencing a recently-logged milestone_tag, or the next unreached
    CDC bucket). Must stay inside R1/R2's existing guardrail boundaries
    (RESPONSIBLE_AI_KB §3) — a suggested prompt is still content the app
    originates, so "never imply behind/ahead" applies to prompt copy too,
    not just chat responses. Content source: derive from
    `milestones_cdc2022.json` + the profile's own memories, not
    LLM-originated suggestions (same never-raw-LLM-origination discipline
    already applied to F9's product recommendations).
  - Both should go through Experience Design (ui-ux-designer) before
    Architecture, same as any UI-bearing feature — no design review has
    happened for a redesigned chat screen yet.
  _Source: human request 2026-07-11._

## Ready for Release

## Released
