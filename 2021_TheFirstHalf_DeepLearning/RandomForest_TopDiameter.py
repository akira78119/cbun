import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

Topdia = pd.read_csv('D:\9_1_Dummy\TopDiameter.csv')

print(Topdia.head())

x = Topdia.iloc[:,[1,2,3,4,5,6,7,8,9,10,11,12,13]].values
y = Topdia.iloc[:,14].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
print("No. of training data: ", len(x_train))
print("No. of test data:", len(y_test))

forest = RandomForestClassifier(n_estimators = 1000)
forest.fit(x_train, y_train)

y_pred = forest.predict(x_test)
print('Accuracy :', metrics.accuracy_score(y_test, y_pred))