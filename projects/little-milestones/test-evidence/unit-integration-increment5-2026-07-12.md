# Unit/Integration Test Evidence — Increment 5 (F13: chat history + dynamic suggested prompts + "Ask" rename/stage card)

Suite: Test-agent, unit/integration (blocking per default policy — no advisory
marking recorded for this suite in PROJECT_CONTEXT.md).
Run date: 2026-07-12
Verified independently against code-agent's claim of 197 backend / 53 frontend
passing.

## Suite totals (re-verified)

- Backend, `python -m pytest -v` from `dev/backend`: **197 passed**, 0 failed, 3 warnings (deprecation only, non-blocking), 5.13s.
- Backend, plain `pytest -v` from `dev/backend`: **197 passed**, 0 failed, 3 warnings, 5.15s. (Identical result under both invocations — same venv resolved either way.)
- Frontend, `npm test -- --run` from `dev/frontend`: **53 passed** (9 test files), 0 failed, 711ms.
- Claimed vs. actual: matches exactly (197/197 backend, 53/53 frontend). No discrepancy found.
- Zero-test-suite caveat: not applicable — all suites contain a nonzero, substantive test count.

---

### Scenario: /chat contract shape unchanged, session_id additive only
- Input: `test_chat_response_gains_session_id_additive_only`, `test_chat_omitting_new_session_still_works_unaffected` (dev/backend/tests/test_chat_sessions.py:40-59); disclaimer-body regression in test_smoke.py:39.
- Expected: response body keys == {text, disclaimer, session_id}; session_id is additive int; clients omitting `new_session` keep old implicit-resume behavior; disclaimer text unchanged from pre-Increment-5 constant.
- Actual: test asserts `set(body.keys()) == {"text","disclaimer","session_id"}` and `isinstance(body["session_id"], int)`; a second test confirms two sequential requests with no `new_session` field land in the same session (proving the old default path is untouched); test_smoke.py's pre-existing disclaimer-constant regression test still passes unmodified, confirming the "text"/"disclaimer" fields are unchanged in content, not just key names.
- Result: PASS
- Evidence: pytest node IDs `test_chat_sessions.py::test_chat_response_gains_session_id_additive_only`, `::test_chat_omitting_new_session_still_works_unaffected`, `test_smoke.py::test_chat_response_payload_contains_exact_disclaimer_constant` — all PASSED in both pytest invocations.

### Scenario: 4-hour boundary property test — real clock manipulation, not a hardcoded-constant check
- Input: `test_gap_over_four_hours_creates_two_sessions`, `test_gap_under_four_hours_with_no_new_session_flag_stays_one_session` (test_chat_sessions.py:77-122), calling `ChatSessionStore.resolve_or_create_session(profile_id, message, now=<explicit datetime>)` with `t0` and `t0 + timedelta(hours=CHAT_SESSION_GAP_HOURS ± delta)`.
- Expected: two writes >4h apart produce two distinct sessions; two writes <4h apart with no forced new session produce one session.
- Actual: test injects an explicit `now=` datetime parameter into the store method (an injectable-clock pattern, not `time.sleep` or a mocked `datetime.now()` monkeypatch) and asserts `created_2 is True`/`session_id_2 != session_id_1` for the >4h case, `created_2 is False`/`session_id_2 == session_id_1` for the <4h case, cross-checked against `store.list_for_profile(1)` row counts (2 vs 1). This is a genuine property test manipulating time, not an assertion that the `CHAT_SESSION_GAP_HOURS` constant merely exists.
- Result: PASS
- Evidence: both node IDs PASSED; `CHAT_SESSION_GAP_HOURS` imported from `app.chat_sessions` and used directly in the `timedelta` arithmetic (test would break if the constant's value changed, confirming it's load-bearing in the test, not decorative).

### Scenario: Snippet immutability after first message
- Input: `test_snippet_set_once_at_creation_never_recomputed` (test_chat_sessions.py:128-138) — two `/chat` POSTs to the same profile within the gap window (second message "A totally different one"), then `GET /profiles/{id}/chat_sessions`.
- Expected: snippet remains the session's first user message even after a second, different message is appended.
- Actual: test asserts `sessions[0]["snippet"] == "First question ever"` (the first message) after a second, unrelated message was sent, and `message_count == 4` (2 messages × user+assistant), confirming the snippet did not get overwritten by the later write. A sibling test also confirms 80-char truncation with `...` suffix.
- Result: PASS
- Evidence: node IDs `test_snippet_set_once_at_creation_never_recomputed`, `test_snippet_truncated_around_eighty_chars` — both PASSED.

### Scenario: Cascade-delete of chat_sessions/chat_messages on profile delete
- Input: `test_profile_delete_cascades_chat_sessions_and_messages` (test_chat_sessions.py:155-169) — create profile, send one chat message (creating a session + 2 messages), `DELETE /profiles/{id}`, then query `chat_sessions`/`chat_messages` row counts directly against the test sqlite connection.
- Expected: both tables' rows for the deleted profile are gone (FK `ON DELETE CASCADE` from §10.1's schema).
- Actual: test asserts `COUNT(*) FROM chat_sessions WHERE profile_id = ?` == 0 and `COUNT(*) FROM chat_messages` == 0 after the profile delete, querying the real sqlite connection directly (not mocked), extending the project's existing FK-cascade test pattern (§7).
- Result: PASS
- Evidence: node ID `test_profile_delete_cascades_chat_sessions_and_messages` PASSED.

### Scenario: Family-scoping — cross-family 404 (not 403) on all three new routes
- Input: `test_chat_sessions_list_route_cross_family_404`, `test_chat_session_messages_route_cross_family_404`, `test_chat_session_delete_route_cross_family_404` (test_chat_sessions.py:208-258) — family A creates a profile + chat session, logs out; family B (separate signup) attempts `GET /profiles/{id}/chat_sessions`, `GET /chat_sessions/{id}/messages`, `DELETE /chat_sessions/{id}` respectively.
- Expected: all three return 404 (not 403) for the non-owning family, per §10.8's confirmed pattern; the delete attempt must not actually delete despite returning 404.
- Actual: all three assert `status_code == 404`. The delete-route test additionally logs back in as family A afterward and confirms the session is still present (`len(still_there.json()) == 1`), proving the cross-family 404 was a genuine authz block, not an accidental successful delete disguised by a wrong status code.
- Result: PASS
- Evidence: all three node IDs PASSED.

### Scenario: Delete permission — any caregiver (not owner-only) can delete a chat session
- Input: `test_caregiver_can_delete_chat_session_not_owner_only` (test_chat_sessions.py:264-289) — owner creates a profile + chat session and an invite code, logs out; a second, non-owner caregiver joins via the invite code and attempts `DELETE /chat_sessions/{id}` while authenticated as the non-owner.
- Expected: 200 (success), per security-architect's §10.8 confirmed decision that chat-session delete is any-caregiver, not owner-only (unlike profile/photo delete which would 403 a non-owner).
- Actual: test explicitly authenticates as the joined (non-owner) caregiver via `/auth/join`, then asserts `resp.status_code == 200` on the delete — genuinely exercises the non-owner path, not just documents the intent in a comment.
- Result: PASS
- Evidence: node ID `test_caregiver_can_delete_chat_session_not_owner_only` PASSED.

### Scenario: Frontend — session resume on open
- Input: `ChatScreen.test.tsx` "resumes the most recent conversation automatically on open" (lines 156-175) — mocks `listChatSessions` to return two sessions (most-recent first) and `listChatMessages`, renders `ChatScreen`.
- Expected: on mount, the screen calls `listChatMessages` with the most-recent session's id (2, not 1) and renders that session's messages in the main chat pane.
- Actual: test asserts `listChatMessages` was called with `2` (the most-recent session id, chosen from the list's ordering, not session 1), and scopes a query to `.lm-chat-main` to confirm the resumed message bubble is actually rendered there (distinguishing it from the history rail's own snippet row which also legitimately contains the same text).
- Result: PASS
- Evidence: node ID within `ChatScreen.test.tsx` describe block "session continuity and history (§9.1)" PASSED.

### Scenario: Frontend — dynamic suggested-prompt chips sourced from server, static-pool fallback only on fetch failure
- Input: two tests (lines 113-130) — one mocks `getSuggestedPrompts` to resolve with server-provided T1/T2 prompt text; the other mocks it to reject with a network error.
- Expected: chips render the server's dynamic text when the fetch succeeds, and explicitly do NOT show the static fallback pool text ("Ideas for rainy-day play"); the static pool is used only when the fetch fails.
- Actual: success-path test asserts the server's exact prompt text renders (`"Fun ways to build strength right now"`, `"What's coming up around 12 months?"`) AND asserts `screen.queryByText("Ideas for rainy-day play")` is null (proving the static pool is NOT shown when the server call succeeds — the stronger, correct assertion, not just "chips render"). Failure-path test rejects the mock and asserts the static-pool text does appear. This is a real source-based check, not merely "some chips are on screen."
- Result: PASS
- Evidence: both node IDs (describe "dynamic suggested prompts (§9.2)") PASSED.

### Scenario: Frontend — stage card's four domain chips at equal visual weight
- Input: "renders the identity strip, elapsed-time text, and all four domain chips at equal weight" (lines 132-144).
- Expected: exactly 4 `.lm-domain-chip` elements, none carrying an additional class that would create a filled/empty visual distinction; no progress bar/ring/fill element for elapsed time (UX_KB stage-card spec: neutral, no completion-bar framing).
- Actual: test asserts `chips.length === 4` and, critically, `chip.className === "lm-domain-chip"` for every chip (i.e., no second modifier class like `.filled`/`.active` exists on any chip — this is a real equal-weight check, not just an existence check), and a sibling test asserts no `[role="progressbar"]` or `progress` element exists inside `.lm-stage-card`.
- Result: PASS
- Evidence: both node IDs (describe "stage card (§9.5)") PASSED.

### Scenario: Frontend — "Ask" rename
- Input: "labels the screen heading with 'Ask', not 'Chat'" (lines 104-110).
- Expected: screen heading reads "Ask — Emma's milestone questions" (renamed per UX_KB §9.5), not "Chat".
- Actual: test asserts `screen.getByText(/Ask — Emma's milestone questions/i)` is found — a positive assertion on the new copy (would fail if the old "Chat" heading were still present, since getByText would not match).
- Result: PASS
- Evidence: node ID PASSED.

### Scenario: next build not run against the live dev server's .next/ dir during the 3 crashed/resumed attempts
- Input: `git log -p --follow -- frontend/tsconfig.json` and `frontend/next-env.d.ts` across the full dev repo history; `git diff HEAD` and `git status` on the working tree; `git show --stat` on both Increment 5 commits (cd620b7 backend, 6e7e327 frontend).
- Expected: no diffs to `tsconfig.json`/`next-env.d.ts` from an accidental `next build` invocation against the running dev server's `.next/` directory during any of the 3 crashed/resumed attempts (a `next build` run would typically rewrite tsconfig's `include`/plugin entries or regenerate next-env.d.ts's triple-slash reference banner in a way that would show as a diff).
- Actual: `tsconfig.json`/`next-env.d.ts` have exactly one commit each in the entire dev repo history (both from the original Increment 1 scaffold, 928cc85) — zero subsequent commits touch either file, including both Increment 5 commits. `git status` on the current working tree is clean (no uncommitted changes anywhere), and `git diff HEAD` on both files is empty. `.next/` itself is gitignored, so it cannot leave a git-visible diff regardless, but the proxy files specified by the task show no evidence of a build having been run and committed/left dirty.
- Result: PASS (no evidence of the described incident)
- Evidence: `git log --oneline -20 -- frontend/tsconfig.json frontend/next-env.d.ts` → only 928cc85 and 0548e1f (the latter is the stale-age-backstop commit, unrelated to tsconfig/next-env content per its diff); `git status` → "nothing to commit, working tree clean"; `git diff HEAD -- frontend/tsconfig.json frontend/next-env.d.ts` → empty.

---

## Gaps between claimed and actual coverage

None found. code-agent's 197/53 claim is exact under both backend invocations
and the frontend invocation. Every ARCHITECTURE_KB §10.9-mandated Test-gate
item (contract test, 4-hour boundary property test, snippet immutability,
cascade-delete, family-scoping ×3, delete-permission) has a real,
specifically-targeted test — confirmed by reading test bodies, not just
names/counts. The frontend spot-check items (session-resume, dynamic-prompt
sourcing with fallback-only-on-failure, stage-card equal-weight chips,
"Ask" rename) are all genuinely exercised with assertions on the correct
underlying behavior (e.g., explicit negative assertion that the static pool
is absent on the success path, explicit className equality check for
chip-weight parity), not superficial rendering checks.

## Gate verdict

**PASS.** Backend 197/197, frontend 53/53, reproduced independently under
both `python -m pytest -v` and plain `pytest -v`. All ARCHITECTURE_KB §10.9
Test-gate ownership items are covered by genuine, specific tests. No
evidence of an accidental `next build` against the live dev `.next/` dir
during the reported crashed/resumed attempts. This suite is blocking (no
advisory marking on record for it) and it passes cleanly — no gate-stop
required from this suite. (Other suites — functional, security,
UX/accessibility, architecture conformance — are out of scope for this
report per the Test-agent's ownership boundary and should be presented
alongside this one, not merged into it.)
