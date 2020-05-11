import json

with open("json") as releases_info:
    releases = json.load(releases_info)
i = 0
while True:
    for release in releases[i]['assets']:
        if release["label"] == "Linux_x64 Tiles":
            print(release["browser_download_url"])
            exit() 
    i += 1
