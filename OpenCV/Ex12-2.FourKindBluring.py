import numpy as np
import cv2

def onChange(x):
    pass

def bluring():
    img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg')
    
    cv2.namedWindow('BlurPane')
    cv2.createTrackbar('Blur Mode', 'BlurPane', 0, 2, onChange)
    cv2.createTrackbar('Blur', 'BlurPane', 0, 20, onChange)

    while(1) :
        mode = cv2.getTrackbarPos('Blur Mode', 'BlurPane')
        val = cv2.getTrackbarPos('Blur', 'BlurPane')*2 + 1

        try:
            if mode == 0:
                blur = cv2.blur(img, (val, val))
            elif mode == 1:
                blur = cv2.GaussianBlur(img, (val, val), 0)
            elif mode == 2:
                blur = cv2.medianBlur(img, val)
            else:
                break
            
            cv2.imshow('BlurPane', blur)
        except:
            break

        if(cv2.waitKey(1) == 27):
            break
    
    cv2.destroyAllWindows()

bluring()
