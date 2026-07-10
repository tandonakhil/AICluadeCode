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

## Placeholders filled in at project-creation time

- `{{PROJECT_NAME}}`, `{{PROJECT_DESCRIPTION}}` — in `README.md.tmpl`.
- `{BACKEND_PORT}`, `{FRONTEND_PORT}` — assigned by deploy-agent, recorded in
  `PROJECT_CONTEXT.md`.
- `LLM_PROVIDER`, `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` — in `.env`, never
  committed (see `.gitignore`).
