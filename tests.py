import pytest
from test_spotify_api import search
from get_token import get_token

SEARCH_QUERY = "Everybody Knows This Is Nowhere"

def test_get_token():
    assert get_token() is not None

def test_get_token_status_code():
    assert get_token().status_code == 200

def test_get_token_access_token():
    assert get_token().json()['access_token'] is not None

def test_search():
    assert search(SEARCH_QUERY) is not None

def test_search_status_code():
    assert search(SEARCH_QUERY).status_code == 200

def test_search_album_name():
    #tests proper return of 
    assert search(SEARCH_QUERY).json()['albums']['items'][0]['external_urls']['spotify'] == 'https://open.spotify.com/album/70Yl2w1p00whfnC7fj94ox'
    assert search(SEARCH_QUERY).json()['albums']['items'][0]['name'] == "Everybody Knows This Is Nowhere"
    assert search(SEARCH_QUERY).json()['albums']['items'][0]['artists'][0]['name'] == "Neil Young"