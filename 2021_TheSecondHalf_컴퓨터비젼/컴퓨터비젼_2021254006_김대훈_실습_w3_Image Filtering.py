#Image Filtering
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\Lena.png').astype(np.float32)/255

noised = (img + 0.2 * np.random.rand(*img.shape).astype(np.float32))
noised = noised.clip(0,1)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

gauss_blur = cv2.GaussianBlur(noised, (7,7),0)
plt.imshow(gauss_blur[:,:,[2,1,0]])
plt.show()

median_blur = cv2.medianBlur((noised*255).astype(np.uint8),7)
plt.imshow(median_blur[:,:,[2,1,0]])
plt.show()

bilat = cv2.bilateralFilter(noised, -1, 0.3, 10)
plt.imshow(bilat[:,:,[2,1,0]])
plt.show()