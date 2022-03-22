#Finding external and internal contours
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\Bnw.png',0)

contours , hierarchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

img_external = np.zeros(img.shape, img.dtype)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(img_external, contours, i, 255, -1)
        
img_internal = np.zeros(img.shape, img.dtype)
for i in range(len(contours)):
    if hierarchy[0][i][3] != -1:
        cv2.drawContours(img_internal, contours, i, 255, -1)

plt.figure(figsize=(10,3))
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('external')
plt.imshow(img_external, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('internal')
plt.imshow(img_internal, cmap='gray')
plt.tight_layout()
plt.show()
