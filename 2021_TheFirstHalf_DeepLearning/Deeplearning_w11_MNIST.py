# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np

# MNIST 데이터셋을 읽고 훈련 집합과 테스트 집합으로 분할
mnist=fetch_openml('mnist_784') #MNIST 데이터셋을 불러옴
mnist.data=mnist.data/255.0
#학습데이터와 테스트데이터 각 각 60000개 씩 사용
x_train=mnist.data[:60000]; x_test=mnist.data[60000:]
y_train=np.int16(mnist.target[:60000]); y_test=np.int16(mnist.target[60000:])

# MLP 분류기 모델을 학습
#다층퍼셉트론 셋팅 후 학습진행(hidden layer 100, earning rate 0.001, batch_size 512)
mlp=MLPClassifier(hidden_layer_sizes=(50),learning_rate_init=0.001,batch_size=128,max_iter=300,solver='adam',verbose=True)
#학습
mlp.fit(x_train,y_train)

# 테스트 Data로 예측
res=mlp.predict(x_test)

# 혼동 행렬
conf=np.zeros((10,10),dtype=np.int16)
for i in range(len(res)):
    conf[res[i]][y_test[i]]+=1
print(conf)

# 정확률 계산
no_correct=0
for i in range(10):
    no_correct+=conf[i][i]
accuracy=no_correct/len(res)
print("테스트 집합에 대한 정확률은", accuracy*100, "%입니다.")