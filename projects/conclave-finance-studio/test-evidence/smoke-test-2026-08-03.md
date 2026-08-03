# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-17 UX redesign
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`6bf8ed9`** · parent repo @ **`5268e9b`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot API_PORT=8021 GES_PORT=8022 .venv/bin/python backend/pilot.py`, then **stdlib HTTP** to `http://127.0.0.1:8021` — no `TestClient`, no in-process shortcut
**Exit code:** 1 (one scenario failed)
**Scenarios: 19 — PASS 18, FAIL 1**

Driven against the **pilot as found**: the warehouse and decision ledger already
on disk in `dev/var/`, not a fresh seed.

## Process lifecycle

`backend/pilot.py` ends in a blocking `uvicorn.run(...)`, so it cannot run to
completion. It was **started, exercised and reaped inside a single command
invocation**, twice for the smoke and twice more for the rendered-UI work.
`start_new_session=True` makes the launcher pid its own process-group id;
teardown calls `os.killpg` on **that group and only that group**. **No
name-based sweep of any kind was run** — a name-matched `pkill` killed the
human's pilot once already.

- human's pilot **pid 39289, port 8030**: verified alive BEFORE and AFTER every
  invocation
- ports 8030/8031: never probed
- `lsof` on 8021 and 8022 after every teardown: **empty**

One `pkill` was issued during this pass, scoped to the literal string
`tagent_order` — a token that appears only in this agent's own pytest
invocations and in no product process. pid 39289 was re-verified listening on
8030 immediately afterwards.

## Effect on the shared ledger, disclosed

The smoke drives the **real** export path, so it writes to
`dev/var/broker_db.sqlite3` — the same file the human's instance on 8030 uses.
It grew **10,559,488 → 10,579,968 bytes (+20,480)** across the pass. Not a
fault: the pilot is the real application and the live-ledger guard's scope is
tests, all eight of whose whole-tree runs left the file byte-identical.

---

### Scenario: S1 - /health serves
- Status: EXECUTED
- Input: GET /health
- Expected: 200
- Actual: 200
- Result: PASS
- Evidence: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`

### Scenario: S2 - every product GET route serves 200 under the pass-17 IA
- Status: EXECUTED
- Input: GET on 17 parameterless product routes
- Expected: 200 on all
- Actual: {"/": 200, "/queue": 200, "/exceptions": 200, "/review": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/readiness": 200, "/dispositions": 200, "/audit/export": 200, "/audit/export/file": 200, "/health": 200}
- Result: PASS
- Evidence: `{"/": 200, "/queue": 200, "/exceptions": 200, "/review": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/readiness": 200, "/dispositions": 200, "/audit/export": 200, "/audit/export/file": 200, "/health": 200}`

### Scenario: S3 - the merged queue serves one screen under all three addresses
- Status: EXECUTED
- Input: GET /queue, /exceptions, /review
- Expected: identical bodies after the inlined stylesheet
- Actual: identical
- Result: PASS
- Evidence: `byte lengths {'/queue': 15957, '/exceptions': 15957, '/review': 15957}`

### Scenario: S4 - the entry point is the queue and Ask is one link from it
- Status: EXECUTED
- Input: GET /
- Expected: exception-queue present, /ask linked, no nl-input on /
- Actual: queue=True ask_linked=True no_nl_input=True
- Result: PASS
- Evidence: `hrefs on / include /ask: True`

### Scenario: S5 - every module that left the queue is visible on the run it is a property of
- Status: EXECUTED
- Input: GET /evidence/run/RUN-2026-06-0412 and GET /
- Expected: six modules present on the run report, three absent from the queue
- Actual: on_run={'fidelity-region': True, 'boundary-region': True, 'coding-region': True, 'boundary-check-table': True, 'check-not-run': True, 'recall-bias-label': True} off_queue={'fidelity-region': True, 'boundary-region': True, 'coding-region': True}
- Result: PASS
- Evidence: `{"on_run": {"fidelity-region": true, "boundary-region": true, "coding-region": true, "boundary-check-table": true, "check-not-run": true, "recall-bias-label": true}, "off_queue": {"fidelity-region": true, "boundary-region": true, "coding-region": true}}`

### Scenario: S6 - the evidential chain finding -> run -> agent -> readiness walks over HTTP
- Status: EXECUTED
- Input: each hop uses the href the PREVIOUS served screen rendered
- Expected: four 200s ending on a readiness page
- Actual: [["/review/ITEM-21400-CP", 200], ["/evidence/run/RUN-2026-06-0412", 200], ["/evidence/agent/agent.crossperiod-surveillance", 200], ["/readiness?agent=agent.crossperiod-surveillance", 200]]
- Result: PASS
- Evidence: `[["/review/ITEM-21400-CP", 200], ["/evidence/run/RUN-2026-06-0412", 200], ["/evidence/agent/agent.crossperiod-surveillance", 200], ["/readiness?agent=agent.crossperiod-surveillance", 200]]`

### Scenario: S7 - the dossier carries exactly one link, the back-reference, and still fetches nothing
- Status: EXECUTED
- Input: GET the dossier the finding links to; count every external-reference construct
- Expected: 8 external-reference counts zero; exactly one href; it is the back-reference
- Actual: ext={'<script': 0, '<link': 0, '<img': 0, '@import': 0, 'url(': 0, 'srcset': 0, 'http://': 0, 'https://': 0} hrefs=['/review/ITEM-21400-CP'] back=/review/ITEM-21400-CP
- Result: PASS
- Evidence: `{"external": {"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0, "srcset": 0, "http://": 0, "https://": 0}, "hrefs": ["/review/ITEM-21400-CP"], "bytes": 33066}`

### Scenario: S8 - the one Approve control is on /approvals/<proposal> and nowhere else
- Status: EXECUTED
- Input: GET /proposal/..., /approvals/..., /review/<item>
- Expected: approve-lines only on the approval screen, linked from the proposal
- Actual: proposal=False approval=True item=False linked=True
- Result: PASS
- Evidence: `approve-lines present only on /approvals/PROP-2026-06-0031`

### Scenario: S9 - AC-F40-11: the journal lines precede the approve control on the approval screen
- Status: EXECUTED
- Input: byte offsets of journal-lines and approve-lines in the served /approvals page
- Expected: journal-lines earlier in reading order
- Actual: journal_lines@27796 approve_lines@29167
- Result: PASS
- Evidence: `offsets 27796 < 29167`

### Scenario: S10 - four of five agents render every condition not_yet_evaluable, never a pass
- Status: EXECUTED
- Input: GET /readiness?agent=<id> for every agent the selector offers
- Expected: 5 agents; 4 wholly not_yet_evaluable; no precision figure where nothing was computed; data-ready=false everywhere
- Actual: agents=5 all_nye=4 fabricated=[] claims_ready=[]
- Result: PASS
- Evidence: `{
 "/readiness?agent=agent.anomaly-detect": {
  "states": [
   "not_yet_evaluable"
  ],
  "n": 5,
  "ready": "false",
  "precision_figure": false,
  "precision_absent": true
 },
 "/readiness?agent=agent.coding-detect": {
  "states": [
   "not_yet_evaluable"
  ],
  "n": 5,
  "ready": "false",
  "precision_figure": false,
  "precision_absent": true
 },
 "/readiness?agent=agent.crossperiod-surveillance": {
  "states": [
   "met",
   "not_met",
   "not_yet_evaluable"
  ],
  "n": 5,
  "ready": "false",
  "precision_figure": true,
  "precision_absent": false
 },
 "/readiness?agent=agent.fidelity-check": {
  "states": [
   "not_yet_evaluable"
  ],
  "n": 5,
  "ready": "false",
  "precision_figure": false,
  "precision_absent": true
 },
 "/readiness?agent=agent.omission-detector": {
  "states": [
   "not_yet_evaluable"
  ],
  "n": 5,
  "ready": "false",
  "precision_figure": false,
  "precision_absent": true
 }
}`

### Scenario: S11 - the author-id / registry-id disagreement is stated on the agent's own page
- Status: EXECUTED
- Input: GET /evidence/agent/agent.crossperiod-surveillance
- Expected: agent-not-in-registry rendered rather than the agent dropped
- Actual: present=True
- Result: PASS
- Evidence: `no entry in the principal registry`

### Scenario: S12 - AC-F5-02: an agent that performed an action appears in the Inventory
- Status: EXECUTED
- Input: GET /inventory, and the authoring agent of every queue item
- Expected: every authoring agent listed in the Inventory
- Actual: absent from /inventory: ['agent.anomaly-detect', 'agent.crossperiod-surveillance', 'agent.fidelity-check', 'agent.omission-detector']
- Result: FAIL
- Evidence: `{"listed": ["agent.anomaly_detector@1", "agent.coding-detect", "agent.omission_detector@1", "agent.threshold_widening@1", "human.controller.jdoe", "human.platform.admin", "service.certifier", "user.a.reyes", "user.d.okafor", "user.j.mbeki", "user.s.haddad"], "authors": ["agent.anomaly-detect", "agent.coding-detect", "agent.crossperiod-surveillance", "agent.fidelity-check", "agent.omission-detector"], "missing": ["agent.anomaly-detect", "agent.crossperiod-surveillance", "agent.fidelity-check", "agent.omission-detector"]}`

### Scenario: S13 - the real export path, driven as found on 8021
- Status: EXECUTED
- Input: viewing-as -> /approvals -> approve -> override (values read off the rendered controls) -> export
- Expected: the export terminates in a retrievable file
- Actual: viewing=200 approve=403 override=200 export=200 file=['/export/CS-E5AC31C89A4A.csv']
- Result: PASS
- Evidence: `{"approve": 403, "override": 200, "override_body": {"reason_code": "material_close_deadline", "authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad"}, "reason_codes_served": ["material_close_deadline", "known_data_defect_upstream", "regulatory_instruction", "documented_control_exception"], "authoriser_fields": ["authoriser_a", "authoriser_b"], "export": 200, "authorised_on": "synthetic_attestation", "file": ["/export/CS-E5AC31C89A4A.csv"]}`

### Scenario: S14 - the produced export file is retrievable and carries the FBDI header
- Status: EXECUTED
- Input: GET /export/CS-E5AC31C89A4A.csv
- Expected: 200, FBDI header, at least one data line
- Actual: status=200 lines=3
- Result: PASS
- Evidence: `STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,REFERENCE21,REFERENCE22,REFERENCE23,R`

### Scenario: S15 - AC-F40-18: the export names its authorisation basis
- Status: EXECUTED
- Input: the export screen from S13
- Expected: synthetic_attestation, never a stored register pass state
- Actual: synthetic_attestation
- Result: PASS
- Evidence: `data-authorised-on='synthetic_attestation'`

### Scenario: S16 - registers 3 and 4 are named as unmet on the auditor's screen
- Status: EXECUTED
- Input: GET /audit/export
- Expected: AC-F1-11 and AC-F1-08 both named as unmet
- Actual: F1-11=True F1-08=True
- Result: PASS
- Evidence: `both criterion IDs present in the served page`

### Scenario: S17 - no green colour token on the served surface
- Status: EXECUTED
- Input: GET /queue, scanning the served bytes including the inlined stylesheet
- Expected: no green colour literal
- Actual: matches=[]
- Result: PASS
- Evidence: `green literals found: []`

### Scenario: S18 - register 15's non-dismissable pilot strip renders on every screen
- Status: EXECUTED
- Input: GET four screens including two new object pages
- Expected: present on all four
- Actual: {"/queue": true, "/approvals": true, "/evidence/run/RUN-2026-06-0412": true, "/ask": true}
- Result: PASS
- Evidence: `{"/queue": true, "/approvals": true, "/evidence/run/RUN-2026-06-0412": true, "/ask": true}`

### Scenario: S19 - an object this build does not have is refused, not substituted
- Status: EXECUTED
- Input: GET four unknown object addresses
- Expected: 404 on all four
- Actual: {"/evidence/run/RUN-NOT-A-RUN": 404, "/evidence/agent/agent.invented": 404, "/evidence/dataset/ds.invented": 404, "/readiness?agent=agent.invented": 404}
- Result: PASS
- Evidence: `{"/evidence/run/RUN-NOT-A-RUN": 404, "/evidence/agent/agent.invented": 404, "/evidence/dataset/ds.invented": 404, "/readiness?agent=agent.invented": 404}`
