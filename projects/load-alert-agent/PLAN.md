# PLAN.md — load-alert-agent

## Feature

Replace the template's placeholder `lookup_status` tool with a real (mocked)
substation load-lookup tool, and have the agent decide whether a load-alert
is warranted based on that data. This is the first real feature for this
project and the only one in scope for this pass — this is a Phase 4
core-only verification run (no functional-agent/industry-expert formally
consulting), similar in spirit and size to `grid-assistant`'s Phase 2
mock-data feature: prove the pipeline end to end with a small fictional
dataset, not build a production grid-monitoring system.

## Template fit (confirmed, not re-decided)

`agentic-workflow` (FastAPI + LangGraph, API-only) is the right fit per its
own manifest: "given a region, look up its status and decide whether to
raise an alert" is the exact worked example in
`dev/TEMPLATE_MANIFEST.md`. Unlike `genai-chatbot`'s context-injection
pattern (used for grid-assistant), this template's shape is a tool-using
`create_react_agent` — so this feature is implemented as a real tool call,
not a system-prompt data dump. That distinction is deliberate and matches
what each template is for.

## Goal for this pass

Prove the pipeline end to end: caller POSTs a substation name (in natural
language) to `/invoke` → agent calls the load-lookup tool → tool returns
structured load data plus a deterministic status classification → agent
composes a final answer that states the load, cites the status, and raises
or does not raise an alert accordingly → agent gracefully declines for
substations not in the mock dataset. No real grid/SCADA integration, no
persistence, no polling/repeated-invocation state, no auth.

## Grounding from the (informal) KBs

`knowledge/DOMAIN_KB.md` and `knowledge/INDUSTRY_KB.md` exist from Intake
but no functional-agent/industry-expert is on this project's roster, so
they're read here only for grounding, not as a formal sign-off. Two points
from them shape this plan directly:

- DOMAIN_KB's alarm-flooding/chattering/hysteresis material is real and
  correct for a production alerting system, but it's about behavior across
  *repeated* evaluations over time (a value oscillating near a threshold
  across polling cycles). This project's `/invoke` is a single stateless
  request/response with no polling loop and no persisted alarm state —
  there is nothing to chatter or flood *yet*. Building hysteresis/debounce
  now would be solving a problem this pass has no state to exhibit.
  Explicitly deferred; flagged as a follow-up below, not built.
- INDUSTRY_KB's framing — AI as auditable decision-support, not autonomous
  control, and alerts should be traceable/explainable — is directly
  actionable at this scale and shapes the alert-decision design below (see
  "Design decisions," #1). It costs nothing extra to build it this way from
  the start.

## File / module changes

### New: `dev/backend/app/mock_substations.py`

- `SUBSTATIONS: dict[str, dict]` — 5 fictional substations, keyed by name.
  Each entry has `rated_capacity_mw` (float) and `current_load_mw` (float).
  Suggested (code-agent may rename, count/shape must match):
  - `"Northgate Substation"`: rated 100, current 62 → ~62% (ok)
  - `"Millbrook Substation"`: rated 80, current 45 → ~56% (ok)
  - `"Cedar Falls Substation"`: rated 60, current 55 → ~92% (warning)
  - `"Fairview Heights Substation"`: rated 50, current 57 → 114% (critical)
  - `"Riverside Junction Substation"`: rated 40, current 36 → exactly 90%
    (boundary edge case — sits exactly on the warning threshold)
- `WARNING_THRESHOLD_PCT = 90` and `CRITICAL_THRESHOLD_PCT = 105` as
  module-level constants (not magic numbers inline), loosely anchored to
  DOMAIN_KB's "sustained loading above ~90-105% of nameplate" note, but not
  claimed as engineering-validated figures — this is mock data for pipeline
  verification, not a real utility's actual operating limits.
- `classify_load(load_percent: float) -> str` — pure function, returns
  `"critical"` if `load_percent >= CRITICAL_THRESHOLD_PCT`, `"warning"` if
  `>= WARNING_THRESHOLD_PCT`, else `"ok"`. No I/O, fully deterministic,
  independently unit-testable.
- `get_substation(name: str) -> dict | None` — case-insensitive lookup by
  name against `SUBSTATIONS`; returns `None` if not found (the tool wrapper
  turns that into a "no data for this substation" message, it does not
  raise/crash).

### Modify: `dev/backend/app/graph.py`

- Remove `lookup_status`. Add:

  ```python
  @tool
  def get_substation_load(substation_name: str) -> dict:
      """Look up current load data for a named substation from the mock
      dataset. Returns rated capacity, current load, load percentage, and a
      deterministic status ("ok" | "warning" | "critical"). Returns an
      error field if the substation name is not in the mock dataset — do
      not guess or invent data for unlisted substations."""
      ...
  ```

  The tool's return value is a small dict (not a formatted string) so the
  model receives structured fields (`load_percent`, `status`) it can quote
  directly rather than re-deriving from prose. `create_react_agent` handles
  dict-returning tools by JSON-serializing the ToolMessage content, which is
  fine for this scale.
- Add a system prompt (via `create_react_agent`'s `prompt=` /
  `state_modifier` argument — code-agent confirms exact param name against
  the installed `langgraph` version) instructing the agent to:
  1. Always call `get_substation_load` before answering a load/status
     question about a named substation — never answer from memory.
  2. Treat the tool's `status` field as authoritative for whether to raise
     an alert: `"warning"` or `"critical"` → the response must explicitly
     say an alert is warranted and state which threshold was crossed;
     `"ok"` → explicitly say no alert is warranted.
  3. State the substation name, current load, rated capacity, load
     percentage, and status in the answer (the "explain-the-alert" shape
     INDUSTRY_KB's backlog suggestion #1 points at) — not just a bare
     yes/no.
  4. If the tool reports no data for the requested substation, say so
     plainly and must not fabricate numbers.
- `build_agent()` and `run_agent()` keep their existing signatures and
  return shape (`{"final_answer": ..., "trace": [...]}"`) — `main.py`'s
  `/invoke` contract is unaffected.

### Not changed in this pass

- `dev/backend/app/main.py` — request/response shape unchanged.
- `dev/backend/app/llm.py` — provider selection is orthogonal to this
  feature.
- No new dependencies — the mock module is pure Python, no new packages.

## Design decisions and trade-offs

1. **Threshold classification is a deterministic code function
   (`classify_load`); the LLM does not compute or decide the status.** The
   LLM's role is to call the tool, read the `status` field, and *compose*
   the alert/no-alert response and its explanation — not to do the
   percentage math or threshold comparison itself. Justification: an
   alerting decision is exactly the kind of thing INDUSTRY_KB flags as
   needing to be auditable/traceable ("why did this fire"), and a
   deterministic function is trivially auditable and unit-testable, whereas
   asking an LLM to compare two floats and decide is strictly worse on
   correctness (occasional arithmetic slips, threshold-adjacent ambiguity)
   for zero upside — nothing here needs the LLM's judgment. Trade-off: this
   is deliberately more rigid than "let the model reason holistically about
   whether this is really alert-worthy" (e.g. no accounting for trend,
   phase imbalance, or cooling-stage escalation per DOMAIN_KB) — acceptable
   because those richer signals don't exist in this mock dataset at all;
   revisit if/when the mock data grows those fields.
2. **A real tool call, not context injection.** This template's intended
   shape (per its own manifest) is a tool-using agent that decides *when*
   to look something up, unlike `genai-chatbot`'s always-present system
   context. With 5 substations this is still small enough that
   context-injection would technically work, but it would exercise the
   wrong pattern for this template and wouldn't verify the
   `create_react_agent` + tool-node wiring this template exists to provide.
3. **Structured dict return from the tool, not a formatted string.**
   Keeps the numeric fields (`load_percent`, `status`) unambiguous in the
   tool trace, which both the model and the Test gate's trace inspection
   can check exactly, rather than parsing them back out of prose.
4. **No hysteresis/debounce/alert-dedupe logic.** DOMAIN_KB is correct that
   production alerting needs this, but it applies to state carried across
   repeated evaluations (a polling loop or persisted alarm state), which
   this stateless single-request template doesn't have. Building it now
   would add complexity with no way to exercise or test it. Flagged as an
   explicit follow-up for `PROJECT_CONTEXT.md`'s backlog if/when this
   project grows a polling or persistence layer.
5. **Boundary case included in the mock data on purpose.** Riverside
   Junction sits at exactly 90% (the warning threshold) to give the Test
   gate a concrete `>=` boundary check, rather than only testing clearly-ok
   and clearly-critical cases.
6. **No new alert/notification channel.** "Raise an alert" means the
   `/invoke` response text says an alert is warranted and why — there is no
   email/Slack/webhook side-effect in this pass. Out of scope; the template
   is a one-shot API invocation, and no delivery mechanism was requested.

## Acceptance criteria (Test gate)

Functional / wiring:
- `GET /health` still returns `200 {"status": "ok"}` (unchanged).
- `dev/backend/app/mock_substations.py` exists, exports `SUBSTATIONS` with
  exactly 5 entries each having `rated_capacity_mw` and `current_load_mw`,
  exports `classify_load()`, and exports `get_substation()`.
- `classify_load()` unit-checkable directly: `classify_load(62)` → `"ok"`,
  `classify_load(90)` → `"warning"` (boundary is inclusive), `classify_load(105)`
  → `"critical"` (boundary is inclusive), `classify_load(104.9)` →
  `"warning"`.
- `get_substation_load` tool is registered on the agent in place of
  `lookup_status` (`lookup_status` no longer exists in `graph.py`).
- `POST /invoke` with a substation question still returns `200` with the
  existing `{"final_answer": ..., "trace": [...]}` shape.

Behavioral (checked via example `/invoke` calls, inspecting both
`final_answer` and `trace`):
- Input: "What's the load on Northgate Substation?" → trace shows a call to
  `get_substation_load` with `substation_name` resolving to Northgate;
  `final_answer` states ~62% load and says no alert / status ok (values
  must match `mock_substations.py`, not be invented).
- Input: "Is Cedar Falls Substation okay?" → trace shows a tool call;
  `final_answer` reports ~92% load, explicitly states this crosses the
  warning threshold, and explicitly says an alert is warranted.
- Input: "Check Fairview Heights Substation" → `final_answer` reports
  ~114% load, explicitly labels it critical, and explicitly says an alert
  is warranted (this is the clearest alert-worthy case).
- Input: "How's Riverside Junction Substation doing?" (exactly 90%, the
  boundary) → `final_answer` reports 90% and classifies it as warning
  (inclusive boundary), not "ok" — this specifically checks the
  `classify_load` boundary is honored end-to-end through the agent, not
  just in the unit function.
- Input: "What's the load at Ashford Substation?" (name not in mock
  dataset) → trace shows a tool call that returns no-data; `final_answer`
  clearly states it has no data for that substation and does not fabricate
  a load percentage or status.
- Input unrelated to substations (e.g. "What's the capital of France?") →
  model may answer normally or note it's scoped to substation load
  queries; must not call the tool with a nonsense argument or claim
  substation data covers the question. (Loose check, confirms the system
  prompt doesn't break general reasoning.)

Out of scope for this Test gate (do not fail the build on these):
- Any real SCADA/grid API connectivity.
- Alert delivery (email/Slack/webhook) — response text only.
- Hysteresis, alarm-flood suppression, or dedupe across repeated calls.
- Trend/rate-of-change, phase imbalance, or cooling-stage signals (not in
  the mock dataset).
- Performance/latency of the LLM call.

## Follow-ups (not built this pass — for `PROJECT_CONTEXT.md` backlog)

- Persisted alarm state + hysteresis/dedupe, if this project grows a
  polling loop or repeated-invocation use case (DOMAIN_KB).
- Trend/duration-aware classification instead of instantaneous
  threshold-only (DOMAIN_KB).
- Incident-history lookup ("has this substation alarmed before")
  (INDUSTRY_KB suggestion #3) — would need a second mock data source.
