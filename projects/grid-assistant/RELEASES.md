# Releases: grid-assistant

Structured record of every promotion to `prod/`. For human-readable summaries
see `CHANGELOG.md`. Each entry is tagged in `prod/` as `v<version>` — rollback
via `git -C prod reset --hard <previous-tag>` after explicit human
confirmation.

## v1.0.0 — 2026-07-09

- **Version bump**: baseline (first release; see rationale below)
- **Release branch**: `release/2026-07-09-v1.0.0` (dev/, cut from `main` @ `84cffcc`)
- **Bundled features**:
  - Mock grid-data chatbot (`POST /chat`) — first feature shipped to `dev`,
    commit `2ea432c` (plus follow-up fixes `15f0466`, `2795c9c`).
  - `GET /regions` endpoint — feature branch
    `feature/2026-07-09-regions-endpoint`, merged to `main` at `84cffcc`.
    Status prior to this release: "Ready for Release."
- **Conflict analysis**: N/A — only one feature (`GET /regions`) was in
  "Ready for Release" state; the chatbot feature was already on `main` with
  no separate pending branch to reconcile against. No pairwise conflict
  analysis was performed since there was nothing to conflict with.
- **Dependency-diff check**: confirmed — single `backend/pyproject.toml`,
  linear history (no divergent feature branches touching dependencies
  concurrently). No conflicting version bumps.
- **Full test suite (release branch, dev/backend/.venv, pytest)**: 9/9
  passed (5 chatbot/mock-data + 4 `/regions`), 0 failed.
- **Approver**: human (release train executed by `release-manager` agent on
  explicit request; test-gate and review-gate sign-offs for both bundled
  features are recorded in `PROJECT_CONTEXT.md`'s Decisions Log / Test
  Results prior to this promotion).
- **Promotion**: `prod/` created fresh (`git init`, first release), `dev/`
  added as local remote (`dev-source`), fetched, merged
  `release/2026-07-09-v1.0.0` into `prod`'s `main`
  (`--allow-unrelated-histories`, fast-forward since `prod/main` was
  previously unborn).
- **Prod commit hash**: `84cffcc2a8fb5e116e78ed04e29520c667535910`
- **Tag**: `v1.0.0` (annotated) on the above commit in `prod/`.

### Why v1.0.0, not two separate versions

This is the project's first promotion to `prod/` — there is no prior
released baseline to version against. Rather than inventing a fiction where
the chatbot feature was "v0.x" and `/regions` is "v1.0," both features are
bundled into a single v1.0.0 baseline release, because:

1. **`prod/` has never existed before now.** Semver bumps describe the delta
   from the *previous public release*. With no previous release, there is
   no meaningful "previous version" to bump from for either feature
   individually — inventing one retroactively would be more confusing than
   informative.
2. **Both features are already merged and co-deployed on `dev/main`** at a
   single commit (`84cffcc`); they've been running together in dev, not as
   independently releasable increments. Treating them as two releases would
   imply an ordering/compatibility relationship that doesn't reflect how
   they were actually built or tested.
3. **1.0.0 (not 0.1.0) is the right starting point** because the chatbot
   feature already went through a full gate pipeline (test/review/deploy)
   and was deployed and smoke-tested standalone before `/regions` was even
   started — this is not a rough/experimental first cut warranting a `0.x`
   pre-1.0 designation. It's a working, tested product being promoted to
   `prod/` for the first time, which is exactly what a v1.0.0 baseline
   represents. `0.1.0` would be the more conservative alternative if the
   team wanted to signal "still stabilizing, breaking changes expected
   before 1.0" — that wasn't the case here.

### Rollback
No prior tag exists — v1.0.0 is the first. Rollback for a future release
would be: `git -C prod reset --hard v1.0.0` (after explicit human
confirmation), restoring this baseline.
