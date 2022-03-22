#Model based fitting using RANSAC
import cv2
import numpy as np
import matplotlib.pyplot as plt
img0 = cv2.imread('D:\TestImage\Lena.png', cv2.IMREAD_GRAYSCALE)
imgl = cv2.imread('D:\TestImage\lena_rotated.png', cv2. IMREAD_GRAYSCALE)

detector = cv2.ORB_create(100)
kps0, fea0 = detector.detectAndCompute(img0, None)
kpsl, feal = detector.detectAndCompute(imgl, None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(fea0, feal)

pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,2)
ptsl = np.float32([kpsl[m.trainIdx].pt for m in matches]).reshape(-1,2)
H, mask = cv2.findHomography(pts0, ptsl, cv2.RANSAC, 3.0)

plt.figure()
plt.subplot(211)
plt.axis('off')
plt.title('all matches')
dbg_img = cv2.drawMatches(img0, kps0, imgl, kpsl, matches, None)
plt.imshow(dbg_img[:,:,[2,1,0]])
plt.subplot(212)
plt.axis('off')
plt.title('filtered matches')
dbg_img = cv2.drawMatches(img0, kps0, imgl, kpsl, [m for i,m in enumerate(matches) if mask[i]], None)
plt.imshow(dbg_img[:,:,[2,1,0]])
plt.tight_layout()
plt.show()
