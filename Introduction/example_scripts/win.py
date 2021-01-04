import sys
from PyQt5.QtWidgets import QWidget,QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(480,320)
    win.move(300,300)
    win.show()

    sys.exit(app.exec_())
