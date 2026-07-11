# Red-team / bias suite — little-milestones, Increment 3 (Test gate)

Owner: responsible-ai-architect. Date: 2026-07-11. Scope: PLAN §7-J item 37
("the full §7-A adversarial suite re-passes under an authenticated caregiver
session") and RESPONSIBLE_AI_KB §5's 7-scenario suite, plus a content-safety
spot check of F9 (`ProductsPanel`/`products.py`) within this file's normal
ownership.

---

## 1. Decision: does §5's 7-scenario suite need a live re-run under real
   auth, or does the pytest-level guardrail regression suffice?

**Decision: no live re-run of the 7 adversarial scenarios is warranted this
pass. The pytest-level regression (guardrail unit tests + the full existing
suite now running through `conftest.py`'s authenticated `client` fixture) is
sufficient evidence for PLAN §7-J item 37.**

Reasoning, applied explicitly rather than defaulting either direction:

- **What actually changed this increment, traced through the code, not just
  the diff summary.** I read `dev/backend/app/auth.py` and
  `dev/backend/app/routes/chat.py` directly rather than taking code-agent's
  report at face value. `get_current_family`'s *signature and return type*
  (`Family(id=...)`) are unchanged from the Increment-1 stub — only its
  *body* now resolves `family.id` from a real session-cookie lookup instead
  of a hardcoded default. Every downstream consumer (`chat.py` line 68:
  `family: Family = Depends(get_current_family)`) receives the identical
  shape it always did. Nothing in the auth layer touches `messages`
  construction, `build_system_prompt`, `model.invoke()`, `_as_text()`, or
  `enforce()` — the entire guardrail-relevant code path in `chat.py` (lines
  75–109) is unreached by anything auth changed. Auth adds a dependency
  *upstream* of profile lookup (which profile a family can see), not a
  wrapper around the request/response body the guardrail logic reads and
  writes.
- **`guardrails.py` itself is untouched this increment** (confirmed by
  reading it directly — no diff markers, matches the Increment-1 version
  referenced in the prior live-rerun report's fix commits `2d80a96` /
  `31b67c5` / `ddeeeeb`, all still present and unmodified). A live re-run
  tests the *model's* behavior under adversarial prompting — that's a
  function of the system prompt, the model weights, and `enforce()`'s
  pattern-matching, none of which auth touches. Re-running the same 7
  prompts against unchanged prompt-construction and unchanged
  post-generation checks would be re-testing a hypothesis already settled by
  the 2026-07-11 live rerun (`red-team-bias-2026-07-11-LIVE-RERUN.md`,
  6/6 PASS) — not testing anything new about *this* increment's actual
  change.
- **What auth *could* plausibly break is a different, narrower risk than
  "does the model still refuse a dosing question"**: could session
  middleware alter how the request or response body is constructed in a way
  that interferes with `enforce()`'s block-and-replace path (e.g. does the
  buffered-response trade-off in ARCHITECTURE_KB §6.1 still hold when a
  session dependency raises before the handler body runs; does a 401 ever
  fire *after* partial guardrail-checked content already started streaming)?
  That is an HTTP-integration-layer question — "is the auth wrapper
  transparent to the request/response envelope" — not a "does the model
  still say the right things" question. It is answered correctly by
  integration tests that assert on status codes, response shape, and that
  `enforce()` still runs (unit tests for `check_framing`/`check_medical`/
  `check_stale_age` plus the full existing suite exercised end-to-end
  through the authenticated `client` fixture in `conftest.py`), not by
  spending live-LLM calls re-verifying model behavior that live-testing
  already confirmed and that nothing this increment touched.
- **Where I would have called for a live re-run, for calibration**: if
  `chat.py`'s response-construction had changed (e.g. a new
  `JSONResponse`/streaming path, a new place `enforce()`'s output could be
  bypassed, or the family/session object had started flowing *into* the
  prompt or the enforce() call in some way it didn't before), that's exactly
  the "session middleware altering how request/response bodies are
  constructed" case the task description flagged as a plausible reason to
  re-run live — and I checked for it specifically. It isn't present:
  `enforce(raw_text, profile_id=profile.id)` at line 91 is byte-for-byte
  unchanged from the Increment-1 version, called with the same arguments,
  on the same `raw_text` computed the same way. There is no plausible
  interaction path from this increment's actual diff to guardrail
  enforcement behavior.
- **Cost side of the call**: live-LLM red-team runs are expensive (token
  spend, wall-clock, and per the prior report's own experience, capable of
  surfacing *unrelated* flakiness like content-block formatting that has
  nothing to do with what's under test this pass) — spending that budget to
  re-confirm an unchanged code path is not the safer default, it's a waste
  that gate discipline (test only what plausibly could have broken) argues
  against. This is not "skip because nothing changed" as a blanket rule —
  it's "skip because I checked what changed and traced it to have zero
  intersection with the mechanism under test."

**Evidence accepted as sufficient for PLAN §7-J item 37:**
- `dev/backend/tests/test_guardrails.py` — unit tests for `check_framing`,
  `check_medical`, `check_stale_age` still pass (guardrail logic itself
  unchanged and independently verified, no auth dependency in these unit
  tests at all since they call the pure functions directly).
- `dev/backend/tests/conftest.py`'s `client` fixture (read directly, lines
  38–58) — the *entire* pre-existing functional/integration suite,
  including every route that exercises `enforce()`, now runs through a
  real, non-bypassed authenticated session (`POST /auth/signup` establishes
  a real session cookie via `TestClient`'s cookie persistence, exactly as a
  browser would) rather than a mocked or stubbed auth layer. This is a
  stronger regression check than a hand-picked live re-run of 7 prompts,
  because it exercises *every* guardrail-touching code path under real
  auth, not just 7 sampled ones.
- Cross-referenced against the live rerun's own fix commits
  (`2d80a96`, `31b67c5`, `ddeeeeb`) — all three fixes are in the code I read
  today and none are in a code path auth touches.

**Not accepted as a substitute, for clarity on the boundary of this
decision**: this reasoning would *not* extend to a future increment that
changes `chat.py`'s response path, adds a new LLM-touching route, or
modifies `prompts.py`/`guardrails.py` — those would warrant a live re-run on
their own terms, unrelated to this specific auth-only diff.

---

## 2. F9 content-safety spot check (`ProductsPanel` / `products.py`)

Read `dev/backend/app/products.py` and
`dev/backend/app/data/products_catalog.json` directly (all 10 checklist
buckets, 20 items).

- **Structural confirmation** (not re-litigating what other suites already
  checked structurally): `products.py`'s module docstring and code confirm
  no import path into `app.llm`/`app.prompts` — the recommendations response
  is built entirely from `_load_catalog()`/`_load_denylist()` reading two
  static JSON files, filtered at serve time. No LLM call occurs anywhere in
  this module.
- **Content-safety pass on `why_this_age` and `safety_note` fields, all 20
  items:**
  - No comparison/ranking language ("best," "top," "#1," "better than," a
    competing product name) in any field — all `why_this_age` text is
    purely developmental-rationale phrasing ("Supports pulling to stand and
    early cruising," "Builds on the fine-motor and problem-solving skills
    from earlier stages").
  - No urgency/scarcity language ("limited time," "must-have," "don't
    miss," "before it's too late") in any field.
  - No brand names, SKUs, prices, or superlative marketing adjectives
    anywhere in the 20 items — matches PLAN §4.5's "categories, not brands"
    design and INDUSTRY_KB §2.3's contextual-only trust posture.
  - `safety_note` fields are consistently supervision/hazard-framed
    ("Supervised awake-time only," "Choose large, one-piece cups," "Always
    with a properly fitted helmet") — none contain comparative or
    persuasive framing; all read as safety instructions, not sales copy.
  - `_meta` block confirms curation ownership and last-reviewed date
    (2026-07-11) per ARCHITECTURE_KB §1.1's shared curation discipline —
    consistent with this being a maintained, reviewed data file rather than
    ad hoc content.

**Verdict: PASS.** 100% curated-catalog content, zero LLM origination
confirmed both structurally (no import path) and by direct content read (no
comparison/ranking/urgency language in any of the 20 items' `why_this_age`/
`safety_note` fields).

---

## 3. Gate verdict

**PASS — PLAN §7-J item 37 satisfied; RESPONSIBLE_AI_KB §5 suite's Increment-
3 auth-regression requirement met via pytest-level evidence, decision
reasoned explicitly above rather than defaulted; F9 content-safety spot check
clean.**

No new guardrail defect found this pass. No live-LLM re-run performed or
required — decision documented in §1 above, distinct from and not
contradicting the 2026-07-11 live rerun's own findings (still valid, since
nothing they tested has changed).

If a future increment touches `chat.py`'s response-construction path,
`prompts.py`, or `guardrails.py` itself, this file's §1 reasoning does not
carry forward automatically — re-assess at that point, not by default
either way.
