import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QFont

from ui_Widget import Ui_Form

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    @pyqtSlot()
    def on_btn_AlignLeft_clicked(self):
        self.ui.lineEdit_Input.setAlignment(Qt.AlignLeft)
    @pyqtSlot()
    def on_btn_AlignCenter_clicked(self):
        self.ui.lineEdit_Input.setAlignment(Qt.AlignCenter)
    @pyqtSlot()
    def on_btn_AlignRight_clicked(self):
        print('靠右')
        self.ui.lineEdit_Input.setAlignment(Qt.AlignRight)

    @pyqtSlot(bool)
    def on_btn_FontBold_clicked(self,checked):
        font = self.ui.lineEdit_Input.font()
        font.setBold(checked)
        self.ui.lineEdit_Input.setFont(font)

    @pyqtSlot(bool)
    def on_btn_FontItalic_clicked(self,checked):
        font = self.ui.lineEdit_Input.font()
        font.setItalic(checked)
        self.ui.lineEdit_Input.setFont(font)

    @pyqtSlot(bool) # 设置下划线
    def on_btn_FontUnderLine_clicked(self,checked):
        font = self.ui.lineEdit_Input.font()
        font.setUnderline(checked)
        font.setPointSize(16) # 设置字体大小
        self.ui.lineEdit_Input.setFont(font)


    @pyqtSlot(bool)
    def on_checkBox_ReadOnly_clicked(self,checked):
        self.ui.lineEdit_Input.setReadOnly(checked)

    @pyqtSlot(bool)
    def on_checkBox_Enabled_clicked(self,checked):
        self.ui.lineEdit_Input.setEnabled(checked)

    @pyqtSlot(bool)
    def on_checkBox_ClearButtonEnabled_clicked(self,checked):
        self.ui.lineEdit_Input.setClearButtonEnabled(checked)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
