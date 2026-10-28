import json
from js import fetch

async def load_json(url):
    response = await fetch(url)
    if not response.ok:
        raise Exception(f"Could not load {url}")
    return await response.json()

async def main():
    manifest = await load_json("./manifest.json")

    all_data = {}
    for filename in manifest:
        all_data[filename] = await load_json("./" + filename)

    print(all_data)

main()
