# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 15:02:39 2024

@author: jayiu
"""

import cv2 as cv
import sys

img = cv.imread("C:/com_vision/source/image/soccer.jpg")

if img is None:
    sys.exit('파일을 찾을 수 없음')
    
cv.imshow('Original_RGB', img)
cv.imshow('Upper Left half', img[:img.shape[0]//2, :img.shape[1]//2, :])
cv.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4, img[1]//4:3*img[1]//4, :])
cv.imshow('B Channel', img[:, :, 0])
cv.imshow('G Channel', img[:, :, 1])
cv.imshow('R Channel', img[:, :, 2])
cv.waitKey()
cv.destroyAllWindows()