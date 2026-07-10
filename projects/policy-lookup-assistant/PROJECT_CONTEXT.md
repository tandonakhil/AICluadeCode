# Project: policy-lookup-assistant

## Overview
- Template: rag-knowledge-base
- Created: 2026-07-05
- Target environment: local (cloud-dev/cloud-prod deferred, see admin/ROADMAP.md)
- Current stage: deployed (dev, local)

## Architecture Summary
Architecture gate complete (joint solution-architect + security-architect
output, 2026-07-05): manifest-driven authority metadata validated at
ingestion time (fail-loud on missing manifest entries), sentinel-token
refusal parsed via exact `.startswith()` match on the model's response
(no regex, no fuzzy match), `sources[]` always populated by the backend
(frontend decides whether to render badges per state). No new dependencies.
An `AskResponse` Pydantic model is added despite PLAN.md's stated deferral
(low-risk, additive, security-endorsed). No authn/authz for this
local/internal-tool-first MVP — explicit decision, revisit before any
shared/public deployment. One open item flagged by both roles for human
decision: whether to add a `max_length` bound to `AskRequest.question` in
this pass (both agree it's cheap; neither unilaterally added it — see
`knowledge/SECURITY_KB.md` section 6). See `knowledge/ARCHITECTURE_KB.md`
and `knowledge/SECURITY_KB.md` for full detail.

## Decisions Log
- 2026-07-05: Scaffolded from `rag-knowledge-base` template (FastAPI+LangChain+Chroma backend, Next.js frontend placeholder). [new-project skill]
- 2026-07-05: Intake complete — domain: utility regulatory/compliance policy lookup (functional-agent); industry: Utilities/Energy (industry-expert). Both KBs written with real research. [Intake gate]
- 2026-07-05: Plan & Backlog approved — 6-item MVP backlog in FEATURES.md; first feature: grounded-refusal + authority-labeled citations (addresses the highest-severity risks from both KBs). See PLAN.md. [plan-agent, approved]
- 2026-07-05: Experience Design approved — single-screen Q&A ledger, 4 states (empty/asking/answered/refused), refusal deliberately styled distinct from error states, authority badges color-coded per DOMAIN_KB's 4-value taxonomy. `DesignSync` genuinely unavailable in this environment (auth error, documented honestly in UX_KB.md, not faked) — component push is a manual/future-run follow-up. [ui-ux-designer, approved]
- 2026-07-05: Architecture gate approved — joint solution-architect + security-architect design for the manifest/sentinel/citation feature. No new dependencies; ingestion-time manifest validation; sentinel parsed via exact-match, not regex; explicit no-auth decision for local/internal MVP (revisit before shared/public deployment); `.env`/`.gitignore` re-verified clean. Open item resolved: add a `max_length` bound to `AskRequest.question` (both roles already agreed it's cheap and worth doing — approved). [solution-architect, security-architect, approved]

## Active Team
Approved 2026-07-05 — **full team** (Phase 4 verification run, deliberately includes every optional agent):
- Core (non-droppable): plan-agent, code-agent, test-agent, review-agent, deploy-agent, ui-ux-designer (template is UI-bearing).
- Optional (all included): functional-agent, industry-expert, solution-architect, security-architect.

- 2026-07-05: Code gate — implemented grounded-refusal + authority-labeled
  citations per PLAN.md/ARCHITECTURE_KB.md/SECURITY_KB.md. Judgment calls:
  (a) `grid_maintenance_policy.txt` manifest entry set to
  `authority: internal_policy`, `label: "Internal Policy"` — the doc reads as
  the utility's own operating standard (maintenance windows, inspection
  SLAs, crew reporting requirements) with no regulator letterhead or
  citation, matching PLAN.md's own baseline read of this doc; (b)
  `renewable_incentives_faq.txt` set to `authority: faq`,
  `label: "FAQ — Informal Guidance"` per its explicit Q&A format; (c) both
  `as_of` placeholder dates set to `2026-01-01` (project creation date), as
  PLAN.md specified, since neither source doc carries a real publication
  date. [code-agent]

## Test Results
- 2026-07-05: Unit/integration — `pytest`: 1/1 passed (`test_health`). All modified modules import cleanly. [test-agent]
- 2026-07-05: Real ingest + behavioral test against live `/ask` (real OpenAI embeddings + Anthropic chat, after resolving an initial `insufficient_quota` billing issue on the OpenAI account): ingested 2 docs → 5 chunks successfully. 4/4 acceptance criteria from PLAN.md passed:
  - Grid maintenance inspection-window question → correct exact answer ("48 hours"), `sufficient_evidence: true`.
  - **Commercial solar rebate cap** (not in corpus — only residential solar and commercial *wind* exist) → correctly refused, `sufficient_evidence: false`. This is the key extrapolation-trap regression test from DOMAIN_KB risk #6 — passed.
  - Out-of-domain question (capital of France) → correctly refused rather than fabricating an answer.
  - Residential solar rebate question → exact verbatim figures returned ("20%... up to $4,000... 12 months"), no paraphrasing/blending.
  - **Finding (minor, not blocking)**: `sources[]` on the grid-maintenance answer included both retrieved docs (`grid_maintenance_policy.txt` AND `renewable_incentives_faq.txt`), even though only the first was actually used in the answer — `sources[]` reflects what retrieval pulled (k=3), not what the model actually cited. Flagged for review-agent; architecture's stated rationale (never parse citations from model prose) is sound, but this means the UI could show an irrelevant source badge. [test-agent]

- 2026-07-06: **Functional-agent domain-correctness suite** (real, executed run — FastAPI `TestClient` against live `app/main.py`, real OpenAI embeddings + Anthropic chat, using the already-ingested Chroma store at `data/chroma_db`, no re-ingestion). Purpose: check domain correctness beyond test-agent's generic behavioral pass, per DOMAIN_KB risks #1 (wrong-authority citations) and #3 (numeric precision). 11/11 checks passed:
  - **Authority-label accuracy test**: asked the substation-inspection question, compared the `/ask` response's `sources[]` entry for `grid_maintenance_policy.txt` field-by-field against `data/sample_docs/manifest.json` (not just "a source is present"). `authority` == `"internal_policy"` exact match, `label` == `"Internal Policy"` exact match, `as_of` == `"2026-01-01"` exact match. `sufficient_evidence: true`, answer contained the exact figure "48 hours".
  - **Second numeric-precision spot check (distinct from test-agent's 48-hour/rebate checks)**: asked about the emergency-maintenance customer-notification rule ("unplanned outage lasting longer than 30 minutes — how quickly must customers be notified?"). Response returned the exact source figure "15 minutes" verbatim (not paraphrased as "promptly" or "quickly"), and correctly distinguished it from the adjacent "30 minutes" duration-trigger figure in the same sentence rather than conflating the two numbers. `sufficient_evidence: true`.
  - No failures to report. Test script and raw JSON responses captured during the run; both source entries in the response (`grid_maintenance_policy.txt` and `renewable_incentives_faq.txt`) matched the known `sources[]`-includes-all-retrieved-docs behavior already flagged (non-blocking) by test-agent — consistent with, not a new instance of, that finding. [functional-agent]

- 2026-07-06: **Industry-expert compliance suite** (real, executed run): asked SCADA-architecture and control-room-access-procedure questions to confirm the corpus-scope/BCSI boundary holds under live testing — both correctly refused with no fabricated operational/security content; a control question still answered correctly, confirming refusal isn't over-triggering generally. `grep`'d the backend for any public/consumer-facing posture (CORS, disclaimer copy, portal branding) — none found, consistent with the approved internal-tool-first scoping. AI-disclosure UI notice correctly not-yet-applicable (frontend unbuilt). **PASS.** [industry-expert]
- 2026-07-06: **Solution-architect architecture suite** (real, executed run): ran `load_documents()` against a temporary directory containing a rogue `.txt` file with no manifest entry — raised the expected `ValueError` naming the offending file; control run with the file removed loaded cleanly, confirming the exception was genuinely caused by the missing entry. Validated the live `AskResponse` contract against both response states (answered/refused) — all required fields present and correctly typed. Real project files/store untouched, temp dir cleaned up. **PASS.** [solution-architect]
- 2026-07-06: **Security-architect security suite** (real, executed run, `tests/test_security.py`, 4 tests): `max_length=2000` constraint confirmed genuinely enforced (2001 chars → 422; exactly 2000 chars → accepted, bound is inclusive). Secrets-leak check confirmed no `.env` ever entered git history and `.gitignore` actively blocks one. **Real finding**: an empty (`""`) or whitespace-only question to `/ask` causes an **unhandled 500** — Anthropic's API itself rejects blank message content, and neither `rag.py` nor `main.py` catches it before it reaches the LLM call. Root cause verified, not guessed. This is ordinary-usage-reachable ("submit with nothing typed"), not an adversarial edge case — **flagged as a blocking finding**, recommends adding `min_length=1` + a strip-and-check validator to `AskRequest.question`. **1/3 checks failed.** [security-architect]

- 2026-07-05: Review gate approved (no changes requested) — implementation matched ARCHITECTURE_KB/SECURITY_KB exactly including the `max_length` constraint; the `sources[]` finding confirmed as the architecture's documented trade-off working as designed, not a defect. [review-agent]
- 2026-07-05: Deploy gate — started `uvicorn app.main:app` locally on port 8421, confirmed serving (`GET /health` → 200), ran post-deploy smoke test (`POST /ask` grid-maintenance question → correct real answer against the live process). Server stopped cleanly after verification. [deploy-agent, target_env=local]

## Phase 4 verification outcome
All 4 optional SMEs (functional-agent, industry-expert, solution-architect, security-architect) plus non-droppable ui-ux-designer participated meaningfully at every applicable gate — real research, real design output, a real cross-role disagreement surfaced and resolved (not rubber-stamped). Confirms the full 9-gate pipeline with a full team works end-to-end, including a real ingest/embed/retrieve cycle against live OpenAI + Anthropic APIs. **The multi-suite Test gate mechanism itself is now verified**, not just designed: all 5 SME suites ran for real against this project — and the mechanism did exactly what it's for: security-architect's suite caught a real, reproducible crash (empty/whitespace question → unhandled 500) that no other suite or gate had surfaced.

- 2026-07-06: **Fixed both bugs found during multi-suite verification** (commit `7a7a469`): (1) `AskRequest.question` now has `min_length=1` plus a `field_validator` rejecting whitespace-only input with a clean 422, instead of reaching Anthropic's API and crashing with an unhandled 500. (2) While re-testing the fix, found a **second, independent bug**: a 2000-char repeated-character boundary-case question crashed `rag.py`'s `response.content.strip()` with `AttributeError: 'list' object has no attribute 'strip'` — LangChain types `AIMessage.content` as `str | list[str | dict]`, and this degenerate input triggered Anthropic returning a list of content blocks rather than a plain string. Added `_extract_text()` to normalize both shapes. Re-ran `test_security.py` (now 4/4 pass) plus a full edge-case sweep (blank, whitespace, 2001-char, 2000-char, normal query) — all correct. [security-architect finding, fixed and re-verified]
- 2026-07-06: **Housekeeping fix found while committing** (commit `1ad971e`): the Chroma vector-store binary data (`backend/data/chroma_db/`) had been committed despite `.gitignore` listing `data/chroma_db/` — the pattern didn't match the actual nested path since gitignore patterns containing a slash are relative to the `.gitignore` file's own location, not repo-root-relative-anywhere. Fixed the pattern to `backend/data/chroma_db/` in both this project and the `rag-knowledge-base` template source, and untracked the already-committed binaries (regeneratable via `python -m app.ingest`).

## Current Status
**Deployed (dev, local), all findings from multi-suite verification resolved and re-verified.** Two real bugs found and fixed (blank-input crash, list-content-shape crash), plus a git-hygiene fix (chroma_db binaries wrongly tracked). All 5 tests pass (`test_smoke.py` + `test_security.py`). Backend port: 8421 (not currently running).

- 2026-07-06: **Frontend implementation (Code gate)** — built the Next.js UI
  for the grounded-refusal + authority-labeled-citations feature per
  `knowledge/UX_KB.md` section 1 (Design Intent). Configured Tailwind v3
  properly (`tailwind.config.js`, `postcss.config.js`, `app/globals.css`
  with `@tailwind` directives — these did not exist before; also added the
  missing `autoprefixer` devDependency required by Tailwind v3's PostCSS
  pipeline). Implemented all 9 components from UX_KB.md 1.4
  (`QuestionInput`, `ScopeStatement`, `AnswerCard`, `SourceBadge`,
  `SourceBadgeList`, `RefusalCard`, `DisclosureNote`, `LoadingIndicator`,
  `QAHistoryItem`) under `app/components/`, plus shared types in
  `app/lib/types.ts` mirroring the backend's `AskResponse`/`SourceInfo`
  contract. `app/page.tsx` is a client component implementing the 4-state
  flow (empty/asking/answered/refused) with `QAHistoryItem`s stacking so
  prior Q&A pairs stay visible; it POSTs to `${NEXT_PUBLIC_API_URL ??
  'http://127.0.0.1:8421'}/ask` rather than hardcoding the port. Verified
  with a real `npm run build` (succeeds) and a `npm run dev` + `curl`
  smoke check confirming Tailwind classes render.
  Judgment calls (UX_KB.md 1.5 left exact hex/class choices to code-agent):
  (a) `regulation` = `bg-blue-900`/white text (deep navy, most saturated);
  (b) `guidance` = `bg-teal-700`/white text; (c) `internal_policy` =
  `bg-amber-100` bg / `text-amber-900` (muted amber/gold); (d) `faq` =
  `bg-slate-100` bg / `text-slate-700` (most muted, gray-blue) — the four
  are ordered darkest/most-saturated-to-lightest so relative authority is
  eyeball-able before reading the label, and every badge always renders the
  authority label text and `as_of` date alongside the color, never color
  alone. Refusal state uses `slate` (bg-slate-50/border-slate-300), never
  red, with a neutral outlined circle-with-dot icon (not a warning/X icon).
  No dark mode, no chat-bubble UI, no mobile-first responsive pass — all
  per UX_KB.md 1.6's explicit non-goals. [code-agent]

## Test Results — Frontend (UX_KB.md implementation)
- 2026-07-06: **Real Playwright browser test** against the live app (backend on :8421, frontend on :3421, Chromium via Playwright, installed for this purpose per TEMPLATE_MANIFEST.md's own stated smoke-test plan). Verified empty state HTML matches spec exactly (scope statement, labeled input, `aria-live` region).
  - **Bug found and fixed**: submitting a question failed with a browser-enforced CORS error (`No 'Access-Control-Allow-Origin' header`) — curl-based testing throughout this project never caught this, since curl doesn't enforce CORS, only real browsers do. Added `CORSMiddleware` scoped to a `FRONTEND_ORIGIN` env var (default `http://127.0.0.1:3421`), not a wildcard, consistent with the no-auth-but-not-wide-open local MVP posture from SECURITY_KB.md. Fixed, committed (`d4e0055`), re-verified.
  - **Answered state, real screenshot verified**: correct answer text, both authority badges rendered with correct colors (amber "Internal Policy," slate "FAQ — Informal Guidance"), each paired with filename + as-of date (never color-only), persistent disclosure note present under the answer, neutral (non-green) container.
  - **Refused state, real screenshot verified**: fixed refusal sentence, scope-statement reminder reappears, visually distinct slate-tinted container with a neutral info-circle icon — explicitly not red/error styling, exactly matching UX_KB.md 1.2/1.5's design intent that refusal is correct behavior, not failure.
  - **UX/accessibility suite (ui-ux-designer) is now genuinely applicable** — this closes the "not yet applicable" gap noted during Phase 4's multi-suite verification pass, which was blocked on the frontend not existing. [test-agent + real browser verification]

- 2026-07-06: **Review gate approved** (one fix requested and applied before sign-off): implementation matches UX_KB.md faithfully (9 components, 4-state flow, color scheme, accessibility basics, non-goals respected); one undocumented 5th "network error" sub-state noted as a minor KB-staleness gap, not blocking; CORS fix scoping (single `FRONTEND_ORIGIN`, not wildcard) confirmed correct. **Second real gitignore-precision bug found**: `frontend/.env.local` had been committed because the `.env` pattern only exact-matched, not `.env.local` — same class of bug as the earlier `chroma_db` path-anchoring issue. Fixed (`.env*` with explicit `.env.example` exceptions), untracked, applied consistently to this project, all 3 templates (`genai-chatbot`, `agentic-workflow`, `rag-knowledge-base`), and retroactively to `grid-assistant`. [review-agent, approved after fix]

## Current Status (frontend addendum)
Both backend and frontend are real, working, and integration-tested end-to-end via an actual browser, not just API-level curl checks. Frontend port: 3421 (proxying to backend :8421 via `NEXT_PUBLIC_API_URL`), backend port: 8421. **Both currently running** — deployed for live human testing, 2026-07-06.

## Environment note
Node.js was not available in this environment; installed via `nvm` (v0.40.1) with Node v24.18.0 LTS during this session, added to `~/.zshrc` so it persists across terminal sessions. This was an environment setup action, not a project-specific one — future frontend work in any project no longer needs this step.
