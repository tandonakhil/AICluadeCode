# Test evidence - unit / integration and every SME suite, gate 11

**Project:** conclave-finance-studio
**Gate:** 11 - pre-smoke suite run
**Date:** 2026-08-06
**Commit under test:** `dev` @ **`c68ad84`**, working tree clean
**Owner:** `test-agent` (unit/integration); SME suites reported, not authored, here
**Blocking:** yes (Test Policy: all suites blocking, no advisory exceptions)
**Status:** `EXECUTED`

## Result

**3,105 scenarios, 3,105 pass, 0 fail, 0 skip, exit 0** in 249s.

Command, per the README: `.venv/bin/python -m pytest` from `dev/`.

## Per-suite breakdown - every suite marked, never merged

| Suite | Owner | Status | Result | Blocking |
|---|---|---|---|---|
| unit / integration (`backend/tests`) | `test-agent` | **`EXECUTED`** | **2,412 / 2,412** | yes |
| functional | `functional-design-agent` | **`EXECUTED`** | **365 / 365** | yes |
| UX | `ui-ux-designer` | **`EXECUTED`** | **194 / 194** | yes |
| red-team | `responsible-ai-architect` | **`EXECUTED`** | **61 / 61** | yes |
| architecture | `solution-architect` | **`EXECUTED`** | **28 / 28** | yes |
| industry | `industry-expert` | **`EXECUTED`** | **23 / 23** | yes |
| security | `security-architect` | **`EXECUTED`** | **22 / 22** | yes |
| **whole tree** | - | **`EXECUTED`** | **3,105 / 3,105** | yes |

No suite is `STATIC ONLY` and none is empty; every count above is non-zero and
was produced by an actual run, not a carried-forward figure.

## Test-count delta - measured by node id, not by counting

Compared against the last recorded run (2026-08-04, `dev` @ `7757e0d`, 3,037
scenarios) by collecting `pytest --collect-only` node ids at **both** commits in
a scratch clone and diffing them.

**3,037 -> 3,105: +71 added, -3 removed, net +68.**

### Added, by file

| File | Added |
|---|---|
| `backend/tests/test_ui_no_orphaned_helper.py` | +26 |
| `backend/tests/test_export_integrity_contract.py` | +17 |
| `backend/tests/test_transport_disclosure.py` | +15 |
| `tests/suites/security/test_transport_disclosure.py` | +8 |
| `backend/tests/test_process_entrypoints.py` | +4 |
| `backend/tests/test_ui_retained_view.py` | +1 |

### Removed - all three named, all three replaced by strictly broader checks

- `backend/tests/test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor-AC-F1-11]`
- `backend/tests/test_export_integrity_contract.py::test_declaring_the_residual_without_naming_its_criterion_is_refused[retention-AC-F1-08]`
- `backend/tests/test_export_integrity_contract.py::test_the_shipped_statement_constructs_and_names_both_criteria`

All three sit in `test_export_integrity_contract.py` and are consequences of pass
25's D2, which added a **third** integrity section (`transport`) to an export that
carried two. None is a coverage reduction:

- `test_declaring_the_residual_without_naming_its_criterion_is_refused[anchor|retention]`
  is replaced by `..._without_naming_its_reference_is_refused[anchor|retention|transport]`
  - broadened from "criterion" to "reference" because the transport weakening
  deliberately has **no** acceptance criterion of its own, and widened from two
  sections to three - plus `test_no_section_is_excused_from_the_residual_clause`
  over all three.
- `test_the_shipped_statement_constructs_and_names_both_criteria` is replaced by
  `test_the_shipped_statement_constructs_and_names_all_three_residuals`.

**No unexplained drop in test count, and no silent replacement:** every one of
the 71 additions is in a file whose subject matter matches passes 24-25 (orphan
check widening, transport disclosure, export integrity contract, process
entrypoints), and the three removals are each superseded by a named broader test
in the same file.

---

# RE-RUN 2 — whole tree at `dev` @ `b447a11` (pass 26)

**Commit under test:** `b447a11` (was `c68ad84`) · **Owner:** `test-agent`
**Blocking:** yes · **Status:** `EXECUTED` · **Command:**
`.venv/bin/python -m pytest` from `dev/`

**Result: 3,158 passed, 0 failed, 0 errors, 0 skipped** in 248.18s.

## Per-suite counts, measured by running each suite alone

| Suite | Owner | Status | Result | Δ vs. `c68ad84` |
|---|---|---|---|---|
| unit / integration (`backend/tests`) | `test-agent` | `EXECUTED` | **2,447 / 2,447** | **+35** |
| functional | `functional-design-agent` | `EXECUTED` | **365 / 365** | 0 |
| UX | `ui-ux-designer` | `EXECUTED` | **194 / 194** | 0 |
| red-team | `responsible-ai-architect` | `EXECUTED` | **61 / 61** | 0 |
| security | `security-architect` | `EXECUTED` | **40 / 40** | **+18** |
| architecture | `solution-architect` | `EXECUTED` | **28 / 28** | 0 |
| industry | `industry-expert` | `EXECUTED` | **23 / 23** | 0 |
| **whole tree** | — | `EXECUTED` | **3,158 / 3,158** | **+53** |

The seven suite totals sum to 3,158 exactly, so no scenario is counted twice and
none is outside a suite.

## Test-count delta — measured by node id, not counted

**3,105 -> 3,158: +55 added, -2 removed, net +53.** Measured by collecting
`pytest --collect-only` node ids at `c68ad84` (in a scratch clone) and at
`b447a11`, sorting both and diffing. The +53 matches `code-agent`'s claim, and
the +35 / +18 suite split reconciles to it (37 backend additions - 2 removals =
+35; 18 security additions).

### The 55 additions, by file

| File | Added |
|---|---|
| `backend/tests/test_provenance_disclosure.py` (new) | 21 |
| `tests/suites/security/test_provenance_disclosure.py` (new) | 18 |
| `backend/tests/test_export_integrity_contract.py` | 13 |
| `backend/tests/test_ui_dossier.py` | 2 |
| `backend/tests/test_ui_chrome.py` | 1 |

### The 2 removals, both named, both renames with strictly broader successors

| Removed | Superseded by |
|---|---|
| `test_export_integrity_contract.py::test_the_contract_covers_all_three_of_the_pilots_structural_weakenings` | `...covers_all_four_of_the_pilots_structural_weakenings` |
| `test_export_integrity_contract.py::test_the_shipped_statement_constructs_and_names_all_three_residuals` | `...constructs_and_names_all_four_residuals` |

Both successors assert over a strictly larger set (four sections rather than
three) in the same file. **No coverage was dropped**, and the count did not fall.

### Changed tests — same node id, changed body

Four, all in shared `_integrity()` helpers, all the same edit: the helper now
also builds the `provenance` section from the real producer. No assertion was
weakened or removed.

- `backend/tests/test_audit_domain_and_export.py::_integrity` (helper)
- `tests/suites/functional/test_f1_evidence_criteria.py::_integrity` (helper)
- `backend/tests/test_ui_chrome.py` — one scenario **inverted, not deleted**: it previously asserted `'data-testid="pilot-strip"' not in markup`
- `backend/tests/test_ui_dossier.py` — one scenario **inverted, not deleted**: it previously asserted `not screen.has("pilot-strip")`

The two inversions are worth naming: both **passed for twenty-five passes while
asserting the defect**, and both are what would have failed had anyone fixed
this by accident. Each carries its old text and the reason in its docstring.
Inverting an assertion is normally a coverage red flag, so it is recorded here
explicitly rather than absorbed into "changed".

## A harness note on reading these counts

An earlier invocation of mine appeared to show the suite producing **no summary
line at all**, which read like a run aborting silently at exit code 0. It was
neither: `pytest.ini` already sets `addopts = -q`, so an explicit `-q` on the
command line makes it `-qq`, and pytest suppresses the summary at verbosity
`< -1`. Recorded because "3,158 passed" is the number this gate turns on, and a
reader reproducing it with `pytest -q` will see the count vanish and should know
why.
