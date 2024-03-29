from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

refresh_token = 'AQAhh2QT9-Jw4HdlKbP0BKwJnrNVX9FIA291Jmg2qv9LOvP0Tv8zdUYcovu9xChI2FGWOzLQxZBghDGF0iSlcN7OpX3A_WDQxbhPYUjkJFC4TeAKd-TLcKT_NAr9Oazr1QGarjrdCMATJU9glwPMHlivGOzMa8fUaT6-R0GyPZVsAdLSN2avfANWnoN5pw'

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"

    }
    data = { "grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
# apparently the sapce after "Bearer " is required, got a 400 error without it. 


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist with this name found")
        return None
    
    return json_result

    # print(json_result)

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result


token = get_token()
# print(token)
result = search_for_artist(token, "Usher")
artist_id = result[0]["id"]
songs = get_songs_by_artist(token, artist_id)
# print(songs)


# for key in songs:
#     if key == 'name':
#         print(songs[key])

for idx, song in enumerate(songs):
    print(f"{idx + 1}. {song['name']}")
