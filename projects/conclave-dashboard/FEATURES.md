# Features: conclave-dashboard

## Backlog — proposed for MVP, awaiting human approval (gate 3)

Presented as per-feature checkboxes. Nothing here is bundled; approve or defer
each line independently.

### F1 — Pipeline state schema (`pipeline-state.json`)
The per-project machine-readable record: gate status, approval value, dates,
participants, artifacts, loop-backs, exceptions, route changes.
**Must round-trip all six gate states, all seven approval values including
`NOT ASKED`, and all three `⊘` reasons distinctly.** A schema that flattens
those destroys the platform's most important distinction.
_Foundation — everything else reads it._

### F2 — `admin/PIPELINE.yaml` (pipeline shape)
Gate order, names, owners, exit criteria, skip rules — static, one file,
becomes the source for `PIPELINE.md` §1–§2. Lands an already-approved roadmap
item deferred on 2026-07-28.

### F3 — Backfill all five existing projects
Real state files for grid-assistant, load-alert-agent, policy-lookup-assistant,
conclave-marketing, little-milestones. The awkward history is the point: a
`NOT ASKED`, two `⚠`, three flavours of `⊘`, eight loop-backs. If the schema
survives these it survives anything.

### F4 — Renderer (state → markdown + HTML)
**One code path, two outputs.** Emits `admin/PIPELINE.md` §3's `classDef` block
and row structure verbatim, so every graph stays identical. This is what makes
`PIPELINE_LOG.md` and `PORTFOLIO_STATUS.md` *generated* rather than
hand-maintained — the strengthening the human approved.

### F5 — Dashboard: project selector + pipeline status
Dropdown project switch (R1), inverted-pyramid layout (R2), key callouts (R3).
Gate position, approvals, what was skipped and why, loop-backs.

### F6 — Runtime status
Health-check each project's recorded served URL. Up / down / unknown /
unreachable as **visible states** — never silently rendered as fine.
_Resolves the intake ambiguity the human answered as "both"._

### F7 — Migrate and retire `admin/kb-server/`
`git mv` into `dev/`. One app, one port, two routes: `/` knowledge base,
`/status` dashboard. **Separately approvable — not bundled with F5.**

### F8 — Staleness surfacing
Every view shows its source file's mtime. A dashboard that cannot say how old
it is has no business being authoritative.

---

## Deferred — proposed OUT of MVP

### F9 — Fix kb-server's content drift at source
Its page, `DESIGN_SPEC.md` and `ROADMAP.md` all say **18 agents / 9 gates**;
actual is **21 and 11**. F7 moves the file; this would rewrite its content
from the registry. Larger scope, and F4's no-hardcoded-counts rule prevents
recurrence either way.

### F10 — Always-on service (`launchd`)
Human chose **manual start** at intake (O1). Recorded so the decision is
visible, not lost.

### F11 — Auto-refresh
`<meta refresh>` or a 30s fetch. An afterthought on top of read-on-request,
not an alternative to it. Only matters if F10 ever lands.

---

## Explicitly out of scope (from intake A8.2, unchanged)
Editing anything from the UI · advancing or approving a gate · auth or
multi-user · remote/public exposure · historical trend charts · notifications.

---

### F12 — Staged intake form at `/intake` (built 2026-07-30, **removed 2026-07-31**)
**Removed — built by mistake.** A `/intake` page was never in the approved
MVP scope; project creation belongs to `/new-project`, driven by the
orchestrator, not to the read-only status console. The route, its template
(`intake.html`), the nav link, and its tests were removed 2026-07-31 at the
human's direction. Recorded here rather than deleted so the misstep stays in
the history.

## In Development

_(none)_

## Ready for Release

_None. No release train cut for this project._

## Released

_None._
