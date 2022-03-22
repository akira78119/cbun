#Stereo rectification
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size' : 20})
np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

data = np.load('D:\TestImage\case1/stereo.npy').item()
Kl, Dl, Kr, Dr, R, T, img_size = data['Kl'], data['Dl'], data['Kr'], data['Dr'], \
                                 data['R'], data['T'], data['img_size']
                                 
left_img = cv2.imread('D:\TestImage\case1/left14.png')
right_img = cv2.imread('D:\TestImage\case1/right14.png')

R1, R2, P1, P2,  Q, validRoil, validRoi2 = cv2.stereoRectify(Kl, Dl, Kr, Dr, img_size, R, T) 

xmap1, ymap1 = cv2.initUndistortRectifyMap(Kl, Dl, R1, Kl, img_size, cv2.CV_32FC1)
xmap2, ymap2 = cv2.initUndistortRectifyMap(Kr, Dr, R2, Kr, img_size, cv2.CV_32FC1)
left_img_rectified = cv2.remap(left_img, xmap1, ymap1, cv2.INTER_LINEAR)
right_img_rectified = cv2.remap(right_img, xmap2, ymap2, cv2.INTER_LINEAR)

plt.figure(0, figsize=(12,10)) 
plt.subplot(221)
plt.title('left original')
plt.imshow(left_img, cmap='gray') 
plt.subplot(222)
plt.title('right original')
plt.imshow(right_img, cmap='gray') 
plt.subplot(223)
plt.titie('left rectified')
plt.imshow(left_img_rectified, cmap='gray') 
plt.subp1ot(224)
plt.title('right rectified')
plt.imshow(right_img_rectified, cmap='gray')
plt.tight_layout()
plt.show()