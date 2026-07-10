# Features: load-alert-agent

## In Development

- **Substation load-check + alert decision** — replace the placeholder
  `lookup_status` tool with a real (mocked) `get_substation_load` tool over
  a small fictional 5-substation dataset (`app/mock_substations.py`); the
  agent calls the tool, then reports load/status and states whether an
  alert is warranted based on a deterministic threshold classification
  (`classify_load`: ok / warning >=90% / critical >=105%) computed in code,
  not by LLM arithmetic. No real grid integration, no alert delivery
  channel, no hysteresis/dedupe (single stateless `/invoke` call, no
  polling state to debounce). See `PLAN.md` for full design and acceptance
  criteria. Status: planned, not yet built.

## Ready for Release

## Released
