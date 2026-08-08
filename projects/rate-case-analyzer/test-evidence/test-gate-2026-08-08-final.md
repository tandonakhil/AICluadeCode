# Test gate — independent re-run and evidence artifact, 2026-08-08 (final)

Executed by `test-agent`. Purpose: make real the evidence the Gate 9 re-audit's
*conditional* pass rested on — the seven newly-closed criteria (`AC-F42-03/04/05`,
`AC-F6-04`, `AC-F6-05`, `AC-F7-04`, `AC-F8-05`) were, until this run, supported only
by a prose report of "899 tests" with no recorded artifact. `verification-agent`
was correct to refuse to score them on a summary alone.

Every number below was derived by this agent from a command it ran in this session.
The orchestrator's figure of 899 was **not** taken as an input to the derivation; it
is compared against the derived total at the end.

**Test policy: all suites blocking (ASM-5), no advisory exceptions.**
All commands ran synchronously within a single invocation. No server, browser, or
watcher was left running past this turn (verified below).

---

## Suite status roll-up (EXECUTED / STATIC ONLY / PARTIAL)

| Suite | Status | Blocking? | Tests | Result |
|---|---|---|---|---|
| unit | **EXECUTED** | blocking | 676 | PASS |
| architecture | **EXECUTED** | blocking | 45 | PASS |
| functional | **EXECUTED** | blocking | 23 | PASS |
| industry | **EXECUTED** | blocking | 26 | PASS |
| security | **EXECUTED** | blocking | 43 | PASS |
| red-team | **EXECUTED** | blocking | 27 | PASS |
| ui | **EXECUTED** | blocking | 48 | PASS |
| rendered-ui | **EXECUTED** (Playwright, real browser, app started and stopped by `run_all.sh`) | blocking | 11 | PASS |
| ux | n/a — shim | n/a | — | `tests/suites/ux/run.sh` is a two-line `exec` of `tests/suites/ui/run.sh` (ASA-8). **Not counted separately**; counting it would double-count `ui`'s 48. |

**Derived total: 899.** No suite was STATIC ONLY. No suite was PARTIAL.

---

## Environment and corpus

### Scenario: corpus-on-disk verify
- Input: `./scripts/seed-data.sh verify`
- Expected: totals matching the corpus of record (25 cases / 179 documents / 644 claims)
- Actual: `public/balanced ok`, `public/probes ok`, `public/risk ok`, `workproduct ok`, `totals: {'cases': 25, 'documents': 179, 'claims': 644}`; exit 0
- Result: PASS
- Evidence: command output, this session

### Scenario: the real stores are loaded, and their contents match disk
- Input: direct `sqlite3` row counts against `data/corpus_public/public.sqlite3` and `data/corpus_workproduct/workproduct.sqlite3` (read directly, not via the app)
- Expected: public + work-product row counts summing to the disk totals
- Actual: public `case=20 document=153 chunk=418 claim=582`; work-product `case=5 document=26 chunk=82 claim=62`. Sums: 25 cases, 179 documents, 644 claims — exactly the disk totals.
- Result: PASS
- Evidence: command output, this session

### Scenario: stores match the CURRENT schema (the `content_hash` staleness risk)
- Input: built a fresh database from `app/stores/schema_sql.CORPUS_SCHEMA` in a temp dir and diffed its full table/column signature against both live stores
- Expected: no missing tables, no extra tables, no column differences — in particular `document.content_hash` present in the live stores
- Actual: both stores — `missing_in_live=[] extra_in_live=[] column_diffs=[]`. `document` columns in both live stores end with `content_hash`, i.e. the stores are **not** stale against the schema change.
- Result: PASS
- Evidence: command output, this session

### Scenario: no process left running past the turn
- Input: `lsof -nP -iTCP:8478 -sTCP:LISTEN`; `ps aux | grep -i "serve_demo|uvicorn|playwright"`
- Expected: nothing this agent started still listening
- Actual: "no listener on 8478". Five long-lived `uvicorn app.main:app` processes exist on ports 8000/8100/8420/8421/8422, all started Sunday 01AM under the system Python 3.9 — **pre-existing, not this project's venv, not started by this turn.** The demo server `run_all.sh` brought up for `rendered-ui` was stopped by the runner ("== stopping the demo server") before the script returned.
- Result: PASS
- Evidence: command output, this session

---

## Full suite run

### Scenario: `tests/run_all.sh` from a clean shell — real exit code
- Input: `env -i HOME=... PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin TERM=dumb bash -lc './tests/run_all.sh'`, run from `dev/` with a scrubbed environment (no inherited `RCA_*` variables, no inherited venv)
- Expected: exit 0, eight suites PASS
- Actual: **`REAL_EXIT_CODE=0`.** Suite results block printed by the runner: `unit PASS`, `architecture PASS`, `functional PASS`, `industry PASS`, `security PASS`, `red-team PASS`, `ui PASS`, `rendered-ui PASS`. `rendered-ui` first reported `NOT EXECUTED: no app listening at http://127.0.0.1:8478`, then the runner's own documented path started a server for the suite's duration (`./scripts/ui-evidence.sh`), the 11 Playwright checks ran against a real browser, and the server was stopped — so the suite is **EXECUTED**, not NOT EXECUTED. Only two `StarletteDeprecationWarning`s (httpx/TestClient), no errors.
- Result: PASS
- Evidence: full transcript, this session

---

## Per-suite counts, independently derived

### Scenario: per-suite count derivation
- Input: `./.venv/bin/python -m pytest tests/suites/<suite> -p no:cacheprovider` for each of unit, architecture, functional, industry, security, red-team, ui; `--collect-only` for rendered-ui (which requires a live app to execute, and was executed within `run_all.sh` above)
- Expected: a count per suite, derived, not repeated from any prior report
- Actual:
  - unit **676 passed** (2.20s)
  - architecture **45 passed** (0.94s)
  - functional **23 passed** (0.09s)
  - industry **26 passed**, 1 warning (0.27s)
  - security **43 passed** (0.43s)
  - red-team **27 passed**, 1 warning (0.43s)
  - ui **48 passed**, 1 warning (0.82s)
  - rendered-ui **11 collected**, 11 executed and passed inside `run_all.sh`
  - Sum: 676 + 45 + 23 + 26 + 43 + 27 + 48 + 11 = **899**
- Result: PASS
- Evidence: command output, this session

### Scenario: agreement with the orchestrator's unrecorded "899"
- Input: comparison of the derived 899 against the orchestrator's prose figure
- Expected: state plainly whether they agree; a mismatch is a finding, not something to reconcile away
- Actual: **they agree — 899 = 899.** The figure is now independently derived and recorded rather than asserted. This is the only respect in which the orchestrator's report is confirmed; the derivation did not use it.
- Result: PASS
- Evidence: counts above

---

## Test-count delta vs. the previously recorded 886-test run

### Scenario: delta against `test-evidence/test-gate-2026-08-08.md` (886 tests)
- Input: per-file collected counts (`pytest --collect-only`, aggregated by file) compared file-by-file against the previous run's recorded per-file figures
- Expected: added / removed / changed named explicitly
- Actual: **+13 added, 0 removed, 0 changed. 886 → 899.**
  - **Added (13):** `tests/suites/unit/test_incremental_ingest.py` — one entirely new file, 13 tests, closing `AC-F42-03/04/05`, `AC-F6-04`, `AC-F6-05`, `AC-F7-04`, `AC-F8-05`.
  - **Unchanged (all 15 pre-existing unit files, count-for-count):** test_binary_extraction 18, test_boundaries 44, test_comparability 33, test_config 47, test_corpus_loader 48, test_coverage 31, test_enums 45, test_grounding 76, test_harness 12, test_ingest 121, test_model 43, test_pipeline 45, test_schema_gaps 26, test_stores 40, test_utility_name 34. Unit 663 → 676.
  - **Unchanged (other suites):** architecture 45, functional 23, industry 26, security 43, red-team 27, ui 48 (test_reachability 27 + test_rendering_invariants 21), rendered-ui 11 — all identical to the previous run.
  - **No unexplained drop anywhere.** The entire delta is the one new file, and it is exactly the file the loop-back was for.
- Result: PASS
- Evidence: per-file `--collect-only` aggregation, this session

---

## Spot-check of the newly-closed behaviour (independent, not by running their tests)

The seven criteria are what the Gate 9 conditional rests on, so beyond running
`test_incremental_ingest.py` (13/13 passed in 0.18s) this agent drove `run_ingest`
directly with its own scenarios and its own assertions, including a
structure-changed search page written by this agent rather than the suite's own
constant. Script: `/private/tmp/.../scratchpad/spotcheck_f42.py` (scratch, this session).
Result: **8 of 8 spot-checks PASS, exit 0.**

### Scenario: A1/A2 — second ingest over unchanged fixtures (AC-F42-03)
- Input: `build_world` with three PA PUC documents; `run_ingest` twice over identical fixtures
- Expected: `documents_seen > 0` **and** `documents_ingested == 0` — both, since `documents_ingested == 0` alone is also true of a run that never reached the docket
- Actual: first run `seen=3, ingested=3`; second run `seen=3, ingested=0, skipped_unchanged=3, status=SUCCEEDED`
- Result: PASS
- Evidence: `PASS A1 ... first(seen=3, ingested=3) second(seen=3, ingested=0, skipped_unchanged=3, status=SUCCEEDED)`

### Scenario: A3 — the no-op is readable in the operator-facing report
- Input: `report.as_text(second_run)`
- Expected: both numbers stated in prose an operator can act on
- Actual: `    documents seen          3` and `(every document was re-seen and none had changed — this run ingested nothing because there was nothing new, not because it found nothing)`
- Result: PASS
- Evidence: report text captured, this session

### Scenario: A4 — negative control, a run that saw nothing at all
- Input: same adapter with an empty index, so the search runs and returns zero entries
- Expected: distinguishable from the unchanged run — `documents_seen == 0` and a `search_notice` recorded affirmatively
- Actual: `seen=0 ingested=0 search_notices=1 adapter_errors=0`. Both runs show `ingested=0`; only `documents_seen` and the notice tell them apart, which is the whole point of the criterion.
- Result: PASS
- Evidence: spot-check output, this session

### Scenario: B1/B2 — a page whose structure changed lands in `adapter_errors`, never `search_notices` (AC-F6-05)
- Input: a PA PUC search page written by this agent (a `<section class="results-cards">` card layout — deliberately *not* the suite's own `STRUCTURE_CHANGED_PAGE`), served to `PaPucAdapter` via `search_pages`
- Expected: `AdapterStructureChanged` raised, captured into `adapter_errors`; `search_notices` empty
- Actual: `adapter_errors=["PA_PUC/R-2024-3042569: AdapterStructureChanged: PA PUC: search page structure changed at https://www.puc.pa.gov/search/document-search/?docket=R-2024-3042569 — expected the results table (id='search-results') and it was not present. Refusing to report this as a zero-result search: an empty list here would be indistinguishable from a docket with no filings, which is how a broken adapter goes unnoticed."]`; `search_notices=[]`
- Result: PASS
- Evidence: spot-check output, this session

### Scenario: B3/B4 — a broken adapter fails the run and is surfaced
- Input: the same structure-changed run's `status` and `report.as_text`
- Expected: status `FAILED` (not `SUCCEEDED`/`PARTIAL`), and the error visible in the report
- Actual: `status=FAILED`; report contains `Adapter errors (1)` with the full message, alongside `Searches returning zero results (0) — stated, so a quiet docket is never mistaken for a broken adapter`
- Result: PASS
- Evidence: spot-check output, this session

---

## Findings (non-blocking, reported not fixed)

### Scenario: seeded documents carry an empty `content_hash`
- Input: `select count(*) from document where content_hash != ''` against both live stores
- Expected: informational — the seed path (`corpus_loader`) is not the ingest path (`run_ingest`), so hashes may legitimately be absent
- Actual: **0 of 153** public and **0 of 26** work-product documents have a non-empty `content_hash`. `app/ingest/writer.py:109` defaults it to `""` when no `content_hashes` map is supplied, which is the seed path. Consequence, traced in `app/jobs/pipeline.py:212` (`changed = [row for row in fetched if row[4] is None or row[4].content_hash != row[3]]`): the first real incremental ingest over seeded documents will see `"" != digest` and report **every** seeded document as changed, re-ingesting it once before hashes populate.
- Result: FINDING, not a failure. The direction is the safe one — it **over**-reports change rather than silently skipping, so it cannot cause the stale-corpus failure mode F42 exists to prevent. It does mean the first post-seed run's `documents_ingested` figure is not a true change count. Recommend `code-agent` either populate `content_hash` at seed time or state this in the run report; not blocking.
- Evidence: command output and the two source lines cited above

### Scenario: AC-ID traceability gap (carried forward from the 2026-08-08 gate-8 evidence)
- Input: previously recorded finding — ~65% of the 342/344 AC-IDs are not literally cited in `tests/` or `app/`
- Expected: state whether the new work changed it
- Actual: unchanged in character. `test_incremental_ingest.py` is a counter-example in the right direction — it cites all seven closed AC-IDs in its module docstring and in per-test docstrings, which is exactly the pattern the earlier finding recommended.
- Result: FINDING (open, non-blocking), with the new file noted as the pattern to follow
- Evidence: `tests/suites/unit/test_incremental_ingest.py` docstrings

---

## Executed vs. merely read — stated explicitly

**Executed in this session** (a command ran and its exit code was observed):
`./scripts/seed-data.sh verify`; direct SQLite row-count and schema-signature
queries against both live stores plus a freshly-built schema; `./tests/run_all.sh`
from a scrubbed `env -i` shell (exit 0, all eight suites, including the Playwright
`rendered-ui` suite against a real browser and a real server); eight per-suite
`pytest` invocations; `pytest --collect-only` per suite and per file;
`test_incremental_ingest.py` on its own (13 passed); and this agent's own
`spotcheck_f42.py` driving `run_ingest` directly (8/8 passed).

**Read, not executed** (used to interpret results, never as evidence of behaviour):
`tests/run_all.sh`, `pyproject.toml`, `tests/suites/ux/run.sh`,
`app/jobs/pipeline.py`, `app/jobs/report.py`, `app/model/ops.py`,
`app/ingest/writer.py`, `app/stores/schema_sql.py`, the body of
`test_incremental_ingest.py`, and `PROJECT_CONTEXT.md`.

**Not run at all:** nothing. No suite is STATIC ONLY. The previous run's
screenshots in `test-evidence/` were **not** re-inspected in this pass — the
`rendered-ui` suite that produces them was re-executed and passed, but this
artifact makes no fresh claim about individual screenshot contents; the 2026-08-08
gate-8 evidence file remains the record for that.

---

## Binding decisions checked against (completeness check)

- **ASM-5 · all suites blocking, no advisory exceptions** — honoured. Every suite is
  marked blocking above; none marked advisory; `rendered-ui` reported EXECUTED only
  because it genuinely ran, and the runner's own `NOT EXECUTED` → exit-1 behaviour
  was left intact.
- **Test Policy line in Active Team ("all suites blocking (ASM-5)")** — consistent
  with the roll-up table.
- **ASM-2 · correctness proven against captured fixtures + synthetic corpus** —
  honoured; every check ran offline, no network, no API key. The F42 spot-check used
  `FixtureTransport` exactly as the design intends.
- **ASM-28 / ASM-30 · the corpus of record must actually be loaded** — verified
  independently this run, on disk *and* in both stores, and additionally verified
  that the stores match the post-`content_hash` schema.
- **ASM-31 · demo safe-minimum guard** — not re-exercised this pass (it was verified
  at gate 8 and nothing in the delta touches it); the `rendered-ui` suite ran against
  the guarded server path, which exercises it implicitly.
- **Gate 9 ruling · `NOT VERIFIED` never folds into a pass, no override used** —
  honoured. This artifact does not assert those seven criteria are verified; it records
  executed evidence that the behaviour behind them exists and behaves as specified,
  for `verification-agent` to score.
- **`test-agent` v1.4.0 process-lifecycle constraint** — honoured; nothing left running.

---

## Verdict

**Exit code 0. Eight blocking suites, all EXECUTED, all PASS. 899 tests derived
independently, +13 vs. the recorded 886, 0 removed, 0 changed.** The seven
newly-closed criteria now rest on a recorded artifact rather than a prose summary,
including an independent spot-check of both load-bearing behaviours. Two
non-blocking findings recorded (empty seed-time `content_hash`; the open AC-ID
traceability gap). Nothing here blocks the gate.
