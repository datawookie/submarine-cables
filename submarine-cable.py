import json
import time
import requests

response = requests.get("https://www.submarinecablemap.com/api/v3/cable/cable-geo.json")
cables = response.json()

ID = [feature["properties"]["id"] for feature in cables["features"]]
ID = sorted(ID)

CITIES = {}

for id in ID:
    print(id)
    response = requests.get(f"https://www.submarinecablemap.com/api/v3/cable/{id}.json")
    cable = response.json()

    cities = [landing["name"] for landing in cable["landing_points"]]

    CITIES[id] = cities

    # Being polite.
    time.sleep(5)

with open("cable-cities.json", "wt") as file:
    json.dump(CITIES, file, indent=2)
