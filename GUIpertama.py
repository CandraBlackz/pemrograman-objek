# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:45:38 2017

@author: Capadesu
"""

import sys

from PyQt5.QtWidgets import *

class GUIpertama(QWidget):
        def __init__(self):
                super().__init__()
                self.initUI()
                
        def initUI(self):
            self.lbl1=QLabel("ANGKA 1 =",self)
            self.lbl2=QLabel("ANGKA 2 =",self)
            self.lbl3=QLabel("JUMLAH  =",self)
            self.tbl1=QPushButton("+",self)
            self.tbl2=QPushButton("-",self)
            self.tbl3=QPushButton("/",self)
            self.tbl4=QPushButton("*",self)
            self.tbl1.clicked.connect(self.Penjumlahan)
            self.tbl2.clicked.connect(self.Pengurangan)
            self.tbl3.clicked.connect(self.Pembagian)
            self.tbl4.clicked.connect(self.Perkalian)
            self.txt1=QLineEdit(self)
            self.txt2=QLineEdit(self)
            self.txt3=QLineEdit(self)
            self.lbl1.move(50,50)
            self.lbl2.move(50,75)
            self.lbl3.move(50,100)
            self.txt1.move(125,50)
            self.txt2.move(125,75)
            self.txt3.move(125,100)
            self.tbl1.move(125,125)
            self.tbl2.move(200,125)
            self.tbl3.move(200,150)
            self.tbl4.move(125,150)
            self.setGeometry(300,300,300,600)
            self.show()
            
        def Penjumlahan(self):
            self.Hasil1=int(self.txt1.text())+int(self.txt2.text())
            self.txt3.setText(str(self.Hasil1))
            
        def Pengurangan(self):
            self.Hasil2=int(self.txt1.text())-int(self.txt2.text())
            self.txt3.setText(str(self.Hasil2))
            
        def Pembagian(self):
            self.Hasil3=int(self.txt1.text())/int(self.txt2.text())
            self.txt3.setText(str(self.Hasil3))
            
        def Perkalian(self):
            self.Hasil4=int(self.txt1.text())*int(self.txt2.text())
            self.txt3.setText(str(self.Hasil4))
            
app1=QApplication(sys.argv)
GUI=GUIpertama()
sys.exit(app1.exec_())