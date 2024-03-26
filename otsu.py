# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:40:05 2024

@author: jayiu
"""

import cv2 as cv
import sys

img = cv.imread("C:/com_vision/source/image/soccer.jpg")

if img is None:
    sys.exit('cant find file')
    
t, bin_img = cv.threshold(img[:, :, 2], 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print("오츄 알고리즘으로 찾은 최적의 임계값", t)

cv.imshow('R Channel', img[:, :, 2])
cv.imshow('R Channel binarization', bin_img)

cv.waitKey()
cv.destroyAllWindows()