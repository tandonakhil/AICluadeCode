# Features: grid-assistant

## In Development

## Ready for Release

## Released

- **v1.0.0** (2026-07-09) — first promotion to `prod/`. Bundles the full
  contents of `dev/main` @ `84cffcc` as a single baseline release (see
  `RELEASES.md` for why these ship together rather than as two versions):
  - Mock grid-data chatbot (`POST /chat`) — first feature shipped to `dev`
    (commit `2ea432c`, plus fixes `15f0466`, `2795c9c`). Previously listed
    here only implicitly via `PROJECT_CONTEXT.md`; now formally recorded as
    released with `v1.0.0`.
  - **feature/2026-07-09-regions-endpoint** — `GET /regions` endpoint
    listing all monitored regions with current status, for a future
    dashboard. Merged to `main` (`84cffcc`), deployed locally,
    smoke-tested against the live process. [enhance-agent]

  Promoted via `release/2026-07-09-v1.0.0`, tagged `v1.0.0` in `prod/` at
  commit `84cffcc2a8fb5e116e78ed04e29520c667535910`. See `CHANGELOG.md` and
  `RELEASES.md` for full details.
