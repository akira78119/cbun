#Pedestrian detection using HoG-SVM
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('D:\TestImage\people.jpg')
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor.getDefaultPeopleDetector())

#검출
locations, weights = hog.detectMultiScale(image)

dbg_image = image.copy()
for loc in locations:
    cv2. rectangle(dbg_image, (loc[0], loc[1]),
                   (loc[0]+loc[2], loc[1]+loc[3]), (0, 255, 0), 2)
    
plt.figure(figsize=(12,6))
plt.subplot(121)
plt.title('original')
plt.axis('off')
plt.imshow(image[:,:,[2,1,0]])
plt.subplot(122)
plt.title('detections')
plt.axis('off')
plt.imshow(dbg_image[:,:,[2,1,0]])
plt.tight_layout()
plt.show()