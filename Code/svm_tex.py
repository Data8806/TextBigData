import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.svm import SVC
from sklearn import datasets
import matplotlib
from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import accuracy_score,recall_score,f1_score

#svm分类器
matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 20

#数据集
X,y = datasets.make_moons(noise=0.15,random_state=666)
plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])

plt.legend()
plt.show()
#创建算法，核rbf
svm = SVC(kernel='rbf',random_state=0,gamma = 0.10,C=10)
svm.fit(X,y)
plot_decision_regions(X,y,clf=svm)
print(svm.score(X,y))
plt.legend(loc='upper left')   
plt.show()
#创建算法,核Poly
svm_1 = SVC(kernel='poly',random_state=0,degree = 3,gamma = 0.10,C=10)
svm_1.fit(X,y)
print(svm_1.score(X,y))
plot_decision_regions(X,y,clf=svm_1)
plt.legend(loc='upper left')
plt.show()
#创建算法,核Sigmoid
svm_2 = SVC(kernel='sigmoid',random_state=0,gamma = 0.10,C=10)
svm_2.fit(X,y)
print(svm_2.score(X,y))
plot_decision_regions(X,y,clf=svm_2)
plt.legend(loc='upper left')
plt.show()