#Gradient Boosting
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,confusion_matrix
import matplotlib.pyplot as plt

Topdia = pd.read_csv('D:\9_1_Dummy\TopDiameter.csv')

x = Topdia.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13]].values
y = Topdia.iloc[:,14].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4)

scaler = StandardScaler()
scaler.fit(x_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

clf = GradientBoostingClassifier(n_estimators = 100, learning_rate = 0.3, max_depth = 1, random_state = 0)
clf.fit(x_train, y_train)

predictions = clf.predict(x_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

