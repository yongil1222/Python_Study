import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('E:/Python_Study/OpenCV/images/example2.jpg')

def hist2D_1():
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0, 180, 0, 256])

    cv2.imshow('hist2D_1', hist)

def hist2D_2():
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0, 180, 0, 256])

    plt.imshow(hist, interpolation='nearest')
    plt.show()

def HSVmap():
    hsvmap = np.zeros((180,256,3), np.uint8)
    h, s = np.indices(hsvmap.shape[:2])

    hsvmap[:,:,0] = h
    hsvmap[:,:,1] = s
    hsvmap[:,:,2] = 255

    hsvmap = cv2.cvtColor(hsvmap, cv2.COLOR_HSV2BGR)

    cv2.imshow('HSVmap', hsvmap)

#hist2D_1()
#hist2D_2()
HSVmap()

cv2.waitKey(0)
cv2.destroyAllWindows()