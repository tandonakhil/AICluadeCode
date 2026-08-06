# Test evidence - clean-checkout reproduction and startup guards, gate 11

**Project:** conclave-finance-studio
**Gate:** 11 - 11 - independent confirmation of `deploy-agent`'s clean-checkout claim
**Date:** 2026-08-06
**Commit under test:** `dev` @ **`c68ad84`**, working tree clean
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**9 scenarios, 9 pass, 0 fail.** `deploy-agent`'s clean-checkout reproduction and
both startup guards are **confirmed independently**.

`dev` was cloned to a scratch directory at `c68ad84` and everything below was run
from the clone. The pilot was started and reaped inside the invocation that
started it. The clone reuses the existing `.venv` **interpreter**; it does not
re-verify `python3 -m venv .venv && pip install -r requirements-dev.txt`, which
`deploy-agent` did verify. What is verified here is the claim under test: that a
fresh checkout of the *code*, with no `var/`, starts and reproduces the chain.

## One harness correction, recorded rather than quietly fixed

**C6 first reported FAIL and was a harness sequencing defect, not a build
defect.** It listed `var/` immediately after `/health` returned 200 and found
only `broker_db.sqlite3`. `warehouse.sqlite3` is created **lazily, on the first
request that reads it**, and `/health` does not read it. The scenario now samples
`var/` twice - at first-serve and after the first real requests - so the lazy
creation is visible in the record instead of being smoothed away by moving the
assertion.

---

### Scenario: C1 - dev clones cleanly and the clone is the commit under test
- Status: EXECUTED
- Input: git clone dev -> scratch
- Expected: clone succeeds, HEAD matches, source tree clean
- Actual: rc=0 clone_head=c68ad84 source_head=c68ad84 source_dirty=''
- Result: PASS
- Evidence: clone at /private/tmp/claude-501/-Users-tandonakhil-Documents-AI-Projects-AICluadeCode/bd1f7c49-717a-452b-b079-87337d94bcef/scratchpad/g11/clean-clone

### Scenario: C2 - var/ is gitignored and absent from a fresh checkout
- Status: EXECUTED
- Input: ls clone/var ; git check-ignore var/warehouse.sqlite3
- Expected: directory absent, and the path is ignored by a real .gitignore rule
- Actual: var_exists=False check_ignore='.gitignore:37:var/\tvar/warehouse.sqlite3'
- Result: PASS
- Evidence: .gitignore:37:var/	var/warehouse.sqlite3

### Scenario: C3 - a credential in the environment refuses startup with exit 3, before uvicorn binds
- Status: EXECUTED
- Input: GES_WAREHOUSE_PASSWORD=... CONCLAVE_ENV=pilot python backend/pilot.py (from the CLONE)
- Expected: exit 3, T4 refusal message on stderr, nothing listening on 8021
- Actual: exit=3 listener_after='' elapsed=0.0s
- Result: PASS
- Evidence: 

```
refusing to start: the api process environment contains credentials it must not hold: GES_WAREHOUSE_PASSWORD
This is the single-process pilot: the guardrail broker runs inside this process, so a credential in this environment is reachable from the interface side by import alone.
```


### Scenario: C4 - CONCLAVE_ENV=production refuses startup with exit 2, before uvicorn binds
- Status: EXECUTED
- Input: CONCLAVE_ENV=production python backend/pilot.py (from the CLONE)
- Expected: exit 2, topology refusal on stderr, nothing listening on 8021
- Actual: exit=2 listener_after=''
- Result: PASS
- Evidence: 

```
refusing to start: backend/pilot.py puts the guardrail broker in the same process as the interface, which is refused in production. Run backend/ges/run.py and backend/app/run.py.
```


### Scenario: C5 - a refused start creates no state
- Status: EXECUTED
- Input: ls clone/var after both refusals
- Expected: var/ still absent
- Actual: var_exists=False
- Result: PASS
- Evidence: guards refuse before anything is built

### Scenario: C7 - all twelve routes and /health serve 200 from the clean checkout
- Status: EXECUTED
- Input: GET twelve routes + /health on the clone's pilot
- Expected: 200 on all thirteen
- Actual: health=200 routes={"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
- Result: PASS
- Evidence: 

```
{"health": "{\"status\":\"ok\",\"env\":\"pilot\",\"tenant\":\"tenant-demo\",\"holds_credentials\":false,\"ges_base_url\":\"http://127.0.0.1:8022\"}", "routes": {"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}}
```


### Scenario: C6 - the pilot creates var/ and both SQLite files itself on first run
- Status: EXECUTED
- Input: start the pilot from the clone with var/ absent; list var/ at first-serve AND after the first real request
- Expected: var/ created; broker_db.sqlite3 at startup, warehouse.sqlite3 by the first request that reads it
- Actual: served=True at_health=['broker_db.sqlite3'] after_first_requests=['broker_db.sqlite3', 'warehouse.sqlite3']
- Result: PASS
- Evidence: 

```
{"at_health": ["broker_db.sqlite3"], "after_traffic": ["broker_db.sqlite3", "warehouse.sqlite3"], "sizes": {"broker_db.sqlite3": 135168, "warehouse.sqlite3": 131072}, "note": "warehouse.sqlite3 is created lazily on first read, not at bind"}
```


### Scenario: C8 - the full approve -> override -> export chain reproduces from the clean checkout
- Status: EXECUTED
- Input: staff approve, controller approve, override, export, fetch the file
- Expected: 403 not_in_capability_allowlist; 403 approval_value_above_ceiling; override 200; export 200; balanced file
- Actual: staff=403(allowlist=True) controller=403(ceiling=True) override=200 export=200 file=['/export/CS-B876AEC47CDD.csv'] Dr=86340.0 Cr=86340.0
- Result: PASS
- Evidence: {"group_ids": ["CS-B876AEC47CDD"], "dr": 86340.0, "cr": 86340.0}

### Scenario: C9 - the evidence export from the clean checkout carries the same three integrity sections
- Status: EXECUTED
- Input: GET /audit/export/file on the clone's pilot
- Expected: anchor=AC-F1-11 reg3, retention=AC-F1-08 reg4, transport=null reg19
- Actual: status=200 unmet={'anchor': 'AC-F1-11', 'retention': 'AC-F1-08', 'transport': None} registers={'anchor': 3, 'retention': 4, 'transport': 19}
- Result: PASS
- Evidence: {"bytes": 84106, "unmet": {"anchor": "AC-F1-11", "retention": "AC-F1-08", "transport": null}, "registers": {"anchor": 3, "retention": 4, "transport": 19}}

---

# RE-RUN 2 — clean checkout + startup guards at `dev` @ `b447a11` (pass 26)

**Commit under test:** `b447a11` · **Owner:** `test-agent` · **Blocking:** yes
**Status:** `EXECUTED` · **Result: 10 scenarios, 10 pass, 0 FAIL** — after two
**harness** corrections, both recorded below rather than quietly fixed.

## Two harness corrections, and why neither is a build finding

1. **C2 first reported FAIL and was wrong.** It ran `git check-ignore var` on a
   fresh clone where `var/` does not exist. `.gitignore:37` is `var/` — a
   **directory-only** pattern — and git cannot classify a path it cannot see as
   a directory, so the bare form returns 1. `git check-ignore var/` and
   `git check-ignore var/warehouse.sqlite3` both return 0 against the same
   clone, and `git ls-tree -r HEAD` contains **zero** `var/` paths. The build
   was never in question; the query form was.
2. **C6 first reported FAIL and was also a harness defect — the SAME shape as
   the sequencing defect corrected in the first gate-11 run.** That run recorded
   that `warehouse.sqlite3` is created "lazily, on the first request that reads
   it". True — but `/queue` and `/audit`, the two routes I sampled after, are
   **not** such a request. Re-run sampling `var/` after `/health` and again
   after each of ten routes, the creating request is named exactly:
   **`GET /monitors`**. `broker_db.sqlite3` is created at startup, before any
   request.

Recorded in full because a harness defect reported as a build failure wastes a
`code-agent` pass, and a harness defect quietly corrected teaches nobody.

## The scenarios (C2 and C6 as re-run and corrected; C1, C3-C5, C7-C10 first-run)

### Scenario: C2 - var/ is gitignored and absent from a fresh checkout (harness corrected: a directory-only pattern cannot match a bare path git cannot classify as a directory when it does not exist)
- Status: EXECUTED
- Input: clone; test `git check-ignore` in three forms; list tracked var/ paths
- Expected: var/ absent; `var/` and `var/<file>` both ignored; zero tracked var/ paths
- Actual: exists=False rc(var)=1 rc(var/)=0 rc(var/file)=0 tracked_var=0
- Result: PASS
- Evidence: matched by '.gitignore:37:var/\tvar/' ; the bare `var` form returns 1 only because the directory is absent - that is a property of git, not of this build

### Scenario: C6 - the pilot creates var/ itself - broker_db.sqlite3 at STARTUP and warehouse.sqlite3 LAZILY, on the first request that actually reads it (harness corrected: /queue and /audit are not such a request)
- Status: EXECUTED
- Input: sample var/ after /health and again after each of ten routes plus the evidence export
- Expected: broker_db present at the first sample; warehouse present by the last; the creating request named
- Actual: first=['broker_db.sqlite3'] created_by='after GET /monitors' last=['broker_db.sqlite3', 'warehouse.sqlite3']
- Result: PASS
- Evidence:

```
[
 [
  "after /health, before any product route",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /queue",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /audit",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /inventory",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /approvals",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /catalogue",
  [
   "broker_db.sqlite3"
  ]
 ],
 [
  "after GET /monitors",
  [
   "broker_db.sqlite3",
   "warehouse.sqlite3"
  ]
 ],
 [
  "after GET /refusals",
  [
   "broker_db.sqlite3",
   "warehouse.sqlite3"
  ]
 ],
 [
  "after GET /ask",
  [
   "broker_db.sqlite3",
   "warehouse.sqlite3"
  ]
 ],
 [
  "after GET /my-probe-history",
  [
   "broker_db.sqlite3",
   "warehouse.sqlite3"
  ]
 ],
 [
  "after GET /audit/export/file",
  [
   "broker_db.sqlite3",
   "warehouse.sqlite3"
  ]
 ]
]
```
### Scenario: C1 - dev clones cleanly and the clone is the commit under test
- Status: EXECUTED
- Input: git clone dev -> scratch
- Expected: HEAD == b447a11
- Actual: HEAD=b447a11
- Result: PASS
- Evidence: b447a11

### Scenario: C3 - a credential in the environment refuses startup with exit 3, before uvicorn binds
- Status: EXECUTED
- Input: GES_WAREHOUSE_PASSWORD set, run backend/pilot.py
- Expected: exit 3, refusal message, nothing ever listening on 8021
- Actual: exit=3 listening=''
- Result: PASS
- Evidence:

```
refusing to start: the api process environment contains credentials it must not hold: GES_WAREHOUSE_PASSWORD
This is the single-process pilot: the guardrail broker runs inside this process, so a credential in this environment is reachable from the interface side by import alone.
```

### Scenario: C4 - CONCLAVE_ENV=production refuses startup with exit 2, before uvicorn binds
- Status: EXECUTED
- Input: CONCLAVE_ENV=production, run backend/pilot.py
- Expected: exit 2, topology refusal, nothing listening
- Actual: exit=2 listening=''
- Result: PASS
- Evidence:

```
refusing to start: backend/pilot.py puts the guardrail broker in the same process as the interface, which is refused in production. Run backend/ges/run.py and backend/app/run.py.
```

### Scenario: C5 - a refused start creates no state
- Status: EXECUTED
- Input: after both refusals, look for var/
- Expected: var/ still absent
- Actual: var_exists=False
- Result: PASS
- Evidence: 

### Scenario: C7 - all twelve routes and /health serve 200 from the clean checkout
- Status: EXECUTED
- Input: GET each
- Expected: 200 on all thirteen
- Actual: {"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200, "/health": 200}
- Result: PASS
- Evidence: 

### Scenario: C8 - the full staff-403 -> controller-403 -> same-person-refused -> override-200 -> export-200 chain reproduces from the clean checkout with a BALANCED file
- Status: EXECUTED
- Input: drive the chain over HTTP against the clone
- Expected: 403 / 403 / not-200 / 200 / 200, Dr == Cr non-zero
- Actual: staff=403 controller=403 same_person=403 override=200 export=200 group=['CS-66456182B911'] lines=2 Dr=86340.0 Cr=86340.0
- Result: PASS
- Evidence: {"group": ["CS-66456182B911"], "dr": 86340.0, "cr": 86340.0, "authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad"}

### Scenario: C9 - the evidence export from the clean checkout carries the same FOUR integrity sections, register 3/4/19/15
- Status: EXECUTED
- Input: GET /audit/export/file from the clone
- Expected: four sections with the same references
- Actual: {"anchor": {"unmet_criterion": "AC-F1-11", "register_entry": 3}, "provenance": {"unmet_criterion": null, "register_entry": 15}, "retention": {"unmet_criterion": "AC-F1-08", "register_entry": 4}, "transport": {"unmet_criterion": null, "register_entry": 19}}
- Result: PASS
- Evidence:

```
{"anchor": {"unmet_criterion": "AC-F1-11", "register_entry": 3}, "provenance": {"unmet_criterion": null, "register_entry": 15}, "retention": {"unmet_criterion": "AC-F1-08", "register_entry": 4}, "transport": {"unmet_criterion": null, "register_entry": 19}}
```

### Scenario: C10 - register 15's disclosure is in the clean-checkout export too, asserted as prose with the version identifier stripped
- Status: EXECUTED
- Input: count each REQUIRED_PHRASE in the clone's export
- Expected: every phrase present
- Actual: {"synthetic fixture data": 1, "synthetic close fixture": 1, "not from an Oracle-sourced warehouse": 1, "cannot support a posting or an assurance conclusion about a real ledger": 1}
- Result: PASS
- Evidence: 
