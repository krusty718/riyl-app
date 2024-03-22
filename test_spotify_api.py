import json
import requests
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import base64
import random
import string
import os

#Using Spotify's Client Credentials Authorization Flow

CLIENT_ID = '5e3b178d331d4a239bd30375ad348520'
CLIENT_SECRET = 'ab3dadd7968f4e6a823c2a7059da47c5'
REDIRECT_URI = 'http://localhost:5000/callback' 

AUTH_URL = 'https://accounts.spotify.com/authorize' #Authorize Endpoint
TOKEN_URL = 'https://accounts.spotify.com/api/token' #Token Endpoint, use POST
API_BASE_URL = 'https://api.spotify.com/v1/'

REC_ENDPOINT = 'https://api.spotify.com/v1/recommendations'
ALBUM_ENDPOINT = 'https://api.spotify.com/v1/albums/'
TRACKS_ENDPOINT = 'https://api.spotify.com/v1/tracks'

def get_token():
    
    data = 'grant_type=client_credentials'
    headers = {
        'Authorization' : 'Basic ' + b64_encode(CLIENT_ID + ':' + CLIENT_SECRET),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    #POST to the TOKEN_URL
    #Using application/x-www-form-urlencoded parameters
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    return response.json()['access_token']

def check_rec():
    ...

def authorize():

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

def refresh_token():
    ...

def b64_encode(s):
    return base64.b64encode(s.encode()).decode()
''
def decode(s):
    return base64.b64decode(s).decode()

def main():
    uri = '70Yl2w1p00whfnC7fj94ox'
    headers = {
        "Authorization" : "Bearer " + get_token()
    }
    #GET album object
    r = requests.get(ALBUM_ENDPOINT+uri, headers=headers)
    if r.status_code == 200:
        query = r.iter_lines(decode_unicode=True)
        for _ in query:
            print(_,end='\n')
    else:
        print("error")




if __name__ == "__main__":
    main()

#http://localhost:5000/callback?code=AQAUy_9rv041scIDp8iWs_LsN-j2IGlU6ofuONbOxMJDfHhX7uUpS6vyZtPpDnVisb93ARdeCS5fFJhNF9BmNyoWU_ZJexZs_1UDVmcIHY36SFnfo3AwONLvqWjgg-uJaHS8krCk_9eV1YbC2BeJyABTqtCrcjEYmSawQ4LJq5NjDg