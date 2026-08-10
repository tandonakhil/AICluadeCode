#!/usr/bin/env bash
# accelerators/auth-core -- executable suite, platform exit-code convention
# (A4 / admin/proposals/2026-08-08-accelerator-layer.md, H4):
#   0 = pass
#   1 = fail
#   3 = no scenarios defined (an empty suite is not a passing suite)
#   4 = cannot execute -> STATIC ONLY, not a suite failure
#
# Standalone: no app server, no long-lived process, no network, no
# credentials. Runs entirely in-process against an in-memory sqlite3
# connection via FastAPI's TestClient (ASGI, no bound socket).
#
# This is written as source for `code-agent`/`test-agent` to vendor and
# EXECUTE inside the consuming project's own test environment (per
# code-agent's duty to copy an accelerator's tests, not just its source) --
# `mas-registrar` does not hold a Bash grant and has not run this script.

set -u
cd "$(dirname "${BASH_SOURCE[0]}")/.."

if ! command -v python3 >/dev/null 2>&1; then
  echo "STATIC ONLY -- python3 not found on PATH" >&2
  exit 4
fi

if ! python3 -c "import pytest, fastapi, passlib, pyotp, cryptography" >/dev/null 2>&1; then
  echo "STATIC ONLY -- one or more required packages (pytest, fastapi, passlib[argon2], pyotp, cryptography) not installed" >&2
  exit 4
fi

collected="$(python3 -m pytest tests/ --collect-only -q 2>/dev/null | grep -c '::test_' || true)"
if [ "${collected:-0}" -eq 0 ]; then
  echo "NO SCENARIOS DEFINED -- pytest collected zero test_* functions under tests/" >&2
  exit 3
fi

python3 -m pytest tests/ -q
status=$?

if [ "$status" -eq 0 ]; then
  echo "PASS -- ${collected} scenarios"
  exit 0
else
  echo "FAIL -- see pytest output above"
  exit 1
fi
