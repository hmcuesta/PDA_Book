import matplotlib
import matplotlib.pyplot as plt
 
def getData():
    lists = [line.strip().split(",") for line in open('wine.data', 'r').readlines()]
    return [list( l[1:14]) for l in lists], [l[0] for l in lists]

matrix, labels = getData()

xaxis1 = []; yaxis1 = []
xaxis2 = []; yaxis2 = []
xaxis3 = []; yaxis3 = []
x = 0
y = 1

for n, elem in enumerate(matrix):
    if int(labels[n]) == 1:
        xaxis1.append(matrix[n][x])
        yaxis1.append(matrix[n][y])
    elif int(labels[n]) == 2:
        xaxis2.append(matrix[n][x])
        yaxis2.append(matrix[n][y])
    elif int(labels[n]) == 3:
        xaxis3.append(matrix[n][x])
        yaxis3.append(matrix[n][y])

fig = plt.figure()
ax = fig.add_subplot(111)
type1 = ax.scatter(xaxis1, yaxis1, s=80, c='white')
type2 = ax.scatter(xaxis2, yaxis2, s=80, c='red')
type3 = ax.scatter(xaxis3, yaxis3, s=80, c='darkred')
 
ax.set_title('Wine Features', fontsize=14)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.legend([type1, type2, type3], ["Class 1", "Class 2", "Class 3"], loc=1)
 
ax.grid(True,linestyle='-',color='0.80')
 
plt.show()
