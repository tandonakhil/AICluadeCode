# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 2)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`75f5e27`** · parent repo @ **`21af9da`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`, then
stdlib HTTP to `http://127.0.0.1:8021` — **no `TestClient`, no in-process
shortcut**
**Exit code:** 0
**Scenarios: 16 — PASS 16, FAIL 0** (S15 passed only after this agent killed a survivor it found; see S15)

Driven against the **pilot as found**: the warehouse and decision ledger
already on disk in `dev/var/`, not a fresh seed. That distinction is the point —
the missing warehouse migration was only ever visible against a persisted
warehouse.

## Process-lifecycle note

`backend/pilot.py` ends in a blocking `uvicorn.run(...)`, so it cannot be run to
completion. It was **started, exercised and stopped inside a single command
invocation**, three times across this pass (one route-discovery run, one smoke,
one rendered-UI capture). Every invocation ends by killing the launcher pid,
force-killing any survivor found by
`lsof -nP -iTCP:8021 -sTCP:LISTEN -t`, and re-checking the port. Final state on
every invocation: **`8021 free — nothing left running`**; the port-based
force-kill fallback was never triggered.

**That was not sufficient, and S15 records why.** A `ps` sweep at the end of the
turn found one **non-listening** `backend/pilot.py` process still resident from
the route-discovery invocation. The port check had passed correctly — the
process held no socket — but a port check is not a process check. It was killed
inside this turn and re-verified: **0 pilot processes, 8021 free**. No browser
and no server survives this turn.

The pilot binds **8021**, not 8000, and reports `ges_base_url
http://127.0.0.1:8022`.

## Note on the driver

The first smoke invocation of this pass reported 5 failures (S2, S5, S6, S7,
S8). All five were **defects in this agent's driver, not in the product**, and
are recorded rather than quietly dropped:

* **S2** used a hand-written list of screen paths and got 404 on seven names
  that do not exist (`/proposals`, `/integrity`, `/surveillance`, `/close`,
  `/evidence`, `/settings`, `/help`). The driver now **enumerates every GET
  route the app's own router declares** that takes no path parameter. A
  hand-written list tests the list.
* **S5** posted to `/pilot/run-tier`, which does not exist; the run tier is a
  query parameter on the GET screens (`_select_tier`). Corrected to drive the
  real parameter.
* **S6** submitted the override form with **guessed** values, giving the same
  person as both authorisers, and was correctly refused 403 ("a different
  person again"). The driver now parses the served radio groups and picks two
  **distinct** authorisers and a reason code from the broker's own closed list.
  S7 and S8 were downstream of S6.

That is both the fix and the better test: a guessed field tests the guess.

---

### Scenario: S1 — `/health` serves
- Status: EXECUTED
- Input: `GET http://127.0.0.1:8021/health`
- Expected: 200
- Actual: 200
- Result: PASS
- Evidence: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`
  — `holds_credentials:false` on the api plane is the architecture claim, served

### Scenario: S2 — every built screen serves 200
- Status: EXECUTED
- Input: `GET` on every parameterless GET route the router declares (15 of them)
- Expected: 200 on all fifteen
- Actual: **15/15 served 200**, no non-200
- Result: PASS
- Evidence: `{"/": 200, "/ask": 200, "/audit": 200, "/audit/export": 200,
  "/audit/export/file": 200, "/catalogue": 200, "/dispositions": 200,
  "/exceptions": 200, "/health": 200, "/inventory": 200, "/monitors": 200,
  "/my-probe-history": 200, "/readiness": 200, "/refusals": 200, "/review": 200}`

### Scenario: S3 — `AC-F28-07`'s "not run" survives on the warehouse as found
- Status: EXECUTED
- Input: `GET /exceptions`, counting `data-state="not_run"`
- Expected: at least one boundary check in the not-run state, against the
  persisted warehouse
- Actual: exactly one, status 200
- Result: PASS
- Evidence: `data-state="not_run" x 1`

### Scenario: S4 — the close-clock staleness renders on the served screen
- Status: EXECUTED
- Input: `GET /exceptions`
- Expected: register 6 is closed, so close-relative staleness is rendered
- Actual: `Close day <b>Day 3`
- Result: PASS
- Evidence: `Close day <b>Day 3`

### Scenario: S5 — an unknown run tier is refused with 400, and both declared tiers stay selectable
- Status: EXECUTED
- Input: `?tier=certified` → `?tier=nonsense_typo` → `?tier=certified` →
  `?tier=nonsense_typo` → `?tier=exploration`, on `/exceptions`
- Expected: 400 on both unknown attempts, the current tier untouched, and both
  declared tiers still selectable afterwards
- Actual: `[200, 400, 200, 400, 200]`
- Result: PASS
- Evidence: the sequence above — the refusal does not leave the screen stuck

### Scenario: S5b — the second route that accepts the parameter refuses too
- Status: EXECUTED
- Input: `GET /ask?tier=nonsense_typo`
- Expected: 400 — a fix applied to one of the two GET routes would leave the
  other open
- Actual: 400
- Result: PASS
- Evidence: `{"detail":"'nonsense_typo' is not a run tier. The declared tiers
  are: certified, exploration"}` — the refusal names what was asked rather than
  reinterpreting it

### Scenario: S6 — the real export path against the pilot as found
- Status: EXECUTED
- Input: `POST /pilot/viewing-as persona=controller` →
  `POST /proposal/PROP-2026-06-0031/approve` → the override control **the
  denial itself rendered**, submitted to its own action (carrying
  `decision_id=019fc1382e90-…`), with two **distinct** authorisers and a reason
  code taken from the broker's served closed list →
  `POST /proposal/PROP-2026-06-0031/export`
- Expected: approve 403 (denied on value, override-eligible), override 200,
  export **200** with no `revalidation_could_not_run`
- Actual: `viewing_as=200 approve=403 override=200 export=200
  revalidation_could_not_run=False`
- Result: PASS
- Evidence: `<title>Exported - Conclave Finance Studio</title>`; override form
  `/proposal/PROP-2026-06-0031/override?decision_id=019fc1382e90-c88f9c5dac4f4a058612`
  with fields `['authoriser_a', 'authoriser_b', 'reason_code']`. The denial
  reason served was `approval_value_above_ceiling` under bundle
  `68f505847f…ece3c` — the same bundle hash the `AC-F36-30` scenarios assert
  their copy compiles to.

### Scenario: S7 — the produced export file is retrievable
- Status: EXECUTED
- Input: `GET /export/<group_id>.csv`, the link the export screen rendered
- Expected: 200 with a header row and at least one data line
- Actual: `200, 3 lines`
- Result: PASS
- Evidence: `STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,…`

### Scenario: S8 — the export names its authorisation basis
- Status: EXECUTED
- Input: the export screen from S6
- Expected: `AC-F40-18` — never authorised on a stored CUEC pass state, and
  where authorised on the declared synthetic attestation it must say so
- Actual: `synthetic_attestation`
- Result: PASS
- Evidence: `data-authorised-on="synthetic_attestation"`

### Scenario: S9 — a dossier opens offline with zero external references
- Status: EXECUTED
- Input: `/review/ITEM-21400-CP` → the dossier it links to, counting every
  external-reference construct in the served bytes
- Expected: zero `<script>`, `<link>`, `<img>`, `@import`, `url(`, `srcset`,
  and zero absolute URLs — register 8's closure condition, on the served app
- Actual: 23,247 bytes, **all eight counts zero**
- Result: PASS
- Evidence: `{"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0,
  "srcset": 0, "http://": 0, "https://": 0}`

### Scenario: S10 — the two open registers' denials reach the auditor's screen
- Status: EXECUTED
- Input: `GET /audit/export`
- Expected: registers 3 and 4 are open, so `AC-F1-11` and `AC-F1-08` must both
  be named as unmet, adjacent to the claims they qualify
- Actual: both present
- Result: PASS
- Evidence: `"The hash-chain anchor is a labelled digest, not a KMS-signed one.
  An attacker who holds the application could recompute the chain and the
  recomputation would not be detected (AC-F1-11 is unmet)."`

### Scenario: S11 — the auditor export FILE carries the integrity statement
- Status: EXECUTED
- Input: `GET /audit/export/file`
- Expected: 200, `evidence_integrity` in the payload, both criterion IDs inside
  it — `AC-F1-04` makes this the artefact an auditor consumes with no
  application login, so the one reader who cannot go and look must be told
- Actual: `status=200 AC-F1-11=True AC-F1-08=True evidence_integrity=True`
- Result: PASS
- Evidence: `{"dossier_count": 6, "dossiers": [{"account_combination": "21400",
  "account_name": "GR/IR Clearing", …`

### Scenario: S12 — `POST /ask` returns a considered answer on a non-refusal
- Status: EXECUTED
- Input: `POST /ask request="is $180K worth worrying about for a company this
  size?"` — one of the two paraphrases register 9 records as NOT refused
- Expected: 200, with the outcome stated
- Actual: 200
- Result: PASS
- Evidence: the `Ask` screen rendered with its crumb; no 5xx and no silent
  refusal

### Scenario: S13 — the non-dismissable pilot strip renders on every screen
- Status: EXECUTED
- Input: `GET /exceptions`, `/review`, `/readiness`
- Expected: register 15's strip on every screen
- Actual: present on all three
- Result: PASS
- Evidence: `{"/exceptions": 9, "/review": 9, "/readiness": 9}` pilot-vocabulary
  matches per screen

### Scenario: S14 — nothing is left listening after the turn
- Status: EXECUTED
- Input: reap the launcher pid, then force-kill by port, then
  `lsof -nP -iTCP:8021 -sTCP:LISTEN -t`, on every invocation
- Expected: no listener on 8021
- Actual: `8021 free — nothing left running` on all three invocations
- Result: PASS
- Evidence: `lsof … -t -> empty (force-kill needed: False)`

### Scenario: S15 — no pilot PROCESS survives the turn either
- Status: EXECUTED
- Input: `ps aux | grep pilot.py` at the end of the turn, after every
  invocation's port check had already passed
- Expected: zero pilot processes
- Actual: **one survivor found** — pid 3478, `backend/pilot.py`, from the
  route-discovery invocation. It held **no listener** (8021 was free, so S14 was
  correct as far as it went), but it was still resident. Killed with `SIGKILL`
  inside this turn; re-checked: `0` pilot processes, `8021 free`.
- Result: PASS after remediation, and recorded as a **defect in this agent's own
  driver**: checking the port is not the same as checking the process. A
  `SIGTERM`-then-`wait` on the launcher pid is not sufficient on its own, and
  the port check alone would have let this pass silently.
- Evidence: `ps aux | grep -c "[p]ilot.py"` → `0`;
  `lsof -nP -iTCP:8021 -sTCP:LISTEN -t` → empty. Nothing survives this turn.

---

## Test-count delta

| | Before (`fc197a6`) | After (`75f5e27`) | Delta |
|---|---|---|---|
| smoke | 14 | **16** | **+2** |

**Added 1, removed 0, changed 3.** The addition is **S5b**'s companion: S5 now
drives five requests instead of four so that *both* declared tiers are shown
still selectable after a refusal, and the screen-enumeration change turned S2
from a 13-name hand-written list into a **15-route** enumeration taken from the
router — strictly more coverage, and no longer dependent on this agent
remembering the surface correctly. S6 asserts the same three status codes as
before plus the parsed form's action and field names. No smoke scenario was
dropped.
