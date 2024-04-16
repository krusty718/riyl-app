import requests
import argparse
from get_token import get_token
import urllib

ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search?'

class Album:
    def __init__(self, name, artists, tracklist, artist_ids, album_id):
        self.name = name
        self.artists = artists
        self.tracklist = tracklist
        self.artist_ids = artist_ids
        self.album_id = album_id

    def __repr__(self):
        return f'Artist(s): {self.artists} \nAlbum: {self.name} \nArtist IDs: {self.artist_ids}  \nTracklist: {self.tracklist} \nArtist IDs: {self.artist_ids} \nAlbum ID: {self.album_id}'
    
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
    
    @property
    def album_id(self):
        return self._album_id
    @album_id.setter
    def album_id(self,album_id):
        self._album_id = album_id

    def get_album(id,headers):
        r = requests.get(ALBUM_ENDPOINT+id, headers=headers)

        name = r.json()['name']
        artists = []
        for _ in range(0,len(r.json()['artists'])):
            if len(r.json()['artists']) > 1:
                artists.append(r.json()['artists'][_]['name'])
            else:
                artists.append(r.json()['artists'][_]['name'])
        tracklist = [r.json()['tracks']['items'][_]['name'] for _ in range(0,r.json()['tracks']['total'])]
        artist_ids = [r.json()['artists'][_]['id'] for _ in range(0,len(r.json()['artists']))]
        album_id = r.json()['id']

        return Album(name,artists,tracklist,artist_ids,album_id)
    
    def search_album(query,headers):
        #TODO update search to accept URI and album ID, using regex or something that Spotiy's API offers?

        limit = 10

        s_query = urllib.parse.quote_plus(f'q={query}&type=album&limit={limit}', safe="=&")
        s = requests.get(url=f'{SEARCH_ENDPOINT}{s_query}', headers=headers)
        
        return [Album.get_album(a['id'],headers) for a in s.json()['albums']['items']] #returns a list of Album objects based on search query


def main():
    id = '2CNEkSE8TADXRT2AzcEt1b'

    parse = argparse.ArgumentParser()
    parse.add_argument("-c", help="-c [CLIENT_SECRET]")
    arg = parse.parse_args()
    secret = arg.c
    
    #HEADERS
    headers = {
        "Authorization" : "Bearer " + get_token.get_token(secret) #Authorization header to pass in to various end points
    }

    album = Album.get_album(id, headers)
    search = Album.search_album(album.name,headers)
    index = 1
    for _ in search:
        print(_)
        index += 1


if __name__ == "__main__":
    main()
