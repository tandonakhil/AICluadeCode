# A4 — `test-scaffold`

Suite scaffold and rendered-UI harnesses, plus the platform's `0/1/3/4`
exit-code convention every other accelerator's own suite must satisfy (H4).
Built **first**, ahead of A1–A3/A5, precisely because it defines that
convention rather than consuming it.

## H1 · Declared contract

Public surface — anything not listed here is private and may change in a
MINOR release without notice:

**`src/browser.py`** (Playwright backend):
- `render(url: str, *, width: int = 1280, height: int = 900, theme: str | None = None)` —
  context manager yielding a `Page`.
- `Page` — wraps a Playwright page; `__getattr__` passes through to the
  underlying Playwright API for anything not listed below. Declared additions:
  - `effective_opacity(locator) -> float`
  - `computed(locator, prop: str) -> str`
  - `has_horizontal_overflow() -> bool`
  - `visible_text() -> str`
  - `screenshot_evidence(name: str, evidence_dir: str = "test-evidence") -> str`
- `HarnessUnavailable(RuntimeError)` — raised, never masqueraded as a pass,
  when Playwright or its browser binary is missing.

**`src/native.py`** (React Native Testing Library backend):
- `run_native_render_tests(pattern: str | None = None, timeout: int = 300) -> NativeResult` —
  runs the project's RNTL/jest suite from its **real entry point**, synchronously.
- `reachable_components(screen_sources: dict[str, str]) -> dict[str, list[str]]` —
  static companion check (JSX element names per screen source); pairs with,
  never replaces, the RNTL run.
- `NativeResult` — dataclass: `passed: bool`, `total: int`, `failed: int`,
  `summary: str`, `__bool__` returns `passed`.
- `HarnessUnavailable(RuntimeError)` — same honest-degradation contract as
  `browser.py`'s.

Everything else in either module (`_require_playwright`, `_require_toolchain`,
`DEV_ROOT`, `MOBILE`) is private implementation detail and may change without
a version bump to the public contract.

## Purpose

A rendered-UI test harness — headless browser for web (`browser.py`), React
Native Testing Library glue for native (`native.py`) — that SME test suites
(`ux`, `functional`, `architecture`, etc.) call into so that **"the component
compiles" and "the component is reachable and rendered" remain two different,
both-required assertions, not one.**

This distinction is not hypothetical. `admin/LESSONS.md`, 2026-07-28: *"A
component-rendering test proves compilation, not reachability."* The F18
mobile build shipped six rendering defects — `Avatar` built and imported but
never rendered; `RemoteImage`/`Lightbox`/gallery state-managed but never
mounted; `ChatHistorySheet` imported AND state-managed AND never mounted —
while every SME test suite reported green, because the only checks in place
proved the components compiled, not that the running app actually reached
and rendered them. `native.py`'s `run_native_render_tests` exists specifically
to close that gap: it mandates rendering **from the screen's or app's real
entry point**, not the component in isolation.

```python
render(<Avatar />)            # passes while Avatar is mounted nowhere
render(<TodayScreen />)       # fails until Avatar is actually wired in
```

`browser.py` exists for the web-side sibling defect: a real compounding-opacity
bug (CSS `opacity` multiplying with a per-shape alpha, leaving an element
composited invisible) and several layout defects shipped because no
non-rendering reviewer could see them — inspecting HTTP responses and HTML
*source* cannot see what a visitor actually sees.

## H2 · Config-vs-code boundary

| What an adopting suite configures | What is fixed (the harness's own API surface) |
|---|---|
| The URL/base path passed to `render()` | The context-manager shape of `render()` — always synchronous, always yields a `Page` |
| Viewport `width`/`height` | The `Page` wrapper's method names and return types |
| `theme` (`"light"`/`"dark"`/`None`) | `effective_opacity`'s ancestor-chain multiplication algorithm |
| `SUITE_REDUCED_MOTION` env var (reduced-motion testing) | `HarnessUnavailable` as the sole honest-degradation signal — a suite must never catch this and report a pass |
| Screenshot `name`/`evidence_dir` for `screenshot_evidence` | The `test-evidence/screenshots/` subdirectory convention |
| `pattern`/`timeout` passed to `run_native_render_tests` | Jest's `--json --silent` invocation and the JSON-line parsing logic |
| The `screen_sources` dict passed to `reachable_components` | The JSX-tag-name regex it applies |
| Project layout: `native.py` expects `mobile/` at `DEV_ROOT/mobile` (three parents up from the harness file, i.e. `dev/tests/suites/harness/native.py`) | The `DEV_ROOT`/`MOBILE` path-derivation logic itself — moving the harness to a different depth requires a fork, not configuration |

Anything not in the left column is welded into the source; varying it means
forking, not configuring.

## H3 · Host decoupling

Both modules import only the Python standard library at module scope
(`contextlib`, `os`, `pathlib` for `browser.py`; `dataclasses`, `json`,
`pathlib`, `shutil`, `subprocess` for `native.py`) plus a **lazily deferred**
`from playwright.sync_api import sync_playwright` inside `_require_playwright`.
Neither module imports any host project's domain package. Verified manually by
reading both files in full at harvest time (2026-08-08) — no `from app.`,
`from backend.`, or project-specific import appears in either — and re-asserted
mechanically by this accelerator's own `tests/run.sh` (check 1/3, a
grep-equivalent scan). `native.py`'s only project-shaped coupling is a
**path convention**, not an import: it expects a `mobile/` directory three
levels above its own vendored location, which is config-by-placement, not code
coupling.

## H4 · Own executable suite

`tests/run.sh` — see that file's own header for the full breakdown. Summary:
it is **static-review-only by necessity**, because this accelerator's payload
*is* the thing that would otherwise spin up a browser/native toolchain, and
H4 itself prohibits a suite starting a long-lived process. What it verifies:

| Check | Static or would-need-live-harness |
|---|---|
| 1. No host-project imports (H3 scan) | **Static** — pure text/import inspection |
| 2. `browser.py`/`native.py` import cleanly | **Static** — a plain Python import; neither module touches Playwright/jest at import time |
| 3. Public surface matches this document's H1 contract | **Static** — `inspect.signature` against the names/params documented above |

What it does **not** and structurally **cannot** verify without a live
harness: that `render()` actually launches a working browser and produces
correct rendered-DOM assertions, or that `run_native_render_tests()` actually
drives jest against a real component tree and catches a real reachability
defect. That evidence is this harness's own production history (H6, below) —
and per `solution-architect`'s "Reuse never lowers the evidence bar," an
adopting project must still prove its **own** use of the harness at its own
Test gate; H6 provenance is not a substitute for that.

Exit codes: `0` all static checks passed, `1` one or more failed, `3` no
harness modules found in `src/`, `4` no `python3` interpreter — the same
convention documented standalone in `kb-seed/_runner_convention.md`.

## H5 · Negative controls

Not applicable in the H5 sense (*"a fixture that makes the guard fire, and one
that makes it not"*) — this accelerator is a harness, not a guard. Its own
honest-degradation behaviour (`HarnessUnavailable` on missing dependency) is
exercised implicitly by `tests/run.sh` check 2, which runs in an environment
where Playwright/jest are typically absent and confirms that absence does not
crash the import or masquerade as a pass — but this is not a formal negative
control in the H5 sense and is not claimed as satisfying H5.

## H6 · Provenance

Harvested 2026-08-08 from five on-disk copies, confirmed **byte-identical**
before harvest (full-file read comparison, not a hash tool — this agent holds
no `Bash`):

- `templates/genai-chatbot/tests/suites/harness/browser.py`
- `templates/agentic-workflow/tests/suites/harness/browser.py`
- `templates/rag-knowledge-base/tests/suites/harness/browser.py`
- `projects/conclave-marketing/dev/tests/suites/harness/browser.py`
- `projects/little-milestones/dev/tests/suites/harness/browser.py`

`src/native.py` harvested from the one source that has it:
`projects/little-milestones/dev/tests/suites/harness/native.py`. It proved
itself in production by catching a real defect all six SME test suites missed
— `ChatHistorySheet` imported, state-managed, and never mounted (see Purpose,
above, and `admin/LESSONS.md` 2026-07-28).

**What was deliberately left behind**: the Maestro + simulator native backend
this platform originally intended (deferred when a toolchain spike found no
simulator available — RNTL fills the gap beneath it, not the same job). Also
left behind: `_runner.sh` itself is **not** vendored into `src/` — it is
per-project authored (see `kb-seed/_runner_convention.md`'s Adoption note) —
and the `conclave-finance-studio` `_runner.sh` variant, which diverges from
the five-way-identical reference in ways recorded in that same file rather
than silently reconciled.

Source files themselves were **not modified** by this harvest — the five
originals in `templates/` and `projects/` are untouched; this is copy-out,
not move.

## H7 · Semver + CHANGELOG

`VERSION` currently `1.0.0` — this is a proven, five-times-battle-tested
harvest (five identical production copies), not a first draft, so it starts
above `0.x`. See `CHANGELOG.md`.

## H8 · Deprecation

Not deprecated. No prior version exists to supersede.

## H9 · Co-signs

Neither co-sign applies: this accelerator touches no credentials, sessions,
secrets or PII (no H9-security trigger), and sits on no grounding, refusal or
guardrail path (no H9-responsible-AI trigger). It is a test harness.

## H10 · Known consumers

At harvest time, these are the **origin** projects/templates this accelerator
was harvested *from* — not yet real "vendored from the catalogue" consumers,
since nothing has been vendored back out of `accelerators/` yet:

| Project/template | File | Version at harvest |
|---|---|---|
| `templates/genai-chatbot` | `tests/suites/harness/browser.py` | pre-accelerator (origin) |
| `templates/agentic-workflow` | `tests/suites/harness/browser.py` | pre-accelerator (origin) |
| `templates/rag-knowledge-base` | `tests/suites/harness/browser.py` | pre-accelerator (origin) |
| `projects/conclave-marketing/dev` | `tests/suites/harness/browser.py` | pre-accelerator (origin) |
| `projects/little-milestones/dev` | `tests/suites/harness/browser.py`, `harness/native.py` | pre-accelerator (origin) |

Once a project vendors `1.0.0` from `accelerators/test-scaffold/` going
forward, that project is added here as a real consumer at the vendored
version, per H10's own rule (`who has the old copy?` must always be
answerable).

## Adoption steps (`code-agent`)

1. Copy `src/browser.py` and, if the project has a native/mobile surface,
   `src/native.py`, into the project's `dev/tests/suites/harness/`.
2. Stamp each vendored file per `accelerators/README.md`'s convention:
   ```
   # VENDORED from accelerators/test-scaffold@1.0.0 on <date>.
   # Local edits are permitted and expected. If you fix a defect here,
   # report it upstream — see accelerators/test-scaffold/ACCELERATOR.md.
   ```
3. Author `dev/tests/suites/_runner.sh` following
   `kb-seed/_runner_convention.md` — it is **not** vendored as a file; it is a
   convention re-authored per project (per `admin/LESSONS.md` 2026-07-26/"B2":
   `code-agent` authors suite entry points at the Code gate).
4. Record the vendor event in `projects/<name>/PROJECT_CONTEXT.md`'s
   `## Accelerators` section: name, version, vendored date, sha256 at vendor
   time, and the reuse/adapt/build-new reason.
5. Install the runtime dependency the harness needs, only if the `ux` suite
   uses rendered checks: `.venv/bin/pip install playwright && .venv/bin/playwright install chromium`.
   `native.py`'s dependency (`node_modules`, `npx`, jest/RNTL) is whatever the
   project's own `mobile/` already requires — nothing extra to install for the
   harness itself.
6. The adopting project's own `ux`/relevant suite must still prove its own use
   of the harness at its own Test gate — vendoring this accelerator's H6
   provenance does not transfer verification (`solution-architect`'s "Reuse
   never lowers the evidence bar").

## Change history

| Date | Version | Change | Approving decision |
|---|---|---|---|
| 2026-08-08 | 1.0.0 | Initial harvest — `browser.py` (five byte-identical sources) and `native.py` (from `little-milestones`), plus this accelerator's own H4 static-review suite and the standalone `_runner.sh` convention doc. | `admin/proposals/2026-08-08-accelerator-layer.md`; human approved this A4 harvest 2026-08-08 |
