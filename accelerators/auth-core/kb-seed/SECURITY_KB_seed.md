# SECURITY_KB seed — auth-core

**SEED ONLY — re-fill the criteria table against YOUR project's attributes
before treating any decision below as yours.** See `ACCELERATOR.md` item 6
for the full requirement: (a) re-derive the multi-tenancy / PII /
network-exposure / deployment-target criteria table against your own
project's actual attributes, not this one's; (b) every decision below not
re-derived from your own re-fill must carry a visible provenance tag in
your own `SECURITY_KB.md` — e.g. *"inherited from accelerators/auth-core@1.0.0,
re-confirmed applicable 2026-08-09"* — never silently deleted or presented
as freshly authored.

Adapted from `little-milestones/knowledge/SECURITY_KB.md` §1 (Authentication
& Authorization Design), §7 (F12 — Hardened auth suite), §9 (Mobile client
authn/authz design). Section numbers below refer to the source document,
kept as citations, not as a numbering scheme to preserve in your own KB.

---

## From §1 — baseline decision and reasoning shape

**Decision pattern to re-derive, not copy:** password hashing via
**argon2id** (not bcrypt — current OWASP-recommended default, no
legacy-bcrypt constraint on a greenfield project); server-side sessions as
an opaque random token (32 bytes, `secrets.token_urlsafe`), stored
**hashed** (SHA-256 — a session token isn't a password, no slow KDF
needed); cookie flags `HttpOnly` / `SameSite=Lax` / conditionally-`Secure`
(only when `ENV=production`, since local dev over plain HTTP would have the
browser silently drop a `Secure` cookie); 30-day sliding expiry capped by a
90-day absolute expiry via `min()`.

**The criteria table that reached this decision (re-fill this against your
project, do not copy these answers):**

| Criterion | little-milestones' answer (for reference only) |
|---|---|
| Multi-tenancy? | Yes — multiple caregivers per family |
| PII / sensitive data? | Yes, unusually sensitive class (a minor child's data) |
| Network exposure beyond localhost? | Yes — intended as a real deployable web app |
| Deployment target? | `local` today, but multi-user by design regardless of hosting |

Every criterion pointed toward "auth required." Your project's table may
answer differently on any row — re-run it. "No auth needed for a local MVP"
is a legitimate conclusion when the table actually supports it; it must be
reasoned to, never defaulted away from or into.

**What was deliberately NOT built in the source project, and why (re-decide
per your own threat model, don't inherit):**
- No OAuth/social login (third-party identity provider flagged as an
  unwanted data-flow for that project's specific privacy posture).
- No magic-link email (would force an email-infrastructure decision that
  project was deliberately deferring at the time).
- No password-strength meter, no breach-list check (e.g. HIBP
  k-anonymity) — left out of this accelerator itself, not just the source
  project. See `ACCELERATOR.md` item 7 for the explicit statement: a future
  adopter handling higher-value credentials should re-evaluate this per
  their own criteria table, not inherit the gap as acceptable.

**Supporting controls, generally reusable:** rate limiting on login (10
attempts / 15 min per IP+email in the source project — tune per your own
threat model); generic auth error messages (no user enumeration via
differential error messages); real server-side session-row delete on
logout (not just a client-side cookie clear).

**Explicit revisit triggers named in the source (re-state for your own
project, they will not be identical):** before any non-local deployment
(confirm `Secure`/HTTPS is actually active, not just toggled in config);
before a password-reset flow ships (needs the same token rigor as any other
high-entropy secret); if the user base or threat model changes (e.g.
monetization, third-party integration, data export); if a regulatory
determination changes.

---

## From §7 — hardened auth suite (password reset, TOTP MFA, session hardening)

**Password reset:** single-use, 30-minute-expiry token
(`secrets.token_urlsafe(32)`, SHA-256-hashed at rest — matches session-token
generation and hash reasoning exactly); one active token per user, enforced
by invalidating any outstanding token for that user in the *same call* as
the insert (never a two-live-token window); generic response (identical
status/body) for known email, unknown email, and send failure — no
enumeration via status, body, or timing; a successful reset deletes **every**
session for the user (a reset is a possible-compromise event) but does
**not** bypass or disable TOTP (an attacker with email access alone must not
be able to strip MFA — that's what recovery codes are for).

**TOTP MFA, strictly opt-in:** RFC 6238 defaults via `pyotp` (SHA-1, 6
digits, 30s step, ±1 step verification window). Secret stored Fernet-
encrypted (recoverable, unlike a password — the server must decrypt it to
verify a code); 8 recovery codes generated at enrollment, argon2id-hashed
(password-class secret, not 256-bit opaque), returned in plaintext exactly
once. **5 failed pending-session attempts destroy the pending session** —
this, not the rate limiter, is named as the primary 6-digit brute-force
control. Never forced: no owner/admin-mandates-MFA capability, per-user
opt-in only, to preserve a low-friction default.

**Session hardening:** self-scoped session listing/revocation
(`GET /sessions`, `DELETE /sessions/{id}`, `POST /sessions/revoke-others`) —
a user manages only their own sessions, cross-user access is 404 (never
403 — do not confirm another user's session even exists). Authenticated
password change deletes every *other* session but not the current one
(deliberately different from reset's delete-all: a logged-in,
password-knowing change is not itself a compromise signal).

---

## From §9 — mobile client authn/authz design

**Decision: one path, not a menu.** `Authorization: Bearer <session_token>`
as an *additional* accepted transport for the exact same session token —
same table, same hashing, same expiry, same `mfa_pending` semantics, same
revocation surface. The cookie path is read first and wins on conflict, so
no browser request's resolution can ever change.

**Rejected alternatives, and why (useful if you're tempted to re-litigate
this for your own mobile client):** letting React Native's platform HTTP
stack carry the session cookie natively (its cookie jar is unencrypted and
inside the default backup set — defeats the whole point); a second,
mobile-only token type (forks the credential model into two lifetimes, two
revocation paths, two places for MFA-pending state to be wrong, for no
threat-model difference that actually exists between web and mobile here);
full OAuth2/PKCE for login (there is no third party to delegate identity
to in a first-party app talking to its own first-party backend — PKCE
*is* correctly used elsewhere in that project, for a genuine third-party
OAuth grant, which is not the same problem).

**Token storage on device: `expo-secure-store` only. `AsyncStorage` is
prohibited, and this is a real vulnerability, not a style preference** — it
is unencrypted and is included in unencrypted device backups by default.
`WHEN_UNLOCKED_THIS_DEVICE_ONLY` keeps the token out of encrypted backups
and out of keychain sync, so a restore onto a different device means
re-login, not an inherited session.

**Client rule on any `401`:** delete the stored token and route to
sign-in once — never retry, never loop (a retry loop would collide with
your own rate limiter and lock the user out of their own account).

**A residual risk stated rather than hidden in the source:** the token
string does not rotate at the pending→full-session transition when TOTP
completes. Documented as pre-existing web behaviour that mobile does not
introduce, and as a candidate for a future hardening pass — re-evaluate
whether that's still an acceptable trade-off for your own threat model.
