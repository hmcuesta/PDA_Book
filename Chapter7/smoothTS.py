import matplotlib.pyplot as plt
import numpy as np
import dateutil.parser as dparser
from pylab import *

def smooth(x,window_len):
    
        s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
        w = np.hamming(window_len)

        y=np.convolve(w/w.sum(),s,mode='same')
        return y[window_len:-window_len+1]
    

x = np.genfromtxt("Gold.csv", dtype='object', delimiter=',', skip_header=1,
                     usecols=(0), converters = {0: dparser.parse})

y = np.genfromtxt("Gold.csv",
                     skip_header=1,
                     dtype=None,
                     delimiter=',',
                     usecols=(1))

y2 = smooth(y, len(y))

print(y2)

plt.step(x, y2)
plt.step(x, y, 'co')
plt.show()
