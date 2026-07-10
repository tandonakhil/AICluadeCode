---
name: modify-feature
description: Correct or adjust a feature that's already in development or already shipped — a lighter-weight mode of enhance-agent, not a separate owner. Targets an existing FEATURES.md entry rather than proposing something new.
---

# /modify-feature

Delegates to `enhance-agent` (see `.claude/agents/enhance-agent.md`'s
"`/modify-feature`" section — this skill is the thin entry point).

1. Identify the target project and the existing `FEATURES.md` entry to
   correct/adjust (ask if ambiguous — this command requires naming an
   existing feature, not describing a new one; if the request sounds like a
   new feature, redirect to `/enhance-project` instead).
2. Hand off to `enhance-agent`, which:
   - Reuses the feature's existing branch if still open, or creates
     `fix/<YYYY-MM-DD>-<slug>` if it was already merged/released.
   - Runs the same re-engagement decision and mini gated pipeline as
     `/enhance-project`, scoped to the correction.
3. Updates the `FEATURES.md` entry and `PROJECT_CONTEXT.md` on completion.

## Guardrails

- This command targets an *existing* feature. Don't use it to sneak a new
  feature through with a lighter process than `/enhance-project` — if in
  doubt, ask whether this is genuinely a correction or actually new scope.
