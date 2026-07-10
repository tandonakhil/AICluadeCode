# Template: rag-knowledge-base

## When plan-agent should pick this template

A question-answering application grounded in a document corpus — the answer
must be retrieved from and cited against real documents, not just conversed
about generically (that's `genai-chatbot`) and not a tool-using automation
task (that's `agentic-workflow`).

## Shape

- `backend/` — FastAPI + LangChain RAG chain + Chroma (embedded, local
  persistence — no external vector DB service needed).
- `frontend/` — Next.js (App Router) + TypeScript + Tailwind + shadcn/ui +
  Vercel AI SDK, same shape as `genai-chatbot`'s chat UI.
- `backend/data/sample_docs/` — a couple of sample documents so the template
  is ingestible and testable out of the box; code-agent replaces these with
  the project's real corpus per the approved plan.

## Run commands

- Ingest (one-time or on-demand): `cd backend && python -m app.ingest`
- Backend: `cd backend && uvicorn app.main:app --reload --port {BACKEND_PORT}`
- Frontend: `cd frontend && npm run dev -- --port {FRONTEND_PORT}`

## Smoke test definition

1. Backend: `GET /health` → `200 OK`.
2. Ingest the sample docs, then `POST /ask` with a question answerable from
   them → `200 OK` with a non-empty answer that cites which source
   document(s) it drew from.
3. Frontend (Playwright, once UI is customized): load the page, ask a
   question, assert a grounded answer with a citation renders.

## Placeholders filled in at project-creation time

- `{{PROJECT_NAME}}`, `{{PROJECT_DESCRIPTION}}` — in `README.md.tmpl`.
- `{BACKEND_PORT}`, `{FRONTEND_PORT}` — assigned by deploy-agent.
- `LLM_PROVIDER`, `ANTHROPIC_API_KEY` / `OPENAI_API_KEY` — in `.env`.
- `backend/data/sample_docs/` — swapped for the project's real corpus.

## Verification status (as of template creation)

Structural checks passed without a real key: `GET /health`, document loading
(2 sample docs), and text-splitting (5 chunks) all verified deterministically.
The full ingest → embed → retrieve → grounded-answer flow requires a real
`OPENAI_API_KEY` and has **not yet been verified end-to-end** — do this the
first time a real project is built from this template, the same way
`genai-chatbot`'s behavioral criteria were verified in Phase 2.

