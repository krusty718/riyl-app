import requests
from get_token import get_token

ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'

class Album:
    def __init__(self, name, artists, tracklist, artist_ids):
        self.name = name
        self.artists = artists
        self.tracklist = tracklist
        self.artist_ids = artist_ids

    def __repr__(self):
        return f'Artist(s): {self.artists},\nAlbum: {self.name},\nArtist IDs: {self.artist_ids}, \nTracklist: {self.tracklist}'
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
         self._name = name
    
    @property
    def artists(self):
        return self._artists
    @artists.setter
    def artists(self,artists):
         self._artists = artists
    
    @property
    def tracklist(self):
        return self._tracklist
    @tracklist.setter
    def tracklist(self,tracklist):
        self._tracklist = tracklist
    
    @property
    def artist_ids(self):
        return self._artist_ids
    @artist_ids.setter
    def artist_ids(self,artist_ids):
        self._artist_ids = artist_ids
    
    def get_album(id,headers):
        r = requests.get(ALBUM_ENDPOINT+id, headers=headers)

        name = r. json()['name']
        artists = []
        for _ in range(0,len(r.json()['artists'])):
            if len(r.json()['artists']) > 1:
                artists.append(r.json()['artists'][_]['name'])
            else:
                artists.append(r.json()['artists'][_]['name'])
        tracklist = [r.json()['tracks']['items'][_]['name'] for _ in range(0,r.json()['tracks']['total'])]
        artist_ids = [r.json()['artists'][_]['id'] for _ in range(0,len(r.json()['artists']))]

        return Album(name,artists,tracklist,artist_ids)

class Search(Album):
    ...
        

