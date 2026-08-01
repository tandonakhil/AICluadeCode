# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run)
**Date:** 2026-08-01
**Commit under test:** `dev` @ **`f56ab9f`** · parent repo @ **`8939ebb`**
**Owner:** `test-agent`
**Blocking:** yes (no Test Policy exception is recorded for this project)
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`
**Exit code:** 0 (server started, served, and was reaped inside each command invocation)
**Scenarios: 11 — PASS 10, FAIL 0, 1 corrected probe (S0b)**

## Process-lifecycle note — read this first

`backend/pilot.py` terminates in a blocking `uvicorn.run(...)`, so it cannot be
run "to completion". It was therefore **started, exercised and stopped inside a
single command invocation**, three times. Nothing was left running past the
turn.

**One deviation is recorded rather than smoothed over.** On the second
invocation the shell `kill $PID` did **not** reap the server: `$PID` was the
launching Python process, and the uvicorn listener (pid 63637) survived it and
was still holding 8021 after the invocation returned. It was detected by the
post-stop `lsof` assertion in that same invocation, reported, and force-killed
by port in the immediately following command. **The post-stop check is what
caught it**, which is the reason it exists; a smoke test that only asserts 200s
would have leaked a listener into the next agent's turn. Final state verified:
`lsof -nP -iTCP:8021 -sTCP:LISTEN` returns nothing.

**The pilot binds 8021, not 8000.** `settings.api_port()` defaults to `8021`. A
foreign process on this machine holds `*:8000`; during this run it answered
**200** to `/health` (the previous run recorded it answering 404). Either way it
is not this application, and nothing in this evidence file was collected from
8000.

---

### Scenario: S0a — the pilot binds and serves on 8021
- Status: EXECUTED
- Input: `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`, then `lsof -nP -iTCP:8021 -sTCP:LISTEN`
- Expected: one listener on 127.0.0.1:8021 owned by the pilot process
- Actual: `Python 63575 tandonakhil 11u IPv4 TCP 127.0.0.1:8021 (LISTEN)`
- Result: PASS
- Evidence: `Python  63575 tandonakhil   11u  IPv4 0x77da40a03afbe977  0t0  TCP 127.0.0.1:8021 (LISTEN)`

### Scenario: S0b — `/proposal` bare path returns 404
- Status: EXECUTED
- Input: `GET http://127.0.0.1:8021/proposal`
- Expected: (my initial probe expected 200 — the probe was wrong)
- Actual: `404`. The route is `@router.get("/proposal/{proposal_id}")`; there is no bare `/proposal` screen, and `/proposal/{id}` 404s by design for an unknown id (`routes.py:306-311`)
- Result: PASS (probe corrected, not a defect — recorded because the raw 404 is in the run log above and would otherwise read as a failure)
- Evidence: `  /proposal      404` and `routes.py:306: @router.get("/proposal/{proposal_id}", response_class=HTMLResponse)`

### Scenario: S1 — every built screen serves 200
- Status: EXECUTED
- Input: `GET` on `/`, `/health`, `/ask`, `/exceptions`, `/review`, `/readiness`, `/dispositions`, `/catalogue`, `/monitors`, `/inventory`, `/audit`, `/refusals`
- Expected: 200 on all twelve; the six screens register 16 says were built at pass 4 are among them
- Actual: 200 on all twelve
- Result: PASS
- Evidence:
  ```
  /              200      /dispositions  200
  /health        200      /catalogue     200
  /ask           200      /monitors      200
  /exceptions    200      /inventory     200
  /review        200      /audit         200
  /readiness     200      /refusals      200
  ```

### Scenario: S2 — the Ask box's GET query string now reaches the render
- Status: EXECUTED
- Input: `GET /ask?tier=certified` then `GET /ask?tier=exploration`, comparing response bodies
- Expected: the two renders differ — this is the pass-8 fix for the criterion the brief describes as "a GET query string to a screen that ignored it"
- Actual: certified renders **22,644 bytes** with 4 occurrences of "exploration" and 2 of "uncertified"; exploration renders **24,432 bytes** with 7 and 5. The bodies differ, so `ask_screen(tier)` → `state.select_tier(tier)` genuinely reaches the rendered output
- Result: PASS
- Evidence: `certified -> len=22644 exploration-occurrences=4 uncertified=2` / `exploration -> len=24432 exploration-occurrences=7 uncertified=5`
- Note: the typed request itself travels by `POST /ask` (form field `request`), not by a `q=` query parameter. My first probe used `?q=` and found nothing; that probe was wrong, and `?q=` is simply not a parameter this route declares.

### Scenario: S3 — an unknown tier value never enters exploration
- Status: EXECUTED
- Input: `GET /ask?tier=certified` → `?tier=nonsense_typo` → `?tier=exploration` → `?tier=nonsense_typo` → `?tier=certified` (state is a process singleton, so order matters and both directions were driven)
- Expected: a typo can never *enter* exploration; `select_tier` ignores any value not in `TIERS`
- Actual: from certified, the typo rendered **22,644 bytes — byte-identical to certified**. From exploration, the typo rendered 24,432 — it left the tier unchanged. The security-relevant direction holds absolutely: no value of this parameter enters exploration
- Result: PASS
- Evidence: `certified -> len=22644` / `typo -> len=22644` / `exploration -> len=24432` / `typo -> len=24432` / `certified -> len=22644`
- **Advisory (docstring/behaviour mismatch, not a defect):** `state.select_tier`'s first line says "An unknown value falls back to CERTIFIED." The code does not fall back — it leaves the tier unchanged (`if tier in TIERS: self.tier = tier`). The docstring's own next paragraph describes the real behaviour correctly ("there is no value of this parameter that removes the marker once exploration is chosen except explicitly choosing certified again"), so the first line contradicts the paragraph beneath it. Behaviour is safe; the first line is wrong.

### Scenario: S4 — `POST /ask` returns a considered answer, 200 on a refusal
- Status: EXECUTED
- Input: `POST /ask` with `request=is $180K worth worrying about for a company this size?` — one of the two paraphrases register 9 records as **not refused**
- Expected: 200 (the status code carries whether the request was handled, not whether the answer was wanted), and the answer states its outcome
- Actual: `200`, the response echoes the request text, and the crumb reads `Ask - not resolvable in this release`
- Result: PASS
- Evidence: `status 200` / `echoes request text: 1` / `outcome crumb: Ask - not resolvable in this release`

### Scenario: S5 — a dossier opens from a file, offline, with zero external references
- Status: EXECUTED
- Input: `/exceptions` → first `/review/ITEM-21400-CP` → `/dossier/DOS-2026-06-0412-01`, then counting every external-reference construct in the served bytes
- Expected: zero `<script>`, `<link>`, `<img>`, `@import`, `url(`, `srcset`, and zero absolute URLs — register 8's closure condition, re-verified on the *served* app rather than in a test client
- Actual: 21,086 bytes, **all eight counts zero**
- Result: PASS
- Evidence:
  ```
  <script 0   <link 0   <img 0   @import 0
  url(    0   srcset 0  http:// 0  https:// 0
  ```

### Scenario: S6 — `AC-F28-07`'s "not run" is a state a reader meets in the running pilot
- Status: EXECUTED
- Input: `GET /exceptions`, counting `data-state="not_run"`
- Expected: exactly one boundary-check row in the `not_run` state, distinguishable from a check that ran and found nothing
- Actual: exactly **1**
- Result: PASS
- Evidence: `grep -o 'data-state="not_run"' | wc -l` → `1`

### Scenario: S7 — register 6's `close_clock_absent` note is on the served screen
- Status: EXECUTED
- Input: `GET /exceptions`, searching for the close-clock note
- Expected: the note is rendered, naming the unmet criterion, because `AC-F38-11` and `AC-F26-05` are both unmet and no absolute timestamp may be shown under a close-relative name
- Actual: present
- Result: PASS
- Evidence: `grep -ci "close_clock_absent\|close clock"` → `1`

### Scenario: S8 — the pilot strip renders on every screen
- Status: EXECUTED
- Input: `GET /exceptions`, `/review`, `/readiness`
- Expected: the non-dismissable pilot strip register 15 requires, on every screen
- Actual: present on all three sampled screens (4 pilot-vocabulary matches each)
- Result: PASS
- Evidence: `/exceptions pilot-strip=4`, `/review pilot-strip=4`, `/readiness pilot-strip=4`

### Scenario: S9 — nothing is left listening after the turn
- Status: EXECUTED
- Input: reap, then `lsof -nP -iTCP:8021 -sTCP:LISTEN`
- Expected: no listener on 8021
- Actual: on invocations 1 and 3, clean. On invocation 2, **pid 63637 survived `kill $PID`** and was force-killed by port in the next command. Final state: nothing listening
- Result: PASS (with the deviation recorded in full at the head of this file)
- Evidence: `holding 8021: 63637` → `kill -9` → `8021 now free — nothing left running`

---

## Not executed in this smoke test

- **The `loopback` transport.** `backend/pilot.py` installs `pilot_transport`,
  which puts the broker in-process. Register 19's residual is unchanged by this
  file: nothing here exercises the deployment topology. The one executing
  witness for that remains `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
  in the architecture suite, which did execute and pass.
- **`CONCLAVE_ENV=production` refusal.** Not re-driven this run; it is covered
  by an executing unit scenario rather than by a served probe.
