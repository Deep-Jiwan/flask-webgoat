"""Tests for /search (UI) endpoint."""


def test_search_no_query(client):
    r = client.get("/search")
    assert r.status_code == 200
    assert b"please provide" in r.data


def test_search_finds_admin(client):
    r = client.get("/search?query=admin")
    assert r.status_code == 200
    assert b"admin" in r.data


def test_search_wildcard(client):
    r = client.get("/search?query=%")
    assert r.status_code == 200


def test_search_no_results(client):
    r = client.get("/search?query=doesnotexist_xyz")
    assert r.status_code == 200
