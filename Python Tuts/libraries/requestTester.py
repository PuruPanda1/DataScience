import json
import requests
import sys

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term="+sys.argv[1])

o = response.json()

for results in o["results"]:
    print(results["trackName"])