""" 히스토그램 평탄화
 사용자로부터 R, G, B 중의 하나의 채널을 입력받고 입력받은 채널에 대한 히스토그램을 그리고 
평탄화를 한 후에 그 영상을 출력하시오. (선택받은 채널 이외의 채널 값은 변화하지 않음)
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
mode = -1

rgb = input('R, G, B 입력:')

if rgb == 'r' or rgb == 'R':
    mode = 2
elif rgb == 'g' or rgb == 'G':
    mode = 1
elif rgb == 'b' or rgb == 'B':
    mode = 0
    
img = cv2.imread('D:\TestImage\image_Peppers512rgb.png')

img_to_his= np.copy(img)

img_G = img[:,:,mode]
#cv2.imshow('gray',img_G)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_to_his[:,:,mode] = cv2.equalizeHist(img_G)
#histEqualizedR = np.histogram(img_to_his, 256, [0,255])
#color_eq = cv2.cvtColor(img_to_his, cv2.COLOR_HSV2BGR)

orgChannels = cv2.split(img)
channels = cv2.split(img_to_his)


colors = ("blue", "green", "red")
plt.figure()
plt.figure(figsize=(8,8))

plt.subplot(221)
plt.axis('off')
plt.title('original')
plt.imshow(img[:,:,[2,1,0]])

plt.subplot(222)
plt.axis('off')
plt.title('equalized color')
plt.imshow(img_to_his[:,:,[2,1,0]])

plt.subplot(223)
plt.title("Orig Histogram")
for (channel, color) in zip(orgChannels, colors):
    color_calchist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(color_calchist, color = color)
    plt.xlim([0, 256])
plt.ylabel("Pixels")
plt.xlabel('pixel value')

plt.subplot(224)
plt.title("equalized Histogram")
for (channel, color) in zip(channels, colors):
    color_calchist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(color_calchist, color = color)
    plt.xlim([0, 256])
    
plt.ylabel("Pixels")
plt.xlabel('pixel value')
plt.show()
