# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:42:35 2024

@author: jayiu
"""

import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사진 특수 효과')
        self.setGeometry(200, 200, 800, 200)
        
        pictureButton = QPushButton('사진 읽기', self)
        embossButton = QPushButton('엠보싱', self)
        cartoonButton = QPushButton('카툰', self)
        sketchButton = QPushButton('스케치', self)
        oilButton = QPushButton('유화', self)
        saveButton = QPushButton('save', self)
        self.pickCombo.addItems(['엠보싱', '카툰','스케치(명암)', '스케치', '유화', 'save'])
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('welcome', self)
        
        pictureButton.setGeometry(10, 10, 100, 30)
        embossButton.setGeometry(110, 10, 100, 30)
        cartoonButton.setGeometry(210, 10, 100, 30)
        sketchButton.setGeometry(310, 10, 100, 30)
        oilButton.setGeometry(410, 10, 100, 30)
        saveButton.setGeometry(510, 10, 100, 30)
        self.pickCombo.setGeometry(510, 40, 110, 30)
        quitButton.setGeometry(620, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 170)
        
        pictureButton.clicked.connect(self.pictureOF)
        embossButton.clicked.connect(self.embossF)
        cartoonButton.clicked.connect(self.cartoonF)
        sketchButton.clicked.connect(self.sketchF)
        oilButton.clicked.connect(self.oilF)
        saveButton.clicked.connect(self.saveF)
        quitButton.clicked.connect(self.quitF)
        
    def pictureOF(self):
        fname = QFileDialog.getOpenFileName(self, '사진 읽기', './')
        self.img = cv.imread(fname[0])
        if self.img is None: sys.exit('cant find file')
        cv.imshow('Painting', self.img)
        
    def embossF(self):
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128,0,255))
        
        cv.imshow('Emboss', self.emboss)
        
    def cartoonF(self):
        self.cartoon = cv.stylization(self.img, sigma_s = 60, sigma_r = 0.45)
        cv.imshow('Cartoon', self.cartoon)
        
    def sketchF(self):
        self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s = 60, sigma_r = 0.07, shade_factor = 0.02)
        cv.imshow('sketch gray', self.sketch_gray)
        cv.imshow('sketch color', self.sketch_color)
        
    def oilF(self):
        self.oil = cv.xphoto.oilPainting(self.img, 10, 1, cv.COLOR_BGR2Lab)
        cv.imshow('Oil Painting', self.oil)