# RIYL - APP

#### Video Demo: [URL](https://youtu.be/pRd3YKVqwAA)

#### Description: A once-popular refrain in music writing, something that always caught my eye when reading reviews in countless publications, print and online, was the ending flourish/abbreviation "RIYL ...", denoting that, if you've read to the end of this popular or, more likely, niche write up, and the felt it necessary, this album is recommended to you if you already like the following. Put more succinctly: Recommended If You Like.



# How-To-Use:

#### This app works best by just inputting an album's name. An album ID or URI will not work, at least not yet but the idea is to keep things easy and allow a user to simply enter a name of an album they know well, or one they're currently listening to.



# get_token(secret)
#### get_token accepts a Client Secret as provided by Spotify's Web API [URL](https://developer.spotify.com/dashboard/5e3b178d331d4a239bd30375ad348520/settings)
#### Assuming access is available, test_spotify_api.py accepts the paramter -c, followed by the Client Secret

    python test_spotify_api.py -c [CLIENT SECRET]
    
#### get_token is a module outside of the main project that simply requests the Bearer Token from Spotify API's Token Endpoint.  It assumes the simple Client Credentials flow and doesn't require the user to authorize via Spotify's Authorization flows.  get_token returns a JSON response, example below:

	from get_token import get_token

	get_token().json()['access_token']

# RIYL-app
## Headers
#### Headers are called in main() using get_token()
	headers  = {
		"Authorization" : "Bearer "  +  get_token().json()['access_token']
		}

## search()
#### The main recommendation engine accepts user input based on album name.  It currently doesn't accept album IDs or album URIs because Spotify API's Search functionality doesn't fully accept it.
#### search() accepts parameters and headers (from main()).  Params are currently built-in but can be changed later on.
