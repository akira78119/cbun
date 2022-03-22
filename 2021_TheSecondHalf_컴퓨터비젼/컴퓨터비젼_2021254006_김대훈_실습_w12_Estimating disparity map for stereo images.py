#Estimating disparity map for stereo images
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size' : 20})
                                 
left_img = cv2.imread('D:\TestImage\left.png')
right_img = cv2.imread('D:\TestImage\right.png')

stereo_bm = cv2.StereoBM_create(32)
dispmap_bm = stereo_bm.compute(cv2.cvtColor(left_img, cv2.COLOR_BGR2GRAY),
                               cv2.cvtColor(right_img, cv2.COLOR_BGR2GRAY))

stereo_sgbm = cv2.StereoSGBMLcreate(0, 32)
dispmap_sgbm = stereo_sgbm.conpute(left_img, right_img)

plt.figure(figsize=(12, 10))
plt.subplot(221)
plt.title('left')
plt.imshow(left_img[:,:, [2,1,0]])
plt.subplot(222)
plt.title('right')
plt.imshow(right_img[:,:, [2,1,0]])
plt.subplot(223)
plt. title('BM')
plt.imshow(dispmap_bm, cmap = 'gray')
plt.subplot(224)
plt. title('SGBM')
plt.imshow(dispmap_sgbm, cmap = 'gray')
plt.show()