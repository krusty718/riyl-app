import pkce
import hashlib
import base64
import random
import string
import requests
import urllib.parse

AUTH_URL = 'https://accounts.spotify.com/authorize' #Authorize Endpoint
CLIENT_ID = '5e3b178d331d4a239bd30375ad348520'
REDIRECT_URI = 'http://localhost:5000/callback'

def authorize():

    code_verifier = pkce.generate_code_verifier(length=128) #code verifier
    hashed_code = hashlib.new('sha256')
    hashed_code.update(b'{code_verifier}') #code challenge using SHA256 algorithm
    code_challenge = base64.b64encode(hashed_code.digest()) #code challenge encoded to base64

    params = {
        'client_id' : CLIENT_ID,
        'response_type': 'code',
        'redirect_uri' : REDIRECT_URI,
        'state' : ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16)),
        'scope' : 'user-read-private user-read-email',
        'code_challenge_method' : 'S256',
        'code_challenge' : code_challenge
    }

    #gets authorization code for token
    uri = requests.get(AUTH_URL, params=params).url
    
    print(uri)                      
    # NEED TO CAPTURE REDIRECTED URL THAT INCLUDES 'CODE' and 'STATE
    # CODE BELOW WORKS ONCE URL CAN BE CAPTURED (Listen in on port, create web server?)

    #p = urllib.parse.urlparse(get_response.url)
    #q = urllib.parse.parse_qs(p.query)
    #code = q['code'][0]
    #state = q['state'][0]
    #print(code)
    #print(state)

authorize()