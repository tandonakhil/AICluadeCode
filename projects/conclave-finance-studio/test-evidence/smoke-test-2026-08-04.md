# Test evidence — post-deploy smoke, against the SERVED pilot on 8021

**Project:** conclave-finance-studio
**Gate:** 8 · Test — pass 22 re-run
**Date:** 2026-08-04
**Commit under test:** `dev` @ **`7757e0d`** · parent repo @ **`299369e`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**38 scenarios, 38 pass, 0 fail, exit 0.** (Pass 20: 29. **+9**, all on the
pass-21/22 work.)

Driven over **stdlib HTTP against a real served process** — no `TestClient`, no
ASGI shortcut. The pilot was started on 8021, driven, and reaped **inside a
single command invocation**, in its own process group
(`start_new_session=True`), torn down with `os.killpg` on **that group only**.
No name-based sweep was run at any point.

## Process lifecycle — the human's pilot

| | |
|---|---|
| human's pilot | **pid 78317, port 8030** |
| pid re-read from `lsof` at the start of this pass | **yes** — it is **not** 59422, so the human restarted it since pass 20; carrying the old pid forward would have been wrong |
| alive BEFORE this invocation | **yes** |
| alive AFTER this invocation | **yes** |
| 8030 / 8031 probed | **never** |
| my listeners on 8021 / 8022 after teardown | **`''` / `''`** (empty) |

## The real export path, driven as found

S13 drove `viewing-as → /approvals → approve → override → export` using values
read off the **rendered controls** (persona keys off the switch, the override
form's action URL with its `decision_id`, the closed reason-code list and both
authoriser lists off the radios the denial page rendered). The approve leg
returned **403** and the override leg **200** — the refusal-then-override path,
not a bypass. Produced file `/export/CS-E06AF285AB69.csv`, retrievable, FBDI
header, 3 lines.

The shared broker ledger grew **10,956,800 → 11,124,736 bytes** across this
pass's smoke and rendered-UI invocations, which is the evidence the write path
really ran. The 3,037-scenario test tree leaves it byte-identical.

## One harness correction this pass, and what it was not

The first run of the extended harness reported **S33 and S34 failing**. Both
were **harness sequencing defects, not build defects**: S13 approves
`PROP-2026-06-0031` early in the run, and an approved proposal renders its seal
rather than its terminal actions — so by the time S33/S34 fetched the approval
screen there was no approve control and therefore no reject radios to read.
Both now read the screen **as captured at S8**, i.e. *in the state in which the
approve control is visible*, which is the state `AC-F41-24`'s **When** clause
names. Recorded because "I fixed my test until it passed" is exactly the move
that has to be visible; the build was never in question, and S8 (which found
the approve control present at that point) is what exposed the contradiction.

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
- Actual: 200 on all 17
- Result: PASS
- Evidence: `/`, `/queue`, `/exceptions`, `/review`, `/approvals`, `/ask`, `/catalogue`, `/monitors`, `/audit`, `/inventory`, `/refusals`, `/my-probe-history`, `/readiness`, `/dispositions`, `/audit/export`, `/audit/export/file`, `/health`

### Scenario: S3 - the merged queue serves one screen under all three addresses
- Status: EXECUTED · Expected: identical bodies · Actual: identical · Result: PASS
- Evidence: `/queue`, `/exceptions`, `/review` all 36,513 bytes, byte-equal

### Scenario: S4 - the entry point is the queue and Ask is one link from it
- Status: EXECUTED · Actual: `queue=True ask_linked=True no_nl_input=True` · Result: PASS

### Scenario: S5 - every module that left the queue is visible on the run it is a property of
- Status: EXECUTED · Actual: six modules on the run report, three absent from the queue · Result: PASS

### Scenario: S6 - the evidential chain finding → run → agent → readiness walks over HTTP
- Status: EXECUTED
- Input: each hop uses the href the PREVIOUS served screen rendered
- Actual: four 200s ending on `/readiness?agent=agent.crossperiod-surveillance`
- Result: PASS

### Scenario: S7 - the dossier carries exactly one link and still fetches nothing
- Status: EXECUTED · Actual: 8 external-reference counts all zero; `hrefs=['/review/ITEM-21400-CP']` · Result: PASS

### Scenario: S8 - the one Approve control is on /approvals/<proposal> and nowhere else
- Status: EXECUTED · Actual: `proposal=False approval=True item=False linked=True` · Result: PASS

### Scenario: S9 - AC-F40-11: journal lines precede the approve control
- Status: EXECUTED · Actual: journal-lines earlier in byte offset than approve-lines · Result: PASS

### Scenario: S10 - four of five agents render every condition not_yet_evaluable, never a pass
- Status: EXECUTED · Actual: `agents=5 all_nye=4 fabricated=[] claims_ready=[]` · Result: PASS

### Scenario: S11 - the author-id / registry-id disagreement is stated on the agent's own page
- Status: EXECUTED · Actual: `present=True` · Result: PASS

### Scenario: S12 - AC-F5-02 is DISCLOSED unmet on /inventory, not claimed
- Status: EXECUTED · Actual: four absent acting agents named, notice present, unqualified sentence absent · Result: PASS

### Scenario: S12b - the unqualified sentence is gone from EVERY surface, not one
- Status: EXECUTED · Actual: false on all four agent pages · Result: PASS

### Scenario: S12c - every lineage row on the served screen states scope and INCOMPLETE
- Status: EXECUTED · Actual: `rows=11 complete=['false'] scope=['decision_ledger']` · Result: PASS

### Scenario: S13 - the real export path, driven as found on 8021
- Status: EXECUTED
- Input: viewing-as → /approvals → approve → override (values read off the rendered controls) → export
- Expected: the export terminates in a retrievable file, via refusal-then-override
- Actual: `viewing=200 approve=403 override=200 export=200 file=['/export/CS-E06AF285AB69.csv']`
- Result: PASS
- Evidence: override body `{reason_code: material_close_deadline, authoriser_a: user.a.reyes, authoriser_b: user.s.haddad}`; four reason codes served; `authorised_on=['synthetic_attestation']`

### Scenario: S14 - the produced export file is retrievable and carries the FBDI header
- Status: EXECUTED · Actual: `status=200 lines=3`, header `STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,…` · Result: PASS

### Scenario: S15 - AC-F40-18: the export names its authorisation basis
- Status: EXECUTED · Actual: `synthetic_attestation` · Result: PASS

### Scenario: S16 - registers 3 and 4 are named as unmet on the auditor's screen
- Status: EXECUTED · Actual: `F1-11=True F1-08=True` · Result: PASS

### Scenario: S17 - no green colour token on the served surface
- Status: EXECUTED · Actual: `matches=[]` · Result: PASS

### Scenario: S18 - register 15's non-dismissable pilot strip renders on every screen
- Status: EXECUTED · Actual: present on all four checked screens · Result: PASS

### Scenario: S19 - an object this build does not have is refused, not substituted
- Status: EXECUTED · Actual: 404 on all four unknown object addresses · Result: PASS

### Scenario: S20 - the served lockup puts .ctx AFTER the row, not inside it
- Status: EXECUTED · Actual: `row=True ctx_after_row=True` · Result: PASS

### Scenario: S21 - the orphaned rule the defect shipped as is gone from the served CSS
- Status: EXECUTED · Actual: `lockup_ctx=True brand=False` · Result: PASS

### Scenario: S22 - the pilot exposes no GES HTTP port, and the broker's answer still reaches a reader
- Status: EXECUTED · Actual: 8022 connection refused (in-process transport, by design); UNKNOWN answer rendered · Result: PASS

### Scenario: S23 - each alias really serves its canonical screen over real HTTP
- Status: EXECUTED · Actual: `{"/exceptions": true, "/review": true}` · Result: PASS

### Scenario: S24 - the post-approval seal renders on the screen you go BACK to
- Status: EXECUTED · Actual: all three screens 200, each with its own marker, none "none recorded" · Result: PASS

### Scenario: S25 - each absent-agent link on /inventory lands on THAT agent's page
- Status: EXECUTED · Actual: four links, four 200s, each `h1` the principal id the row names · Result: PASS

### Scenario: S26 - the population answer is rendered UNKNOWN on /inventory
- Status: EXECUTED · Actual: `node=True computable=['false'] unknown_in_text=True` · Result: PASS

### Scenario: S27 - the unqualified AC-F5-02 claim is on NO served screen
- Status: EXECUTED · Actual: `crawled=46 offenders=[]`, all five agent pages among them · Result: PASS

---

## New this pass — the derived retained view, over real HTTP

### Scenario: S28 - the auditor export is PRODUCED and every dossier carries the DERIVED view
- Status: EXECUTED
- Input: GET `/audit/export/file` on the served pilot
- Expected: 200, at least one dossier, each `approver_view` carrying all nine evidential testids
- Actual: **`status=200 dossiers=6 missing={}`**
- Result: PASS
- Evidence: required testids `retained-view`, `approval-consequence`, `approval-subject`, `authorship-trio`, `approval-detection-evidence`, `evidence-set`, `in-force-panel`, `journal-lines`, `authorship-closure` — none missing on any of the six

### Scenario: S29 - every retained view in the served export opens from a file, offline
- Status: EXECUTED
- Input: scan each `approver_view` for 13 external-reference / active-content constructs
- Expected: zero hits, every dossier (`ARCHITECTURE_KB` §9.4, `AC-F1-10`)
- Actual: **zero offenders on all six.** Constructs checked: `<link`, `<img`, `<script`, `@import`, `url(`, `srcset`, `http://`, `https://`, `<form`, `<a `, `<a>`, `onclick`, `onload`
- Result: PASS
- Evidence: view sizes 5,929–6,588 bytes per dossier; `offenders={}`

### Scenario: S30 - the retained view is byte-identical across two independent renders
- Status: EXECUTED
- Input: GET `/audit/export/file` twice, compare each dossier's `approver_view` bytes
- Expected: identical on every dossier (§9.4 consequence 2, ARCH-16)
- Actual: **`dossiers=6 differing=[]`**
- Result: PASS
- Evidence: SHA-256 prefixes — `ITEM-11500-PA 5ee2a41e69a0a1fe`, `ITEM-13800-AB 6b3f85ac1fa9f806`, `ITEM-18300-OM 4818968b4fcc0e25`, `ITEM-19900-FD 3f0840e111c4d037`, `ITEM-21400-CP d19708be159bd685`, `ITEM-54100-CD 794bc5c627eb5329`

### Scenario: S31 - approver_view and rendered_view are the same bytes, not two answers
- Status: EXECUTED · Expected: equal on every dossier · Actual: `differing=[]` · Result: PASS

### Scenario: S32 - the artefact contains each evidential element's OWN RENDERED BYTES
- Status: EXECUTED
- Input: extract each element's **full markup** from the SERVED approval screen by tag balancing, then require that byte string verbatim in the export's retained view
- Expected: all eight found verbatim — the element's own bytes, not the same words re-rendered
- Actual: **all eight `verbatim_in_artefact: true`** (375 / 642 / 1,230 / 1,032 / 582 / 381 / … bytes)
- Result: PASS
- Evidence: this is the scenario that distinguishes *derived* from *assembled*; it compares **screen → artefact**, which is strictly stronger than the in-tree check (see the advisory in `mutation-tests-2026-08-04.md` M3b)

### Scenario: S33 - the rendered reject radios carry the six reason CODES, never a row index
- Status: EXECUTED
- Input: read every `rejection-reason` radio's `value` off the served approval screen, in the state the approve control is visible
- Expected: six distinct non-numeric codes, each equal to its `data-reason-code`
- Actual: **`['evidence_insufficient','population_not_covered','resolution_wrong','already_handled','data_stale_or_wrong','judgement_disagreement']`**, `index_like=[]`, values identical to `data-reason-code`
- Result: PASS
- Evidence: these are exactly `workflow.store.REJECTION_CODES`, the list the `CHECK` constraint is built from

### Scenario: S34 - AC-F41-24 on the served screen: a non-approving terminal action is there too
- Status: EXECUTED
- Expected: both present, different endpoints, the alternative neither approve nor override nor behind a disclosure
- Actual: `approve_action=/proposal/PROP-2026-06-0031/approve`, `other_action=/review/ITEM-54100-CD/reject`, `in_details=False`, other form 2,169 bytes
- Result: PASS

### Scenario: S35 - AC-F41-22 on the served finding screen, at both permission levels
- Status: EXECUTED
- Input: GET `/review/ITEM-54100-CD` as `staff` and as `controller`
- Expected: the three elements present, and nothing that approves, at either level
- Actual: both personas — `evidence-set`, `resolution-row`, `rejection-reasons` all true; `approve-lines` false; `approval-control` false; **zero forms whose action contains `approve`**
- Result: PASS

### Scenario: S36 - AC-F5-08 rows state "not recorded"; AC-F5-07 is stated NOT MET on the same screen
- Status: EXECUTED
- Expected: at least four "not recorded" statements, `AC-F5-07` named, no blank/dash placeholder
- Actual: **`not_recorded=24 AC-F5-07_named=True placeholders=[]`**
- Result: PASS
