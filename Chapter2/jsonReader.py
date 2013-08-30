import json
from pprint import pprint

with open("pokemon.json") as f:
    data = json.loads(f.read())
    pprint(data)
