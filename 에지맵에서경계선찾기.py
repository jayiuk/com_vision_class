# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:58:57 2024

@author: jayiu
"""

import cv2 as cv
img = cv.imread("C:/com_vision/source/image/soccer.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 100, 200)

contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
lcontour = []

for i in range(len(contour)):
    if contour[i].shape[0] > 100:
        lcontour.append(contour[i])

cv.drawContours(img, lcontour, -1, (255, 0, 150), 3)
cv.imshow('original with contours', img)
cv.imshow('canny', canny)

cv.waitKey()
cv.destroyAllWindows()