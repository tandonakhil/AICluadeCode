# Changelog — `accelerators/test-scaffold`

## 1.0.0 — 2026-08-08

Initial harvest (A4, built first per `accelerators/CATALOGUE.md`'s stated
build order, since every other accelerator's own H4 suite depends on the
convention this one defines).

- `src/browser.py` — Playwright-backed rendered-UI harness, harvested
  verbatim from five confirmed-byte-identical sources (`templates/genai-chatbot`,
  `templates/agentic-workflow`, `templates/rag-knowledge-base`,
  `projects/conclave-marketing/dev`, `projects/little-milestones/dev`, all at
  `tests/suites/harness/browser.py`). No content changes.
- `src/native.py` — React Native Testing Library-backed rendered-UI harness,
  harvested verbatim from `projects/little-milestones/dev/tests/suites/harness/native.py`.
  No content changes.
- `tests/run.sh` — this accelerator's own H4 admission suite. Static-review-only
  by necessity (no live browser/app process per H4); checks host-decoupling
  (H3), clean import, and public-surface signature conformance to
  `ACCELERATOR.md`.
- `kb-seed/_runner_convention.md` — the platform's `0/1/3/4` exit-code
  convention as a standalone, citable document, plus the recorded (not
  resolved) `conclave-finance-studio` `_runner.sh` delta.
- `ACCELERATOR.md` — H1 contract, H2 config table, H6 provenance, H10
  known-origin list, adoption steps.

Approving decision: `admin/proposals/2026-08-08-accelerator-layer.md`; human
approved this A4 harvest 2026-08-08.
