import pytest

from sistema import app, db


@pytest.fixture(scope='module')
def test_app():
    app.config.from_object('sistema.config.TestingConfig')
    with app.app_context():
        yield app


@pytest.fixture(scope='module')
def teste_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
