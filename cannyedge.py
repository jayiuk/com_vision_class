# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:45:13 2024

@author: jayiu
"""

import cv2 as cv
img = cv.imread("C:/com_vision/source/image/soccer.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny_1 = cv.Canny(gray, 50, 150)
canny_2 = cv.Canny(gray, 100, 200)

cv.imshow('original', gray)
cv.imshow('canny1', canny_1)
cv.imshow('canny2', canny_2)

cv.waitKey()
cv.destroyAllWindows()