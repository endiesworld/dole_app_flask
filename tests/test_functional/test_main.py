"""
This file (test_recipes.py) contains the functional tests for the `recipes` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `recipes` blueprint.
"""
from app import create_app


def test_home_page_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Dole Analytics App." in response.data
    assert b"You will have to login to Dole Analytics" in response.data
    assert b"before you can use the Dole Analytics APP." in response.data
    assert b"Thank you." in response.data

def test_home_page_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Welcome to Dole Analytics App." not in response.data
