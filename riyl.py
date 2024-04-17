import requests
import base64
import urllib.parse
import os
from get_token.get_token import get_token
from ascii_logo import main as ascii_img
from spotify import Album
import argparse

#Using Spotify's Client Credentials Authorization Flow

REDIRECT_URI = 'http://localhost:5000/callback' 

AUTH_URL = 'https://accounts.spotify.com/authorize' #Authorize Endpoint
API_BASE_URL = 'https://api.spotify.com/v1/'

REC_ENDPOINT = 'https://api.spotify.com/v1/recommendations?'
ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'
ARTIST_ENDPOINT = 'https://api.spotify.com/v1/artists/'
TRACKS_ENDPOINT = 'https://api.spotify.com/v1/tracks/'
AUDIO_FEATS_ENDPOINT = 'https://api.spotify.com/v1/audio-features/'
SEARCH_ENDPOINT = 'https://api.spotify.com/v1/search?'

#######################
## HELPER FUNCTIONS ###
#######################
def b64_encode(s):
    return base64.b64encode(s.encode()).decode()

def decode(s):
    return base64.b64decode(s).decode()

def get_album(album_id, headers):
    return requests.get(ALBUM_ENDPOINT+album_id, headers=headers)

def get_artist(artist_id, headers):
    return requests.get(ARTIST_ENDPOINT+artist_id, headers=headers)

def get_track():
    #TODO function gets track using TRACKS_ENDPOINT, instead of putting this in main
    ...

def get_audio_features():
    #TODO function gets audio features from a track using AUDIO_FEATS_ENDPOINT, instead of putting this in main
    ...

def response_debug(r):
    query = r.iter_lines(decode_unicode=True) #prints out entire Response object in readable format (optional)
    for _ in query:
        print(_,end='\n')

def search(query,headers):
    #TODO update search to accept URI and album ID, using regex or something that Spotiy's API offers?

    limit = 10
    s_query = urllib.parse.quote_plus(f'q={query}&type=album&limit={limit}', safe="=&")
    r = requests.get(url=f'{SEARCH_ENDPOINT}{s_query}', headers=headers)
    return r

def rec_albums(limit, artist_id, tracklist):
    ...

#################
##  APP LOGIC ##
#################

def main():

    parse = argparse.ArgumentParser()
    parse.add_argument("-c", help="-c [CLIENT_SECRET]")
    arg = parse.parse_args()
    secret = arg.c
    
    #HEADERS
    headers = {
        "Authorization" : "Bearer " + get_token(secret) #Authorization header to pass in to various end points
    }
    
    try:
        s = Album.search_album(input("Enter an album name: "),headers) #Accept an album title, can also accept artist and album title or whatever Spotify's Search API can accept

        os.system("clear")
        ascii_img()

        index = 1
        for a in s:
            print(f"{index}. {a.artists} - {a.name}")
            index += 1

        
        try:
            r = Album.get_album(s[int(input("\nPlease choose an album from 1 to 10: ")) - 1].album_id,headers)

            limit = 5
            #seed_tracks are limited to two, should be least popular and most popular, need function to set the two and add in params
            params = f"limit={limit}&seed_artists={[id for id in r.artist_ids]}&seed_tracks={r.tracklist[0]}" #params to be passed into the Recommendation GET Request, limit to 10 recommendations

            #TODO mechanism for how/what we want to seed to the recommendation engine to provide us 10 album recs
            #artist, least popular track on album, most popular track on album, and audio features, e.g., 'min_valence, max_valence', and so on?
            
            os.system("clear")
            ascii_img()

            print(r)
            
            rec = requests.get(REC_ENDPOINT,headers=headers, params=params)
            print(rec.status_code)
            print(f"\nRecommending based on {r.artists} - {r.name}\n\n")
            for i in range(0,limit):
                for _ in range(0,len(rec.json()['tracks'][i]['artists'])):
                    print(rec.json()['tracks'][i]['artists'][_]['name'], end=" - ") #prints artist(s)
                print(f"\'{rec.json()['tracks'][i]['album']['name']}\'")
                print(rec.json()['tracks'][i]['album']['external_urls']['spotify'])
        except KeyError:
            pass
    except ValueError:
        pass

        
    """
    #l = [a['artists'][b]['name'] for a in searched_albums for b in range(0,len(a['artists']))]
    #d = [a['name'] for a in searched_albums for b in range(0,len(a['artists']))]

    #TODO this maybe goes into a function that can return two track IDs from the album, the one with the lowest popularity score and the highest
    for _ in tracklist:
       t = requests.get(TRACKS_ENDPOINT+_,headers=headers)
       #print(t.json()['popularity']) #prints popularity of each track on the album
    
    #GET track audio features
    #TODO use get_audio_features() function here, but we would need to return some kind of dict that has two values, one for the least and one for the most popular track to then be inputted into the recommendatin engine
    audio = requests.get(AUDIO_FEATS_ENDPOINT+tracklist[0],headers=headers)
    """
        
if __name__ == "__main__":
    os.system("clear")
    ascii_img()
    main()
