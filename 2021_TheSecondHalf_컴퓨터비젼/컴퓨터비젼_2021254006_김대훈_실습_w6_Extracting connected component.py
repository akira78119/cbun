#Extracting connected component
import cv2, numpy as np

img = cv2.imread('C:\Bnw.png',cv2.IMREAD_GRAYSCALE)

connectivity = 8
num_labels, labelmap = cv2.connectedComponents(img, connectivity, cv2.CV_32S)

img = np.hstack((img, labelmap.astype(np.float32)/(num_labels - 1)))
cv2.imshow('Connected components', img)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.imread('C:\Lena.png', cv2.IMREAD_GRAYSCALE)
otsu_thr, otsu_mask = cv2.threshold(img, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

output = cv2.connectedComponentsWithStats(otsu_mask, connectivity, cv2.CV_32S)

num_labels , labelmap, stats, centers = output

colored = np.full((img.shape[0], img.shape[1],3),0, np.uint8)

for i in range(1, num_labels):
    if stats[i][4] > 200:
        colored[labelmap == i] = (0, 255*i/num_labels, 255*(num_labels-i)/num_labels)
        cv2.circle(colored, (int(centers[i][0]), int(centers[i][1])), 5, (255, 0,0), cv2.FILLED)
        
img = cv2.cvtColor(otsu_mask*255, cv2.COLOR_GRAY2BGR)

cv2.imshow('Connected components',np.hstack((img,colored)))
cv2.waitKey()
cv2.destroyAllWindows()