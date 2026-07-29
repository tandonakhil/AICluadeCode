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

Eleven gates, each followed by a **human approval that cannot be skipped**. A
gate never advances on the orchestrator's own judgement.

**Layout.** Reads left-to-right, **max 7 boxes per row**, wrapping to the next
line. A pipeline is a journey and a journey reads along the page — but eleven
gates plus eleven approvals in one line is unreadable, so rows carry **3 gates
and their 3 approvals (6 boxes)** and wrap. Rows never split a gate from the
approval that closes it.

**Human checkpoints are boxes, not edge labels.** The `✋` diamonds are
first-class nodes with their own state, because the approval *is* a step — the
single step where the pipeline stops and waits for a person. Rendering it as a
decoration on an arrow understates what it is. When the run is waiting on you,
that diamond renders **activated** — thick border, `✋ YOU / approve?` — and is
the loudest thing in the graph.

```mermaid
flowchart TB
  subgraph r1 [" "]
    direction LR
    G1["⬜ 1<br/>Intake"] --> H1{"✋<br/>—"} --> G2["⬜ 2<br/>Team"] --> H2{"✋<br/>—"} --> G3["⬜ 3<br/>Plan"] --> H3{"✋<br/>—"}
  end
  subgraph r2 [" "]
    direction LR
    G4["⬜ 4<br/>Functional"] --> H4{"✋<br/>—"} --> G5["⬜ 5<br/>Experience"] --> H5{"✋<br/>—"} --> G6["⬜ 6<br/>Architecture"] --> H6{"✋<br/>—"}
  end
  subgraph r3 [" "]
    direction LR
    G7["⬜ 7<br/>Code"] --> H7{"✋<br/>—"} --> G8["⬜ 8<br/>Test"] --> H8{"✋<br/>—"} --> G9["⬜ 9<br/>Verify"] --> H9{"✋<br/>—"}
  end
  subgraph r4 [" "]
    direction LR
    G10["⬜ 10<br/>Review"] --> H10{"✋<br/>—"} --> G11["⬜ 11<br/>Deploy"] --> H11{"✋<br/>—"}
  end
  H3 --> G4
  H6 --> G7
  H9 --> G10
  H11 --> DONE(["Deployed · dev local"])
  G8 -.->|FAILED| G7
  G9 -.->|NOT VERIFIED| G7
  G10 -.->|request-changes| G7
  G10 -.->|escalate| G6
  G11 -.->|smoke failed| G7
  classDef done    fill:#eef6ef,stroke:#2f6f43,color:#123021
  classDef active  fill:#fff8e6,stroke:#8a6410,stroke-width:2px,color:#3d2c04
  classDef looped  fill:#fdf0ec,stroke:#a3341f,stroke-width:2px,color:#3d1109
  classDef warn    fill:#fff8e6,stroke:#8a6410,stroke-width:2px,color:#3d2c04
  classDef pending fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d
  classDef skipped fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d,stroke-dasharray:4 3
  classDef skip_na  fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d,stroke-dasharray:4 3
  classDef skip_pre fill:#eef1f6,stroke:#8d99ab,color:#5b6675,stroke-dasharray:1 3
  classDef skip_owed fill:#f8ded7,stroke:#a3341f,stroke-width:3px,color:#3d1109
  classDef hdone   fill:#dcefe2,stroke:#2f6f43,color:#123021
  classDef hwait   fill:#ffe9a8,stroke:#8a6410,stroke-width:4px,color:#3d2c04
  classDef hpend   fill:#fafbfc,stroke:#cfd5dd,color:#98a1ad,stroke-dasharray:3 3
  classDef hskip   fill:#fafbfc,stroke:#cfd5dd,color:#98a1ad,stroke-dasharray:3 3
  classDef hpre    fill:#eef1f6,stroke:#8d99ab,color:#5b6675,stroke-dasharray:1 3
  classDef hnone   fill:#f8ded7,stroke:#a3341f,stroke-width:3px,color:#3d1109
  classDef rowbox  fill:none,stroke:none
  class G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,DONE pending
  class H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11 hpend
  class r1,r2,r3,r4 rowbox
```

Gate owners and artifacts are in the table below rather than in the node
labels — at eleven nodes across, long labels make the graph unreadable, and the
graph's job is position-at-a-glance, not reference.

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

The orchestrator re-renders the graph **at every step**, using these states.

### Gate states

| Glyph | Class | Meaning |
|-------|-------|---------|
| `✅` | `done` | Gate closed, human approved |
| `▶` | `active` | Currently running |
| `↩` | `looped` | Failed and sent work back; will re-run |
| `⚠` | `warn` | Ran, but incompletely — see the log |
| `⬜` | `pending` | Not started |

### The three reasons a gate shows `⊘` — never one glyph

| Label | Class | Meaning |
|-------|-------|---------|
| `⊘ n/a` | `skip_na` | **Not applicable by template.** No approval was owed. |
| `⊘ pre-gate` | `skip_pre` | **The gate did not exist** when this project ran. A real coverage gap, not a template exclusion. |
| **`⊘ SKIPPED`** | `skip_owed` | **Owed and skipped.** Renders in alarm red. |

These were a single `⊘` with a single `✋ n/a` until 2026-07-29, when
`ui-ux-designer` found that `admin/PORTFOLIO_STATUS.md` was committing the
conflation *in the file that is supposed to be the source of truth*: all five
projects rendered gate 4 identically to `load-alert-agent`'s genuinely
not-applicable gate 5, while the prose above them said the gates did not exist.
Two different facts, one glyph. That is the same failure that hid a skipped
Review gate for two days, rebuilt by the party who had just written the rule
against it.

### Human-checkpoint states

| Label | Class | Meaning |
|-------|-------|---------|
| `✋ approved` | `hdone` | The human approved this gate |
| **`✋ YOU / approve?`** | `hwait` | **Activated — waiting on the human right now** |
| `✋ —` | `hpend` | Not reached yet |
| `✋ n/a` | `hskip` | Gate not applicable by template — no approval owed |
| `✋ pre-gate` | `hpre` | The gate did not exist yet — no approval owed |
| **`✋ NOT ASKED`** | `hnone` | **A gate closed without the approval it owed** |

`hnone` exists because of a real event: the orchestrator skipped
little-milestones' Review gate and asked nobody. It renders in alarm red and
should be rare enough to be shocking. It is not the same as `hskip` — one is a
gate that owed no approval, the other is an approval that was owed and never
requested.

### Class definitions — copy verbatim

```
classDef done    fill:#eef6ef,stroke:#2f6f43,color:#123021
classDef active  fill:#fff8e6,stroke:#8a6410,stroke-width:2px,color:#3d2c04
classDef looped  fill:#fdf0ec,stroke:#a3341f,stroke-width:2px,color:#3d1109
classDef warn    fill:#fff8e6,stroke:#8a6410,stroke-width:2px,color:#3d2c04
classDef pending fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d
classDef skipped fill:#f4f5f7,stroke:#b8bfc9,color:#767f8d,stroke-dasharray:4 3
classDef hdone   fill:#dcefe2,stroke:#2f6f43,color:#123021
classDef hwait   fill:#ffe9a8,stroke:#8a6410,stroke-width:4px,color:#3d2c04
classDef hpend   fill:#fafbfc,stroke:#cfd5dd,color:#98a1ad,stroke-dasharray:3 3
classDef hskip   fill:#fafbfc,stroke:#cfd5dd,color:#98a1ad,stroke-dasharray:3 3
classDef hnone   fill:#f8ded7,stroke:#a3341f,stroke-width:3px,color:#3d1109
classDef rowbox  fill:none,stroke:none
```

### Row structure — copy verbatim

Three gates and their three approvals per row, wrapping. Rows are invisible
`subgraph` containers (`rowbox`), which is what produces the wrap:

```
flowchart TB
  subgraph r1 [" "]
    direction LR
    G1[...] --> H1{...} --> G2[...] --> H2{...} --> G3[...] --> H3{...}
  end
  subgraph r2 [" "]
    direction LR
    G4[...] --> H4{...} --> G5[...] --> H5{...} --> G6[...] --> H6{...}
  end
  H3 --> G4
```

---

## 3a. The graph is a mandatory control

**The graph is not a status decoration. It is a control, and it is maintained
at every step.** Three obligations, all binding:

1. **Update it at every step**, not only at gate boundaries — a gate opening, a
   gate closing, a loop-back, a re-run, an SME re-engagement, a scope change, an
   exception granted. If the state of the run changed, the graph changed.
2. **Show it at every gate**, before the approval question.
3. **Keep it true.** A graph that lags the run is worse than no graph: it
   asserts a position that is false, and it is *believed*, because it looks
   authoritative.

**A step that does not update the graph is not finished.** The graph in
`projects/<name>/PIPELINE_LOG.md` and the actual state of the run are the same
fact recorded twice; if they ever disagree, the run is not under control.

### Mandatory gate report-out

**Every gate ends with a visual report-out. This is not optional and it is not
conditional on the human asking.** A gate that closes without one has not
closed correctly.

The report-out is always these five parts, in this order:

1. **Position** — gate number and name, and whether it is running, awaiting
   approval, or blocked.
2. **The graph** — left-to-right, current state, using §3's notation and
   `classDef` block verbatim. **Publish it as an Artifact and give the link.**
   Mermaid does not render in a terminal; a graph pasted as source into a CLI
   reply is not a visual report-out, it is unreadable text pretending to be
   one. Re-publish the same file path every time so each project keeps one
   stable, bookmarkable URL across the whole run.
3. **What this gate produced** — artifacts, by path.
4. **What was skipped and why**, if anything — and `⊘ not applicable`,
   `⊘ gate did not exist`, and `⊘ skipped without exception` must be
   distinguished. They look identical in a graph and are entirely different
   facts.
5. **What is being asked** — the specific approval decision, and what happens
   on each answer.

Then, and only then, the approval question.

**Why mandatory.** The failure this prevents is not the human being uninformed
— it is the human being *asked to approve something whose position they cannot
see*. An approval given without knowing which gates were skipped to arrive
there is not informed consent, and the F18 build produced exactly that: gates
skipped, work approved, and the omission invisible until a human found seven
defects by hand on the running app.

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
- `admin/PORTFOLIO_STATUS.md` — current-state graph for every project
- `.claude/skills/project-status/SKILL.md` — `/ProjectStatus`, the on-demand
  read-only view of either one project or the whole portfolio
- `.claude/skills/new-project/SKILL.md` — the executable form of §1
