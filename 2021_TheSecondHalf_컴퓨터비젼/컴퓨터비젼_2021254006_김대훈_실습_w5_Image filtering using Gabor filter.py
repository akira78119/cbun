#Image filtering using Gabor filter
import math
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\Lena.png',0).astype(np.float32) / 255

kernel = cv2.getGaborKernel((21,31), 5, 1, 10, 1, 0, cv2.CV_32F)
kernel /= math.sqrt((kernel*kernel).sum())

filtered = cv2.filter2D(img, -1, kernel)

plt.figure(figsize=(8,3))
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.title('kernel')
plt.imshow(kernel, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('filtered')
plt.imshow(filtered, cmap='gray')

plt.tight_layout()
plt.show()