# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:08:25 2024

@author: jayiu
"""

from PyQt5.QtWidgets import *
import sys
import winsound

class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('삑 소리 내기')
        self.setGeometry(200, 200, 500, 100)
        
        short_b = QPushButton('짧게 삑', self)
        long_b = QPushButton('길게 삑', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('hi', self)
        
        short_b.setGeometry(10, 10, 100, 30)
        long_b.setGeometry(110, 10, 100, 30)
        quitButton.setGeometry(210, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 70)
        
        short_b.clicked.connect(self.short_b_f)
        long_b.clicked.connect(self.long_b_f)
        quitButton.clicked.connect(self.quit_f)
        
        
    def short_b_f(self):
        self.label.setText('주파수1000, 0.5초동안 소리냄')
        winsound.Beep(1000, 500)
        
    def long_b_f(self):
        self.label.setText('주파수 1000, 3초동안 소리냄')
        winsound.Beep(1000, 3000)
        
    def quit_f(self):
        self.close()
        
app = QApplication(sys.argv)
win = BeepSound()
win.show()
app.exec_()