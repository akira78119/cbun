#Binarization using Otsu algorithm
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\Lena.png',0)

otsu_thr , otsu_mask = cv2.threshold(img, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('Estmated threshold (Osu):', otsu_thr)

plt.figure(figsize=(6,3))
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(img, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.title('Otsu thrshold')
plt.imshow(otsu_mask, cmap='gray')
plt.tight_layout()
plt.show()
