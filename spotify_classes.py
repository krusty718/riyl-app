import requests
from get_token import get_token

ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'

class Album():
    def __init__(self, name, artists, tracklist):
        self.name = name
        self.artists = artists
        self.tracklist = tracklist
    

def get_album():
    return Album(name, artists, tracklist)

    return requests.get(ALBUM_ENDPOINT+album_id, headers=headers)
        

