import pytest
from test_spotify_api import search
import requests
from get_token import get_token

def test_get_token():
    assert get_token() is not None

def test_get_token_status_code():
    assert get_token().status_code == 200

def test_get_token_access_token():
    assert get_token().json()['access_token'] is not None

def test_search():
    assert search() is not None

def test_search_status_code():
    assert search().status_code == 200
