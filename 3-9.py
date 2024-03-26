# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:28:04 2024

@author: jayiu
"""

import cv2 as cv
import numpy as np
import time

def my_cvtGray1(bgr_img):
    g = np.zeros([bgr_img.shape[0], bgr_img.shape[1]])
    for r in range(bgr_img.shape[0]):
        for c in range(bgr_img.shape[1]):
            g[r, c] = 0.114*bgr_img[r, c, 0] + 0.587 * bgr_img[r, c, 1] + 0.299*bgr_img[r, c, 2]
    return np.uint8(g)

def my_cvtGray2(bgr_img):
    g = np.zeros([bgr_img.shape[0], bgr_img.shape[1]])
    g = 0.114*bgr_img[:, :, 0] + 0.587*bgr_img[:, :, 1] + 0.299*bgr_img[:, :, 2]
    return np.uint8(g)

img = cv.imread("C:/com_vision/source/image/girl_laughing.jpg")

start = time.time()
my_cvtGray1(img)
print('my time1 : ', time.time()-start)

start = time.time()
my_cvtGray2(img)
print('my time2 : ', time.time() - start)

start = time.time()
cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print('opencv time : ', time.time() - start)