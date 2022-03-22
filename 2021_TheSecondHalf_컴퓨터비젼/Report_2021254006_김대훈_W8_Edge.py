""" Mid-Term Projrct 2021254006 김대훈"""
import math
import cv2, numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\TestImage\_2dBumps.png',0)
assert img is not None

img_color = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)    #결과 보여줄 이미지
img_Buf = np.copy(img)                              #필터 적용 버퍼 이미지
img_show = np.copy(img)                             #현재까지 진행 된 결과 이미지
img_bb = np.copy(img)                               #마우스 선택 이미지
width, height = img.shape[1], img.shape[0]

cnt = 1
kernelSize = 3
kernel =np.ones((kernelSize, kernelSize),np.uint8)

rect_Seleted = False
mouse_pressed = False
s_x,s_y,e_x,e_y = 0,0,0,0
mode = -1

#선택 된 circle만 표기 함수
def show_result(circle):
    img_color = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)    #버퍼에 원본 복사
    for i in circle[0,:]:
        nDist = math.sqrt(pow(abs(e_y-i[1]),2) + pow(abs(e_x-i[0]),2))
        if nDist < i[2]:
            cv2.circle(img_color,(i[0],i[1]),i[2],(0,55,0),2)
    cv2.imshow("defect image", img_color)
    
def mouse_callback(event, _x, _y, flags, param):
    global img, img_bb, img_show, s_x,s_y,e_x,e_y, mouse_pressed, rect_Seleted
    
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = _x,_y
        
    elif event == cv2.EVENT_MOUSEMOVE:
       if  mouse_pressed:
           e_x, e_y = _x,_y
           img_bb = np.copy(img_show)
           cv2.rectangle(img_bb, (s_x,s_y), (e_x,e_y), (255,0,255),2)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        rect_Seleted = True
        e_x, e_y = _x,_y
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)
cv2.waitKey(1)

finish = False
while not finish:
    cv2.imshow("image", img_show)
    key = cv2.waitKey(1)

    if key == ord('b') or key == ord('B'): #Edge # Canny #bilateralFilter
        #img_show = cv2.bilateralFilter(img_show, 11, 17, 17) #Blur to reduce noise 
        img_Buf = cv2.Canny(img_show, 130, 200) 
        #img_Buf = cv2.bilateralFilter(img_show, -1, 0.3, 10)
        #kernel = cv2.getGaborKernel((21,31), 5, 1, 10, 1, 0, cv2.CV_32F)
        #kernel /= math.sqrt((kernel*kernel).sum())
        #img_Buf = cv2.filter2D(img_show, -1, kernel)
    elif key == ord('g') or key == ord('G'): #Gausian
        img_Buf = cv2.GaussianBlur(img_show, (5,5),0)
    elif key == ord('s') or key == ord('S'): #Sobel
        img_Buf = cv2.Sobel(img_show, cv2.CV_8U, 1, 1)
    elif key == ord('e') or key == ord('E'): #Erosion
        img_Buf = cv2.morphologyEx(img_show, cv2.MORPH_ERODE, kernel, iterations=cnt)
    elif key == ord('d') or key == ord('D'): #Dilation
        img_Buf = cv2.morphologyEx(img_show, cv2.MORPH_DILATE, kernel, iterations=cnt) 
    elif key == ord('o') or key == ord('O'): #Opening
        img_Buf = cv2.morphologyEx(img_show, cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel), iterations=cnt)
    elif key == ord('c') or key == ord('C'): #Closing
        img_Buf = cv2.morphologyEx(img_show, cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel), iterations=cnt)
    elif key == ord('x') or key == ord('X'): #xDelete
        img_show = np.copy(img)
        img_Buf = np.copy(img_show)
    elif key == ord('a') or key == ord('A'): #Calc
        #circle = cv2.HoughCircles(img_show, cv2.HOUGH_GRADIENT_ALT, 1, 10, 40, 80, 0, 0)
        circle = cv2.HoughCircles(img_show, cv2.HOUGH_GRADIENT, 1, 25, 30, 100, 30, 0, 255)
        print(circle)
        circle = np.uint16(np.around(circle))

        show_result(circle) #결과 함수 호출
        
        #contours , _ = cv2.findContours(img_Buf, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #print("contours!", contours)
        #contour = contours[1]
        #print("contour!", contour)
        #ellipse = cv2.fitEllipse(contour)
        #print("ellipse!", ellipse)
        # 반환된 값은 타원그리기 인자로 바로 활용할 수 있음.
        #cv2.ellipse(img_color, ellipse, (125,0,0), 3)
        
        #cv2.ellipse(img, center, axes, angle, 0, 360,(0,255,0),3)
        #ellipse = cv2.fitEllipse(pts)
        #cv2.ellipse(img, ellipse, (0,255,255), 3)
    elif rect_Seleted:
        rect_Seleted = False
        print("Seleted mouse position ",e_x, e_y)
    elif key == 27:
        break

    img_show = np.copy(img_Buf)
    
cv2.destroyAllWindows()
