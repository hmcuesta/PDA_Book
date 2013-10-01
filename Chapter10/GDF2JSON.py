import numpy as np
import json
from io import StringIO

nodes = np.genfromtxt("nodes.csv", dtype='object', delimiter=',', skip_header=1,
                     usecols=(0,1,3))

links = np.genfromtxt("links.csv", dtype='object', delimiter=',', skip_header=1,
                     usecols=(0,1))

for n in range(len(nodes)):
    for ls in range(len(links)):
        if nodes[n][0] == links[ls][0]:
            links[ls][0] = n
        
        if nodes[n][0] == links[ls][1]:
            links[ls][1] = n
data ={}

lst = []
for x in nodes:
    d = {}
    d["name"] = str(x[1]).replace("b'","").replace("'","")
    lst.append(d)
        
data["nodes"] = lst

lnks = []

for ls in links:
    d = {}
    d["source"] = ls[0]
    d["target"] = ls[1]
    lnks.append(d)

data["links"] = lnks

with open("newJson.json","w") as f:    
    f.write(json.dumps(data))







