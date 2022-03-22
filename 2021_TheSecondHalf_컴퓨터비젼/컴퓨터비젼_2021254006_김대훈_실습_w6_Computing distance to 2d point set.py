#Computing distance to 2d point set
import cv2, numpy as np
import matplotlib.pyplot as plt

img= np.full((400, 600), 255, np.uint8)
cv2.circle(img, (320, 240), 100, 0)

distmap = cv2.distanceTransform(img, cv2.DIST_L2, cv2.DIST_MASK_PRECISE)

plt.figure()
plt.imshow(distmap, cmap='gray')
plt.show()