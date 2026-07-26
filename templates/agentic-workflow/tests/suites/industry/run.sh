#!/usr/bin/env bash
# Entry point for the "industry" suite. Invoked by its owning SME agent
# (scoped Bash) and aggregated by test-agent at the Test gate.
exec "$(dirname "${BASH_SOURCE[0]}")/../_runner.sh" industry
