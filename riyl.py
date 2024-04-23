import requests
import base64
import urllib.parse
import os
from get_token.get_token import get_token
from ascii_logo import main as ascii_img
from spotify import Album
import argparse

#Using Spotify's Client Credentials Authorization Flow
#TODO mechanism for how/what we want to seed to the recommendation engine to provide us 10 album recs
#artist, least popular track on album, most popular track on album, and audio features, e.g., 'min_valence, max_valence', and so on?
            

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

def response_debug(r):
    query = r.iter_lines(decode_unicode=True) #prints out entire Response object in readable format (optional)
    for _ in query:
        print(_,end='\n')


#################
##  APP LOGIC ###
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
            print(f"{index}. {', '.join(a.artists)} - {a.name}")
            index += 1

        try:
            r = Album.get_album(s[int(input("\nPlease choose an album from 1 to 10: ")) - 1].album_id,headers)
            
            os.system("clear")
            ascii_img()

            limit = 5
            rec = Album.rec_albums(r, limit=limit,headers=headers)

            print(f"\nRecommending based on {', '.join(r.artists)} - {r.name}\n\n")

            for i in range(0,limit):
                for _ in range(0,len(rec.json()['tracks'][i]['artists'])):
                    print(rec.json()['tracks'][i]['artists'][_]['name'], end=" - ") #prints artist(s)
                print(f"\'{rec.json()['tracks'][i]['album']['name']}\'")
                print(rec.json()['tracks'][i]['album']['external_urls']['spotify'])
                
        except KeyError:
            pass
    except ValueError:
        pass
        
if __name__ == "__main__":
    os.system("clear")
    ascii_img()
    main()
