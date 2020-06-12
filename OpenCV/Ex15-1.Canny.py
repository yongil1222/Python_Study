import numpy as np
import cv2
import matplotlib.pyplot as plt

def canny():
    img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg', cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)

    cv2.imshow('original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()