import numpy as np
import mlpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

wine = np.loadtxt('wine.data', delimiter=',')
x, y = wine[:, 1:4], wine[:, 0].astype(np.int)
print(x.shape)
print(y.shape)

pca = mlpy.PCA() 
pca.learn(x) 
z = pca.transform(x, k=2) 
print(z.shape)


fig1 = plt.figure(1)
title = plt.title("PCA on wine dataset")
plot = plt.scatter(z[:, 0], z[:, 1], c=y,s=90, cmap = cm.Reds)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")
plt.show()


svm = mlpy.LibSvm(kernel_type='rbf', gamma=20 ) 
svm.learn(z, y) 


xmin, xmax = z[:,0].min()-0.1, z[:,0].max()+0.1
ymin, ymax = z[:,1].min()-0.1, z[:,1].max()+0.1
xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.01), np.arange(ymin, ymax, 0.01))
grid = np.c_[xx.ravel(), yy.ravel()]


result = svm.pred(grid)

fig2 = plt.figure(2)
title = plt.title("SVM (linear kernel) on PCA")
plot1 = plt.pcolormesh(xx, yy, result.reshape(xx.shape), cmap = cm.Greys_r)
plot2 = plt.scatter(z[:, 0], z[:, 1], c=y, s=90, cmap = cm.Reds)
labx = plt.xlabel("First component")
laby = plt.ylabel("Second component")
limx = plt.xlim(xmin, xmax)
limy = plt.ylim(ymin, ymax)
plt.show()
