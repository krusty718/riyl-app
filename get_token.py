import requests
import base64

CLIENT_ID = '5e3b178d331d4a239bd30375ad348520'
CLIENT_SECRET = 'ab3dadd7968f4e6a823c2a7059da47c5'
TOKEN_URL = 'https://accounts.spotify.com/api/token'

def b64_encode(s):
    return base64.b64encode(s.encode()).decode()

def decode(s):
    return base64.b64decode(s).decode()

#gets token using Spotify's Client Credentials Authorization Flow
def get_token():

    data = 'grant_type=client_credentials'
    headers = {
        'Authorization' : 'Basic ' + b64_encode(CLIENT_ID + ':' + CLIENT_SECRET),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    #POST to the TOKEN_URL
    #Using application/x-www-form-urlencoded parameters
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    return response
