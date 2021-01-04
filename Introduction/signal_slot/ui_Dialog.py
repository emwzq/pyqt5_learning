# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\QtApp\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 456)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chkBoxUnder = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxUnder.setObjectName("chkBoxUnder")
        self.horizontalLayout.addWidget(self.chkBoxUnder)
        self.chkBoxItalic = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxItalic.setObjectName("chkBoxItalic")
        self.horizontalLayout.addWidget(self.chkBoxItalic)
        self.chkBoxBold = QtWidgets.QCheckBox(self.groupBox)
        self.chkBoxBold.setObjectName("chkBoxBold")
        self.horizontalLayout.addWidget(self.chkBoxBold)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioBlack = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioBlack.setObjectName("radioBlack")
        self.horizontalLayout_2.addWidget(self.radioBlack)
        self.radioRed = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioRed.setObjectName("radioRed")
        self.horizontalLayout_2.addWidget(self.radioRed)
        self.radioBlue = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioBlue.setObjectName("radioBlue")
        self.horizontalLayout_2.addWidget(self.radioBlue)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.textEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnClear = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_3.addWidget(self.btnClear)
        spacerItem = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnOK = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_3.addWidget(self.btnOK)
        spacerItem1 = QtWidgets.QSpacerItem(115, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Dialog)
        self.btnClose.clicked.connect(Dialog.close)
        self.btnOK.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.chkBoxUnder, self.chkBoxItalic)
        Dialog.setTabOrder(self.chkBoxItalic, self.chkBoxBold)
        Dialog.setTabOrder(self.chkBoxBold, self.radioBlack)
        Dialog.setTabOrder(self.radioBlack, self.radioRed)
        Dialog.setTabOrder(self.radioRed, self.radioBlue)
        Dialog.setTabOrder(self.radioBlue, self.textEdit)
        Dialog.setTabOrder(self.textEdit, self.btnClear)
        Dialog.setTabOrder(self.btnClear, self.btnOK)
        Dialog.setTabOrder(self.btnOK, self.btnClose)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "GroupBox"))
        self.chkBoxUnder.setText(_translate("Dialog", "Underline"))
        self.chkBoxItalic.setText(_translate("Dialog", "Italic"))
        self.chkBoxBold.setText(_translate("Dialog", "Bold"))
        self.groupBox_3.setTitle(_translate("Dialog", "GroupBox"))
        self.radioBlack.setText(_translate("Dialog", "Black"))
        self.radioRed.setText(_translate("Dialog", "Red"))
        self.radioBlue.setText(_translate("Dialog", "Blue"))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox"))
        self.btnClear.setText(_translate("Dialog", "清空"))
        self.btnOK.setText(_translate("Dialog", "确定"))
        self.btnClose.setText(_translate("Dialog", "退出"))