
from spotipy.oauth2 import SpotifyClientCredentials
import json, os, spotipy, requests_html, sys
from bs4 import BeautifulSoup
from time import sleep

working_directory = r"spotify"
clientID = "29d1ade7ca97462696eb9455ea99e70b"
clientSECRET = "33c2047705374ccdb55db8f20aa84444"

credentials = SpotifyClientCredentials(
    client_id=clientID,
    client_secret=clientSECRET
)

SpotifySession = spotipy.Spotify(
    client_credentials_manager=credentials
)

username = "n59x8638lkhuawa8ykrbqpt93"
pythonARGS = sys.argv
if len(pythonARGS) == 2:
    username = pythonARGS[1]

spotifyURL = "https://open.spotify.com"
userURL = f"https://open.spotify.com/user/{username}"

print(f"get request to: '{userURL}'.")
print("...")

session = requests_html.HTMLSession()
response = session.get(userURL)
response.html.render(sleep=1)
print("html session created successfully.")

sp = BeautifulSoup(response.html.html, "html.parser")
user_playlists = sp.findAll("div", attrs={
    "class": "_3802c04052af0bb5d03956299250789e-scss"
})
user_playlists = list(user_playlists)

print("getting all playlists urls...")
playlistURLs = []
for up in user_playlists:
    playlistURL_element = up.find("a", {
        "class": "f7ebc3d96230ee12a84a9b0b4b81bb8f-scss"
    })
    playlistURL = playlistURL_element["href"]
    playlistURLs.append(spotifyURL + playlistURL)

SpotifyPlaylists = []
for playlistURL in playlistURLs:  
    playlistDICT = SpotifySession.playlist(playlistURL)
    
    playlist = {
        "name": playlistDICT['name'],
        "url": playlistDICT['external_urls']['spotify'],
        "by": playlistDICT['owner']['display_name'],
        "playlist_duration": None,
        "songs": []
    }

    playlist_duration = 0
    for i in range(len(playlistDICT['tracks']['items'])):
        song_duration_seconds = playlistDICT['tracks']['items'][i]['track']['duration_ms'] // 1000
        song = {
            "song_name": playlistDICT['tracks']['items'][i]['track']['name'],
            "song_url": playlistDICT['tracks']['items'][i]['track']['external_urls']['spotify'],
            "artists": [
                
            ],
            "album_name": playlistDICT['tracks']['items'][i]['track']['album']['name'],
            "album_url": playlistDICT['tracks']['items'][i]['track']['album']['external_urls']['spotify'],
            "song_duration": str(song_duration_seconds)
        }
        
        artists = playlistDICT['tracks']['items'][i]['track']['artists']
        for ar in artists:
            song['artists'].append(
                {
                    "artist_name": ar["name"],
                    "artist_url": ar["external_urls"]["spotify"]
                }
            )
        
        playlist_duration += song_duration_seconds
        playlist['songs'].append(song)

    playlist['playlist_duration'] = str(playlist_duration)
    SpotifyPlaylists.append(playlist)


SpotifyPlaylistsJSON = json.dumps(SpotifyPlaylists, indent=4)

with open(working_directory + "\\SpotifyPlaylists.json", 'w+', encoding='utf-8') as file:
    file.truncate(0)
    file.write(SpotifyPlaylistsJSON)

os.system(working_directory + "\\SpotifyPlaylists.json")