#W11 Report2
import cv2
import numpy as np

fileName1 = []
fileName2 = []
fileName1.append('D:\TestImage\stitching\boat1.jpg')
fileName2.append('D:\TestImage\stitching\boat2.jpg')
fileName1.append('D:\TestImage\stitching\budapest1.jpg')
fileName2.append('D:\TestImage\stitching\budapest2.jpg')
fileName1.append('D:\TestImage\stitching\newspaper1.jpg')
fileName2.append('D:\TestImage\stitching\newspaper2.jpg')
fileName1.append('D:\TestImage\stitching\s1.jpg')
fileName2.append('D:\TestImage\stitching\s2.jpg')


for id in range(len(fileName1)):
    img1 = cv2.imread(fileName1[id], cv2.IMREAD_COLOR)
    img2 = cv2.imread(fileName2[id], cv2.IMREAD_COLOR)

    sizeX = img1.shape[1]
    scale = 1200 / sizeX
    scale = scale / 2

    #Surf
    detectorSurf = cv2.xfeatures2d.SURF_create(10000)
    keypointSurf1, featureSurf1 = detectorSurf.detectAndCompute(img1, None)
    keypointSurf2, featureSurf2 = detectorSurf.detectAndCompute(img2, None)

    matcherSurf = cv2.BFMatcher_create(cv2.NORM_L2, False)
    matchesSurf = matcherSurf.match(featureSurf1, featureSurf2)

    pointsSurf1 = np.float32([keypointSurf1[m.queryIdx].pt for m in matchesSurf]).reshape(-1,1,2)
    pointsSurf2 = np.float32([keypointSurf2[m.trainIdx].pt for m in matchesSurf]).reshape(-1,1,2)

    H_Surf, maskSurf = cv2.findHomography(pointsSurf1, pointsSurf2, cv2.RANSAC, 5.0)

    imgAllMatch = cv2.drawMatches(img1, keypointSurf1, img2, keypointSurf2, matchesSurf, None)
    imgFilteredMatch = cv2.drawMatches(img1, keypointSurf1, img2, keypointSurf2, [m for i, m in enumerate(matchesSurf) if maskSurf[i]], None)
    imgAllMatch = cv2.resize(imgAllMatch, dsize=(0, 0), fx=scale, fy=scale)
    imgFilteredMatch = cv2.resize(imgFilteredMatch, dsize=(0, 0), fx=scale, fy=scale)
    cv2.imshow('Surf all match', imgAllMatch)
    cv2.imshow('filtered matches', imgFilteredMatch)
    cv2.waitKey()
    cv2.destroyAllWindows()

    #SIFT
    detectorSIFT = cv2.xfeatures2d.SIFT_create(50)

    keypointSIFT1, featureSIFT1 = detectorSIFT.detectAndCompute(img1, None)
    keypointSIFT2, featureSIFT2 = detectorSIFT.detectAndCompute(img2, None)

    matcherSIFT = cv2.BFMatcher_create(cv2.NORM_L2, False)
    matchesSIFT = matcherSIFT.match(featureSIFT1, featureSIFT2)

    pointsSIFT1 = np.float32([keypointSIFT1[m.queryIdx].pt for m in matchesSIFT]).reshape(-1, 1, 2)
    pointsSIFT2 = np.float32([keypointSIFT2[m.trainIdx].pt for m in matchesSIFT]).reshape(-1, 1, 2)

    H, maskSIFT = cv2.findHomography(pointsSIFT1, pointsSIFT2, cv2.RANSAC, 5.0)

    imgAllMatch = cv2.drawMatches(img1, keypointSIFT1, img2, keypointSIFT2, matchesSIFT, None)
    imgFilteredMatch = cv2.drawMatches(img1, keypointSIFT1, img2, keypointSIFT2, [m for i, m in enumerate(matchesSIFT) if maskSIFT[i]], None)
    imgAllMatch = cv2.resize(imgAllMatch, dsize=(0, 0), fx=scale, fy=scale)
    imgFilteredMatch = cv2.resize(imgFilteredMatch, dsize=(0, 0), fx=scale, fy=scale)
    cv2.imshow('SIFT all match', imgAllMatch)
    cv2.imshow('filtered matches', imgFilteredMatch)
    cv2.waitKey()
    cv2.destroyAllWindows()

    #ORB
    detectorORB = cv2.ORB_create(100)
    keypointORB1, featureORB1 = detectorORB.detectAndCompute(img1, None)
    keypointORB2, featureORB2 = detectorORB.detectAndCompute(img2, None)

    matcherORB = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
    matchesORB = matcherORB.match(featureORB1, featureORB2)

    pointsORB1 = np.float32([keypointORB1[m.queryIdx].pt for m in matchesORB]).reshape(-1, 2)
    pointsORB2 = np.float32([keypointORB2[m.trainIdx].pt for m in matchesORB]).reshape(-1, 2)
    H, maskORB = cv2.findHomography(pointsORB1, pointsORB2, cv2.RANSAC, 3.0)

    imgAllMatch = cv2.drawMatches(img1, keypointORB1, img2, keypointORB2, matchesORB, None)
    imgFilteredMatch = cv2.drawMatches(img1, keypointORB1, img2, keypointORB2,
                                       [m for i, m in enumerate(matchesORB) if maskORB[i]], None)
    imgAllMatch = cv2.resize(imgAllMatch, dsize=(0, 0), fx=scale, fy=scale)
    imgFilteredMatch = cv2.resize(imgFilteredMatch, dsize=(0, 0), fx=scale, fy=scale)
    cv2.imshow('orb all match', imgAllMatch)
    cv2.imshow('filtered matches', imgFilteredMatch)
    cv2.waitKey()
    cv2.destroyAllWindows()