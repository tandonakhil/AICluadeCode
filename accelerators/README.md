# `accelerators/` — orientation

A **peer of `templates/`**, never nested inside it. Governed on the platform
axis via `/admin-panel`.

Established by `admin/proposals/2026-08-08-accelerator-layer.md`, approved by
the human 2026-08-08.

## What an accelerator is

A **hardened, self-contained component** — with a declared contract, its own
runnable test suite, and a provenance document — that a future project can copy
in rather than re-derive. The qualifying test is *"is this a strong, well-built
component a future project would want?"* — **not** *"has it been built twice?"*
Built once, well, is enough. (That is the human's explicit scope correction of
2026-08-08, which overrode a proposed rule-of-three promotion bar.)

The cost an accelerator removes is **re-derivation, not typing**. A single
Architecture gate runs 65k–132k tokens; `rate-case-analyzer` re-derived
`policy-lookup-assistant`'s grounding contract at full gate cost and changed one
signature. Savings are counted in **fractions of a gate not re-derived**.

## How it differs from a template

The boundary is **cardinality and selection time**:

| | `templates/` | `accelerators/` |
|---|---|---|
| How many apply | **Exactly one** per project | **Zero to many** per project |
| Chosen when | At project creation, before Intake | At the **Architecture gate**, per entry |
| Scope | The whole scaffold — the shape of the app | One component with a declared contract |
| Chosen by | `plan-agent`'s recommendation + human confirm | `solution-architect`'s Reuse Decision Table |

A template answers *"what shape is this project?"* An accelerator answers
*"which already-solved problems does this project not need to solve again?"*

The mechanism also exists because templates **structurally cannot express
cross-template reuse**: `tests/suites/harness/browser.py` is byte-identical in
five places, three of them *inside* `templates/`. The template mechanism's own
answer to "this is shared across templates" is to paste it three times.

## Distribution: vendoring by copy, with a provenance stamp

Accelerators are **copied into** a project, never referenced from it. This is
not a compromise — it is what demonstrably already works here (`app/llm.py` has
been byte-identical across four independent repos for a month).

Every vendored file carries a stamp:

```
# VENDORED from accelerators/auth-core@1.2.0 on 2026-08-08.
# Local edits are permitted and expected. If you fix a defect here,
# report it upstream — see accelerators/auth-core/ACCELERATOR.md.
```

Provenance is additionally recorded in an `## Accelerators` section of
`projects/<name>/PROJECT_CONTEXT.md`: **name, version, vendored date, sha256 at
vendor time, and the reuse/adapt/build-new reason.** That file sits at project
root, **outside `dev/`**, so it survives `dev/` being an independent git repo
and is readable by every gate without cloning anything.

Copy-in vendoring's one real weakness is that it cannot notice divergence — and
that is exactly what failed when `little-milestones`' red-team-discovered
`max_tokens=4096` fix never went back upstream. So the mechanism is **copy plus
the missing half**: `solution-architect`'s architecture suite carries
`test_accelerator_provenance` and `test_accelerator_drift`, which **report**
clean / local divergence / upstream ahead, and **never auto-sync**.

## Hard rule — projects NEVER reference `accelerators/` at runtime

**No git submodules. No `pip install -e`. No cross-repo path dependencies. No
imports, symlinks or sys.path entries reaching out of the project tree.**

Recorded here so it is not re-litigated: every such mechanism creates a
cross-repo coupling this platform has deliberately never had; each makes `dev/`
non-self-contained; and each would break `deploy-agent`'s local-only model and
`release-manager`'s `dev/`→`prod/` promotion. `projects/<name>/dev/` are
independent git repos, there is no monorepo and no package registry.

The absence of a registry **structurally immunises this platform against the
distributed-monolith failure mode — a feature to preserve, not a limitation to
fix later.** Copy-in keeps every project exactly as independent as it is today,
and pays for it with a **drift report** rather than with coupling.

## Layout

```
accelerators/
  CATALOGUE.md                 # compact index — read at EVERY Architecture gate
  ADMISSION.md                 # H1–H10
  README.md                    # this file
  <name>/
    ACCELERATOR.md             # H1 contract, H2 config table, H6 provenance,
                               # H10 consumers, adoption steps
    VERSION                    # semver
    CHANGELOG.md
    src/                       # the vendorable payload
    tests/run.sh               # H4, platform exit codes
    tests/negative_controls/   # H5, where applicable
    kb-seed/                   # optional SECURITY_KB / ARCHITECTURE_KB fragments
```

## Who does what

Ownership splits by verb; there is deliberately **no accelerator-curator
agent** and **no new gate** (both were evaluated and rejected — no distinct
gate, no distinct per-project KB, no distinct test suite, heavy overlap).

| Verb | Owner |
|---|---|
| Consult before designing new | `solution-architect` |
| Nominate for harvest | `solution-architect` |
| **Approve promotion into the catalogue** | **the human** |
| Write the catalogue row + place the files | `mas-registrar` |
| Version / deprecate / CHANGELOG | `mas-release-manager` |
| Copy an accelerator into a project | `code-agent` |
| Audit `CATALOGUE.md` against disk | `mas-architect` |

`solution-architect` holds **no write access** to `accelerators/` and must never
fix a catalogue defect in place — it reports defects by slug and version.

## Two honest caveats

- **Token savings are inferred, not measured.** Nothing has been reused yet, so
  every figure in the approving proposal is order-of-magnitude. `usage-monitor`
  should record real pre/post figures on the first project that adopts an
  accelerator; that one data point is worth more than the whole estimate column.
- **A catalogue also *adds* tokens** — `CATALOGUE.md` is read at every
  Architecture gate forever. That is why the index stays compact, and why the
  size constraint is written into the file itself.
