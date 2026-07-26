# Template: agentic-workflow

## When plan-agent should pick this template

A multi-step, tool-using agent invoked programmatically (API-first) — no
human-facing chat UI required (that's `genai-chatbot`), and no document corpus
to ground answers in (that's `rag-knowledge-base`). Good fit for backend
automation: e.g. "given a region, look up its status and decide whether to
raise an alert."

## Shape

- `backend/` only — FastAPI + LangGraph. No `frontend/`; `ui-ux-designer` and
  the Experience Design gate are not applicable to this template (see
  `admin/MAS_REGISTRY.md`).

## Run commands

- Backend: `cd backend && uvicorn app.main:app --reload --port {BACKEND_PORT}`

## Smoke test definition

1. `GET /health` → `200 OK`.
2. `POST /invoke` with a sample input → `200 OK` with a structured response
   containing the agent's tool-call trace and final answer (exact shape
   depends on what the project's graph does — the acceptance criteria for
   each project's actual graph are defined in that project's `PLAN.md`).

There is no frontend smoke test for this template — deploy-agent's per-template
branching treats a project built from this template as "one-shot API
invocation," not "long-running UI to click through."

## SME test suites (executable)

Each SME-owned suite has a runnable entry point at
`tests/suites/<suite>/run.sh`, invoked by its owning agent (scoped `Bash`) and
aggregated by `test-agent`. See `tests/suites/README.md` for the full
convention and the owner of each suite.

Exit codes are meaningful and `test-agent` maps them directly:
`0` executed+passed · `1` executed+failed · `3` **no scenarios defined (not a
pass)** · `4` cannot execute (report STATIC-ONLY).

`code-agent` authors/extends these entry points at the Code gate for whichever
suites are active on the project.

### Rendered-UI verification (the `ux` suite)

`tests/suites/harness/browser.py` provides a Playwright-backed helper for
asserting on what actually renders — composited opacity, computed styles,
horizontal overflow, visible text, and screenshots into `test-evidence/` —
rather than on HTML source.

Setup (once per project, only if the `ux` suite uses rendered checks):

```sh
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
```

Process-lifecycle rule: a browser or server started inside a subagent's turn
dies with that turn. The harness drives Playwright synchronously in a single
invocation; any long-lived app server must already be started by
`deploy-agent` or the orchestrator. If Playwright is absent the harness reports
STATIC-ONLY rather than failing — an honest "could not verify" beats a false
pass.

## Placeholders filled in at project-creation time

- `{{PROJECT_NAME}}`, `{{PROJECT_DESCRIPTION}}` — in `README.md.tmpl`.
- `{BACKEND_PORT}` — assigned by deploy-agent, recorded in `PROJECT_CONTEXT.md`.
- `LLM_PROVIDER`, `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` — in `.env`.
- The placeholder tool in `app/graph.py` (`lookup_status`) is a stand-in —
  `code-agent` replaces it with the project's real tool(s) per the approved
  plan; the graph wiring pattern (StateGraph with a tool node) stays.
