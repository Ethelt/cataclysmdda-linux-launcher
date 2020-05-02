import json

with open("json") as releases_info:
    releases = json.load(releases_info)
for release in releases[0]['assets']:
    if release["label"] == "Linux_x64 Tiles":
        print(release["browser_download_url"])
