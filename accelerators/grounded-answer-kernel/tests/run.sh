#!/usr/bin/env bash
# accelerators/grounded-answer-kernel/tests/run.sh -- this accelerator's own
# H4 admission suite.
#
# STATIC-ONLY / EXECUTION-PENDING: this script and test_kernel.py were
# written by mas-registrar, which holds no Bash tool grant and therefore
# could NOT run this suite. It is committed as STATIC ONLY -- NOT EXECUTED,
# per this platform's standing policy for claims that cannot be run inside
# the writing agent's own turn. The next agent or human with a Python +
# pytest environment should execute this for real before the suite is
# treated as a green H4 pass. This is disclosed rather than silently
# omitted (see ACCELERATOR.md, H4/H6 sections).
#
# The sentinel's zero-import/no-regex/no-substring property and the coverage
# ledger's seal-invariant ARE genuinely testable as pure-Python unit tests
# with no live service, no network, and no credentials -- that is the whole
# point of L1 and L3 being written the way they are.
#
# Exit codes -- the platform convention (accelerators/test-scaffold):
#   0 = all checks passed
#   1 = one or more checks failed
#   3 = no scenarios defined
#   4 = cannot execute (no interpreter / no pytest) -- used here because
#       this suite has never actually been run, which this script discloses
#       up front rather than reporting a 0 it cannot back.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "-- accelerators/grounded-answer-kernel -- H4 admission suite --"
echo ""
echo "STATIC ONLY -- NOT EXECUTED by the agent that wrote this file (no Bash grant)."
echo "test_kernel.py exercises: sentinel closure (1), CoverageLedger.seal()"
echo "balance invariant + no-public-constructor (2-3), build_sources arity (4),"
echo "verify() all-or-nothing discard (5), abstention UNKNOWN-never-negative (6)."
echo ""

if [ ! -f "$HERE/test_kernel.py" ]; then
  echo "NO SCENARIOS DEFINED -- test_kernel.py is missing."
  exit 3
fi

PY="$(command -v python3 || true)"
if [ -z "$PY" ]; then
  echo "CANNOT EXECUTE -- no python3 interpreter found."
  exit 4
fi

if ! "$PY" -c "import pytest" 2>/dev/null; then
  echo "CANNOT EXECUTE -- pytest is not installed in this environment."
  echo "(numpy is also required by src/l2_retrieval/hash_embed.py if that"
  echo "module is imported by an extended run of this suite.)"
  exit 4
fi

echo "interpreter: $PY"
echo "running: pytest $HERE/test_kernel.py -v"
echo ""

if "$PY" -m pytest "$HERE/test_kernel.py" -v; then
  echo ""
  echo "EXECUTED -- all checks passed."
  exit 0
else
  echo ""
  echo "EXECUTED -- one or more checks FAILED."
  exit 1
fi
