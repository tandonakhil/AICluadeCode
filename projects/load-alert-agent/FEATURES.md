# Features: load-alert-agent

## In Development

## Ready for Release

## Released

- **feature/2026-07-09-list-substation-names** — adds `get_all_substation_names()`
  helper to `mock_substations.py`. Independent of any other feature's logic.
  Released in v1.0.0 (2026-07-09).
- **feature/2026-07-09-critical-substations-filter** — adds
  `get_critical_substations()` filter to `mock_substations.py`. Independent
  of any other feature's logic. Bundled with `list-substation-names` in the
  same release train; both append near the end of the same file, producing
  a real proximity conflict (confirmed via git merge) resolved by keeping
  both functions. Released in v1.0.0 (2026-07-09).

- **Substation load-check + alert decision** — replaced the placeholder
  `lookup_status` tool with a real (mocked) `get_substation_load` tool over
  a fictional 5-substation dataset; the agent calls the tool, then reports
  load/status and states whether an alert is warranted based on a
  deterministic threshold classification (`classify_load`: ok / warning
  >=90% / critical >=105%) computed in code, not by LLM arithmetic. Live
  since Phase 4 (2026-07-06). See `PLAN.md` for full design/acceptance
  criteria and `PROJECT_CONTEXT.md` for deploy history.
