import numpy as np
import cv2

def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.imshow('Image 1', img1)
    cv2.imshow('Image 2', img2)

    add_img1 = img1 + img2
    add_img2 = cv2.add(img1, img2)

    cv2.imshow('img1 + img2', add_img1)
    cv2.imshow('add(img1, img2)', add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

addImage('E:/Python_Study/OpenCV/images/example1.jpg', 'E:/Python_Study/OpenCV/images/example2.jpg')