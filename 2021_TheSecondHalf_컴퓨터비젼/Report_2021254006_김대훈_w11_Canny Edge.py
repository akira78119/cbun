#W11 Report1
import cv2
import numpy as np
import matplotlib.pyplot as plt

fileName = []
fileName.append('D:\TestImage\stitching\boat1.jpg')
fileName.append('D:\TestImage\stitching\budapest1.jpg')
fileName.append('D:\TestImage\stitching\newspaper1.jpg')
fileName.append('D:\TestImage\stitching\s1.jpg')

for i in range(len(fileName)):
    img = cv2.imread(fileName[i], cv2.IMREAD_COLOR)

    #Canny Edge
    show_CannyImg = cv2.Canny(img, 200,100)

    #코너검출
    corners = cv2.cornerHarris(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 2, 3, 0.04)
    corners = cv2.dilate(corners, None)

    show_HarrisImg = np.copy(img)
    show_HarrisImg [corners > 0.1 * corners.max()] = [0,0,255]

    # Display
    plt.figure(figsize=[17, 6])
    plt.subplot(131)
    plt.axis('off')
    plt.title('Original color')
    plt.imshow(img[:, :, [2, 1, 0]])

    plt.subplot(132)
    plt.axis('off')
    plt.title('Canny Edge')
    plt.imshow(show_CannyImg, cmap='gray')

    plt.subplot(133)
    plt.axis('off')
    plt.title('Harris Corner')
    plt.imshow(show_HarrisImg[:, :, [2, 1, 0]])

    plt.tight_layout()
    plt.show()
