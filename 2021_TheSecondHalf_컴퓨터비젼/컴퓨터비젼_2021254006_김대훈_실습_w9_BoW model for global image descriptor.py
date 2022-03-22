#BoW model for global image descriptor
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
matplotlib.rc('font',size=18)

img0 = cv2.imread('D:\TestImage\people.jpg', cv2.IMREAD_GRAYSCALE)
imgl = cv2.imread('D:\TestImage\face.jpg', cv2.IMREAD_GRAYSCALE)

detector = cv2.ORB_create(500)
_, fea0 = detector.detectAndCompute(img0, None)
_, fea1 = detector.detectAndCompute(imgl, None)
descr_type = fea0.dtype

bow_trainer = cv2.BOWKMeansTrainer(50)
bow_trainer.add(np.float32(fea0))
bow_trainer.add(np.float32(fea1))
vocab = bow_trainer.cluster().astype(descr_type)

bow_descr = cv2.B0WImgDescriptorExtractor(detector, cv2.BFMatcher(cv2.NORM_HAMMING))
bow_descr.setVocabulary(vocab)

img = cv2.imread('D:\TestImage\Lena.png', cv2.IMREAD_GRAYSCALE)
kps = detector.detect(img, None)
descr = bow_descr. compute (img, kps)
plt.figure(figsize=(10,8))
plt.title('image BoW descriptor')
plt.bar(np.arange(len(descr[0])), descr[0])
plt.xlabel('vocabulary element')
plt.ylabel('frequency')
plt.tight_layout()
plt.show()