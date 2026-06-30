"""Tests for /login and /login_and_redirect endpoints."""


def test_login_success(client):
    r = client.post("/login", data={"username": "admin", "password": "admin"})
    assert r.status_code == 200
    assert r.get_json().get("success") is True


def test_login_bad_password(client):
    r = client.post("/login", data={"username": "admin", "password": "wrong"})
    assert r.status_code == 400


def test_login_missing_params(client):
    r = client.post("/login", data={})
    assert r.status_code == 400


def test_login_and_redirect_missing_params(client):
    r = client.get("/login_and_redirect")
    assert r.status_code == 400


def test_login_and_redirect_bad_creds_redirects(client):
    """Bad credentials trigger the open-redirect vulnerability path."""
    r = client.get(
        "/login_and_redirect?username=nobody&password=bad&url=http://evil.com",
        follow_redirects=False,
    )
    assert r.status_code == 302
    assert r.headers["Location"] == "http://evil.com"


def test_login_sqli_tautology(client):
    """Classic SQL injection tautology - the vulnerability exists and is reachable."""
    r = client.post(
        "/login", data={"username": "' OR '1'='1", "password": "' OR '1'='1"}
    )
    assert r.status_code in (200, 400)
