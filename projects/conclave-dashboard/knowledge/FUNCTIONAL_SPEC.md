# Functional Spec — conclave-dashboard

Gate 4. Every criterion carries a **stable ID**, never reused and never
renumbered. These are the contract the Verification gate audits: each must map
to a named, executed, passing check or it reports `NOT VERIFIED`.

Source: `FEATURES.md` (F1–F8 MVP), `INTAKE.md`, `UX_KB.md`.

---

## F1 · Pipeline state schema

**AC-F1-01** GIVEN a `pipeline-state.json` WHEN it is validated THEN all six
gate states round-trip distinctly: `done` `active` `looped` `warn` `pending`
`skipped`.

**AC-F1-02** GIVEN a gate with `status: skipped` WHEN it is read THEN its
`skip_reason` is exactly one of `not_applicable` · `gate_did_not_exist` ·
`skipped_without_exception`, and the three are **never** collapsed.
*This is the platform's most important distinction; a schema that flattens it
destroys it.*

**AC-F1-03** GIVEN a gate WHEN its approval is read THEN it is one of
`approved` · `approved_override` · `batch_authorized` · `request_changes` ·
`escalate` · `skipped_recorded` · `exception_human` · `not_asked`.
`not_asked` must survive round-trip — it exists because of a real event.

**AC-F1-04** GIVEN a state file missing a required field WHEN loaded THEN the
loader **raises with the field name and file path** and the caller reports it.
It must never substitute a default that renders as plausible.

**AC-F1-05** GIVEN a malformed/corrupt state file WHEN loaded THEN the failure
is **reported as an error state**, never rendered as green, empty, or absent.

---

## F2 · `admin/PIPELINE.yaml`

**AC-F2-01** GIVEN `PIPELINE.yaml` WHEN parsed THEN it yields exactly the 11
gates in canonical order with name, owner, and skip rules.

**AC-F2-02** GIVEN the YAML and `admin/PIPELINE.md` §1–§2 WHEN compared THEN
gate count, order and names agree. A mismatch is a **test failure**, not a
warning.

---

## F3 · Backfill

**AC-F3-01** GIVEN each of the five existing projects THEN a valid
`pipeline-state.json` exists and validates against F1.

**AC-F3-02** GIVEN `little-milestones` THEN its state carries: gate 10
`skipped` + `skipped_without_exception` + approval `not_asked`; gates 4 and 9
`skipped` + `gate_did_not_exist`; gates 6 and 8 `warn`; and 8 loop-backs.
*The awkward history is the test.*

**AC-F3-03** GIVEN `load-alert-agent` THEN gate 5 is `skipped` +
`not_applicable` — and renders **visibly differently** from gates 4 and 9,
which are `gate_did_not_exist`.

---

## F4 · Renderer

**AC-F4-01** GIVEN a state file WHEN rendered to markdown THEN the mermaid
block emits `admin/PIPELINE.md` §3's `classDef` lines **byte-identical**.

**AC-F4-02** GIVEN the same state WHEN rendered to HTML and to markdown THEN
both report the same gate position, approvals and skip reasons.
*One code path, two outputs — they cannot disagree.*

**AC-F4-03** GIVEN 11 gates WHEN rendered THEN rows carry max 7 boxes
(3 gates + 3 approvals), wrapping, per §3's row structure.

**AC-F4-04** GIVEN generated markdown THEN it carries a header naming its
source file and generation timestamp, so no reader mistakes it for
hand-authored.

---

## F5 · Dashboard — selector and pipeline status

**AC-F5-01** GIVEN the dashboard WHEN loaded THEN a **project selector**
(dropdown) is present and switching it changes the displayed project.

**AC-F5-02** GIVEN any project selected THEN an **always-visible portfolio
row** shows every other project's headline status.
*A closed dropdown cannot carry state; without this row a red project is
invisible by design.*

**AC-F5-03** GIVEN a selected project THEN its gate position, approvals, skip
reasons and loop-backs are all visible without further navigation.

**AC-F5-04** GIVEN any RAG chip THEN it is one of `green` `amber` `red`
`unknown`. A chip that cannot enumerate its reasons renders **`unknown`,
never green**.

**AC-F5-05** GIVEN a count that cannot be established THEN it renders `?`,
never `0`. *`0` is an assertion.*

**AC-F5-06** GIVEN colour is removed (greyscale) THEN **no fact is lost** —
every status is also carried by text or shape.

**AC-F5-07** GIVEN the default load THEN the theme is **Quiet Ledger, light**.

---

## F6 · Runtime status

**AC-F6-01** GIVEN a project with a recorded served URL WHEN probed THEN the
result is one of `up` · `down` · `degraded` · `unknown` · `no_url_recorded`.

**AC-F6-02** GIVEN a host that accepts the connection but returns non-2xx at
the probed path THEN the state is **`degraded`**, never `up` and never `down`.
*`little-milestones` on :8000 answers but 404s at `/`. Calling that either up
or down is a lie.*

**AC-F6-03** GIVEN a probe that times out or errors THEN the state is
`unknown` with the reason shown — never silently `down`.

**AC-F6-04** GIVEN a project with no recorded URL THEN `no_url_recorded` is
shown as its own state, not as a failure.

**AC-F6-05** GIVEN any probe THEN it has a bounded timeout and never blocks
page render beyond it.

---

## F7 · kb-server migration

**AC-F7-01** GIVEN the migrated app THEN `/` serves the knowledge base and
`/status` serves the dashboard, from **one** Flask app on one port.

**AC-F7-02** GIVEN the migration is complete THEN `admin/kb-server/` no longer
contains a running application.

---

## F8 · Staleness

**AC-F8-01** GIVEN any rendered view THEN the **source file's mtime** is shown.

**AC-F8-02** GIVEN a project that is **in flight** (a gate `active`, or an
approval `awaiting`) AND whose state is older than the threshold THEN it is
visibly marked stale.

**AC-F8-03** GIVEN a project that is **not** in flight THEN it is **never**
marked stale, however old its state file is. *Revised 2026-07-29: the original
criterion equated "old" with "stale" and flagged all six projects, including a
released one whose record had correctly not changed in days. A board that cries
wolf gets ignored — which is precisely the failure this project exists to
avoid. Staleness means "the record may not reflect reality", not "time has
passed."*

---

## Cross-cutting — apply to every feature

**AC-X-01 · No hardcoded counts.** No gate count, agent count, gate name or
project name is hardcoded anywhere — **including in copy**. Every figure comes
from state at render time. *`kb-server/DESIGN_SPEC.md` hardcoded "Eighteen
agents / Nine gates" into the design document; the real numbers are 21 and 11,
so even a data-wired page would have shipped wrong.* **Mechanically checkable.**

**AC-X-02 · Single source of truth.** `PIPELINE_LOG.md` and
`PORTFOLIO_STATUS.md` are **generated**, not hand-maintained. No fact exists in
two hand-edited places.

**AC-X-03 · Read-only.** The dashboard performs no writes to any project, and
no route mutates state.

**AC-X-04 · Read at request time.** State is read **inside the route handler**,
never at import or into a module-level global. *A cached-at-import "live"
dashboard serves state as of process start — the stale-kb-server failure in a
new costume.*

**AC-X-05 · Cross-project read boundary.** The app reads sibling projects
read-only and path-scoped, and imports nothing from any project.

**AC-X-06 · Honest degradation.** Unknown, unreachable and stale are **visible
states** everywhere. Nothing that could not be established renders as fine.
