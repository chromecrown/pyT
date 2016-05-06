#coding=utf-8

#coding=utf-8

import urllib
from urllib import quote

def getHttp(url):
    """
    发送get请求
    """
    import urllib2
    res = ""
    try:
        response = urllib2.urlopen(url)
        res = response.read()
    except Exception as e:
        print "ee:",e
    return res

def getIPBelong(IPStr):
    """
    get ip belong area
    """
    import json
    try:
        url = "http://ip.taobao.com/service/getIpInfo.php?ip=$"
        url = url.replace("$",IPStr)
        res = getHttp(url)
        print "res",res
        print type(res)
        dicData = json.loads(res)
        print "dic data:",dicData
        print "type(dicData):",type(dicData)
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    ipstr = "8.8.8.8"
    getIPBelong(ipstr)