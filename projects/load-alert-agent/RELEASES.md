# Releases: load-alert-agent

## v1.0.0 — 2026-07-09

- **This is load-alert-agent's first promotion to `prod/`** — bundles the
  full contents of `dev/main` as the baseline, same reasoning as
  `grid-assistant`'s own v1.0.0 (no prior release to version against; this
  app already went through a full gate pipeline and was deployed/smoke-tested
  before this promotion, so it warrants a 1.0.0 baseline, not a 0.x pre-release).
- **Bundled features**:
  - Substation load-check + alert decision (Phase 4, 2026-07-06 — the
    original `/invoke` feature, already deployed to `dev` before this
    project ever cut a release)
  - `feature/2026-07-09-list-substation-names`
  - `feature/2026-07-09-critical-substations-filter`
- **Release branch**: `release/2026-07-09-v1.0.0` (dev/)
- **Conflicts resolved**: 1 proximity conflict in `backend/app/mock_substations.py`
  (both new-feature branches appended a distinct, independently-named
  function near the end of the same file; no shared logic). Resolution: kept
  both `get_all_substation_names()` and `get_critical_substations()`.
  Resolved via the automated-triage fast path; lightweight human confirm
  simulated for this scripted verification run.
- **Tests**: `pytest` — 1 passed (existing smoke test suite; no
  feature-specific unit tests present in this repo for the two new
  functions). Additional manual functional check: both new functions
  imported and called together against the mock dataset, results
  cross-validated against `classify_load` — consistent.
- **Semver**: v1.0.0 baseline (first release, not a bump from anything).
- **Approver**: tandonakhil@gmail.com (simulated lightweight confirm, scripted
  verification run)
- **Prod commit**: `7cf253210922588f18e40012fa90d2352452a3c6` (tag `v1.0.0`)
