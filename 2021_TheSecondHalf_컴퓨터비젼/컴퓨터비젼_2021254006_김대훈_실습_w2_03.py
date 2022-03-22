import argparse
import cv2, numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', default='C:\Lena.png',help='Image path')
params = parser.parse_args()
img = cv2.imread(params.path)
image_to_Buf = np.copy(img)
image_to_show = np.copy(img)
width, height = img.shape[1], img.shape[0]

mouse_pressed = False
s_x,s_y,e_x,e_y = 0,0,0,0
mode = -1

def mouse_callback(event, x, y, flags, param):
    global img, image_to_Buf, image_to_show, s_x,s_y,e_x,e_y, mouse_pressed
    
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        s_x, s_y = x,y
        image_to_show = np.copy(image_to_Buf)
        
    elif event == cv2.EVENT_MOUSEMOVE:
       if  mouse_pressed:
           e_x, e_y = x,y
           image_to_show = np.copy(image_to_Buf)
           
           if mode == 1:
               cv2.line(image_to_show, (s_x,s_y), (e_x,e_y), (255,0,0),3)
           elif mode == 2:
               cv2.rectangle(image_to_show, (s_x,s_y), (e_x,e_y), (0,0,255),3)
           elif mode == 3:
               cv2.arrowedLine(image_to_show, (s_x,s_y), (e_x,e_y), (0,255,0),3)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        e_x, e_y = x,y
        image_to_Buf = np.copy(image_to_show)
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

finish = False
while not finish:
    cv2.imshow("image", image_to_show)
    key = cv2.waitKey(1)

    if key == ord('l'):
        mode = 1        
        #print('sx=',s_x,'sy=',s_y,'ex=',e_x,'ey=',e_y)
    elif key == ord('r'):
        mode = 2
    elif key == ord('a'):
        mode = 3
    elif key == ord('c'):
        image_to_show = np.copy(img)
        image_to_Buf = np.copy(image_to_show)
    elif key == ord('w'):
        cv2.imwrite("D:\Lena_draw.png",image_to_Buf,[cv2.IMWRITE_JPEG_QUALITY,0])
    elif key == 27:
        break
    
cv2.destroyAllWindows()
