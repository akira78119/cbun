from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('D:\9_1_Dummy\TopDiameter.csv', header=None, sep="\s+")
#df.columns = ['index','TopDia','TopPxlCnt','TopThreshold','TopRadiusX','TopRadiusY','TopPxlRatio','BtmDia','BtmPxlCnt',
#              'BtmThreshold','BtmRadiusX','BtmRadiusY','BtmPxlRatio','Btm2Top','Judge']

#print(df.head())
#X = df[['TopDia']].values
#y = df['Judge'].values

Topdia = pd.read_csv('D:\9_1_Dummy\TopDiameter.csv')

X = Topdia.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13]].values
y = Topdia.iloc[:,14].values

tree = DecisionTreeRegressor(max_depth = 3)
tree.fit(X,y)

sort_idx = X.flatten().argsort()
plt.scatter(X[sort_idx], y[sort_idx], c='Lightblue')
plt.plot(X[sort_idx], tree.predict(X[sort_idx]), color='red',linewidth=2)
plt.xlabel('TopDia')
plt.ylabel('Judge')
plt.show()