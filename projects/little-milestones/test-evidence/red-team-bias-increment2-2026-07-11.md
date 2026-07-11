# Red-team / bias suite — Increment 2 (F8 digest, F6 timeline R1 exposure)

Owner: responsible-ai-architect. Date: 2026-07-11.
Scope per task: F8's content-only digest (`app/digest.py::build_digest`,
`GET /profiles/{id}/digest`) and F6's timeline chapter markers
(`app/timeline.py`, `GET /profiles/{id}/timeline`). F7 (photos) out of
scope — no LLM surface, verified structurally by architecture/security
suites in parallel.

Method: static code review of `digest.py`, `timeline.py`, `ages.py`,
`prompts.py`, `guardrails.py`, `milestones.py`,
`data/milestones_cdc2022.json`, `routes/digest.py`, `routes/memories.py`,
`main.py`. **No live calls were made** — see "Live-call recommendation"
at the end for why static review was judged sufficient for a verdict here,
and what's optionally left for the orchestrator to spot-check.

Reference: `knowledge/RESPONSIBLE_AI_KB.md` §3.5 (digest boundary), §5
scenario 5 (digest unattended-generation probe); `PLAN.md` §7-H items 25–27
(Increment-2 digest acceptance criteria — 28–29 explicitly excluded, they
are Increment-3 delivery scope); `PLAN.md` §7-F item 19 (timeline schema
lint).

---

## Scenario 1 — R1 framing lint on digest content, and whether `enforce()` applies

**Question:** does `build_digest`'s milestone content ever produce
"expected_by"/"on_track"/comparison language, and does it need to run
through `guardrails.py`'s `enforce()`?

**Evidence:**
- `digest.py` imports only `app.ages`, `app.milestones`, `app.profiles`,
  and `DISCLAIMER` from `app.prompts`. It imports nothing from `app.llm`
  and never constructs or sends a prompt. `routes/digest.py` confirms the
  same — no `guardrails` import, no `enforce()` call, anywhere in the
  digest path.
- Tracing every field `build_digest` can emit:
  - `age_line` — four fixed f-string templates (newborn / out-of-range /
    corrected / chronological), only numbers and the child's name
    interpolated. No comparison language in any branch.
  - `milestones` — `_framed_milestones()` renders **only** the fixed
    CDC-2022 sentence template `"Most children — at least 75% — {text} by
    {bucket_months} months."` over entries pulled verbatim from
    `data/milestones_cdc2022.json`. The JSON file's milestone `text`
    fields (all 10 buckets read in full) contain plain behavioral
    descriptions ("Rolls from tummy to back," "Says about 50 words," etc.)
    with zero instances of "behind," "delayed," "ahead," "on track,"
    "percentile," or reassurance phrasing ("don't worry," "plenty of
    kids"). There is no code path by which `_framed_milestones` can emit
    anything the curated table doesn't already contain.
  - `activities` — `fill_activity_names()` only substitutes `{name}` into
    curated `title`/`description`/`supervision_note` strings from the same
    JSON file; no other transformation.
  - `memory_prompt` — three fixed template sentences (see Scenario 4).
  - `disclaimer` — the `DISCLAIMER` constant.
- **Conclusion: `build_digest` is pure template/curated-data assembly with
  no LLM involvement at any point in its call graph.** There is no
  generative step that could originate forbidden framing — the guardrail
  question "could this drift into 'behind'/'on track' language" is
  structurally moot for this function, the same way it's moot for
  `products.py`'s catalog serving (ARCHITECTURE_KB §6.3's reasoning
  applies here too, even though that section only names F9 explicitly).
  Red-teaming it with adversarial *prompts* (as if it were a chat
  response) is not a meaningful test — there is no prompt input to this
  function at all; its only inputs are profile/date data.

**Finding — documentation drift, not a guardrail gap (flag for
solution-architect):** ARCHITECTURE_KB §6.1 states the framing check
"[runs] on the complete buffered text before being released to the client
**for non-streaming paths like `/digest`**" — as written, this describes
`guardrails.check_framing` as applying to `/digest`. It does not, in the
shipped code. Given Scenario 1's conclusion above, this is **not a
guardrail-coverage defect** (there's no generated text to check, and
running a denylist regex over already-vetted curated strings would be
inert busywork, not added safety), but the KB text overstates what the
mechanism does and should be corrected to say `/digest` content is exempt
by construction rather than implying it is covered by the same check as
`/chat`. This is a paper-trail accuracy issue for solution-architect to
fix in ARCHITECTURE_KB §6.1, not a code defect for code-agent.

**Verdict: PASS**, with the documentation-drift note above forwarded.

---

## Scenario 2 — Newborn / out-of-range digest modes (PLAN §7-H item 26)

**Fixtures traced (age-mode branches in `ages.py::compute_age`, exercised
by `build_digest`):**

| Mode | Trigger | `build_digest` behavior observed in code |
|---|---|---|
| `newborn` (effective age < 2 months) | `effective_months < 2` | `milestones = []` (no comparison at all); `activities` = the 2-month curated bucket's activities only (`get_bucket_content(2)`), i.e. "Supervised tummy time" and "Face-to-face talk time" — both already carry safe-sleep-consistent supervision notes ("Always awake and within arm's reach — never used as a sleep position"). `age_line` states "is a newborn (under 2 months)." No fabricated milestone content of any kind. |
| `out_of_range` (effective age > 36 months) | `effective_months > 36` | `milestones = []`, `activities = []`. `age_line` states plainly: "is over 36 months — little-milestones covers birth through 36 months." No extrapolated 40-month (or any) milestone content — the function returns early on this branch before reaching `get_bucket_content`. |
| `normal`, but `get_bucket_content(bucket)` returns `None` (defensive branch — should be unreachable given `CHECKLIST_BUCKETS` and the JSON table are in sync, but coded defensively) | n/a | `milestones = []`, `activities = []`, no fabrication. |

**Cross-check against PLAN §3.3's out-of-range design intent:** PLAN
states chat/activities for out-of-range should still "answer general
age-appropriate-activity questions with the limitation stated." Digest's
out-of-range branch returns zero activities rather than general
age-appropriate ones — this is **not a fabrication or framing risk**
(nothing invented), but it is a narrower behavior than `/activities`
offers for the same age mode. Flagging as a UX/product-completeness
observation, not a responsible-AI defect — out of this file's lane to
require digest to backfill general activity content; noted so it doesn't
get silently assumed to already match `/activities`' behavior.

**Verdict: PASS** on the substantive check (no extrapolated/fabricated
milestone content in either out-of-range mode) — genuinely defined-mode
content, never invented, matching PLAN §7-H item 26 exactly. Minor
completeness observation recorded above, not blocking.

---

## Scenario 3 — Timeline neutral chapter markers (F6, R1)

**Evidence (`app/timeline.py`):**
- `ChapterEntry` schema: `{entry_type: "chapter", bucket_months: int,
  label: str, anchor_date: str}`. No `expected_by`, `status`, `on_track`,
  or any expected-vs-actual field exists anywhere in the module's type
  definitions (`AgeAtMoment`, `MemoryEntry`, `ChapterEntry`) — matching
  PLAN §4.2's "hard R1 rule, enforced in the payload shape itself" and
  §7-F item 19's schema-lint requirement.
- `_passed_chapter_markers()` builds `label=f"{bucket} months"` — literally
  just the number and the word "months," e.g. `"4 months"`, `"6 months"`.
  No comparison, no percentile, no "reached"/"achieved"/"on schedule"
  wording. This matches the task's expectation exactly.
- Markers are filtered to buckets the child has **passed** by effective
  (corrected-where-applicable) age (`bucket > today_ages.effective_months:
  continue`) — this is itself a factual/chronological filter, not an
  assessment; a chapter marker's presence says "the calendar has reached
  this point," never "the child has/hasn't met this bucket's milestones."
  No milestone *content* (from `milestones_cdc2022.json`) is pulled into
  the timeline at all — chapter markers carry only the bucket number and
  an anchor date, never the actual CDC checklist text, so there's no path
  by which a milestone description could be misread as an assessment of
  that specific child.
- Sort-priority logic places a marker before a same-day memory
  (`sort_priority: markers sort before a same-day memory`), a display
  detail with no framing implication.

**Cross-check with ui-ux-designer's parallel visual check (per task):**
this file's static review confirms the **payload** carries no
comparison/assessment field or language for the UI to render; whether the
rendered UI itself avoids introducing comparison framing at the
presentation layer (e.g. color-coding markers against a "typical range,"
which the schema gives no data for anyway) is ui-ux-designer's parallel
verification, not duplicated here.

**Verdict: PASS.** Chapter markers are truly neutral labels; the R1
schema lint (PLAN §7-F item 19) is satisfied by construction, not just by
convention.

---

## Scenario 4 — Memory prompt tone check (PLAN §4.4)

**Evidence (`digest.py::_memory_prompt`):**

```
if last_memory_date is None:
    "Log {name}'s first moment to start their journey."
elif days_since >= 14:
    "It's been a while since you added a moment for {name} -- "
    "anything worth remembering from this week?"
else:
    "Anything from this week worth adding to {name}'s journey?"
```

**Tone analysis (not just factual correctness — the task specifically
asks for a guilt-trip check):**
- None of the three templates use second-person accusatory framing
  ("you haven't," "you forgot," "don't forget," "you're falling behind on
  logging"). The subject of each sentence is the *moment/journey*, not the
  parent's inaction.
- The `days_since >= 14` branch — the one most likely to carry an implicit
  "you've neglected this" undertone — is phrased as an observation about
  elapsed time ("it's been a while since you added a moment") immediately
  paired with an *invitation*, not a directive ("anything worth
  remembering... ?" is a question, not an imperative like "add a moment
  now"). This reads as closer to "no pressure, whenever you have
  something" than "you're behind on your parenting-app homework."
- No streak mechanic, no "days since last entry" counter surfaced to the
  parent, no comparison to other users' logging frequency — none of the
  engagement-guilt patterns common in habit-tracking apps are present
  here. This matches RESPONSIBLE_AI_KB §2's stated audience sensitivity
  (a sleep-deprived, possibly anxious parent) — the copy does not add a
  second, unrelated source of inadequacy on top of the milestone-anxiety
  concern this file is centrally worried about.
- Minor stylistic note, not a defect: "It's been a while" is doing real
  work to keep this soft — if a future revision changes this copy, that
  phrase (elapsed-time observation + question, never "you forgot"/"don't
  forget") is the load-bearing pattern to preserve.

**Verdict: PASS.** No guilt-tripping or failure-implying framing found in
any of the three memory-prompt branches.

---

## Cross-scenario finding: `_memory_prompt`'s date math is server-computed, not model-touched

Noted for completeness rather than as a new finding: `days_since` is a
plain `date` subtraction in `digest.py`, not an LLM computation — same
"age math is server code, never the LLM" discipline DOMAIN_KB R4 requires
elsewhere (`ages.py`) is followed here too, incidentally reinforcing that
this whole endpoint has no generative component (Scenario 1).

---

## Live-call recommendation (optional, non-blocking)

`build_digest` is a pure, deterministic function (same inputs → same
output, no I/O beyond reading the already-reviewed curated JSON), and its
full branch set (newborn / out-of-range / normal-with-content /
normal-defensive-None, plus all three `_memory_prompt` branches) was
traced exhaustively above by reading the source directly — static review
is not a weaker substitute for a live call here the way it would be for
LLM-generated chat output, since there's no model in the loop whose actual
runtime behavior could differ from what the code says it does.

**Verdict does not depend on a live call.** If the orchestrator wants a
belt-and-suspenders confirmation of wiring/schema (not of any judgment
call in this file), the following would be a reasonable spot-check, not a
blocking request:

```
curl -s http://localhost:8000/profiles/1/digest | python3 -m json.tool
curl -s http://localhost:8000/profiles/<newborn-fixture-id>/digest | python3 -m json.tool
curl -s http://localhost:8000/profiles/<out-of-range-fixture-id>/digest | python3 -m json.tool
curl -s http://localhost:8000/profiles/1/timeline | python3 -m json.tool
```
— asserting the response JSON keys match `{age_line, milestones,
activities, memory_prompt, disclaimer}` for `/digest` and that no
`/timeline` entry contains an `expected_by`/`status`/`on_track` key. If
fixture ids for a newborn (<2mo) and an out-of-range (>36mo) profile don't
already exist among ids 1–3, the orchestrator would need to create them
via `POST /profiles` first (DOB set accordingly) before this spot-check is
possible.

---

## Gate verdict

**PASS** for the Increment-2 red-team/bias suite's F8-digest and
F6-timeline scope.

- Scenario 1 (framing lint / `enforce()` applicability): PASS — digest is
  pure curated-data assembly, no LLM involvement, guardrail moot by
  construction. One documentation-drift note forwarded to
  solution-architect for ARCHITECTURE_KB §6.1 (not a code defect, not
  blocking).
- Scenario 2 (newborn/out-of-range modes): PASS — defined-mode content
  only, never fabricated/extrapolated, per PLAN §7-H item 26. One
  completeness observation (out-of-range digest omits general activities
  that `/activities` would still offer) recorded as non-blocking.
- Scenario 3 (timeline neutral markers): PASS — schema and label content
  both confirmed R1-clean.
- Scenario 4 (memory-prompt tone): PASS — no guilt-tripping framing found.

No blocking findings. Two non-blocking notes forwarded (documentation
drift in ARCHITECTURE_KB §6.1; digest out-of-range activity-completeness
observation) — neither requires code changes to pass this gate, but both
are worth a maintainer's attention at the next convenient pass.
