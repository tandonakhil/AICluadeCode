# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test (final re-run)
**Date:** 2026-08-02
**Commit under test:** `dev` @ **`fc197a6`** · parent repo @ **`7ec615a`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`, then
stdlib HTTP to `http://127.0.0.1:8021` — **no `TestClient`, no in-process
shortcut, no `curl` wrapper around the app**
**Exit code:** 0
**Scenarios: 14 — PASS 14, FAIL 0**

Driven against the **pilot as found**: the warehouse and ledger already on disk
in `dev/var/`, not a fresh seed. That distinction is the point — the missing
warehouse migration was only ever visible against a persisted warehouse.

## Process-lifecycle note

`backend/pilot.py` ends in a blocking `uvicorn.run(...)`, so it cannot be run to
completion. It was **started, exercised and stopped inside a single command
invocation**, four times across this run (one diagnostic, one smoke, one
rendered-UI capture, one discarded first attempt). Every invocation ends by
killing the launcher pid, force-killing any survivor found by
`lsof -nP -iTCP:8021 -sTCP:LISTEN -t`, and re-checking the port. Final state on
every invocation: **`8021 free — nothing left running`**. No browser and no
server survives this turn.

The pilot binds **8021**, not 8000. A foreign process on this machine holds
`*:8000`; nothing here was collected from it.

## Note on the first attempt

The first smoke invocation reported 4 failures (S4, S6, S7, S8). All four were
**defects in this agent's driver, not in the product**, and are recorded rather
than quietly dropped:

* S4 searched for `Close day\s*\d+` where the shell renders
  `Close day <b>Day 3</b>`;
* S6 **guessed** the override form's field names (`override_reason_code`,
  `second_authoriser`) and got 403; the served form uses `authoriser_a`,
  `authoriser_b`, `reason_code` and carries the denied `decision_id` on its
  action. S7 and S8 then failed downstream of S6.

The driver was corrected to **parse and submit the override control the denial
itself rendered** — its action, its field names and its served values — rather
than a hand-written guess. That is both the fix and the better test: a guessed
form field tests the guess.

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
- Input: `GET` on `/`, `/ask`, `/exceptions`, `/review`, `/readiness`,
  `/dispositions`, `/catalogue`, `/monitors`, `/inventory`, `/audit`,
  `/refusals`, `/audit/export`, `/my-probe-history`
- Expected: 200 on all thirteen
- Actual: 200 on 13 of 13
- Result: PASS
- Evidence: `{"/": 200, "/ask": 200, "/exceptions": 200, "/review": 200, "/readiness": 200, "/dispositions": 200, "/catalogue": 200, "/monitors": 200, "/inventory": 200, "/audit": 200, "/refusals": 200, "/audit/export": 200, "/my-probe-history": 200}`

### Scenario: S3 — `AC-F28-07`'s "not run" survives on the warehouse as found
- Status: EXECUTED
- Input: `GET /exceptions`, counting `data-state="not_run"`
- Expected: exactly one boundary check in the not-run state, against the
  persisted warehouse rather than a fresh seed
- Actual: exactly **1**
- Result: PASS
- Evidence: `data-state="not_run" occurrences = 1 (against the persisted
  var/warehouse.sqlite3, not a fresh seed)`. This is the state a re-seeded
  warehouse silently destroys.

### Scenario: S4 — the close-clock staleness renders on the served screen
- Status: EXECUTED
- Input: `GET /exceptions`
- Expected: register 6 is closed, so `AC-F38-11`'s close-relative staleness is
  on the page shell's provenance strip, as a close-day count and not a wall date
- Actual: `close_day=Day 3 staleness_days_behind=1`
- Result: PASS
- Evidence: `data-testid="close-clock-staleness" data-close-days-behind="1">Staleness <b>1 close day(s) behind the close clock</b></span>`

### Scenario: S5 — an unknown run tier is refused with 400, in both directions
- Status: EXECUTED
- Input: `?tier=certified` → `?tier=nonsense_typo` → `?tier=certified` →
  `?tier=exploration` → `?tier=nonsense_typo` → `?tier=exploration`. The tier is
  a process singleton, so order is the point and both directions were driven.
- Expected: 400 both times, the current tier untouched, and the two tiers still
  rendering differently (so this is not a route that refuses everything)
- Actual: `codes=[200, 400, 200, 200, 400, 200]`; certified renders 23,076 bytes
  on both sides of the typo and exploration 24,864 on both sides
- Result: PASS
- Evidence: `{"codes": [200, 400, 200, 200, 400, 200], "sizes": {"certified": [23076, 23076], "exploration": [24864, 24864]}}`

### Scenario: S5b — the second route that accepts the parameter refuses too
- Status: EXECUTED
- Input: `GET /exceptions?tier=nonsense_typo`
- Expected: 400 — a fix applied to one of the two GET routes would leave the
  leak reachable through the other
- Actual: **400**
- Result: PASS
- Evidence: `{"detail":"'nonsense_typo' is not a run tier. The declared tiers are: certified, exploration"}`

### Scenario: S6 — the real export path against the pilot as found
- Status: EXECUTED
- Input: `POST /pilot/viewing-as persona=controller` →
  `POST /proposal/PROP-2026-06-0031/approve` → the override control **the denial
  itself rendered**, submitted with its own action (carrying
  `decision_id=019fc0dadc7a-…`), two **distinct** authorisers and a served
  reason code → `POST /proposal/PROP-2026-06-0031/export`
- Expected: approve 403 (denied on value, override-eligible), override 200,
  export **200** with no `revalidation_could_not_run`
- Actual: `viewing_as=200 approve=403 override=200 export=200 revalidation_could_not_run=False`
- Result: PASS
- Evidence: `<title>Exported - Conclave Finance Studio</title>`. The denial
  reason served was `approval_value_above_ceiling` under bundle
  `68f5058…ece3c`.

### Scenario: S7 — the produced export file is retrievable
- Status: EXECUTED
- Input: `GET /export/CS-43E02BF8F3FE.csv`
- Expected: 200 with a header row and at least one data line
- Actual: `200, 3 lines`
- Result: PASS
- Evidence: `STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,REFERENCE21,REFERENCE22,REFERENCE23,…`

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
- Input: `/review/ITEM-21400-CP` → `/dossier/DOS-2026-06-0412-01`, counting
  every external-reference construct in the served bytes
- Expected: zero `<script>`, `<link>`, `<img>`, `@import`, `url(`, `srcset`, and
  zero absolute URLs — register 8's closure condition, on the served app
- Actual: 22,615 bytes, **all eight counts zero**
- Result: PASS
- Evidence: `{"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0, "srcset": 0, "http://": 0, "https://": 0}`

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
- Evidence: `{"dossier_count": 6, "dossiers": [{"account_combination": "21400", "account_name": "GR/IR Clearing", "amount": "312480.00", "approved_by": "not approved in this period", …`

### Scenario: S12 — `POST /ask` returns a considered answer, 200 on a non-refusal
- Status: EXECUTED
- Input: `POST /ask request="is $180K worth worrying about for a company this size?"`
  — one of the two paraphrases register 9 records as NOT refused
- Expected: 200, with the outcome stated
- Actual: `200`
- Result: PASS
- Evidence: crumb `Ask - not answerable from the certified layer`

### Scenario: S13 — the non-dismissable pilot strip renders on every screen
- Status: EXECUTED
- Input: `GET /exceptions`, `/review`, `/readiness`
- Expected: register 15's strip on every screen
- Actual: present on all three
- Result: PASS
- Evidence: `{"/exceptions": 8, "/review": 8, "/readiness": 8}` pilot-vocabulary matches

### Scenario: S14 — nothing is left listening after the turn
- Status: EXECUTED
- Input: reap the launcher pid, then force-kill by port, then
  `lsof -nP -iTCP:8021 -sTCP:LISTEN`, on every invocation
- Expected: no listener on 8021
- Actual: clean on all four invocations; no invocation needed the force-kill
  fallback — the launcher pid was the uvicorn listener each time
- Result: PASS
- Evidence: `8021 free — nothing left running`, four times

---

## Test-count delta

14 → 14 scenarios. **0 added, 0 removed, 2 changed** — S4 and S6 were rewritten
to assert against the served markup and the served form rather than against
hand-written strings, and both now assert **more**: S4 additionally reads
`data-close-days-behind`, and S6 additionally proves the override control is
reachable and submittable **as rendered**, with two distinct authorisers drawn
from the served list.

Previous run: 14 scenarios, 14 PASS.

## Not executed in this smoke test

- **The `loopback` transport.** `backend/pilot.py` installs `pilot_transport`,
  which puts the broker in-process, so nothing here exercises the two-process
  deployment topology. Deferred-substitution register 19 is unchanged by this
  run. The one executing witness remains
  `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
  in the architecture suite, which did execute and pass.
- **`CONCLAVE_ENV=production` refusal.** Covered by an executing unit scenario
  rather than by a served probe.
