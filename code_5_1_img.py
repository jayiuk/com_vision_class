# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:59:50 2024

@author: user
"""

import cv2 as cv
import numpy as np

img = np.zeros([10, 10], np.float32) # 기본이 np.float64 / CV_32F를 쓸 것이라 맞추어줌 
for i in range(2,7):
    img[i,3:(i+2)] = 1

print(img)

ux = np.array([[-1, 0, 1]])
uy = np.array([[-1, 0, 1]]).transpose()
k = cv.getGaussianKernel(3, 1)
g = np.outer(k, k.transpose())
dy = cv.filter2D(img, cv.CV_32F, uy)
dx = cv.filter2D(img, cv.CV_32F, ux)
dyy = dy * dy
dxx = dx * dx
dyx = dy * dx
gdyy = cv.filter2D(dyy, cv.CV_32F, g)
gdxx = cv.filter2D(dxx, cv.CV_32F, g)
gdyx = cv.filter2D(dyx, cv.CV_32F, g)
C = (gdyy*gdxx-gdyx*gdyx)-0.04*(gdyy+gdxx)*(gdyy+gdxx)
for j in range(1, C.shape[0]-1):
    for i in range(1, C.shape[1]-1):
        if C[j, i] > 0.1 and sum(sum(C[j, i] > C[j-1:j+2, i-1:i+2])) == 8:
            img[j, i] = 9
np.set_printoptions(precision=2)
print(dy)
print(dx)
print(dyy)
print(dxx)
print(dyx)
print(gdyy)
print(gdxx)
print(gdyx)
print(C)
print(img)

popping = np.zeros([160, 160], np.uint8)
for j in range(0, 160):
    for i in range(0, 160):
        popping[j, i] = np.uint8((C[j//16, i//16]+0.06)*700)
cv.imshow('image display2', popping)
cv.waitKey()
cv.destroyAllWindows()