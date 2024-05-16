import requests
import base64
import json

TOKEN_URL = 'https://accounts.spotify.com/api/token'
CLIENT_ID = '5e3b178d331d4a239bd30375ad348520'

def b64_encode(s):
    return base64.b64encode(s.encode()).decode()

def decode(s):
    return base64.b64decode(s).decode()

#gets token using Spotify's Client Credentials Authorization Flow
def get_token(CLIENT_SECRET):

    """
    with open("config.cfg", "r") as f:
        parsed_json = json.load(f)

    CLIENT_ID = parsed_json['CLIENT_ID']
    CLIENT_SECRET = parsed_json['CLIENT_SECRET']
    """

    data = 'grant_type=client_credentials'
    headers = {
        'Authorization' : 'Basic ' + b64_encode(CLIENT_ID + ':' + CLIENT_SECRET),
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    #POST to the TOKEN_URL
    #Using application/x-www-form-urlencoded parameters
    response = requests.post(TOKEN_URL, headers=headers, data=data)
    return response.json()['access_token']

if __name__ == "__main__":
    get_token()