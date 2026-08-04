# Test evidence — post-deploy smoke, against the SERVED pilot on 8021

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-19 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`e00a214`** · parent repo @ **`8dcb490`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**29 scenarios, 29 pass, 0 fail, exit 0.**

Driven over **stdlib HTTP against a real served process** — no `TestClient`, no
ASGI shortcut. The pilot was started on 8021/8022, driven, and reaped **inside a
single command invocation**, in its own process group (`start_new_session=True`),
torn down with `os.killpg` on **that group only**. No name-based sweep was run at
any point.

## Process lifecycle — the human's pilot

| | |
|---|---|
| human's pilot | **pid 59422, port 8030** |
| alive BEFORE this invocation | **yes** |
| alive AFTER this invocation | **yes** |
| 8030 / 8031 probed | **never** |
| my listeners on 8021 / 8022 after teardown | **`''` / `''`** (empty) |

The pid differs from last pass's 50367 — the human restarted their pilot between
runs. It was re-read from `lsof` at the start of this pass rather than carried
forward, and checked again after every invocation.

## The real export path

S13 drove `viewing-as → /approvals → approve → override → export` using the
values read off the rendered controls, and terminated in a retrievable file:
`/export/CS-0034B894B391.csv`, FBDI header present, 3 lines. The approve leg
returned **403** and the override leg **200** — the refusal-then-override path,
not a bypass. The shared ledger grew **10,739,712 → 10,780,672 bytes** across the
smoke and rendered-UI invocations, which is the evidence the write path really
ran; the 2,987-scenario test tree left it byte-identical.

## The S22 correction

Pass 18 recorded S22 as **MIS-TARGETED** — it accepted a non-200 from the API
port as a pass. The re-target found the real reason: `backend/pilot.py` calls
`pilot_transport.install()`, which puts the broker **in-process**, so there is no
GES HTTP listener on 8022 at all. S22 now asserts that fact (connection refused,
by design) *and* that the broker's own statement string reaches a reader on the
served screen instead of over a port. It can now fail in both directions.

---

### Scenario: S1 - /health serves
- Status: EXECUTED
- Input: GET /health
- Expected: 200
- Actual: 200
- Result: PASS
- Evidence: {"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}

### Scenario: S2 - every product GET route serves 200 under the pass-17 IA
- Status: EXECUTED
- Input: GET on 17 parameterless product routes
- Expected: 200 on all
- Actual: {"/": 200, "/queue": 200, "/exceptions": 200, "/review": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/readiness": 200, "/dispositions": 200, "/audit/export": 200, "/audit/export/file": 200, "/health": 200}
- Result: PASS
- Evidence: {"/": 200, "/queue": 200, "/exceptions": 200, "/review": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/readiness": 200, "/dispositions": 200, "/audit/export": 200, "/audit/export/file": 200, "/health": 200}

### Scenario: S3 - the merged queue serves one screen under all three addresses
- Status: EXECUTED
- Input: GET /queue, /exceptions, /review
- Expected: identical bodies after the inlined stylesheet
- Actual: identical
- Result: PASS
- Evidence: byte lengths {'/queue': 15987, '/exceptions': 15987, '/review': 15987}

### Scenario: S4 - the entry point is the queue and Ask is one link from it
- Status: EXECUTED
- Input: GET /
- Expected: exception-queue present, /ask linked, no nl-input on /
- Actual: queue=True ask_linked=True no_nl_input=True
- Result: PASS
- Evidence: hrefs on / include /ask: True

### Scenario: S5 - every module that left the queue is visible on the run it is a property of
- Status: EXECUTED
- Input: GET /evidence/run/RUN-2026-06-0412 and GET /
- Expected: six modules present on the run report, three absent from the queue
- Actual: on_run={'fidelity-region': True, 'boundary-region': True, 'coding-region': True, 'boundary-check-table': True, 'check-not-run': True, 'recall-bias-label': True} off_queue={'fidelity-region': True, 'boundary-region': True, 'coding-region': True}
- Result: PASS
- Evidence: {"on_run": {"fidelity-region": true, "boundary-region": true, "coding-region": true, "boundary-check-table": true, "check-not-run": true, "recall-bias-label": true}, "off_queue": {"fidelity-region": true, "boundary-region": true, "coding-region": true}}

### Scenario: S6 - the evidential chain finding -> run -> agent -> readiness walks over HTTP
- Status: EXECUTED
- Input: each hop uses the href the PREVIOUS served screen rendered
- Expected: four 200s ending on a readiness page
- Actual: [["/review/ITEM-21400-CP", 200], ["/evidence/run/RUN-2026-06-0412", 200], ["/evidence/agent/agent.crossperiod-surveillance", 200], ["/readiness?agent=agent.crossperiod-surveillance", 200]]
- Result: PASS
- Evidence: [["/review/ITEM-21400-CP", 200], ["/evidence/run/RUN-2026-06-0412", 200], ["/evidence/agent/agent.crossperiod-surveillance", 200], ["/readiness?agent=agent.crossperiod-surveillance", 200]]

### Scenario: S7 - the dossier carries exactly one link, the back-reference, and still fetches nothing
- Status: EXECUTED
- Input: GET the dossier the finding links to; count every external-reference construct
- Expected: 8 external-reference counts zero; exactly one href; it is the back-reference
- Actual: ext={'<script': 0, '<link': 0, '<img': 0, '@import': 0, 'url(': 0, 'srcset': 0, 'http://': 0, 'https://': 0} hrefs=['/review/ITEM-21400-CP'] back=/review/ITEM-21400-CP
- Result: PASS
- Evidence: {"external": {"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0, "srcset": 0, "http://": 0, "https://": 0}, "hrefs": ["/review/ITEM-21400-CP"], "bytes": 32473}

### Scenario: S8 - the one Approve control is on /approvals/<proposal> and nowhere else
- Status: EXECUTED
- Input: GET /proposal/..., /approvals/..., /review/<item>
- Expected: approve-lines only on the approval screen, linked from the proposal
- Actual: proposal=False approval=True item=False linked=True
- Result: PASS
- Evidence: approve-lines present only on /approvals/PROP-2026-06-0031

### Scenario: S9 - AC-F40-11: the journal lines precede the approve control on the approval screen
- Status: EXECUTED
- Input: byte offsets of journal-lines and approve-lines in the served /approvals page
- Expected: journal-lines earlier in reading order
- Actual: journal_lines@27233 approve_lines@28604
- Result: PASS
- Evidence: offsets 27233 < 28604

### Scenario: S10 - four of five agents render every condition not_yet_evaluable, never a pass
- Status: EXECUTED
- Input: GET /readiness?agent=<id> for every agent the selector offers
- Expected: 5 agents; 4 wholly not_yet_evaluable; no precision figure where nothing was computed; data-ready=false everywhere
- Actual: agents=5 all_nye=4 fabricated=[] claims_ready=[]
- Result: PASS
- Evidence: {  "/readiness?agent=agent.anomaly-detect": {   "states": [    "not_yet_evaluable"   ],   "n": 5,   "ready": "false",   "precision_figure": false,   "precision_absent": true  },  "/readiness?agent=agent.coding-detect": {   "states": [    "not_yet_evaluable"   ],   "n": 5,   "ready": "false",   "precision_figure": false,   "precision_absent": true  },  "/readiness?agent=agent.crossperiod-surveillance": {   "states": [    "met",    "not_met",    "not_yet_evaluable"   ],   "n": 5,   "ready": "false",   "precision_figure": true,   "precision_absent": false  },  "/readiness?agent=agent.fidelity-che

### Scenario: S11 - the author-id / registry-id disagreement is stated on the agent's own page
- Status: EXECUTED
- Input: GET /evidence/agent/agent.crossperiod-surveillance
- Expected: agent-not-in-registry rendered rather than the agent dropped
- Actual: present=True
- Result: PASS
- Evidence: no entry in the principal registry

### Scenario: S12 - AC-F5-02 is DISCLOSED unmet on /inventory, not claimed
- Status: EXECUTED
- Input: GET /inventory
- Expected: 4 absent acting agents named, AC-F5-02 stated NOT met, and the unqualified sentence gone
- Actual: absent=['agent.anomaly-detect', 'agent.crossperiod-surveillance', 'agent.fidelity-check', 'agent.omission-detector'] notice=True unqualified_sentence=False
- Result: PASS
- Evidence: {"absent": ["agent.anomaly-detect", "agent.crossperiod-surveillance", "agent.fidelity-check", "agent.omission-detector"], "has_notice": true, "unqualified_on_inventory": false}

### Scenario: S12b - the unqualified sentence is gone from EVERY surface, not one
- Status: EXECUTED
- Input: GET /evidence/agent/<id> for each of the four agents /inventory names as absent
- Expected: none of the four pages repeats the claim the build records as unmet
- Actual: {"agent.anomaly-detect": false, "agent.crossperiod-surveillance": false, "agent.fidelity-check": false, "agent.omission-detector": false}
- Result: PASS
- Evidence: {"agent.anomaly-detect": false, "agent.crossperiod-surveillance": false, "agent.fidelity-check": false, "agent.omission-detector": false}

### Scenario: S12c - every lineage row on the served screen states scope and INCOMPLETE
- Status: EXECUTED
- Input: GET /inventory, reading data-complete/data-scope off the rendered rows
- Expected: every row false + decision_ledger
- Actual: rows=11 complete=['false'] scope=['decision_ledger']
- Result: PASS
- Evidence: {"rows": 11, "complete_values": ["false"], "scope_values": ["decision_ledger"]}

### Scenario: S13 - the real export path, driven as found on 8021
- Status: EXECUTED
- Input: viewing-as -> /approvals -> approve -> override (values read off the rendered controls) -> export
- Expected: the export terminates in a retrievable file
- Actual: viewing=200 approve=403 override=200 export=200 file=['/export/CS-0034B894B391.csv']
- Result: PASS
- Evidence: {"approve": 403, "override": 200, "override_body": {"reason_code": "material_close_deadline", "authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad"}, "reason_codes_served": ["material_close_deadline", "known_data_defect_upstream", "regulatory_instruction", "documented_control_exception"], "authoriser_fields": ["authoriser_a", "authoriser_b"], "export": 200, "authorised_on": "synthetic_attestation", "file": ["/export/CS-0034B894B391.csv"]}

### Scenario: S14 - the produced export file is retrievable and carries the FBDI header
- Status: EXECUTED
- Input: GET /export/CS-0034B894B391.csv
- Expected: 200, FBDI header, at least one data line
- Actual: status=200 lines=3
- Result: PASS
- Evidence: STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,REFERENCE21,REFERENCE22,REFERENCE23,R

### Scenario: S15 - AC-F40-18: the export names its authorisation basis
- Status: EXECUTED
- Input: the export screen from S13
- Expected: synthetic_attestation, never a stored register pass state
- Actual: synthetic_attestation
- Result: PASS
- Evidence: data-authorised-on='synthetic_attestation'

### Scenario: S16 - registers 3 and 4 are named as unmet on the auditor's screen
- Status: EXECUTED
- Input: GET /audit/export
- Expected: AC-F1-11 and AC-F1-08 both named as unmet
- Actual: F1-11=True F1-08=True
- Result: PASS
- Evidence: both criterion IDs present in the served page

### Scenario: S17 - no green colour token on the served surface
- Status: EXECUTED
- Input: GET /queue, scanning the served bytes including the inlined stylesheet
- Expected: no green colour literal
- Actual: matches=[]
- Result: PASS
- Evidence: green literals found: []

### Scenario: S18 - register 15's non-dismissable pilot strip renders on every screen
- Status: EXECUTED
- Input: GET four screens including two new object pages
- Expected: present on all four
- Actual: {"/queue": true, "/approvals": true, "/evidence/run/RUN-2026-06-0412": true, "/ask": true}
- Result: PASS
- Evidence: {"/queue": true, "/approvals": true, "/evidence/run/RUN-2026-06-0412": true, "/ask": true}

### Scenario: S19 - an object this build does not have is refused, not substituted
- Status: EXECUTED
- Input: GET four unknown object addresses
- Expected: 404 on all four
- Actual: {"/evidence/run/RUN-NOT-A-RUN": 404, "/evidence/agent/agent.invented": 404, "/evidence/dataset/ds.invented": 404, "/readiness?agent=agent.invented": 404}
- Result: PASS
- Evidence: {"/evidence/run/RUN-NOT-A-RUN": 404, "/evidence/agent/agent.invented": 404, "/evidence/dataset/ds.invented": 404, "/readiness?agent=agent.invented": 404}

### Scenario: S20 - the served lockup puts .ctx AFTER the row, not inside it
- Status: EXECUTED
- Input: GET /queue, reading the served markup of the lockup block
- Expected: .lockup-row present and .ctx a following sibling
- Actual: row=True ctx_after_row=True
- Result: PASS
- Evidence: served markup: .lockup > [.lockup-row, .ctx]

### Scenario: S21 - the orphaned rule the defect shipped as is gone from the served CSS
- Status: EXECUTED
- Input: GET /queue, scanning the inlined stylesheet
- Expected: .lockup .ctx present, .brand absent
- Actual: lockup_ctx=True brand=False
- Result: PASS
- Evidence: served bytes, not the module source

### Scenario: S22 - the pilot exposes no GES HTTP port, and the broker's answer still reaches a reader
- Status: EXECUTED
- Input: connect to 127.0.0.1:8022 /ges/inventory, then read /inventory
- Expected: connection refused on 8022 (in-process transport, by design) AND the UNKNOWN answer with its scope rendered on the screen
- Actual: ges_port_status=0 answer_node=True statement_rendered=True
- Result: PASS
- Evidence: {"ges_8022": "connection refused: [Errno 61] Connection refused", "answer_present": true, "statement_rendered": true}

### Scenario: S25 - each absent-agent link on /inventory lands on THAT agent's page
- Status: EXECUTED
- Input: GET /inventory, follow every absent-agent-link, read the h1
- Expected: four links, four 200s, each h1 the principal id the row names
- Actual: {"agent.anomaly-detect": {"href": "/evidence/agent/agent.anomaly-detect", "status": 200, "h1": "agent.anomaly-detect"}, "agent.crossperiod-surveillance": {"href": "/evidence/agent/agent.crossperiod-surveillance", "status": 200, "h1": "agent.crossperiod-surveillance"}, "agent.fidelity-check": {"href": "/evidence/agent/agent.fidelity-check", "status": 200, "h1": "agent.fidelity-check"}, "agent.omission-detector": {"href": "/evidence/agent/agent.omission-detector", "status": 200, "h1": "agent.omission-detector"}}
- Result: PASS
- Evidence: {  "agent.anomaly-detect": {   "href": "/evidence/agent/agent.anomaly-detect",   "status": 200,   "h1": "agent.anomaly-detect"  },  "agent.crossperiod-surveillance": {   "href": "/evidence/agent/agent.crossperiod-surveillance",   "status": 200,   "h1": "agent.crossperiod-surveillance"  },  "agent.fidelity-check": {   "href": "/evidence/agent/agent.fidelity-check",   "status": 200,   "h1": "agent.fidelity-check"  },  "agent.omission-detector": {   "href": "/evidence/agent/agent.omission-detector",   "status": 200,   "h1": "agent.omission-detector"  } }

### Scenario: S26 - the population answer is rendered UNKNOWN on /inventory
- Status: EXECUTED
- Input: GET /inventory
- Expected: unregistered-actors-answer present, data-computable=false, UNKNOWN in the text
- Actual: node=True computable=false unknown_in_text=True
- Result: PASS
- Evidence: {"present": true, "data_computable": "false"}

### Scenario: S27 - the unqualified AC-F5-02 claim is on NO served screen
- Status: EXECUTED
- Input: crawl from / over real HTTP following rendered links
- Expected: zero offenders AND the four agent pages actually reached (so it cannot pass by reaching nothing)
- Actual: crawled=46 offenders=[] agent_pages=['/evidence/agent/agent.anomaly-detect', '/evidence/agent/agent.coding-detect', '/evidence/agent/agent.crossperiod-surveillance', '/evidence/agent/agent.fidelity-check', '/evidence/agent/agent.omission-detector']
- Result: PASS
- Evidence: {  "urls_crawled": 46,  "offenders": [],  "agent_pages": [   "/evidence/agent/agent.anomaly-detect",   "/evidence/agent/agent.coding-detect",   "/evidence/agent/agent.crossperiod-surveillance",   "/evidence/agent/agent.fidelity-check",   "/evidence/agent/agent.omission-detector"  ] }

### Scenario: S23 - each alias really serves its canonical screen over real HTTP
- Status: EXECUTED
- Input: GET each alias and its canonical, comparing the bytes after </style>
- Expected: identical bodies
- Actual: {"/exceptions": true, "/review": true}
- Result: PASS
- Evidence: {"/exceptions": true, "/review": true}

### Scenario: S24 - the post-approval seal renders on the screen you go BACK to
- Status: EXECUTED
- Input: GET the approval and proposal screens after the S13 approval
- Expected: the approved artefact is rendered with its seal
- Actual: {"/approvals": {"status": 200, "seal": true, "card_approved": false}, "/approvals/PROP-2026-06-0031": {"status": 200, "seal": true, "card_approved": true}, "/proposal/PROP-2026-06-0031": {"status": 200, "seal": true, "card_approved": false}}
- Result: PASS
- Evidence: {"/approvals": {"status": 200, "seal": true, "card_approved": false}, "/approvals/PROP-2026-06-0031": {"status": 200, "seal": true, "card_approved": true}, "/proposal/PROP-2026-06-0031": {"status": 200, "seal": true, "card_approved": false}}
