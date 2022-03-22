import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

iris = datasets.load_iris()
print('Class names : ', iris.target_names)
print('target : [0:setosa, 1:versicolor, 2:virginica]')
print('No. of Data :', len(iris.data))
print('Feature names :', iris.feature_names)

data = pd.DataFrame({'sepal length': iris.data[:, 0], 'sepal width': iris.data[:, 1], 'petal length': iris.data[:, 2],'petal width': iris.data[:, 3], 'species': iris.target})
print(data.head())

x = data[['sepal length', 'sepal width', 'petal length', 'petal width']]
y = data['species']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
print("No. of training data: ", len(x_train))
print("No. of test data:", len(y_test))

forest = RandomForestClassifier(n_estimators = 100)
forest.fit(x_train, y_train)

y_pred = forest.predict(x_test)
print('Accuracy :', metrics.accuracy_score(y_test, y_pred))