import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

from ui_MainWindow import Ui_MainWindow

class QmyMainWindow(QMainWindow):
    def __init__(self,parrent=None):
        super().__init__(parrent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('串口调试助手')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QmyMainWindow()
    ex.show()
    sys.exit(app.exec_())
