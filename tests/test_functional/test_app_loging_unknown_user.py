import pytest
from flask import session

from app import database as db
from app.models import User


@pytest.fixture(scope='class')
def setup(flask_app):
    def do_teardown():
        with flask_app.app_context():
            db.session.query(User).delete()
            db.session.commit()
            
    def do_setup():
        with flask_app.app_context():
            user = User(username="emmanuel", email="endiesworld@gmail.com")
            user.set_password("password")
            db.session.add(user)
            db.session.commit()
            
    do_teardown()
    yield do_setup()
    do_teardown()


class TestAllLoginOptions:
    
    # Test GET request to login page
    def test_login_route(self, test_client):
        response =test_client.get('/login')
        
        assert response.status_code == 200
        assert b'Sign In' in response.data
        assert b'New User?' in response.data
        assert b'Click to Sign up' in response.data

    # Test invalid login
    def test_invalid_login(self, test_client):
        response =test_client.post(('/login'), data={
            'username': 'invalid_username',
            'password': 'invalid_password',
            'remember_me': False
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Invalid username or password' in response.data
        assert b'New User?' in response.data
        assert b'Click to Sign up' in response.data

    # Test valid login
    def test_valid_login(self, test_client, setup):
        response =test_client.post(('/login'), data={
            'username': 'emmanuel',
            'password': 'password',
            'remember_me': True
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Hello, emmanuel!' in response.data
        assert b'Welcome to Dole Analytics App.' in response.data
        