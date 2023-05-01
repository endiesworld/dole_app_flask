"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from app.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    user = User(username='emmanuel', email='endiesworld@gmail.com')
    user.set_password('emmanuelokoro')
    assert user.email == 'endiesworld@gmail.com'
    assert user.password != 'emmanuelokoro'
    assert user.__repr__() == '<User: emmanuel>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous
