# mas-architect consolidated review — 2026-07-26

Advisory review of `admin/proposals/2026-07-25-agent-improvements.md`.
**Nothing implemented. Every item needs per-item human approval before
`mas-registrar` acts.**

## Headline judgments

1. The two reported drifts are the visible part of a **systemic** problem — the
   registry's Tools column mixes *enforceable frontmatter grants* with
   *prose-only scoping annotations*. **8 more rows** have the same defect.
   Fix the column shape, not the two rows.
2. `code-agent`'s broad Bash is **correct — the registry is wrong**.
   `review-agent`'s broad Bash is **not** correct, but `Bash(git diff)` is also
   wrong. Different resolutions.
3. plan-agent PO/PRD is **one role, not two** — fold in, don't create a
   product-owner agent. **But "main reviewer of features" transfers decision
   rights to an agent — recommended AGAINST.** See C.
4. Mobile was filed under `code-agent`. **It is not a code-agent item** —
   code-agent needs almost nothing. It's a template + toolchain + test-harness
   + deploy-target + security-model program, and its distribution half is
   **blocked on cloud `target_env`, which the human deselected**. Internally
   inconsistent.
5. Headless-browser and mobile-E2E are **not the same capability**. Don't
   bundle. Build Playwright first — it pays off on every existing project today.

## A — Registry drift

- **code-agent**: correct the REGISTRY to disk (`Read, Write, Edit, Grep, Glob,
  Bash`). Scoping to `Bash(git)` would break the Code gate immediately — it
  needs npm/pip/pytest/tsc/build/linters. Add shell-discipline prose instead
  (confine to `dev/`, no `prod/`, no `git push`/`reset --hard`, no long-lived
  servers in-turn).
- **review-agent**: **both are wrong** → `Read, Grep, Glob, Bash` + hard
  read-only discipline. It needs `git log/show/status`, not just diff; it
  lacked Grep/Glob entirely, which is likely *why* Bash got widened. Rejected
  alternative (drop Bash, orchestrator hands it a diff) recorded so it isn't
  re-litigated.
- **8 more prose-only-scope rows**: functional-agent, industry-expert,
  solution-architect, security-architect, responsible-ai-architect,
  ui-ux-designer (`Write (KB)` vs `Write`), deliverables-agent,
  synthetic-data-agent (`Bash (scoped)` vs `Bash`).
- **Fix**: split registry Tools column into **`Tool grant`** (verbatim
  frontmatter, byte-comparable) and **`Scope constraint`** (prose, advisory).
- **Two phantom findings to VERIFY EMPIRICALLY, not assume**:
  - `Bash(git)` scoping syntax may not be honored in subagent frontmatter
    (that syntax belongs to the permissions system). `release-manager` and
    `enhance-agent` may silently hold unrestricted Bash — or have the grant
    dropped entirely.
  - `DesignSync` may be a phantom tool (LESSONS already records "DesignSync
    unavailable"). Audit should report `UNRESOLVABLE`, not `MATCH`.
- **Prevention**: mas-architect drift audit (verdicts: MATCH / DRIFT / MISSING
  ON DISK / ORPHAN / UNRESOLVABLE; also compares `status`), run as pre-flight on
  every `propose-agent` and **blocking before any platform version cut**. No
  tool change needed. mas-registrar gets a `verify` action + **post-write
  self-check** (re-read file, echo frontmatter, confirm) + **real versioning**
  (`version:`/`updated:` frontmatter, `## Change history`, registry Version
  column, semver: MAJOR=gate/core/KB/suite change, MINOR=tool or new required
  behavior, PATCH=clarification; backfill all to 1.0.0 with real build dates).
- **7th contract question — interruption/resumability**: declare write set up
  front; never reference a file that doesn't exist yet; checkpoint per coherent
  unit (= code-agent's phased commits, same fix); on resume re-read on-disk
  state. Makes the phased-commit item an instance of a general rule.

## B — Queued LESSONS backlog

- **B1 Write→Edit (HIGHEST PRIORITY — destroyed ARCHITECTURE_KB 787 lines and
  UX_KB 458 lines, one day apart; both recoveries depended on transcripts
  existing).** Do **both** halves:
  - Grants: `Edit` for all append-target agents; where creation is also needed,
    keep `Write` bound by **"`Write` only if the file does not exist — `Read`
    first; if the Read succeeds, `Write` is off the table."** Affects
    ui-ux-designer, solution-architect, security-architect,
    responsible-ai-architect, functional-agent, industry-expert,
    synthetic-data-agent, plan-agent, enhance-agent, release-manager,
    usage-monitor. **Exclude deliverables-agent** (regenerates wholesale —
    `Write` is semantically correct).
  - Git backstop: orchestrator commits `projects/<name>/` root artifacts
    (root md + `knowledge/` + `test-evidence/` + `design-review/`; NOT
    `dev/`/`prod/`/`.venv`) at every gate close. **Verify `.gitignore` with a
    real `git check-ignore -v` pass first** (`dev/.venv/` has hundreds of files
    on disk).
  - **Policy conflict to resolve**: DOMAIN_KB records an orchestrator-proxy
    KB-write policy that conflicts with registry KB ownership. Recommend
    **agent-writes-with-Edit; retire the proxy** — but record it as an explicit
    decision; two contradictory policies are running today.
- **B2 scoped Bash for the 6 suite-owning SMEs**: none has a shell tool today —
  responsible-ai-architect could only return `STATIC ONLY — NOT EXECUTED`; when
  actually run it found **3 defects static review missed**. Use the proven
  `synthetic-data-agent` pattern: code-agent authors
  `dev/tests/suites/<suite>/run.sh`; each SME's Bash scoped to invoking its own
  entry point + read-only result inspection. Also makes advisory-vs-blocking
  meaningful (today unexecuted and passing are indistinguishable).
- **B3 completeness-check rollout**: go **wider** than queued — add test-agent,
  review-agent, deploy-agent, enhance-agent. Load-bearing wording: agent must
  **state explicitly which binding decisions it checked and how the output
  satisfies each**, else it's aspirational.
- **B4 review-agent cross-KB sweep**: add a **third verdict — `escalate`**
  (contradiction between two SME KBs is not code-agent's to fix). Names both
  KBs/owners and quotes the conflict. Lane discipline: review-agent reports
  that they disagree, never adjudicates which is right. Scope: changed KBs by
  default, full sweep at `/cut-release`.
- **B5**: land checkbox-backlog (plan-agent — as a *default pre-selection,
  never the decision*) and rendered-mockup-before-approval (ui-ux-designer) in
  contract text.

## C — plan-agent → product owner + PRD (CORE-5 role change)

- **One role. Fold into plan-agent.** A PO agent would sit at the same gate,
  own no distinct KB and no test suite — two of six contract answers empty =
  it's an artifact/capability, not a role.
- **DISAGREES with "main reviewer of features."** Granting an agent authority
  to reject a human-requested feature **inverts the human-in-command claim that
  is the product's central pitch and is live on the site**, and creates a silent
  failure mode (a rejected feature never reaches the checkbox list).
  **Recommended instead: feature steward + recommender-of-record** — single
  consolidation point for all feature sources; explicit reasoned recommendation
  per feature (approve-MVP / approve-later / recommend-reject + rationale);
  accountable for PRD integrity; **never removes a feature from the human's
  view** — a recommend-reject appears on the checkbox list like a deferred item.
- **Overlap: nobody loses their pass; everyone gains a durable destination.**
  functional-agent's challenges get recorded in a PRD **Challenge Log with
  dispositions** (today they evaporate into the transcript); industry-expert
  proposes into a **Candidate Backlog**; review-agent's "intent" reference
  becomes **PRD + Decisions Log instead of the transient PLAN.md** (a material
  gain — checking intent against a doc superseded every gate is the structural
  reason drift is hard to catch); enhance-agent must land every feature in the
  PRD.
- **Contract**: gate **unchanged** (Plan & Backlog; deliberately NOT added to
  Intake — that would put a core-5 agent upstream of Team Composition and turn
  a role expansion into a structural change). Core, non-droppable. New artifact
  `projects/<name>/PRD.md` at **project root, NOT under `knowledge/`** (that
  namespace is SME research). No test suite. Tools `Read, Write, Edit, Grep,
  Glob` — **not Bash** (writes no code), **not WebSearch** (that's
  industry/functional-agent's lane). Version bump **MAJOR**.
- **PRD vs PLAN vs FEATURES**: PRD = standing, product-level, intent +
  rationale + acceptance criteria. PLAN = transient, per-increment, *how*.
  FEATURES = state ledger (status/released). **Hard rule: PRD never records
  release status; FEATURES never records rationale.**
- **The join key — most valuable structural piece**: stable feature IDs
  (`F-001`) minted in the PRD, referenced by FEATURES, PLAN, test-evidence,
  release notes. Makes reconciliation mechanical.
- **Anti-stale**: append-only dated; every enhancement must land in PRD;
  review-agent reconciles PRD↔FEATURES IDs (orphan ID = finding);
  `Last reconciled:` refreshed at `/cut-release`.
- **Scale it**: sections 1/3/6 minimum for small projects, rest as-needed, or
  every small project pays enterprise tax.
- **Do NOT retro-fit**: PRDs start at next `/new-project`; existing projects get
  a **backfill-lite** on their next enhancement (register derived mechanically
  from FEATURES; rationale left `not recorded — predates PRD`). Fabricated
  rationale in the spec of record is worse than none.

## D — Mobile

- **Re-scope**: not a code-agent item (code-agent needs **no tool change**).
  It's a platform program.
- **Direction: React Native + Expo.** Reuses proven TypeScript/React
  competence; Expo reaches real-device without the full native chain first;
  jest+RNTL matches test-agent's existing shape. **Reject native
  Swift+Kotlin** (2 toolchains, ~2x SME surface, no reuse, no requirement
  justifying it) and **Flutter** (Dart = zero existing competence) — record both
  as considered-and-rejected.
- **Responsive/PWA recommended as the honest first step**, shipped separately
  and labelled honestly — achievable today, must never be marketed as "mobile
  apps."
- **Backend unchanged** (Python/FastAPI) — a mobile app is just another API
  client; all templates already split backend/frontend. Genuinely additive.
- **Toolchain must be VERIFIED, not assumed** — Xcode is a multi-GB install and
  is **unverified on this machine**; that's the largest unknown. **Do the spike
  first**: boot a simulator, run a trivial Expo app, screenshot it. If Xcode
  can't be installed, the iOS half isn't real — surface that in hour one.
- **Human-owned prerequisites**: Apple Developer ($99/yr) and Google Play ($25)
  accounts. **No Apple account = TestFlight impossible, full stop.** Absent
  them the honest claim is *"apps that run on a simulator and your own devices
  via a dev build"* — not *"we ship mobile apps."*
- **Simulator lifecycle constraint**: a process started inside a subagent's turn
  dies with the turn (LESSONS 2026-07-09), so the **simulator must be booted by
  deploy-agent/orchestrator, not inside test-agent's turn.** Design in up front.
- **E2E: Maestro over Detox** (YAML flows, no native build instrumentation).
- **Distribution must be a SEPARATE parameter from `target_env`** (`target_env`
  = where it runs; `distribution` = how it reaches a user). Conflating them
  produces an unmaintainable stub — and `target_env` is already stubbed once.
- **Cloud dependency (most important constraint)**: simulator + own-device work
  **without** cloud. **Distribution to anyone off-LAN requires a publicly
  reachable API = cloud `target_env`.** The human selected mobile but deselected
  cloud — inconsistent past a simulator. **Recommend re-selecting cloud**; if
  declined, mobile must be permanently scoped/marketed as simulator/own-device
  only, as a *recorded decision*, not a discovered surprise.
- **Biggest SME change is security-architect (M)**: a mobile client cannot hold
  secrets — the templates' `.env`-with-API-key pattern becomes an outright
  vulnerability in a shipped binary. Requires server-side-only keys,
  Keychain/Keystore token storage, PKCE public-client auth. **ui-ux-designer
  (M)**: needs a mobile analogue of the rendered-preview mechanism (device
  frames) or the human's non-negotiable mockup-before-approval rule silently
  stops working for mobile.
- **Site honesty**: the boundary lines were REMOVED from the live page
  2026-07-25, so **the site is currently silent on mobile — no false claim
  today**. But `DOMAIN_KB.md` still lists native mobile under HARD OUT, so KB
  and site now describe different worlds (an in-the-wild instance of the B4
  problem). **Staged evidence-gated claims**: (i) responsive/PWA after a passing
  viewport suite → "mobile-web"; (ii) RN on real simulator + device with passing
  Maestro → "cross-platform apps you run on your own devices"; (iii) cloud +
  paid accounts + a real store build → "app-store distribution." Each stage gets
  its own CITATIONS row + evidence artifact; amend DOMAIN_KB in the same pass
  (moving HARD OUT → MUST HEDGE is itself a claims change).
- Risk framing: DOMAIN_KB records that "built by Conclave itself" is the site's
  strongest asset and cuts both ways — **a mobile claim that fails a live demo
  does more damage than no claim at all.**

## Recommended build order

1. **Contract sweep (P0, one registrar pass)** — B1 (+git backstop) · A1 both
   drifts · A2 column split · A3 audit+verify+versioning · A4 7th question +
   phased commits · B3 rollout · B5 · deploy URL/health · test-count delta.
   *Nothing ships before the KB-destruction fix.* Closes 2026-07-20 P1 item 1.
2. **Suite execution** — B2 scoped Bash + `run.sh` convention.
3. **Rendered-UI verification (web)** — Playwright · COPY_MANIFEST ·
   review-agent copy-drift · B4 cross-KB sweep.
4. **PRD / plan-agent** — before mobile, so mobile's requirements land in a PRD.
5. deploy-agent rollback + redeploy verification.
6. Golden-set evals (needs 3's harness + 4's IDs).
7. Mobile-web / PWA — honest claim (i).
8. **Mobile toolchain spike** — can run in parallel from Phase 1; do early
   *because it might return bad news*.
9. **Cloud `target_env`** — recommend re-selecting.
10. RN/Expo template + E2E + deploy targets + security rework — claim (ii).
11. Store distribution — claim (iii).

**Defer**: store distribution (blocked on non-engineering factors — no date),
native/Flutter (record as rejected), acceptance-criteria coverage (after PRD ID
spine), feature flags (trigger unmet), multi-tenant (trigger unmet).

---

# HUMAN DECISIONS — 2026-07-26

- **Phase 1 contract sweep: APPROVED as recommended** (full bundle, one registrar pass).
- **plan-agent: APPROVED as steward + recommender-of-record** — mas-architect's
  counter-proposal accepted; agent does NOT get feature-rejection authority.
  Every feature, including recommend-rejects, still reaches the human's
  checkbox list. Human retains final say.
- **Mobile: toolchain spike FIRST** (approved), before any commitment or claim.
- **Cloud `target_env`: RE-SELECTED** (approved) — unblocks mobile distribution
  and makes the live FDE claim true.

# MOBILE TOOLCHAIN SPIKE — RESULT (2026-07-26, run for real)

Host: macOS 26.5.2, arm64 (Apple Silicon).

| Component | Status |
|---|---|
| Node / npm | **v24.18.0 / 11.16.0 — present** |
| Xcode (full) | **MISSING** — only Command Line Tools at `/Library/Developer/CommandLineTools`; `xcodebuild` unavailable |
| iOS Simulator | **UNAVAILABLE** — `xcrun simctl list devices available` returned no devices |
| Android SDK | **MISSING** |
| Android Studio | **MISSING** |
| adb / Java (JDK) | **MISSING** ("Unable to locate a Java Runtime") |
| watchman | MISSING |
| CocoaPods | MISSING |

**Verdict: neither an iOS simulator nor an Android emulator can run on this
machine today.** This is the blocker mas-architect predicted, surfaced before
any roadmap date or site claim was committed — which is exactly why the spike
was sequenced first.

**What this changes:**

- **Simulator/emulator development is blocked on large, human-owned installs**
  that no agent can perform: full **Xcode** (multi-GB, App Store / Apple ID) for
  iOS, and **Android Studio + SDK + a JDK** for Android.
- **BUT physical-device development is achievable today.** Expo Go runs a React
  Native app on a real iPhone/Android phone over LAN via the Expo dev server,
  which needs only Node — already present. That is a real, unblocked path to
  "running on a real device" without Xcode or Android Studio.
- Therefore the recommended near-term mobile scope is **Expo + physical device
  via Expo Go**, with simulator/emulator work gated on the human installing the
  toolchains, and store distribution still gated on cloud `target_env` (now
  approved) plus paid developer accounts (Apple $99/yr, Google $25) that remain
  human-owned.
- **No mobile claim may go on the site at this stage.** Per the staged
  evidence-gated ladder, stage (ii) requires a real app on a real device with a
  passing E2E suite. Nothing has been demonstrated yet.

# RESOLVED FINDING — DesignSync is NOT a phantom

mas-architect flagged `DesignSync` as possibly naming a tool absent from the
runtime. **Checked: it is present and available in this session's tool
registry.** The audit should record it `MATCH`, not `UNRESOLVABLE`. The
LESSONS "DesignSync unavailable" note refers to a specific subagent invocation
context, not to the tool being nonexistent.

**Still unverified**: whether `Bash(git)` parenthesised scoping is honoured in
subagent frontmatter (affects `release-manager`, `enhance-agent`). Treat as
`Bash` + prose until empirically tested.
