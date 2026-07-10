# Security KB: grid-assistant

> First entry in this file. `grid-assistant` predates Team Composition/SME
> agents, so no security record exists for the original mock grid-data
> chatbot feature. This entry establishes the security posture for the
> project as it stands today (both `/health`+`/chat` already deployed, and
> the new `GET /regions` enhancement), since Authentication & Authorization
> Design must describe the whole surface it applies to, not just the newest
> endpoint in isolation.

## Authentication & Authorization Design

**Decision: no authentication or authorization on any endpoint
(`/health`, `/chat`, `/regions`) at this stage.**

### Criteria evaluated

- **Multi-tenancy?** No. Single-user, single-deployment local app. No
  concept of separate tenants or accounts exists anywhere in the codebase.
- **PII?** No. `GRID_DATA` contains only fictional region names, load
  percentages, and status strings — no user data, no personal data of any
  kind flows through `/chat` or `/regions`.
- **Network exposure beyond localhost?** No, today. `PROJECT_CONTEXT.md`
  confirms current deployment is `uvicorn app.main:app` run locally on port
  8420, started on demand, not behind any reverse proxy or public-facing
  infrastructure. `dev/ROADMAP.md`-adjacent notes (cloud-dev/cloud-prod)
  mark any non-local deployment as explicitly deferred.
- **Deployment target?** Local dev machine only, per
  `PROJECT_CONTEXT.md`'s "Target environment: local (cloud-dev/cloud-prod
  deferred)."
- **Data sensitivity if disclosed?** Low. All data served (mock grid
  regions and their load/status) is fictional/static, checked into the
  repo in plain sight (`mock_grid_data.py`). Disclosure carries no
  confidentiality risk today.
- **Write/mutation surface?** None. `/regions` is read-only (`GET`, no
  body). `/chat` accepts free-text input but only reads `GRID_DATA`; it
  performs no writes, no state mutation, no side effects beyond an LLM call.

### Conclusion

No auth is a reasoned, not asserted, conclusion given all of the above:
single-user, no PII, localhost-only, low-sensitivity static data, no
mutation surface. This matches `PLAN.md`'s "Out of scope: Auth/rate-limiting
on `/regions` (matches current `/health` and `/chat`, which also have none)"
and is consistent with `security-architect`'s guardrail against over-building
enterprise-grade controls for a legitimately low-risk local MVP.

### Revisit triggers

Revisit this decision — do not silently continue under it — when **any** of
the following becomes true:

1. **Any non-local deployment** (cloud-dev, cloud-prod, or anything reachable
   from outside the developer's own machine), even for internal/team-only
   use.
2. **Multi-user support** of any kind (even a shared internal tool with more
   than one person hitting the same running instance).
3. **`GRID_DATA` is swapped for a real data source** (tracked separately per
   `mock_grid_data.py`'s module docstring and noted again below) — real
   operational grid data is a meaningfully different sensitivity class than
   fictional mock data, even though it's still not PII.
4. **A write/mutation endpoint is added** (e.g. anything that could change
   grid configuration, acknowledge alerts, trigger actions) — read-only-only
   no-auth reasoning does not extend to mutation.
5. **The future dashboard consumer (`PLAN.md`'s stated audience for
   `/regions`) is built and exposed anywhere other than the same localhost
   as the backend.**

## Endpoint-specific notes

### `GET /regions`

Reviewed for input-validation and information-disclosure risk despite
having no request parameters (no query string, no path params, no body):

- **No input validation surface exists** — there is nothing to validate.
  This isn't a gap, just a consequence of the endpoint's shape; noted for
  completeness rather than as a finding.
- **Information disclosure is not risk-free by default, only risk-free
  *given current exposure*.** The endpoint returns the full contents of
  `GRID_DATA` unconditionally to any caller who can reach it — there's no
  partial-response or per-caller filtering logic. Today that's fine because
  (a) the data is fictional and already public in the repo, and (b) the only
  caller who can reach it is the local developer. **The moment this endpoint
  is exposed beyond localhost, or `GRID_DATA` is swapped for real grid data,
  "returns everything to anyone who asks" becomes a genuine information
  disclosure concern** (real infrastructure load/status data is the kind of
  operational detail that's normally treated as sensitive — even without
  being PII, it's useful reconnaissance for anyone probing grid
  infrastructure). This is the same trigger as #3 above, called out
  separately here because it's specifically about `/regions`'s
  unconditional-full-dump response shape rather than auth in general —
  fixing it later means adding response filtering, not just auth.
- **Determinism is a security non-issue here**, not just a correctness
  property — no randomness/timestamps means no risk of leaking
  server-internal state (clock, request counters, etc.) through response
  variance.
- **Matches `PLAN.md`'s acceptance criterion 4** (testable via `TestClient`
  with no API keys, no network access) — confirms `/regions` genuinely has
  no external dependency that could itself become an attack surface (unlike
  `/chat`, which calls out to an LLM provider).

### `POST /chat` (pre-existing, noted for completeness)

Not in scope for this enhancement's code changes, but since this is the
first `SECURITY_KB.md` entry it's worth recording: `/chat` accepts
free-text user input and forwards it to an LLM (`SystemMessage` +
`HumanMessage`). No input validation/sanitization beyond Pydantic's
`str` type check exists today. This is a reasonable no-auth posture under
the same criteria above, but is a distinct risk class from `/regions`
(prompt injection / LLM-directed input) that falls more naturally under
`responsible-ai-architect`'s guardrail lens than this KB's authn/authz
scope — flagged here only so the boundary between the two KBs is explicit.

## Secrets handling

Confirmed (re-verified for this enhancement, no change from prior state):

- `dev/backend/.env` exists locally, holding `ANTHROPIC_API_KEY`/
  `OPENAI_API_KEY`; `dev/.gitignore` excludes `.env*` while explicitly
  allowlisting `.env.example`/`backend/.env.example` — API keys are not at
  risk of being committed.
- `GET /regions` introduces no new secrets, credentials, or configuration —
  it reads only the static, already-committed `GRID_DATA` dict. No secrets
  handling changes required for this enhancement.

## Decisions Log (this file)

- 2026-07-09: First `SECURITY_KB.md` entry. No-auth posture confirmed for
  `/health`, `/chat`, and the new `/regions` endpoint, with explicit
  criteria and revisit triggers (see above). Flagged (not blocking):
  `/regions`'s unconditional full-dataset response becomes an information
  disclosure concern the moment it's exposed beyond localhost or backed by
  real grid data — response filtering, not just auth, would be needed at
  that point. [security-architect]
