import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

import os
from dotenv import load_dotenv

load_dotenv()

spotify_oauth_scope= "playlist-modify-public playlist-modify-private"

def sp_oauth_scope(): 
    sp_oauth = SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        scope=spotify_oauth_scope,
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI")) 
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    return sp
def sp_client_scope():
    sp_client = SpotifyClientCredentials(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
    sp = spotipy.Spotify(auth_manager=sp_client)
    return sp