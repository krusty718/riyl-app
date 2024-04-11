from riyl import search, get_album, get_artist
from get_token import get_token

SEARCH_QUERY = "Everybody Knows This Is Nowhere"
ARTIST_ID = '6v8FB84lnmJs434UJf2Mrm'
ALBUM_ID = '70Yl2w1p00whfnC7fj94ox'
HEADERS = {
    "Authorization" : "Bearer " + get_token().json()['access_token']
    }

def test_get_token():
    assert get_token() is not None

def test_get_token_status_code():
    assert get_token().status_code == 200

def test_get_token_access_token():
    assert get_token().json()['access_token'] is not None

def test_search():
    assert search(SEARCH_QUERY,HEADERS) is not None

def test_search_status_code():
    assert search(SEARCH_QUERY,HEADERS).status_code == 200

def test_search_album_name():
    assert search(SEARCH_QUERY,HEADERS).json()['albums']['items'][0]['external_urls']['spotify'] == 'https://open.spotify.com/album/70Yl2w1p00whfnC7fj94ox'
    assert search(SEARCH_QUERY,HEADERS).json()['albums']['items'][0]['name'] == "Everybody Knows This Is Nowhere"
    assert search(SEARCH_QUERY,HEADERS).json()['albums']['items'][0]['artists'][0]['name'] == "Neil Young"
    assert search(SEARCH_QUERY,HEADERS).json()['albums']['limit'] == 10

def test_get_album():
    assert get_album(ALBUM_ID,HEADERS).status_code == 200
    assert get_album(ALBUM_ID,HEADERS).json()['name'] == "Everybody Knows This Is Nowhere"

def test_get_artist():
    assert get_artist(ARTIST_ID,HEADERS).status_code == 200
    assert get_artist(ARTIST_ID,HEADERS).json()['name'] == "Neil Young"