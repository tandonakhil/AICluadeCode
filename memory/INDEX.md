# Project Index

| Project | Template | Stage | Env | Last Updated | Notes |
|---|---|---|---|---|---|
| grid-assistant | genai-chatbot | promoted (prod, v1.0.0) | local | 2026-07-09 | first project through the full lifecycle: pipeline, enhance-agent, and release-manager all verified here |
| policy-lookup-assistant | rag-knowledge-base | deployed (dev, local) | local | 2026-07-05 | Phase 4 full-team verification run — all 5 SMEs engaged, 9-gate pipeline validated end-to-end |
| load-alert-agent | agentic-workflow | promoted (prod, v1.0.0) | local | 2026-07-09 | Phase 4 core-only run + Phase 9 real conflict-resolution verification (2 conflicting features, proximity-conflict fast path proven) |
| little-milestones | genai-chatbot | deployed (dev, local) -- F18 native mobile shipped, post-deploy fix cycle | local | 2026-07-28 | F1-F17 web + **F18 React Native/Expo mobile** (multi-surface). 499 tests green across backend/web/mobile/6 SME suites. 8 loop-backs, 7 human-found. Outstanding: night theme, offline queue. See `PIPELINE_LOG.md` |
| conclave-marketing | custom (marketing site, FastAPI) | deployed (dev, local) | local | 2026-07-17 | All 9 gates complete, F1-F12 MVP shipped; multi-page (Home/Solutions/Contact) at :8100; F13 (real contact address) deferred, human-owned |
| conclave-finance-studio | custom (FastAPI, server-rendered) | **MVP1 complete — all 11 gates** | dev, local | 2026-08-06 | Runnable at http://127.0.0.1:8030/. 3,158 scenarios, 12 suites, 6 orderings, 0 failures. 256/265 criteria verified; 9 overridden by the human 2026-08-05 and named individually. 26 code passes, 6 gate-8 loop-backs, 2 gate-9 blocks — none a failing test. Current Status change to `deployed` awaits the human. |
| conclave-dashboard | custom (Flask + Jinja2) | gate 11 of 11 | dev, local | 2026-07-31 | Admin-panel feature: live pipeline dashboard for every project. 11-gate wrapped graph, RAG rollup, `/status` and `/intake` console. 36/36 acceptance criteria verified. |
