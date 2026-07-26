# Template: genai-chatbot

## When plan-agent should pick this template

A conversational, chat-first application where a user talks to an LLM,
optionally with tool use — no document corpus to ground answers in (that's
`rag-knowledge-base`), and a human-facing UI is required (an API-only agent
belongs in `agentic-workflow`).

## Shape

- `backend/` — FastAPI + LangChain, calls Anthropic or OpenAI depending on
  `LLM_PROVIDER` in `.env`.
- `frontend/` — Next.js (App Router) + TypeScript + Tailwind + shadcn/ui +
  Vercel AI SDK, streaming chat UI.

## Run commands

- Backend: `cd backend && uvicorn app.main:app --reload --port {BACKEND_PORT}`
- Frontend: `cd frontend && npm run dev -- --port {FRONTEND_PORT}`

## Smoke test definition

1. Backend: `GET /health` → `200 OK`.
2. Backend: `POST /chat` with `{"message": "hello"}` → streamed response body
   is non-empty.
3. Frontend (Playwright, once UI is customized past the placeholder): load the
   page, type a message, assert a response renders.

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
- `{BACKEND_PORT}`, `{FRONTEND_PORT}` — assigned by deploy-agent, recorded in
  `PROJECT_CONTEXT.md`.
- `LLM_PROVIDER`, `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` — in `.env`, never
  committed (see `.gitignore`).
