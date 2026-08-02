# Test evidence — post-deploy smoke test

**Project:** conclave-finance-studio
**Gate:** 8 · Test (re-run, pass 13 verification)
**Date:** 2026-07-31
**Commit under test:** `dev` @ **`55878c9`** · parent repo @ **`8697994`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`
**Entry point:** `CONCLAVE_ENV=pilot .venv/bin/python backend/pilot.py`, then
stdlib HTTP to `http://127.0.0.1:8021` — **no `TestClient`, no `curl` shortcuts
around the app**
**Exit code:** 0
**Scenarios: 14 — PASS 14, FAIL 0**

Previous run: **13 scenarios, 12 PASS, 1 FAIL** (the unknown run tier). That
failure is scenario S5 below and it now passes.

## Process-lifecycle note

`backend/pilot.py` ends in a blocking `uvicorn.run(...)`, so it cannot be run to
completion. It was **started, exercised and stopped inside a single command
invocation**, five times across this run (four fix-verification drives plus this
smoke). Each invocation ends with `lsof -nP -iTCP:8021 -sTCP:LISTEN`, force-kills
any survivor by port, and fails the script if the port is still held. Final state
verified: **`8021 free — nothing left running`**. No browser, simulator or server
survives this turn.

The pilot binds **8021**, not 8000. A foreign process on this machine holds
`*:8000`; nothing here was collected from it.

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
- Actual: 200 on all thirteen, none missing
- Result: PASS
- Evidence: `{"/": 200, "/ask": 200, "/exceptions": 200, "/review": 200,
  "/readiness": 200, "/dispositions": 200, "/catalogue": 200, "/monitors": 200,
  "/inventory": 200, "/audit": 200, "/refusals": 200, "/audit/export": 200,
  "/my-probe-history": 200}`

### Scenario: S3 — `AC-F28-07`'s "not run" is a state a reader meets in the running pilot
- Status: EXECUTED
- Input: `GET /exceptions`, counting `data-state="not_run"`
- Expected: exactly one boundary check in the not-run state, distinguishable
  from one that ran and found nothing
- Actual: exactly **1**
- Result: PASS
- Evidence: `data-state="not_run" occurrences = 1`. This is the state a persisted
  warehouse from an earlier full seed silently destroys — see F1-4 in
  `fix-verification-2026-07-31.md`.

### Scenario: S4 — the close-clock staleness renders on the served screen
- Status: EXECUTED
- Input: `GET /exceptions`
- Expected: register 6 is closed, so `AC-F38-11`'s close-relative staleness is on
  the page shell's provenance strip
- Actual: present, `Close day 3`
- Result: PASS
- Evidence: `Close day ` inside the provenance strip

### Scenario: S5 — an unknown run tier is refused with 400, in both directions
- Status: EXECUTED
- Input: `/ask?tier=certified` → `?tier=nonsense_typo` → `?tier=certified` →
  `?tier=exploration` → `?tier=nonsense_typo` → `?tier=exploration`. The tier is
  a process singleton, so order is the point and both directions were driven.
- Expected: 400 both times, and the current tier untouched
- Actual: **400** from certified and **400** from exploration; certified renders
  23,076 bytes on both sides of the typo and exploration 24,864 on both sides.
  The two tiers still render differently, so this is not a route that refuses
  everything.
- Result: **PASS — this is the previous run's one FAIL, now fixed**
- Evidence: `{"detail":"'nonsense_typo' is not a run tier. The declared tiers
  are: certified, exploration"}`

### Scenario: S5b — the second route that accepts the parameter refuses too
- Status: EXECUTED
- Input: `GET /exceptions?tier=nonsense_typo`
- Expected: 400 — a fix applied to one of the two GET routes would leave the leak
  reachable through the other
- Actual: **400**, same body
- Result: PASS
- Evidence: `{"detail":"'nonsense_typo' is not a run tier. The declared tiers are: certified, exploration"}`

### Scenario: S6 — the real export path against the persisted warehouse
- Status: EXECUTED
- Input: `POST /pilot/viewing-as persona=controller` →
  `POST /proposal/PROP-2026-06-0031/approve` → the override control the denial
  rendered, with two authorisers and a reason code →
  `POST /proposal/PROP-2026-06-0031/export`
- Expected: approve 403 (denied on value, override-eligible), override 200,
  export **200** with no `revalidation_could_not_run`
- Actual: `approve=403 override=200 export=200 revalidation_could_not_run=False`
- Result: **PASS — this drive returned 403 at gate 8**
- Evidence: `<title>Exported - Conclave Finance Studio</title>`

### Scenario: S7 — the produced export file is retrievable
- Status: EXECUTED
- Input: `GET /export/CS-E1F420D4F62A.csv`
- Expected: 200 with a header row and at least one line
- Actual: `200, 3 lines`
- Result: PASS
- Evidence: `STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,...`

### Scenario: S8 — the export names its authorisation basis
- Status: EXECUTED
- Input: the export screen from S6
- Expected: `AC-F40-18` — the export must not be authorised on a stored CUEC pass
  state, and where it is authorised on the declared synthetic attestation it must
  say so, as a status kept separate from `no_drift`
- Actual: present
- Result: PASS
- Evidence: `<div class="refused" data-testid="cuec-probe-panel" data-authorised-on="synthetic_attestation">`

### Scenario: S9 — a dossier opens from a file, offline, with zero external references
- Status: EXECUTED
- Input: `/exceptions` → `/review/…` → `/dossier/DOS-2026-06-0412-11`, counting
  every external-reference construct in the served bytes
- Expected: zero `<script>`, `<link>`, `<img>`, `@import`, `url(`, `srcset`, and
  zero absolute URLs — register 8's closure condition, re-verified on the served
  app
- Actual: 22,463 bytes, **all eight counts zero**
- Result: PASS
- Evidence: `{"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0,
  "srcset": 0, "http://": 0, "https://": 0}`

### Scenario: S10 — the two open registers' denials reach the auditor's screen
- Status: EXECUTED
- Input: `GET /audit/export`
- Expected: registers 3 and 4 are open, so `AC-F1-11` and `AC-F1-08` must both be
  named as unmet, adjacent to the claims they qualify
- Actual: both present
- Result: PASS
- Evidence: `"The hash-chain anchor is a labelled digest, not a KMS-signed one.
  An attacker who holds the application could recompute the chain and the
  recomputation would not be detected (AC-F1-11 is unmet)."`

### Scenario: S11 — the auditor export FILE carries the integrity statement
- Status: EXECUTED
- Input: `GET /audit/export/file`
- Expected: 200, `evidence_integrity` in the payload, both criterion IDs inside
  it — because `AC-F1-04` makes this file the artefact an auditor consumes with
  no application login, so the one reader who cannot go and look must be told
- Actual: `status=200 AC-F1-11=True AC-F1-08=True evidence_integrity=True`
- Result: PASS
- Evidence: `{"dossier_count": 6, "dossiers": [{"account_combination": "21400",
  "account_name": "GR/IR Clearing", "amount": "312480.00", ...`

### Scenario: S12 — `POST /ask` returns a considered answer, 200 on a non-refusal
- Status: EXECUTED
- Input: `POST /ask request="is $180K worth worrying about for a company this
  size?"` — one of the two paraphrases register 9 records as NOT refused
- Expected: 200, with the outcome stated
- Actual: `200`, crumb `Ask - not answerable from the certified layer`
- Result: PASS
- Evidence: `Ask - not answerable from the certified layer`

### Scenario: S13 — the non-dismissable pilot strip renders on every screen
- Status: EXECUTED
- Input: `GET /exceptions`, `/review`, `/readiness`
- Expected: register 15's strip on every screen
- Actual: present on all three
- Result: PASS
- Evidence: `{"/exceptions": 8, "/review": 8, "/readiness": 8}` pilot-vocabulary matches

### Scenario: S14 — nothing is left listening after the turn
- Status: EXECUTED
- Input: reap, then `lsof -nP -iTCP:8021 -sTCP:LISTEN`, on every one of the five
  invocations
- Expected: no listener on 8021
- Actual: clean on all five. Unlike the previous run, no invocation needed a
  force-kill by port — the launcher pid was the uvicorn listener each time.
- Result: PASS
- Evidence: `8021 free — nothing left running`, five times

---

## Not executed in this smoke test

- **The `loopback` transport.** `backend/pilot.py` installs `pilot_transport`,
  which puts the broker in-process, so nothing here exercises the two-process
  deployment topology. Register 19 is unchanged by this run. The one executing
  witness remains
  `test_ARCH_04_the_deployment_topology_is_two_processes_talking_over_a_socket`
  in the architecture suite, which did execute and pass.
- **`CONCLAVE_ENV=production` refusal.** Covered by an executing unit scenario
  rather than by a served probe.
