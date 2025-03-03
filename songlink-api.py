import requests
import json
import os
import urllib.parse

def query_songlink_api(song_url):
    url = f"https://api.song.link/v1-alpha.1/links?url={urllib.parse.quote(song_url)}"
    response = requests.get(url)
    return response

def parse_songlink_response(response):
    if response.status_code == 200:
        data = response.json()
        linksByPlatform = [item.['url'] for item in data['linksByPlatform'].values()]
        linksByPlatform_dict = {p:l for (p,l) in zip(data['linksByPlatform'].keys(), linksByPlatform)}
        return linksByPlatform_dict
    else:
        return None