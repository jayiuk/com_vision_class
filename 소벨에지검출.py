# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:15:48 2024

@author: jayiu
"""

import cv2 as cv
img = cv.imread("C:/com_vision/source/image/soccer.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize = 3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize = 3)
sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv.imshow('original', gray)
cv.imshow('sobelx', sobel_x)
cv.imshow('sobely', sobel_y)
cv.imshow('edge strength', edge_strength)

cv.waitKey()
cv.destroyAllWindows()