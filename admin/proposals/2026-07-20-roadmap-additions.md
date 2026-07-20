# Staged proposal: platform roadmap additions (mas-architect, 2026-07-20)

**Status: PENDING — human deferred approval ("wait to approve roadmap, we
will build website first", 2026-07-20). Nothing here is approved; no
ROADMAP.md changes made. Re-present via `/admin-panel roadmap` when the
website work settles.**

Advisory summary (full deliverable in session transcript 2026-07-20):

## P1 — build next
1. **Platform contract sweep** (contract changes, S) — apply the four queued
   LESSONS.md items in one pass: (a) Write→Edit grants for all KB-appending
   agents + per-gate git commits of project root files (the Write-wipe
   pitfall recurred twice: ARCHITECTURE_KB 2026-07-11, UX_KB 2026-07-12);
   (b) scoped Bash for suite-owning SMEs (responsible-ai-architect,
   security-architect) so suite owners can execute their suites; (c)
   completeness-check guardrail rolled into remaining gate owners; (d)
   human's checkbox-backlog + rendered-mockup rules landed in plan-agent /
   ui-ux-designer contract text. Touches many agents' tool grants; no gate
   order or core/optional changes.
2. **Cloud `target_env` for deploy-agent** (infra + core-agent extension, L)
   — re-prioritization of an existing ROADMAP.md backlog item, not new.
   FDE positioning ("we bring the platform to you") is not credible while
   deploy is local-only. One real cloud target (container + IaC), per-
   project environment manifest, smoke tests stay with test-agent.
   Modifies a core-5 agent — needs its own design review before build.
3. **Project packaging / "Conclave-to-go"** (new skill + composition of
   deliverables-agent + release-manager, L) — `/package-project` producing a
   self-contained artifact (prod tree, pinned deps, env manifest, runbook,
   deliverables pack) with a boundary audit: no secrets, no cross-project
   references, no absolute local paths.

## P2 — after P1
4. **Golden-set behavioral evals** (test-agent + templates, M) — versioned
   prompt→expected-behavior suites (`tests/evals/` convention) re-run on
   every enhancement/release; seeded from test-evidence red-team findings +
   synthetic-data personas. Explicitly NOT a new eval agent (overlap rule).
5. **Compliance & audit reporting pack** (deliverables-agent extension, M) —
   per-project evidence pack from SECURITY_KB / RESPONSIBLE_AI_KB /
   test-evidence / Decisions Log, NIST-AI-RMF-shaped, honest "not assessed"
   gaps preserved; folds in the two pending deliverables-agent remnants
   (Excel rollups, HTML regeneration wiring).
6. **Post-deploy runtime observability baseline** (templates +
   usage-monitor extension, M) — minimal structured logging/traces
   (OTel-compatible, no external service) in all three templates;
   usage-monitor reads them for post-deploy health rollups.

## P3 — later, on a real trigger
7. **Multi-tenant / customer workspace isolation** (infra, M) — per-customer
   grouping, secrets isolation, export boundaries. Build at first
   second-customer engagement (feature-flags discipline).
8. **Standard runtime guardrails module** (templates, S/M) — shared
   input-screening/output-normalization tested by responsible-ai-architect's
   suite. Depends on item 4.

Not re-proposed (already on ROADMAP.md): feature flags (trigger unmet);
deliverables-agent remnants (folded into item 5); cloud target_env
(re-prioritized as item 2, not duplicated).
