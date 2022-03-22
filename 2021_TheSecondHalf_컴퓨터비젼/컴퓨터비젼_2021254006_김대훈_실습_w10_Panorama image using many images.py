#Panorama image using many images
import cv2

images = []

images.append(cv2.imread('D:\TestImage\1.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('D:\TestImage\2.jpg', cv2.IMREAD_COLOR))

stitcher = cv2.createStitcher()
ret, pano = stitcher.stitch(images)

if ret == cv2.STITCHER_0K:
    pano = cv2.resize(pano, dsize=(0, 0), fx=0.2, fy=0.2) 
    cv2.imshow('panorama', pano)
    cv2.waitKey()
    
    cv2. destroyAllWindows()
else:
    print('Error during stichinq')