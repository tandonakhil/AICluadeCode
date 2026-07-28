# The Conclave Pipeline — canonical definition

**This file is the source of truth for the pipeline's *shape*.**
`admin/MAS_REGISTRY.md` remains the source of truth for *who* each agent is.
`.claude/skills/new-project/SKILL.md` is the executable form of this order —
if the two ever disagree, this file and the registry win, and the skill is the
one to correct.

Maintained by the **orchestrator** (see `admin/ORCHESTRATOR.md`). Any change to
gate order, gate ownership, or approval authority goes through `mas-architect`
review and human approval first, exactly like an agent contract.

---

## 1. The pipeline

Eleven gates. Every arrow marked ✋ is a **human approval that cannot be
skipped**. A gate never advances on the orchestrator's own judgement.

```mermaid
flowchart TD
  REQ([Human request]) -->|start| G1

  G1["**1 · Intake**<br/>domain + industry questions<br/>functional-agent · industry-expert"]
  G2["**2 · Team Composition**<br/>roster + cost estimate<br/>orchestrator · usage-monitor"]
  G3["**3 · Plan &amp; Backlog**<br/>PLAN.md + MVP scope<br/>plan-agent"]
  G4["**4 · Functional Design**<br/>FUNCTIONAL_SPEC.md · AC-* IDs<br/>functional-design-agent"]
  G5["**5 · Experience Design**<br/>flows + rendered mockup<br/>ui-ux-designer"]
  G6["**6 · Architecture**<br/>+ mandatory Impact Analysis<br/>solution-architect · security-architect"]
  G7["**7 · Code**<br/>+ unit &amp; reachability tests<br/>code-agent"]
  G8["**8 · Test**<br/>unit/integration + 6 SME suites<br/>test-agent"]
  G9["**9 · Verification**<br/>every AC → executed check<br/>verification-agent · BLOCKING"]
  G10["**10 · Review**<br/>diff hygiene · wiring sweep<br/>review-agent"]
  G11["**11 · Deploy**<br/>run local + smoke test<br/>deploy-agent"]
  DONE([Deployed · dev local])

  G1 -->|✋| G2 -->|✋| G3 -->|✋| G4 -->|✋| G5 -->|✋| G6 -->|✋| G7
  G7 -->|✋| G8 -->|✋| G9 -->|✋| G10 -->|✋| G11 -->|✋| DONE

  G8  -.->|suite FAILED| G7
  G9  -.->|NOT VERIFIED| G7
  G10 -.->|request-changes| G7
  G10 -.->|escalate · KBs disagree| G6
  G11 -.->|smoke failed| G7

  classDef gate fill:#eef4fb,stroke:#2b6cb0,stroke-width:1px,color:#0f2b46
  classDef block fill:#fdf0ec,stroke:#a3341f,stroke-width:2px,color:#3d1109
  classDef term fill:#eef6ef,stroke:#2f6f43,color:#123021
  class G1,G2,G3,G4,G5,G6,G7,G8,G10,G11 gate
  class G9 block
  class REQ,DONE term
```

**Dotted arrows are the loops.** They are not exceptions — they are the normal
operation of a pipeline that is actually checking anything. A run with no
loop-backs is more likely to mean the checks are weak than that the code was
perfect.

---

## 2. Gate reference

| # | Gate | Owner (final say) | Human checkpoint | Exit criteria | Loops back to |
|---|------|-------------------|------------------|---------------|---------------|
| 1 | Intake | orchestrator | Confirm domain + industry | `DOMAIN_KB.md`, `INDUSTRY_KB.md` seeded | — |
| 2 | Team Composition | orchestrator | **Approve roster + Test Policy** | Roster in `PROJECT_CONTEXT.md`; cost estimate shown | — |
| 3 | Plan & Backlog | plan-agent | **Approve MVP scope** (per-feature checkboxes) | `PLAN.md`; approved backlog in `FEATURES.md` | — |
| 4 | Functional Design | functional-design-agent | Approve acceptance criteria | `FUNCTIONAL_SPEC.md`, every AC carrying a stable ID | 3 |
| 5 | Experience Design | ui-ux-designer | **Approve from a rendered mockup**, never spec text | `UX_KB.md`; mockup in `design-review/` | 4 |
| 6 | Architecture | solution-architect + security-architect (joint) | Approve design + Impact Analysis | `ARCHITECTURE_KB.md` incl. blast radius; `SECURITY_KB.md` | 5 |
| 7 | Code | code-agent | Approve implementation summary | Commits; unit + reachability tests in the same commit | 6 |
| 8 | Test | test-agent | Approve per-suite report | Every suite `EXECUTED`; blocking suites pass | **7** |
| 9 | **Verification** | verification-agent | Approve evidence matrix | Every `AC-*` → named executed passing check | **7** |
| 10 | Review | review-agent | Approve verdict | `approve` (not `request-changes`/`escalate`) | **7** or 6 |
| 11 | Deploy | deploy-agent | Approve deployment | App up; smoke test passes | 7 |

### Gates that may be skipped, and how

- **5 · Experience Design** — not applicable to `agentic-workflow` (no UI).
  Skipped by template, recorded, not silently omitted.
- **Any gate whose only active SMEs were dropped** at Team Composition still
  "runs" in the sense that its absence is written into `PROJECT_CONTEXT.md`.
  An unreviewed gate must be visible later, never absent.
- **Nothing else.** A gate skipped for any other reason is a **human
  exception**: explicitly requested, explicitly approved, and recorded in the
  Decisions Log with its reason. The orchestrator may not grant itself one.

---

## 3. Progress notation

The orchestrator re-renders the graph **at every gate**, using these states.
The notation is deliberately small — five states, one glyph each.

| Glyph | State | Meaning |
|-------|-------|---------|
| `✅` | `done` | Gate closed, human approved |
| `▶` | `active` | Currently running, or awaiting human approval |
| `↩` | `looped` | Failed and sent work back; will re-run |
| `⬜` | `pending` | Not started |
| `⊘` | `skipped` | N/A for this template, or SMEs dropped — recorded |

Mermaid class definitions to reuse verbatim, so every render looks the same:

```
classDef done    fill:#eef6ef,stroke:#2f6f43,color:#123021
classDef active  fill:#fff8e6,stroke:#8a6410,stroke-width:2px,color:#3d2c04
classDef looped  fill:#fdf0ec,stroke:#a3341f,stroke-width:2px,color:#3d1109
classDef pending fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d
classDef skipped fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d,stroke-dasharray:4 3
```

---

## 4. The orchestrator's obligations

1. **Create** `projects/<name>/PIPELINE_LOG.md` at project start, from
   `admin/templates/PIPELINE_LOG_TEMPLATE.md`.
2. **Render the graph at every gate**, before asking for approval — current
   state, what was just produced, what comes next. The human should never have
   to ask "where are we?"
3. **Log the row** on every gate close: gate, date, participants, artifacts,
   approval, and any exception with its reason.
4. **Redraw on any change of shape.** A mid-flight scope change, an
   enhancement, a re-opened gate, or an SME re-engagement all change the
   route. The graph must show the route actually being taken, not the one
   planned at the start. A stale graph is worse than none — it asserts
   something false.
5. **Never mark a gate `done` that the human did not approve.** The log is
   evidence; if it can be written optimistically it is worth nothing.

**Why the log exists.** During the F18 mobile build the orchestrator skipped
gates and nothing detected it, because the only party who could see the
omission was the party making it. `PIPELINE_LOG.md` makes non-compliance
visible to someone else — `review-agent` at Review, `release-manager` at
`/cut-release`, and the human at any point. That is the entire design intent:
not another rule, but a record that makes the existing rules checkable.

---

## 5. Related files

- `admin/MAS_REGISTRY.md` — who each agent is, its gate, tools, version
- `admin/ORCHESTRATOR.md` — the orchestrator's own contract
- `admin/samples/PIPELINE_WALKTHROUGH.md` — a full worked run, including a
  failing Test loop, a `NOT VERIFIED` loop, a `request-changes` loop, and a
  mid-enhancement redraw
- `admin/templates/PIPELINE_LOG_TEMPLATE.md` — the per-project tracker
- `.claude/skills/new-project/SKILL.md` — the executable form of §1
