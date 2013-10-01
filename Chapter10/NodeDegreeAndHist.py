import numpy as np
import matplotlib.pyplot as plt
import operator

links = np.genfromtxt("links.csv", dtype=str, delimiter=',', skip_header=1,
                     usecols=(0,1))

dic = {}
#Node Degree
for n in sorted(np.reshape(links,558)):

    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1
    
size = len(dic)

#Centrality
sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)

plt.bar(range(size),list(dic.values()))
plt.xticks(range(size), list(dic.keys()), rotation=90)
plt.show()


#Histogram
histogram = {}

for n in range(26):
    histogram[n] = operator.countOf(list(dic.values()), n)

plt.plot(range(26),list(histogram.values()))
plt.show()
