import requests
import base64
import random
import string

#Using Spotify's Client Credentials Authorization Flow

CLIENT_ID = '5e3b178d331d4a239bd30375ad348520'
CLIENT_SECRET = 'ab3dadd7968f4e6a823c2a7059da47c5'
REDIRECT_URI = 'http://localhost:5000/callback' 

AUTH_URL = 'https://accounts.spotify.com/authorize' #Authorize Endpoint
TOKEN_URL = 'https://accounts.spotify.com/api/token' #Token Endpoint, use POST
API_BASE_URL = 'https://api.spotify.com/v1/'

REC_ENDPOINT = 'https://api.spotify.com/v1/recommendations?'
ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'
TRACKS_ENDPOINT = 'https://api.spotify.com/v1/tracks/'
AUDIO_FEATS_ENDPOINT = 'https://api.spotify.com/v1/audio-features/'


def b64_encode(s):
    return base64.b64encode(s.encode()).decode()

def decode(s):
    return base64.b64decode(s).decode()

def get_token():
    #gets token using Spotify's Client Credentials Authorization Flow
    
    data = 'grant_type=client_credentials'
    headers = {
        'Authorization' : 'Basic ' + b64_encode(CLIENT_ID + ':' + CLIENT_SECRET),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    #POST to the TOKEN_URL
    #Using application/x-www-form-urlencoded parameters
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    return response.json()['access_token']

def authorize():
    #TODO remove or change authorization flow, right now it's Client Credentials and there's no need for a user to give authorization
    #GET to the AUTH_URL
    params = {
        'client_id' : CLIENT_ID,
        'response_type': 'code',
        'redirect_uri' : REDIRECT_URI,
        'state' : ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16)),
        'show_dialog' : False
    }

    #gets authorization code for token
    get_response = requests.get(AUTH_URL, params=params)
    print(get_response.url)

def get_album(uri, headers):
    #TODO add album input or search feature
    return requests.get(ALBUM_ENDPOINT+uri, headers=headers)

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

def search():
    #TODO create a simple search function, maybe one that takes only an album, artist or track?
    ...

def main():
    #TODO "uri" variable eventually something the get_album function returns so this isn't in main
    uri = '70Yl2w1p00whfnC7fj94ox' #using Neil Young's 'Everybody Knows This Is Nowhere" as an example
    
    headers = {
        "Authorization" : "Bearer " + get_token() #Authorization header to pass in to various end points
    }

    #GET album object, for now assuming  response status_code is 200
    #TODO only headers would be passed in here, uri is captured inside the function
    r = get_album(uri,headers)

    #TODO possibly create a get_tracklist function?
    tracklist = [r.json()['tracks']['items'][_]['id'] for _ in range(0,r.json()['tracks']['total'])] #list of tracks IDs from album
    print(tracklist)
    #TODO possibly create a get artist_id function?
    artist_id = r.json()['artists'][0]['id']
    print(artist_id)

    #TODO this maybe goes into a function that can return two track IDs from the album, the one with the lowest popularity socre and the highest
    for _ in tracklist:
       t = requests.get(TRACKS_ENDPOINT+_,headers=headers)
       #print(t.json()['popularity']) #prints popularity of each track on the album
    
    #GET track audio features
    #TODO use get_audio_features() function here, but we would need to return some kind of dict that has two values, one for the least and one for the most popular track to then be inputted into the recommendatin engine
    audio = requests.get(AUDIO_FEATS_ENDPOINT+tracklist[0],headers=headers)
    
    #seed_tracks are limited to two, should be least popular and most popular, need function to set the two and add in params
    params = f"limit={1}&seed_artists={artist_id}&seed_tracks={tracklist[0]}" #params to be passed into the Recommendation GET Request, limit to 10 recommendations
    

    #TODO mechanism for how/what we want to seed to the recommendation engine to provide us 10 album recs
    #artist, least popular track on album, most popular track on album, and audio features, e.g., 'min_valence, max_valence', and so on?
    rec = requests.get(REC_ENDPOINT,headers=headers, params=params)
    print(rec.json()['tracks'][0]['album']['external_urls']['spotify'])

if __name__ == "__main__":
    main()