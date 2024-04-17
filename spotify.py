import requests
import argparse
from get_token import get_token
import urllib

ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search?'
REC_ENDPOINT = 'https://api.spotify.com/v1/recommendations?'

class Album:
    def __init__(self, name, artists, tracklist, tracklist_ids, artist_ids, album_id):
        self.name = name
        self.artists = artists
        self.tracklist = tracklist
        self.artist_ids = artist_ids
        self.album_id = album_id
        self.tracklist_ids = tracklist_ids

    def __repr__(self):
        return f'Artist(s): {self.artists} \nAlbum: {self.name} \nArtist IDs: {self.artist_ids}  \nTracklist: {self.tracklist} \nAlbum ID: {self.album_id}'
    
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
    
    @property
    def tracklist_ids(self):
        return self._tracklist_ids
    @tracklist_ids.setter
    def tracklist_ids(self,tracklist_ids):
        self._tracklist_ids = tracklist_ids

    def get_album(id,headers):
        r = requests.get(ALBUM_ENDPOINT+id, headers=headers)

        name = r.json()['name']
        artists = [_['name'] for _ in r.json()['artists']]
        tracklist = [_['name'] for _ in r.json()['tracks']['items']]
        tracklist_ids = [_['id'] for _ in r.json()['tracks']['items']]
        artist_ids = [_['id'] for _ in r.json()['artists']]        
        album_id = r.json()['id']

        return Album(name,artists,tracklist,tracklist_ids,artist_ids,album_id)
    
    def search_album(query,headers):
        #TODO update search to accept URI and album ID, using regex or something that Spotiy's API offers?

        limit = 10

        s_query = urllib.parse.quote_plus(f'q={query}&type=album&limit={limit}', safe="=&")
        s = requests.get(url=f'{SEARCH_ENDPOINT}{s_query}', headers=headers)
        
        return [Album.get_album(a['id'],headers) for a in s.json()['albums']['items']] #returns a list of Album objects based on search query

    def rec_albums(self,limit,headers):
        #limit min 1, default 20, max 100

        params = f"limit={limit}&seed_artists={','.join(self.artist_ids)}&seed_tracks={self.tracklist_ids[0]}" #params to be passed into the Recommendation GET Request, limit to 10 recommendations
        rec = requests.get(REC_ENDPOINT,headers=headers, params=params)
        
        return rec
"""
def main():
    boys = '2CNEkSE8TADXRT2AzcEt1b'
    neil = '70Yl2w1p00whfnC7fj94ox'

    parse = argparse.ArgumentParser()
    parse.add_argument("-c", help="-c [CLIENT_SECRET]")
    arg = parse.parse_args()
    secret = arg.c
    
    #HEADERS
    headers = {
        "Authorization" : "Bearer " + get_token.get_token(secret) #Authorization header to pass in to various end points
    }

    album = Album.get_album(neil, headers)
    search = Album.search_album(album.name,headers)
    for _ in search:
        print(_)


if __name__ == "__main__":
    main()
"""