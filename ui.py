# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled4.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1088, 612)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(620, 25, 468, 370))
        self.textEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(1)
        self.textEdit.setObjectName("textEdit")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 620, 612))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(4)
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(620, 400, 468, 212))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit_2.setObjectName("textEdit_2")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(620, 400, 468, 175))
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(678, 583, 141, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(870, 583, 81, 21))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(980, 579, 93, 28))
        font = QtGui.QFont()
        font.setFamily("霞鹜新晰黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(634, 586, 41, 16))
        font = QtGui.QFont()
        font.setFamily("霞鹜新晰黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(828, 586, 41, 16))
        font = QtGui.QFont()
        font.setFamily("霞鹜新晰黑")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(620, 0, 468, 25))
        font = QtGui.QFont()
        font.setFamily("OPPOSans")
        font.setUnderline(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: white;border:1px;")
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setMidLineWidth(0)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1063, -1, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255,255,255);\n"
"border-radius:5px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2.raise_()
        self.textBrowser.raise_()
        self.textEdit.raise_()
        self.listWidget.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.tableWidget.raise_()
        self.pushButton_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "标题"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "来源"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "日期"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "类型"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(8)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(9)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(10)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(11)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(12)
        item.setText(_translate("Form", "New Item"))
        item = self.listWidget.item(13)
        item.setText(_translate("Form", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "查找"))
        self.label.setText(_translate("Form", "主题："))
        self.label_2.setText(_translate("Form", "数量："))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'OPPOSans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "⚙️"))