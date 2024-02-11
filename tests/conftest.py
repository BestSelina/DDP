import pytest
from app import app as flask_app


@pytest.fixture
def app():
    print("111")
    yield flask_app


@pytest.fixture
def client(app):
    print("222")
    return app.test_client()

@pytest.fixture()
def runner(app):
    print("333")
    return app.test_cli_runner()