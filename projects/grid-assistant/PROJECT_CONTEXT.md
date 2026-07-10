# Project: grid-assistant

## Overview
- Template: genai-chatbot
- Created: 2026-07-05
- Target environment: local (cloud-dev/cloud-prod deferred, see admin/ROADMAP.md)
- Current stage: deployed (dev, local)

## Architecture Summary
`backend/app/mock_grid_data.py` holds a static `GRID_DATA` dict (4 fictional
regions — Northfield, Sunridge Valley, Bay Corridor, Highland Basin — each
with `load_percentage` and `status`) plus `format_grid_context()`, which
renders it into a plain-text block for prompt injection. No I/O, no external
calls, no async — pure static lookup, swappable later without touching the
endpoint.

`backend/app/main.py`'s `/chat` handler builds a system prompt each request
that states the assistant's role as a grid status assistant, embeds
`format_grid_context()`'s output as the sole source of grid-status truth, and
instructs the model to say it has no data for regions not listed rather than
guessing. It sends this via LangChain's `SystemMessage` + `HumanMessage` list
to `model.stream(...)`, replacing the prior raw-string call. Request/response
shape (`{"message": str}` in, streamed text out) is unchanged, so the
frontend placeholder and existing smoke test are unaffected. `llm.py`
(provider selection) and `frontend/app/page.tsx` are untouched — grid context
is a prompt-construction concern layered on top of the existing template.

## Decisions Log
- 2026-07-05: Scaffolded from `genai-chatbot` template (FastAPI+LangChain backend, Next.js frontend placeholder). [new-project skill]
- 2026-07-05: Approved PLAN.md for first feature — mock grid-data chatbot. System-prompt injection (not tool-calling) for the 4-region mock dataset; static Python dict, not JSON/DB; no LangChain prompt templates yet; refusal behavior is instruction-based, not code-enforced. See `PLAN.md` for full rationale. [plan-agent, approved by human]

## Test Results
- 2026-07-05: Test gate run against `dev/backend` (commit `2ea432c`). [test-agent]
  - **Unit/integration (pytest, `backend/tests/`): 5 passed, 0 failed.**
    - `test_smoke.py::test_health` — `GET /health` returns `200 {"status": "ok"}` (unchanged, pre-existing).
    - `test_mock_grid_data.py` (new, written this pass — no prior coverage existed for this module): confirms `GRID_DATA` has exactly 4 entries, each with `load_percentage`/`status` keys of the right types, and `format_grid_context()` returns a non-empty string containing every region name. Covers the "Functional / wiring" mock-data acceptance criteria from `PLAN.md`.
    - Note: the `POST /chat` non-empty-streamed-response wiring criterion has no dedicated test (would require a live LLM call — see gap below); only the mock-data module and `/health` are covered by automated tests today.
  - **Behavioral (qualitative) criteria: UNTESTED — known gap, not a pass.** `PLAN.md`'s 5 example prompts against `/chat` (region load lookup, "which regions do you have data for," out-of-scope region refusal, highest-load reasoning, unrelated general-knowledge question) require a real LLM call. Checked for credentials: `backend/.env` does not exist (only `.env.example`, which has `ANTHROPIC_API_KEY=` and `OPENAI_API_KEY=` blank), and no `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` are set in the shell environment. Without a real key, `/chat` cannot be exercised end-to-end, so these criteria remain unverified pending a human supplying a real API key.

- 2026-07-05: Behavioral criteria re-run with a real `ANTHROPIC_API_KEY` supplied by the human. All 5 example prompts from `PLAN.md` verified against the live `/chat` endpoint via `TestClient`: region load lookup (Northfield, 62%/normal — matches `GRID_DATA` exactly), region listing (all 4, no extras), out-of-scope refusal (Tokyo — declined without fabricating data), highest-load reasoning (correctly identified Highland Basin at 97%), and the unrelated general-knowledge question (answered normally while noting its primary scope — passes the loose check). **5/5 behavioral criteria pass.** [test-agent]
  - **Bug found during this run, not yet fixed**: `main.py` never calls `load_dotenv()` despite `python-dotenv` being a declared dependency — `.env` is not picked up automatically; verification required manually exporting the env vars. This will block `deploy-agent` from running the app standalone and should be fixed before the Deploy gate.

- 2026-07-05: Fixed the `load_dotenv()` gap (commit `15f0466`) — `main.py` now loads `.env` automatically. Re-ran full suite: 5/5 unit tests still pass, and confirmed `.env` auto-loads without manual export (`Bay Corridor` query returned correct data). Also relaxed `requires-python` from `>=3.11` to `>=3.9` in this project and the `genai-chatbot` template source, since 3.9.6 runs everything correctly and there was no functional reason for the higher floor. [code-agent, human-approved fix]

- 2026-07-05: Review gate approved (no changes requested) — decision-intent match confirmed against Decisions Log, code style/hygiene clean, `.env`/`.gitignore` handling verified safe. [review-agent]
- 2026-07-05: Deploy gate — started `uvicorn app.main:app` locally on port 8420, confirmed serving (`GET /health` → 200), ran post-deploy smoke test (`POST /chat` "load on Sunridge Valley?" → correctly returned 88%/elevated from the live process, not just TestClient). Server stopped cleanly after verification. [deploy-agent, target_env=local]
- 2026-07-09: Implemented `GET /regions` per approved `PLAN.md` (branch `feature/2026-07-09-regions-endpoint`). Added a `RegionStatus` Pydantic model and a synchronous `GET /regions` (`response_model=list[RegionStatus]`) endpoint to `backend/app/main.py`, reshaping the existing `GRID_DATA` dict into a list of `{name, load_percentage, status}` objects in insertion order — no changes to `mock_grid_data.py`, `llm.py`, `/chat`, or the frontend. Added `backend/tests/test_regions.py` covering status code, exact shape/keys, the exact 4-region JSON payload, and cross-call determinism. Full suite: 9/9 passed (5 pre-existing + 4 new), no live LLM call needed since `/regions` has no external dependency. Matches the no-auth posture and design decisions recorded in `knowledge/ARCHITECTURE_KB.md` and `knowledge/SECURITY_KB.md`. [code-agent]

- 2026-07-09: Test gate re-confirmed by test-agent (9/9 pytest) plus a response-shape check confirming `/regions` leaks no fields beyond the approved `{name, load_percentage, status}` — addresses security-architect's flagged information-disclosure concern for today's exposure (localhost-only, fictional data). Review gate approved, no changes requested — decision-intent match confirmed against PLAN.md/ARCHITECTURE_KB.md, and solution-architect's forward-looking `Literal["normal","elevated","critical"]` suggestion correctly deferred (not blocking this pass). Deploy gate: merged `feature/2026-07-09-regions-endpoint` to `main` (`84cffcc`), redeployed locally, smoke-tested `GET /regions` against the live process — correct 4-region JSON. Feature status: Ready for Release (not yet promoted to `prod/`). [enhance-agent, full mini-pipeline]
- 2026-07-09: **enhance-agent verification (Phase 5)**: this was the platform's first real `/enhance-project` run. Confirmed the re-engagement mechanism works correctly on an edge case — grid-assistant predates Team Composition entirely (built in Phase 2's reduced pipeline, no original roster recorded) — and enhance-agent still correctly enforced the always-re-engage set (solution-architect, security-architect, responsible-ai-architect, ui-ux-designer) while respecting the human's choice to leave functional-agent/industry-expert out. `ui-ux-designer` and `responsible-ai-architect` both correctly reported "nothing to design/guard here" for this feature rather than fabricating work — the intended non-duplication/non-fabrication behavior. This feature's Architecture gate created this project's first `ARCHITECTURE_KB.md`, `SECURITY_KB.md`, and `RESPONSIBLE_AI_KB.md` (retroactively, scoped to just this feature, not a full-project backfill).

- 2026-07-09: **First release: `v1.0.0`, promoted to `prod/`.** [release-manager] Only one feature was in "Ready for Release" (`GET /regions`), so no conflict analysis was needed — reported plainly rather than run as a no-op. Since `prod/` never previously existed, chose to establish a single `v1.0.0` baseline bundling everything currently on `dev/main` @ `84cffcc` (mock grid-data chatbot + `GET /regions`) rather than inventing separate retroactive versions for each — there is no prior public release to bump from, and the chatbot feature had already been through a full gate pipeline and standalone deploy, so `1.0.0` (not a pre-1.0 `0.1.0`) accurately reflects "first working promotion," not "unstable first cut." Full rationale in `RELEASES.md`. Cut `release/2026-07-09-v1.0.0` from `main` in `dev/`; full pytest suite re-run on the release branch: **9/9 passed** (5 chatbot/mock-data + 4 `/regions`), 0 failed. Dependency-diff check on `backend/pyproject.toml` confirmed trivial (single linear history, no concurrent conflicting bumps). Created `projects/grid-assistant/prod/` fresh (`git init`), added `dev/` as local remote (`dev-source`), fetched, merged the release branch into `prod`'s `main` (fast-forward, `--allow-unrelated-histories` since `prod/main` was unborn), and tagged `v1.0.0` at commit `84cffcc2a8fb5e116e78ed04e29520c667535910`. Created `CHANGELOG.md` and `RELEASES.md` at the project root (both new). `FEATURES.md` updated to move both bundled features to "Released."

- 2026-07-09: **[consult]** `responsible-ai-architect` consulted: does `/chat`'s
  system prompt adequately guard against role-play/instruction-override
  attempts or off-topic conversation drift? Answer: no — the existing prompt
  (`dev/backend/app/main.py::chat()`) only guards against data fabrication
  for unlisted regions (tested and working); it has no role-lock, no
  instruction-override resistance, and no off-topic scope limiting, so a
  user could push the model into a different persona or an extended
  unrelated conversation with no prompt-level pushback. Severity assessed as
  low-to-moderate and not blocking given today's localhost-only,
  unauthenticated, single-developer exposure, but recommended before any
  wider exposure: add a short role-lock clause and an off-topic-handling
  clause to the system prompt (instruction-based, consistent with this
  project's existing non-code-enforced refusal design). Not implemented as
  part of this consult — advisory for the next `code-agent` pass touching
  `/chat`. Full reasoning in `knowledge/RESPONSIBLE_AI_KB.md`. Does not add
  `responsible-ai-architect` to any Active Team roster (this project
  predates Team Composition history; a consult never changes roster status).
  [responsible-ai-architect, consult]

## Current Status
**Released `v1.0.0` to `prod/`, 2 features shipped.** Mock grid-data chatbot (first feature) and `GET /regions` (second feature, via `/enhance-project`) are both live end-to-end in `dev/` and now promoted to `projects/grid-assistant/prod/` (tagged `v1.0.0`, commit `84cffcc2a8fb5e116e78ed04e29520c667535910`). `dev/` backend port: 8420 (not currently running — start on demand via `uvicorn app.main:app --port 8420` from `dev/backend` with `.venv` activated and `.env` exported). No features currently in "Ready for Release" — next feature train starts fresh.
