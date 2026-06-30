"""Tests for /message, /grep_processes, /deserialized_descr endpoints."""
import base64
import pickle


def test_message_requires_auth(client):
    r = client.post("/message", data={"filename": "test", "text": "hello"})
    assert r.status_code == 200
    assert "error" in r.get_json()


def test_message_success(auth_client, tmp_path, monkeypatch):
    """Write a message file - session user_id=1 so data/1/ is created."""
    (tmp_path / "data").mkdir()
    monkeypatch.chdir(tmp_path)
    r = auth_client.post("/message", data={"filename": "note", "text": "hello world"})
    assert r.status_code == 200
    assert r.get_json().get("success") is True
    written = (tmp_path / "data" / "1" / "note.txt").read_text()
    assert written == "hello world"


def test_message_missing_filename(auth_client):
    r = auth_client.post("/message", data={"text": "hello"})
    assert r.status_code == 200
    assert "error" in r.get_json()


def test_grep_processes_returns_json(client):
    r = client.get("/grep_processes?name=python")
    assert r.status_code == 200
    assert "names" in r.get_json()


def test_deserialized_descr_success(auth_client):
    payload = base64.urlsafe_b64encode(pickle.dumps("safe_string")).decode()
    r = auth_client.post("/deserialized_descr", data={"pickled": payload})
    assert r.status_code == 200
    assert r.get_json().get("success") is True


def test_deserialized_descr_rce_reachable(auth_client):
    """Confirm insecure deserialization accepts arbitrary payloads."""
    class Harmless:
        def __reduce__(self):
            return (str, ("rce_test",))

    payload = base64.urlsafe_b64encode(pickle.dumps(Harmless())).decode()
    r = auth_client.post("/deserialized_descr", data={"pickled": payload})
    assert r.status_code == 200
    assert "rce_test" in r.get_json().get("description", "")
