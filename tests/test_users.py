"""Tests for /create_user endpoint."""


def test_create_user_requires_auth(client):
    r = client.post(
        "/create_user",
        data={"username": "newuser", "password": "pass", "access_level": "1"},
    )
    assert r.status_code == 200
    assert "error" in r.get_json()


def test_create_user_success(auth_client):
    r = auth_client.post(
        "/create_user",
        data={"username": "testuser", "password": "abc", "access_level": "2"},
    )
    assert r.status_code == 200
    assert r.get_json().get("success") is True


def test_create_user_short_password(auth_client):
    r = auth_client.post(
        "/create_user",
        data={"username": "u2", "password": "ab", "access_level": "2"},
    )
    assert r.status_code == 402


def test_create_user_missing_params(auth_client):
    r = auth_client.post("/create_user", data={"username": "u3"})
    assert r.status_code == 400
