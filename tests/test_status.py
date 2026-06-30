"""Tests for /status and /ping endpoints."""


def test_status_ok(client):
    r = client.get("/status")
    assert r.status_code == 200
    assert r.get_json() == {"success": True}


def test_ping_ok(client):
    r = client.get("/ping")
    assert r.status_code == 200
    assert r.get_json() == {"success": True}
