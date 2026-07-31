# Test evidence — post-deploy smoke test

**Run date:** 2026-08-01 (Gate 8 · Test re-run, post-pass-5)
**Commit under test:** `dev` @ `b1b5dde` — "The ID-to-scenario joins stop being inferred, and 186 + 77 stops being 262"
**Project repo:** `6dae43e`
**Owner:** `test-agent`
**Entry point:** `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`
**Status:** `EXECUTED`
**Scenarios:** 9 executed — 9 PASS, 0 FAIL
**Blocking:** yes

**The pilot binds 8021, not 8000.** `common/settings.api_port()` defaults to
`8021`. An unrelated Python process (pid 20395) holds `*:8000` on this machine
and answers 404 to everything; a smoke test aimed there reports false failures.
Scenario S5 below records both ports side by side so the next reader does not
have to rediscover it.

**Process lifecycle.** The pilot was started, exercised and stopped inside each
single command invocation, with a `trap ... EXIT` reaping the child and a
post-stop `lsof` proving nothing was left listening. No server, browser or
process outlives this agent's turn. Four invocations were used (S1–S6, S7, S8,
and the parameterised-screen probe); each started and stopped its own pilot.

This file REPLACES `smoke-test-2026-07-31.md`, which described a pre-pass-5
commit and reported "thirteen routed screens served 200" — a figure that does
not correspond to the routes this build serves.

---

## Per-scenario evidence

### Scenario: S1 — every parameterless GET route serves 200
- Input: `GET http://127.0.0.1:8021{route}` for all 17 parameterless GET routes enumerated from `app.main:app` at runtime
- Expected: HTTP 200 on every one
- Actual: 200 on all 17
- Result: PASS
- Evidence:
  ```
  / 200   /ask 200   /audit 200   /audit/export 200   /catalogue 200
  /dispositions 200   /docs 200   /docs/oauth2-redirect 200   /exceptions 200
  /health 200   /inventory 200   /monitors 200   /openapi.json 200
  /readiness 200   /redoc 200   /refusals 200   /review 200
  ```
  Twelve of these are rendered screens (`/`, `/ask`, `/audit`, `/audit/export`,
  `/catalogue`, `/dispositions`, `/exceptions`, `/inventory`, `/monitors`,
  `/readiness`, `/refusals`, `/review`); the remaining five are `/health` and
  FastAPI's own `/docs`, `/docs/oauth2-redirect`, `/openapi.json`, `/redoc`.
  Four further GET surfaces are parameterised (`/dossier/{id}`,
  `/proposal/{id}`, `/review/{item_id}`, `/export/{group_id}.csv`) — sixteen
  screens in total, matching the register's pass-4 count.

### Scenario: S2 — the pilot strip renders on every screen
- Input: `grep -c pilot-strip` over the body of each of the 17 routes above
- Expected: present on all twelve rendered screens
- Actual: present on all twelve; absent from `/health`, `/openapi.json`, `/docs`, `/docs/oauth2-redirect`, `/redoc`
- Result: PASS
- Evidence: the five without a strip are FastAPI machinery and a JSON health
  endpoint, not screens a reviewer reads findings on. Recorded explicitly
  rather than filtered out, because a bare "12/12" would hide which routes were
  excluded and on whose judgement.

### Scenario: S3 — the F28 "not run" state on the served screen is a real detector run
- Input: `GET /exceptions` from the running pilot
- Expected: five boundary-check rows; exactly one in state `not_run`; that one names the absent warehouse object; the run statement does not read as an all-clear
- Actual: 5 rows, 1 × `data-state="not_run"`, naming `dw.fx_revaluation`
- Result: PASS
- Evidence:
  ```
  boundary-check rows: 5
  data-state="not_run":  1
  names dw.fx_revaluation: 1
  backtest-no-claim panels: 1
  close_clock_absent note: 1
  ```
  This is the scenario the brief asked to be confirmed. The pilot warehouse
  omits exactly one object — `pilot_transport.PILOT_OMITTED_OBJECTS =
  ("fx_revaluation",)` — so the F28 A9 FX/CTA check has no dataset to read and
  reports NOT RUN. It is an object that does not EXIST, not an empty table:
  an empty table answers with zero rows, and a check concluding from zero rows
  is the failure convention C2 forbids. **"Not run" is therefore a state a
  reader actually meets in the running pilot**, not only inside a test fixture.

### Scenario: S4 — the dossier carries zero external references
- Input: `GET /dossier/DOS-2026-06-0412-06` (the first dossier link reachable from `/exceptions`)
- Expected: no `<script>`, `<link>`, `<img>`, `@import`, `srcset`, and no absolute http(s) URL
- Actual: all six counts zero
- Result: PASS
- Evidence: `<script>: 0  <link>: 0  <img>: 0  @import: 0  srcset: 0  http(s)://: 0`
  — the exhibit opens from a file, offline, which is the seven-year property.

### Scenario: S5 — 8021 is the pilot; 8000 is not this application
- Input: `GET http://127.0.0.1:8000/` and `GET http://127.0.0.1:8021/`
- Expected: the pilot answers only on 8021
- Actual: `8000/ -> 404`, `8021/ -> 200`
- Result: PASS
- Evidence: `lsof -nP -iTCP:8000 -sTCP:LISTEN` → `Python 20395 tandonakhil ... TCP *:8000 (LISTEN)` — a foreign process, running before the pilot started and still running after it stopped.

### Scenario: S6 — the pilot transport is refused under `CONCLAVE_ENV=production`
- Input: `CONCLAVE_ENV=production .venv/bin/python backend/pilot.py`
- Expected: refuses to start, naming the boundary it would collapse and the two commands that do not
- Actual: exit code 2 with that message
- Result: PASS
- Evidence: `refusing to start: backend/pilot.py puts the guardrail broker in the same process as the interface, which is refused in production. Run backend/ges/run.py and backend/app/run.py.`

### Scenario: S7 — a parameterised review screen serves from the entry point
- Input: `GET /review`, follow the first `/review/{item_id}` link
- Expected: 200
- Actual: `/review/ITEM-21400-CP -> 200`
- Result: PASS
- Evidence: link discovered by parsing the served `/review` markup, not hard-coded.

### Scenario: S8 — a staff-persona approval is refused by the broker
- Input: `POST /proposal/PROP-2026-06-0031/approve` with no persona switch (default staff accountant)
- Expected: refused, in the refusal grammar, not a 500 and not a silent success
- Actual: **HTTP 403**, page titled "Not approved", rendered in the refusal grammar (`.refused` styling, refusal vocabulary present)
- Result: PASS
- Evidence: `HTTP 403`; document title `Not approved - Conclave Finance Studio`.
  Note for the next reader: the proposal screen is **not** reachable by
  link-following from the served pilot — `/proposal/{id}` appeared in no
  navigation traversal from `/`, `/exceptions`, `/review`, `/review/{item}`,
  `/readiness`, `/monitors`, `/dispositions`, `/inventory` or `/audit`. That is
  by design (pass 4 register: six controls exist only as the result of an
  action, and a companion test asserts they are NOT reachable by navigation),
  so the scenario was driven by direct URL. A curl-only smoke that walks links
  cannot reach this control at all.

### Scenario: S9 — `/health` answers and declares the process role
- Input: `GET /health`
- Expected: 200 with a body naming the environment and whether this process holds credentials
- Actual: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`
- Result: PASS
- Evidence: recorded verbatim. Worth a reader's attention: `ges_base_url`
  reports `http://127.0.0.1:8022` even though in this configuration the broker
  is in-process and nothing is listening on 8022. It is the configured value,
  not an observed one. Not a defect — but a reader taking `/health` as evidence
  that the two-process topology is running would be wrong, and the pilot strip
  is what tells them otherwise.

---

## Nothing left running

```
== stopping pilot ==
== residual listeners on 8021 after stop ==
(none — nothing left running)
```
Repeated after each of the four invocations.
