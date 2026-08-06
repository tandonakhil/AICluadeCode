# Test evidence - post-deploy smoke, gate 11, against a freshly deployed pilot on 8021

**Project:** conclave-finance-studio
**Gate:** 11 - post-deploy smoke (the handoff `deploy-agent` reported as owed)
**Date:** 2026-08-06
**Commit under test:** `dev` @ **`c68ad84`**, working tree clean
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## Result

**60 scenarios, 58 pass, 2 FAIL.** Two failures, both the same finding, both
build findings rather than harness defects - see G4b and G14.

Driven over stdlib HTTP against a real served process; no `TestClient`, no ASGI
shortcut. **Two** pilots were started and reaped inside the single command
invocation that started them, each in its own process group
(`start_new_session=True`), torn down with `os.killpg` on that group only. No
name-based sweep at any point. The G-series needed `PROP-2026-06-0031`
*unapproved*, and the S-series' S13 approves it, so they ran on separate fresh
instances rather than sharing one.

## Process lifecycle - the human's pilot

| | |
|---|---|
| human's pilot | **pid 30526, port 8030** (`lsof` re-read at the start of every invocation) |
| alive BEFORE | yes |
| alive AFTER | yes |
| 8030 / 8031 probed or signalled | **never** |
| my listeners on 8021 / 8022 after teardown | `''` / `''` |
| shared SQLite state | **isolated.** `CONCLAVE_VAR_DIR` pointed at a *copy* of `dev/var`, so this smoke could not write into the two SQLite files a live browser session on 8030 is reading. Disclosed because it is a deploy-config departure from `deploy-agent`'s run, made to protect the human's session. |

## Two harness corrections this pass, both recorded rather than quietly fixed

1. **G11b read the wrong key.** It asserted `register` where the payload names
   the field `register_entry`. Harness defect; the build was never in question.
   All three sections carry `register_entry` 3, 4 and 19 correctly.
2. **G4b and G14 first passed for the wrong reason, and that is the more
   important one.** Both scan for the data-provenance disclosure. Both went
   green on the substring `fixture` - which occurs only inside the dataset
   *version identifier* `gl_balances vfixture-2026.06.03-a`. An identifier is
   not a statement. The scenarios now strip that token before counting, and
   both then FAIL, which is the true answer. Recorded in full because a green
   that papered over the finding is exactly what this gate exists to catch, and
   it was caught by reading the recorded evidence rather than the verdict.

---

## The gate-11 checks (G-series)

### Scenario: G1 - the twelve routes deploy-agent walked all serve 200
- Status: EXECUTED
- Input: GET each of the ten navigable screens plus the two declared aliases
- Expected: twelve routes, 200 on every one
- Actual: {"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
- Result: PASS
- Evidence: 

```
{"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
```


### Scenario: G1b - the ten navigable screens are the ones the served shell links to
- Status: EXECUTED
- Input: read the nav hrefs off GET /
- Expected: the ten I checked are exactly the ten linked from /
- Actual: derived=['/', '/approvals', '/ask', '/audit', '/catalogue', '/inventory', '/monitors', '/my-probe-history', '/queue', '/refusals']
- Result: PASS
- Evidence: 

```
{"linked": ["/approvals", "/ask", "/audit", "/catalogue", "/inventory", "/monitors", "/my-probe-history", "/queue", "/refusals"], "checked": ["/", "/approvals", "/ask", "/audit", "/catalogue", "/inventory", "/monitors", "/my-probe-history", "/queue", "/refusals"]}
```


### Scenario: G2 - /health returns 200 with the exact payload deploy-agent recorded
- Status: EXECUTED
- Input: GET /health
- Expected: {"status": "ok", "env": "pilot", "tenant": "tenant-demo", "holds_credentials": false, "ges_base_url": "http://127.0.0.1:8022"}
- Actual: status=200 mismatch={}
- Result: PASS
- Evidence: {"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}

### Scenario: G3 - /exceptions and /review are byte-identical to /queue as declared aliases
- Status: EXECUTED
- Input: GET all three and compare the full response bodies
- Expected: identical bytes and identical length on all three
- Actual: identical={'/exceptions': True, '/review': True} sizes={'/queue': 37345, '/exceptions': 37345, '/review': 37345}
- Result: PASS
- Evidence: {"/queue": 37345, "/exceptions": 37345, "/review": 37345}

### Scenario: G4 - the pilot strip (synthetic fixture data) is on all ten navigable screens
- Status: EXECUTED
- Input: GET each of the ten navigable screens
- Expected: pilot-strip present on all ten
- Actual: screens=10 missing=[]
- Result: PASS
- Evidence: 

```
{
 "/": {
  "pilot": true,
  "topology": true
 },
 "/queue": {
  "pilot": true,
  "topology": true
 },
 "/approvals": {
  "pilot": true,
  "topology": true
 },
 "/ask": {
  "pilot": true,
  "topology": true
 },
 "/catalogue": {
  "pilot": true,
  "topology": true
 },
 "/monitors": {
  "pilot": true,
  "topology": true
 },
 "/audit": {
  "pilot": true,
  "topology": true
 },
 "/inventory": {
  "pilot": true,
  "topology": true
 },
 "/refusals": {
  "pilot": true,
  "topology": true
 },
 "/my-probe-history": {
  "pilot": true,
  "topology": true
 },
 "/dossier/DOS-2026-06-0412-01": {
  "pilot": false,
  "topology": true
 }
}
```


### Scenario: G4b - the shell-off exhibit discloses that its figures are synthetic fixture data
- Status: EXECUTED
- Input: GET /dossier/DOS-2026-06-0412-01 and scan its full text for the data-provenance statement
- Expected: the exhibit states, in some wording of its own, that the figures are synthetic and cannot support a posting or an assurance conclusion - which is what chrome.py:1047 claims it carries in place of the pilot strip
- Actual: on_/queue={'synthetic': 2, 'fixture': 2, 'cannot support a posting': 1, 'assurance conclusion': 2} on_exhibit={'synthetic': 0, 'fixture': 0, 'cannot support a posting': 0, 'assurance conclusion': 0}
- Result: FAIL
- Evidence: 

```
{"screen_counts": {"synthetic": 2, "fixture": 2, "cannot support a posting": 1, "assurance conclusion": 2}, "exhibit_counts": {"synthetic": 0, "fixture": 0, "cannot support a posting": 0, "assurance conclusion": 0}, "exhibit_bytes": 33305, "exhibit_carries": ["close-clock-staleness", "provenance", "transport-topology-state"]}
```


### Scenario: G5 - the topology strip (broker inside this process) is on all ten screens and the shell-off dossier
- Status: EXECUTED
- Input: same eleven surfaces, reading transport-topology-state
- Expected: present on all eleven, data-transport=in-process
- Actual: surfaces=11 missing=[]
- Result: PASS
- Evidence: {"missing": [], "transport_attr": ["in-process"]}

### Scenario: G5b - no control on the served screen dismisses the topology strip
- Status: EXECUTED
- Input: scan /queue for a dismiss/close/hide control
- Expected: none
- Actual: matches=0
- Result: PASS
- Evidence: []

### Scenario: G6 - /inventory names the four absent agents and records AC-F5-02 and AC-F5-07 NOT met
- Status: EXECUTED
- Input: GET /inventory
- Expected: the four principals named; both criterion IDs stated unmet
- Actual: absent=['agent.anomaly-detect', 'agent.crossperiod-surveillance', 'agent.fidelity-check', 'agent.omission-detector'] AC-F5-02=True AC-F5-07=True not_met_language=True
- Result: PASS
- Evidence: 

```
{"absent": ["agent.anomaly-detect", "agent.crossperiod-surveillance", "agent.fidelity-check", "agent.omission-detector"], "expected": ["agent.anomaly-detect", "agent.crossperiod-surveillance", "agent.fidelity-check", "agent.omission-detector"], "AC_F5_02_named": true, "AC_F5_07_named": true}
```


### Scenario: G7 - approve as staff accountant is refused 403 not_in_capability_allowlist, and NO override control is rendered
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/approve as persona=staff
- Expected: 403; reason not_in_capability_allowlist; stated not override-eligible; no override control at all, not a disabled one
- Actual: status=403 allowlist=True not_override_eligible=True override_control=False override_forms=[]
- Result: PASS
- Evidence: 

```
{"status": 403, "reason_attrs": ["not_in_capability_allowlist"], "not_override_eligible": true, "override_control_present": false, "override_form_actions": [], "disabled_elements_on_page": 0}
```


### Scenario: G8 - approve as controller is refused 403 approval_value_above_ceiling, and the override IS offered with two authorisers
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/approve as persona=controller
- Expected: 403; reason approval_value_above_ceiling; rule quant.approval_value_ceiling; override control with authoriser_a and authoriser_b and a closed reason list
- Actual: status=403 ceiling=True rule=True override_control=True two_authoriser_fields=True reasons=4
- Result: PASS
- Evidence: 

```
{"status": 403, "override_action": ["/proposal/PROP-2026-06-0031/override?decision_id=019fd8d63cea-70d8904397c4494c8097"], "reason_codes": ["documented_control_exception", "known_data_defect_upstream", "material_close_deadline", "regulatory_instruction"], "authoriser_a_options": ["user.a.reyes", "user.s.haddad"], "authoriser_b_options": ["user.a.reyes", "user.s.haddad"]}
```


### Scenario: G8b - the staff refusal and the controller refusal are different reasons
- Status: EXECUTED
- Input: compare the two 403 bodies
- Expected: different reason codes, and only the controller's is override-eligible
- Actual: staff_allowlist=True controller_ceiling=True staff_override_ctl=False controller_override_ctl=True
- Result: PASS
- Evidence: SoD control is live: the capability denial is not override-eligible; the ceiling denial is

### Scenario: G9 - override with two distinct authorisers is accepted 200
- Status: EXECUTED
- Input: POST the override the denial page rendered, values read off its own radios
- Expected: 200, two DISTINCT authorisers, approval recorded
- Actual: status=200 a=user.a.reyes b=user.s.haddad distinct=True approved_text=True
- Result: PASS
- Evidence: {"reason_code": "material_close_deadline", "authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad"}

### Scenario: G9b - the same person cannot be both authorisers
- Status: EXECUTED
- Input: POST the override again with authoriser_a == authoriser_b
- Expected: refused (not 200)
- Actual: status=403
- Result: PASS
- Evidence: 

```
<!DOCTYPE html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=1440"><title>Override refused - Conclave Finance Studio</title><style>:root{--accent:#1D4ED8;--accent-bg:#ECF1FE;--bg:#F6F6F3;--gold:#8A5A17;--gold-bg:#FBF1DF;--ink:#14161A;--ink-2:#4A4
```


### Scenario: G10 - export returns 200 and produces a BALANCED Journal Import file
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/export, then GET the produced file
- Expected: 200; GL_INTERFACE header; sum(ENTERED_DR) == sum(ENTERED_CR), non-zero
- Actual: export=200 file=['/export/CS-DFCE57230FD8.csv'] status=200 data_lines=2 Dr=86340.0 Cr=86340.0 balanced=True
- Result: PASS
- Evidence: 

```
{"group_ids": ["CS-DFCE57230FD8"], "header": ["STATUS", "LEDGER_ID", "USER_JE_SOURCE_NAME", "USER_JE_CATEGORY_NAME", "ACCOUNTING_DATE", "CURRENCY_CODE", "DATE_CREATED", "ACTUAL_FLAG"], "entered_dr": 86340.0, "entered_cr": 86340.0, "data_lines": 2}
```


### Scenario: G10b - the Journal Import CSV is the ERP artefact and carries no integrity sections
- Status: EXECUTED
- Input: scan the produced CSV
- Expected: no evidence_integrity, no criterion IDs
- Actual: clean=True
- Result: PASS
- Evidence: the three sections live in the EVIDENCE export, not this one

### Scenario: G11 - the evidence export carries all three integrity sections, each naming what it does not meet
- Status: EXECUTED
- Input: GET /audit/export/file
- Expected: {"unmet_criterion": {"anchor": "AC-F1-11", "retention": "AC-F1-08", "transport": null}}
- Actual: status=200 sections=['anchor', 'retention', 'transport'] unmet={'anchor': 'AC-F1-11', 'retention': 'AC-F1-08', 'transport': None}
- Result: PASS
- Evidence: 

```
{
 "bytes": 84106,
 "sections": [
  "anchor",
  "retention",
  "transport"
 ],
 "unmet_criterion": {
  "anchor": "AC-F1-11",
  "retention": "AC-F1-08",
  "transport": null
 },
 "register": {
  "anchor": 3,
  "retention": 4,
  "transport": 19
 },
 "detail": {
  "anchor": {
   "is_stub": true,
   "register_entry": 3,
   "signature_prefix": "STUB-UNSIGNED:",
   "signer": "StubAnchorSigner",
   "statement": "The hash-chain anchor in this build is a LABELLED DIGEST, not a KMS-signed Ed25519 signature. Every anchor it produces is prefixed 'STUB-UNSIGNED:' and every anchor row carries signer_is_stub. What this evidence therefore supports: tamper-DETECTION against accidental modification and against a party who does not recompute the chain. What it does NOT support: tamper-evidence against a party holding application-level write access, who could recompute the whole chain undetected (AC-F1-11 unmet, deferred-substitution register 3).",
   "unmet_criterion": "AC-F1-11"
  },
  "retention": {
   "label": "Retention stamp",
   "register_entry": 4,
   "retention_enforced": false,
   "retention_expiry": "2033-07-03",
   "statement": "This is a retention STAMP, not enforcement. This build applies no retention lock: the archive is a local store whose objects are deletable, so nothing prevents this record being destroyed before the date above. Seven-year immutable retention is NOT met by this build (AC-F1-08, deferred-substitution register 4). What IS true: the evidence store is append-only within the running system and hash-chained, so a modification by a party who does not recompute the chain is detectable.",
   "unmet_criterion": "AC-F1-08"
  },
  "transport": {
   "process_boundary_enforced": false,
   "register_entry": 19,
   "statement": "THE GUARDRAIL BROKER RAN INSIDE THE INTERFACE PROCESS for this build. Every broker fact in this export - each eligibility, decision, refusal and routing answer - was obtained over the in-process transport, so the trust boundary between the interface and the broker was a module boundary and not a process boundary. What this evidence therefore supports: that the broker was asked, what it answered, and that the answer was recorded. What it does NOT support: any conclusion about the two-process deployment, because code running in the interface process could reach the broker's executor directly, which is the property the split exists to deny. This weakening has NO ACCEPTANCE CRITERION OF ITS OWN; it is carried by ARCHITECTURE_KB 3.2 and
```


### Scenario: G11b - the transport section carries the weakening explicitly, register 19
- Status: EXECUTED
- Input: read evidence_integrity.transport
- Expected: register 19 and the explicit no-criterion statement
- Actual: register_entry=19 statement=True
- Result: PASS
- Evidence: 

```
{"process_boundary_enforced": false, "register_entry": 19, "statement": "THE GUARDRAIL BROKER RAN INSIDE THE INTERFACE PROCESS for this build. Every broker fact in this export - each eligibility, decision, refusal and routing answer - was obtained over the in-process transport, so the trust boundary between the interface and the broker was a module boundary and not a process boundary. What this evidence therefore supports: that the broker was asked, what it answered, and that the answer was recorded. What it does NOT support: any conclusion about the two-process deployment, because code running in the interface process could reach the broker's executor directly, which is the property the split exists to deny. This weakening has NO ACCEPTANCE CRITERION OF ITS OWN; it is carried by ARCHITECTURE_KB 3.2 and deferred-substitution register entry 19.", "transport": "in-process", "unmet_criterio
```


### Scenario: G12 - INDEPENDENT: the export's rendered views carry ZERO style blocks against many class attributes
- Status: EXECUTED
- Input: count '<style' and 'class=' occurrences in every rendered_view of the served export
- Expected: 0 style blocks, a large non-zero class count - register 35 / ARCHITECTURE_KB 25.4 as an open item
- Actual: export_bytes=84106 dossiers=6 style_blocks=0 class_attrs=624
- Result: PASS
- Evidence: 

```
{"export_bytes": 84106, "per_dossier_style": {"ITEM-21400-CP": 0, "ITEM-18300-OM": 0, "ITEM-54100-CD": 0, "ITEM-11500-PA": 0, "ITEM-13800-AB": 0, "ITEM-19900-FD": 0}, "per_dossier_class": {"ITEM-21400-CP": 109, "ITEM-18300-OM": 109, "ITEM-54100-CD": 103, "ITEM-11500-PA": 100, "ITEM-13800-AB": 103, "ITEM-19900-FD": 100}, "total_style_blocks": 0, "total_class_attributes": 624}
```


### Scenario: G13 - INDEPENDENT: AC-F41-03 is NOT CHECKABLE in the export artefact - CONFIRMED, but not by the mechanism 25.4 names
- Status: EXECUTED
- Input: compare the live shell-off exhibit with the export's rendered_view for the subject of AC-F41-03 (riskiest element at the largest computed font size)
- Expected: live exhibit: style-inlined, .riskband .big carries the size, riskiest-figure present. export artefact: nothing to check against
- Actual: live_inlined=True live_rule=.riskband .big{font-size:40px live_riskiest_figure=True | artefact_riskiest_figure=0 artefact_riskband=0 artefact_rule=0 artefact_font_size_decls=0
- Result: PASS
- Evidence: 

```
{"live_exhibit": {"bytes": 33305, "style_blocks": 1, "largest_rule": ".riskband .big{font-size:40px", "riskiest_figure_present": true}, "export_artefact": {"riskiest_figure": 0, "riskband_class": 0, "style_rule": 0, "font_size_declarations": 0}, "finding": "25.4 reasons that the artefact 'carries a class name and no size'. It carries NEITHER: the risk band is absent from the export's rendered_view entirely, because that view is derived from the approval screen and pass 21 deliberately did not bring the risk band across. AC-F41-03 is not checkable in the artefact - confirmed - and inlining the stylesheet, the ruled remedy, would NOT make it checkable, because the element it is about is not there to size."}
```


### Scenario: G13b - the artefact carries no font-size declaration of any kind
- Status: EXECUTED
- Input: grep every rendered_view for 'font-size'
- Expected: zero occurrences
- Actual: occurrences=0
- Result: PASS
- Evidence: confirms G13 is an absence of information, not a differently-located value

### Scenario: G14 - the evidence export discloses that its figures are synthetic fixture data
- Status: EXECUTED
- Input: scan the whole 84 KB /audit/export/file payload
- Expected: the data-provenance disclosure register 15 puts on every screen appears somewhere in the artefact
- Actual: counts={'synthetic': 0, 'fixture': 0, 'cannot support a posting': 0, 'assurance conclusion': 0, 'pilot build': 0}
- Result: FAIL
- Evidence: 

```
{"export_bytes": 84106, "counts": {"synthetic": 0, "fixture": 0, "cannot support a posting": 0, "assurance conclusion": 0, "pilot build": 0}, "export_statement": "This export contains every dossier recorded for period 202606: 6 in total. Every reference in this file resolves within this file. 1 manufactured review-quality probe item(s) for this period are excluded and are counted here: they are items this system created to test its own review surface, not findings about this ledger, and they are recorded in the F12 retained disposition record marked as prob"}
```


---

## Regression - the 38 pass-22 smoke scenarios, re-run unchanged

All 38 pass at `c68ad84`. Numbers are unchanged from
`smoke-test-2026-08-04.md`; only the commit moved.

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
- Evidence: 

```
{"/": 200, "/queue": 200, "/exceptions": 200, "/review": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/readiness": 200, "/dispositions": 200, "/audit/export": 200, "/audit/export/file": 200, "/health": 200}
```


### Scenario: S3 - the merged queue serves one screen under all three addresses
- Status: EXECUTED
- Input: GET /queue, /exceptions, /review
- Expected: identical bodies
- Actual: identical
- Result: PASS
- Evidence: {"/queue": 37345, "/exceptions": 37345, "/review": 37345}

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
- Evidence: 

```
{"on_run": {"fidelity-region": true, "boundary-region": true, "coding-region": true, "boundary-check-table": true, "check-not-run": true, "recall-bias-label": true}, "off_queue": {"fidelity-region": true, "boundary-region": true, "coding-region": true}}
```


### Scenario: S6 - the evidential chain finding -> run -> agent -> readiness walks over HTTP
- Status: EXECUTED
- Input: each hop uses the href the PREVIOUS served screen rendered
- Expected: four 200s ending on a readiness page
- Actual: [["/review/ITEM-21400-CP", 200], ["/evidence/run/RUN-2026-06-0412", 200], ["/evidence/agent/agent.crossperiod-surveillance", 200], ["/readiness?agent=agent.crossperiod-surveillance", 200]]
- Result: PASS
- Evidence: 

```
[["/review/ITEM-21400-CP", 200], ["/evidence/run/RUN-2026-06-0412", 200], ["/evidence/agent/agent.crossperiod-surveillance", 200], ["/readiness?agent=agent.crossperiod-surveillance", 200]]
```


### Scenario: S7 - the dossier carries exactly one link, the back-reference, and still fetches nothing
- Status: EXECUTED
- Input: GET the dossier the finding links to; count every external-reference construct
- Expected: 8 external-reference counts zero; exactly one href; it is the back-reference
- Actual: ext={'<script': 0, '<link': 0, '<img': 0, '@import': 0, 'url(': 0, 'srcset': 0, 'http://': 0, 'https://': 0} hrefs=['/review/ITEM-21400-CP']
- Result: PASS
- Evidence: {"external": {"<script": 0, "<link": 0, "<img": 0, "@import": 0, "url(": 0, "srcset": 0, "http://": 0, "https://": 0}, "hrefs": ["/review/ITEM-21400-CP"], "bytes": 33305}

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
- Actual: journal_lines@30587 approve_lines@31958
- Result: PASS
- Evidence: offsets 30587 < 31958

### Scenario: S10 - four of five agents render every condition not_yet_evaluable, never a pass
- Status: EXECUTED
- Input: GET /readiness?agent=<id> for every agent the selector offers
- Expected: 5 agents; 4 wholly not_yet_evaluable; no fabricated precision; data-ready=false everywhere
- Actual: agents=5 all_nye=4 fabricated=[] claims_ready=[]
- Result: PASS
- Evidence: 

```
{
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
}
```


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
- Expected: 4 absent acting agents named, AC-F5-02 stated NOT met, unqualified sentence gone
- Actual: absent=['agent.anomaly-detect', 'agent.crossperiod-surveillance', 'agent.fidelity-check', 'agent.omission-detector'] notice=True unqualified_sentence=False
- Result: PASS
- Evidence: 

```
{"absent": ["agent.anomaly-detect", "agent.crossperiod-surveillance", "agent.fidelity-check", "agent.omission-detector"], "has_notice": true, "unqualified_on_inventory": false}
```


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
- Actual: viewing=200 approve=403 override=200 export=200 file=['/export/CS-636BDBB82D84.csv']
- Result: PASS
- Evidence: 

```
{"approve": 403, "override": 200, "override_body": {"reason_code": "material_close_deadline", "authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad"}, "reason_codes_served": ["material_close_deadline", "known_data_defect_upstream", "regulatory_instruction", "documented_control_exception"], "authoriser_fields": ["authoriser_a", "authoriser_b"], "export": 200, "authorised_on": ["synthetic_attestation"], "file": ["/export/CS-636BDBB82D84.csv"]}
```


### Scenario: S14 - the produced export file is retrievable and carries the FBDI header
- Status: EXECUTED
- Input: GET /export/CS-636BDBB82D84.csv
- Expected: 200, FBDI header, at least one data line
- Actual: status=200 lines=3
- Result: PASS
- Evidence: 

```
STATUS,LEDGER_ID,USER_JE_SOURCE_NAME,USER_JE_CATEGORY_NAME,ACCOUNTING_DATE,CURRENCY_CODE,DATE_CREATED,ACTUAL_FLAG,SEGMENT1,SEGMENT2,SEGMENT3,ENTERED_DR,ENTERED_CR,GROUP_ID,REFERENCE1,REFERENCE21,REFER
```


### Scenario: S15 - AC-F40-18: the export names its authorisation basis
- Status: EXECUTED
- Input: the export screen from S13
- Expected: synthetic_attestation, never a stored register pass state
- Actual: synthetic_attestation
- Result: PASS
- Evidence: data-authorised-on=['synthetic_attestation']

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
- Expected: connection refused on 8022 (in-process transport, by design) AND the UNKNOWN answer rendered
- Actual: ges_8022='connection refused: [Errno 61] Connection refused' answer_node=True statement_rendered=True
- Result: PASS
- Evidence: {"ges_8022": "connection refused: [Errno 61] Connection refused", "answer_present": true, "statement_rendered": true}

### Scenario: S25 - each absent-agent link on /inventory lands on THAT agent's page
- Status: EXECUTED
- Input: GET /inventory, follow every absent-agent-link, read the h1
- Expected: four links, four 200s, each h1 the principal id the row names
- Actual: {"agent.crossperiod-surveillance": {"href": "/evidence/agent/agent.crossperiod-surveillance", "status": 200, "h1": "agent.crossperiod-surveillance"}, "agent.omission-detector": {"href": "/evidence/agent/agent.omission-detector", "status": 200, "h1": "agent.omission-detector"}, "agent.anomaly-detect": {"href": "/evidence/agent/agent.anomaly-detect", "status": 200, "h1": "agent.anomaly-detect"}, "agent.fidelity-check": {"href": "/evidence/agent/agent.fidelity-check", "status": 200, "h1": "agent.fidelity-check"}}
- Result: PASS
- Evidence: 

```
{
 "agent.crossperiod-surveillance": {
  "href": "/evidence/agent/agent.crossperiod-surveillance",
  "status": 200,
  "h1": "agent.crossperiod-surveillance"
 },
 "agent.omission-detector": {
  "href": "/evidence/agent/agent.omission-detector",
  "status": 200,
  "h1": "agent.omission-detector"
 },
 "agent.anomaly-detect": {
  "href": "/evidence/agent/agent.anomaly-detect",
  "status": 200,
  "h1": "agent.anomaly-detect"
 },
 "agent.fidelity-check": {
  "href": "/evidence/agent/agent.fidelity-check",
  "status": 200,
  "h1": "agent.fidelity-check"
 }
}
```


### Scenario: S26 - the population answer is rendered UNKNOWN on /inventory
- Status: EXECUTED
- Input: GET /inventory
- Expected: unregistered-actors-answer present, data-computable=false, UNKNOWN in the text
- Actual: node=True computable=['false'] unknown_in_text=True
- Result: PASS
- Evidence: {"present": true, "data_computable": ["false"]}

### Scenario: S27 - the unqualified AC-F5-02 claim is on NO served screen
- Status: EXECUTED
- Input: crawl from / over real HTTP following rendered links
- Expected: zero offenders AND the four agent pages actually reached
- Actual: crawled=46 offenders=[] agent_pages=['/evidence/agent/agent.anomaly-detect', '/evidence/agent/agent.coding-detect', '/evidence/agent/agent.crossperiod-surveillance', '/evidence/agent/agent.fidelity-check', '/evidence/agent/agent.omission-detector']
- Result: PASS
- Evidence: 

```
{
 "urls_crawled": 46,
 "offenders": [],
 "agent_pages": [
  "/evidence/agent/agent.anomaly-detect",
  "/evidence/agent/agent.coding-detect",
  "/evidence/agent/agent.crossperiod-surveillance",
  "/evidence/agent/agent.fidelity-check",
  "/evidence/agent/agent.omission-detector"
 ]
}
```


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
- Actual: {"/approvals": {"status": 200, "marker": "approvals-recorded", "present": true, "none_recorded": false}, "/approvals/PROP-2026-06-0031": {"status": 200, "marker": "approval-recorded-seal", "present": true, "none_recorded": false}, "/proposal/PROP-2026-06-0031": {"status": 200, "marker": "proposal-approval-card", "present": true, "none_recorded": false}}
- Result: PASS
- Evidence: 

```
{"/approvals": {"status": 200, "marker": "approvals-recorded", "present": true, "none_recorded": false}, "/approvals/PROP-2026-06-0031": {"status": 200, "marker": "approval-recorded-seal", "present": true, "none_recorded": false}, "/proposal/PROP-2026-06-0031": {"status": 200, "marker": "proposal-approval-card", "present": true, "none_recorded": false}}
```


### Scenario: S28 - the auditor export is produced and every dossier carries the DERIVED retained view
- Status: EXECUTED
- Input: GET /audit/export/file
- Expected: 200, at least one dossier, each approver_view carrying all nine evidential testids
- Actual: status=200 dossiers=6 missing={}
- Result: PASS
- Evidence: 

```
{"status": 200, "dossiers": 6, "testids_required": ["retained-view", "approval-consequence", "approval-subject", "authorship-trio", "approval-detection-evidence", "evidence-set", "in-force-panel", "journal-lines", "authorship-closure"], "missing_per_dossier": {}}
```


### Scenario: S29 - every retained view in the served export opens from a file, offline
- Status: EXECUTED
- Input: scan each approver_view for 13 external-reference / active-content constructs
- Expected: zero hits on all of them, on every dossier
- Actual: dossiers=6 offenders={}
- Result: PASS
- Evidence: 

```
{"constructs_checked": ["<link", "<img", "<script", "@import", "url(", "srcset", "http://", "https://", "<form", "<a ", "<a>", "onclick", "onload"], "offenders": {}, "view_bytes": {"ITEM-21400-CP": 6588, "ITEM-18300-OM": 6224, "ITEM-54100-CD": 6040, "ITEM-11500-PA": 5929, "ITEM-13800-AB": 6068, "ITEM-19900-FD": 6017}}
```


### Scenario: S30 - the retained view is byte-identical across two independent renders
- Status: EXECUTED
- Input: GET /audit/export/file twice, compare each dossier's approver_view bytes
- Expected: identical on every dossier
- Actual: dossiers=6 differing=[]
- Result: PASS
- Evidence: 

```
{"differing": [], "sha_sample": {"ITEM-11500-PA": "5ee2a41e69a0a1fe", "ITEM-13800-AB": "6b3f85ac1fa9f806", "ITEM-18300-OM": "4818968b4fcc0e25", "ITEM-19900-FD": "3f0840e111c4d037", "ITEM-21400-CP": "d19708be159bd685", "ITEM-54100-CD": "794bc5c627eb5329"}}
```


### Scenario: S31 - approver_view and rendered_view are the same bytes, not two answers
- Status: EXECUTED
- Input: compare the two fields on every dossier in the served export
- Expected: equal on every dossier
- Actual: differing=[]
- Result: PASS
- Evidence: {"differing": []}

### Scenario: S32 - the artefact contains each evidential element's OWN RENDERED BYTES
- Status: EXECUTED
- Input: extract each element's full markup from the served approval screen; require it verbatim in the export's retained view
- Expected: every one of the eight found verbatim, not the same words re-rendered
- Actual: {"approval-consequence": true, "approval-subject": true, "authorship-trio": true, "approval-detection-evidence": true, "evidence-set": true, "in-force-panel": true, "journal-lines": true, "authorship-closure": true}
- Result: PASS
- Evidence: 

```
{
 "approval-consequence": {
  "on_screen": true,
  "bytes": 375,
  "verbatim_in_artefact": true
 },
 "approval-subject": {
  "on_screen": true,
  "bytes": 642,
  "verbatim_in_artefact": true
 },
 "authorship-trio": {
  "on_screen": true,
  "bytes": 1230,
  "verbatim_in_artefact": true
 },
 "approval-detection-evidence": {
  "on_screen": true,
  "bytes": 1032,
  "verbatim_in_artefact": true
 },
 "evidence-set": {
  "on_screen": true,
  "bytes": 582,
  "verbatim_in_artefact": true
 },
 "in-force-panel": {
  "on_screen": true,
  "bytes": 813,
  "verbatim_in_artefact": true
 },
 "journal-lines": {
  "on_screen": true,
  "bytes": 687,
  "verbatim_in_artefact": true
 },
 "authorship-closure": {
  "on_screen": true,
  "bytes": 521,
  "verbatim_in_artefact": true
 }
}
```


### Scenario: S33 - the rendered reject radios carry the six reason CODES, never a row index
- Status: EXECUTED
- Input: read every rejection-reason radio's value off the served approval screen
- Expected: six distinct non-numeric codes, each equal to its data-reason-code
- Actual: n=6 values=['evidence_insufficient', 'population_not_covered', 'resolution_wrong', 'already_handled', 'data_stale_or_wrong', 'judgement_disagreement'] index_like=[]
- Result: PASS
- Evidence: 

```
{"values": ["evidence_insufficient", "population_not_covered", "resolution_wrong", "already_handled", "data_stale_or_wrong", "judgement_disagreement"], "data_reason_code": ["evidence_insufficient", "population_not_covered", "resolution_wrong", "already_handled", "data_stale_or_wrong", "judgement_disagreement"]}
```


### Scenario: S34 - AC-F41-24 on the served screen: a non-approving terminal action is there too
- Status: EXECUTED
- Input: the approval screen as captured at S8, in the state the approve control is visible
- Expected: both present, different endpoints, the alternative neither approve nor override nor disclosed
- Actual: approve=True other=True approve_action=/proposal/PROP-2026-06-0031/approve other_action=/review/ITEM-54100-CD/reject in_details=False
- Result: PASS
- Evidence: {"approve_action": "/proposal/PROP-2026-06-0031/approve", "other_action": "/review/ITEM-54100-CD/reject", "other_bytes": 2169}

### Scenario: S35 - AC-F41-22 on the served finding screen, at both permission levels
- Status: EXECUTED
- Input: GET /review/ITEM-54100-CD as staff and as controller
- Expected: the three elements present, and nothing that approves, at either level
- Actual: {"staff": {"evidence-set": true, "resolution-row": true, "rejection-reasons": true, "approve-lines": false, "approval-control": false, "approve_forms": []}, "controller": {"evidence-set": true, "resolution-row": true, "rejection-reasons": true, "approve-lines": false, "approval-control": false, "approve_forms": []}}
- Result: PASS
- Evidence: 

```
{
 "staff": {
  "evidence-set": true,
  "resolution-row": true,
  "rejection-reasons": true,
  "approve-lines": false,
  "approval-control": false,
  "approve_forms": []
 },
 "controller": {
  "evidence-set": true,
  "resolution-row": true,
  "rejection-reasons": true,
  "approve-lines": false,
  "approval-control": false,
  "approve_forms": []
 }
}
```


### Scenario: S36 - AC-F5-08 rows state 'not recorded'; AC-F5-07 is stated NOT MET on the same screen
- Status: EXECUTED
- Input: GET /inventory
- Expected: at least four 'not recorded' statements, AC-F5-07 named, no blank/dash placeholder
- Actual: not_recorded=24 AC-F5-07_named=True placeholders=[]
- Result: PASS
- Evidence: {"not_recorded_count": 24, "AC_F5_07_named": true}

---

# RE-RUN 2 — gate 11 post-deploy smoke at `dev` @ `b447a11` (pass 26)

**Commit under test:** `b447a11` (was `c68ad84`)
**Owner:** `test-agent` · **Blocking:** yes · **Status:** `EXECUTED`
**Result: 21 scenarios, 21 pass, 0 FAIL.** The two failures recorded above
(G4b, G14) are **CLOSED**.

Driven over stdlib HTTP against a real served pilot on 8021, started and reaped
by process group inside the single command invocation that started it. No
`TestClient`, no ASGI shortcut. `CONCLAVE_VAR_DIR` again pointed at a **copy**
of `dev/var` so this run could not write into the SQLite files the human's
browser session on 8030 is reading.

**The disclosure is asserted as PROSE, never as the substring `fixture`.** Every
scan strips the dataset-version identifier (`gl_balances vFIXTURE-2026.06.03-a`
and any `vFIXTURE-*` form) before counting, and then counts the four multi-word
phrases in `provenance.REQUIRED_PHRASES`. **G4c is the negative control on my
own check** — the identifier alone satisfies none of the four.

## The scenarios

### Scenario: G2 - /health returns 200 with the payload deploy-agent recorded
- Status: EXECUTED
- Input: GET /health
- Expected: 200, status ok, env pilot, holds_credentials false
- Actual: {"status": "ok", "env": "pilot", "tenant": "tenant-demo", "holds_credentials": false, "ges_base_url": "http://127.0.0.1:8022"}
- Result: PASS
- Evidence: {"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}

### Scenario: G1 - the twelve routes deploy-agent walked all serve 200
- Status: EXECUTED
- Input: GET each of ten screens plus two aliases
- Expected: 200 on every one
- Actual: {"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
- Result: PASS
- Evidence:

```
{"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
```

### Scenario: G3 - /exceptions and /review are byte-identical to /queue
- Status: EXECUTED
- Input: compare served bytes
- Expected: identical to /queue
- Actual: {"/exceptions": [true, 37335], "/review": [true, 37335]}
- Result: PASS
- Evidence: queue=37335 bytes

### Scenario: G4 - the register-15 pilot strip is on all ten navigable screens, asserted as prose after stripping the version identifier
- Status: EXECUTED
- Input: scan each screen for all four REQUIRED_PHRASES
- Expected: every phrase present on every screen
- Actual: {"/": 1, "/queue": 1, "/approvals": 1, "/ask": 1, "/catalogue": 1, "/monitors": 1, "/audit": 1, "/inventory": 1, "/refusals": 1, "/my-probe-history": 1}
- Result: PASS
- Evidence:

```
["synthetic fixture data", "synthetic close fixture", "not from an Oracle-sourced warehouse", "cannot support a posting or an assurance conclusion about a real ledger"]
```

### Scenario: G4b - THE FIX: the shell-off /dossier exhibit discloses that its figures are not a real ledger
- Status: EXECUTED
- Input: GET /dossier/DOS-2026-06-0412-01, strip the version identifier, count each phrase
- Expected: 200 and every required phrase present at least once
- Actual: status=200 bytes=33587 hits={"synthetic fixture data": 1, "synthetic close fixture": 1, "not from an Oracle-sourced warehouse": 1, "cannot support a posting or an assurance conclusion about a real ledger": 1} (bare 'fixture' occurrences before stripping: 4)
- Result: PASS
- Evidence:

```
{"synthetic fixture data": 1, "synthetic close fixture": 1, "not from an Oracle-sourced warehouse": 1, "cannot support a posting or an assurance conclusion about a real ledger": 1}
```

### Scenario: G4c - NEGATIVE CONTROL on this check: the version identifier alone satisfies none of the four phrases
- Status: EXECUTED
- Input: count each phrase inside 'gl_balances vFIXTURE-2026.06.03-a'
- Expected: zero for all four
- Actual: {"synthetic fixture data": 0, "synthetic close fixture": 0, "not from an Oracle-sourced warehouse": 0, "cannot support a posting or an assurance conclusion about a real ledger": 0}
- Result: PASS
- Evidence: this is the check that stops the 2026-08-06 false pass recurring

### Scenario: G5b - the topology strip is still on the shell-off exhibit (pass 25's 5(c), topology half, unchanged)
- Status: EXECUTED
- Input: scan /dossier/DOS-2026-06-0412-01 for the topology disclosure
- Expected: present
- Actual: transport-topology-state=1, 'module boundary'=1
- Result: PASS
- Evidence: 

### Scenario: G4d - the exhibit still drops the navigation with the shell - a statement about the figures is not navigation
- Status: EXECUTED
- Input: count <nav elements on the exhibit vs on /queue
- Expected: 0 on the exhibit
- Actual: exhibit=0 queue=1
- Result: PASS
- Evidence: 

### Scenario: G5 - the topology strip is on all ten navigable screens
- Status: EXECUTED
- Input: scan each screen
- Expected: present on all ten
- Actual: {"/": true, "/queue": true, "/approvals": true, "/ask": true, "/catalogue": true, "/monitors": true, "/audit": true, "/inventory": true, "/refusals": true, "/my-probe-history": true}
- Result: PASS
- Evidence: 

### Scenario: G6 - /inventory names the four absent agents and records AC-F5-02 and AC-F5-07 NOT met
- Status: EXECUTED
- Input: GET /inventory
- Expected: four agent ids present, both criteria named unmet
- Actual: {"agents": {"agent.crossperiod-surveillance": true, "agent.omission-detector": true, "agent.anomaly-detect": true, "agent.fidelity-check": true}, "AC-F5-02": true, "AC-F5-07": true}
- Result: PASS
- Evidence: 

### Scenario: G7 - approve as staff accountant is refused 403 not_in_capability_allowlist, and NO override control is rendered
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/approve as persona=staff
- Expected: 403, allowlist reason, no override form at all
- Actual: status=403 allowlist=True override_form=False
- Result: PASS
- Evidence: 

### Scenario: G8 - approve as controller is refused 403 approval_value_above_ceiling and the override IS offered, two authorisers, closed reason list
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/approve as persona=controller
- Expected: 403, ceiling reason, rule named, override form, >=2 distinct authoriser options each side, closed reason list
- Actual: status=403 ceiling=True rule=True action=['/proposal/PROP-2026-06-0031/override?decision_id=019fd94f6a7b-8debc3259a3a43f3b8ca'] a=['user.a.reyes', 'user.s.haddad'] b=['user.a.reyes', 'user.s.haddad'] reasons=['documented_control_exception', 'known_data_defect_upstream', 'material_close_deadline', 'regulatory_instruction']
- Result: PASS
- Evidence: ["documented_control_exception", "known_data_defect_upstream", "material_close_deadline", "regulatory_instruction"]

### Scenario: G8b - the staff refusal and the controller refusal are different reasons and only the controller's is override-eligible
- Status: EXECUTED
- Input: compare the two 403 bodies
- Expected: different codes; staff not override-eligible
- Actual: staff_allowlist=True controller_ceiling=True staff_override_ctl=False controller_override_ctl=True
- Result: PASS
- Evidence: 

### Scenario: G9b - NEGATIVE CONTROL: the same person twice is refused as second authoriser
- Status: EXECUTED
- Input: POST the override with authoriser_a == authoriser_b == user.a.reyes
- Expected: refused, not 200
- Actual: status=403
- Result: PASS
- Evidence:

```
<!DOCTYPE html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=1440"><title>Override refused - Conclave Finance Studio</title><style>:root{--accent:#1D4ED8;--accent-bg:
```

### Scenario: G9 - override with two DISTINCT authorisers is accepted 200
- Status: EXECUTED
- Input: POST the override read off its own radios: a=user.a.reyes b=user.s.haddad
- Expected: 200, approval recorded
- Actual: status=200 approved_text=True
- Result: PASS
- Evidence: {"authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad", "reason_code": "documented_control_exception"}

### Scenario: G10 - export returns 200 and produces a BALANCED Journal Import file
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/export then GET the produced file
- Expected: 200; file retrievable; sum(Dr) == sum(Cr), non-zero
- Actual: export=200 groups=['CS-7C51B8EC0C27'] data_lines=2 Dr=86340.0 Cr=86340.0 balanced=True
- Result: PASS
- Evidence:

```
{"group": ["CS-7C51B8EC0C27"], "header": ["STATUS", "LEDGER_ID", "USER_JE_SOURCE_NAME", "USER_JE_CATEGORY_NAME", "ACCOUNTING_DATE", "CURRENCY_CODE", "DATE_CREATED", "ACTUAL_FLAG"], "entered_dr": 86340.0, "entered_cr": 86340.0}
```

### Scenario: G10b - the Journal Import CSV is the ERP artefact and carries no integrity sections
- Status: EXECUTED
- Input: scan the produced CSV
- Expected: no evidence_integrity, no AC ids
- Actual: evidence_integrity=0 AC-=0
- Result: PASS
- Evidence: 

### Scenario: G11 - the served evidence export carries ALL FOUR integrity sections, each naming what it does not meet
- Status: EXECUTED
- Input: GET /audit/export/file
- Expected: 200; sections anchor/retention/transport/provenance; AC-F1-11, AC-F1-08, register 19, register 15
- Actual: status=200 bytes=85045 sections={"anchor": {"unmet_criterion": "AC-F1-11", "register_entry": 3}, "provenance": {"unmet_criterion": null, "register_entry": 15}, "retention": {"unmet_criterion": "AC-F1-08", "register_entry": 4}, "transport": {"unmet_criterion": null, "register_entry": 19}}
- Result: PASS
- Evidence:

```
{"anchor": {"unmet_criterion": "AC-F1-11", "register_entry": 3}, "provenance": {"unmet_criterion": null, "register_entry": 15}, "retention": {"unmet_criterion": "AC-F1-08", "register_entry": 4}, "transport": {"unmet_criterion": null, "register_entry": 19}}
```

### Scenario: G14 - THE FIX: the served evidence export discloses that its figures are not a real ledger, with unmet_criterion null and register 15
- Status: EXECUTED
- Input: GET /audit/export/file, strip the version identifier, count each phrase
- Expected: every phrase present; unmet_criterion null; register_entry 15; no invented AC id in the statement
- Actual: hits={"synthetic fixture data": 1, "synthetic close fixture": 1, "not from an Oracle-sourced warehouse": 1, "cannot support a posting or an assurance conclusion about a real ledger": 1} unmet_criterion=None register_entry=15 AC-in-statement=False
- Result: PASS
- Evidence:

```
{"dataset_version": "gl_balances vFIXTURE-2026.06.03-a", "real_ledger_sourced": false, "register_entry": 15, "statement": "THE FIGURES IN THIS ARTEFACT ARE NOT A REAL LEDGER. Pilot build - synthetic fixture data. Figures here come from the twelve-period synthetic close fixture, not from an Oracle-sourced warehouse. They cannot support a posting or an assurance conclusion about a real ledger. What this evidence therefore supports: that the pipeline ran, what it detected, what the broker was asked, what it answered and who approved. What it does NOT support: any statement of fact about a real en
```

### Scenario: G14b - the export states it THROUGH the integrity contract, not as free prose beside it
- Status: EXECUTED
- Input: look for the phrases inside evidence_integrity.provenance.statement rather than anywhere in the file
- Expected: every phrase inside the contract-carried statement
- Actual: {"synthetic fixture data": true, "synthetic close fixture": true, "not from an Oracle-sourced warehouse": true, "cannot support a posting or an assurance conclusion about a real ledger": true}
- Result: PASS
- Evidence: 

### Scenario: G12 - the export's rendered views still carry ZERO style blocks (register 35 observation, re-measured, NOT re-litigated)
- Status: EXECUTED
- Input: count <style occurrences in the export artefact
- Expected: recorded as an observation only
- Actual: style_blocks=0 rendered_view_fields=6
- Result: PASS
- Evidence:

```
solution-architect re-ruled this at gate 10; AC-F41-03 is a SCREEN criterion and ARCH-16 must not assert it against this artefact. Register 35 stays open for LEGIBILITY. Recorded, not asserted.
```

## DISCRIMINATION CHECK — the same harness run against the PRE-FIX build

A passing check proves nothing unless it can fail. The identical harness was run
unchanged against a served pilot at **`c68ad84`** (the pre-fix commit), taking
the phrase list from the post-fix build so only the SERVED CODE differed.

**Result there: 21 scenarios, 17 pass, 4 FAIL** — G4b, G11, G14 and G14b, with
the exhibit at 33,305 bytes and the export at 84,106 bytes and **zero**
occurrences of all four phrases in each. Those are the same byte counts recorded
in the original gate-11 run above, which is the join proving this is the same
artefact and the same defect.

Note the recorded detail on the pre-fix exhibit: **`bare 'fixture' occurrences
before stripping: 2`.** An unstripped substring check would have counted those
two and reported green. That is precisely the false pass this harness now
refuses to make.

### Scenario: G2 - /health returns 200 with the payload deploy-agent recorded
- Status: EXECUTED
- Input: GET /health
- Expected: 200, status ok, env pilot, holds_credentials false
- Actual: {"status": "ok", "env": "pilot", "tenant": "tenant-demo", "holds_credentials": false, "ges_base_url": "http://127.0.0.1:8022"}
- Result: PASS
- Evidence: {"status":"ok","env":"pilot","tenant":"tenant-demo","holds_credentials":false,"ges_base_url":"http://127.0.0.1:8022"}

### Scenario: G1 - the twelve routes deploy-agent walked all serve 200
- Status: EXECUTED
- Input: GET each of ten screens plus two aliases
- Expected: 200 on every one
- Actual: {"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
- Result: PASS
- Evidence:

```
{"/": 200, "/queue": 200, "/approvals": 200, "/ask": 200, "/catalogue": 200, "/monitors": 200, "/audit": 200, "/inventory": 200, "/refusals": 200, "/my-probe-history": 200, "/exceptions": 200, "/review": 200}
```

### Scenario: G3 - /exceptions and /review are byte-identical to /queue
- Status: EXECUTED
- Input: compare served bytes
- Expected: identical to /queue
- Actual: {"/exceptions": [true, 37345], "/review": [true, 37345]}
- Result: PASS
- Evidence: queue=37345 bytes

### Scenario: G4 - the register-15 pilot strip is on all ten navigable screens, asserted as prose after stripping the version identifier
- Status: EXECUTED
- Input: scan each screen for all four REQUIRED_PHRASES
- Expected: every phrase present on every screen
- Actual: {"/": 1, "/queue": 1, "/approvals": 1, "/ask": 1, "/catalogue": 1, "/monitors": 1, "/audit": 1, "/inventory": 1, "/refusals": 1, "/my-probe-history": 1}
- Result: PASS
- Evidence:

```
["synthetic fixture data", "synthetic close fixture", "not from an Oracle-sourced warehouse", "cannot support a posting or an assurance conclusion about a real ledger"]
```

### Scenario: G4b - THE FIX: the shell-off /dossier exhibit discloses that its figures are not a real ledger
- Status: EXECUTED
- Input: GET /dossier/DOS-2026-06-0412-01, strip the version identifier, count each phrase
- Expected: 200 and every required phrase present at least once
- Actual: status=200 bytes=33305 hits={"synthetic fixture data": 0, "synthetic close fixture": 0, "not from an Oracle-sourced warehouse": 0, "cannot support a posting or an assurance conclusion about a real ledger": 0} (bare 'fixture' occurrences before stripping: 2)
- Result: FAIL
- Evidence:

```
{"synthetic fixture data": 0, "synthetic close fixture": 0, "not from an Oracle-sourced warehouse": 0, "cannot support a posting or an assurance conclusion about a real ledger": 0}
```

### Scenario: G4c - NEGATIVE CONTROL on this check: the version identifier alone satisfies none of the four phrases
- Status: EXECUTED
- Input: count each phrase inside 'gl_balances vFIXTURE-2026.06.03-a'
- Expected: zero for all four
- Actual: {"synthetic fixture data": 0, "synthetic close fixture": 0, "not from an Oracle-sourced warehouse": 0, "cannot support a posting or an assurance conclusion about a real ledger": 0}
- Result: PASS
- Evidence: this is the check that stops the 2026-08-06 false pass recurring

### Scenario: G5b - the topology strip is still on the shell-off exhibit (pass 25's 5(c), topology half, unchanged)
- Status: EXECUTED
- Input: scan /dossier/DOS-2026-06-0412-01 for the topology disclosure
- Expected: present
- Actual: transport-topology-state=1, 'module boundary'=1
- Result: PASS
- Evidence: 

### Scenario: G4d - the exhibit still drops the navigation with the shell - a statement about the figures is not navigation
- Status: EXECUTED
- Input: count <nav elements on the exhibit vs on /queue
- Expected: 0 on the exhibit
- Actual: exhibit=0 queue=1
- Result: PASS
- Evidence: 

### Scenario: G5 - the topology strip is on all ten navigable screens
- Status: EXECUTED
- Input: scan each screen
- Expected: present on all ten
- Actual: {"/": true, "/queue": true, "/approvals": true, "/ask": true, "/catalogue": true, "/monitors": true, "/audit": true, "/inventory": true, "/refusals": true, "/my-probe-history": true}
- Result: PASS
- Evidence: 

### Scenario: G6 - /inventory names the four absent agents and records AC-F5-02 and AC-F5-07 NOT met
- Status: EXECUTED
- Input: GET /inventory
- Expected: four agent ids present, both criteria named unmet
- Actual: {"agents": {"agent.crossperiod-surveillance": true, "agent.omission-detector": true, "agent.anomaly-detect": true, "agent.fidelity-check": true}, "AC-F5-02": true, "AC-F5-07": true}
- Result: PASS
- Evidence: 

### Scenario: G7 - approve as staff accountant is refused 403 not_in_capability_allowlist, and NO override control is rendered
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/approve as persona=staff
- Expected: 403, allowlist reason, no override form at all
- Actual: status=403 allowlist=True override_form=False
- Result: PASS
- Evidence: 

### Scenario: G8 - approve as controller is refused 403 approval_value_above_ceiling and the override IS offered, two authorisers, closed reason list
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/approve as persona=controller
- Expected: 403, ceiling reason, rule named, override form, >=2 distinct authoriser options each side, closed reason list
- Actual: status=403 ceiling=True rule=True action=['/proposal/PROP-2026-06-0031/override?decision_id=019fd94ffc32-25297c1f59ed48b8a281'] a=['user.a.reyes', 'user.s.haddad'] b=['user.a.reyes', 'user.s.haddad'] reasons=['documented_control_exception', 'known_data_defect_upstream', 'material_close_deadline', 'regulatory_instruction']
- Result: PASS
- Evidence: ["documented_control_exception", "known_data_defect_upstream", "material_close_deadline", "regulatory_instruction"]

### Scenario: G8b - the staff refusal and the controller refusal are different reasons and only the controller's is override-eligible
- Status: EXECUTED
- Input: compare the two 403 bodies
- Expected: different codes; staff not override-eligible
- Actual: staff_allowlist=True controller_ceiling=True staff_override_ctl=False controller_override_ctl=True
- Result: PASS
- Evidence: 

### Scenario: G9b - NEGATIVE CONTROL: the same person twice is refused as second authoriser
- Status: EXECUTED
- Input: POST the override with authoriser_a == authoriser_b == user.a.reyes
- Expected: refused, not 200
- Actual: status=403
- Result: PASS
- Evidence:

```
<!DOCTYPE html><html lang="en" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=1440"><title>Override refused - Conclave Finance Studio</title><style>:root{--accent:#1D4ED8;--accent-bg:
```

### Scenario: G9 - override with two DISTINCT authorisers is accepted 200
- Status: EXECUTED
- Input: POST the override read off its own radios: a=user.a.reyes b=user.s.haddad
- Expected: 200, approval recorded
- Actual: status=200 approved_text=True
- Result: PASS
- Evidence: {"authoriser_a": "user.a.reyes", "authoriser_b": "user.s.haddad", "reason_code": "documented_control_exception"}

### Scenario: G10 - export returns 200 and produces a BALANCED Journal Import file
- Status: EXECUTED
- Input: POST /proposal/PROP-2026-06-0031/export then GET the produced file
- Expected: 200; file retrievable; sum(Dr) == sum(Cr), non-zero
- Actual: export=200 groups=['CS-280A780F50E2'] data_lines=2 Dr=86340.0 Cr=86340.0 balanced=True
- Result: PASS
- Evidence:

```
{"group": ["CS-280A780F50E2"], "header": ["STATUS", "LEDGER_ID", "USER_JE_SOURCE_NAME", "USER_JE_CATEGORY_NAME", "ACCOUNTING_DATE", "CURRENCY_CODE", "DATE_CREATED", "ACTUAL_FLAG"], "entered_dr": 86340.0, "entered_cr": 86340.0}
```

### Scenario: G10b - the Journal Import CSV is the ERP artefact and carries no integrity sections
- Status: EXECUTED
- Input: scan the produced CSV
- Expected: no evidence_integrity, no AC ids
- Actual: evidence_integrity=0 AC-=0
- Result: PASS
- Evidence: 

### Scenario: G11 - the served evidence export carries ALL FOUR integrity sections, each naming what it does not meet
- Status: EXECUTED
- Input: GET /audit/export/file
- Expected: 200; sections anchor/retention/transport/provenance; AC-F1-11, AC-F1-08, register 19, register 15
- Actual: status=200 bytes=84106 sections={"anchor": {"unmet_criterion": "AC-F1-11", "register_entry": 3}, "retention": {"unmet_criterion": "AC-F1-08", "register_entry": 4}, "transport": {"unmet_criterion": null, "register_entry": 19}}
- Result: FAIL
- Evidence:

```
{"anchor": {"unmet_criterion": "AC-F1-11", "register_entry": 3}, "retention": {"unmet_criterion": "AC-F1-08", "register_entry": 4}, "transport": {"unmet_criterion": null, "register_entry": 19}}
```

### Scenario: G14 - THE FIX: the served evidence export discloses that its figures are not a real ledger, with unmet_criterion null and register 15
- Status: EXECUTED
- Input: GET /audit/export/file, strip the version identifier, count each phrase
- Expected: every phrase present; unmet_criterion null; register_entry 15; no invented AC id in the statement
- Actual: hits={"synthetic fixture data": 0, "synthetic close fixture": 0, "not from an Oracle-sourced warehouse": 0, "cannot support a posting or an assurance conclusion about a real ledger": 0} unmet_criterion=None register_entry=None AC-in-statement=False
- Result: FAIL
- Evidence: {}

### Scenario: G14b - the export states it THROUGH the integrity contract, not as free prose beside it
- Status: EXECUTED
- Input: look for the phrases inside evidence_integrity.provenance.statement rather than anywhere in the file
- Expected: every phrase inside the contract-carried statement
- Actual: {"synthetic fixture data": false, "synthetic close fixture": false, "not from an Oracle-sourced warehouse": false, "cannot support a posting or an assurance conclusion about a real ledger": false}
- Result: FAIL
- Evidence: 

### Scenario: G12 - the export's rendered views still carry ZERO style blocks (register 35 observation, re-measured, NOT re-litigated)
- Status: EXECUTED
- Input: count <style occurrences in the export artefact
- Expected: recorded as an observation only
- Actual: style_blocks=0 rendered_view_fields=6
- Result: PASS
- Evidence:

```
solution-architect re-ruled this at gate 10; AC-F41-03 is a SCREEN criterion and ARCH-16 must not assert it against this artefact. Register 35 stays open for LEGIBILITY. Recorded, not asserted.
```
