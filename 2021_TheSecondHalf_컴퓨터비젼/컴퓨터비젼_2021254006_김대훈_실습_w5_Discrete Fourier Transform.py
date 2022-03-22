#Discrete Fourier Transform
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:\Lena.png',0).astype(np.float32) / 255

fft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted = np.fft.fftshift(fft, axes=[0, 1])
magnitude = cv2.magnitude(shifted[:,:,0], shifted[:,:,1])
magnitude = np.log(magnitude)

plt.axis('off')
plt.imshow(magnitude, cmap='gray')
plt.tight_layout(True)
plt.show()

restotred = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

cv2.imshow('restored',restotred)
cv2.waitKey()
cv2.destroyAllWindows()