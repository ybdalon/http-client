# -*- coding: utf-8 -*-
import time
import httplib
import threading
import ssl
import traceback

def GetKeyValue(s='abc:123', keyword='abc:', End=' '):
        if s.find(keyword)!=-1:
            startN=s.find(keyword)+len(keyword)
            if s[startN:].find(End)!=-1:
                EndN=s[startN:].find(End)+startN
                return s[startN:EndN]
            else:
                return s[startN:]
        else:
            return

def url_parse(url):
    '''
    url = 'http://127.0.0.1:8000/path/abc.html'
    return 'http', '127.0.0.1:8000', '/path/abc.html' 
    '''
    if url.find('://')!=-1:
        temps1 = url.split('://')
        if len(temps1)<1:
            return '', '', ''
        protocol = temps1[0]
        if temps1[1].find('/') == -1:
            host = temps1[1]
            uri = '/'
            return protocol, host, uri
        temps2 = temps1[1].split('/')
        host = temps2[0]
        uri = '/' + '/'.join(temps2[1:])
        return protocol, host, uri
    else:
        return '', '', ''

class taskTools:
    def __init__(self, target = ('127.0.0.1', 8000),  runCount = 1, interv = 0.1, 
                 reqMethod = 'GET', postData = '',  URLList = ['http://127.0.0.1:8000'], sourceIPs = []):
        self.target = target
        self.runCount = runCount
        self.interv = interv
        self.http_headers = {}
        self.method = reqMethod
        self.URLList = URLList    #URLList的列表
        self.sourceIPs = sourceIPs
        self.persistN = False   #定义是否一个连接多个GET
        self.ifStop = False
        self.ifPrint = 1 #0 表示不打印，1表示只打印HTTP头部信息，2表示打印全部
        self.statisticHttpHeader = 'Server-IP'
        self.statisticKeyword = 'Server-IP'
        self.statisticDic = {}
        self.statisticCountOfKeyword = 0
        self.sockTimeOut = 2
        self.sockCloseWaitTime = 0
        self.threadCount = 0
        self.postData = postData
        self.threads = 1
        #self.ifFinished = False  #不知道起线程后，如何将这个标志位传给主程序。有可能要将GUI和主业务逻辑完全分离！
    def if_print(self, s, level = 1):
        if self.ifPrint >= level:
            print s
    def run(self):
        self.starttime = time.time()
        print '>>>START TIME: %s<<<<'%time.ctime(self.starttime)
        self.threadCount = threading.activeCount()
        if self.threads == 1:
            self.do_task()
        else:
            for i in xrange(self.threads):
                t = threading.Thread(target = self.do_task)
                t.start()
        self.print_result()
    def do_task(self):
        count = 1
        while count <= self.runCount and not self.ifStop:
            if self.sourceIPs:
                for ip in self.sourceIPs:
                    if not self.ifStop:
                        if count == self.runCount + 1:
                            break
                        else:
                            self.if_print("###############Count: %s###############"%count)
                            if self.persistN:
                                self.http_con(ip)
                            else:
                                self.perUrl_http_con(ip)
                        count += 1
                        time.sleep(self.interv)
            else:
                self.if_print("###############Count: %s###############"%count)
                if self.persistN:
                    self.http_con()
                else:
                    self.perUrl_http_con()
                count += 1
                time.sleep(self.interv)

    def print_result(self):
        while threading.activeCount() != self.threadCount:
            time.sleep(3)            
        #self.ifFinished = 1
        print '\n\n[task finihed]'
        #print进入sys.stdout后，可以传递给class Widget，从而将停止“按钮”复位成“执行任务”
        self.endtime = time.time()
        print "########    TEST over! [%s] RESULT    ########\n#    Pass Time %s second"%(time.ctime(self.endtime),
                                                                        (self.endtime-self.starttime)) 
        if self.statisticDic:
            for k in self.statisticDic.keys():
                print '#    [%s: %s] hit counts: %d'%(self.statisticHttpHeader,
                                                k, self.statisticDic[k])     
        print "#    keyword %s appears %d times"%(self.statisticKeyword, self.statisticCountOfKeyword)
        print "####################################################################"
    def http_con(self, sourceIp = ''):
        if sourceIp:
            conn = httplib.HTTPConnection(self.target[0],
                                          self.target[1],
                                          timeout=self.sockTimeOut,
                                          source_address = (sourceIp, 0))
        else:
            conn = httplib.HTTPConnection(self.target[0],
                                          self.target[1],
                                          timeout = self.sockTimeOut)
        for url in self.URLList:
            prot, host, uri = url_parse(url)
            self.http_headers['Host'] = host
            try:
                if self.method == 'POST' or self.method=='PUT':
                    conn.request(self.method, uri, body=self.postData, headers=self.http_headers)
                else:
                    conn.request(self.method, uri,headers=self.http_headers)
            except:
                self.if_print("the server %s is down!"%(self.target, ))
                return
            try:
                res = conn.getresponse()
            except:
                self.if_print('socket timeout!')
                return
            self.if_print('reason: %s\nstatus: %s'%(res.reason, res.status))
            res_header = res.getheaders()
            #统计功能。如果server回复的头部中有IP地址。（只在HTTP头部中搜寻Server-IP头部）
            if res.getheader(self.statisticHttpHeader):
                if not self.statisticDic.has_key(res.getheader(self.statisticHttpHeader)):
                    self.statisticDic[res.getheader(self.statisticHttpHeader)] = 1
                else:
                    self.statisticDic[res.getheader(self.statisticHttpHeader)] += 1
            #统计功能完毕
            for h in res_header:
                self.if_print('%s: %s'%(h[0], h[1]))
            try:
                temp = res.read()
            except:
                self.if_print("recv data error!", 3)
                return
            if temp.find(self.statisticKeyword)!=-1:
                self.statisticCountOfKeyword += 1
            self.if_print(temp, 2)
        if self.sockCloseWaitTime:
            time.sleep(self.sockCloseWaitTime)
        conn.close()
    def perUrl_http_con(self, sourceIp = ''):
        for url in self.URLList:
            prot, host, uri = url_parse(url)
            self.http_headers['Host'] = host
            if prot == 'https':
                ssl._create_default_https_context = ssl._create_unverified_context
                if sourceIp:
                    conn = httplib.HTTPSConnection(self.target[0],
                                                  self.target[1],
                                                  timeout=self.sockTimeOut,
                                                  source_address=(sourceIp, 0))
                else:
                    conn = httplib.HTTPSConnection(self.target[0],
                                                  self.target[1],
                                                  timeout = self.sockTimeOut)
            else:
                if sourceIp:
                    conn = httplib.HTTPConnection(self.target[0],
                                                  self.target[1],
                                                  timeout=self.sockTimeOut,
                                                  source_address=(sourceIp, 0))
                else:
                    conn = httplib.HTTPConnection(self.target[0],
                                                  self.target[1],
                                                  timeout = self.sockTimeOut)
            try:
                if self.method == 'POST' or self.method=='PUT':
                    conn.request(self.method, uri, body=self.postData, headers=self.http_headers)
                else:
                    conn.request(self.method, uri, headers = self.http_headers)
            except:
                #traceback.print_exc()
                self.if_print("the server %s is down!"%(self.target, ))
                continue
            try:
                res = conn.getresponse()
            except:
                self.if_print('socket timeout or connection be reset!')
                continue
            self.if_print('reason: %s\nstatus: %s'%(res.reason, res.status))
            res_header = res.getheaders()
            #统计功能。如果server回复的头部中有IP地址。（只在HTTP头部中搜寻Server-IP头部）
            if res.getheader(self.statisticHttpHeader):
                if  not self.statisticDic.has_key(res.getheader(self.statisticHttpHeader)):
                    self.statisticDic[res.getheader(self.statisticHttpHeader)] = 1
                else:
                    self.statisticDic[res.getheader(self.statisticHttpHeader)] += 1
            #统计功能完毕
            for h in res_header:
                self.if_print('%s: %s'%(h[0], h[1]))
            try:
                temp = res.read()
            except:
                self.if_print("recv data error!", 3)
                continue
            if temp.find(self.statisticKeyword)!=-1:
                self.statisticCountOfKeyword += 1
            self.if_print(temp, 2)
            if self.sockCloseWaitTime:
                time.sleep(self.sockCloseWaitTime)
            conn.close()
        
if __name__ == '__main__':
    print url_parse('https://192.168.10.1:80/abc/1.html')
    t = taskTools(target = ('192.168.10.105', 443), reqMethod='POST', postData = '123=789&abc=345',
                  URLList= ['https://www.baidu.com/1.php'])
    t.run()


