import pytest
from flask_webgoat import create_app


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def auth_client(client):
    """Client pre-authenticated as admin (access_level=0)."""
    client.post("/login", data={"username": "admin", "password": "admin"})
    return client
