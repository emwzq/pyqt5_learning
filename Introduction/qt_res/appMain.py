import sys
from PyQt5.QtWidgets import QWidget,QApplication
from ui_Widget import Ui_Widget

class QmyWidget(QWidget):
    def __init__(self,parrent=None):
        super().__init__(parrent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = QmyWidget()
    myWidget.show()
    sys.exit(app.exec_())
