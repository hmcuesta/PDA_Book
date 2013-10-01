import numpy as np
import operator
from pylab import *

nodes = np.genfromtxt("nodes.csv", dtype=str, delimiter=',', skip_header=1,
                     usecols=(2))


counter = operator.countOf(nodes, 'male')
male = (counter *100) / len(nodes)
female = 100 - male
print(female)

figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Male', 'Female'
fracs = [male,female]
explode=(0, 0.05)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
             
title('Male to Female Ratio', bbox={'facecolor':'0.8', 'pad':5})

show()
