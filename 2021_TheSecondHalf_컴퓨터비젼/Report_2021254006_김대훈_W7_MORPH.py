""" 모폴로지 필터
영상을 이진화한 후에 사용자로부터 Erosion, Dilation, Opening, Closing에 대한 선택과
횟수를 입력받아서 해당 결과를 출력하시오.
"""
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\TestImage\lena.png', cv2.IMREAD_GRAYSCALE)
assert img is not None
result, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                                   cv2.THRESH_BINARY_INV, 11, 10)

typ = input('Erode? 1, Dilate? 2, Open? 3, Close? 4: ')

cnt = int(input('count : '))

kernelSize = 3
kernel =np.ones((kernelSize, kernelSize),np.uint8)

if typ=='1':
    result = cv2.morphologyEx(binary, cv2.MORPH_ERODE, kernel, iterations=cnt)
elif typ=='2':
    result = cv2.morphologyEx(binary, cv2.MORPH_DILATE, kernel, iterations=cnt) 
elif typ=='3':
    result = cv2.morphologyEx(binary, cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernelSize, kernelSize)), iterations=cnt) 
elif typ=='4':
    result = cv2.morphologyEx(binary, cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernelSize, kernelSize)), iterations=cnt) 

plt.figure()
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('binary')
plt.imshow(binary, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('result')
plt.imshow(result, cmap='gray')
plt.tight_layout()
plt.show()