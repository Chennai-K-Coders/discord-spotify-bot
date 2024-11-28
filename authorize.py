from flask import Flask , request

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import os
from dotenv import load_dotenv


load_dotenv()

spotify_oauth_scope= "playlist-modify-public playlist-modify-private"

sp_oauth = SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                        scope=spotify_oauth_scope,
                        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI")) 
sp = spotipy.Spotify(auth_manager=sp_oauth)


app = Flask(__name__)

@app.route('/callback/spotify',methods=['GET'])

def reterive_code():
    sp_oauth.get_access_token(code=request.args.get('code'),as_dict=False)
    return 'User Authorized'

if __name__ == '__main__' :
    app.run(port=8080)