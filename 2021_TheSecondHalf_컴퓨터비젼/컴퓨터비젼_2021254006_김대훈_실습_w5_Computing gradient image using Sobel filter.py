#Computing gradient image using Sobel filter
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\Lena.png',0) #0 gray

dx = cv2.Sobel(img, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_32F, 0, 1)

#grab = cv2.sqrt(dx*dx+dy*dy)

plt.figure(figsize=(8,3))
plt.subplot(131)
plt.axis('off')
plt.title('image')
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.imshow(dx, cmap='gray')
plt.title(r'$\frac{dI}{dx}$')
plt.subplot(133)
plt.axis('off')
plt.title(r'$\frac{dI}{dy}$')
plt.imshow(dy, cmap='gray')
plt.tight_layout()
plt.show()