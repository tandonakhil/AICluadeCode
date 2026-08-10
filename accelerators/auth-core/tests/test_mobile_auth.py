"""
Mobile bearer-token transport.

The design allows the SAME session token to arrive by cookie (web) or by
`Authorization: Bearer` (native). These tests exist to prove the two
properties the design depends on:

  1. Bearer genuinely authenticates — otherwise the app doesn't work.
  2. The cookie path is bit-for-bit unchanged, and the cookie WINS on
     conflict — this is the no-regression guarantee for the web app.

Plus the two anti-footgun properties: a mobile client must be handed its
token in a header and must NOT be sent a Set-Cookie, and the token header
must never be exposed to cross-origin browser JS via CORS.

Adapted from `little-milestones/dev/backend/tests/test_mobile_auth.py`
(F18). Genericization notes: none needed -- this module tests the
transport layer, which never touches the tenant field.
"""

from __future__ import annotations

from fastapi.testclient import TestClient

from .conftest import MOBILE_HEADERS, TOKEN_HEADER, signup_mobile


def test_mobile_signup_issues_header_token_and_no_cookie(unauthenticated_client: TestClient):
    res = unauthenticated_client.post(
        "/auth/signup",
        json={"email": "hdr@example.com", "password": "correct-horse-battery-staple"},
        headers=MOBILE_HEADERS,
    )
    assert res.status_code == 201
    assert res.headers.get(TOKEN_HEADER)
    assert "set-cookie" not in {k.lower() for k in res.headers.keys()}, (
        "a native client must not be sent Set-Cookie — the device cookie jar is "
        "unencrypted and inside the default backup set"
    )


def test_web_signup_still_sets_cookie_and_no_token_header(unauthenticated_client: TestClient):
    res = unauthenticated_client.post(
        "/auth/signup",
        json={"email": "web@example.com", "password": "correct-horse-battery-staple"},
    )
    assert res.status_code == 201
    assert "set-cookie" in {k.lower() for k in res.headers.keys()}
    assert TOKEN_HEADER not in res.headers


def test_bearer_token_authenticates_a_data_route(unauthenticated_client: TestClient):
    token = signup_mobile(unauthenticated_client, "mobile@example.com")
    unauthenticated_client.cookies.clear()  # prove it is the header doing the work

    res = unauthenticated_client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200, res.text
    assert res.json()["email"] == "mobile@example.com"


def test_no_credentials_is_still_401(unauthenticated_client: TestClient):
    unauthenticated_client.cookies.clear()
    assert unauthenticated_client.get("/auth/me").status_code == 401


def test_garbage_bearer_is_401(unauthenticated_client: TestClient):
    unauthenticated_client.cookies.clear()
    res = unauthenticated_client.get(
        "/auth/me", headers={"Authorization": "Bearer not-a-real-token"}
    )
    assert res.status_code == 401


def test_malformed_authorization_header_is_401(unauthenticated_client: TestClient):
    unauthenticated_client.cookies.clear()
    for value in ("Basic abc123", "Bearer", "Bearer    ", "token abc"):
        res = unauthenticated_client.get("/auth/me", headers={"Authorization": value})
        assert res.status_code == 401, f"{value!r} should not authenticate"


def test_cookie_wins_on_conflict(unauthenticated_client: TestClient):
    """Load-bearing for the no-regression claim: when both transports are
    present, the cookie must resolve — so no browser request's outcome can
    be changed by the existence of the bearer path."""
    res_a = unauthenticated_client.post(
        "/auth/signup",
        json={"email": "cookie-user@example.com", "password": "correct-horse-battery-staple"},
    )
    assert res_a.status_code == 201

    other = TestClient(unauthenticated_client.app)
    res_b = other.post(
        "/auth/signup",
        json={"email": "bearer-user@example.com", "password": "correct-horse-battery-staple"},
        headers=MOBILE_HEADERS,
    )
    assert res_b.status_code == 201
    bearer_token = res_b.headers[TOKEN_HEADER]

    res = unauthenticated_client.get(
        "/auth/me", headers={"Authorization": f"Bearer {bearer_token}"}
    )
    assert res.status_code == 200
    assert res.json()["email"] == "cookie-user@example.com", (
        "cookie must take precedence — otherwise a bearer header could change "
        "how an existing browser request resolves"
    )


def test_logout_over_bearer_revokes_server_side(unauthenticated_client: TestClient):
    token = signup_mobile(unauthenticated_client, "logout@example.com")
    unauthenticated_client.cookies.clear()
    auth = {"Authorization": f"Bearer {token}"}

    assert unauthenticated_client.get("/auth/me", headers=auth).status_code == 200
    assert unauthenticated_client.post("/auth/logout", headers=auth).status_code in (200, 204)
    assert unauthenticated_client.get("/auth/me", headers=auth).status_code == 401, (
        "the token must be dead server-side after logout"
    )


def test_authorization_value_not_exposed_via_cors(unauthenticated_client: TestClient):
    """`X-LM-Session-Token` must never be readable by cross-origin JS.

    NOTE: this reference app does not itself mount CORSMiddleware (that is
    an adopting-project wiring concern, H2) -- this test asserts the
    invariant on the response as issued and documents it as a required
    assertion for any adopting project's own CORS configuration test, per
    ACCELERATOR.md H2 / security-architect co-sign item 8(b)."""
    res = unauthenticated_client.post(
        "/auth/signup",
        json={"email": "cors@example.com", "password": "correct-horse-battery-staple"},
        headers=MOBILE_HEADERS,
    )
    exposed = res.headers.get("access-control-expose-headers", "")
    assert TOKEN_HEADER.lower() not in exposed.lower(), (
        "exposing the session-token header to browser JS would defeat its fail-safe"
    )
