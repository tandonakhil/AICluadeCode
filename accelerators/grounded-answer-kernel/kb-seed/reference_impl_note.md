# Reference implementation -- NOT included in this harvest pass

Stated plainly, per the prior review's finding: this harvest pass moved
**contracts and pure-logic kernels** (L0's doc, L1's sentinel/refusal/
sources, L2's protocol/hash_embed, L3's coverage_ledger/abstention/verify)
into `accelerators/grounded-answer-kernel/`. It does **not** include a
worked, wired-together reference implementation running these four layers
end-to-end over two sample documents.

The prior review named this gap explicitly: **"otherwise L3 reads as
theory."** A pure `verify()` function and an unconstructible-if-unbalanced
`Coverage` class are individually testable (see `tests/test_kernel.py`), but
nothing in this accelerator currently shows an adopter the full path --
ingest two documents, embed them with `hash_embed`, retrieve, compose,
verify, seal a coverage ledger, and render either an answer or a named
refusal -- glued together and runnable against real (if tiny) data.

**This is a named follow-up, not a silent omission.** Recommended next step:
a `reference/` subdirectory (not yet created) containing:

- two short sample documents (public domain or synthetic, matching the
  spirit of `rate-case-analyzer`'s synthetic corpus discipline);
- a `wire.py` showing one way to join L1 + L2 + L3 (analogous in *purpose*,
  not in domain content, to RCA's `app/wiring/compose_root.py` -- the one
  named join point whose import closure contains both the store and the
  retriever, which is what makes an import-boundary assertion meaningful
  rather than merely "nobody happens to import that");
- one worked query that resolves to an answer with sources, and one worked
  query that resolves to a refusal naming its gap, both runnable via
  `tests/run.sh` with no credentials.

Until that exists, an adopting project's `solution-architect` should expect
to do real integration work wiring L1/L2/L3 together, not to find a running
example to copy. This is disclosed here so a future architect evaluating
this accelerator for `reuse` does not discover the gap three gates in --
per the admission brief, "written so a future architect can decide *not* to
use it."
