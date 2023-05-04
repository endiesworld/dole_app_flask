import pytest

from app import create_app, database as db
from app.models import User
from global_config import TestingConfig


@pytest.fixture(scope='session')
def flask_app():
    # Create a Flask app configured for testing
    app = create_app(config_class=TestingConfig)
    
    # Create the database tables
    with app.app_context():
        print("******** CREATED DATABASE ********")
        db.create_all()
    
    yield app

    # Drop all the database tables after the test run
    with app.app_context():
        print("******** DROP DATABASE IF EXISTS_2 ********")
        db.session.remove()
        db.drop_all()
        

@pytest.fixture(scope='session')
def test_client_2(flask_app):
    with flask_app.app_context():
        user = User(username="emmanuel", email="endiesworld@gmail.com")
        user.set_password("password")
        db.session.add(user)
        db.session.commit()
        
@pytest.fixture(scope='function')
def test_client(flask_app):
    with flask_app.test_client() as client:
       
        yield client


