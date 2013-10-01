import numpy as np
import mlpy
from mlpy import KernelRidge
import matplotlib.pyplot as plt

np.random.seed(10)

targetValues = np.genfromtxt("Gold.csv",
                     skip_header=1,
                     dtype=None,
                     delimiter=',',
                     usecols=(1))

trainingPoints = np.arange(125).reshape(-1, 1)
testPoints = np.arange(126).reshape(-1, 1)

#training kernel matrix
knl = mlpy.kernel_gaussian(trainingPoints, trainingPoints, sigma=1)
#testing kernel matrix
knlTest = mlpy.kernel_gaussian(testPoints, trainingPoints, sigma=1)

knlRidge = KernelRidge(lmb=0.01, kernel=None)
knlRidge.learn(knl, targetValues)
resultPoints = knlRidge.pred(knlTest)

print(resultPoints)

fig = plt.figure(1)
plot1 = plt.plot(trainingPoints, targetValues, 'o')
plot2 = plt.plot(testPoints, resultPoints)
plt.show()

