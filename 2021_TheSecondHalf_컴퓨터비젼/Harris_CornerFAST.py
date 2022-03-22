"""Corner Detection(Harris Corner, FAST)"""
import cv2
import numpy as np

img = cv2.imread('D:\TestImage\SK-1_FRAME_IMAGE\F2_F2.png', cv2.IMREAD_COLOR)
#img = cv2.imread('D:\TestImage\Grid\GridResize.jpg', cv2.IMREAD_COLOR)
#코너검출
corners = cv2.cornerHarris(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), 2, 3, 0.04)

corners = cv2.dilate(corners, None)

show_img = np.copy(img)
show_img[corners>0.1*corners.max()]=[0,0,255]

corners = cv2.normalize(corners, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
show_img = np.hstack((show_img, cv2.cvtColor(corners, cv2.COLOR_GRAY2BGR)))

#outfile = open("D:\TestImage\points_NORM_MINMAX.txt", "w")
for p in corners:
    cv2.circle(show_img, (int(p[0]),int(p[1])), 2, (0, 255, 0), cv2.FILLED)#tuple(p)
    #outfile.write("%s,%s,%s\n" %(p[0],p[1],p[2]))
    
#outfile.close()

cv2.imshow('Harris corner detetor', show_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

#outfile = open("D:\TestImage\Grid_FAST_FEATURE.txt", "w")

fast = cv2.FastFeatureDetector_create(30, True, cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
kp = fast.detect(img)

show_img = np.copy(img)
for p in cv2.KeyPoint_convert(kp):
    cv2.circle(show_img, (int(p[0]),int(p[1])), 2, (0, 255, 0), cv2.FILLED)#tuple(p)
    #outfile.write("%s,%s\n" %(p[0],p[1]))
    
#outfile.close()

cv2.imshow('FAST corner detector', show_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
    
#outfile = open("D:\TestImage\points_setNonmaxSuppression.txt", "w")
fast.setNonmaxSuppression(False)
kp = fast.detect(img)

for p in cv2.KeyPoint_convert(kp):
    cv2.circle(show_img, (int(p[0]),int(p[1])), 2, (0, 255, 0), cv2.FILLED)
    #outfile.write("%s,%s\n" %(p[0],p[1]))
    
#outfile.close()

cv2.imshow('FAST corner detector', show_img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()