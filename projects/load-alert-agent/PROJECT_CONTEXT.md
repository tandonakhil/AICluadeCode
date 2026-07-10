# Project: load-alert-agent

## Overview
- Template: agentic-workflow (API-only, no UI)
- Created: 2026-07-05
- Target environment: local (cloud-dev/cloud-prod deferred, see admin/ROADMAP.md)
- Current stage: deployed (dev, local)

## Architecture Summary
`backend/app/mock_substations.py` is a new pure-Python module holding a
fictional `SUBSTATIONS` dict (5 substations, each with
`rated_capacity_mw`/`current_load_mw`), a deterministic `classify_load()`
(ok / warning >=90% / critical >=105%), and a case-insensitive
`get_substation()` lookup. `backend/app/graph.py`'s placeholder
`lookup_status` tool is replaced with `get_substation_load`, a `@tool`
that looks up the mock data, computes `load_percent`, and returns a
structured dict (`substation_name`, `rated_capacity_mw`, `current_load_mw`,
`load_percent`, `status`) — or an `error` field if the name isn't in the
mock dataset. `create_react_agent` is now given a `prompt=` system message
instructing the agent to always call the tool, treat `status` as
authoritative for the alert decision, state the numbers, and explicitly
say whether an alert is warranted. `main.py` and `llm.py` are unchanged;
the `/invoke` request/response contract is preserved.

## Decisions Log
- 2026-07-05: Scaffolded from `agentic-workflow` template (FastAPI + LangGraph, API-only). [new-project skill]
- 2026-07-06: Plan & Backlog drafted for the substation load-check feature (`PLAN.md`): real mocked `get_substation_load` tool over 5 fictional substations replaces `lookup_status`; alert threshold classification (`classify_load`, ok/warning>=90%/critical>=105%) is a deterministic code function, not LLM-decided, for auditability; hysteresis/dedupe explicitly deferred (no polling/persistence in this pass). Approved. [plan-agent, approved]
- 2026-07-06: Implemented per PLAN.md. Judgment calls: used the plan's suggested substation values verbatim (Northgate 100/62≈62% ok, Millbrook 80/45≈56% ok, Cedar Falls 60/55≈92% warning, Fairview Heights 50/57=114% critical, Riverside Junction 40/36=90% exact boundary/warning); confirmed against the installed `langgraph` (0.6.x, matching the template's unpinned `>=0.2` dependency) that `create_react_agent` takes `prompt=` (not the older `state_modifier=`) for the system prompt; added `from __future__ import annotations` to `mock_substations.py` so the `dict | None` return-type hint from the plan works under the template's `requires-python >=3.9` floor (no local `.venv` existed yet to install and run pytest against — verified with `py_compile` plus a standalone import/exercise of `classify_load`/`get_substation` instead; full agent behavior deferred to the Test gate). [code-agent]

## Active Team
Approved 2026-07-05 — **core-only** (Phase 4 verification run, deliberately drops every optional agent):
- Core (non-droppable): plan-agent, code-agent, test-agent, review-agent, deploy-agent.
- ui-ux-designer: **not applicable** — `agentic-workflow` is API-only, no UI-bearing template component to design for. Not presented as a droppable choice; it's structurally absent.
- Optional (all dropped): functional-agent, industry-expert, solution-architect, security-architect. Their Intake-time KBs (`knowledge/DOMAIN_KB.md`, `knowledge/INDUSTRY_KB.md`) remain on disk per the unconditional-Intake rule, but none of them participate from here forward.

Pipeline for this project is therefore: Intake → Team Composition → Plan & Backlog → Code → Test → Review → Deploy (Experience Design and Architecture gates both skipped — no ui-ux-designer applicable, no architects on roster).

## Test Results
- 2026-07-06: Unit/integration — `pytest`: 1/1 passed (`test_health`). Deterministic `classify_load`/`get_substation` checks confirmed all 5 mock substations classify correctly (ok/warning/critical) and unknown lookups return `None`. [test-agent]
- 2026-07-06: Real behavioral test against the live agent (real Anthropic call, reused already-verified key from grid-assistant with your OK): 5/5 acceptance criteria from PLAN.md passed:
  - Northgate (62%, ok) → no alert, correct.
  - Fairview Heights (114%, critical) → alert warranted, correct, matches `classify_load` exactly.
  - **Riverside Junction (exactly 90.0% boundary)** → correctly classified `warning` (boundary-inclusive `>=` comparison working as designed) — this was the deliberately-planted edge case.
  - Unknown substation → tool was called, returned its `error` field, agent reported "no data" without fabricating numbers.
  - Off-topic question (capital of France) → answered normally, tool was **not** called (trace: `HumanMessage → AIMessage`, no `ToolMessage`) — correctly avoided misfiring the tool, satisfying that acceptance criterion.
  - **Finding (minor, not blocking)**: the system prompt says to "always call `get_substation_load` before answering," but the off-topic case shows the agent correctly *not* calling it — the actual (desired) behavior is more nuanced than the prompt's literal wording. Flagged for review-agent as a prompt-precision nit, not a functional defect (the acceptance criterion it needed to satisfy — don't misfire the tool — passed). [test-agent]
- 2026-07-06: Review gate approved (no changes requested) — decision-intent match confirmed against PLAN.md; the prompt-wording finding turned out to be a mischaracterization by test-agent's summary, not the prompt itself (the actual prompt text already scopes tool-calling to named-substation questions correctly). [review-agent]
- 2026-07-06: Deploy gate — started `uvicorn app.main:app` locally on port 8422, confirmed serving (`GET /health` → 200), ran post-deploy smoke test (`POST /invoke` Cedar Falls query → correct real result, 91.67%/warning/alert-warranted, against the live process). Server stopped cleanly after verification. [deploy-agent, target_env=local]

## Phase 4 verification outcome
Confirmed: all 4 optional SMEs correctly dropped and did not participate past Intake; `ui-ux-designer` and the Experience Design gate were correctly structurally absent (not just declined) for this API-only template; Architecture gate was skipped since no architects were on the roster; the reduced Intake → Team Composition → Plan & Backlog → Code → Test → Review → Deploy pipeline ran cleanly end-to-end with real agent behavior verified against a live Anthropic call, including a deliberately-planted exact-boundary edge case (90.0% → `warning`).

## Current Status
**Deployed (dev, local).** First feature (substation load-check + alert decision) is live end-to-end through the reduced core-only pipeline. Backend port: 8422 (not currently running).
