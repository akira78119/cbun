import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

Topdia = pd.read_csv('D:\9_1_Dummy\TopDiameter.csv')

X = Topdia.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13]].values
y = Topdia.iloc[:,14].values

model = BaggingClassifier(DecisionTreeClassifier(max_depth = 10), n_estimators = 100, random_state = 0).fit(X,y)

x_min = X[:, 0].min() - 1
x_max = X[:, 0].max() + 1
y_min = X[:, 1].min() - 1
y_max = X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

plt.subplot(122)
Z2 = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z2, alpha=0.6, cmap=mpl.cm.jet)
plt.scatter(X[:,0], X[:, 1], c=y, alpha=1, s=50, cmap=mpl.cm.jet,edgecolors="k")
plt.title("Bagging of decision trees")
plt.tight_layout()
plt.show()