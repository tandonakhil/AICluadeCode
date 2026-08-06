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
