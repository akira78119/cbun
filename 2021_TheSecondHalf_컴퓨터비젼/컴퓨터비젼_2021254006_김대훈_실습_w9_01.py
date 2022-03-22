# -*- coding: utf-8 -*-
import cv2
import matplotlib.pyplot as pit 
import numpy as np
import math

img0i  = cv2.imread(’../data/Lena.png.)
M = i np.array([[math.cos(np.pi/12), -math.sin(np.pi/12), 0]
[math.sin(np.pi/12), math.cos(np.pi/12), 0], [w]])
Moff = np.eye(3)
Moff[0ᄉ2] = -img0.shape[l]/2
Moff[1^2] = -img0.shape[0]/2 print(np.linalg.inv(Mofff)
imgl = cv2.warpPerspective(img0, np.linalg.
(img0.shape[1], img0.shape[0]),
cv2.imwrite(■../data/Lena rotated.png *, imgl)
img0 = cv2.imread(*../data/Lena.png't cv2.IMREAD_GRAYSCALE)
imgl = cv2.imread('../data/Lena_rotated.png', cv2.IMREAD_GRAYSCALE) detector     =  cv2.ORB_create(100)
kps0,     fea0  =       detector.detectAndCompute(img0,       None)

kpslj feal = detector.detectAndCompute(imgl} None)
                  
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)

matchesOl  = matcher.knnMatch(fea0, feal, =2)
matcheslO = matcher.knnMatch(fealJ fea0? =2)
def ratio testfmatches, ratio thr):
                  good_matches = [] for m in matches:
ratio = m[0].distance / m[l].distance if ratio < ratio_thr:
goodmatches.append(m[0])
return good_matches
RATIO THR =0.7          # Lower values mean more aggressive filtering.
，■•냥，ᅳᅳᅳ•〜*'ᅳᅳᅳᅳ바''ᅳ*，'ᅳv*ᅳv*ᅳv*ᅳᅳv*바，，，*一w•'바，'，바，^^
good_matches01 = ratio_test(matchesOl, RATIO_THR)
good_matchesl0 = ratio_test(matchesl0, RATIO_THR)
good_matchesl0_ = {(m.trainldx, m.queryldx) for m in good_matchesl0}
finalmatches = [m for m in goodmatchesOl if (m.queryldx, m.trainldx) in good_matchesl0_] dbgimg = cv2.drawMatches(img0, kps0, imgl, kpsl, finalmatches. None)
pit.figure()
pit.imshow(dbg_img[:으: J: 2스1A0]])
pit. tight__layout () plt.show()