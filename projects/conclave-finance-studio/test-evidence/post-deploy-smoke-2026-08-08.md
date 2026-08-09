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
