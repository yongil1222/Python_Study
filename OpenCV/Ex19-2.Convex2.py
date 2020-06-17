import numpy as np
import cv2

def convex_rect():
    img = cv2.imread('E:/Python_Study/OpenCV/images/star.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(img_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[5]

    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.drawContours(img, [box], 0, (0,255,0), 3)

    cv2.imshow('rectangle', img)

def convex_circle():
    img = cv2.imread('E:/Python_Study/OpenCV/images/star.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = img.shape[:2]

    ret, thr = cv2.threshold(img_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[5]

    (x,y), r = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    r = int(r)

    cv2.circle(img, center, r, (255,0,0), 3)

    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipse, (0,255,0), 3)

    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    ly = int((-x*vy/vx)+y)
    ry = int(((cols-x)*vy/vx)+y)

    cv2.line(img, (cols-1, ry), (0,ly), (0,0,255), 2)

    cv2.imshow('fitting', img)

convex_rect()
convex_circle()

cv2.waitKey(0)
cv2.destroyAllWindows()
