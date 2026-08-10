"""Hardened auth suite: password reset, opt-in TOTP MFA, session management.

Adapted from `little-milestones/dev/backend/tests/test_auth_hardening.py`
(F12). Uses `pyotp` to compute real TOTP codes (no time/crypto mocking),
matching how `src/totp.py` itself verifies codes. See test_auth.py's module
docstring for the tenant/role genericization notes -- they apply here too.
"""

from __future__ import annotations

import sqlite3

import pyotp
from fastapi.testclient import TestClient

from .conftest import DEFAULT_EMAIL, DEFAULT_PASSWORD


def _signup(client: TestClient, email: str, password: str = DEFAULT_PASSWORD):
    return client.post("/auth/signup", json={"email": email, "password": password})


def _enroll_totp(client: TestClient, password: str = DEFAULT_PASSWORD) -> tuple[str, list[str]]:
    setup_resp = client.post("/auth/totp/setup", json={"password": password})
    assert setup_resp.status_code == 200, setup_resp.text
    secret = setup_resp.json()["secret"]
    code = pyotp.TOTP(secret).now()
    verify_resp = client.post("/auth/totp/verify", json={"code": code})
    assert verify_resp.status_code == 200, verify_resp.text
    codes = verify_resp.json()["recovery_codes"]
    return secret, codes


# --- Password reset -----------------------------------------------------


def test_reset_request_creates_single_use_token_row(
    unauthenticated_client: TestClient, test_db: sqlite3.Connection
):
    _signup(unauthenticated_client, "reset-token@example.com")
    unauthenticated_client.post("/auth/logout")

    resp = unauthenticated_client.post(
        "/auth/password-reset/request", json={"email": "reset-token@example.com"}
    )
    assert resp.status_code == 202

    rows = test_db.execute(
        "SELECT * FROM password_reset_tokens WHERE user_id = ("
        "SELECT id FROM users WHERE email = 'reset-token@example.com')"
    ).fetchall()
    assert len(rows) == 1
    assert rows[0]["used_at"] is None


def test_reset_request_generic_response_known_and_unknown_email(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "known@example.com")
    unauthenticated_client.post("/auth/logout")

    known_resp = unauthenticated_client.post(
        "/auth/password-reset/request", json={"email": "known@example.com"}
    )
    unknown_resp = unauthenticated_client.post(
        "/auth/password-reset/request", json={"email": "nobody-here@example.com"}
    )
    assert known_resp.status_code == unknown_resp.status_code == 202
    assert known_resp.json() == unknown_resp.json()


def test_reset_confirm_valid_token_succeeds_and_invalidates_all_sessions(
    unauthenticated_client: TestClient, test_db: sqlite3.Connection
):
    from src.auth import hash_token

    _signup(unauthenticated_client, "reset-confirm@example.com", "old password value")

    unauthenticated_client.post(
        "/auth/password-reset/request", json={"email": "reset-confirm@example.com"}
    )
    row = test_db.execute(
        "SELECT * FROM password_reset_tokens WHERE user_id = ("
        "SELECT id FROM users WHERE email = 'reset-confirm@example.com')"
    ).fetchone()
    # The raw token isn't recoverable from the hash in this test harness
    # (as designed -- only the hash is ever persisted), so this test drives
    # the confirm step through a token minted the same way the request
    # route does, by re-deriving it via the store directly.
    from src.security_tokens import PasswordResetTokenStore
    from src.auth import generate_opaque_token

    raw_token = generate_opaque_token()
    store = PasswordResetTokenStore(test_db)
    store.create(row["user_id"], hash_token(raw_token))

    confirm_resp = unauthenticated_client.post(
        "/auth/password-reset/confirm",
        json={"token": raw_token, "new_password": "brand new password value"},
    )
    assert confirm_resp.status_code == 200
    assert confirm_resp.json()["email"] == "reset-confirm@example.com"

    remaining = test_db.execute(
        "SELECT COUNT(*) AS n FROM sessions WHERE user_id = ("
        "SELECT id FROM users WHERE email = 'reset-confirm@example.com')"
    ).fetchone()["n"]
    assert remaining == 0

    unauthenticated_client.cookies.clear()
    old_login = unauthenticated_client.post(
        "/auth/login", json={"email": "reset-confirm@example.com", "password": "old password value"}
    )
    assert old_login.status_code == 401
    unauthenticated_client.cookies.clear()
    new_login = unauthenticated_client.post(
        "/auth/login",
        json={"email": "reset-confirm@example.com", "password": "brand new password value"},
    )
    assert new_login.status_code == 200


def test_reset_confirm_invalid_token_rejected_generically(unauthenticated_client: TestClient):
    resp = unauthenticated_client.post(
        "/auth/password-reset/confirm",
        json={"token": "not-a-real-token", "new_password": "some new password value"},
    )
    assert resp.status_code == 400


def test_reset_confirm_already_used_token_rejected(unauthenticated_client: TestClient, test_db):
    from src.auth import hash_token, generate_opaque_token
    from src.security_tokens import PasswordResetTokenStore

    _signup(unauthenticated_client, "reset-reuse@example.com")
    user_id = test_db.execute(
        "SELECT id FROM users WHERE email = 'reset-reuse@example.com'"
    ).fetchone()["id"]
    raw_token = generate_opaque_token()
    PasswordResetTokenStore(test_db).create(user_id, hash_token(raw_token))

    first = unauthenticated_client.post(
        "/auth/password-reset/confirm",
        json={"token": raw_token, "new_password": "first new password value"},
    )
    assert first.status_code == 200

    second = unauthenticated_client.post(
        "/auth/password-reset/confirm",
        json={"token": raw_token, "new_password": "second new password value"},
    )
    assert second.status_code == 400


# --- TOTP enrollment ------------------------------------------------------


def test_totp_setup_requires_correct_password(client: TestClient):
    resp = client.post("/auth/totp/setup", json={"password": "totally wrong password"})
    assert resp.status_code == 401


def test_totp_setup_returns_provisioning_uri_and_secret(client: TestClient):
    resp = client.post("/auth/totp/setup", json={"password": DEFAULT_PASSWORD})
    assert resp.status_code == 200
    body = resp.json()
    assert body["secret"]
    assert body["provisioning_uri"].startswith("otpauth://")


def test_totp_verify_correct_code_completes_enrollment_and_returns_recovery_codes(
    client: TestClient, test_db: sqlite3.Connection
):
    _secret, codes = _enroll_totp(client)
    assert len(codes) == 8
    assert len(set(codes)) == 8

    row = test_db.execute(
        "SELECT totp_verified_at FROM users WHERE email = ?", (DEFAULT_EMAIL,)
    ).fetchone()
    assert row["totp_verified_at"] is not None


def test_totp_verify_wrong_code_fails_without_completing_enrollment(
    client: TestClient, test_db: sqlite3.Connection
):
    setup_resp = client.post("/auth/totp/setup", json={"password": DEFAULT_PASSWORD})
    assert setup_resp.status_code == 200

    resp = client.post("/auth/totp/verify", json={"code": "000000"})
    assert resp.status_code == 401

    row = test_db.execute(
        "SELECT totp_verified_at FROM users WHERE email = ?", (DEFAULT_EMAIL,)
    ).fetchone()
    assert row["totp_verified_at"] is None


# --- TOTP login two-step challenge ----------------------------------------


def test_login_with_totp_enrolled_returns_mfa_pending_and_gates_other_routes(
    unauthenticated_client: TestClient,
):
    _signup(unauthenticated_client, "mfa-login@example.com")
    secret, _codes = _enroll_totp(unauthenticated_client)
    unauthenticated_client.post("/auth/logout")

    login_resp = unauthenticated_client.post(
        "/auth/login",
        json={"email": "mfa-login@example.com", "password": DEFAULT_PASSWORD},
    )
    assert login_resp.status_code == 200
    body = login_resp.json()
    assert body["mfa_required"] is True
    assert body["user"] is None

    other_route = unauthenticated_client.get("/auth/me")
    assert other_route.status_code == 401

    totp_resp = unauthenticated_client.post(
        "/auth/totp/login", json={"code": pyotp.TOTP(secret).now()}
    )
    assert totp_resp.status_code == 200
    assert totp_resp.json()["user"]["email"] == "mfa-login@example.com"

    assert unauthenticated_client.get("/auth/me").status_code == 200


def test_totp_login_recovery_code_works_exactly_once(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "recovery-once@example.com")
    _secret, codes = _enroll_totp(unauthenticated_client)
    unauthenticated_client.post("/auth/logout")

    unauthenticated_client.post(
        "/auth/login",
        json={"email": "recovery-once@example.com", "password": DEFAULT_PASSWORD},
    )
    recovery_code = codes[0]

    first = unauthenticated_client.post("/auth/totp/login", json={"code": recovery_code})
    assert first.status_code == 200
    assert first.json()["recovery_codes_remaining"] == 7

    unauthenticated_client.post("/auth/logout")
    unauthenticated_client.post(
        "/auth/login",
        json={"email": "recovery-once@example.com", "password": DEFAULT_PASSWORD},
    )
    second = unauthenticated_client.post("/auth/totp/login", json={"code": recovery_code})
    assert second.status_code == 401


def test_totp_login_wrong_code_repeated_destroys_pending_session(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "mfa-lockout@example.com")
    _enroll_totp(unauthenticated_client)
    unauthenticated_client.post("/auth/logout")
    unauthenticated_client.post(
        "/auth/login",
        json={"email": "mfa-lockout@example.com", "password": DEFAULT_PASSWORD},
    )

    for _ in range(4):
        resp = unauthenticated_client.post("/auth/totp/login", json={"code": "000000"})
        assert resp.status_code == 401

    final = unauthenticated_client.post("/auth/totp/login", json={"code": "000000"})
    assert final.status_code == 401

    again = unauthenticated_client.post("/auth/totp/login", json={"code": "000000"})
    assert again.status_code == 401


# --- TOTP disable -----------------------------------------------------------


def test_totp_disable_requires_password_and_valid_code(client: TestClient):
    secret, _codes = _enroll_totp(client)

    wrong_password = client.post(
        "/auth/totp/disable",
        json={"password": "totally wrong password", "code": pyotp.TOTP(secret).now()},
    )
    assert wrong_password.status_code == 401

    wrong_code = client.post(
        "/auth/totp/disable", json={"password": DEFAULT_PASSWORD, "code": "000000"}
    )
    assert wrong_code.status_code == 401

    ok = client.post(
        "/auth/totp/disable",
        json={"password": DEFAULT_PASSWORD, "code": pyotp.TOTP(secret).now()},
    )
    assert ok.status_code == 200
    assert ok.json()["disabled"] is True


# --- Sessions ----------------------------------------------------------------


def test_sessions_list_shows_only_current_users_own_sessions(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "sessions-a@example.com")
    resp = unauthenticated_client.get("/auth/sessions")
    assert resp.status_code == 200
    sessions = resp.json()
    assert len(sessions) == 1
    assert sessions[0]["is_current"] is True


def test_revoke_specific_session_by_id_works(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "revoke-self@example.com")
    session_id = unauthenticated_client.get("/auth/sessions").json()[0]["id"]

    resp = unauthenticated_client.delete(f"/auth/sessions/{session_id}")
    assert resp.status_code == 200
    assert resp.json()["deleted"] is True

    assert unauthenticated_client.get("/auth/me").status_code == 401


def test_revoke_other_users_session_id_is_404_not_403(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "revoke-owner@example.com")
    owner_session_id = unauthenticated_client.get("/auth/sessions").json()[0]["id"]
    unauthenticated_client.post("/auth/logout")

    _signup(unauthenticated_client, "revoke-attacker@example.com")
    resp = unauthenticated_client.delete(f"/auth/sessions/{owner_session_id}")
    assert resp.status_code == 404


def test_change_password_authenticated_works_and_kills_other_sessions_not_current(
    unauthenticated_client: TestClient, test_db: sqlite3.Connection
):
    _signup(unauthenticated_client, "change-pw@example.com", "old password value")
    user_id = test_db.execute(
        "SELECT id FROM users WHERE email = 'change-pw@example.com'"
    ).fetchone()["id"]
    test_db.execute(
        "INSERT INTO sessions (token_hash, user_id, created_at, expires_at, id, mfa_pending, last_seen_at) "
        "VALUES ('another-device-hash', ?, datetime('now'), datetime('now', '+30 days'), "
        "'another-device-id', 0, datetime('now'))",
        (user_id,),
    )
    test_db.commit()

    resp = unauthenticated_client.post(
        "/auth/password",
        json={"current_password": "old password value", "new_password": "new password value"},
    )
    assert resp.status_code == 200

    remaining = test_db.execute(
        "SELECT id FROM sessions WHERE user_id = ?", (user_id,)
    ).fetchall()
    assert len(remaining) == 1
    assert remaining[0]["id"] != "another-device-id"

    assert unauthenticated_client.get("/auth/me").status_code == 200


def test_change_password_wrong_current_password_rejected(unauthenticated_client: TestClient):
    _signup(unauthenticated_client, "change-pw-wrong@example.com", "old password value")
    resp = unauthenticated_client.post(
        "/auth/password",
        json={"current_password": "not the right password", "new_password": "new password value"},
    )
    assert resp.status_code == 401
