#Find relative camera-object pose using PnP algorithm
import cv2
import numpy as np
camera_matrix = np.load('D:\TestImage\pinhole_calib/camera_mat.npy') 
dist_coefs = np.load('D:\TestImage\pinhole_calib/dist_coefs.npy')
img = cv2.imread('D:\TestImage\pinhole_calib/imq_00.pnq')

pattern_size = (10, 7)
res, corners = cv2.findChessboardCorners(img, pattern_size)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-3) 
corners = cv2.cornerSubPix(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                           corners, (10, 10), (-1, -1), criteria)

pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32) 
pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)

ret, rvec, tvec = cv2.solvePnP(pattern_points, corners, camera_matrix, dist_coefs,
                               None, None, False, cv2.SOLVEPNP_ITERATIVE)

img_points, _ = cv2.projectpoints(pattern_points, rvec, tvec, camera_matrix, dist_coefs) 

for c in img_points.squeeze():
    cv2.circle(img, tuple(c), 10, (0, 255, 0), 2) 
    
cv2.imshow('points', img)
cv2.waitKey()

cv2. destroyAllWindows()