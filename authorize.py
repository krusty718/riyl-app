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