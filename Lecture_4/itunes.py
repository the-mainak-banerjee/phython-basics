# Please install this requests package by using pip install cowsay
import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" +  sys.argv[1])

res = response.json()

# print(json.dumps(res, indent=2))

for result in res["results"]:
    print(result['trackName'])
