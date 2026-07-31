# Intake form — standard checklist

**The only way work enters this platform.** A free-form prompt is a *request*,
not an intake. The orchestrator's job on receiving one is to **redirect the
human to this form**, fill in what the prompt already answered, and ask only
what is still open.

Three paths. Pick one at Q0; the rest of the form branches from there.

| Path | When | Ends at |
|---|---|---|
| **A · New project** | Nothing exists yet | `/new-project` |
| **B · Enhancement** | New capability on an existing project | `/enhance-project` |
| **C · Modification** | Fix/adjust something already built | `/modify-feature` |

> **Why a form at all.** Every expensive failure this platform has had traces to
> a question nobody asked — not to a question answered wrongly. The desktop web
> went untested because nobody asked "which surfaces does this touch?"
> Deliverables went 15 days stale because nobody asked "what else describes
> this?" A form is not bureaucracy; it is the list of questions that have
> already cost us something.

---

## Q0 · Path

- [ ] **A** — new project
- [ ] **B** — enhancement to an existing project → which one? `____________`
- [ ] **C** — modification of an existing feature → which project + feature? `____________`

**If B or C**, the request is *tagged to that project* and runs its mini
pipeline. It does not become a new project. If the human is unsure whether
something is a new project or an enhancement, default to **enhancement** and
say so — a wrongly-split project is far more expensive to merge later than a
wrongly-merged one is to split.

---

# Path A · New project

## A1 · Identity

| # | Question | Why it's asked |
|---|---|---|
| A1.1 | **Project name** (slug-able) | Becomes the directory, the branch prefix, and the registry row |
| A1.2 | **One line**: what is this? | If it can't be said in one line, scope isn't settled |
| A1.3 | **Who asked for it / who owns it?** | Approval authority at every gate |

## A2 · Problem

| # | Question | Why it's asked |
|---|---|---|
| A2.1 | **What problem does this solve?** | |
| A2.2 | **For whom, specifically?** Named role, not "users" | Drives Experience Design |
| A2.3 | **What do they do today instead?** | If the honest answer is "nothing, and that's fine", stop here |
| A2.4 | **What happens if we don't build it?** | Separates a real need from an interesting idea |

## A3 · Users and context

| # | Question | Why it's asked |
|---|---|---|
| A3.1 | **Where and when is this used?** Control room, field, phone at 2am? | Context dictates the whole design |
| A3.2 | **What is the user's state of mind?** Rushed, stressed, browsing? | A tool used under pressure needs different affordances |
| A3.3 | **How many users, roughly?** | Scale and cost |

## A4 · Domain and industry *(the two unconditional Intake questions)*

| # | Question | Owner |
|---|---|---|
| A4.1 | **What functional/technical domain is this?** | `functional-agent` |
| A4.2 | **Which industry/sector?** | `industry-expert` |

Both are asked **regardless of the eventual roster** — they resolve the
ordering circularity with Team Composition and are cheap.

## A5 · Surfaces — **do not skip this one**

| # | Question | Why it's asked |
|---|---|---|
| A5.1 | **Which surfaces?** Desktop web · mobile web · native mobile · API-only · CLI · scheduled job | |
| A5.2 | **Any surface likely to be added later?** | |
| A5.3 | **If more than one: do they share a backend?** | |

> **This question exists because it was never asked.** little-milestones was
> built as a web project; a native mobile surface was added later; and a shared
> backend change then shipped to desktop web with **zero** web-side test
> coverage, because every test suite had been written `test_mobile_*`. A
> multi-surface answer here makes `solution-architect` **non-droppable** and its
> Impact Analysis mandatory. Getting A5 wrong is not a documentation error, it
> is a whole untested surface.

## A6 · Data

| # | Question | Why it's asked |
|---|---|---|
| A6.1 | **What data does this read?** Where from? | |
| A6.2 | **What does it store?** | |
| A6.3 | **Any PII, children's data, health, financial, or regulated data?** | Forces `security-architect` and often `responsible-ai-architect` onto the roster |
| A6.4 | **Retention:** how long, and who can delete it? | |

## A7 · AI behaviour *(if the system generates or decides anything)*

| # | Question | Why it's asked |
|---|---|---|
| A7.1 | **What must it never say or do?** | Becomes `responsible-ai-architect`'s guardrails and the red-team suite |
| A7.2 | **What is the worst plausible harm if it's confidently wrong?** | |
| A7.3 | **Must any output be grounded/cited rather than generated?** | |
| A7.4 | **Who is accountable for an answer a user acts on?** | |

> A7.2 is the highest-yield question on this form. On `outage-comms-assistant`
> it produced "a call-centre agent repeats an invented restoration time to a
> household with a medical device" — which shaped the architecture, the
> guardrails, and two test suites.

## A8 · Success and scope

| # | Question | Why it's asked |
|---|---|---|
| A8.1 | **How will we know it worked?** Observable, not "users are happy" | Seeds the acceptance criteria at Functional Design |
| A8.2 | **What is explicitly OUT of scope?** | The most-skipped and most-valuable line on the form |
| A8.3 | **What's the smallest useful version?** | MVP scope at Plan & Backlog |

## A9 · Constraints

| # | Question |
|---|---|
| A9.1 | **Deadline?** Real or preferred? |
| A9.2 | **Token/cost budget?** (`usage-monitor` enforces softly) |
| A9.3 | **Compliance or audit obligations?** |
| A9.4 | **Anything that must be reused** — existing auth, data store, design system? |

## A10 · Template

| # | Question |
|---|---|
| A10.1 | `genai-chatbot` · `agentic-workflow` · `rag-knowledge-base` · custom |
| A10.2 | If genuinely ambiguous between two — **say so and ask**, don't guess |

---

# Path B · Enhancement to an existing project

Shorter, because the project's context already exists. **Do not re-ask what
`PROJECT_CONTEXT.md` already answers** — read it first.

| # | Question | Why it's asked |
|---|---|---|
| B1 | **Which project?** | |
| B2 | **Feature name** (slug-able) | Becomes `feature/<date>-<slug>` |
| B3 | **What changes observably for the user?** | If nothing does, this is refactoring, not a feature |
| B4 | **Which surfaces does it touch?** Which does it NOT, and why? | Seeds the mandatory Impact Analysis |
| B5 | **Does it touch data, auth, or stored state?** | Pulls in `security-architect` |
| B6 | **Does it change what the AI says or decides?** | Pulls in `responsible-ai-architect` |
| B7 | **Any dropped SME to re-engage?** | The re-engagement decision, made explicitly |
| B8 | **How will we know it worked?** | Acceptance criteria |
| B9 | **What is out of scope for this enhancement?** | Prevents mid-flight scope growth — and if scope grows anyway, the route is redrawn |

---

# Path C · Modification of an existing feature

| # | Question |
|---|---|
| C1 | **Which project, which `FEATURES.md` entry?** |
| C2 | **What is wrong, or what needs adjusting?** |
| C3 | **Is the feature's branch still open, or already merged?** (reuse vs. `fix/<date>-<slug>`) |
| C4 | **Is this a defect, or a change of mind?** Both are fine; they route differently |
| C5 | **Which acceptance criteria change?** If none, why is the behaviour changing? |
| C6 | **How did this escape?** Which gate should have caught it? |

> **C6 is mandatory and its answer goes to `admin/LESSONS.md`.** Seven of eight
> defects on little-milestones were found by the human on the running app. A
> modification that doesn't ask which gate missed it guarantees the next one
> escapes the same way.

---

# Research-derived options

When discovery, research, or an SME produces **options** rather than an answer
— three possible approaches, two candidate integrations, several features an
industry scan suggests — **each option enters through this form as its own
candidate.** They are not implicitly chosen, bundled, or carried into Plan as
settled.

Procedure:

1. List every option surfaced. Do not pre-filter to a favourite.
2. For each, answer the **minimum viable intake**: what problem it solves
   (A2.1), which surfaces it touches (A5.1), and what's out of scope (A8.2).
3. Present them to the human as **per-option checkboxes** — never bundled into
   one accept/reject.
4. Only selected options proceed. Rejected ones are recorded with their reason
   in `PROJECT_CONTEXT.md`'s Decisions Log, so they are not silently
   re-proposed later.

> **Why.** An option that arrives inside a research summary and is never
> explicitly chosen still ends up built — it just never got scoped, costed, or
> approved. Research output is input to intake, never a substitute for it.

---

# Orchestrator obligations

1. **Never start a build from a free-form prompt.** Redirect to this form.
2. **Pre-fill it.** The prompt usually answers several questions already —
   fill those in, show the human what was inferred, and ask only what's open.
   A form that re-asks what was just said is the fastest way to make people
   stop using it.
3. **Ask the open questions ONE AT A TIME, in the console.** One question per
   turn — never two in a message, never a form or page to collect them unless
   the human asks for one. Use checkboxes where the answer is a choice; a
   multiSelect `AskUserQuestion` is still one question.
4. **A5 (surfaces) and A7.2 (worst plausible harm) are never skipped.** Both
   have already cost this platform real defects.
5. **Record the completed form** at `projects/<name>/INTAKE.md` for path A, or
   append it to the `FEATURES.md` entry for paths B and C. It is the record of
   what was asked and what was answered — including the questions whose answer
   was "we don't know yet," which are themselves findings.
6. **An unanswered mandatory question blocks the Intake gate.** "We'll figure
   it out later" is an acceptable *answer* — it is recorded as such and becomes
   a known risk. It is not acceptable to leave the question unasked.
