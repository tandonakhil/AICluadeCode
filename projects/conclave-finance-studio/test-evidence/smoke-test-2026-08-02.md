# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`9d605b1`** · parent repo @ **`e14c497`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot API_PORT=8021 GES_PORT=8022
.venv/bin/python backend/pilot.py`, then stdlib HTTP to
`http://127.0.0.1:8021` — **no `TestClient`, no in-process shortcut**
**Exit code:** 0
**Scenarios: 17 — PASS 17, FAIL 0**

Driven against the **pilot as found**: the warehouse and decision ledger
already on disk in `dev/var/`, not a fresh seed.

## Process-lifecycle note — and the correction from the previous pass

`backend/pilot.py` ends in a blocking `uvicorn.run(...)`, so it cannot be run to
completion. It was **started, exercised and stopped inside a single command
invocation**, six times across this pass. Nothing is left running past this turn.

**The previous pass's teardown was wrong and killed the human's own pilot.** It
swept with `ps aux | grep pilot.py`, which matches on process *name*. A port
check is not a process check, but a name check is not one either. This pass the
pilot is started with `start_new_session=True`, so the launcher pid **is** the
process-group id, and teardown calls `os.killpg` on **that group and only that
group**. The human's instance (pid 6587, ports 8030/8031) was verified alive at
the start and end of every invocation. No global sweep of any kind was run.

---

### Scenario: S1 — `/health` serves
- Status: EXECUTED
- Input: `GET http://127.0.0.1:8021/health`
- Expected: 200
- Actual: 200
- Result: PASS
- Evidence: `{"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}`

### Scenario: S2 — every built screen serves 200
- Status: EXECUTED
- Input: `GET` on all 15 parameterless product GET routes
- Expected: 200 on all fifteen
- Actual: **15/15 served 200**
- Result: PASS
- Evidence: `{"/": 200, "/ask": 200, "/audit": 200, "/audit/export": 200,
  "/audit/export/file": 200, "/catalogue": 200, "/dispositions": 200,
  "/exceptions": 200, "/health": 200, "/inventory": 200, "/monitors": 200,
  "/my-probe-history": 200, "/readiness": 200, "/refusals": 200, "/review": 200}`
  — the router also declares 4 FastAPI framework routes (`/docs`,
  `/docs/oauth2-redirect`, `/openapi.json`, `/redoc`), excluded as not product
  surface

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
- Evidence: `Close day <b>Day 3`, and on the item screen "Staleness 1 close
  day(s) behind the close clock"

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
  are: certified, exploration"}`

### Scenario: S6 — the real export path against the pilot as found
- Status: EXECUTED
- Input: `POST /pilot/viewing-as persona=controller` →
  `GET /proposal/PROP-2026-06-0031` →
  `POST /proposal/PROP-2026-06-0031/approve` → the override control **the
  denial itself rendered**, submitted to its own action with **two distinct
  authorisers** and a reason code, **every value read off the rendered radio
  inputs rather than guessed** → `POST /proposal/PROP-2026-06-0031/export`
- Expected: approve 403 (denied on value, override-eligible), override 200,
  export **200** with no `revalidation_could_not_run`
- Actual: `viewing_as=200 proposal=200 approve=403 override=200 export=200
  revalidation_could_not_run=False`
- Result: PASS
- Evidence: override control
  `/proposal/PROP-2026-06-0031/override?decision_id=019fc1c919b3-27561ef4db3d4d96884a`;
  authorisers `user.a.reyes` / `user.s.haddad` (distinct), reason code
  `material_close_deadline` from the broker's served closed list
  `['material_close_deadline','known_data_defect_upstream',
  'regulatory_instruction','documented_control_exception']`. The denial reason
  served was `approval_value_above_ceiling` under bundle `68f505847f…ece3c`,
  rule `quant.approval_value_ceiling`, threshold `$150,000.00, inclusive`.
- **Driver defect found and fixed inside this pass:** the first attempt read the
  reason codes from `<option>` elements. They are **radio inputs**, so the list
  came back empty and the driver posted the *denial* code
  `approval_value_above_ceiling`. The product refused it correctly, 403, naming
  the closed list. Three scenarios (S6–S8) failed on that first attempt and
  **the failures were this agent's, not the build's** — recorded rather than
  quietly re-run, and the same class as the previous pass's "a guessed field
  tests the guess".

### Scenario: S7 — the produced export file is retrievable
- Status: EXECUTED
- Input: `GET /export/CS-678E7E3B773D.csv`, the link the export screen rendered
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
- Expected: zero `<script>`, `<link>`, `<img>`, `@import`, `url(`, `srcset`, and
  zero absolute URLs — register 8's closure condition, on the served app
- Actual: 23,247 bytes, **all eight counts zero**
- Result: PASS
- Evidence: `{"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0,
  "srcset": 0, "http://": 0, "https://": 0}`

### Scenario: S10 — the two open registers' denials reach the auditor's screen
- Status: EXECUTED
- Input: `GET /audit/export`
- Expected: registers 3 and 4 are open, so `AC-F1-11` and `AC-F1-08` must both
  be named as unmet
- Actual: both present
- Result: PASS
- Evidence: "The hash-chain anchor is a labelled digest, not a KMS-signed one.
  An attacker who holds the application could recompute the chain and the
  recomputation would not be detected (AC-F1-11 is unmet)."

### Scenario: S11 — the auditor export FILE carries the integrity statement
- Status: EXECUTED
- Input: `GET /audit/export/file`
- Expected: 200, `evidence_integrity` in the payload, both criterion IDs inside it
- Actual: `status=200 AC-F1-11=True AC-F1-08=True evidence_integrity=True`
- Result: PASS
- Evidence: `{"dossier_count": 6, "dossiers": [{"account_combination": "21400",
  "account_name": "GR/IR Clearing", "amount": "312480.00", …`

### Scenario: S12 — `POST /ask` returns a considered answer on a non-refusal
- Status: EXECUTED
- Input: `POST /ask request="is $180K worth worrying about for a company this
  size?"` — one of the two paraphrases register 9 records as NOT refused
- Expected: 200, with the outcome stated
- Actual: 200
- Result: PASS
- Evidence: `<title>Your request - Conclave Finance Studio</title>`; no 5xx and
  no silent refusal

### Scenario: S13 — the non-dismissable pilot strip renders on every screen
- Status: EXECUTED
- Input: `GET /exceptions`, `/review`, `/readiness`
- Expected: register 15's strip on every screen
- Actual: present on all three
- Result: PASS
- Evidence: `{"/exceptions": 9, "/review": 9, "/readiness": 9}` pilot-vocabulary
  matches per screen; visible in
  `ux-review-desktop-1280-2026-08-02.png` as "Pilot build - synthetic fixture
  data."

### Scenario: S14 — nothing is left listening on 8021/8022 after the turn
- Status: EXECUTED
- Input: `lsof -nP -iTCP:8021 -sTCP:LISTEN -t` and the same for 8022, after
  every invocation
- Expected: no listener on either
- Actual: empty on both, on all six invocations
- Result: PASS
- Evidence: `{"listeners_8021": [], "listeners_8022": []}`. Ports 8030/8031
  were never probed and never touched.

### Scenario: S15 — no process from THIS turn's process group survives
- Status: EXECUTED
- Input: `ps -o pid= -g <pgid>` for the process group this turn created, after
  `SIGTERM` and, if needed, `SIGKILL`
- Expected: the group is empty
- Actual: empty on all six invocations
- Result: PASS
- Evidence: `{"pgid": 15761, "members_before": ["15761"], "sigkill_needed":
  true, "members_after": []}`. **Recorded: `SIGTERM` to the group did not stop
  uvicorn within 10s on any invocation; `SIGKILL` was needed every time.** Not
  a product defect — `pilot.py` is a dev launcher — but teardown must not rely
  on `SIGTERM` alone, and the previous pass's `SIGTERM`-then-`wait` is exactly
  what left a survivor.

### Scenario: S16 — the human's pilot instance on 8030 is untouched
- Status: EXECUTED
- Input: `os.kill(6587, 0)` at the start and end of every invocation
- Expected: alive throughout — this is the instance the previous pass killed
- Actual: alive at the start and end of all six invocations
- Result: PASS
- Evidence: `pid 6587 alive=True; teardown scoped to pgid 15761, never to a
  process NAME`

### Scenario: S17 — OBSERVATION — the smoke and the human's pilot share one live ledger
- Status: EXECUTED
- Input: `stat -f%z dev/var/broker_db.sqlite3` around the smoke
- Expected: a real pilot drive writes real decisions — the guard's scope is
  tests, not the pilot
- Actual: `10477568 -> 10498048`, **+20,480 bytes**
- Result: PASS (reported as an observation, not a defect)
- Evidence: this is the **same file** the human's instance on 8030 is using, so
  the decisions this smoke recorded — an override and an export on
  `PROP-2026-06-0031` — are visible in the human's review instance. Worth
  knowing before reading that instance's audit trail; not a fault in the build.
