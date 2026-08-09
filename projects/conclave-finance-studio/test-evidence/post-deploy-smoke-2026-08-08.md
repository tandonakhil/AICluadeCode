# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test — `close-cockpit-home` close
**Date:** 2026-08-08
**Commit under test:** `dev` @ **`7ecba21`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `STATIC ONLY — NOT EXECUTED`

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
