#Image Segmentation using K-means algorithm
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\TestImage\lena.png').astype(np.float32) / 255
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

data = img_lab.reshape((-1,3))


num_classes = 8
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 50, 0.1)
_, labels, centers = cv2.kmeans(data, num_classes, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

segmented_lab = centers[labels.flatten()].reshape(img.shape)
segmented = cv2.cvtColor(segmented_lab, cv2.COLOR_Lab2RGB)

plt.figure()
plt.subplot(121)
plt.axis('off')
plt.title('original')
plt.imshow(img[:,:,[2,1,0]])
plt.subplot(122)
plt.axis('off')
plt.title('segmented')
plt.imshow(segmented)

plt.show()