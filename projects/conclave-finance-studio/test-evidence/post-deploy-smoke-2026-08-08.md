# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test — `close-cockpit-home` close
**Date:** 2026-08-08
**Commit under test:** `dev` @ **`7ecba21`** (pass 2)
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `STATIC ONLY — NOT EXECUTED` (pass 2) — **SUPERSEDED at pass 3, see
below: `EXECUTED`, 13/13 PASS, against `f313d41`**

## Reason

No process is listening on this build's assigned ports (`API_PORT=8021`,
`GES_PORT=8022`) at the time of this gate. `lsof -nP -iTCP:8021 -sTCP:LISTEN`
and `-iTCP:8022` both return nothing. The last confirmed live deploy of this
port pair (gate 11, 2026-08-06, commit `b447a11`) is not the commit under
test here (`7ecba21`), and per this agent's process-lifecycle constraint a
long-lived server is started by `deploy-agent`/the orchestrator before this
agent is invoked — never inside this agent's own turn. This agent does not
start one.

**Ports confirmed untouched, checked by PID re-read from `lsof`, not by
name:** the human's pilot on **8030** (pid 48206) and the design preview on
**8050** (pid 85436) were both running at the start of this session and are
still running, unchanged, at the end of it.

## What this means for the gate

The post-deploy smoke test is a **blocking** suite per this project's Test
Policy. `STATIC ONLY — NOT EXECUTED` does **not** satisfy that blocking
obligation and is **not** folded into the aggregate pass count above. The
gate should surface this as an unmet gate condition: `deploy-agent` (or the
orchestrator) needs to bring up a served instance of `7ecba21` on a distinct
port before this scenario can move from `STATIC ONLY` to `EXECUTED`.

Everything else reported in this gate's evidence (`unit-integration-2026-08-08.md`,
`order-independence-2026-08-08.md`, `close-cockpit-home-verification-2026-08-08.md`)
was driven through `TestClient(app)` / real Chromium against the in-process
ASGI app, which is a real HTTP-shaped path through the application but is
not the same claim as "a served instance answered on a bound port," which is
what this scenario specifically checks.

---

# PASS 3 — SUPERSEDES the above: `EXECUTED`, `dev` @ `f313d41`

**Commit under test:** `f313d41` · **Owner:** `test-agent` · **Blocking:** yes
**Status:** `EXECUTED`

`deploy-agent`'s 2026-08-08 walk of `7ecba21` confirmed the app serves
correctly, but a manual walk does not satisfy this scenario's blocking
obligation as an **executed suite result** — that is still owed distinctly.
This pass stands up its own fresh instance rather than accepting the manual
walk as a substitute.

**Method — synchronous within one command invocation, no long-lived process
left running past this agent's turn:** `CONCLAVE_ENV=pilot API_PORT=8021
GES_PORT=8022 .venv/bin/python backend/pilot.py`, launched in its own process
group (`start_new_session=True`), `CONCLAVE_VAR_DIR` pointed at a scratch copy
of `dev/var` (never the shared `dev/var` the human's 8030 session reads),
driven over real stdlib `urllib` HTTP (no `TestClient`, no ASGI shortcut),
torn down by `SIGTERM` to the process group before the invocation returned.

**Result: 13 scenarios, 13 pass, 0 FAIL.** Full per-scenario detail —
`/health`, the twelve routes, the cockpit entry point, drawer-only nav, both
standing disclosures, FP&A absence, and `AC-COCKPIT-20`'s three-way
badge/queue/cockpit agreement re-verified live on a freshly served instance —
is recorded in `close-cockpit-home-verification-2026-08-08.md`, "PASS 3 —
final confirmation," item 4.

**Process lifecycle:** pilot pid confirmed dead and `lsof -nP -iTCP
-sTCP:LISTEN` confirms 8021/8022 free immediately after teardown. The human's
pilot (8030, pid 48206) and the design preview (8050, pid 85436) were checked
by `lsof` PID re-read before and after this run and are unchanged — never
probed, never signalled.

**This closes the gap the pass-2 entry above records.** The post-deploy smoke
test's blocking obligation is now met by an `EXECUTED` result, not a
`STATIC ONLY` one and not a manual walk.

---

# PASS 4 — SUPERSEDES the above: `EXECUTED`, `dev` @ `f925a3f` — Gate 11 final smoke

**Commit under test:** `f925a3f` · **Owner:** `test-agent` · **Blocking:** yes
**Status:** `EXECUTED`

`deploy-agent`'s gate-11 walk of `f925a3f` (`PROJECT_CONTEXT.md`, 2026-08-08)
confirmed the "N left" fix live, but named this scenario's formal executed
result as still owed distinctly ("a formal `test-agent` run against `f925a3f`
specifically has not happened and is still owed"). This pass supplies it —
re-run against the exact deploy commit rather than carried forward from pass
3's result at `f313d41`.

**Method — identical to pass 3, synchronous within one command invocation, no
long-lived process left running past this agent's turn:** `CONCLAVE_ENV=pilot
API_PORT=8021 GES_PORT=8022 .venv/bin/python backend/pilot.py`, launched in
its own process group (`start_new_session=True`), `CONCLAVE_VAR_DIR` pointed
at a scratch copy of `dev/var` (never the shared `dev/var` the human's 8030
session reads), driven over real stdlib `urllib` HTTP, torn down by `SIGTERM`
to the process group before the invocation returned.

**Result: 15 scenarios, 15 pass, 0 FAIL** — two more than pass 3's 13: an
explicit "N left" exact-string check on the `.ct` span (this gate's specific
finding) and an explicit three-way numeric-equality assertion (pass 3 checked
the two deltas and the row absence but not `cockpit == badge == rows` as one
assertion). Full per-scenario detail below and in
`close-cockpit-home-verification-2026-08-08.md`'s "PASS 4" section.

**First attempt's script had four scoring bugs, all in the ad-hoc smoke
script itself, not the application — caught and corrected before this
result:**
1. Sidebar-absence check flagged `.navitem`/`.navgrp` as a bare substring
   hit, which matched this build's own HTML **comment** documenting the
   sidebar's removal history (rendered verbatim from `chrome.py`'s
   docstring) — corrected to check for a live CSS rule block or `class=`
   attribute use, matching `deploy-agent`'s own note ("every occurrence of
   those strings is inline CSS comment documenting the removal, checked
   individually").
2. The topology disclosure's real `data-testid` is
   `transport-topology-state`, not `topology-strip` as the script first
   assumed.
3. `POST /review/{id}/resolve` takes `application/x-www-form-urlencoded`
   (matching `tests/uihelpers.py::post()`'s `CLIENT.post(path, data=data)`),
   not JSON — the script's first JSON POST 422'd.
4. `/queue`'s row testid is `exception-row` (`data-item-id` carries the item
   id), not a guessed `queue-row`.

All four corrected against the real markup (`TestClient(app)` dump) and the
suite's own harness (`test_close_cockpit_criteria.py::TestAC_COCKPIT_20`)
before re-running live. **No defect in the application** — the first
attempt's 7 apparent failures were entirely script bugs, named individually
above rather than silently discarded.

### Scenario: startup — /health reachable within 30s
- Status: EXECUTED · Expected: 200 within 30s · Actual: reachable · Result: PASS

### Scenario: G2 — /health payload
- Status: EXECUTED
- Expected: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`
- Actual: exact match
- Result: PASS

### Scenario: G1 — twelve routes all 200
- Status: EXECUTED
- Actual: `{"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}`
- Result: PASS

### Scenario: ENTRY — / renders the close cockpit, not the queue
- Status: EXECUTED
- Expected: `cockpit-h1`, `close-tracker`, `cockpit-acts`, `cockpit-coverage-strip` present; `exception-queue` absent
- Actual: all four cockpit markers present, `exception-queue` absent
- Result: PASS

### Scenario: NAV — drawer present, no live sidebar markup on /
- Status: EXECUTED
- Expected: `drawer` testid present; no live `.navitem`/`.navgrp` CSS rule or
  `class=` use (a bare substring hit on the removal-history HTML comment is
  not counted as a defect)
- Actual: drawer present; zero live rule/class hits
- Result: PASS

### Scenario: DISCLOSURE — pilot-strip present on /
- Status: EXECUTED · Actual: present (`data-testid="pilot-strip"`) · Result: PASS

### Scenario: DISCLOSURE — transport-topology-state strip present on /
- Status: EXECUTED · Actual: present (`data-testid="transport-topology-state"`) · Result: PASS

### Scenario: FPA — /fpa /fp-and-a /fpna all 404, no FP&A string on /
- Status: EXECUTED
- Actual: `{"/fpa": 404, "/fp-and-a": 404, "/fpna": 404}`, no "FP&A"/"FPNA" string on `/`
- Result: PASS

### Scenario: RETURN CONTROL — cockpit-return renders "N left", not a bare digit (gate 10's finding, this gate's specific reason for existing)
- Status: EXECUTED
- Expected: the exact string `"<N> left"` inside the `.ct` span, live on a
  served instance
- Actual: `<a ... data-testid="cockpit-return" ...>Close - 2026-06<span class="ct">6 left</span></a>`
- Result: **PASS**

### Scenario: AC-COCKPIT-20 setup — badge/cockpit/row counts readable and in agreement before any action
- Status: EXECUTED · Actual: `before_cockpit=6 before_badge=6 rows_before=6` (all three equal) · Result: PASS

### Scenario: AC-COCKPIT-20 — resolve returned 200
- Status: EXECUTED · Input: `POST /review/ITEM-13800-CP-1/resolve` (form-encoded: `resolution_type=R1`, `explanation`, `expiry_period=2026-08`, `clears_by=2026-08`)
- Actual: 200 · Result: PASS

### Scenario: AC-COCKPIT-20 — drawer badge decremented on a live served instance
- Status: EXECUTED · Expected: 6 -> 5 · Actual: 6 -> 5 · Result: PASS

### Scenario: AC-COCKPIT-20 — /queue row count decremented on a live served instance
- Status: EXECUTED · Expected: 6 -> 5 · Actual: 6 -> 5 · Result: PASS

### Scenario: AC-COCKPIT-20 — resolved item no longer a /queue row
- Status: EXECUTED · Actual: absent from `/queue`'s rendered rows · Result: PASS

### Scenario: AC-COCKPIT-20 — three-way agreement: cockpit count == drawer badge == /queue rows, live
- Status: EXECUTED · Expected: all three equal after the resolve · Actual: `cockpit=5 badge=5 rows=5` · Result: PASS

**Process lifecycle, this smoke run:** pilot pid confirmed dead (`pid_alive:
False`) and `lsof -nP -iTCP:8021/8022 -sTCP:LISTEN` both empty immediately
after teardown. The human's pilot (8030, pid 48206) and the design preview
(8050, pid 85436) were re-checked by `lsof` PID immediately before launch and
immediately after teardown and are unchanged — never probed, never signalled.

**Result: EXECUTED, 15/15 PASS, against the exact deploy commit `f925a3f`.**
This satisfies the smoke test's blocking obligation for gate 11 — the prior
pass-3 result (against `f313d41`) is superseded, not carried forward.
