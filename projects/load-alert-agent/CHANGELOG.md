# Changelog: load-alert-agent

## v1.0.0 — 2026-07-09

### Added
- `get_all_substation_names()` in `mock_substations.py` — returns every known
  substation name. (`feature/2026-07-09-list-substation-names`)
- `get_critical_substations()` in `mock_substations.py` — returns substation
  names currently classified as `critical` per the existing `classify_load`
  threshold logic. (`feature/2026-07-09-critical-substations-filter`)

### Notes
- Both features touched the end of the same file (`mock_substations.py`) and
  produced a real git merge conflict when combined. Classified as a
  **proximity conflict**: each feature adds an independently-named function
  with no shared logic or overlapping lines — resolution kept both
  functions, unmodified from their source branches.
