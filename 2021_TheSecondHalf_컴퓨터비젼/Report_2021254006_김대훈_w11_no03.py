#W11 Report3
import cv2
import numpy as np
import glob

imagesPath = []

imagesPath.append(list(sorted(glob.glob('D:\TestImage\stitching\s*.jpg'))))
imagesPath.append(list(sorted(glob.glob('D:\TestImage\stitching\ewspaper*.jpg'))))
imagesPath.append(list(sorted(glob.glob('D:\TestImage\stitching\budapest*.jpg'))))
imagesPath.append(list(sorted(glob.glob('D:\TestImage\stitching\boat*.jpg'))))

stitcher = cv2.createStitcher()

for i in range(len(imagesPath)):
    images = []
    for img_path in range(len(imagesPath[i])):
        images.append(cv2.imread(imagesPath[i][img_path], cv2.IMREAD_COLOR))

    ret, pano = stitcher.stitch(images)

    images.clear()
    sizeX = pano.shape[1]
    scale = 1200 / sizeX
    if ret == cv2.STITCHER_OK:
        pano = cv2.resize(pano, dsize=(0,0), fx=scale, fy=scale)
        cv2.imshow('panorama', pano)
        cv2.waitKey()
        cv2.destroyAllWindows()

    else:
        print('error during stitching')