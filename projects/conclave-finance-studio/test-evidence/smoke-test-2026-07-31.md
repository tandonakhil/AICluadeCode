# Test evidence — post-deploy smoke test — 2026-07-31

**Project**: conclave-finance-studio · **Gate**: 8 · Test
**Run**: 2026-07-31, gate-8 verification run by `test-agent`
**Status**: `EXECUTED`
**Process lifecycle**: the pilot was started, exercised and stopped **inside a
single command invocation**. No server, browser or test process was left
running past the turn. `pgrep -f backend/pilot.py` after the run returned
nothing.

**Configuration under test**: `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`
— the SINGLE-PROCESS pilot. Per deferred-substitution register entry 19, this
configuration installs `backend/pilot_transport.py` and the trust boundary is a
**module** boundary, not the process boundary `ARCHITECTURE_KB` §3.2 requires.
Nothing below is evidence about the two-process deployment topology.

---

### Scenario: the pilot starts and binds
- Input: `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`
- Expected: the process starts, prints the boundary warning, and binds a port
- Actual: started; printed the four-line boundary warning naming
  `backend/pilot_transport.py`; bound `http://127.0.0.1:8021/`
- Result: PASS
- Evidence: `Uvicorn running on http://127.0.0.1:8021 (Press CTRL+C to quit)`.
  Note the port is **8021**, not 8000 — an unrelated process was already
  answering 404 on 8000 and a smoke test aimed at the documented-by-assumption
  port would have reported thirteen false 404s. It did on the first attempt;
  recorded because a smoke test that reads a stranger's server is the same
  defect class this gate is auditing.

### Scenario: every routed screen serves
- Input: `GET` against each of the thirteen routed URLs
- Expected: HTTP 200 for all thirteen
- Actual: 200 for all thirteen
- Result: PASS
- Evidence:
  ```
  200  /                                      200  /dispositions
  200  /ask                                   200  /catalogue
  200  /exceptions                            200  /monitors
  200  /review                                200  /inventory
  200  /proposal/PROP-2026-06-0031            200  /audit
  200  /dossier/DOS-2026-06-0412-01           200  /refusals
  200  /readiness
  ```

### Scenario: the served page is the application, not an error shell
- Input: `GET /`
- Expected: the Ask screen's own title
- Actual: `<title>Ask - Conclave Finance Studio</title>`
- Result: PASS
- Evidence: as above.

### Scenario: the pilot strip is present on a findings screen
- Input: `GET /exceptions`, count case-insensitive occurrences of "pilot"
- Expected: > 0 — register entry 15 requires a non-dismissable pilot strip
- Actual: 4 occurrences
- Result: PASS
- Evidence: `curl -s .../exceptions | grep -ci pilot` → `4`

### Scenario: the dossier is self-contained and offline-openable
- Input: `GET /dossier/DOS-2026-06-0412-01`, count `<script` / `<link` /
  `<img` / `@import` / `srcset`
- Expected: 0 — `ARCHITECTURE_KB` §9.4 and register entry 8's closure
- Actual: 0
- Result: PASS
- Evidence: `grep -cE "<script|<link|<img|@import|srcset"` → `0`

### Scenario: the write path refuses a staff-accountant approval at the broker
- Input: `POST /proposal/PROP-2026-06-0031/approve` as the default (staff)
  persona
- Expected: 403 — the broker denies, the interface does not hide the control
- Actual: 403
- Result: PASS
- Evidence: `curl -o /dev/null -w "%{http_code}" -X POST .../approve` → `403`

### Scenario: the pilot stops cleanly and leaves nothing running
- Input: `kill $PILOT_PID; wait; pgrep -f "backend/pilot.py"`
- Expected: no surviving process
- Actual: `no pilot process remains`
- Result: PASS
- Evidence: as above.

---

## Not covered by this smoke test

The smoke test exercised the **pilot** transport only. The two-process
deployment topology —

```
CONCLAVE_PROCESS_ROLE=ges .venv/bin/python backend/ges/run.py
CONCLAVE_PROCESS_ROLE=api .venv/bin/python backend/app/run.py
```

— was **not** started and **not** smoke-tested. Every screen result above was
obtained with the guardrail broker inside the interface process. See the
register cross-check for why that matters.
