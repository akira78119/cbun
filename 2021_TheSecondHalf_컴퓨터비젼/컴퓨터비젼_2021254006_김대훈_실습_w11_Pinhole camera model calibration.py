#Pinhole camera model calibration

import cv2 
import numpy as np
import os

pattern_size = (10, 7)
samples = []
file_list = os.listdir('D:\TestImage\pinhole_calib2')
img_file_list = [file for file in file_list if file.startswith('img')]

for filename in img_file_list:
    frame = cv2.imread(os.path.join('D:\TestImage\pinhole_calib2', filename)) 
    res, corners = cv2.findChessboardCorners(frame, pattern_size)
    
    img_show = np.copy(frame)
    cv2.drawChessboardCorners(img_show, pattern_size, corners, res)
    cv2.putText(img_show, 'Samples captured: %d' % len(samples), (0, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    cv2.imshow('chessboard', img_show)
    
    wait_time = 0 if res else 30
    k = cv2.waitKey(wait_time)
    
    if k == ord('s') and res:
        samples.append((cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), corners)) 
    elif k == 27:
        break


cv2. destroyAllWindows()

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 1e-3) 

for i in range(len(samples)):
    img, corners = samples[i]
    corners = cv2.cornerSubPix(img, corners, (10, 10), (-1,-1), criteria) 
    
pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)

images, corners = zip(*samples)

pattern_points = [pattern_points]*len(corners)

rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(
    pattern_points, corners, images[0].shape, None, None) 

np.save('camera_mat.npy', camera_matrix)
np.save('dist_coefs.npy', dist_coefs)

print(np.load('camera_mat.npy'))
print(np.load('dist_coefs.npy'))