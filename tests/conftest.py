# import pytest

# from app import create_app, database as db
# from app.models import User
# from global_config import TestingConfig

# @pytest.fixture(scope='module')
# def test_client():
#     # Create a Flask app configured for testing
#     flask_app = create_app()
#     flask_app.config.from_object(TestingConfig)

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client  # this is where the testing happens!

import pytest

from alembic import command
from alembic.config import Config

from app import create_app, database as db
from app.models import User
from global_config import TestingConfig


@pytest.fixture(scope='session')
def app():
    # Create a Flask app configured for testing
    flask_app = create_app()
    flask_app.config.from_object(TestingConfig)

    # Create the database tables
    with flask_app.app_context():
        db.create_all()

    yield flask_app

    # Drop all the database tables after the test run
    with flask_app.app_context():
        db.drop_all()

@pytest.fixture(scope='session')
def alembic_config(app):
    # Initialize the Alembic migration engine
    alembic_cfg = Config('migrations/alembic.ini')
    alembic_cfg.set_main_option('script_location', 'migrations')
    alembic_cfg.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])
    command.upgrade(alembic_cfg, 'head')

    yield alembic_cfg

    # Tear down the Alembic migration engine
    command.downgrade(alembic_cfg, 'base')