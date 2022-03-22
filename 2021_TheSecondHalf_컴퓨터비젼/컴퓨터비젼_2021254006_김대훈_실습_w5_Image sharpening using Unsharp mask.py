#Image sharpening using Unsharp mask
import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

img = cv2.imread('C:\Lena.png')

KSIZE = 11
ALPHA = 2
kernel = cv2.getGaussianKernel(KSIZE,0)
kernel = -ALPHA * kernel @ kernel.T
kernel[KSIZE//2, KSIZE//2] += 1 + ALPHA
print(kernel.shape, kernel.dtype, kernel.sum())

filtered = cv2.filter2D(img, -1, kernel)

plt.figure(figsize=(8,4))
plt.subplot(121)
plt.axis('off')
plt.title('image')
plt.imshow(img[:,:,[2,1,0]])
plt.subplot(122)
plt.axis('off')
plt.title('filtered')
plt.imshow(filtered[:,:,[2,1,0]])
plt.tight_layout(True)
plt.show()

cv2.imshow('before',img)
cv2.imshow('after',filtered)
cv2.waitKey()
cv2.destroyAllWindows()