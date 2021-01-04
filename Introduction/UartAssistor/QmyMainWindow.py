import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5. QtCore import pyqtSlot
from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parrent=None):
        super().__init__(parrent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('串口调试助手')

        self.i = 0


    @pyqtSlot()
    def on_btnSerial_clicked(self):
        i_str = '%d'%self.i
        self.ui.comboBox_SerialPort.addItem(i_str)
        self.i +=1

        bps = self.ui.comboBox_Baudrate.currentText()
        print(type(bps))
        print(bps)

    @pyqtSlot()
    def on_checkBox_RxHex_clicked(self):
        checked = self.ui.checkBox_RxHex.isChecked()
        if checked :
            print('16进制接受')
        else:
            print('ASCII 接收')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QmyMainWindow()
    ex.show()
    sys.exit(app.exec_())
