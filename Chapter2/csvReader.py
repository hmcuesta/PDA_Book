import csv

with open("pokemon.csv") as f:
    data = csv.reader(f)
    for line in data:
        print(" id: {0} , typeTwo: {1}, name:  {2}, type: {3}"
              .format(line[0],line[1],line[2],line[3]))
