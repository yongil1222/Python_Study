import numpy as np
import cv2

def pyramid():
    img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg', cv2.IMREAD_GRAYSCALE)
    tmp = img.copy()

    win_titles = ['Level 1', 'Level 2', 'Level 3']
    g_down = []
    g_up = []
    img_shape = []

    g_down.append(tmp)
    img_shape.append(tmp.shape)

    for i in range(3):
        tmp1 = cv2.pyrDown(tmp)
        g_down.append(tmp1)
        img_shape.append(tmp1.shape)
        tmp = tmp1
    
    for i in range(3):
        tmp = g_down[i]
        tmp1 = cv2.pyrUp(tmp)
        tmp = cv2.resize(tmp1, dsize=(img_shape[i][1], img_shape[i][0]), interpolation=cv2.INTER_CUBIC)
        g_up.append(tmp)
    
    for i in range(3):
        tmp = cv2.subtract(g_down[i], g_up[i])
        cv2.imshow(win_titles[i], tmp)
    
    pyr = cv2.add(g_down[0], g_up[0])
    added = cv2.add(img, pyr)
    cv2.imshow('result' , added)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

pyramid()