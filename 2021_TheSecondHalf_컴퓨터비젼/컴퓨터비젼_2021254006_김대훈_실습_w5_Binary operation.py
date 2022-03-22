#Binary operation
import cv2, numpy as np
import matplotlib.pyplot as plt

circle_img= np.zeros((500,500), np.uint8)
cv2.circle(circle_img, (250,250), 100, 255, -1)

rect_img = np.zeros((500,500), np.uint8)
cv2.rectangle(rect_img, (100,100), (400,250), 255, -1)

circle_and_rect_img = circle_img & rect_img
circle_or_rect_img = circle_img | rect_img

plt.figure(figsize=(10,10))
plt.subplot(221)
plt.axis('off')
plt.title('circle')
plt.imshow(circle_img, cmap='gray')
plt.subplot(222)
plt.axis('off')
plt.title('rectangle')
plt.imshow(rect_img, cmap='gray')
plt.subplot(223)
plt.axis('off')
plt.title('circle & rectangle')
plt.imshow(circle_and_rect_img, cmap='gray')
plt.subplot(224)
plt.axis('off')
plt.title('circle | rectangle')
plt.imshow(circle_or_rect_img, cmap='gray')

plt.tight_layout(True)
plt.show()