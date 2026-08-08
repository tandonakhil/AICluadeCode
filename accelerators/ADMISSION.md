# Admission criteria — H1 through H10

An entry enters `accelerators/CATALOGUE.md` only if **all ten** hold. Not most.

`solution-architect` + `security-architect` **jointly approve admission**;
`mas-architect` reviews any change to the *shape* of the catalogue itself; the
**human approves every promotion** into the catalogue. `mas-registrar` writes
the row and places the files only after that approval.

Source: `admin/proposals/2026-08-08-accelerator-layer.md`, approved by the human
2026-08-08.

---

## H1 · Declared contract

A named public surface. Anything not listed is **private** and may change in a
MINOR release without notice. An adopter who reaches past the declared surface
has forked, whether or not they noticed.

## H2 · Config-vs-code boundary, stated as a table

An explicit table of what an adopter changes **by configuration** versus what
requires a **fork**. *"It's configurable"* without the table **fails admission**.
The failure mode this prevents is the adopter who discovers, three gates in, that
the one thing they needed to vary is welded into the source.

## H3 · Host decoupling, proven

No import of a host project's domain modules — and *proven*, not asserted, by
pointing **A5's own closure checker** at the accelerator. The catalogue eats its
own dog food: the structural conformance kit is the instrument that admits
everything else, including itself.

## H4 · Own executable suite

At `accelerators/<name>/tests/run.sh`, in the **platform exit-code convention**
(A4 defines it: `0` pass, `1` fail, `3` = no scenarios defined — so *an empty
suite is not a passing suite* — `4` = cannot execute → `STATIC ONLY`), and
**standalone**: no app server, **no long-lived process**, no network, **no
credentials**.

- The **no-long-lived-process rule traces to `admin/LESSONS.md`, 2026-07-09**: a
  process started inside a subagent's turn dies when that turn ends, so a suite
  that starts a server is a suite that reports on nothing.
- **UI accelerators need reachability-from-entry-point tests, never standalone
  renders** — traces to `admin/LESSONS.md`, 2026-07-28. A test that renders a
  component directly passes perfectly while that component is mounted nowhere in
  the real application; that is precisely defects 1–4 of the F18 ledger.

These attributions are recorded because they are *why* the rules are trusted:
each was paid for by a real defect, not reasoned out in advance.

## H5 · Negative control for anything that is a guard

A fixture that makes the guard **fire**, and one that makes it **not** fire. A
guard admitted without a negative control is a guard **nobody has confirmed can
fail** — it may be passing because it is correct or because it is inert, and
nothing distinguishes those two states.

Traces to `admin/LESSONS.md`, 2026-07-28: *always run a negative control before
trusting a new guard.*

## H6 · Provenance and rationale doc

Exact source paths and commit, **what defect it prevents**, and **what was
deliberately left behind**. Written so that a future architect can decide **not**
to use it — a document that only argues for adoption is marketing, and the
Reuse Decision Table requires a real basis for `build-new` as much as for
`reuse`.

## H7 · Semver + CHANGELOG

Per-entry `VERSION` and `CHANGELOG.md`. A **MAJOR requires a migration note
naming every known consumer** (which is what makes H10 load-bearing rather than
decorative).

## H8 · Deprecation is marking, never deletion

A superseded accelerator **stays runnable**. Its catalogue entry records what
supersedes it and why. Deleting it would silently strand every project that
vendored it and destroy the record of why the older shape existed.

## H9 · Co-signs

- **Security co-sign** (`security-architect`) for anything touching
  credentials, sessions, secrets or PII — **A1 unconditionally**.
- **Responsible-AI co-sign** (`responsible-ai-architect`) for anything on a
  grounding, refusal or guardrail path — **A2**.

## H10 · Known-consumers list

Every entry names the projects that vendored it **and at which version**.
Without it, *"who has the old copy?"* is unanswerable — the exact condition
under which the `max_tokens=4096` fix stayed trapped in `little-milestones`
while every other chatbot inherited the broken default.

---

## Standing note — admission is not verification transfer

Passing H1–H10 says the accelerator is **fit to be offered**. It says nothing
about whether an adopting project has verified its own use of it. Evidence
produced in the *source* project **does not transfer**; see
`solution-architect`'s contract, "Reuse never lowers the evidence bar."
