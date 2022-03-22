""" 주파수 도메인 필터링
 DFT를 통해서 영상을 주파수 도메인으로 바꿔서 출력 한 후에 사용자로부터 반지름을 입력받아서
그 크기만큼의 원을 그린 후에 DFT 결과에 곱해준 후에 IDFT를 해서 필터링된 영상을 출력하시오. 
사용자로부터 Low pass인지 High Pass인지를 입력받아 Low pass면 원 안을 통과시키고, High Pass면 원 바깥을 통과시키도록 하시오.
"""

import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\TestImage\lena.png',0).astype(np.float32) / 255

radius = input('radius:')
LowHighpass = input('Low pass? 0 , High Pass? 1:')

fft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft, axes=[0,1])
mask = np.zeros(fft_shift.shape, np.uint8)

magnitude = cv2.magnitude(fft_shift[:,:,0], fft_shift[:,:,1])
magnitude = np.log(magnitude)

centerX = mask.shape[0]//2
centerY = mask.shape[1]//2

distance = int(radius) * int(radius)
for yy in range(0, mask.shape[1]):
    for xx in range(0, mask.shape[0]):
        nDist = ( pow(abs(yy-centerY),2) + pow(abs(xx-centerX),2) )
        if nDist < distance:
            mask[xx,yy,:] =1
            
if int(LowHighpass) == 1:
    mask = 1 - mask
    
#cv2.circle(mask, (int(mask.shape[0]/2),int(mask.shape[1]/2)), int(radius), (0,0,255), -1)

fft_shift *= mask
fft = np.fft.ifftshift(fft_shift, axes=[0, 1])
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

magnitude2 = cv2.magnitude(fft_shift[:,:,0], fft_shift[:,:,1])
magnitude2 = np.log(magnitude2)

plt.figure()
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(img, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('filtered')
plt.imshow(filtered, cmap='gray')
plt.subplot(133)
plt.axis('off')
plt.title('mask')
plt.imshow(magnitude2, cmap='gray')

plt.show()