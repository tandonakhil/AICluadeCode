---
name: cut-release
description: Bundle a project's "Ready for Release" features into a versioned release train and promote to prod/. Owned by release-manager (project-level, distinct from mas-release-manager's platform-level /admin-panel release).
---

# /cut-release

Delegates to `release-manager` (see `.claude/agents/release-manager.md` for
the full procedure — this skill is the thin entry point).

1. Identify the target project. Confirm it has at least one feature in
   "Ready for Release" status in `FEATURES.md` — if none, say so and stop
   (not an error, just nothing to release).
2. Hand off to `release-manager`, which runs, with human approval at each
   numbered checkpoint:
   - Feature selection (which "Ready for Release" items to bundle).
   - Conflict analysis (auto-merge clean features, flag overlapping ones).
   - Conflict resolution, if needed (`code-agent`-assisted, always
     human-approved before applying).
   - Full regression suite on the merged release branch.
   - Semantic version confirmation.
   - Optional dry-run.
   - **Explicit approval before `prod/` promotion** — this is a separate,
     higher-stakes checkpoint from the regression-suite approval.
   - `CHANGELOG.md`/`RELEASES.md` updates, `FEATURES.md` status updates.

## Guardrails

- Never promote to `prod/` without two distinct human approvals (test
  results, then the promotion itself) — never collapse these into one.
- This is a different command from `/admin-panel release`, which cuts a
  *platform* version, not a project release.
