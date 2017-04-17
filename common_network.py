import json
import requests


def get_mastodon_data_json():
    link = 'https://instances.mastodon.xyz/instances.json'
    r = requests.get(link)
    return json.loads(r.text)
