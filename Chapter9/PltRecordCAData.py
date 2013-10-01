import pylab as plt
import numpy as np

#data = np.array([215,10,0,205,20,0,191,34,0,155,70,0,108,100,17,75,120,30,47,115,63,30,90,105,19,62,144,14,41,170,11,22,192,10,10,205,10,5,210,10,1,214,10,0,215,10,0,215,10,0,215,10,0,215,10,0,215,10,0,215,10,0,215,10,0,215,10,0,215])
data = np.array([215,10,0,153,72,0,54,171,0,2,223,0,0,225,0,0,178,47,0,72,153,0,6,219,0,0,225,47,0,178,153,0,72,219,0,6,225,0,0])

result = data.reshape(-1,3)

print(len(result[:,1]))
print(len(range(0,16)))

length = len(result)


plt.plot(range(0,length), result[:,0], marker = 'o', lw = 3, color = "green")
plt.plot(range(0,length), result[:,1], marker = 'x', linestyle = '--',lw = 3, color = "red")
plt.plot(range(0,length), result[:,2], marker = '*', linestyle = ':',lw = 3, color = "blue")
plt.show()


#Suseptibles: 35 Infected: 153 Recovered: 37 Times: 4


