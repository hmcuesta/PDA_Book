from PIL import Image
from numpy import array
import mlpy
from collections import OrderedDict


data = {}
   
for fn in range(1,658):
    img = Image.open("ImgFolder\\{0}.jpg".format(fn))
    arr = array(img)
    list = []
    for n in arr: list.append(n[0][0])
    for n in arr: list.append(n[0][1])
    for n in arr: list.append(n[0][2])
    data[fn] = list
   
reference = data[31]

result ={}

for x, y in data.items():
    dist = mlpy.dtw_std(reference, y, dist_only=True)
    result[x] = dist


sortedRes = OrderedDict(sorted(result.items(), key=lambda x: x[1]))
for a,b in sortedRes.items():
    print("{0}-{1}".format(a,b))




