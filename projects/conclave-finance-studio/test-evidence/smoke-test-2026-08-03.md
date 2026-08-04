# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test — re-run after the pass-18 loop-back
**Date:** 2026-08-03
**Commit under test:** `dev` @ **`1b1b56e`** · parent repo @ **`2f9b373`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot API_PORT=8021 GES_PORT=8022 .venv/bin/python backend/pilot.py`,
then **stdlib HTTP** to `http://127.0.0.1:8021` — no `TestClient`, no
in-process shortcut
**Exit code:** 1 (one scenario failed)
**Scenarios: 26 — PASS 24, FAIL 1, MIS-TARGETED 1**

Driven against the **pilot as found**: the warehouse and decision ledger
already on disk in `dev/var/`, not a fresh seed.

## Process lifecycle

`backend/pilot.py` ends in a blocking `uvicorn.run(...)`, so it cannot run to
completion. It was **started, exercised and reaped inside a single command
invocation**, twice across this pass (once for the smoke, once for the
rendered-UI work). `start_new_session=True` makes the launcher pid its own
process-group id; teardown calls `os.killpg` on **that group and only that
group**. **No name-based sweep of any kind was run.**

- the human's pilot, **pid 50367, port 8030**: `alive BEFORE: True`,
  `alive AFTER: True` on every invocation
- ports 8030/8031: never probed, never connected to, never signalled
- `listener on 8021 after teardown: ''`, `listener on 8022 after teardown: ''`

## Effect on the shared ledger, disclosed

The smoke drives the **real** export path, so it writes to
`dev/var/broker_db.sqlite3` — the same file the human's instance on 8030 uses.
It grew **10,702,848 → 10,723,328 bytes (+20,480)**. Not a fault: the pilot is
the real application. The *test tree* left it byte-identical across all six
whole-tree runs, which is what the live-ledger guard is for.

---

### Scenario: S1 - /health serves
- Status: EXECUTED · Input: `GET /health` · Expected: 200 · Actual: **200**
- Result: PASS
- Evidence: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`

### Scenario: S2 - every product GET route serves 200
- Status: EXECUTED · Input: 17 product routes · Expected: 200 on all
- Actual: **200 on all 17**
- Result: PASS
- Evidence: `/`, `/queue`, `/exceptions`, `/review`, `/approvals`, `/ask`, `/catalogue`, `/monitors`, `/audit`, `/inventory`, `/refusals`, `/my-probe-history`, `/readiness`, `/dispositions`, `/audit/export`, `/audit/export/file`, `/health` — all 200

### Scenario: S3 - the merged queue serves one screen under all three addresses
- Status: EXECUTED · Expected: identical bodies · Actual: **identical**
- Result: PASS · Evidence: bytes after `</style>` compared, `/queue` = `/exceptions` = `/review`

### Scenario: S4 - the entry point is the queue and Ask is one link from it
- Status: EXECUTED · Actual: `queue=True ask_linked=True no_nl_input=True`
- Result: PASS

### Scenario: S5 - every module that left the queue is visible on the run it is a property of
- Status: EXECUTED · Actual: all regions present on `/evidence/run/...`
- Result: PASS · Evidence: `fidelity-region`, `boundary-region`, `coding-region`, `boundary-check-table`, `check-not-run`, `recall-bias-lab` all `True`

### Scenario: S6 - the evidential chain walks over HTTP
- Status: EXECUTED · Actual: `/review/ITEM-21400-CP` 200 → `/evidence/run/RUN-2026-06-0412` 200 → `/evidence/agent/agent.crossperiod-surveillance` 200 → `/readiness?agent=...` 200
- Result: PASS

### Scenario: S7 - the dossier carries exactly one link and fetches nothing
- Status: EXECUTED · Actual: `{'<script':0,'<link':0,'<img':0,'@import':0,'url(':0,'srcset':0,'http://':0,'https://':0}`, one href
- Result: PASS · Evidence: `hrefs=['/review/ITEM-21400-CP']`

### Scenario: S8 - the one Approve control is on /approvals/<proposal> and nowhere else
- Status: EXECUTED · Actual: `proposal=False approval=True item=False linked=True`
- Result: PASS

### Scenario: S9 - AC-F40-11: journal lines precede the approve control
- Status: EXECUTED · Actual: `journal_lines@27233 approve_lines@28604`
- Result: PASS

### Scenario: S10 - four of five agents render every condition not_yet_evaluable
- Status: EXECUTED · Actual: `agents=5 all_nye=4 fabricated=[] claims_ready=[]`
- Result: PASS

### Scenario: S11 - the author-id / registry-id disagreement is stated on the agent's own page
- Status: EXECUTED · Actual: `present=True`
- Result: PASS · Evidence: *"no entry in the principal registry"* rendered

### Scenario: S12 - AC-F5-02 is DISCLOSED unmet on /inventory, not claimed
- Status: EXECUTED
- Input: `GET /inventory`
- Expected: 4 absent acting agents named, `AC-F5-02` stated NOT met, the
  unqualified sentence gone
- Actual: `absent=['agent.anomaly-detect','agent.crossperiod-surveillance','agent.fidelity-check','agent.omission-detector'] notice=True unqualified_sentence=False`
- Result: PASS
- Evidence: `{"absent": [...4...], "has_notice": true, "unqualified_on_inventory": false}`

### Scenario: S12b - **FINDING: the unqualified sentence is gone from ONE surface, not every surface**
- Status: EXECUTED
- Input: `GET /evidence/agent/<id>` for each of the four agents `/inventory`
  names as absent and links to
- Expected: none of the four repeats the claim the build records as unmet
- Actual: **all four carry it verbatim** —
  `{"agent.anomaly-detect": true, "agent.crossperiod-surveillance": true,
  "agent.fidelity-check": true, "agent.omission-detector": true}`
- Result: **FAIL**
- Evidence: rendered confirmation and full analysis in
  `rendered-ui-2026-08-03.md` R7 and `functional-2026-08-03.md` Finding 1

### Scenario: S12c - every lineage row on the served screen states scope and INCOMPLETE
- Status: EXECUTED · Actual: `rows=11 complete=['false'] scope=['decision_ledger']`
- Result: PASS

### Scenario: S13 - the real export path, driven as found on 8021
- Status: EXECUTED
- Input: viewing-as → `/approvals` → approve → override (values read off the
  rendered controls, not hard-coded) → export
- Expected: the export terminates in a retrievable file
- Actual: `viewing=200 approve=403 override=200 export=200 file=['/export/CS-7D6BD7B4793A.csv']`
- Result: PASS
- Evidence: `{"approve": 403, "override": 200, "override_body": {"reason_code": "material_close_deadline", "authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad"}, "reason_codes_served": ["material_close_deadline","known_data_defect_upstream","regulatory_instruction","documented_control_exception"], "authoriser_fields": ["authoriser_a","authoriser_b"], "export": 200, "authorised_on": "synthetic_attestation"}`

### Scenario: S14 - the produced export file is retrievable and carries the FBDI header
- Status: EXECUTED · Actual: `status=200 lines=3`
- Result: PASS
- Evidence: `STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,...`

### Scenario: S15 - AC-F40-18: the export names its authorisation basis
- Status: EXECUTED · Actual: `synthetic_attestation`, never a stored register pass state
- Result: PASS · Evidence: `data-authorised-on='synthetic_attestation'`

### Scenario: S16 - registers 3 and 4 are named as unmet on the auditor's screen
- Status: EXECUTED · Actual: `F1-11=True F1-08=True`
- Result: PASS

### Scenario: S17 - no green colour token on the served surface
- Status: EXECUTED · Actual: `matches=[]`
- Result: PASS

### Scenario: S18 - the non-dismissable pilot strip renders on every screen
- Status: EXECUTED · Actual: `{"/queue": true, "/approvals": true, "/evidence/run/RUN-2026-06-0412": true, "/ask": true}`
- Result: PASS

### Scenario: S19 - an object this build does not have is refused, not substituted
- Status: EXECUTED · Actual: 404 on all four unknown object addresses
- Result: PASS

### Scenario: S20 - the served lockup puts `.ctx` AFTER the row, not inside it
- Status: EXECUTED
- Input: the served markup of the lockup block on `/queue`
- Expected: `.lockup-row` present and `.ctx` a following sibling
- Actual: `row=True ctx_after_row=True`
- Result: PASS
- Evidence: served bytes show `.lockup > [.lockup-row, .ctx]`

### Scenario: S21 - the orphaned rule the defect shipped as is gone from the served CSS
- Status: EXECUTED
- Input: the inlined stylesheet in the served `/queue` bytes
- Expected: `.lockup .ctx` present, `.brand` absent
- Actual: `lockup_ctx=True brand=False`
- Result: PASS
- Evidence: asserted on the served bytes, not on the module source

### Scenario: S22 - the broker's `unregistered_actors`
- Status: **MIS-TARGETED — NOT A PASS.** My scenario asked `GET /ges/inventory`
  on **8021**, which is the api process; the broker's route lives on the GES
  surface, and under `pilot_transport` there is no socket on 8022 at all
- Input: `GET /ges/inventory` on 8021
- Actual: **404** (`{"detail":"Not Found"}`), `unregistered_actors=None`
- Result: **NOT A RESULT.** Recorded as such rather than as the pass its
  permissive assertion would have allowed
- Evidence: the field WAS measured, in-process, and the measurement is a
  finding: **`unregistered_actors == []` while four agents that acted are
  absent.** See `functional-2026-08-03.md` Finding 3

### Scenario: S23 - each alias really serves its canonical screen over real HTTP
- Status: EXECUTED · Actual: `{"/exceptions": true, "/review": true}` — bodies
  after `</style>` byte-identical to `/queue`
- Result: PASS
- Evidence: the unit-tree guard is confirmed over a real socket, not only
  in-process

### Scenario: S24 - the post-approval seal renders on the screen you go BACK to
- Status: EXECUTED
- Input: `/approvals`, `/approvals/PROP-2026-06-0031`, `/proposal/PROP-2026-06-0031`
  after the S13 approval
- Expected: the approved artefact renders with its seal
- Actual: `{"/approvals": {"seal": true}, "/approvals/PROP-2026-06-0031": {"seal": true, "card_approved": true}, "/proposal/PROP-2026-06-0031": {"seal": true}}`
- Result: PASS
- Evidence: the live counterpart of mutation M4 — `.seal` and `.card.approved`
  are genuinely rendered, over HTTP, on the screens the new traversal revisits
