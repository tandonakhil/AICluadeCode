# Test suites — SME-owned, executable

Each subdirectory is a **test suite owned by one SME agent** (see
`admin/MAS_REGISTRY.md` for the authoritative owner of each). The owning agent
invokes its own suite via that suite's `run.sh` using its scoped `Bash` grant.
`test-agent` aggregates all active suites into the per-suite report at the Test
gate.

| Suite | Owner | Checks |
|---|---|---|
| `functional/` | functional-agent | Domain correctness |
| `industry/` | industry-expert | Industry / compliance expectations |
| `ux/` | ui-ux-designer | UX, usability, accessibility, **rendered output** |
| `architecture/` | solution-architect | Architecture conformance, contracts |
| `security/` | security-architect | Authz boundaries, input validation, secrets |
| `redteam/` | responsible-ai-architect | Red-team, bias, content guardrails |

`test-agent` owns unit/integration separately — that stays the project's main
`pytest` run, not a suite here.

## Why this exists

Before this convention, the six SME agents owned suites but had **no shell
tool**, so they could only ever produce a static review. That is not
verification. The real cost was measured: `responsible-ai-architect` once
returned `STATIC ONLY — NOT EXECUTED` on 6 of 7 scenarios; when the suite was
actually executed it surfaced **three defects the static review had missed**.

## Running a suite

```sh
tests/suites/<suite>/run.sh
```

## Exit codes (meaningful — test-agent maps these to its report)

| Code | Meaning | How test-agent must report it |
|---|---|---|
| `0` | Executed, all scenarios passed | **EXECUTED — passed** |
| `1` | Executed, one or more failed | **EXECUTED — failed** (blocking unless the project's Test Policy marks this suite advisory) |
| `3` | No scenarios defined | **EMPTY — not a pass.** An empty suite must never be reported as passing |
| `4` | Cannot execute (missing interpreter/dependency) | **STATIC-ONLY** — findings are review-only, not verification |

The `3` and `4` codes exist specifically so an unexecuted suite and a passing
suite are never indistinguishable in the report.

## Adding scenarios

Drop `test_*.py` files into the suite's directory. They run under the
project's own venv (`dev/.venv` or `dev/backend/.venv`) via `pytest`. Capture
per-scenario evidence into `test-evidence/` in the format `test-agent`'s
contract defines (Input / Expected / Actual / Result / Evidence).

## Rendered-UI checks (the `ux` suite)

`harness/browser.py` provides a Playwright-backed helper for asserting on what
actually **renders** — computed styles, the accessibility tree, visible text,
and screenshots — rather than on HTML source. This is the class of defect that
was previously invisible to every automated check: a real compounding-opacity
bug and several layout defects shipped because no non-rendering reviewer could
see them, and a human had to report them by hand.

**Process-lifecycle rule:** a server or browser started *inside a subagent's
turn dies when that turn ends*. The harness therefore drives Playwright
synchronously within a single command invocation. Any long-lived app server the
suite needs must be started by `deploy-agent` or the orchestrator first — never
backgrounded from inside a suite.

Setup (once per project, if the `ux` suite uses rendered checks):

```sh
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
```

If Playwright is absent the harness reports **STATIC-ONLY** (exit `4`) rather
than failing — an honest "could not verify" beats a false pass.
