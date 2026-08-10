"""Security suite — mobile bearer transport, gaps beyond test_mobile_auth.py:
expiry/revocation over bearer, MFA-over-bearer, the authz boundary re-run
over bearer, the secrets-leak sweep, and on-device storage requirements.

Adapted from `little-milestones/dev/tests/suites/security/
test_mobile_bearer_auth.py`. Condensed relative to the source (which also
covered header-gating on every issuing route and a `client` column
structural check specific to little-milestones' own session-listing UI) --
this file keeps the scenarios that test this accelerator's own `src/`
primitives directly. See ACCELERATOR.md item 5 ("floor, never a ceiling"):
an adopting project's own security suite should still author scenarios
specific to its own wiring, not treat this pack as exhaustive.
"""

from __future__ import annotations

import io
import logging
import re
from datetime import datetime, timedelta, timezone

import pyotp
from fastapi.testclient import TestClient

from .conftest import DEFAULT_PASSWORD, MOBILE_HEADERS, TOKEN_HEADER, bearer, read_text, signup_mobile

# Was a hardcoded "correct-horse-battery-staple" (hyphens) -- diverged from
# conftest.py's DEFAULT_PASSWORD ("correct horse battery staple", spaces),
# which is what signup_mobile() actually signs up with. Every TOTP-setup
# call in this file authenticates with the *wrong* password and 401s. Now
# imported from the single source of truth instead of re-typed. Caught by
# actually executing the suite, not by the STATIC ONLY review that first
# shipped it.
PASSWORD = DEFAULT_PASSWORD


# --- expiry / revocation over bearer --------------------------------------


def test_expired_token_is_401_over_bearer(unauthenticated_client: TestClient, test_db):
    token = signup_mobile(unauthenticated_client, "expiry@example.com")
    assert unauthenticated_client.get("/auth/me", headers=bearer(token)).status_code == 200

    past = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
    test_db.execute("UPDATE sessions SET expires_at = ?", (past,))
    test_db.commit()

    res = unauthenticated_client.get("/auth/me", headers=bearer(token))
    assert res.status_code == 401, res.text


def test_revoked_session_is_401_over_bearer(unauthenticated_client: TestClient):
    token = signup_mobile(unauthenticated_client, "revoke@example.com")
    sessions = unauthenticated_client.get("/auth/sessions", headers=bearer(token))
    assert sessions.status_code == 200, sessions.text
    sid = sessions.json()[0]["id"]

    revoked = unauthenticated_client.delete(f"/auth/sessions/{sid}", headers=bearer(token))
    assert revoked.status_code in (200, 204), revoked.text

    assert unauthenticated_client.get("/auth/me", headers=bearer(token)).status_code == 401


# --- ordering guarantee ------------------------------------------------------


def test_invalid_cookie_beats_valid_bearer(unauthenticated_client: TestClient):
    """The cookie is read FIRST and wins on conflict, even a stale one --
    otherwise the ordering is really 'whichever happens to work'."""
    token = signup_mobile(unauthenticated_client, "order@example.com")
    unauthenticated_client.cookies.set("session", "a-stale-cookie-value")

    res = unauthenticated_client.get("/auth/me", headers=bearer(token))
    assert res.status_code == 401, (
        "cookie must be read first and win even when it is the invalid one; "
        f"got {res.status_code}"
    )


# --- MFA over bearer ------------------------------------------------------


def _enroll_totp_over_bearer(client: TestClient, token: str) -> str:
    setup = client.post("/auth/totp/setup", json={"password": PASSWORD}, headers=bearer(token))
    assert setup.status_code == 200, setup.text
    secret = setup.json()["secret"]
    verify = client.post(
        "/auth/totp/verify", json={"code": pyotp.TOTP(secret).now()}, headers=bearer(token)
    )
    assert verify.status_code == 200, verify.text
    return secret


def test_mfa_pending_bearer_is_gated_everywhere_but_totp_login(unauthenticated_client: TestClient):
    token = signup_mobile(unauthenticated_client, "mfa@example.com")
    secret = _enroll_totp_over_bearer(unauthenticated_client, token)

    login = unauthenticated_client.post(
        "/auth/login",
        json={"email": "mfa@example.com", "password": PASSWORD},
        headers=MOBILE_HEADERS,
    )
    assert login.status_code == 200
    assert login.json().get("mfa_required") is True
    pending = login.headers.get(TOKEN_HEADER)
    assert pending, "the pending token must reach a native client via the header"

    for path in ("/auth/me", "/auth/sessions"):
        res = unauthenticated_client.get(path, headers=bearer(pending))
        assert res.status_code == 401, f"{path} reachable with a mfa_pending bearer"

    ok = unauthenticated_client.post(
        "/auth/totp/login", json={"code": pyotp.TOTP(secret).now()}, headers=bearer(pending)
    )
    assert ok.status_code == 200, ok.text
    assert unauthenticated_client.get("/auth/me", headers=bearer(pending)).status_code == 200


def test_five_failed_totp_codes_destroy_the_pending_session_over_bearer(
    unauthenticated_client: TestClient,
):
    token = signup_mobile(unauthenticated_client, "mfa5@example.com")
    _enroll_totp_over_bearer(unauthenticated_client, token)

    login = unauthenticated_client.post(
        "/auth/login",
        json={"email": "mfa5@example.com", "password": PASSWORD},
        headers=MOBILE_HEADERS,
    )
    pending = login.headers.get(TOKEN_HEADER)

    for _ in range(5):
        res = unauthenticated_client.post(
            "/auth/totp/login", json={"code": "000000"}, headers=bearer(pending)
        )
        assert res.status_code == 401

    after = unauthenticated_client.post(
        "/auth/totp/login", json={"code": "123456"}, headers=bearer(pending)
    )
    assert after.status_code == 401


# --- authz boundary re-run over bearer --------------------------------------


def test_cross_tenant_item_access_is_404_over_bearer(unauthenticated_client: TestClient):
    a = signup_mobile(unauthenticated_client, "tenant-a@example.com")
    b = signup_mobile(unauthenticated_client, "tenant-b@example.com")
    item = unauthenticated_client.post("/items", headers=bearer(a)).json()

    res = unauthenticated_client.get(f"/items/{item['id']}", headers=bearer(b))
    assert res.status_code == 404, "cross-tenant must be 404, never 403 (no existence leak)"


def test_cross_user_session_revoke_is_404_over_bearer(unauthenticated_client: TestClient):
    a = signup_mobile(unauthenticated_client, "sess-a@example.com")
    b = signup_mobile(unauthenticated_client, "sess-b@example.com")
    a_session_id = unauthenticated_client.get("/auth/sessions", headers=bearer(a)).json()[0]["id"]

    res = unauthenticated_client.delete(f"/auth/sessions/{a_session_id}", headers=bearer(b))
    assert res.status_code == 404, res.text
    assert unauthenticated_client.get("/auth/me", headers=bearer(a)).status_code == 200


# --- secrets-leak sweep -----------------------------------------------------


def test_no_token_or_authorization_value_reaches_the_logs(unauthenticated_client: TestClient):
    buf = io.StringIO()
    handler = logging.StreamHandler(buf)
    handler.setLevel(logging.DEBUG)
    root = logging.getLogger()
    root.addHandler(handler)
    prev_level = root.level
    root.setLevel(logging.DEBUG)
    try:
        token = signup_mobile(unauthenticated_client, "leak@example.com")
        secret = _enroll_totp_over_bearer(unauthenticated_client, token)
        login = unauthenticated_client.post(
            "/auth/login",
            json={"email": "leak@example.com", "password": PASSWORD},
            headers=MOBILE_HEADERS,
        )
        pending = login.headers[TOKEN_HEADER]
        unauthenticated_client.post(
            "/auth/totp/login", json={"code": pyotp.TOTP(secret).now()}, headers=bearer(pending)
        )
        unauthenticated_client.get("/auth/me", headers=bearer(pending))
        unauthenticated_client.post("/auth/logout", headers=bearer(pending))
    finally:
        root.removeHandler(handler)
        root.setLevel(prev_level)

    logged = buf.getvalue()
    assert token not in logged, "raw session token found in log output"
    assert pending not in logged, "raw pending/session token found in log output"
    assert "Bearer " not in logged, "an Authorization header value was logged"
    assert PASSWORD not in logged, "a password was logged"


# --- on-device storage (mobile source is the artifact under test) ----------


def test_token_is_never_written_to_asyncstorage(mobile_root):
    hits = []
    for path in mobile_root.rglob("*.ts*"):
        text = re.sub(r"/\*.*?\*/", "", read_text(path), flags=re.S)
        text = re.sub(r"^\s*//.*$", "", text, flags=re.M)
        if "AsyncStorage" in text:
            hits.append(path.name)
    assert not hits, f"AsyncStorage referenced in {hits}"


def test_securestore_uses_when_unlocked_this_device_only(mobile_root):
    src = read_text(mobile_root / "tokenStore.ts")
    assert "SecureStore.setItemAsync" in src
    assert "WHEN_UNLOCKED_THIS_DEVICE_ONLY" in src


def test_dev_preview_only_label_present_on_web_fallback(mobile_root):
    """The web-fallback label must survive verbatim into any vendored copy
    (security-architect co-sign item 8(c))."""
    src = read_text(mobile_root / "tokenStore.ts")
    assert "DEV PREVIEW ONLY" in src
