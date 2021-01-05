import sys
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import pyqtSlot

from Ui_Widget import Ui_Form

class QmyWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.count = 0

    @pyqtSlot()
    def on_btn_read_clicked(self):
        getText = self.ui.textEdit.toPlainText()
        print('btn read: ' + getText)

    @pyqtSlot()
    def on_btn_write_clicked(self):
        putText = '第 %d 次写入\n'%self.count
        self.count +=1
        #self.ui.textEdit.setPlainText(putText) # 相当于清空后再写
        self.ui.textEdit.appendPlainText(putText)
        #self.ui.textEdit.insertPlainText(putText)
'''
setPlainText(text_str)
  设置普通文本内容
insertPlainText(text_str)
  插入普通文本
appendPlainText(text_str)
  追加普通文本
appendHtml(html_str)
  追加HTML字符串
toPlainText() -> 转换成纯文本
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QmyWidget()
    form.show()
    sys.exit(app.exec_())
