# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataInputOutput.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataInputOutput(object):
    def setupUi(self, DataInputOutput):
        DataInputOutput.setObjectName("DataInputOutput")
        DataInputOutput.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DataInputOutput)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(DataInputOutput)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_Count = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Count.setObjectName("lineEdit_Count")
        self.gridLayout.addWidget(self.lineEdit_Count, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        self.lineEdit_Price = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Price.setObjectName("lineEdit_Price")
        self.gridLayout.addWidget(self.lineEdit_Price, 0, 4, 1, 1)
        self.btn_Calculate = QtWidgets.QPushButton(self.groupBox)
        self.btn_Calculate.setObjectName("btn_Calculate")
        self.gridLayout.addWidget(self.btn_Calculate, 1, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.lineEdit_Total = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Total.setObjectName("lineEdit_Total")
        self.gridLayout.addWidget(self.lineEdit_Total, 1, 3, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(DataInputOutput)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.spinBox_Count = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_Count.setObjectName("spinBox_Count")
        self.gridLayout_2.addWidget(self.spinBox_Count, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.doubleSpinBox_Price = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_Price.setObjectName("doubleSpinBox_Price")
        self.gridLayout_2.addWidget(self.doubleSpinBox_Price, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)
        self.doubleSpinBox_Total = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_Total.setObjectName("doubleSpinBox_Total")
        self.gridLayout_2.addWidget(self.doubleSpinBox_Total, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(DataInputOutput)
        QtCore.QMetaObject.connectSlotsByName(DataInputOutput)

    def retranslateUi(self, DataInputOutput):
        _translate = QtCore.QCoreApplication.translate
        DataInputOutput.setWindowTitle(_translate("DataInputOutput", "Form"))
        self.groupBox.setTitle(_translate("DataInputOutput", "QLineEdit 输入和显示"))
        self.label.setText(_translate("DataInputOutput", "数量"))
        self.label_2.setText(_translate("DataInputOutput", "单价"))
        self.btn_Calculate.setText(_translate("DataInputOutput", "计算总价"))
        self.label_3.setText(_translate("DataInputOutput", "总价"))
        self.groupBox_2.setTitle(_translate("DataInputOutput", "SpinBox 输入输出显示"))
        self.label_4.setText(_translate("DataInputOutput", "数量"))
        self.spinBox_Count.setSuffix(_translate("DataInputOutput", "kg"))
        self.label_5.setText(_translate("DataInputOutput", "单价"))
        self.doubleSpinBox_Price.setPrefix(_translate("DataInputOutput", "$"))
        self.doubleSpinBox_Price.setSuffix(_translate("DataInputOutput", "元"))
        self.label_6.setText(_translate("DataInputOutput", "自动计算总价"))
        self.doubleSpinBox_Total.setPrefix(_translate("DataInputOutput", "$"))
