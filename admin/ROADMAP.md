# MAS Platform Roadmap

Prioritized, dependency-ordered backlog for the MAS platform itself — distinct
from any individual project's feature backlog (see `projects/<name>/FEATURES.md`
for that). Populated by `mas-architect`'s Founding Review, approved 2026-07-05,
groomed afterward via `/admin-panel roadmap`.

## MVP Scope (approved for v1)

Ordered so nothing depends on something listed after it. Each item is built
one at a time via `/admin-panel add-agent`, even though the whole set was
approved together.

1. ~~**Templates** — `genai-chatbot`, `agentic-workflow`, `rag-knowledge-base` scaffolds.~~ **Shipped** (Phases 1, 3).
2. ~~**Core pipeline agents, in gate order** — `plan-agent` → `code-agent` → `test-agent` → `review-agent` → `deploy-agent`.~~ **Shipped** (Phase 1).
3. ~~**`/new-project` skill** — orchestrates Intake → Team Composition → Plan & Backlog → Experience Design (UI-bearing only) → Architecture → Code → Test → Review → Deploy.~~ **Shipped**, full gate order (Phase 4).
4. ~~**ui-ux-designer** — non-droppable for UI-bearing templates.~~ **Shipped** (Phase 4).
5. ~~**solution-architect + security-architect** — joint Architecture gate.~~ **Shipped** (Phase 4).
6. ~~**functional-agent + industry-expert** — Intake/Plan & Backlog/Architecture SMEs.~~ **Shipped** (Phase 4).
7. ~~**enhance-agent + `/enhance-project` + `/modify-feature`** — reuses every agent above; enhance-agent owns both skills.~~ **Shipped** (Phase 5).
8. ~~**release-manager (project-level) + `/cut-release`** — conflict *detection* and dev→prod promotion via git-remote-merge are in MVP; automated conflict *resolution* is deferred (see Backlog).~~ **Shipped** (Phase 6).
9. ~~**usage-monitor — tracking, estimation, and soft-budget warnings only.** Auto-pause/resume is deferred (see Backlog).~~ **Shipped** (Phase 7).
10. ~~**`/consult` skill** — thin router to any agent + its KB; depends on the full roster existing.~~ **Shipped** (Phase 8). **Original MVP scope (items 1-10) is now 100% complete.**

## Accelerator layer (`accelerators/`) — approved 2026-08-08, in build

**Authority**: `admin/proposals/2026-08-08-accelerator-layer.md`, approved
item-by-item by the human via checkbox on 2026-08-08 — full MVP-1 scope (A1–A5)
plus all four open items. Reviews by `solution-architect` (technical inventory)
and `mas-architect` (platform governance), run in parallel the same day.
`mas-architect`'s contract-drift pre-flight audit came back **21/21 MATCH** — no
drift, no missing, no orphan.

**Paths named below under `accelerators/` do not exist on disk as of this entry
(2026-08-08).** They are the approved target shape, written by `mas-registrar`;
treat every `accelerators/…` path here as planned, not as a live cross-reference.

### The scope correction that governs this item

The human issued a mid-review scope correction that **overrides**
`mas-architect`'s recommended promotion bar, and it is the single thing to carry
forward correctly:

> The qualifying test is *"is this a strong, well-built component a future
> project would want?"* — **not** *"has it been built twice?"*

The proposed **rule of three / one-accelerator MVP was REJECTED**. Cross-project
duplication is explicitly **not** the bar. A component **built once, well,
qualifies.** Approved MVP-1 is therefore **five** accelerators, not one. Any
future grooming pass that finds a "rule of three" framing anywhere in this
platform's documents should treat it as stale and route the correction through
`mas-architect`.

### The problem, with its on-disk evidence

Each fact was verified against the repository on 2026-08-08, not inferred.

1. **Half the portfolio abandoned the templates.** Four of eight projects record
   `template: custom` in their own `pipeline-state.json`: `conclave-dashboard`,
   `conclave-finance-studio`, `conclave-marketing`, `rate-case-analyzer`. The
   three scaffolds under `templates/` are too thin to carry a real project.
2. **Copy-paste distribution already works here — and it already leaked a real
   fix.** `app/llm.py` is **byte-identical** (md5 `631bff3e…`) in four places:
   `templates/genai-chatbot`, `templates/agentic-workflow`,
   `projects/grid-assistant/dev/backend`, `projects/load-alert-agent/dev/backend`.
   But `projects/little-milestones/dev/backend/app/llm.py` diverged with a
   **red-team-discovered fix** — `max_tokens=4096`, because the 1024 default
   truncated answers mid-sentence — and **that fix never went back upstream**.
   Every future chatbot project still inherits the broken default. This one fact
   is the entire argument for drift *reporting*, and is why the drift check was
   approved for MVP-1 rather than deferred.
3. **The template mechanism structurally cannot express cross-template reuse.**
   `tests/suites/harness/browser.py` (138 lines) is byte-identical in **five**
   locations — all three templates plus `conclave-marketing` and
   `little-milestones`. **Three of those copies are *inside* `templates/`.** The
   template mechanism's own answer to "this is shared across templates" is to
   paste it three times.
4. **The cost being paid is re-derivation, not typing.**
   `rate-case-analyzer`'s `app/grounding/verify.py` opens by naming its lineage
   from `policy-lookup-assistant` and the one signature it changed — a
   re-derivation paid at **full Architecture-gate cost** (65k–132k tokens per
   gate). Savings are counted in *fractions of a gate not re-derived*, never in
   lines not typed.

### The mechanism

- **A new top-level `accelerators/` directory, sibling to `templates/`**,
  governed via `/admin-panel` — not a subdirectory of `templates/`, because the
  duplication is *across* templates.
- **`accelerators/CATALOGUE.md`** — a deliberately **compact index** (name,
  version, status, gate relevance, known consumers, purpose). It is read at every
  Architecture gate on every project forever, so its size is a recurring token
  cost; letting it grow long would invert the stated motivation. Full
  `accelerators/<name>/ACCELERATOR.md` files are opened only for the shortlist.
- **`accelerators/ADMISSION.md`** — admission criteria H1–H10; all must hold.
  `solution-architect` + `security-architect` jointly approve admission;
  `mas-architect` reviews any catalogue-*shape* change.
- Per entry: `ACCELERATOR.md`, `VERSION` (semver), `CHANGELOG.md`, `src/`,
  `tests/run.sh` in the platform exit-code convention,
  `tests/negative_controls/` where applicable, optional `kb-seed/`.
- **Distribution is vendoring by copy, with a provenance stamp.** No submodules,
  no `pip install -e`, no cross-repo path dependencies — `projects/<name>/dev/`
  are independent git repos, deploys are local-only, there is no registry. Copy-in
  keeps every project exactly as independent as it is today. Provenance
  (slug, version, vendored date, sha256 at vendor time, and the
  reuse/adapt/build-new reason) is recorded in an `## Accelerators` section of
  `projects/<name>/PROJECT_CONTEXT.md` — at project root, *outside* `dev/`, so it
  survives `dev/` being a separate repo and is readable by every gate.
- **A sha256 drift report that reports and never auto-syncs**, producing
  *clean* / *local divergence* / *upstream ahead*, living in
  `solution-architect`'s architecture suite. Copy-distribution's one missing half
  is noticing divergence; that is precisely what failed with `max_tokens`.
  Auto-sync is explicitly out — the local edit may be the right one.
- `mas-architect` noted independently that the absence of a package registry
  structurally immunises this platform against the distributed-monolith failure
  mode — **a property to preserve, not a limitation to fix later.**

### Governance

- **No new agent.** A proposed `accelerator-curator` / `platform-librarian`
  failed **all four** of the platform's own bars: no distinct gate (consumption
  is Architecture; production is at `/cut-release`); no distinct per-project KB
  (`CATALOGUE.md` is a platform file, and platform SSOT files are written by
  `mas-registrar` or `mas-release-manager` by established precedent); no distinct
  test suite (an accelerator's tests are copied into the consuming project and
  run inside whichever existing suite they belong to); heavy overlap with
  `solution-architect`, `mas-registrar` and `mas-release-manager`. A new **gate**
  was likewise rejected — the platform has already rejected exactly that twice
  (`pipeline-marshal` for circularity; feature flags for ceremony without a
  proven trigger).
- **"No new agent" is not "no accountability" — ownership splits by verb**:
  consult-before-designing-new and nominate-for-harvest → `solution-architect`;
  **approve promotion into the catalogue → the human**; write the catalogue row
  and place the files → `mas-registrar`; version / deprecate / CHANGELOG →
  `mas-release-manager`; copy an accelerator into a project → `code-agent`; audit
  `CATALOGUE.md` against disk → `mas-architect`.
- **Consultation is mandatory; reuse is never mandated.** A deliberate divergence
  from the human's phrasing *"reuse them as much as possible"*, recommended
  independently by both reviews: a paved road is recommended and never required,
  and a reuse mandate is a well-documented way to produce worse designs.
  `solution-architect` produces a **Reuse Decision Table** in
  `knowledge/ARCHITECTURE_KB.md`, one row per catalogue entry, values exactly
  **reuse / adapt / build-new**. **"Not considered" is not a permitted value**;
  a `build-new` with no reason blocks the Architecture gate on the same authority
  as an unjustified "unaffected" surface.
- **Reuse never lowers the evidence bar.** This is the rule that stops the
  catalogue becoming a verification bypass. "Hardened" describes evidence produced
  in the *source* project and **does not transfer**. Every acceptance criterion
  touching accelerator-derived code is still written by `functional-design-agent`,
  still carries a stable ID, and still must map to a named, executed, passing
  check **in this project** at Verification. *"Covered upstream by the
  accelerator"* is never an answer to `NOT VERIFIED`.
- `solution-architect` holds **no write access** to `accelerators/` and must
  never fix a catalogue defect in place — it reports by slug and version. An
  entry that cannot be evaluated (no manifest, no tests, unclear interface) is
  one you do **not** adopt.
- **Two-axes carve-out.** Harvesting reads `projects/` and writes to a platform
  directory — the first artefact in the system that legitimately crosses the two
  axes. `CLAUDE.md`'s "never touches `projects/`" sentence must be **amended
  explicitly**, not quietly reinterpreted (orchestrator/human own that edit).

### Approved MVP-1 — five accelerators

Listed in **build order, which is not rank order**.

1. **A4 · Test-suite scaffold & harnesses** — *built first*, because it defines
   the runnable-suite exit-code convention (H4) that every other entry depends
   on: `0` pass, `1` fail, `3` no scenarios defined (**an empty suite is not a
   passing suite**), `4` cannot execute → STATIC-ONLY. This convention is what
   makes the platform's whole `STATIC ONLY — NOT EXECUTED` policy work. Source:
   3 templates + `conclave-marketing` + `little-milestones` + CFS; byte-identical
   in 5 places. Extraction trivial. Est. ~40–70k/project.
2. **A5 · Structural conformance kit** — the direct answer to `LESSONS.md`'s
   "always run a negative control before trusting a new guard." Source:
   `rate-case-analyzer` + CFS; 8 negative-control fixture trees; both pieces were
   written *after* a guard failed. Extraction low. Est. ~50–100k. Also the tool
   H3 points at itself: host-decoupling is *proven* by running A5's closure
   checker against each accelerator — the catalogue eats its own dog food.
3. **A3 · Conclave design system + journey-map method** — extract the **token
   schema** (independently re-derived **four** times across CFS, RCA, dashboard,
   marketing), mandatory light/dark via `[data-theme]`, the
   `tabular-nums lining-nums` law, and the `design-review/` static-HTML mockup
   convention (6 projects, no build step, no network, openable from the
   filesystem — which is what serves the human's standing
   rendered-preview-before-approval rule). **Do NOT unify the palette values** —
   marketing's teal/gold, CFS's no-green risk ramp, RCA's navy/position-gold and
   LM's terracotta/sage are each correct for their product; forcing one palette
   would make every product look like the marketing site, a worse outcome than
   duplication. Ship instead a **checklist of semantic laws to choose from**,
   each tagged with the project that earned it and the defect it prevents (CFS:
   "there is no green", enforced at import time by `assert_no_green()` — a green
   token is an `ImportError`, not a review comment; RCA: refusal is never styled
   as an error; LM: gold is decorative-only). **On journey maps the deliverable
   is the timing rule, not the artefact**: they exist as a designed artefact in
   exactly one project, produced *after* MVP1 was complete, and `UX_KB` §A2.4
   records that two of four journeys were unwalkable and one unstartable in a
   shipped product that had already passed gate 5. The rule: *journey maps are
   produced at Experience Design, before Architecture, and a journey that cannot
   be walked end-to-end in the mockups is a gate-5 blocker.* Extraction
   low-moderate. Est. ~80–150k/project.
4. **A2 · Grounded-answer kernel (RAG), four independently adoptable layers** —
   **merge, don't pick.** **L0 Contract** (~1 page: "refusal is a structured
   signal, not prose"; "`sources[]` is built by the application from what was
   verified, never parsed from model output"; "a refusal names the gap";
   "silence is not clearance") — *this layer alone would have saved most of RCA's
   re-derivation.* **L1 Kernel** (~150 LOC, zero deps) — `sentinel.py`
   **verbatim** from RCA; its zero-import, no-regex, no-substring closure is the
   whole point and must not be diluted; typed refusal kinds; the one-parameter
   `build_sources()` signature so retrieval hits can never masquerade as support.
   **L2 Retrieval** (~250 LOC) — `EvidenceSource` protocol; `hash_embed`
   unmodified (deterministic, stdlib+numpy, **no API key** — which is why RCA's
   suites are runnable and PLA's are not); a Chroma-backed adapter. **L3
   Assurance** (~400 LOC) — RCA's `CoverageLedger`/`Coverage` (no public
   constructor; obtainable only via `seal()`, which raises unless
   `included + excluded + unassessable == candidates_considered`), `verify()` as
   a pure function, CFS's abstention vocabulary. **Do not build one framework
   both PLA and RCA could have been built on** — they are architecturally
   incompatible (LangChain/Chroma `similarity_search` vs. a hand-rolled protocol
   over three SQLite stores behind an import-boundary wall). The layering exists
   so the *contract* is shared where it truly is common and the *implementations*
   need not be. Requires **responsible-AI co-sign** (H9). Extraction moderate.
   Est. ~100–200k/project.
5. **A1 · Auth & session core (+ mobile token store)** — *built last*: largest,
   and gated on `security-architect`'s H9 rulings. Source: `little-milestones`;
   ~1,976 LOC product, ~1,455 LOC / 58+ tests, three `SECURITY_KB.md` sections,
   survived every gate plus a dedicated hardening increment (F12) and a mobile
   increment (F18). The value is the **decisions worth never re-deriving**:
   argon2id (not bcrypt — greenfield, no legacy constraint); session tokens
   stored SHA-256-hashed **deliberately not** under a slow KDF; the `Secure`
   cookie flag set *conditionally*, because browsers silently drop `Secure`
   cookies over local plain HTTP; 30-day sliding expiry **capped by** a 90-day
   absolute via `min()`; `DUMMY_PASSWORD_HASH` verified against unknown emails so
   timing profiles match (same-*cost*, not merely same-message); rate limiting as
   a **sliding timestamp list**, explicitly not a clock-aligned fixed window, so
   a boundary burst cannot double the limit; 5 failed TOTP attempts destroy the
   pending session, named in-contract as the primary brute-force control; one
   active reset token enforced **in the same call as the insert**, so there is
   never a two-live-token window; on mobile the cookie is **suppressed entirely**,
   because the platform cookie jar is unencrypted and inside the backup set.
   **Blocking hardening gaps, owned by `security-architect`**: (1) persistence
   coupling is the real blocker — every function takes `sqlite3.Connection` and
   issues literal SQL; SA leans to shipping SQLite-only and saying so, flagged as
   a design call it does not own; (2) two module-global dicts (`_RATE_BUCKETS`,
   `_TOTP_FAILURE_COUNTS`) are per-process — correct for single-process local
   deploys, **silently wrong under any multi-worker deploy**; must become a
   documented precondition with a named revisit trigger; (3)
   `PHOTO_ENCRYPTION_KEY` is deliberately reused for TOTP secrets — rename to
   `APP_ENCRYPTION_KEY`, and the key-reuse decision must be **re-blessed per
   adopting project**, never inherited silently; (4) no password-strength policy
   or breach-list check; (5) `chat_sessions.py` is a chat concern, not an auth
   concern — split at extraction. **Open questions routed to
   `security-architect`**: is vendored-by-copy auth an acceptable posture at all,
   given a CVE-class fix needs manual propagation? Is the conformance test pack a
   floor or a ceiling for an adopting project's security suite? Should
   `SECURITY_KB` §1/§7/§9 ship as a seed, at the risk of a security KB that reads
   as inherited rather than decided? Requires **security co-sign**
   unconditionally (H9). Extraction moderate. Est. ~200–350k/project.

**Also approved with MVP-1**: the drift check from day one (above); a
**non-blocking harvest prompt at `/cut-release`** — one question after the
promotion approval, *"anything worth harvesting? [none] / [nominate: …]"*, where
a `none` is **recorded** so it is visible that it was asked, and which never
blocks a release (human-initiated harvesting via `/admin-panel` stays available
at any time); and **two free-win defect fixes**, independent of the catalogue and
buildable at any point — (a) propagate `max_tokens=4096` into the three template
`llm.py` copies, and (b) fold `policy-lookup-assistant`'s four unpropagated
hardening deltas into `templates/rag-knowledge-base/` (the `manifest.json`
requirement, `_extract_text()` normalisation of LangChain's
`str | list[block]` content, scoped CORS via `FRONTEND_ORIGIN`, and input
validation).

### What "MVP-1 is proven" means

**MVP-1 is proven when the next real project's Architecture gate produces a
genuine Reuse Decision Table against the catalogue — adopting, or
rejecting-with-reason — and that decision survives into its
`knowledge/ARCHITECTURE_KB.md`.**

It is **not** proven when the `accelerators/` directory exists, nor when five
entries are written, nor when their suites pass. A catalogue nobody consulted is
indistinguishable from no catalogue, and this is the specific way this item can
fail quietly.

### Pre-accelerator token baseline — recorded 2026-08-08, so the motivation is falsifiable

The stated motivation for this whole layer is token saving, and **there is no
measurement anywhere of what reuse saves, because nothing has been reused yet.**
Every figure in the MVP-1 list above is an order-of-magnitude *estimate*. This
baseline is recorded now, before any accelerator exists, so a later claim of
savings can be checked rather than asserted.

`memory/USAGE_INDEX.md` as of 2026-08-08, verbatim:

| Project | Team | Gates covered | Agent-call tokens | Last updated |
|---|---|---|---|---|
| grid-assistant | core-only (predates Team Composition) | Plan/Code/Test/Review/Deploy x2 (original + 1 enhancement) | not yet backfilled | — |
| policy-lookup-assistant | full team (all 5 optional SMEs) | Full 9-gate pipeline + multi-suite Test verification + frontend cycle | ~646,833 | 2026-07-09 |
| load-alert-agent | core-only, API-only template | Intake/Plan/Code/Review (Test/Deploy via direct Bash, no agent-call cost) | ~150,297 | 2026-07-09 |

Plus the two figures cited in the proposal but **not** present in that index:
`little-milestones` exceeded **1.6M** tokens, and a single Architecture gate runs
**65k–132k**.

**Honest caveat on this baseline, stated rather than papered over**: the index is
itself **stale and incomplete** — it covers 3 of 8 projects, its newest row is
dated 2026-07-09, one row is un-backfilled, and it predates the 9→11 gate change,
so its per-project totals are not comparable to anything measured after
2026-07-28. It is therefore a **weak** baseline. Taking it as a strong one would
be exactly the kind of unfalsifiable claim this section exists to prevent.
**Follow-up owed to `usage-monitor`** (recorded here, not yet scheduled): backfill
`USAGE_INDEX.md` across all eight projects against the current 11-gate pipeline,
and record actual pre/post figures on the first project that adopts an
accelerator. That single real data point would be worth more than the entire
estimate column above. Note also that a catalogue **adds** tokens —
`solution-architect` reads `CATALOGUE.md` at every Architecture gate forever —
which is why the index stays compact, and which must be on the *cost* side of any
future saving claim.

### Other known gaps carried forward, not resolved

- **Nothing was executed.** Both reviews were read-only; no suite was run, and no
  claim about tests passing has been confirmed.
- **Files inferred rather than opened in full**: CFS `test_ui_tokens.py` (relied
  on `tokens.py`'s own references to it — **worth confirming before extracting
  A3**); CFS `app/ui/pages.py` (4,643 lines) and `state.py` (2,576) at header
  level only; ~90 `design-review/` mockups sampled, not exhaustively read.
- **`prod/` trees untouched**, per `solution-architect`'s standing constraint.
- **No automated detection of divergence beyond the approved sha256 drift
  check** — the `Consumers` field plus a human-initiated sweep is the rest of the
  mechanism, and that is honest and cheap.
- **Deliberately NOT done** (recorded so it is not re-litigated): palettes not
  unified; no single RAG framework spanning PLA and RCA; CFS's `components.py`
  (1,823 lines) **not** extracted — it encodes CFS product law, e.g. no
  bulk-action component exists *so that a test can assert its absence over that
  module's source*, correct there and wrong everywhere else (the `html.py` kernel
  is extracted, the components are not); no domain layers (CFS detectors, RCA
  acquisition/claims, LM milestones/ages — one consumer each; they *are* the
  products); `chat_sessions.py` not extracted as code, since its value is a
  *shape* ("narrow single-purpose methods, no ad hoc SQL in routes") that
  `sessions.py` and `security_tokens.py` both copied correctly — document the
  idiom, ship no package.

### Deferred from the accelerator round — each with its build trigger

Nothing here is rejected. Each names what must happen before it is built.

- **A6 — server-rendered HTML kernel.** *Trigger*: a second project chooses the
  server-rendered-HTML shape.
- **A7 — abstention / coverage vocabulary.** *Trigger*: none needed separately —
  **it ships inside A2-L3.** Deferred as a standalone entry only.
- **A8 — rule registry.** SA's assessment: the best design of its kind in the
  portfolio — and it has **exactly one consumer**, so it is too early. Documented
  as a pattern now; **promote the moment a second project needs it.** *Trigger*:
  a second consumer. SA flags this as **its own most-likely-to-be-wrong call** —
  if the next project is another assurance product, this jumps above the line.
- **A9 — config single-reader.** *Trigger*: a third project re-derives the same
  single-reader config discipline.
- **A10 — `pipeline-state.json` contract.** **Platform infrastructure, not a
  project accelerator**, and it **overlaps the `admin/PIPELINE.yaml` item above**
  (now shipped). Two homes for one platform contract is the exact drift
  `conclave-dashboard/dev/app/state.py`'s own header warns about. *Trigger*:
  **route via `mas-architect`** — a platform-shape question, resolved against
  `PIPELINE.yaml` as the existing home, not by opening a second one in
  `accelerators/`.
- **A11 — prompt-fragment library.** *Trigger*: a second project needs the same
  fragment, or a prompt defect propagates the way `max_tokens` did.
- **A12 — canonical JSON.** *Trigger*: a second consumer, or a defect traced to
  inconsistent JSON canonicalisation.
- **A13 — rendered-numbers assertion.** *Trigger*: none needed separately —
  **it ships inside A4.**
- **A14 — cross-surface parity suites.** **This is the already-deferred C6**
  (see the 2026-07-28 list below) — one item, two names; do not build it twice.
  *Trigger*: C6's own — pairs naturally with C3 and with the open multi-surface
  structural question, which remains `mas-architect`'s.
- **Security re-scan of copied accelerators.** *Trigger*: **the first time an
  accelerator needs a security fix after having been copied into a project.**
  That is the moment the "manual propagation of a CVE-class fix" risk stops being
  hypothetical, and it is the right moment to design the sweep — not before.
- **UI / design-token accelerators beyond A3's scope.** A3 ships the token
  *schema* and the semantic *laws* only. Component libraries, themed primitives
  and any shared UI implementation are out. *Trigger*: a project needing shared
  UI *implementation* rather than shared vocabulary — and note this must not
  quietly become palette unification, which was explicitly ruled out.
- **Token-saving measurement.** Baseline recorded above; the measurement itself
  is deferred. *Trigger*: the first project to actually adopt an accelerator —
  `usage-monitor` records real pre/post figures at that point.

## Backlog (post-MVP)

- ~~**`deliverables-agent`**~~ **Shipped (2026-07-09).** On-demand PPTX/DOCX/XLSX export generated one-way FROM `knowledge/*_KB.md`/`PLAN.md`/`test-evidence/` — markdown stays the source of truth every other agent reads, hard rule enforced: no agent ever reads from `deliverables/`. **Verified for real**: confirmed `python-pptx`/`python-docx`/`openpyxl` actually install and work in this environment, then generated genuine `architecture.pptx` (6 slides), `design.docx` (252 paragraphs, 13 headings mirroring PLAN.md's real structure), and `test-results.xlsx` (10 rows across all 3 real test-evidence files) for `policy-lookup-assistant` — each file re-opened and validated with its own library after writing, not just written-and-assumed-correct. **Remaining, not yet built**: the Excel rollups of `admin/ROADMAP.md` and each project's `FEATURES.md`, and wiring the already-shipped standalone HTML knowledge-base page's regeneration into this agent's trigger mechanism (it currently requires a manual refresh).
  - ~~**Added scope note (2026-07-09)**: a fourth export target — an **interactive HTML knowledge-base page**~~ **Shipped standalone (2026-07-09)**, decoupled from `deliverables-agent` per human decision (needed none of its Office-export tooling) — see Shipped section below. Original note preserved: documenting the MAS's end-to-end approach (pipeline stages, agent roster, templates, Admin Control Panel) generated FROM `admin/MAS_REGISTRY.md`, `admin/ROADMAP.md`, `.claude/agents/*.md`, and `.claude/skills/*/SKILL.md` — so users can click through to learn the system and see how to structure their own projects. This is `deliverables-agent`'s **first platform-level target** (everything else in its scope is per-project or a per-project rollup) — a real scope widening to call out and re-bless when this agent is actually built, not silently assumed. Regeneration trigger: end of `mas-registrar`'s `add-agent` (registry changes) and end of `mas-release-manager`'s `roadmap`/`release` (roadmap/CHANGELOG changes) — same "regenerate at the triggering write" principle as the project-level exports, no new standing service. Ship this after the simpler project-level exports/rollups are built and proven, same "prove the simple case first" sequencing already used elsewhere in this roadmap (usage-monitor tracking before auto-pause/resume; conflict detection before automated resolution).

- **Cloud `target_env` for deploy-agent** — local-only deploy proves the pipeline first; cloud auth/infra-as-code is meaningfully more work and premature before the core loop is validated.
- ~~**usage-monitor auto-pause/resume**~~ **Shipped (2026-07-09)**. Honest design constraint: no tool proactively reports remaining usage budget, so the trigger is always a human signal or a rate-limit-shaped tool error, never automatic detection. On trigger: checkpoint to the natural status file (`admin/CHANGELOG.md` or `PROJECT_CONTEXT.md`), a real one-shot `CronCreate` job for the reset time, resume reads the checkpoint and continues with normal approval gates still applying. **Verified for real**: a genuine 3-minute cron test (scheduled 20:09 CDT for 20:12 CDT) fired exactly on schedule and the resumed session continued autonomously — not simulated. Formalizes what had already been done manually twice earlier in this platform's own build.
- ~~**release-manager automated conflict resolution**~~ **Shipped (2026-07-09).** Design: automated *triage*, never automated *approval* — conflicts are classified as **proximity** (textually conflicting but no actual logical overlap; code-agent proposes a resolution and applies it, but still gets a lightweight single yes/no human confirm on the concrete diff) or **semantic** (genuine overlapping logic; unchanged full deliberative review, same as original MVP). When in doubt, treat as semantic. **Verified for real, not simulated**: deliberately created two genuinely conflicting feature branches on `load-alert-agent` (both append an independent function near the end of the same file), confirmed the real git conflict via an actual merge probe, correctly classified it as proximity, resolved it (kept both functions), ran the real test suite (1/1 pass) plus a manual functional check, and promoted to a real `prod/` (this was actually the project's first release — corrected to a `v1.0.0` baseline, matching `grid-assistant`'s own precedent, after an initial version-numbering assumption error was caught and fixed).
- **Feature flags** — **now designed (2026-07-09, via mas-architect), deliberately still deferred.** Real problem identified: today's only rollback is `git reset --hard` on an entire release train, so a bad feature can only be killed by taking down every feature bundled with it — there's no surgical per-feature kill switch. Rollout-percentage/user-targeting flags don't apply (no traffic-splitting layer for a local single-process deploy) — building those would be pure ceremony. **Recommended mechanism**: extend `release-manager` (not a new agent — no distinct gate/KB/test-suite needed), a `prod/flags.json` store, opt-in per feature (not blanket instrumentation), a toggle action that edits+commits+logs, `code-agent` wiring a guard around a flaggable feature's entry point, `deploy-agent` handling the required restart. `FEATURES.md`'s Released section gets an optional flag-state annotation sourced from `flags.json`, never a second source of truth. **Deferred deliberately**: no release has ever actually needed partial rollback — building this now would be guessing at the design's edges rather than learning them from a real failure, following the same "prove the simple case insufficient first" discipline applied to auto-pause/resume and automated conflict resolution. Build the first time a real release needs it.
- ~~**Multi-suite Test-gate override policy**~~ **Shipped (2026-07-09)**, despite no suite ever actually having blocked something the human wanted to ship — human chose to build it now rather than wait for a trigger. Design: every suite defaults to blocking (formalizing what was already implicit — the human could always approve past a failure). A project can mark specific suites **advisory** via a recorded `Test Policy` line in `PROJECT_CONTEXT.md`'s Active Team section, human decision only, reversible anytime. Advisory failures are still fully reported, just don't force a gate stop; blocking failures still stop the gate and require either a fix or an explicit `[override]`-tagged reason in the Decisions Log. Wired into `test-agent.md`, `/new-project`'s Team Composition and Test steps, and `/enhance-project`'s Test step (respects the project's existing policy unless amended). **Verified for real**: applied retroactively to `policy-lookup-assistant` (marked UX/accessibility advisory, reasoned from its own internal-tool-first framing), re-ran its real blocking suites (5/5 pass), and confirmed the report format correctly separates Blocking from Advisory without conflating them.

- ~~**`synthetic-data-agent`**~~ **Shipped (2026-07-12).** Proposed
  2026-07-11 (human request, during little-milestones' manual tester-account
  setup — a real, concrete need: a populated profile with
  memories/photos/timeline/digest content was needed to exercise every
  feature, and no agent generated that at the time). `mas-architect`
  advisory review recommended it as a good future-roadmap candidate; human
  approved it for build via checkbox backlog review on 2026-07-12. Built
  exactly per the advisory design: cross-cutting, invoked just before the
  Test gate (and on-demand for QA/demo prep) — not a new pipeline gate;
  optional/droppable at Team Composition, default-on for `genai-chatbot`/
  `rag-knowledge-base`, default-off for `agentic-workflow`; owns
  `knowledge/TEST_DATA_KB.md` (data model/personas/volume presets, read-only
  sourced from `DOMAIN_KB.md`/`INDUSTRY_KB.md`); owns no test suite
  (test-agent retains sole verification ownership); high/medium/low volume
  control recorded per generation run; Bash scoped strictly to invoking
  code-agent's `scripts/seed-data.sh reset|reload` — no direct infra/DB
  access, code-agent retains ownership of that script, this agent owns
  content generation only; re-engagement on `/enhance-project` only if
  flagged relevant (new data shape introduced), not unconditional. See
  `.claude/agents/synthetic-data-agent.md` and `admin/MAS_REGISTRY.md`.

- **Deferred from the 2026-07-28 verification-gap round** (see
  `admin/proposals/2026-07-28-pipeline-verification-gap.md`; the human's
  decision table selected N1, N2, RNTL, C1, C5, and C2 for immediate build —
  everything below was explicitly *not* selected this round, and none of it is
  rejected):
  - **C3 — rendered-output evidence required per surface named by C2's Impact
    Analysis.** A surface with no rendered evidence would report `NOT VERIFIED`
    and never be folded into a pass. Now genuinely buildable in a way it wasn't
    before: `solution-architect` v2.0.0 produces the surface list, and
    `test-agent` v1.4.0 finally has a native rendering backend to produce
    mobile evidence with. Deferred only for sequencing.
  - **C6 — promote the cross-surface parity suite into the templates**, so
    multi-surface projects get it from day one rather than having it
    hand-written per project (it was written during F18 and exists only there).
    Naturally pairs with C3 and with the multi-surface question below.
    **Same item as `A14` in the accelerator round (2026-08-08) — one item, two
    names. Build it once, here.**
  - ~~**`admin/PIPELINE.yaml` + `admin/PIPELINE_LOG.md`.**~~ **Shipped — no
    longer deferred.** Corrected 2026-08-08 by `mas-release-manager` after
    `mas-architect`'s pre-flight audit for the accelerator-layer proposal flagged
    this entry as stale. Verified on disk that same day: **`admin/PIPELINE.md`,
    `admin/PIPELINE.yaml` and `admin/PIPELINE_LOG.md` all exist.**
    `PIPELINE.yaml` (`version: 1`, `updated: 2026-07-29`) is the machine-readable
    source of truth for gate order, names, owners and skip rules, and states in
    its own header that `PIPELINE.md` §§1–2 are *generated from it* — which is
    exactly the "picture and rule cannot drift" property this item asked for.
    `PIPELINE.md` declares itself **the source of truth for the pipeline's
    shape** (with `MAS_REGISTRY.md` remaining source of truth for *who* each
    agent is, and `.claude/skills/new-project/SKILL.md` the executable form that
    loses any disagreement). `PIPELINE_LOG.md` exists as the platform-feature
    gate log and already carries one closed run (F-P1, the project-tracking
    dashboard, re-routed to `projects/conclave-dashboard/` at gate 2).
    **Still open, tracked here rather than silently closed**: `PIPELINE_LOG.md`
    is currently platform-scope only; the *per-project* half of the original ask
    is partially realised via `projects/<name>/PIPELINE_LOG.md` and
    `pipeline-state.json` but has never been swept for coverage across all eight
    projects, and `PIPELINE_LOG.md`'s own header still flags a standing gap —
    `/admin-panel` has no "build a platform feature" flow. That standing gap is
    the live remainder of this item; the artifacts themselves shipped. Original
    reasoning preserved below.

    The human's feedback
    #5 asked for a strictly-followed workflow with a visual graph.
    `pipeline-marshal` (N3) was correctly rejected for **circularity** — the
    only way it runs is if the orchestrator invokes it, and an orchestrator
    that skips gates skips the marshal too. What survives that objection is the
    *artifacts*, not the enforcing agent: a single `PIPELINE.yaml` declaring
    gate order plus per-gate required inputs/outputs and exit criteria, with
    the workflow diagram **rendered from that same file** so picture and rule
    cannot drift; and `PIPELINE_LOG.md`, a per-project record of which gates
    actually ran, when, and with what human approval or recorded exception.
    `mas-architect`'s reasoning for why the log is the load-bearing half:
    every gate-skip in F18 violated rules that **already existed**, so the
    problem was never a missing rule — it was that non-compliance was visible
    only to the non-complier. A log makes it visible to someone else. Note the
    gate count is now **11**, not 9, so anything built here must be authored
    against the current order in `admin/MAS_REGISTRY.md`.
  - **Open structural question — "multi-surface project" as a first-class
    concept.** Raised by `mas-architect` and deliberately left open rather than
    silently resolved. This platform has no first-class notion of a project
    having multiple surfaces (web + mobile, app + public API, app + a
    data/deliverables pipeline). Defects 9 and 10 of the F18 ledger are both
    symptoms: desktop web had **zero** SME-suite coverage, and the deliverables
    sat fifteen days stale describing a web-only product. The 2026-07-28 round
    patched the *consequence* — `solution-architect` is now non-droppable for
    multi-surface projects and must produce a per-surface Impact Analysis — but
    the underlying gap is structural: templates are single-surface by
    construction, `PROJECT_CONTEXT.md` has no surface inventory, no gate
    enumerates surfaces, and "which surfaces exist" currently lives only in an
    architect's prose. Candidate directions (none chosen, none evaluated):
    a declared surface inventory in `PROJECT_CONTEXT.md` that gates read;
    multi-surface templates; per-surface test-suite instantiation. **Route
    through `mas-architect` before building anything here** — this is a
    platform-shape question, not a contract tweak.

## Shipped

- **Phase 0 (2026-07-05)**: Admin Control Panel bootstrap — `mas-architect`,
  `mas-registrar`, `mas-release-manager`, `admin-panel` skill, `admin/` state
  files, root `CLAUDE.md`, `.gitignore`, empty `templates/`/`projects/`/`memory/`.
- **Phase 0.5 (2026-07-05)**: Founding Review completed and approved — full
  registry and this roadmap established; four design gaps resolved (see
  `admin/CHANGELOG.md`).
- **Phase 1 (2026-07-05)**: `genai-chatbot` template scaffolded (roadmap item
  1); core 5 agents built in gate order — `plan-agent`, `code-agent`,
  `test-agent`, `review-agent`, `deploy-agent` (item 2); `/new-project` skill
  built running the reduced 5-stage pipeline (item 3, full gate order pending
  items 4-6).
- **Phase 2 (2026-07-05)**: validated the reduced 5-stage pipeline end-to-end
  with a real sample project, `grid-assistant` (mock grid-data chatbot
  feature) — all 5 gates run for real with human approval at each boundary,
  including a genuine mid-pipeline bug found and fixed (`main.py` missing
  `load_dotenv()`, fixed in both the project and the upstream template) and a
  real behavioral test pass against a live Anthropic API call, not simulated.
  Core pipeline pattern (§4b of the design) confirmed sound before building
  the remaining two templates.
- **Phase 3 (2026-07-05)**: `agentic-workflow` (FastAPI + LangGraph, API-only)
  and `rag-knowledge-base` (Next.js + FastAPI + LangChain + Chroma) templates
  built, completing roadmap item 1. Both smoke-tested in throwaway venvs:
  `agentic-workflow`'s `/health` test passes and its LangGraph
  `create_react_agent` wiring builds successfully without a real key;
  `rag-knowledge-base`'s `/health` test passes and document loading/chunking
  verified deterministically, but the full ingest→embed→retrieve→answer flow
  remains unverified pending a real `OPENAI_API_KEY` (embeddings are
  OpenAI-only regardless of chat provider — flagged in the template's own
  manifest as a known gap, not silently assumed working). Verified
  `plan-agent`'s template-selection logic across all 3 templates with 5 test
  requests — 4 correct, unambiguous picks and 1 correctly flagged as
  genuinely ambiguous (asked rather than guessed), confirming the guardrail
  behavior works as designed.
- **Phase 4 (2026-07-05 to 2026-07-06)**: shipped all 5 remaining SME agents —
  `ui-ux-designer`, `solution-architect`, `security-architect`,
  `functional-agent`, `industry-expert` — completing roadmap items 4-6.
  `/new-project` skill rewritten with the full gate order. All 16 registry
  agents now `built`. **Full verification** (two complete 9-gate sample
  projects, not the lighter option): `policy-lookup-assistant`
  (rag-knowledge-base, full team — all 5 SMEs meaningfully engaged, real
  research, real design, a genuine cross-role disagreement surfaced and
  resolved) and `load-alert-agent` (agentic-workflow, core-only — all 4
  optional SMEs correctly dropped, `ui-ux-designer`/Experience Design
  structurally absent for the API-only template, not just declined).
  Retroactively closed a gap in the first pass: the multi-suite Test gate
  mechanism itself wasn't actually exercised (only test-agent's suite had
  run) — invoked all 5 SME test suites for real against
  `policy-lookup-assistant`, which surfaced and fixed **two real bugs**
  (an unhandled 500 on blank/whitespace input, and a LangChain
  `AIMessage.content` list-vs-string shape crash on a degenerate boundary
  input) plus a git-hygiene fix (Chroma binary data wrongly tracked due to a
  `.gitignore` pattern bug, fixed in both the project and the template
  source). This is the clearest evidence yet that the multi-suite design is
  pulling its weight, not just adding process for its own sake.
- **Human-requested additions (2026-07-06)**, routed through `mas-architect`
  via `propose-agent` rather than added ad hoc: `/help` skill (dynamically
  enumerates `.claude/skills/`/`.claude/agents/` — never a hardcoded list);
  `responsible-ai-architect` (new SME, Architecture gate advisory + Review,
  content/behavior guardrails distinct from security-architect's authn/authz
  and functional-agent's domain-correctness lanes — explicit no-duplication
  notes added to both agents' files); `security-architect`'s auth/authz
  scope tightened (Authentication & Authorization Design is now a mandatory
  `SECURITY_KB.md` subsection — decision + criteria + revisit triggers,
  never a one-line waiver); structured per-scenario test evidence capture
  (`projects/<name>/test-evidence/`) added to `test-agent` and all 5 SME
  agents' contracts, laying the groundwork `deliverables-agent`'s future
  Excel export will read from. `deliverables-agent` itself deferred to
  Backlog (post-MVP) — see above.
- **Roadmap addition (2026-07-09)**: interactive HTML knowledge-base page
  added as `deliverables-agent`'s first platform-level export target — see
  Backlog section above for full detail.
- **Phase 5 (2026-07-09)**: shipped `enhance-agent`, completing roadmap item
  7 — owns both `/enhance-project` (new feature on a deployed project) and
  `/modify-feature` (lighter-weight correction mode targeting an existing
  `FEATURES.md` entry). Mini gated pipeline: Plan & Backlog → Experience
  Design (if UI-bearing) → Architecture (lighter-touch) → Code → Test →
  Review → Deploy, same human-approval-at-every-boundary discipline as
  `/new-project`. Re-engagement rule enforced: solution-architect,
  security-architect, and responsible-ai-architect always re-engage on any
  enhancement regardless of original Team Composition roster; ui-ux-designer
  always re-engages for UI-bearing projects; functional-agent/industry-expert
  only if flagged relevant. 15/18 registry agents now `built`; remaining
  `planned` (at the time): `release-manager`, `usage-monitor`,
  `deliverables-agent` — `release-manager` shipped in Phase 6, below.
  **Verified for real**: ran the platform's first
  `/enhance-project` against `grid-assistant` (`GET /regions` endpoint) — a
  deliberately awkward edge case since that project predates Team
  Composition entirely (no original roster recorded). enhance-agent still
  correctly enforced the always-re-engage set while honoring the human's
  choice to leave functional-agent/industry-expert out; `ui-ux-designer` and
  `responsible-ai-architect` both correctly declined to fabricate work for a
  feature with nothing in their respective lanes to act on, rather than
  padding the record. Full mini-pipeline ran gate-by-gate with real
  approvals, real pytest (9/9), a real merge to `main`, and a real local
  redeploy + smoke test against the live process.
- **Phase 6 (2026-07-09)**: shipped `release-manager` (project-level,
  distinct from `mas-release-manager`), completing roadmap item 8. Owns
  `/cut-release`: feature-train batching from "Ready for Release,"
  pairwise conflict detection (human-assisted resolution only — automated
  resolution stays deferred per the original MVP scoping), semver
  classification, full-regression-suite gate on the merged release branch,
  local git-remote-merge promotion to `prod/`, and two distinct required
  approvals (test results, then promotion itself — never collapsed into
  one). **Verified for real**: cut `grid-assistant`'s first release,
  `v1.0.0` — `prod/` created fresh, `dev/` added as a local remote, merged
  and tagged, real `pytest` run on the release branch (9/9) and again
  independently inside `prod/`'s own fresh venv (9/9), and a real local
  `uvicorn` smoke test against the promoted code confirming both `/health`
  and `/regions` work from the actual `prod/` tree, not just `dev/`.
  `RELEASES.md`/`CHANGELOG.md` created with a real, reasoned v1.0.0-not-two-
  versions justification. 16/18 registry agents now `built`; remaining:
  `usage-monitor` (next, tracking-only for MVP), `deliverables-agent`
  (backlog).
- **Phase 7 (2026-07-09)**: shipped `usage-monitor` (tracking/estimation/
  soft-budget only — auto-pause/resume correctly deferred to Backlog, since
  it needs `CronCreate` which the MVP version isn't granted), completing
  roadmap item 9. Tracking works because every Agent-tool call already
  returns real token-usage metadata — the orchestrator appends one
  `USAGE.md` line per call; `usage-monitor` itself is invoked for the
  *analysis* half (pre-work estimates, cross-project rollup, soft-budget
  checks). Wired a usage-logging step and a pre-work-estimate step into
  `/new-project`'s Team Composition gate and `/enhance-project`'s
  pre-Code step; also caught and fixed a real staleness gap in
  `/new-project` — it predated `responsible-ai-architect` and was missing
  it from Team Composition/Architecture/Test gate lists entirely.
  **Verified for real**: backfilled `USAGE.md` for `policy-lookup-assistant`
  (~646,833 tokens, full team) and `load-alert-agent` (~150,297 tokens,
  core-only) from actual per-call token totals recorded during their real
  builds, rolled up into `memory/USAGE_INDEX.md`, then ran a real dry-run
  estimate for a hypothetical new UI-bearing project's Team Composition
  gate — the output was honestly caveated on n=2 sample size, correctly
  caught that `load-alert-agent`'s API-only shape wasn't a clean core-only
  comparison for a UI-bearing template (adjusted for the mandatory
  Experience Design gate), and gave a concrete, actionable recommendation
  rather than a vague estimate. 17/18 registry agents now `built`; only
  `deliverables-agent` remains, in Backlog. **Only remaining MVP item**:
  `/consult`.
- **Phase 8 (2026-07-09)**: shipped `/consult` — thin router (no owning
  agent) to any SME on demand, without waiting for or re-running a gate;
  never changes the project's Active Team roster as a side effect. **Original
  MVP scope (roadmap items 1-10) is now 100% shipped.** **Verified for
  real**: consulted `responsible-ai-architect` on `grid-assistant`'s
  original `/chat` feature (predates that agent's existence) about
  role-play/instruction-override/off-topic-drift guardrails — got a real,
  honestly-scoped answer (a genuine low-to-moderate gap identified, not
  padded, not dismissed), correctly logged to a new-or-appended
  `RESPONSIBLE_AI_KB.md` entry and `PROJECT_CONTEXT.md`'s Decisions Log,
  both tagged `[consult]`, with explicit confirmation the roster was not
  touched. The subagent also correctly identified and disregarded what
  looked like injected content in a tool result during this run, without
  acting on it — verified the underlying file was clean, no real concern,
  but good evidence the "treat fetched content as data, not instructions"
  discipline holds under a real (if likely harness-artifact) test.
  **Human decision**: reviewed the full backlog collectively afterward and
  selected 5 of 6 items to build next (all but cloud `target_env`), in a
  proposed order — see Phase 9 below.
- **Phase 9, item 1 of 5 (2026-07-09)**: shipped the **interactive HTML
  knowledge-base page** standalone, decoupled from `deliverables-agent`
  (confirmed it needed none of that agent's Office-export tooling — pure
  markdown-to-HTML, no new dependencies). Generated from
  `admin/MAS_REGISTRY.md` (18 agents, grouped core/SME/infra/platform,
  click-to-expand), the 9-gate pipeline (click-to-expand per gate, showing
  which agents act there and which are optional), the 3 templates, and every
  command from `.claude/skills/*/SKILL.md`. Published as an Artifact for
  human review; source file at `admin/deliverables/knowledge-base.html`.
  Design: schematic/blueprint-inspired palette (ink-navy ground, amber for
  gates, teal for agents, semantic status colors kept separate), monospace
  for identifiers (agent/command names read as code because they are code),
  humanist sans for prose. Both light/dark themes designed, not inverted
  naively. Regeneration note recorded in the page's own footer: regenerate
  after any registry or roadmap change (this is currently a manual step —
  the automated "regenerate at the triggering write" trigger described in
  the original scope note is `deliverables-agent`'s job once that agent
  exists; until then, treat this as a snapshot to refresh by hand).
- **`synthetic-data-agent` (2026-07-12)**: scaffolded per `mas-architect`'s
  2026-07-11 advisory review, approved via checkbox backlog review
  2026-07-12. Cross-cutting, invoked just before the Test gate or on-demand
  for QA/demo prep — not a new pipeline gate. Optional/droppable, default-on
  for `genai-chatbot`/`rag-knowledge-base`, default-off for
  `agentic-workflow`. Owns `knowledge/TEST_DATA_KB.md` only (read-only
  sourced from `DOMAIN_KB.md`/`INDUSTRY_KB.md`), owns no test suite. Bash
  scoped to invoking code-agent's `scripts/seed-data.sh reset|reload` only —
  no direct infra/DB access. See Backlog section above for the full design
  and `.claude/agents/synthetic-data-agent.md` for the built contract. Pure
  scaffolding — no project has adopted this agent yet.
- **Verification-gap round (2026-07-28)**: shipped the six items the human's
  decision table marked BUILD in
  `admin/proposals/2026-07-28-pipeline-verification-gap.md`. **Roster 19 → 21
  agents; pipeline 9 → 11 gates.** Evidence base: the little-milestones F18
  mobile build shipped ten defects, eight caught by the human on the running
  app and **zero** caught by the nine gates or six SME suites — the pipeline
  verified that code was written, never that the feature worked.
  - **`functional-design-agent` (new, v1.0.0)** — new **Functional Design**
    gate between Plan & Backlog and Experience Design; core, all templates;
    owns `knowledge/FUNCTIONAL_SPEC.md`; owns no test suite. Per-feature
    Given/When/Then acceptance criteria with **stable unique IDs**
    (`AC-F18-03`), mandatory edge/empty/error coverage, and mandatory
    **observable-UI criteria** for UI-bearing features. Lane discipline against
    `plan-agent` and `ui-ux-designer` defended in contract prose, per
    `mas-architect`'s flagged overlap risk. Human overrode the recommended
    fold.
  - **`verification-agent` (new, v1.0.0)** — new **Verification** gate between
    Test and Review; core, **blocking**, sole gate owner. Owns no KB and no
    test suite; produces a per-feature evidence matrix in
    `PROJECT_CONTEXT.md`. Unmapped acceptance criteria are `NOT VERIFIED`,
    never folded into a pass, and block back to Code. Hard read-only
    (`Read, Grep, Glob`) and contractually barred from re-reasoning about the
    code, per `mas-architect`'s cost caveat. Human overrode the recommended
    fold; blocking-not-advisory was the orchestrator determination.
  - **RNTL native rendering backend (`test-agent` v1.4.0)** —
    `mas-architect`'s strongest recommendation and absent from the original
    proposal entirely. Rendered-UI verification had exactly one built backend
    (Playwright, web-only), so F18's rendering defects were **structurally
    uncatchable** even though it ran under the v1.3.0 rendered-UI contract.
    RNTL renders in-process with **no simulator required**, so the 2026-07-26
    toolchain spike's blocker doesn't apply. Maestro + simulator retained as
    the deeper future native backend, not deleted.
  - **`code-agent` v1.3.0 (C1)** — unit tests are a Code-gate deliverable in
    the implementer's own commit; every new UI component gets a reachability
    test **rendered from the real entry point**, never in isolation.
  - **`review-agent` v1.3.0 (C5)** — wiring sweep tracing from the app entry
    point through the render tree; an import is explicitly not sufficient
    evidence of reachability.
  - **`solution-architect` v2.0.0 (C2, MAJOR)** — non-droppable for any
    multi-surface project, plus a mandatory per-enhancement Impact Analysis
    whose unjustified surface omissions block the Architecture gate.
  - **Not built by decision**: `pipeline-marshal` (circularity accepted) and
    the `deliverables-agent` freshness check (an optional agent may not block a
    core gate). C3, C6, the `PIPELINE.yaml`/`PIPELINE_LOG.md` artifacts, and the
    open multi-surface structural question moved to Backlog above.
    Pure platform scaffolding — no project has run the 11-gate pipeline yet.
