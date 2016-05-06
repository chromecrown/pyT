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
    return value:dict type
    """
    import json
    returnVal = {}
    try:
        url = "http://ip.taobao.com/service/getIpInfo.php?ip=$"
        url = url.replace("$",IPStr)
        res = getHttp(url)
        dicData = json.loads(res)
        returnVal = dicData
    except Exception as e:
        print(e)
        return returnVal
    return returnVal

if __name__ == "__main__":
    ipstr = "1.1.1.7"
    getIPBelong(ipstr)