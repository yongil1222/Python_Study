import numpy as np
import cv2

def onChange(x):
    pass

def bluring():
    img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg')
    cv2.namedWindow('Blur Image')

    cv2.createTrackbar('Blur', 'Blur Image', 0, 50, onChange)

    while True:
        i = cv2.getTrackbarPos('Blur', 'Blur Image') + 1
        kernel = np.ones((i,i),np.float32)/i**2
        blur = cv2.filter2D(img, -1, kernel)
        cv2.imshow('Blur Image', blur)
    
        if( cv2.waitKey(1) == 27) :
            break

    cv2.destroyAllWindows()

bluring()