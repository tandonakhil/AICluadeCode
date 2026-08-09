# Test evidence — order independence, the seeded-shuffle gap closed

**Project:** conclave-finance-studio
**Gate:** 8 · Test — `close-cockpit-home` close
**Date:** 2026-08-08
**Commit under test:** `dev` @ **`7ecba21`**
**Owner:** `test-agent`
**Blocking:** yes
**Status:** `EXECUTED`

## The gap this closes

`code-agent`'s pass-2 commit message recorded that `pytest-randomly` was not
installed in this project's `.venv`, so order independence had been checked
only by forward and reversed **file** order — not by the seeded shuffles
(1 / 7 / 42 / 20260731) this project's history has used throughout the build
to catch cross-scenario state leaks. Three real defects were found this way
in earlier passes and are recorded elsewhere in `PROJECT_CONTEXT.md`: the run
tier leak, the persona leak (`ux` suite run in reverse left
`TestUX14ControllerNightOverMonitors` as the acting persona), and an
interleaved-shuffle order dependence. A gap in the tooling that finds this
class of defect is a real gap, not a formality, so it was closed rather than
worked around.

## What was done

`pytest-randomly>=3.15` added to `dev/requirements-dev.txt` (with a comment
naming why) and installed into **this project's own `.venv`**
(`.venv/bin/pip install pytest-randomly`) — not the platform environment.
Installed version: `pytest-randomly-4.0.1`.

## Method

Six whole-tree runs, no `-k`, no deselection, no `-x` — every run collects
and executes all 3,192 scenarios. `-o addopts=""` is used throughout because
`pytest.ini`'s own `addopts = -q` combined with an explicit `-q` on the
command line becomes `-qq`, which suppresses the pass/fail summary line
below verbosity −1 (recorded at pass 26 and reproduced here — an empty-looking
tail is not an aborted run).

## Result

| Order | Result | Wall |
|---|---|---|
| file (`-p no:randomly`) | **3192 passed** | 267.90s |
| reversed (scratchpad-held `pytest_collection_modifyitems` plugin, `items.reverse()`, loaded by `PYTHONPATH` — outside `dev/`, so the tree under test cannot influence its own shuffle) | **3192 passed** | 274.19s |
| seed 1 (`-p randomly --randomly-seed=1`) | **3192 passed** | 274.84s |
| seed 7 (`--randomly-seed=7`) | **3192 passed** | 275.29s |
| seed 42 (`--randomly-seed=42`) | **3192 passed** | 276.26s |
| seed 20260731 (`--randomly-seed=20260731`) | **3192 passed** | 273.87s |

**Six for six, 3,192 every time, exit 0 every time.** No scenario depends on
another having run first, and no scenario is order-sensitive through
process-scoped state (`app.ui.state`'s `PilotState`, the probe store, the
broker ledger) under any of the four seeds this project's history names, nor
under a full collection reversal.

## Finding

**No order dependence found.** The three previously-found leaks (run tier,
persona, interleaved shuffle) all stayed fixed under seeds this specific
sweep had not previously been able to exercise directly. This is reported
plainly, as the gate instruction required: the seeded shuffles did not find
what the file-order runs missed, which is itself the useful outcome of
finally being able to run them — the gap is closed and the answer it gives
is negative, not skipped.

---

### Scenario: `pytest-randomly` installed into the project's own `.venv`
- Status: EXECUTED
- Input: `dev/requirements-dev.txt` edited (`pytest-randomly>=3.15` added, with
  a comment naming why), then `.venv/bin/python -m pip install pytest-randomly`
- Expected: importable from `dev/.venv`, not from the platform environment
- Actual: `pytest-randomly-4.0.1` installed, confirmed via
  `.venv/bin/python -m pip show pytest-randomly`
- Result: PASS

### Scenario: file order (baseline)
- Status: EXECUTED · Input: `-p no:randomly -o addopts="" -q`
- Actual: **`3192 passed in 267.90s`**, exit 0
- Result: PASS

### Scenario: reversed order
- Status: EXECUTED · Input: `PYTHONPATH=<scratchpad>` `-p no:randomly -p reverse_plugin -o addopts="" -q`, plugin does `items.reverse()`, held outside `dev/`
- Actual: **`3192 passed in 274.19s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 1
- Status: EXECUTED · Input: `-o addopts="" -q -p randomly --randomly-seed=1`
- Actual: **`3192 passed in 274.84s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 7
- Status: EXECUTED · Input: `--randomly-seed=7`
- Actual: **`3192 passed in 275.29s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 42
- Status: EXECUTED · Input: `--randomly-seed=42`
- Actual: **`3192 passed in 276.26s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 20260731
- Status: EXECUTED · Input: `--randomly-seed=20260731`
- Actual: **`3192 passed in 273.87s`**, exit 0
- Result: PASS

### Scenario: the shuffled runs collect the same population, not a subset
- Status: EXECUTED
- Input: each run's own summary line
- Expected: 3,192 in every order — a shuffle that collected fewer would pass
  while testing less
- Actual: **3,192 in all six**
- Result: PASS

---

# PASS 3 — re-run at `dev` @ `f313d41` (final confirmation)

**Commit under test:** `f313d41` (was `7ecba21`) · **Owner:** `test-agent` ·
**Blocking:** yes · **Status:** `EXECUTED`

`AC-COCKPIT-20`'s new test adds one scenario to the collected population
(3,192 -> 3,193); the sweep is re-run in full rather than assumed to still
hold, since this is the third pass on this enhancement.

## Result

| Order | Result | Wall |
|---|---|---|
| file (`-p no:randomly -o addopts=""`) | **3193 passed** | 313.07s |
| reversed (node ids collected in file order, `tac`'d, passed explicitly on the command line — held outside `dev/`, same property as pass 2's out-of-tree plugin: the tree under test cannot influence its own shuffle) | **3193 passed** | 311.36s |
| seed 1 (`-p randomly --randomly-seed=1`) | **3193 passed** | 313.29s |
| seed 7 (`--randomly-seed=7`) | **3193 passed** | 313.36s |
| seed 42 (`--randomly-seed=42`) | **3193 passed** | 314.44s |
| seed 20260731 (`--randomly-seed=20260731`) | **3193 passed** | 315.17s |

**Six for six, 3,193 every time, exit 0 every time. No order dependence
found**, including under the one new scenario (`AC-COCKPIT-20`'s three-way
resolve-and-compare test, which mutates process-scoped `PilotState` by
actually resolving an item — the exact shape of state a shuffle-sensitive
leak would show up in).

### Scenario: file order, pass 3
- Status: EXECUTED · Input: `-p no:randomly -o addopts="" -q`
- Actual: **`3193 passed in 313.07s`**, exit 0
- Result: PASS

### Scenario: reversed order, pass 3
- Status: EXECUTED · Input: node ids collected forward, reversed with `tac`,
  passed explicitly to `pytest -p no:randomly -o addopts=""`
- Actual: **`3193 passed in 311.36s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 1, pass 3
- Status: EXECUTED · Input: `-p randomly --randomly-seed=1 -o addopts=""`
- Actual: **`3193 passed in 313.29s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 7, pass 3
- Status: EXECUTED · Input: `--randomly-seed=7`
- Actual: **`3193 passed in 313.36s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 42, pass 3
- Status: EXECUTED · Input: `--randomly-seed=42`
- Actual: **`3193 passed in 314.44s`**, exit 0
- Result: PASS

### Scenario: seeded shuffle, seed 20260731, pass 3
- Status: EXECUTED · Input: `--randomly-seed=20260731`
- Actual: **`3193 passed in 315.17s`**, exit 0
- Result: PASS

### Scenario: the shuffled runs collect the same population, not a subset, pass 3
- Status: EXECUTED
- Input: each run's own summary line
- Expected: 3,193 in every order
- Actual: **3,193 in all six**
- Result: PASS
