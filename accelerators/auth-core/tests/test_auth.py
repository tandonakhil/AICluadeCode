"""Core auth: signup/login/logout, cookie flags, rate limiting, unauthenticated
401s, tenant isolation, role enforcement.

Adapted from `little-milestones/dev/backend/tests/test_auth.py`. Adaptation
notes (see ACCELERATOR.md item 5, "floor never a ceiling"):
 - `family_id` -> the generic `tenant_id` (this accelerator's
   `PrincipalResolver` seam); the reference app's tenant/role vocabulary is
   `owner`/`member`, not little-milestones' `owner`/`caregiver`.
 - Tests that exercised little-milestones' own domain routes (`/profiles`,
   `/invites`) are replaced by the synthetic `/items` resource in
   `_reference_app.py`, since this accelerator must not depend on any host
   project's domain modules (H3).
 - `test_login_unknown_email_calls_verify_password` is NEW, not in the
   source pack -- added to close the gap identified by security-architect
   co-sign item 8(d): the original suite asserted the *behavioural* outcome
   of the unknown-email path (401, generic message) but never asserted the
   *mechanism* (verify_password is actually called against the dummy hash)
   that gives constant-cost enumeration resistance its guarantee.
"""

from __future__ import annotations

import sqlite3

from fastapi.testclient import TestClient

from src.auth import DUMMY_PASSWORD_HASH, check_rate_limit, reset_rate_limits


def _signup(client: TestClient, email: str, password: str = "correct horse battery staple"):
    return client.post("/auth/signup", json={"email": email, "password": password})


# --- Signup ---------------------------------------------------------------


def test_signup_creates_owner_of_a_new_tenant(unauthenticated_client: TestClient):
    resp = _signup(unauthenticated_client, "first@example.com")
    assert resp.status_code == 201
    body = resp.json()
    assert body["role"] == "owner"
    assert body["tenant_id"] is not None
    assert "password_hash" not in body
    assert unauthenticated_client.cookies.get("session") is not None


def test_signup_duplicate_email_conflict(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "dupe@example.com")
    unauthenticated_client.post("/auth/logout")
    resp = _signup(unauthenticated_client, "dupe@example.com")
    assert resp.status_code == 409


def test_signup_rejects_short_password(unauthenticated_client: TestClient):
    resp = unauthenticated_client.post(
        "/auth/signup", json={"email": "ok@example.com", "password": "short"}
    )
    assert resp.status_code == 422


def test_password_stored_only_as_argon2_hash(
    unauthenticated_client: TestClient, test_db: sqlite3.Connection
):
    _signup(unauthenticated_client, "hashed@example.com", password="correct horse battery staple")
    row = test_db.execute(
        "SELECT password_hash FROM users WHERE email = 'hashed@example.com'"
    ).fetchone()
    assert row["password_hash"] != "correct horse battery staple"
    assert row["password_hash"].startswith("$argon2")


# --- Session cookie ---------------------------------------------------------


def test_session_cookie_is_httponly_and_samesite_lax(unauthenticated_client: TestClient):
    resp = _signup(unauthenticated_client, "cookie@example.com")
    set_cookie = resp.headers.get("set-cookie", "")
    assert "HttpOnly" in set_cookie
    assert "samesite=lax" in set_cookie.lower()


def test_session_cookie_secure_flag_conditional_on_env(unauthenticated_client: TestClient, monkeypatch):
    monkeypatch.delenv("ENV", raising=False)
    resp = _signup(unauthenticated_client, "nosecure@example.com")
    assert "Secure" not in resp.headers.get("set-cookie", "")

    unauthenticated_client.post("/auth/logout")
    monkeypatch.setenv("ENV", "production")
    resp2 = _signup(unauthenticated_client, "secure@example.com")
    assert "Secure" in resp2.headers.get("set-cookie", "")
    monkeypatch.delenv("ENV", raising=False)


# --- Login / logout ---------------------------------------------------------


def test_login_success_sets_new_session(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "login@example.com", "correct horse battery staple")
    unauthenticated_client.post("/auth/logout")
    resp = unauthenticated_client.post(
        "/auth/login",
        json={"email": "login@example.com", "password": "correct horse battery staple"},
    )
    assert resp.status_code == 200
    assert unauthenticated_client.cookies.get("session") is not None


def test_login_wrong_password_generic_401(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "wrongpw@example.com", "correct horse battery staple")
    unauthenticated_client.post("/auth/logout")
    resp = unauthenticated_client.post(
        "/auth/login", json={"email": "wrongpw@example.com", "password": "totally wrong password"}
    )
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid email or password"


def test_login_unknown_email_same_generic_401(unauthenticated_client: TestClient):
    resp = unauthenticated_client.post(
        "/auth/login", json={"email": "nobody@example.com", "password": "whatever password"}
    )
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid email or password"


def test_login_unknown_email_calls_verify_password(unauthenticated_client: TestClient, monkeypatch):
    """Closes the gap named in ACCELERATOR.md / security-architect co-sign
    item 8(d): asserts the MECHANISM, not just the outcome -- an unknown
    email still runs a real argon2id verify against DUMMY_PASSWORD_HASH, so
    the response-time profile for "no such user" doesn't itself distinguish
    the two cases."""
    calls = []
    from src.auth import verify_password as real_verify

    def _spy(plain, hashed):
        calls.append(hashed)
        return real_verify(plain, hashed)

    # Patched where it is USED (the reference app's `from src.auth import
    # verify_password`), not where it is defined -- `src.auth`'s own name
    # binding is a separate reference once imported by value.
    monkeypatch.setattr("tests._reference_app.verify_password", _spy)
    unauthenticated_client.post(
        "/auth/login", json={"email": "no-such-user@example.com", "password": "whatever"}
    )
    assert calls, "verify_password was never called for an unknown email"
    assert calls[0] == DUMMY_PASSWORD_HASH


def test_login_rate_limited_after_repeated_attempts(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "ratelimited@example.com", "correct horse battery staple")
    unauthenticated_client.post("/auth/logout")
    reset_rate_limits()
    for _ in range(10):
        resp = unauthenticated_client.post(
            "/auth/login", json={"email": "ratelimited@example.com", "password": "wrong password"}
        )
        assert resp.status_code == 401
    resp = unauthenticated_client.post(
        "/auth/login", json={"email": "ratelimited@example.com", "password": "wrong password"}
    )
    assert resp.status_code == 429


def test_logout_deletes_session_row_server_side(
    unauthenticated_client: TestClient, test_db: sqlite3.Connection
):
    _signup(unauthenticated_client, "logout@example.com")
    count_before = test_db.execute("SELECT COUNT(*) AS n FROM sessions").fetchone()["n"]
    assert count_before == 1

    resp = unauthenticated_client.post("/auth/logout")
    assert resp.status_code == 200
    count_after = test_db.execute("SELECT COUNT(*) AS n FROM sessions").fetchone()["n"]
    assert count_after == 0

    # The old cookie (if replayed) must no longer authenticate.
    assert unauthenticated_client.get("/auth/me").status_code == 401


def test_logout_idempotent_with_no_session(unauthenticated_client: TestClient):
    assert unauthenticated_client.post("/auth/logout").status_code == 200


# --- Unauthenticated access ------------------------------------------------


def test_data_route_without_session_is_401(unauthenticated_client: TestClient):
    assert unauthenticated_client.get("/auth/me").status_code == 401
    assert unauthenticated_client.post("/items").status_code == 401


# --- Tenant isolation (cross-tenant 404, not 403) ---------------------------


def test_cross_tenant_item_access_is_404_not_403(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "tenantA@example.com")
    item = unauthenticated_client.post("/items").json()
    unauthenticated_client.post("/auth/logout")

    _signup(unauthenticated_client, "tenantB@example.com")
    resp = unauthenticated_client.get(f"/items/{item['id']}")
    assert resp.status_code == 404


# --- Role enforcement --------------------------------------------------------


def test_member_cannot_delete_item_owner_can(unauthenticated_client: TestClient, test_db):
    owner_resp = _signup(unauthenticated_client, "roleowner@example.com")
    tenant_id = owner_resp.json()["tenant_id"]
    item = unauthenticated_client.post("/items").json()
    unauthenticated_client.post("/auth/logout")

    unauthenticated_client.post(
        "/auth/join",
        params={"tenant_id": tenant_id},
        json={"email": "rolemember@example.com", "password": "correct horse battery staple"},
    )
    resp = unauthenticated_client.delete(f"/items/{item['id']}")
    assert resp.status_code == 403
    unauthenticated_client.post("/auth/logout")

    unauthenticated_client.post(
        "/auth/login", json={"email": "roleowner@example.com", "password": "correct horse battery staple"}
    )
    resp2 = unauthenticated_client.delete(f"/items/{item['id']}")
    assert resp2.status_code == 200


def test_rate_limit_helper_windowing():
    reset_rate_limits()
    key = "unit-test-key"
    for _ in range(5):
        assert check_rate_limit(key, max_requests=5, window_seconds=60) is True
    assert check_rate_limit(key, max_requests=5, window_seconds=60) is False
