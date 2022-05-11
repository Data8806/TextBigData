import numpy as np

from matplotlib import pyplot as plt

inX = np.array([1.5,1.3])

labels = np.array(["A","A","B","B"])
groupd = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])

# for i in range(groupd.shape[0]):
#     if labels[i] == "A":
#         plt.scatter(groupd[i,0],groupd[i,1],marker="*",color ="red")
#     elif labels[i] == "B":
#         plt.scatter(groupd[i,0],groupd[i,1],marker="*",color ="blue")

# plt.scatter(inX[0],inX[1],marker="^",color = "green")

plt.scatter(groupd[np.where(labels=="A"),0],groupd[np.where(labels=="A"),1],c="r",marker="*")

plt.scatter(groupd[np.where(labels=="B"),0],groupd[np.where(labels=="B"),1],c="g",marker="*")

plt.scatter(inX[0],inX[1],c="b",marker="^")

plt.show()