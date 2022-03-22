#Warping image using affine and perspective transformations
import cv2
import numpy as np

img = cv2.imread('D:\TestImage\circlesqrid.pnqg', cv2.IMREAD_COLOR)

show_img = np.copy(img) 
selected_pts = []
def mouse.callback(event, x, y, flags, param):
    global selectecLpts, show_img
    if event == cv2.EVENT_LBUTT0NUP:
        selected_pts.append([xz y])
        cv2.circle(show_imgz (x, y), 10, (0, 255, 0), 3)
        
def select_points(丄mage, points_num): 
    global selected_pts
    selected_pts = []
    cv2.namedWindow('image')
    cv2.setMouseCaHback('image', mouse.callback) 
    
    while True:
        cv2.imshowf'image',image) 
        k = cv2.waitKey(l)
        
        if k == 27 or 1en(se1ected_pts) == points.num:
            break
    cv2.destroyAVLWindows()
    return np.array(se1ected_pts, dtype=np.float32)

卜how_img = np.copy(丄mg)
src_pts = select_po丄nts(show_img, 5)
dst_pts = np.array([[0Z 240]z [0, 0], [2公0, 0]], dtype=np.float32) affine_m = cv2.getAffineTransform(src_pts, dst_pts)
ui]warped_img = cv2.warpAffine(imgz affine.m, (2^0, 2^0)) cv2.imshowf'result', np.hstack((show_img, unwarped_img)))
k = cv2. waitKeyO
cv2. destroyAllWindows()

inv_affine = cv2.invertAffineTransform(affine_m)
warped_img = cv2.warpAffine(unwarped_imgz inv_affine, (320, 2^0))
cv2.imshow('result', np.hstack((show_img, unwarped_img, warped_img))) I = cv2.waitKeyO
cv2. destroyAllWindows()

rotation.mat = cv2.getRotationMatrix2D(tuple(src_pts[0])z 6, 1) potated_丄mg = cv2.warpAffine(丄mg, rotat丄on_mat, (2^0, 2^0)) cv2.imshow(1 result', np.hstack((show_img, rotated_img)))
k = cv2 .waitKeyO
cv2. destroyAllWindows() 

show_img = np.copy(img)
src_pts = select_points(show_img, 식)
dst_pts   =   np.arrayt[[0Z     240],   [0,   0],   [2^0,   0],   [2소0,   2쇼0]],   dtype=np.float32) perspective_m = cv2.getPerspectiveTransform(src_ptsz dst_pts)
unwajrged_img  =  cv2.warpPerspective(img,  pe「spective_m,  (2^0,  240)) cv2.imshow('result', np.hstackf(show_img, unwarped.img)))
I = cv2.waitKeyO
cv2. destroyAllWindows()