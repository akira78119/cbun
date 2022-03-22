#Image segmentation using watershed
import cv2
import numpy as np
from random import randint

img = cv2.imread('D:\TestImage\lena.png')
show_img = np.copy(img)

seeds = np.full(img.shape[0:2], 0 , np.int32)
segmentation = np.full(img.shape, 0, np.uint8)

n_seeds = 9

colors = []
for m in range(n_seeds):
    colors.append((255 * m / n_seeds, randint(0, 255), randint(0, 255)))
    
mouse_pressed = False
current_seed = 1
seeds_updateed = False

def mouse_callback(event, x, y, flags, param):
    global mouse_pressed, seeds_updateed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        cv2.circle(seeds, (x, y), 5, (current_seed), cv2.FILLED)
        cv2.circle(show_img, (x,y), 5, colors[current_seed - 1], cv2.FILLED)
        seeds_updateed = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv2.circle(seeds, (x,y), 5, (current_seed), cv2.FILLED)
            cv2.circle(show_img, (x,y), 5, colors[current_seed - 1], cv2.FILLED)
            seeds_updateed = True
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
         
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('segmaentation', segmentation)
    cv2.imshow('image', show_img)
    
    k = cv2.waitKey(1)
    
    if k == 27:
        break
    elif k ==ord('c'):
        show_img = np.copy(img)
        seeds = np.full(img.shape[0:2], 0, np.int32)
        segmentation = np.full(img.shape, 0, np.uint8)
    elif k > 0 and chr(k).isdigit():
        n = int(chr(k))
        if 1 <= n <= n_seeds and not mouse_pressed:
            current_seed = n
            
    if seeds_updateed and not mouse_pressed:
        seeds_copy = np.copy(seeds)
        cv2.watershed(img, seeds_copy)
        segmentation = np.full(img.shape, 0, np.uint8)
        for m in range(n_seeds):
            segmentation[seeds_copy == (m + 1)] = colors[m]
            
        seeds_updateed = False
        
cv2.destroyAllWindows()
    