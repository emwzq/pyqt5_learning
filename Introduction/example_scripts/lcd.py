#coding:utf-8
 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)
 
class SigSlot(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.setWindowTitle('slider')
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal,self)
         
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)
         
        self.setLayout(vbox)
         
        slider.valueChanged.connect(lcd.display)
        slider.valueChanged.connect(self.display)
        self.resize(350,250)

    def display(self,event):
        print(event)
         
app = QApplication([])
qb = SigSlot()
qb.show()
sys.exit(app.exec_())
