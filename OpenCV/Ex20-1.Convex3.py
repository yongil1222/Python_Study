import numpy as np
import cv2

def convex():
    img = cv2.imread('E:/Python_Study/OpenCV/images/korea.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(img_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[18]

    mmt = cv2.moments(cnt)
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    x, y, w, h = cv2.boundingRect(cnt)
    korea_rect_area = w * h
    korea_area = cv2.contourArea(cnt)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    ellipse = cv2.fitEllipse(cnt)

    leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
    rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
    toptmost = tuple(cnt[cnt[:,:,1].argmin()][0])
    bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

    aspect_ratio = w / h
    extent = korea_area / korea_rect_area
    solidity = korea_area / hull_area

    print('Korea Aspect Ratio:\t%.3f' %aspect_ratio)
    print('Korea Extent:\t%.3f' %extent)
    print('Korea Solidity:\t%.3f' %solidity)
    print('Korea Orientation:\t%.3f' %ellipse[2])

    equivalent_diameter = np.sqrt(4*korea_area/np.pi)
    korea_radius = int(equivalent_diameter/2)

    cv2.circle(img, (cx, cy), 3, (255, 255, 255), -1)
    cv2.circle(img, (cx, cy), korea_radius, (0, 0, 255), 2)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.ellipse(img, ellipse, (50, 50, 50), 2)

    cv2.circle(img, (leftmost), 3, (0,0,255),-1)
    cv2.circle(img, (rightmost), 3, (0,0,255),-1)
    cv2.circle(img, (toptmost), 3, (0,0,255),-1)
    cv2.circle(img, (bottommost), 3, (0,0,255),-1)


    cv2.imshow('Korea Features', img)

convex();
cv2.waitKey(0)
cv2.destroyAllWindows()
