import numpy as np
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

data = np.array([[30,12],[300,162],[35,19],[50,102],[110,222],[130,112],[190,152],[220,212]])

plt.scatter(data[:,0], data[:,1])   #데이터 위치의 산포도
plt.title("Linear Regression")
plt.xlabel("Delivert Distance")
plt.ylabel("Delievry Time")
plt.axis([0,420,0,300])

x = data[:, 0].reshape(-1,1)
y = data[:, 1].reshape(-1,1)


model = LinearRegression()
model.fit(x,y)          #모델 학습

y_pred = model.predict(x)       #예측값 계산
plt.plot(x,y_pred, color = 'r')
plt.show()