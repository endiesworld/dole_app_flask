import pytest

from alembic import command
from alembic.config import Config
from sqlalchemy.exc import OperationalError

from app import create_app, database as db
from app.models import User
from global_config import TestingConfig


@pytest.fixture(scope='session')
def flask_app():
    # Create a Flask app configured for testing
    app = create_app(config_class=TestingConfig)
    
    # Create the database tables
    with app.app_context():
        print("CREATE DATABASE")
        db.create_all()
    
    yield app

    # Drop all the database tables after the test run
    with app.app_context():
        print("DROP DATABASE IF EXISTS_2")
        db.session.remove()
        db.drop_all()
        

# @pytest.fixture(scope='session')
# def alembic_config(flask_app):
#     # Initialize the Alembic migration engine
#     alembic_cfg = Config('migrations/alembic.ini')
#     alembic_cfg.set_main_option('script_location', 'migrations')
#     command.upgrade(alembic_cfg, 'head')
#     print("ALEMBIC Migration RAN HERE")
#     yield alembic_cfg

#     # Tear down the Alembic migration engine
#     command.downgrade(alembic_cfg, 'base')


@pytest.fixture(scope='function')
def test_client(flask_app):
    with flask_app.test_client() as client:
        # If you're using Flask-Security or a similar extension that
        # requires a user to be logged in, you can add code here to
        # log in a test user before running the tests.
        yield client


