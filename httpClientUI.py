# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python27\YB_pyqtUI\client.ui'
#
# Created: Wed Jul 25 12:15:57 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HTTPClient(object):
    def setupUi(self, HTTPClient):
        HTTPClient.setObjectName(_fromUtf8("HTTPClient"))
        HTTPClient.setEnabled(True)
        HTTPClient.resize(705, 627)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HTTPClient.sizePolicy().hasHeightForWidth())
        HTTPClient.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(False)
        HTTPClient.setFont(font)
        HTTPClient.setAcceptDrops(True)
        HTTPClient.setStatusTip(_fromUtf8(""))
        HTTPClient.setAutoFillBackground(False)
        HTTPClient.setStyleSheet(_fromUtf8("selection-background-color: rgb(249, 249, 249);"))
        self.tabWidget = QtGui.QTabWidget(HTTPClient)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 681, 551))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.baseConfig = QtGui.QWidget()
        self.baseConfig.setObjectName(_fromUtf8("baseConfig"))
        self.label = QtGui.QLabel(self.baseConfig)
        self.label.setGeometry(QtCore.QRect(18, 25, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.targetLineEdit = QtGui.QLineEdit(self.baseConfig)
        self.targetLineEdit.setGeometry(QtCore.QRect(67, 23, 161, 20))
        self.targetLineEdit.setObjectName(_fromUtf8("targetLineEdit"))
        self.label_4 = QtGui.QLabel(self.baseConfig)
        self.label_4.setGeometry(QtCore.QRect(374, 23, 51, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.runCountSpinBox = QtGui.QSpinBox(self.baseConfig)
        self.runCountSpinBox.setGeometry(QtCore.QRect(427, 21, 81, 22))
        self.runCountSpinBox.setMinimum(1)
        self.runCountSpinBox.setMaximum(9999999)
        self.runCountSpinBox.setProperty("value", 1)
        self.runCountSpinBox.setObjectName(_fromUtf8("runCountSpinBox"))
        self.label_5 = QtGui.QLabel(self.baseConfig)
        self.label_5.setGeometry(QtCore.QRect(529, 24, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.baseConfig)
        self.label_6.setGeometry(QtCore.QRect(243, 24, 31, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.intervDoubleSpinBox = QtGui.QDoubleSpinBox(self.baseConfig)
        self.intervDoubleSpinBox.setGeometry(QtCore.QRect(588, 21, 62, 22))
        self.intervDoubleSpinBox.setDecimals(3)
        self.intervDoubleSpinBox.setMaximum(60.0)
        self.intervDoubleSpinBox.setProperty("value", 1.0)
        self.intervDoubleSpinBox.setObjectName(_fromUtf8("intervDoubleSpinBox"))
        self.reqMethodComboBox = QtGui.QComboBox(self.baseConfig)
        self.reqMethodComboBox.setGeometry(QtCore.QRect(273, 21, 81, 22))
        self.reqMethodComboBox.setObjectName(_fromUtf8("reqMethodComboBox"))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.reqMethodComboBox.addItem(_fromUtf8(""))
        self.formLayoutWidget = QtGui.QWidget(self.baseConfig)
        self.formLayoutWidget.setGeometry(QtCore.QRect(13, 60, 651, 461))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.customHeadersTextEdit = QtGui.QTextEdit(self.formLayoutWidget)
        self.customHeadersTextEdit.setObjectName(_fromUtf8("customHeadersTextEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.customHeadersTextEdit)
        self.URLTextEdit = QtGui.QTextEdit(self.formLayoutWidget)
        self.URLTextEdit.setObjectName(_fromUtf8("URLTextEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.URLTextEdit)
        self.dataTypeComboBox = QtGui.QComboBox(self.baseConfig)
        self.dataTypeComboBox.setEnabled(True)
        self.dataTypeComboBox.setGeometry(QtCore.QRect(20, 0, 241, 22))
        self.dataTypeComboBox.setEditable(False)
        self.dataTypeComboBox.setObjectName(_fromUtf8("dataTypeComboBox"))
        self.dataTypeComboBox.addItem(_fromUtf8(""))
        self.dataTypeComboBox.addItem(_fromUtf8(""))
        self.dataTypeComboBox.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.baseConfig, _fromUtf8(""))
        self.advanceConfig = QtGui.QWidget()
        self.advanceConfig.setObjectName(_fromUtf8("advanceConfig"))
        self.sockOptionGroupBox = QtGui.QGroupBox(self.advanceConfig)
        self.sockOptionGroupBox.setGeometry(QtCore.QRect(20, 30, 641, 201))
        self.sockOptionGroupBox.setObjectName(_fromUtf8("sockOptionGroupBox"))
        self.ifSouceSimCheckBox = QtGui.QCheckBox(self.sockOptionGroupBox)
        self.ifSouceSimCheckBox.setGeometry(QtCore.QRect(20, 70, 361, 16))
        self.ifSouceSimCheckBox.setObjectName(_fromUtf8("ifSouceSimCheckBox"))
        self.sourceIpsLineEdit = QtGui.QLineEdit(self.sockOptionGroupBox)
        self.sourceIpsLineEdit.setEnabled(True)
        self.sourceIpsLineEdit.setGeometry(QtCore.QRect(39, 100, 321, 20))
        self.sourceIpsLineEdit.setObjectName(_fromUtf8("sourceIpsLineEdit"))
        self.label_7 = QtGui.QLabel(self.sockOptionGroupBox)
        self.label_7.setGeometry(QtCore.QRect(200, 31, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.sockTimeOutSpinBox = QtGui.QSpinBox(self.sockOptionGroupBox)
        self.sockTimeOutSpinBox.setGeometry(QtCore.QRect(300, 29, 51, 22))
        self.sockTimeOutSpinBox.setMinimum(1)
        self.sockTimeOutSpinBox.setMaximum(60)
        self.sockTimeOutSpinBox.setProperty("value", 2)
        self.sockTimeOutSpinBox.setObjectName(_fromUtf8("sockTimeOutSpinBox"))
        self.label_8 = QtGui.QLabel(self.sockOptionGroupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.sockCloseWaitTimeSpinBox = QtGui.QSpinBox(self.sockOptionGroupBox)
        self.sockCloseWaitTimeSpinBox.setGeometry(QtCore.QRect(106, 28, 51, 22))
        self.sockCloseWaitTimeSpinBox.setMinimum(0)
        self.sockCloseWaitTimeSpinBox.setMaximum(60)
        self.sockCloseWaitTimeSpinBox.setProperty("value", 0)
        self.sockCloseWaitTimeSpinBox.setObjectName(_fromUtf8("sockCloseWaitTimeSpinBox"))
        self.addIPaddrPushButton = QtGui.QPushButton(self.sockOptionGroupBox)
        self.addIPaddrPushButton.setGeometry(QtCore.QRect(400, 99, 61, 23))
        self.addIPaddrPushButton.setObjectName(_fromUtf8("addIPaddrPushButton"))
        self.delIPaddrPushButton = QtGui.QPushButton(self.sockOptionGroupBox)
        self.delIPaddrPushButton.setGeometry(QtCore.QRect(469, 99, 61, 23))
        self.delIPaddrPushButton.setObjectName(_fromUtf8("delIPaddrPushButton"))
        self.threadCountSpinBox = QtGui.QSpinBox(self.sockOptionGroupBox)
        self.threadCountSpinBox.setGeometry(QtCore.QRect(436, 28, 91, 22))
        self.threadCountSpinBox.setMinimum(1)
        self.threadCountSpinBox.setMaximum(2000)
        self.threadCountSpinBox.setProperty("value", 1)
        self.threadCountSpinBox.setObjectName(_fromUtf8("threadCountSpinBox"))
        self.label_9 = QtGui.QLabel(self.sockOptionGroupBox)
        self.label_9.setGeometry(QtCore.QRect(390, 32, 41, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.httpOptionsGroupBox = QtGui.QGroupBox(self.advanceConfig)
        self.httpOptionsGroupBox.setGeometry(QtCore.QRect(20, 240, 641, 281))
        self.httpOptionsGroupBox.setCheckable(False)
        self.httpOptionsGroupBox.setChecked(False)
        self.httpOptionsGroupBox.setObjectName(_fromUtf8("httpOptionsGroupBox"))
        self.persistCheckBox = QtGui.QCheckBox(self.httpOptionsGroupBox)
        self.persistCheckBox.setGeometry(QtCore.QRect(20, 30, 301, 16))
        self.persistCheckBox.setChecked(False)
        self.persistCheckBox.setObjectName(_fromUtf8("persistCheckBox"))
        self.httpStatisCheckBox = QtGui.QCheckBox(self.httpOptionsGroupBox)
        self.httpStatisCheckBox.setGeometry(QtCore.QRect(20, 57, 301, 16))
        self.httpStatisCheckBox.setCheckable(True)
        self.httpStatisCheckBox.setChecked(False)
        self.httpStatisCheckBox.setTristate(False)
        self.httpStatisCheckBox.setObjectName(_fromUtf8("httpStatisCheckBox"))
        self.statisticKeywordLineEdit = QtGui.QLineEdit(self.httpOptionsGroupBox)
        self.statisticKeywordLineEdit.setEnabled(True)
        self.statisticKeywordLineEdit.setGeometry(QtCore.QRect(36, 79, 261, 20))
        self.statisticKeywordLineEdit.setToolTip(_fromUtf8(""))
        self.statisticKeywordLineEdit.setAutoFillBackground(False)
        self.statisticKeywordLineEdit.setDragEnabled(False)
        self.statisticKeywordLineEdit.setReadOnly(True)
        self.statisticKeywordLineEdit.setObjectName(_fromUtf8("statisticKeywordLineEdit"))
        self.httpPageStatisCheckBox = QtGui.QCheckBox(self.httpOptionsGroupBox)
        self.httpPageStatisCheckBox.setGeometry(QtCore.QRect(20, 110, 331, 16))
        self.httpPageStatisCheckBox.setCheckable(True)
        self.httpPageStatisCheckBox.setChecked(False)
        self.httpPageStatisCheckBox.setTristate(False)
        self.httpPageStatisCheckBox.setObjectName(_fromUtf8("httpPageStatisCheckBox"))
        self.pageStatisticKeywordLineEdit = QtGui.QLineEdit(self.httpOptionsGroupBox)
        self.pageStatisticKeywordLineEdit.setEnabled(True)
        self.pageStatisticKeywordLineEdit.setGeometry(QtCore.QRect(36, 134, 261, 20))
        self.pageStatisticKeywordLineEdit.setToolTip(_fromUtf8(""))
        self.pageStatisticKeywordLineEdit.setReadOnly(True)
        self.pageStatisticKeywordLineEdit.setObjectName(_fromUtf8("pageStatisticKeywordLineEdit"))
        self.tabWidget.addTab(self.advanceConfig, _fromUtf8(""))
        self.monitorPage = QtGui.QWidget()
        self.monitorPage.setObjectName(_fromUtf8("monitorPage"))
        self.printTextEdit = QtGui.QTextEdit(self.monitorPage)
        self.printTextEdit.setGeometry(QtCore.QRect(7, 40, 661, 481))
        self.printTextEdit.setObjectName(_fromUtf8("printTextEdit"))
        self.ifPrintCheckBox = QtGui.QCheckBox(self.monitorPage)
        self.ifPrintCheckBox.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.ifPrintCheckBox.setChecked(True)
        self.ifPrintCheckBox.setObjectName(_fromUtf8("ifPrintCheckBox"))
        self.cleanPrintPushButton = QtGui.QPushButton(self.monitorPage)
        self.cleanPrintPushButton.setGeometry(QtCore.QRect(590, 10, 75, 23))
        self.cleanPrintPushButton.setObjectName(_fromUtf8("cleanPrintPushButton"))
        self.displayRadioButton = QtGui.QRadioButton(self.monitorPage)
        self.displayRadioButton.setGeometry(QtCore.QRect(100, 20, 111, 16))
        self.displayRadioButton.setChecked(True)
        self.displayRadioButton.setObjectName(_fromUtf8("displayRadioButton"))
        self.display_allRadioButton = QtGui.QRadioButton(self.monitorPage)
        self.display_allRadioButton.setGeometry(QtCore.QRect(230, 20, 89, 16))
        self.display_allRadioButton.setObjectName(_fromUtf8("display_allRadioButton"))
        self.tabWidget.addTab(self.monitorPage, _fromUtf8(""))
        self.httpEncodePage = QtGui.QWidget()
        self.httpEncodePage.setObjectName(_fromUtf8("httpEncodePage"))
        self.httpBeforeCodeTextEdit = QtGui.QTextEdit(self.httpEncodePage)
        self.httpBeforeCodeTextEdit.setGeometry(QtCore.QRect(20, 40, 641, 161))
        self.httpBeforeCodeTextEdit.setObjectName(_fromUtf8("httpBeforeCodeTextEdit"))
        self.httpAfterCodeTextEdit = QtGui.QTextEdit(self.httpEncodePage)
        self.httpAfterCodeTextEdit.setGeometry(QtCore.QRect(20, 260, 641, 231))
        self.httpAfterCodeTextEdit.setObjectName(_fromUtf8("httpAfterCodeTextEdit"))
        self.httpEncodePushButton = QtGui.QPushButton(self.httpEncodePage)
        self.httpEncodePushButton.setGeometry(QtCore.QRect(580, 210, 81, 23))
        self.httpEncodePushButton.setObjectName(_fromUtf8("httpEncodePushButton"))
        self.httpDecodePushButton = QtGui.QPushButton(self.httpEncodePage)
        self.httpDecodePushButton.setGeometry(QtCore.QRect(580, 500, 81, 23))
        self.httpDecodePushButton.setObjectName(_fromUtf8("httpDecodePushButton"))
        self.label_11 = QtGui.QLabel(self.httpEncodePage)
        self.label_11.setGeometry(QtCore.QRect(21, 16, 301, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.httpEncodePage)
        self.label_12.setGeometry(QtCore.QRect(20, 240, 301, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tabWidget.addTab(self.httpEncodePage, _fromUtf8(""))
        self.helpInfo = QtGui.QWidget()
        self.helpInfo.setObjectName(_fromUtf8("helpInfo"))
        self.groupBox = QtGui.QGroupBox(self.helpInfo)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 641, 491))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(0, 20, 641, 471))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.helpInfo, _fromUtf8(""))
        self.horizontalLayoutWidget = QtGui.QWidget(HTTPClient)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(360, 580, 331, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.confirmPushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.confirmPushButton.setObjectName(_fromUtf8("confirmPushButton"))
        self.horizontalLayout.addWidget(self.confirmPushButton)
        self.defaultPushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.defaultPushButton.setObjectName(_fromUtf8("defaultPushButton"))
        self.horizontalLayout.addWidget(self.defaultPushButton)
        self.runtaskPushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.runtaskPushButton.setObjectName(_fromUtf8("runtaskPushButton"))
        self.horizontalLayout.addWidget(self.runtaskPushButton)

        self.retranslateUi(HTTPClient)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HTTPClient)

    def retranslateUi(self, HTTPClient):
        HTTPClient.setWindowTitle(_translate("HTTPClient", "HTTP客户端", None))
        self.label.setText(_translate("HTTPClient", "IP:PORT", None))
        self.targetLineEdit.setToolTip(_translate("HTTPClient", "<html><head/><body><p>IPV6的格式为[3ffe:100::1234]:8000 </p><p>也可填写域名和端口：www.baidu.com:80</p></body></html>", None))
        self.targetLineEdit.setText(_translate("HTTPClient", "127.0.0.1:8000", None))
        self.label_4.setText(_translate("HTTPClient", "运行次数", None))
        self.label_5.setText(_translate("HTTPClient", "请求间隔", None))
        self.label_6.setText(_translate("HTTPClient", "方法", None))
        self.reqMethodComboBox.setItemText(0, _translate("HTTPClient", "GET", None))
        self.reqMethodComboBox.setItemText(1, _translate("HTTPClient", "POST", None))
        self.reqMethodComboBox.setItemText(2, _translate("HTTPClient", "DELETE", None))
        self.reqMethodComboBox.setItemText(3, _translate("HTTPClient", "HEAD", None))
        self.reqMethodComboBox.setItemText(4, _translate("HTTPClient", "PUT", None))
        self.reqMethodComboBox.setItemText(5, _translate("HTTPClient", "TRACE", None))
        self.reqMethodComboBox.setItemText(6, _translate("HTTPClient", "CONNECT", None))
        self.label_2.setText(_translate("HTTPClient", "URL（可多个）", None))
        self.label_3.setText(_translate("HTTPClient", "HTTP自定义头部", None))
        self.URLTextEdit.setHtml(_translate("HTTPClient", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">http://127.0.0.1:8000/</p></body></html>", None))
        self.dataTypeComboBox.setItemText(0, _translate("HTTPClient", "URL-Encoding", None))
        self.dataTypeComboBox.setItemText(1, _translate("HTTPClient", "Json", None))
        self.dataTypeComboBox.setItemText(2, _translate("HTTPClient", "Text-XML", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.baseConfig), _translate("HTTPClient", "基本配置", None))
        self.sockOptionGroupBox.setTitle(_translate("HTTPClient", "Socket Options", None))
        self.ifSouceSimCheckBox.setText(_translate("HTTPClient", "源IP模拟（请先将网卡改名为eth0，再添加IP地址）", None))
        self.sourceIpsLineEdit.setToolTip(_translate("HTTPClient", "格式： 172.16.10.20-30", None))
        self.label_7.setText(_translate("HTTPClient", "Socket Timeout", None))
        self.label_8.setText(_translate("HTTPClient", "连接断开等待", None))
        self.addIPaddrPushButton.setText(_translate("HTTPClient", "添加IP", None))
        self.delIPaddrPushButton.setText(_translate("HTTPClient", "删除IP", None))
        self.label_9.setText(_translate("HTTPClient", "线程数", None))
        self.httpOptionsGroupBox.setTitle(_translate("HTTPClient", "HTTP 选项", None))
        self.persistCheckBox.setText(_translate("HTTPClient", "PERSIST(勾选后，将在一条连接里面请求URL)", None))
        self.httpStatisCheckBox.setText(_translate("HTTPClient", "HTTP头名称(统计头部内容，在结果中输出)", None))
        self.statisticKeywordLineEdit.setText(_translate("HTTPClient", "Server-IP", None))
        self.httpPageStatisCheckBox.setText(_translate("HTTPClient", "页面关键字统计（每个页面统计第一个出现的关键字一次）", None))
        self.pageStatisticKeywordLineEdit.setText(_translate("HTTPClient", "Server-IP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.advanceConfig), _translate("HTTPClient", "高级配置", None))
        self.ifPrintCheckBox.setText(_translate("HTTPClient", "程序输出", None))
        self.cleanPrintPushButton.setText(_translate("HTTPClient", "清除页面", None))
        self.displayRadioButton.setText(_translate("HTTPClient", "只显示HTTP头部", None))
        self.display_allRadioButton.setText(_translate("HTTPClient", "全部显示", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.monitorPage), _translate("HTTPClient", "监控", None))
        self.httpBeforeCodeTextEdit.setHtml(_translate("HTTPClient", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">scope=bbs&amp;q=C语言</p></body></html>", None))
        self.httpAfterCodeTextEdit.setHtml(_translate("HTTPClient", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">scope=bbs&amp;q=C%E8%AF%AD%E8%A8%80</p></body></html>", None))
        self.httpEncodePushButton.setText(_translate("HTTPClient", "HTTP URL编码", None))
        self.httpDecodePushButton.setText(_translate("HTTPClient", "HTTP URL解码", None))
        self.label_11.setText(_translate("HTTPClient", "源数据（json或者key1=value1&key2=value2格式）", None))
        self.label_12.setText(_translate("HTTPClient", "编码后的数据", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.httpEncodePage), _translate("HTTPClient", "HTTP编码工具", None))
        self.groupBox.setTitle(_translate("HTTPClient", "Version 2.0", None))
        self.textBrowser.setHtml(_translate("HTTPClient", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Version 2.1</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HTTP 测试客户端</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">作者：YB.Dalon</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">邮箱：yb890102@126.com</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#ff0000;\">申明： 本程序只用于学习、演示和交流，请勿用于其他用途</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; text-decoration: underline; color:#ff0000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20180515</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.helpInfo), _translate("HTTPClient", "帮助", None))
        self.confirmPushButton.setText(_translate("HTTPClient", "确认配置", None))
        self.defaultPushButton.setText(_translate("HTTPClient", "恢复默认", None))
        self.runtaskPushButton.setText(_translate("HTTPClient", "执行任务", None))

