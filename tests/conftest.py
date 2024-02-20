import pytest
from app import create_app

@pytest.fixture
def app():
    """"
    This fixture is used to get the flask application instance
    """

    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture
def client(app):
    """
    This fixture is used to get the application test client
    """
    return app.test_client()
