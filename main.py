from flask import Flask
from get_token.get_token import get_token
from spotify import Album

app = Flask("__name__")

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/<name>")
def riyl(name):
    album_name = name
    headers = {
        "Authorization" : "Bearer " + get_token() #Authorization header to pass in to various end points
    }

    s = Album.search_album(album_name,headers) #Accept an album title, can also accept artist and album title or whatever Spotify's Search API can accept

    index = 1
    for a in s:
        print(f"{index}. {', '.join(a.artists)} - {a.name}")
        index += 1

    r = Album.get_album(s[int(input("\nPlease choose an album from 1 to 10: ")) - 1].album_id,headers)
    
    limit = 5
    rec = Album.rec_albums(r, limit=limit,headers=headers)

    print(f"\nRecommending based on {', '.join(r.artists)} - {r.name}\n\n")

    recs = []
    for i in range(0,limit):
        for _ in range(0,len(rec.json()['tracks'][i]['artists'])):
            print(rec.json()['tracks'][i]['artists'][_]['name'], end=" - ") #prints artist(s)
        print(f"\'{rec.json()['tracks'][i]['album']['name']}\'")
        recs = [rec for rec in rec.json()['tracks'][i]['album']['name']]
        print(rec.json()['tracks'][i]['album']['external_urls']['spotify'])
    return recs

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)