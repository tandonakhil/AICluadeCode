# Changelog: grid-assistant

All notable changes to this project are documented in this file.

## [1.0.0] - 2026-07-09

First release. Establishes the v1.0.0 baseline by promoting everything
currently on `dev/main` to `prod/` in one bundle (see `RELEASES.md` for the
full structured record and rationale on why this ships as v1.0.0 rather than
versioning the two features separately).

### Added
- **Mock grid-data chatbot** (`POST /chat`): FastAPI + LangChain backend that
  answers questions about 4 fictional grid regions (Northfield, Sunridge
  Valley, Bay Corridor, Highland Basin) by injecting a static `GRID_DATA`
  dict into the system prompt. Refuses to fabricate data for regions it
  doesn't have. Streamed text response via `model.stream(...)`.
- **`GET /regions` endpoint**: read-only, deterministic JSON endpoint
  returning all 4 monitored regions with `name`, `load_percentage`, and
  `status`, for a future dashboard to consume. Pure reshape of the existing
  `GRID_DATA` dict — no new dependencies, no LLM/network call required.

### Fixed
- `main.py` now calls `load_dotenv()` so `.env` is picked up automatically
  (previously required manually exporting env vars to run the app).

### Changed
- Relaxed `requires-python` from `>=3.11` to `>=3.9` (no functional reason
  for the higher floor; verified working on 3.9.6).
- Widened `.gitignore`'s `.env` pattern to also catch `.env.local` variants.

### Notes
- No authentication/rate-limiting on any endpoint — matches this app's
  current dev-stage posture (localhost-only, fictional data). Tracked as a
  known gap, not a regression.
- Full backend test suite: **9/9 passing** (5 for the chatbot/mock-data
  feature, 4 for `/regions`) on the release branch prior to promotion.
