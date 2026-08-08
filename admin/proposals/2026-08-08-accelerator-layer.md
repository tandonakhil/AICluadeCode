# Proposal — the accelerator layer (`accelerators/`)

**Raised**: 2026-08-08 by the human.
**Status**: **APPROVED by the human 2026-08-08** (full MVP-1 scope, A1–A5, plus
all four open items). Ready for `mas-registrar`.
**Reviews**: `solution-architect` (technical inventory) and `mas-architect`
(platform governance), run in parallel 2026-08-08.
**Route**: `/admin-panel` — platform axis. Touches `projects/` read-only, for
harvest only; see the two-axes carve-out in §6.

---

## The human's request, verbatim

> New activity for admin - we need to look and evaluate all projects to see
> components which have been developed already should be move to accelerators,
> also find industry leading ways to harden these accelerators and make them
> plug and play. few examples would include
>
> 1) Deisgn principles from conclave, design language, and journey maps approach
> 2) Authentication and authorization module
> 3) Reusable RAG frameworks
> 4) Others which you can research and recommend
>
> Solution Architect to review and recommend with orchesterator
>
> These will become part of our integrated offering, additional role for Solution
> Architect when he is deisgning new projects or enhancing he should always
> reference our accelerators and reuse them as much as possible to avoid tokens

**Scope correction issued by the human mid-review**, after the orchestrator's
first brief over-weighted cross-project duplication:

> not ony components which are re-used within projects, just evaluate key
> components from each project, like we build a authentication and authorization
> module for little milestones, that will be a good accelerator for future.
> eavlaute this in detail, look at examples I shared in the begining

This correction is load-bearing and is recorded here because it **overrides**
one of `mas-architect`'s recommendations (§4). The qualifying test for the
catalogue is *"is this a strong, well-built component a future project would
want?"* — **not** *"has it been built twice?"* Built once, well, is enough.

---

## Evidence base — three facts verified on disk

Not anticipatory. Each was checked against the repository, not inferred.

### 1. Half the portfolio abandoned the templates

Four of eight projects record `template: custom` in their own
`pipeline-state.json`: `conclave-dashboard`, `conclave-finance-studio`,
`conclave-marketing`, `rate-case-analyzer`. The three scaffolds under
`templates/` are too thin to carry a real project, and this layer is the
correction.

### 2. Copy-paste distribution works here — and it already leaked a real fix

`app/llm.py` is **byte-identical** (md5 `631bff3e…`) in four places:
`templates/genai-chatbot`, `templates/agentic-workflow`,
`projects/grid-assistant/dev/backend`, `projects/load-alert-agent/dev/backend`.

But `projects/little-milestones/dev/backend/app/llm.py` diverged with a
**red-team-discovered fix** — `max_tokens=4096`, because the 1024 default
truncated answers mid-sentence — and **that fix never went back upstream**.
Every future chatbot project still inherits the broken default.

This single fact is the entire argument for a catalogue with **drift
reporting**, and it is why the drift check was approved for MVP-1 rather than
deferred.

### 3. The template mechanism structurally cannot express cross-template reuse

`tests/suites/harness/browser.py` (138 lines) is byte-identical in **five**
locations — all three templates plus `conclave-marketing` and
`little-milestones`. Three of those copies are *inside* `templates/`. The
template mechanism's own answer to "this is shared across templates" is to
paste it three times. The identical SME-suite prose block is likewise
duplicated verbatim across all three `TEMPLATE_MANIFEST.md` files.

### 4. The cost being paid is re-derivation, not typing

`rate-case-analyzer`'s `app/grounding/verify.py` opens by explicitly naming its
lineage from `policy-lookup-assistant` and stating the one signature it
changed. That re-derivation was paid at **full Architecture-gate cost**. Per
`memory/USAGE_INDEX.md`, `policy-lookup-assistant`'s whole pipeline ran ~647k
tokens; `little-milestones` exceeded 1.6M; a single Architecture gate runs
65k–132k.

**Savings should be counted in fractions of a gate not re-derived**, not lines
not typed.

---

## Approved MVP-1 scope

Approved per-item by checkbox, 2026-08-08. All five accelerators, plus all four
open items.

| # | Accelerator | Source | Maturity | Extraction | Est. saving |
|---|---|---|---|---|---|
| **A1** | Auth & session core (+ mobile token store) | little-milestones | ~1,976 LOC, 58+ tests, hardened by a dedicated increment (F12) and a mobile increment (F18) | Moderate | ~200–350k/project |
| **A2** | Grounded-answer kernel (RAG, 4 layers) | rate-case-analyzer + policy-lookup-assistant + template | RCA: 899 tests, gate 10; contract survived two independent derivations | Moderate | ~100–200k/project |
| **A3** | Conclave design system + journey-map method | CFS + marketing + RCA + dashboard + LM | Token schema independently re-derived 4× | Low-moderate | ~80–150k/project |
| **A4** | Test-suite scaffold & harnesses | 3 templates + marketing + LM + CFS | Byte-identical in 5 places | Trivial | ~40–70k/project |
| **A5** | Structural conformance kit | rate-case-analyzer + CFS | 8 negative-control fixture trees; both pieces written *after* a guard failed | Low | ~50–100k |

**Build order is not rank order.** `A4` is built **first**: every other
accelerator must ship a runnable suite in the platform's exit-code convention
(admission criterion H4), and A4 is what defines it.

### Also approved

- **Drift check from day one.** sha256 provenance + a drift report producing
  *clean* / *local divergence* / *upstream ahead*, living in
  `solution-architect`'s architecture suite. **Reports, never auto-syncs.**
  Resolves the one live conflict between the two reviews in the SA's favour —
  this is the check that would have caught the `max_tokens` leak, and it is what
  makes copy-in vendoring safe rather than merely cheap.
- **Harvest prompt at `/cut-release`.** One non-blocking question after the
  promotion approval: *"anything worth harvesting? [none] / [nominate: …]"* A
  `none` is **recorded**, so it is visible that it was asked. Never blocks a
  release. Human-initiated harvesting via `/admin-panel` remains available at
  any time.
- **Two free-win defect fixes**, independent of the catalogue:
  1. Propagate `max_tokens=4096` into the three template `llm.py` copies.
  2. Fold `policy-lookup-assistant`'s four unpropagated hardening deltas into
     `templates/rag-knowledge-base/`: the `manifest.json` requirement,
     `_extract_text()` normalisation of LangChain's `str | list[block]` content,
     scoped CORS via `FRONTEND_ORIGIN`, and input validation.

### Explicitly below the cut line

`A6` server-rendered HTML kernel · `A7` abstention/coverage vocabulary (ships
inside A2-L3) · `A8` rule registry (**too early — one consumer**; documented as
a pattern, promoted when a second project needs it) · `A9` config
single-reader · `A10` `pipeline-state.json` contract (**platform
infrastructure, not a project accelerator** — overlaps the deferred
`admin/PIPELINE.yaml` item; route via `mas-architect`) · `A11` prompt-fragment
library · `A12` canonical JSON · `A13` rendered-numbers assertion (ships inside
A4) · `A14` cross-surface parity suites (**= deferred ROADMAP C6**).

---

## The four named seeds — findings

### Seed 1 — design principles, design language, journey maps

**There is one coherent *structural* design language and four legitimately
different *palettes*.**

Extract: the token schema (`paper`/`bg` → `surface` → `surface-2` → `surface-3`;
`line` + `line-2`; `ink` → `ink-2` → `ink-3`; `accent` + `accent-bg`; `shadow`),
independently re-derived **four times** across CFS, RCA, dashboard and
marketing; mandatory light/dark via `[data-theme]`; the
`tabular-nums lining-nums` law; the `design-review/` static-HTML mockup
convention (6 projects, no build step, no network, openable from the
filesystem — which is what serves the human's standing rendered-preview-before-
approval rule).

**Do NOT unify the palette values.** Marketing's teal/gold, CFS's no-green risk
ramp, RCA's navy/position-gold and LM's terracotta/sage are each correct for
their product. Forcing one palette would make every product look like the
marketing site — a worse outcome than duplication.

Extract instead a **checklist of semantic laws to choose from**, each tagged
with the project that earned it and the defect it prevents (CFS: "there is no
green", enforced at import time by `assert_no_green()` converting every token to
HSL and refusing hue band 75°–175° above a chroma floor — a green token is an
`ImportError`, not a review comment; RCA: refusal is never styled as an error;
LM: gold is decorative-only, never meaning-bearing).

**On journey maps — the finding is uncomfortable and is the actual
deliverable.** They exist as a designed artefact in exactly one project:
`conclave-finance-studio/design-review/redesign-2026-08-02/v2-journeys.html`.
They were produced **on 2026-08-02, after MVP1 was complete**, in a thread the
human opened *after using the running pilot*. `UX_KB` §A2.4 records that **two
of the four journeys were unwalkable and one unstartable** — severity-A gaps in
a shipped product whose eleven-item flat nav had already passed gate 5.

So the accelerator is **the timing rule, not the artefact**: *journey maps are
produced at Experience Design, before Architecture, and a journey that cannot be
walked end-to-end in the mockups is a gate-5 blocker.*

### Seed 2 — authn/authz (highest-ranked candidate)

The human was right and the orchestrator's first brief was wrong to demote it.
~1,976 LOC product, ~1,455 LOC / 58+ tests, three `SECURITY_KB.md` sections,
survived every gate plus a dedicated hardening increment.

Non-obvious decisions worth never re-deriving: argon2id (not bcrypt — greenfield,
no legacy constraint); session tokens stored SHA-256-hashed **deliberately not**
under a slow KDF; `Secure` cookie flag set *conditionally* because browsers
silently drop `Secure` cookies over local plain HTTP; 30-day sliding expiry
**capped by** a 90-day absolute via `min()`; `DUMMY_PASSWORD_HASH` verified
against unknown emails so timing profiles match (same-cost, not just
same-message); rate limiting as a **sliding timestamp list**, explicitly not a
clock-aligned fixed window, so a boundary burst cannot double the limit; 5
failed TOTP attempts destroy the pending session, named in-contract as the
primary brute-force control; one active reset token enforced **in the same call
as the insert**, so there is never a two-live-token window; on mobile the cookie
is **suppressed entirely** because the platform cookie jar is unencrypted and
inside the backup set.

**Hardening gaps to close before it is droppable** — `security-architect` owns
these:

1. **Persistence coupling is the real blocker.** Every function takes
   `sqlite3.Connection` and issues literal SQL. SA leans to shipping SQLite-only
   and saying so, on the grounds that a repository abstraction is exactly the
   premature abstraction to avoid — but flags it as a design call, not its own.
2. **Two module-global dicts** (`_RATE_BUCKETS`, `_TOTP_FAILURE_COUNTS`) are
   per-process — correct for single-process local deploys, silently wrong under
   any multi-worker deploy. Must be a **documented precondition with a named
   revisit trigger**.
3. **`PHOTO_ENCRYPTION_KEY`** is deliberately reused for TOTP secrets. Rename to
   `APP_ENCRYPTION_KEY`; the key-reuse decision must be **re-blessed per
   adopting project**, never inherited silently.
4. No password-strength policy or breach-list check.
5. `chat_sessions.py` is a chat concern, not an auth concern — split at
   extraction.

**Questions routed to `security-architect`**: is vendored-by-copy auth an
acceptable posture at all, given a CVE-class fix needs manual propagation? Is
the conformance test pack a floor or a ceiling for an adopting project's
security suite? Should `SECURITY_KB` §1/§7/§9 ship as a seed (risking a security
KB that reads as inherited rather than decided)?

### Seed 3 — reusable RAG

**Merge, don't pick.** Four layers, each independently adoptable:

- **L0 · Contract** (doc, ~1 page). "Refusal is a structured signal, not prose."
  "`sources[]` is built by the application from what was verified, never parsed
  from model output." "A refusal names the gap." "Silence is not clearance."
  *This layer alone would have saved most of RCA's re-derivation.*
- **L1 · Kernel** (~150 LOC, zero deps). `sentinel.py` **verbatim** from RCA —
  its zero-import, no-regex, no-substring closure is the whole point and must
  not be diluted; typed refusal kinds; the one-parameter `build_sources()`
  signature, so retrieval hits can never masquerade as support.
- **L2 · Retrieval** (~250 LOC). `EvidenceSource` protocol; `hash_embed`
  unmodified (deterministic, stdlib+numpy, **no API key** — which is why RCA's
  suites are runnable and PLA's are not); a Chroma-backed adapter so PLA-shaped
  projects satisfy the same protocol.
- **L3 · Assurance** (~400 LOC). RCA's `CoverageLedger`/`Coverage` (no public
  constructor — obtainable only via `seal()`, which raises unless
  `included + excluded + unassessable == candidates_considered`); `verify()` as
  a pure function; CFS's abstention vocabulary.

**Do not build one framework both PLA and RCA could have been built on.** They
are architecturally incompatible — LangChain/Chroma `similarity_search` versus a
hand-rolled protocol over three SQLite stores behind an import-boundary wall.
The layering exists precisely so the *contract* can be shared where it really is
common and the *implementations* need not be.

### Seed 4 — others

Ranked in the table above. Beyond the named seeds, the ones most worth pressing
on are **A4** (cheapest win in the portfolio; its 0/1/3/4 exit-code convention —
where `3` = no scenarios defined, so *an empty suite is not a passing suite*, and
`4` = cannot execute → STATIC-ONLY — is the mechanism that makes the platform's
whole `STATIC ONLY — NOT EXECUTED` policy work) and **A5** (the direct answer to
`LESSONS.md`'s "always run a negative control before trusting a new guard").

---

## Admission criteria (H1–H10)

An entry enters the catalogue only if **all** hold. `solution-architect` +
`security-architect` jointly approve admission; `mas-architect` reviews any
catalogue-*shape* change.

- **H1 · Declared contract.** A named public surface. Anything unlisted is
  private and may change in a MINOR.
- **H2 · Config-vs-code boundary, stated as a table.** What an adopter changes
  by configuration vs. what requires a fork. *"It's configurable"* without the
  table fails admission.
- **H3 · Host decoupling, proven.** No import of a host project's domain
  modules — proven by pointing A5's own closure checker at the accelerator. The
  catalogue eats its own dog food.
- **H4 · Own executable suite** at `accelerators/<name>/tests/run.sh`, platform
  exit codes, standalone: no app server, **no long-lived process**
  (`LESSONS.md` 2026-07-09), no network, **no credentials**. UI accelerators
  need reachability-from-entry-point tests, never standalone renders
  (`LESSONS.md` 2026-07-28).
- **H5 · Negative control for anything that is a guard.** A fixture that makes
  it fire and one that makes it not. A guard admitted without one is a guard
  nobody has confirmed can fail.
- **H6 · Provenance and rationale doc** — exact paths and commit, what defect it
  prevents, what was deliberately left behind. Written so a future architect can
  decide **not** to use it.
- **H7 · Semver + CHANGELOG.** MAJOR requires a migration note naming every
  known consumer.
- **H8 · Deprecation is marking, never deletion.** A superseded accelerator
  stays runnable; its entry records what supersedes it and why.
- **H9 · Security co-sign** for anything touching credentials, sessions, secrets
  or PII (A1 unconditionally). **Responsible-AI co-sign** for anything on a
  grounding/refusal/guardrail path (A2).
- **H10 · Known-consumers list.** Every entry names the projects that vendored
  it and at which version — without it, "who has the old copy" is unanswerable.

---

## Catalogue shape on disk

Constraints are real: local-only deploys, `projects/<name>/dev/` are
**independent git repos**, no monorepo, no package registry. Therefore **no
submodules, no `pip install -e`, no cross-repo path dependencies.**

```
accelerators/                          # peer of templates/, governed via /admin-panel
  CATALOGUE.md                         # compact index: name, version, status,
                                       # gate relevance, known consumers, purpose
  ADMISSION.md                         # H1–H10
  <name>/
    ACCELERATOR.md                     # H1 contract, H2 config table,
                                       # H6 provenance, H10 consumers, adoption steps
    VERSION                            # semver
    CHANGELOG.md
    src/                               # the vendorable payload
    tests/run.sh                       # H4, platform exit codes
    tests/negative_controls/           # H5 where applicable
    kb-seed/                           # optional SECURITY_KB / ARCHITECTURE_KB fragments
```

`CATALOGUE.md` stays a **compact index**. It is read at every Architecture gate
on every project forever, so its size is a recurring token cost; letting it grow
long would invert the stated motivation. Full `ACCELERATOR.md` files are read
only for the shortlist.

### Distribution: vendoring by copy, with a provenance stamp

Not a compromise — it is what demonstrably already works here (`llm.py`
byte-identical across four repos for a month). The one thing copy-distribution
lacks is a way to notice divergence, and that is exactly what failed with the
`max_tokens` fix. So the mechanism is **copy plus the missing half**.

```
# VENDORED from accelerators/auth-core@1.2.0 on 2026-08-08.
# Local edits are permitted and expected. If you fix a defect here,
# report it upstream — see accelerators/auth-core/ACCELERATOR.md.
```

Provenance is recorded in an `## Accelerators` section of
`projects/<name>/PROJECT_CONTEXT.md` — name, version, vendored date, sha256 at
vendor time, and the reuse/adapt/build-new reason. That file sits at project
root, **outside `dev/`**, so it survives `dev/` being an independent repo and is
readable by every gate without cloning anything.

**Why not a shared install or a git submodule** — recorded so it is not
re-litigated: both create a cross-repo coupling this platform has deliberately
never had, both make `dev/` non-self-contained, and both would break
`deploy-agent`'s local-only model and `release-manager`'s `dev/`→`prod/`
promotion. Copy-in keeps every project exactly as independent as it is today and
pays for it with a **drift report** rather than with coupling.

`mas-architect` reached the same conclusion independently, noting that the
absence of a registry structurally immunises this platform against the
distributed-monolith failure mode — **a feature to preserve, not a limitation to
fix later.**

---

## Governance

### No new agent

A proposed `accelerator-curator` / `platform-librarian` fails all four of the
platform's own bars: **no distinct gate** (consumption is Architecture,
production is at `/cut-release`); **no distinct per-project KB**
(`accelerators/CATALOGUE.md` is a platform file, and platform SSOT files are
written by `mas-registrar` or `mas-release-manager` by established precedent);
**no distinct test suite** (an accelerator's tests are copied into the consuming
project and run inside whichever existing suite they belong to — a 7th
`accelerator` slug would be duplication, not coverage); **heavy overlap** with
`solution-architect`, `mas-registrar` and `mas-release-manager`.

A new gate is likewise rejected — the platform has already rejected exactly that
twice (`pipeline-marshal` for circularity, feature-flags for ceremony without a
proven trigger).

### Ownership splits by verb

"No new agent" must not be heard as "no accountability".

| Verb | Owner |
|---|---|
| Consult before designing new | `solution-architect` |
| Nominate for harvest | `solution-architect` |
| **Approve promotion into the catalogue** | **the human** |
| Write the catalogue row + place the files | `mas-registrar` |
| Version / deprecate / CHANGELOG | `mas-release-manager` |
| Copy an accelerator into a project | `code-agent` |
| Audit `CATALOGUE.md` against disk | `mas-architect` |

### Contract changes

⚠ = high blast radius. Every change is **additive**; none moves a gate, changes
any agent's core-vs-optional status, changes KB or test-suite ownership, or
**widens a tool grant** — so the 2026-07-26 standing rule on disclosing tool-grant
widenings is not triggered.

| Agent | Change | Bump |
|---|---|---|
| `solution-architect` ⚠ | Mandatory catalogue consultation + Reuse Decision Table; Impact Analysis gains an accelerator row; architecture suite gains provenance + drift scenarios | 2.0.0 → **2.1.0** MINOR |
| `code-agent` ⚠ core 7 | Copy **verbatim**; copy the accelerator's **tests**, not just its source; record slug/version/date; **record any local divergence** in `PROJECT_CONTEXT.md` | 1.3.0 → **1.4.0** MINOR |
| `mas-registrar` ⚠ platform core | Write scope gains `accelerators/**` | MINOR |
| `mas-release-manager` ⚠ platform core | Gains accelerator versioning, deprecation, CHANGELOG | MINOR |
| `release-manager` | The non-blocking harvest question at `/cut-release`; a `none` is recorded | MINOR |
| `mas-architect` | Drift audit extended to `CATALOGUE.md` vs disk (`MISSING ON DISK` / `ORPHAN`) | 1.1.1 → **1.2.0** MINOR |

**Confirmed unchanged**: `verification-agent` (deliberately — its hard
read-only, no-`Bash`, no-re-reasoning design is load-bearing, and this proposal
needs nothing from it), `test-agent`, `plan-agent` (choosing accelerators at
Plan would pre-empt the Architecture gate), `review-agent`, `ui-ux-designer`,
`security-architect` contract (it is *consulted* under H9, its contract is
untouched), `enhance-agent` (its mini pipeline already invokes
`solution-architect` at Architecture, so the duty applies automatically —
skill-line only), and `templates/`.

### `solution-architect`'s new duty — the exact shape

Permitted decisions are exactly **reuse / adapt / build-new**, one row per
catalogue entry, in a Reuse Decision Table in `knowledge/ARCHITECTURE_KB.md`.
**"Not considered" is not a permitted value** — an unlisted catalogue entry is
an unanswered question, in exactly the way an unlisted surface is. A
`build-new` with no reason blocks the gate on the same authority as an
unjustified "unaffected" surface.

**Consultation is mandatory; reuse is not.** This is a deliberate divergence
from the human's phrasing *"reuse them as much as possible"*, and both reviews
independently recommended it: the golden-path literature is explicit that a
paved road is recommended and never required, and a reuse **mandate** is a
well-documented way to produce worse designs. Forcing a component into a design
it does not suit is worse than writing the right thing fresh.

**Reuse never lowers the evidence bar.** This is the rule that stops the
catalogue becoming a verification bypass. "Hardened" describes evidence produced
in the *source* project and **does not transfer**. Every acceptance criterion
touching accelerator-derived code is still written by `functional-design-agent`,
still carries a stable ID, and still must map to a named, executed, passing
check **in this project** at Verification. *"Covered upstream by the
accelerator"* is never an answer to `NOT VERIFIED`.

**If the catalogue is stale or wrong**: read the entry's `CHANGELOG.md` and
consumers list before adopting; an entry that cannot be evaluated (no manifest,
no tests, unclear interface) is one you do **not** adopt; report catalogue
defects by slug and version — `solution-architect` holds no write access to
`accelerators/` and must never fix one in place.

---

## Two-axes carve-out (governance flag — not pedantry)

`CLAUDE.md` currently states platform governance "Never reachable from project
commands; never touches `projects/`." **Harvesting reads `projects/` and writes
to a platform directory.** This is the first artefact in the system that
legitimately crosses the two axes.

The sentence must be **amended explicitly**, not quietly reinterpreted. This
platform's documented failure mode is rules that exist and are not followed; a
silently-reinterpreted rule is the same disease.

---

## What was deliberately NOT done

1. **Palettes not unified** — four products, four correct identities.
2. **No single RAG framework** spanning PLA and RCA — architecturally
   incompatible; the layering exists to avoid an interface satisfying neither.
3. **CFS's `components.py` not extracted** — 1,823 lines encoding CFS product
   law (no bulk-action component exists *so that a test can assert its absence
   over this module's source*). Correct there, wrong everywhere else. The
   `html.py` kernel is extracted; the components are not.
4. **No domain layers** — CFS's detectors, RCA's acquisition/claims, LM's
   milestones/ages. One project each; they are the products.
5. **`chat_sessions.py` not extracted as code** — its value is a *shape*
   ("narrow single-purpose methods, no ad hoc SQL in routes"). `sessions.py` and
   `security_tokens.py` both copied the shape, not the code, and that was right.
   Document the idiom, ship no package.
6. **A8 rule registry deferred** — the best design of its kind in the portfolio,
   with exactly one consumer. SA flags this as its most likely-to-be-wrong call:
   if the next project is another assurance product, it jumps above the line.
7. **A10 kept out of the catalogue** — `pipeline-state.json` is *platform*
   infrastructure and overlaps the deferred `admin/PIPELINE.yaml` item. Two
   homes for one platform contract is the exact drift
   `conclave-dashboard/dev/app/state.py`'s own header warns about.
8. **The multi-surface question stays open** — A14/C6 helps; it does not resolve
   whether a project should declare a surface inventory. Remains
   `mas-architect`'s.

---

## Known gaps and unverified claims — stated, not papered over

- **Nothing was executed.** Both reviews were read-only; no suite was run and no
  claim about tests passing has been confirmed.
- **Token savings are inferred, not measured.** There is **no measurement
  anywhere of what reuse saves**, because nothing has been reused yet. All
  figures are order-of-magnitude. `usage-monitor` should record actual pre/post
  figures on the first project that adopts an accelerator — that one data point
  would be worth more than the whole estimate column. Recording the
  pre-accelerator `USAGE_INDEX.md` baseline **now** is what makes the stated
  motivation falsifiable later.
- **A catalogue also *adds* tokens** — `solution-architect` reads `CATALOGUE.md`
  at every Architecture gate forever. This is why the index stays compact.
- **Files inferred rather than opened in full**: CFS `test_ui_tokens.py`
  (relied on `tokens.py`'s own references to it — worth confirming before
  extracting A3); CFS `app/ui/pages.py` (4,643 lines) and `state.py` (2,576) at
  header level only; ~90 `design-review/` mockups sampled, not exhaustively read.
- **`prod/` trees untouched**, per `solution-architect`'s standing constraint.
- **No automated detection of divergence between the catalogue and copies**
  beyond the approved sha256 drift check — the `Consumers` field plus a
  human-initiated sweep is the rest of the mechanism, and that is honest and
  cheap.

---

## Housekeeping surfaced by `mas-architect`'s pre-flight audit

The contract-drift audit came back **21/21 MATCH** — no drift, no missing, no
orphan. Two documentation-freshness findings, not blocking:

1. `admin/ROADMAP.md` still lists `admin/PIPELINE.yaml` + `PIPELINE_LOG.md` as
   **deferred backlog**, but `admin/PIPELINE.md`, `PIPELINE.yaml` and
   `PIPELINE_LOG.md` all exist on disk, and `PIPELINE.md` declares itself the
   source of truth for the pipeline's shape. The roadmap is describing a world
   that ended. `mas-release-manager`'s to fix.
2. `CLAUDE.md`'s directory map does not mention `admin/PIPELINE.md` at all,
   though it is now an SSOT file.

---

## Build sequence

1. `mas-registrar` — scaffold `accelerators/` (`CATALOGUE.md`, `ADMISSION.md`),
   apply the six contract changes, update `admin/MAS_REGISTRY.md`.
2. Orchestrator/human — `CLAUDE.md` directory map + the two-axes carve-out.
3. `mas-release-manager` — the `ROADMAP.md` entry, plus housekeeping fix (1).
4. **A4 first** — it defines the suite convention every other entry needs.
5. Then A5 → A3 → A2 → A1 (A1 last: largest, and gated on
   `security-architect`'s rulings under H9).
6. The two free-win defect fixes, at any point — they are independent.

**MVP-1 is proven when** the next real project's Architecture gate produces a
genuine Reuse Decision Table against the catalogue — adopting or
rejecting-with-reason — and the decision survives into `ARCHITECTURE_KB.md`.
Not when the directory exists.

---

## Approval record

| Item | Decision | Date |
|---|---|---|
| A1 Auth & session core | **Approved** | 2026-08-08 |
| A2 Grounded-answer kernel | **Approved** | 2026-08-08 |
| A3 Conclave design system | **Approved** | 2026-08-08 |
| A4 Test-suite scaffold & harnesses | **Approved** | 2026-08-08 |
| A5 Structural conformance kit | **Approved** | 2026-08-08 |
| Drift check from day one | **Approved** | 2026-08-08 |
| Harvest prompt at `/cut-release` | **Approved** | 2026-08-08 |
| Two free-win defect fixes | **Approved** | 2026-08-08 |
| Rule-of-three promotion bar | **Rejected** — overridden by the human's scope correction; built once, well, is enough | 2026-08-08 |
