#BRIEF, ORB feature
import cv2
import numpy as np

img = cv2.imread('D:\TestImage\SK-1_FRAME_IMAGE\F3_F1.png', cv2.IMREAD_COLOR)

orb = cv2.ORB_create()
orb.setMaxFeatures(200)

keyPoints = orb.detect(img, None)
keyPoints, descriptors = orb.compute(img, keyPoints)

show_img = cv2.drawKeypoints(img, keyPoints, None, (0, 0, 255),
                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('ORB descriptors', show_img)
cv2.waitKey()
cv2.destroyAllWindows()

brief = cv2.xfeatures2d.BriefDescriptorExtractor_create(32, True) 

keyPoints, descriptors = brief.compute(img, keyPoints)

show_img = cv2.drawKeypoints(img, keyPoints, None, (0, 255, 0),
                             cv2. DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('BRIEF descriptors', show_img)
cv2.waitKey()
cv2.destroyAllWindows()

