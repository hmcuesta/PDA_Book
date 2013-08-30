import json
import csv
from pprint import pprint

typePokemon = {}

with open("pokemon.json") as f:
    data = json.loads(f.read())
   
    for line in data:

        if line["type"] not in typePokemon:
            typePokemon[line["type"]] = 1
        else:
            typePokemon[line["type"]] = typePokemon.get(line["type"]) + 1

with open("sumPokemon.csv", "w") as a:
    w = csv.writer(a)
    
    for key, value in sorted(typePokemon.items(), key=lambda x: x[1]):
        w.writerow([key,str(value)])
    
    
    pprint(typePokemon)

    
  
