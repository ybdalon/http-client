# -*- coding: utf-8 -*-
import sys, time, random
import httplib, socket
import threading
from PyQt4 import QtGui, QtCore
from httpClientUI import Ui_HTTPClient
from pydoc import gui
from clientTool import taskTools, GetKeyValue
from IPConfig import *
from urlcodeHandle import *
#by yb
#version 2.0

class Widget(QtGui.QWidget, Ui_HTTPClient):
    #定义一个信号
    txt_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('T1.ico'))
        #将信号连接到一个函数（槽）
        self.txt_signal.connect(self.write_to_textbox)
        self.runtaskPushButton.setCheckable(1)
        self.sourceIpsLineEdit.hide()
        self.addIPaddrPushButton.hide()
        self.delIPaddrPushButton.hide()
        #隐藏post_data_type选框
        self.dataTypeComboBox.setVisible(0)
        #连接执行任务按钮到函数if_run_task，确定是否执行任务
        self.connect(self.runtaskPushButton, QtCore.SIGNAL('clicked()'), self.if_run_task)
        self.connect(self.confirmPushButton, QtCore.SIGNAL('clicked()'), self.confirm_config)
        self.connect(self.defaultPushButton, QtCore.SIGNAL('clicked()'), self.clear_config)
        self.connect(self.ifSouceSimCheckBox, QtCore.SIGNAL('clicked()'), self.sourceSim_config_show)
        self.connect(self.addIPaddrPushButton, QtCore.SIGNAL('clicked()'), self.add_IPs_to_eth0)
        self.connect(self.delIPaddrPushButton, QtCore.SIGNAL('clicked()'), self.del_IPs_to_eth0 )
        self.connect(self.httpStatisCheckBox, QtCore.SIGNAL('clicked()'), self.enableStatisticKeywordLineEdit)
        self.connect(self.httpPageStatisCheckBox, QtCore.SIGNAL('clicked()'), self.enablePageStatisticKeywordLineEdit)
        self.connect(self.display_allRadioButton, QtCore.SIGNAL('clicked()'), self.set_print_all)
        #确定程序的打印是否显示到界面，做到实时生效
        self.connect(self.ifPrintCheckBox, QtCore.SIGNAL('stateChanged(int)'), self.change_ifPrint)
        #连接http编码按钮
        self.connect(self.httpEncodePushButton,  QtCore.SIGNAL('clicked()'), self.http_url_encode)
        #连接http解码按钮
        self.connect(self.httpDecodePushButton, QtCore.SIGNAL('clicked()'), self.http_url_decode)
        #连接清除按钮
        self.connect(self.cleanPrintPushButton, QtCore.SIGNAL('clicked()'), self.printTextEdit.clear)
        #连接请求类型
        self.connect(self.reqMethodComboBox, QtCore.SIGNAL('currentIndexChanged(int)'), self.add_post_data)
        #为是否在执行任务设置一个标志位
        self.ifRunTask = False
        #程序输出是否显示到界面的标志位等于界面的checkBox开关的值
        self.ifPrint = 0    #0 表示不打印，1表示只打印HTTP头部信息，2表示打印全部
        self.taskDoer = None
        self.http_headers = {}
        self.sourceIpStr = ''
        self.sourceIPs = []
        self.threads = 1
    def enableStatisticKeywordLineEdit(self):
        if self.httpStatisCheckBox.isChecked():
            self.statisticKeywordLineEdit.setReadOnly(0)
        else:
            self.statisticKeywordLineEdit.setReadOnly(1)
    def enablePageStatisticKeywordLineEdit(self):
        if self.httpPageStatisCheckBox.isChecked():
            self.pageStatisticKeywordLineEdit.setReadOnly(0)
        else:
            self.pageStatisticKeywordLineEdit.setReadOnly(1)
    def add_post_data(self):
        if self.reqMethodComboBox.currentText() == 'POST' or self.reqMethodComboBox.currentText() == 'PUT':
            if self.dataTypeComboBox.isVisible() == 0:
                self.postDataTextEdit = QtGui.QTextEdit()
                self.postDataTextEdit.setObjectName("postDataTextEdit")
                #self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.postDataTextEdit)
                self.dataTypeComboBox.setVisible(1)
                self.formLayout.insertRow(0, self.dataTypeComboBox)
                self.formLayout.insertRow(1, self.postDataTextEdit)
        else:
            self.dataTypeComboBox.setVisible(0)
            self.formLayout.removeWidget(self.dataTypeComboBox)
            self.formLayout.removeWidget(self.postDataTextEdit)
            self.postDataTextEdit.close()

    def confirm_config(self):
        #从当前界面再次获取参数（参数修改后需要重新获取）
        targetTuple = str(self.targetLineEdit.text())
        #目标参数，为目标套接字元组
        if targetTuple.find(']') != -1:
            self.target = (targetTuple.split(']:')[0][1:], int(targetTuple.split(']:')[1]))
        else:
            self.target = (targetTuple.split(':')[0], int(targetTuple.split(':')[1]))
        #运行次数
        self.runCount = self.runCountSpinBox.value()
        #运行间隔
        self.interv = self.intervDoubleSpinBox.value()
        #HTTP请求类型（目前只支持GET）
        self.reqMethod = str(self.reqMethodComboBox.currentText())
        #URL框中的所有URL，转成一个URL列表
        self.URLList = [l for l in str(self.URLTextEdit.toPlainText()).split('\n') if l]
        #获取源IP模拟的源IP信息
        if self.ifSouceSimCheckBox.isChecked():
            self.sourceIpStr = str(self.sourceIpsLineEdit.text())
        else:
            self.sourceIpStr = ''
        #取得自定义头部中的内容
        self.parse_custom_headers()
        #获取body数据
        if self.reqMethod == 'POST' or self.reqMethod == 'PUT':
            self.bodyData = str(self.postDataTextEdit.toPlainText())
        else:
            self.bodyData = ''
        #socket option中socket wait time定义，此参数定义完成数据交互后，客户端保持连接的时间
        self.sockCloseWaitTime = self.sockCloseWaitTimeSpinBox.value()
        #socket timeout，类似tcp idle time
        self.sockTimeOut = self.sockTimeOutSpinBox.value()
        #是否一个连接传所有URL
        self.persistN = self.persistCheckBox.isChecked()
        #确定是否定义了需要统计的http头部内容
        if self.httpStatisCheckBox.isChecked():
            self.statisticHttpHeader = str(self.statisticKeywordLineEdit.text())
        else:
            self.statisticHttpHeader = ''
        if self.httpPageStatisCheckBox.isChecked():
            self.statisticKeyword = str(self.pageStatisticKeywordLineEdit.text())
        else:
            self.statisticKeyword = ''
        #是否打印程序输出的标志位
        if self.ifPrintCheckBox.isChecked() and self.display_allRadioButton.isChecked():
            self.ifPrint = 2
        elif self.ifPrintCheckBox.isChecked():
            self.ifPrint = 1
        else:
            self.ifPrint = 0
        self.threads = self.threadCountSpinBox.value()
    def clear_config(self):
        #恢复到默认的配置.先重置页面上的参数到默认，再调用函数confirm_config，将从界面中得到类中的内部变量值
        self.targetLineEdit.setText("127.0.0.1:8000")
        self.URLTextEdit.setText('http://127.0.0.1:8000/index.htm')
        self.customHeadersTextEdit.setText('')
        self.reqMethodComboBox.setItemText(0, 'GET')
        self.sourceIpsLineEdit.setText('')
        self.runCountSpinBox.setValue(10)
        self.intervDoubleSpinBox.setValue(1.0)
        self.sockCloseWaitTimeSpinBox.setValue(0)
        self.sockTimeOutSpinBox.setValue(2)
        self.ifSouceSimCheckBox.setChecked(0)
        self.sourceSim_config_show()
        self.persistCheckBox.setChecked(0)
        self.httpStatisCheckBox.setChecked(0)
        self.statisticKeywordLineEdit.setText('Server-IP')
        self.statisticKeywordLineEdit.setReadOnly(1)
        self.httpPageStatisCheckBox.setChecked(0)
        self.pageStatisticKeywordLineEdit.setText('Server-IP')
        self.pageStatisticKeywordLineEdit.setReadOnly(1)
        self.confirm_config()
    def parse_custom_headers(self):
        #解析自定义头部框中的内容，得到自定义头部的内容，为一个字典类型
        self.http_headers = {}
        tempstr = str(self.customHeadersTextEdit.toPlainText())
        if tempstr:
            for l in tempstr.split('\n'):
                if l.find(':') != -1:
                    self.http_headers[l.split(':')[0]] = l.split(':')[1].strip('\n').strip()
    def get_args(self):
        self.confirm_config()

    def write(self, s):
        self.txt_signal.emit(s)
    #修饰后，可以不阻塞地接收信号，后面函数为对信号的处理
    @QtCore.pyqtSlot(str)
    def write_to_textbox(self, text):
        try:
            s = str(text)
        except:
            self.printTextEdit.append(text)
            return
        if s == '\n':
            pass
        elif s == '[task finihed]':
            self.runtaskPushButton.setText(u"执行任务")
            self.ifRunTask = False
        else:
            self.printTextEdit.append(text)
    def add_IPs_to_eth0(self):
        self.sourceIpStr = str(self.sourceIpsLineEdit.text())
        if not self.sourceIpStr:
            QtGui.QMessageBox.information(self ,"Information" ,
                                    u"请填写源IP信息！格式： 172.16.10.20-30")
        else:
            ips = convt_IPs(self.sourceIpStr)
            if ips:
                add_client_sip(ips)
                QtGui.QMessageBox.information(self ,"Information" ,
                                    u"IP地址配置并准备完成，请检查网卡eth0！")
            elif not ips:
                 QtGui.QMessageBox.information(self ,"Information" ,
                                    u"IP格式： 172.16.10.20-30,仅支持IP最后一段递增！")
    def del_IPs_to_eth0(self):
        self.sourceIpStr = str(self.sourceIpsLineEdit.text())
        if not self.sourceIpStr:
            QtGui.QMessageBox.information(self ,"Information" ,
                                    u"请填写源IP信息！格式： 172.16.10.20-30")
        else:
            ips = convt_IPs(self.sourceIpStr)
            if ips:
                delete_client_sip(ips)
                QtGui.QMessageBox.information(self ,"Information" ,
                                    u"IP地址已经删除！")
            elif not ips:
                 QtGui.QMessageBox.information(self ,"Information" ,
                                    u"IP格式： 172.16.10.20-30,仅支持IP最后一段递增！")
    def change_ifPrint(self):
        if self.ifPrintCheckBox.isChecked():
            self.displayRadioButton.setVisible(1)
            self.display_allRadioButton.setVisible(1)
            self.ifPrint = 1
            if self.taskDoer:
                self.taskDoer.ifPrint = self.ifPrint
        else:
            self.displayRadioButton.click()
            self.displayRadioButton.setVisible(0)
            self.display_allRadioButton.setVisible(0)
            self.ifPrint = 0
            if self.taskDoer:
                self.taskDoer.ifPrint = self.ifPrint
    def set_print_all(self):
        self.ifPrint = 2
        if self.taskDoer:
            self.taskDoer.ifPrint = self.ifPrint

    def sourceSim_config_show(self):
        if self.ifSouceSimCheckBox.isChecked():
            self.sourceIpsLineEdit.setVisible(1)
            self.addIPaddrPushButton.setVisible(1)
            self.delIPaddrPushButton.setVisible(1)
        else:
            self.sourceIpsLineEdit.hide()
            self.addIPaddrPushButton.hide()
            self.delIPaddrPushButton.hide()
    def if_run_task(self):
        #是否执行任务，runtaskPushButton有两种状态： “执行任务”和“停止”
        #if self.runtaskPushButton.text() == u"执行任务":
        if self.ifRunTask == False:
            self.runtaskPushButton.setText(u"停止")
            self.printTextEdit.setText('')
            self.run_task()
            self.ifRunTask = True
        #elif self.runtaskPushButton.text() == u"停止":
        elif self.ifRunTask == True:
            self.runtaskPushButton.setText(u"执行任务")
            self.stop_task()
            self.ifRunTask = False
    def run_task(self):
        self.get_args()
        self.taskDoer = taskTools(self.target, self.runCount, self.interv,
                                  self.reqMethod, self.bodyData, self.URLList, self.sourceIPs)
        if self.http_headers:
            self.taskDoer.http_headers = self.http_headers
        if self.persistN:
            self.taskDoer.persistN = True
            self.taskDoer.http_headers['Connection'] = 'Keep-Alive'
        else:
            self.taskDoer.persistN = False
            if not self.http_headers.has_key('Connection'):
                self.taskDoer.http_headers['Connection'] = 'Close'
        if self.sockCloseWaitTime > 0:
            self.taskDoer.sockCloseWaitTime = self.sockCloseWaitTime
        if self.sockTimeOut != 2:
            self.taskDoer.sockTimeOut = self.sockTimeOut
        if self.sourceIpStr:
            self.sourceIPs = convt_IPs(self.sourceIpStr)
        else:
            self.sourceIPs = []
        self.taskDoer.sourceIPs = self.sourceIPs
        if self.statisticHttpHeader:
            self.taskDoer.statisticHttpHeader = self.statisticHttpHeader
        if self.statisticKeyword:
            self.taskDoer.statisticKeyword = self.statisticKeyword
        self.taskDoer.ifPrint = self.ifPrint
        self.taskDoer.threads = self.threads
        thr = threading.Thread(target = self.taskDoer.run)
        thr.setDaemon(1)
        thr.start()
    def stop_task(self):
        self.taskDoer.ifStop = True
    def http_url_encode(self):
        '''将带中文的URLkey=value或者json转成urlcode的格式'''
        s = self.httpBeforeCodeTextEdit.toPlainText()
        s1 = unicode(s.toUtf8(), 'utf-8', 'ignore')
        s2 = get_urlencode(s1)
        self.httpAfterCodeTextEdit.setHtml(s2)
    def http_url_decode(self):
        ''''''
        s = self.httpAfterCodeTextEdit.toPlainText()
        s1 = get_urldecode(GetKeyValue(repr(s), "(u'", "')"))
        self.httpBeforeCodeTextEdit.setHtml(s1.decode('utf8'))

def main():
    app = QtGui.QApplication(sys.argv)
    clientGui = Widget()
    clientGui.show()
    sys.stdout = clientGui
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




