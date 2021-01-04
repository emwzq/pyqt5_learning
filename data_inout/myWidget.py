import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot

from Ui_DataInputOutput import Ui_DataInputOutput

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_DataInputOutput()
        self.ui.setupUi(self)

    @pyqtSlot()
    def on_btn_Calculate_clicked(self):
        num = int(self.ui.lineEdit_Count.text())
        price = float(self.ui.lineEdit_Price.text())
        total = num * price
        self.ui.lineEdit_Total.setText('%0.2f' % total)

    @pyqtSlot(int)
    def on_spinBox_Count_valueChanged(self,count):
        price = self.ui.doubleSpinBox_Price.value()
        self.ui.doubleSpinBox_Total.setValue(count * price)
    
    @pyqtSlot(float)
    def on_doubleSpinBox_Price_valueChanged(self,price):
        count = self.ui.spinBox_Count.value()
        self.ui.doubleSpinBox_Total.setValue(count * price)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
