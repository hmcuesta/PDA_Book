import matplotlib.pyplot as plt
import numpy as np
import dateutil.parser as dparser
from pylab import *
import mlpy

def smooth(x,window_len):
    
        s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
        w = np.hamming(window_len)

        y=np.convolve(w/w.sum(),s,mode='same')
        return y[window_len:-window_len+1]
    


y = np.genfromtxt("Gold.csv",
                     skip_header=1,
                     dtype=None,
                     delimiter=',',
                     usecols=(1))


targetValues = smooth(y, len(y))


np.random.seed(10)

trainingPoints = np.arange(125).reshape(-1, 1)
testPoints = np.arange(126).reshape(-1, 1)


knl = mlpy.kernel_gaussian(trainingPoints, trainingPoints, sigma=1)
knlTest = mlpy.kernel_gaussian(testPoints, trainingPoints, sigma=1)

knlRidge = mlpy.KernelRidge(lmb=0.01, kernel=None)
knlRidge.learn(knl, targetValues)
resultPoints = knlRidge.pred(knlTest)

print(resultPoints)


plt.step(trainingPoints, targetValues, 'o')
plt.step(testPoints, resultPoints)
plt.show()

