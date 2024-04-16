# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:21:56 2024

@author: jayiu
"""

import cv2 as cv
img = cv.imread("C:/com_vision/source/image/mot_color70.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray, None)
gray = cv.drawKeypoints(gray, kp, None, flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow("sift", gray)

cv.waitKey()
cv.destroyAllWindows()
print(len(kp)) 