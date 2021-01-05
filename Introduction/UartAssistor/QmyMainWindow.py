import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5. QtCore import pyqtSlot,QTimer

from ui_MainWindow import Ui_MainWindow

import  serial
import  serial.tools.list_ports
import  re


class QmyMainWindow(QMainWindow):
    def __init__(self,parrent=None):
        super().__init__(parrent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('串口调试助手')

        
        # 串口相关操作
        self.ser    = serial.Serial()
        self.currentCom = 'COM1'
        self.currentBps = 9600
        self.on_btnSerial_clicked()
       
        # 定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.serial_monitor)
        self.timer.start(100)

    ######## 串口操作相关函数   ##################
    def get_serial_ports(self):
        ports_ = list( serial.tools.list_ports.comports() )
        self.ports = {}
        for i in ports_:
            # i[0] -- 端口号
            # i[1] -- 端口名或描述
            self.ports[i[1]] = i[0]

    ######## PyQt 界面绑定函数  ##################
    @pyqtSlot()
    def on_btnSerial_clicked(self):
        self.get_serial_ports()
        self.ui.comboBox_SerialPort.clear()
        for k in self.ports:
            self.ui.comboBox_SerialPort.addItem(k,self.ports[k])
            
    @pyqtSlot(str)
    def on_comboBox_SerialPort_currentIndexChanged(self,curText):
        com = self.ui.comboBox_SerialPort.currentData()
        self.currentCom = com
        self.ser.setPort( self.currentCom )

    @pyqtSlot(str)
    def on_comboBox_Baudrate_currentIndexChanged(self,curText):
        self.currentBps = int(curText)
        self.ser.baudrate = self.currentBps   

    @pyqtSlot()
    def on_checkBox_RxHex_clicked(self):
        checked = self.ui.checkBox_RxHex.isChecked()

    def on_btn_Clr_clicked(self):
        self.ui.textEdit_Rec.setPlainText('')

    @pyqtSlot()
    def on_btn_SerOpen_clicked(self):
        self.ser.setPort( self.currentCom )
        self.ser.baudrate = self.currentBps   
        self.timeout = 1
        self.ser.writeTimeout = 1
        if self.ser.isOpen() == False:
            self.ser.open()
            self.PrintLog( self.currentCom + ' open Sucess')
            return 1
        else:
            self.PrintLog( self.currentCom + ' had been opened')
            return 0
    @pyqtSlot()        
    def on_btn_SerClose_clicked(self):
        if self.ser.isOpen():
            self.ser.close()
            self.PrintLog( self.currentCom + ' Close success')
            

    @pyqtSlot()
    def on_btn_Send_clicked(self):
        text = self.ui.textEdit_Send.toPlainText()
        text_list = re.split(r'\s+',text)
        hex_list = []
        for i in text_list:
            if i != '':
                hex_list.append( int(i,16) )

        if self.ser.isOpen():
            if len(hex_list) != 0:
                self.ser.write( bytes( hex_list ) )

    def serial_monitor(self):
        self.timer.start(100)
        LineWrap = self.ui.chkBox_LineWrap.isChecked()
        if self.ser.isOpen():
            n = self.ser.inWaiting()
            if n != 0:
                checked = self.ui.checkBox_RxHex.isChecked()
                if (checked) :
                    data = list( self.ser.read(n) )
                    text = ''
                    for i in data:
                        text += '%02x '%i
                    if LineWrap:
                        self.PrintLog(text)
                    else:
                        self.ui.textEdit_Rec.insertPlainText(text)
                else:
                    text = str( self.ser.read(n) )
                    self.PrintLog(text)



    def PrintLog(self,text):
        self.ui.textEdit_Rec.appendPlainText(str(text) )



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QmyMainWindow()
    ex.show()
    sys.exit(app.exec_())
