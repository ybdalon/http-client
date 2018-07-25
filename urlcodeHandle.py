# -*- coding: utf-8 -*-
import urllib
import json

def get_urlencode(s):
    ''''if s is json, convert directly;'''
    s = s.encode('utf8')
    try:
        json.loads(s, encoding='utf-8')
        return urllib.urlencode(eval(s))
    except:
        pass
    res = []
    for i in s.split('&'):
        try:
            res.append('%s=%s' % (urllib.quote(i.split('=')[0]),
                                  urllib.quote(i.split('=')[1])))
        except:
            return
    return '&'.join(res)

def get_urldecode(s):
    '''
    :param s:   format:   key=value&key2=value
    :return:
    '''
    res = []
    for i in s.split('&'):
        try:
            res.append('%s=%s' % (urllib.unquote(i.split('=')[0]),
                                  urllib.unquote(i.split('=')[1])))
        except:
            return
    return '&'.join(res)


if __name__ == '__main__':
    a = u'scope=bbs&q=C语言'
    b = u'{"abc":"123", "测试":"OK"}'
    c = 'scope=bbs&q=C%E8%AF%AD%E8%A8%80'
    print get_urlencode(a)
    print get_urlencode(b)
    print get_urldecode(c)

