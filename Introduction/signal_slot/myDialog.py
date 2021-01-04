import sys
from PyQt5.QtWidgets import QWidget,QApplication,QDialog
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt,pyqtSlot
from ui_Dialog import Ui_Dialog

class QmyDialog(QDialog):
    def __init__(self,parrent=None):
        super().__init__(parrent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.radioBlack.clicked.connect( self.do_setTextColor )
        self.ui.radioRed  .clicked.connect( self.do_setTextColor )
        self.ui.radioBlue .clicked.connect( self.do_setTextColor )

    def on_btnClear_clicked(self):
        self.ui.textEdit.clear()

    def on_chkBoxBold_toggled(self,checked):
        font = self.ui.textEdit.font()
        font.setBold(checked)
        self.ui.textEdit.setFont(font)

    def on_chkBoxItalic_toggled(self,checked):
        font = self.ui.textEdit.font()
        font.setItalic(checked)
        self.ui.textEdit.setFont(font)

    def on_chkBoxUnder_toggled(self,checked):
        font = self.ui.textEdit.font()
        font.setUnderline(checked)
        self.ui.textEdit.setFont(font)

    def do_setTextColor(self):
        plet = self.ui.textEdit.palette() # 获取调色板palette
        if (self.ui.radioBlack.isChecked()):
            plet.setColor( QPalette.Text,Qt.black)
        elif (self.ui.radioRed.isChecked()):
            plet.setColor( QPalette.Text,Qt.red)
        elif (self.ui.radioBlue.isChecked()):
            plet.setColor( QPalette.Text,Qt.blue)
        self.ui.textEdit.setPalette(plet)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyDialog()
    form.show()
    sys.exit(app.exec_())
