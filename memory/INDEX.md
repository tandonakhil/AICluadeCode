# Project Index

| Project | Template | Stage | Env | Last Updated | Notes |
|---|---|---|---|---|---|
| grid-assistant | genai-chatbot | promoted (prod, v1.0.0) | local | 2026-07-09 | first project through the full lifecycle: pipeline, enhance-agent, and release-manager all verified here |
| policy-lookup-assistant | rag-knowledge-base | deployed (dev, local) | local | 2026-07-05 | Phase 4 full-team verification run — all 5 SMEs engaged, 9-gate pipeline validated end-to-end |
| load-alert-agent | agentic-workflow | promoted (prod, v1.0.0) | local | 2026-07-09 | Phase 4 core-only run + Phase 9 real conflict-resolution verification (2 conflicting features, proximity-conflict fast path proven) |
| little-milestones | genai-chatbot | deployed (dev, local) -- F18 native mobile shipped, post-deploy fix cycle | local | 2026-07-28 | F1-F17 web + **F18 React Native/Expo mobile** (multi-surface). 499 tests green across backend/web/mobile/6 SME suites. 8 loop-backs, 7 human-found. Outstanding: night theme, offline queue. See `PIPELINE_LOG.md` |
| conclave-marketing | custom (marketing site, FastAPI) | deployed (dev, local) | local | 2026-07-17 | All 9 gates complete, F1-F12 MVP shipped; multi-page (Home/Solutions/Contact) at :8100; F13 (real contact address) deferred, human-owned |
| conclave-finance-studio | custom (FastAPI, server-rendered) | gate 10 Review — code items closed, 2 KB escalations routed | dev, local | 2026-08-05 | MVP1 built and runnable at http://127.0.0.1:8030/. 3,037 scenarios, 10 suites, 6 orderings, 0 failures. Gate 9: **256 of 265 VERIFIED, 0 FAILED, 0 CONTRADICTED**; 9 NOT VERIFIED, all overridden by the human 2026-08-05 and named in the Decisions Log. 4 of those 9 were closeable and ship unbuilt (F5 registry id-space gap); 5 are dependency-bound. |
| conclave-dashboard | custom (Flask + Jinja2) | gate 11 of 11 | dev, local | 2026-07-31 | Admin-panel feature: live pipeline dashboard for every project. 11-gate wrapped graph, RAG rollup, `/status` and `/intake` console. 36/36 acceptance criteria verified. |
