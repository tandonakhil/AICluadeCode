# PLAN: `GET /regions` endpoint

## Scope
Enhancement to the deployed `grid-assistant` backend (branch
`feature/2026-07-09-regions-endpoint`). Adds a read-only, deterministic
endpoint that returns the current state of all monitored regions as
structured JSON, for a future dashboard to consume. No LLM call, no user
input, no new external dependencies — this is a thin serialization layer
over the existing `GRID_DATA` dict in `mock_grid_data.py`. This plan
supersedes the prior `PLAN.md` (mock grid-data chatbot feature, already
shipped — see `PROJECT_CONTEXT.md`'s Decisions Log for that history) and
covers only this one feature.

Template/architecture already in place (FastAPI + LangChain `genai-chatbot`
scaffold) is unchanged by this feature; nothing here touches `/chat` or
`llm.py`.

## File/module changes

### `backend/app/mock_grid_data.py`
No changes to `GRID_DATA` or `format_grid_context()`. Both are reused as-is.

### `backend/app/main.py`
1. Add import: change the existing
   `from app.mock_grid_data import format_grid_context` line to
   `from app.mock_grid_data import GRID_DATA, format_grid_context`.
2. Add a new Pydantic response model, `RegionStatus`:
   ```python
   class RegionStatus(BaseModel):
       name: str
       load_percentage: int
       status: str
   ```
3. Add a new endpoint:
   ```python
   @app.get("/regions", response_model=list[RegionStatus])
   def regions():
       return [
           {"name": name, "load_percentage": data["load_percentage"], "status": data["status"]}
           for name, data in GRID_DATA.items()
       ]
   ```
   - Placed after `/health` and before `/chat` for readability (ordering is
     not functionally significant).
   - Synchronous `def`, matching the existing `/health` and `/chat` handler
     style — no `async`, no I/O.

No changes to `frontend/`, `llm.py`, `.env`/`.env.example`, or dependencies
(`pydantic` and `fastapi` are already in use; `list[RegionStatus]` requires
no new package).

## Design decisions
- **New Pydantic response model (`RegionStatus`), not a raw dict return.**
  FastAPI's `response_model` gives automatic OpenAPI schema generation
  (useful for the future dashboard consuming this) and a validation
  guarantee that every region entry has the right shape/types, at
  negligible cost. This matches `ChatRequest`'s existing use of `BaseModel`
  for structure, keeping style consistent within `main.py`.
- **No new module.** Given there's exactly one endpoint and it's a direct
  reshape of `GRID_DATA`, adding a `routers/` package or separate file would
  be premature structure for a template this small. Revisit if/when a
  second non-chat endpoint arrives.
- **List of objects (each including `name`), not a dict keyed by region
  name.** A list is easier for typical frontend table/list rendering and
  avoids the dashboard needing to know region names are dict keys vs. a
  `name` field. Order follows `GRID_DATA`'s insertion order (Python dicts
  preserve insertion order), which is stable given `GRID_DATA` is a static
  literal.
- **No pagination, filtering, or query params.** Out of scope — only 4
  regions exist today, and the mock dataset is static.

## Acceptance criteria (Test gate)

Given the current `GRID_DATA`:
```python
{
    "Northfield": {"load_percentage": 62, "status": "normal"},
    "Sunridge Valley": {"load_percentage": 88, "status": "elevated"},
    "Bay Corridor": {"load_percentage": 45, "status": "normal"},
    "Highland Basin": {"load_percentage": 97, "status": "critical"},
}
```

1. **Status code / method**: `GET /regions` returns HTTP `200`.
2. **Shape**: response body is a JSON array of exactly 4 objects, each with
   exactly the keys `name`, `load_percentage`, `status` (types: `str`,
   `int`, `str`).
3. **Exact expected JSON** (order matches `GRID_DATA` insertion order):
   ```json
   [
     {"name": "Northfield", "load_percentage": 62, "status": "normal"},
     {"name": "Sunridge Valley", "load_percentage": 88, "status": "elevated"},
     {"name": "Bay Corridor", "load_percentage": 45, "status": "normal"},
     {"name": "Highland Basin", "load_percentage": 97, "status": "critical"}
   ]
   ```
4. **No LLM/network dependency**: endpoint must be testable via `TestClient`
   with no `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` set and no network access —
   confirms this stays a pure data-serving endpoint (unlike `/chat`, which
   requires live credentials per `PROJECT_CONTEXT.md`'s prior Test Results).
5. **Determinism**: two consecutive calls to `GET /regions` return
   byte-identical JSON (no randomness, no timestamps).
6. **Regression**: existing `test_smoke.py::test_health` and
   `test_mock_grid_data.py` still pass unchanged — this feature must not
   modify `GRID_DATA` or `format_grid_context()`, and `/chat` behavior is
   untouched.
7. **New test file**: `backend/tests/test_regions.py` should be added
   (mirroring the `test_mock_grid_data.py` pattern) asserting criteria 1–3
   directly against a `TestClient(app)` instance.

## Out of scope
- Any dashboard/frontend consumer of this endpoint.
- Auth/rate-limiting on `/regions` (matches current `/health` and `/chat`,
  which also have none — consistent with the rest of this dev-stage app).
- Swapping `GRID_DATA` for a real data source (tracked separately, per
  `mock_grid_data.py`'s module docstring).
