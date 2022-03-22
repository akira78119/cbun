#Distorting and undistorting points
import cv2
import numpy as np

camera_matrix = np.load('D:\TestImage\Grid/camera_mat.npy')
dist_coefs = np.load('D:\TestImage\Grid/dist_coefs.npy')

img = cv2.imread('D:\TestImage\Grid/Grid_0.jpg') 
pattern_size = (10, 7)
res, corners = cv2.findChessboardCorners(img, pattern_size)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-3)
corners = cv2.cornerSubPix(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                           corners, (10, 10), (-1, -1), criteria)
h_corners = cv2.undistortPoints(corners, camera_matrix, dist_coefs)
h_corners = np.c_[h_corners.squeeze(), np.ones(len(h_corners))]

img_pts, _ = cv2.projectPoints(h_corners, (0, 0, 0), (0, 0, 0), camera_matrix, None)

for c in corners:
    cv2.circle(img, tuple(c[0]), 10, (0, 255, 0), 2)
    
for c in img_pts.squeeze().astype(np.float32):
    cv2.circle(img, tuple(c), 5, (0, 0, 255), 2)
    
cv2.imshow('undistorted corners', img)
#cv2.waitKey()
#cv2. destroyAllWindows()

img_pts, _ = cv2.projectPoints(h_corners, (0, 0, 0), (0, 0, 0), camera_matrix, dist_coefs)

for c in img_pts.squeeze().astype(np.float32):
    cv2.circle(img, tuple(c), 2, (255, 255, 0), 2)
    
cv2.imshow('reprojected corners', img)
cv2.waitKey()
cv2. destroyAllWindows()