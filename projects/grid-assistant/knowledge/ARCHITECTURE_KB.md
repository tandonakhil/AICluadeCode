# Architecture KB: grid-assistant

> First entry in this file. `grid-assistant` predates Team Composition/SME
> agents, so no architecture record exists for the original mock grid-data
> chatbot feature (see `PROJECT_CONTEXT.md`'s Decisions Log and the
> now-superseded `PLAN.md` history for that). This entry covers only the
> `GET /regions` enhancement (`feature/2026-07-09-regions-endpoint`) — it is
> not a retroactive architecture doc for the whole project.

## Feature: `GET /regions` endpoint

### Design

- **Shape**: one new Pydantic response model (`RegionStatus`: `name: str`,
  `load_percentage: int`, `status: str`) plus one new synchronous endpoint
  function (`GET /regions`, `response_model=list[RegionStatus]`), added
  directly to `backend/app/main.py`. No new module, no new file.
- **Data source**: reuses `GRID_DATA` from `backend/app/mock_grid_data.py`
  unchanged — a direct reshape (dict → list of typed objects), no new
  computation, no I/O.
- **Consistency with existing style**: matches `ChatRequest`'s existing use
  of `BaseModel` for request/response shape, and `/health`'s/`/chat`'s
  synchronous `def` handler style (no `async`, since there's no I/O to await).

### Assessment: is a new Pydantic model + one endpoint the right shape?

Yes, for the current scale (1 endpoint, 4 static regions, single file). Three
things worth confirming as this feature graduates beyond MVP:

1. **`response_model` is correct, not just convenient.** It buys automatic
   OpenAPI schema generation and a real validation guarantee — if `GRID_DATA`
   ever gets a malformed entry (wrong type, missing key), FastAPI raises a
   500 with a clear validation error instead of silently serializing garbage.
   That is the right failure mode for a contract a dashboard will depend on.
2. **No new module is right-sized for one endpoint, but is the first
   deferred-structure trigger.** `PLAN.md` explicitly defers a `routers/`
   package until a second non-chat endpoint arrives. Flagging that trigger
   here so the next enhancement doesn't have to rediscover it: if a second
   data-serving endpoint (e.g. `/regions/{name}` or `/alerts`) is added,
   split `main.py` into routers at that point rather than letting a single
   file accumulate unrelated endpoint families.
3. **List-of-objects-with-`name`, not dict-keyed-by-name, is the right
   contract shape for a dashboard consumer** — it's directly renderable as a
   table/list without the frontend needing to know region names double as
   dict keys, and it's the more idiomatic REST collection shape.

### Contract/versioning considerations for the future dashboard consumer

- **No versioning scheme exists yet** (no `/v1/` prefix, no schema version
  field). This is fine for a single first-party consumer during active
  development, but is a real gap the moment `/regions`'s shape needs to
  change after a dashboard is built against it. Recommend: if/when a
  breaking shape change is needed post-dashboard-launch (e.g. renaming
  `load_percentage`, adding required fields), either add a new field as
  *optional* first, or introduce path versioning at that point — don't
  silently break the existing shape.
- **`status` is an unconstrained `str`, not an enum/`Literal`.** Today
  `GRID_DATA` only produces `"normal"`, `"elevated"`, `"critical"`, but
  nothing in the type system enforces that closed set. A dashboard consumer
  will likely branch UI behavior (color, icon) on this field's exact values.
  Recommend tightening to `Literal["normal", "elevated", "critical"]` (or an
  `Enum`) the next time this endpoint is touched — cheap now, and it turns
  "dashboard silently fails to color an unrecognized status string" into a
  caught-at-serialization-time error instead, consistent with the
  `response_model` validation guarantee already chosen above. Not blocking
  for this PLAN's scope (out-of-scope items already exclude data-source
  swaps), but worth a backlog note.
- **No pagination/filtering is a reasonable now-decision, not a
  contract risk** — with 4 static regions this is correctly deferred per
  `PLAN.md`. If the region count grows meaningfully (real data source,
  dozens of regions), revisit before that data source swap, not before.

### Other technical considerations

- **Determinism/statelessness**: confirmed by design — no randomness, no
  timestamps, no shared mutable state touched by this handler. Matches
  `PLAN.md`'s acceptance criterion 5 directly; nothing else to add.
- **No coupling introduced to `/chat` or `llm.py`**: confirmed by reading
  `main.py` — the new endpoint imports only `GRID_DATA` (a new import
  alongside the existing `format_grid_context` import) and does not touch
  the LLM path. Consistent with `PLAN.md`'s stated scope.

## Decisions Log (this file)

- 2026-07-09: First `ARCHITECTURE_KB.md` entry, scoped to the `GET /regions`
  enhancement. Design approved as proposed in `PLAN.md`: new `RegionStatus`
  Pydantic model + one endpoint in `main.py`, no new module. Flagged for
  future revisit (not blocking): tighten `status` to a `Literal`/`Enum`, and
  introduce API versioning before any breaking shape change once a real
  dashboard consumer exists. [solution-architect]
