import requests
import os
import urllib.parse

def query_songlink_api(song_url):
    url = f"https://api.song.link/v1-alpha.1/links?url={urllib.parse.quote(song_url)}"
    response = requests.get(url)
    return response

def parse_songlink_response(response):
    if response.status_code == 200:
        data = response.json()
        
    else:
        return None