# We are using spotipy for this code

import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get("spotify_client_id"),
                                                           client_secret=os.environ.get("spotify_secret")))

# playlist_link = input("Enter the playlist link : ")

def playlist_details(playlist_link):
    # playlist_link = "https://open.spotify.com/playlist/0rdQNVf2nfwMHwQyWBr22Y"

    # playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    playlist_URI = playlist_link.split("?")[0]
    song_details = [x["track"] for x in sp.playlist_tracks(playlist_URI)["items"]]

    artists = []
    names = []

    for i in song_details :
        artists.append(i["album"]["artists"][0]["name"])
        names.append(i["name"])


    print(names)
    return names,artists