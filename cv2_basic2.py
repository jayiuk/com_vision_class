# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:03:38 2024

@author: jayiu
"""

import cv2 as cv
import sys
img = cv.imread('C:/com_vision/source/image/soccer.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_small = cv.resize(gray, dsize = (0,0), fx = 0.5, fy = 0.5)
cv.imwrite('C:/com_vision/source/image/soccer_gray.jpg', gray)
cv.imwrite('C:/com_vision/source/image/soccer_gray_small.jpg', gray_small)
cv.imshow('Image Display', img)
cv.imshow('Gray Image', gray)
cv.imshow('Gray Image Small', gray_small)
cv.waitKey()
cv.destroyAllWindows()