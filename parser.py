import json

releases = json.loads(r.content)
for release in releases[0]['assets']:
    if release["label"] == "Linux_x64 Tiles":
        print(release["browser_download_url"])
