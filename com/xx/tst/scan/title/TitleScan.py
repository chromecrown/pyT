#coding=utf-8

def getURLTitleByReq(URL,timeout=10):
    """
    调用requests请求http
    """
    import requests
    
    retData = {}#返回值字典
    titleStr = ""#title字符串值
    preTitle = "<title>"
    sufTitle = "</title>"
    try:
        r = requests.get(url,timeout=timeout)
        txt = r.text
        titlePreIndex = txt.find(preTitle)+len(preTitle)#<title>索引
        titleSufIndex = txt.find(sufTitle)#</title>索引
        titleStr = txt[titlePreIndex:titleSufIndex]
        
        retData["title"] = str(titleStr)
        retData["url"] = URL
    except Exception as e:
        print(e)
    finally:
        return retData

def getURLTitle(URL):
    """
    扫描一个url
    """
    import urllib2,socket
    retData = {}#返回值字典
    titleStr = ""#title字符串值
    preTitle = "<title>"
    sufTitle = "</title>"
    try:
        #socket.setdefaulttimeout(10)#10秒超时时间
        #urllib2.socket.setdefaulttimeout(10)#另一种设置方式
        #python2.6以后
        res = urllib2.urlopen(URL, timeout=10)
        #打开url并读取返回内容
        txt = res.read()
        titlePreIndex = txt.find(preTitle)+len(preTitle)#<title>索引
        titleSufIndex = txt.find(sufTitle)#</title>索引
        titleStr = txt[titlePreIndex:titleSufIndex]
        retData["title"] = str(titleStr)
        retData["url"] = URL
    except Exception as e:
        print(e)
    finally:
        return retData
    
if __name__=="__main__":
    url = "http://www.le.com"
    url = "http://10.150.140.110"
    url = "http://news.qq.com"
#     res = getURLTitle(url)
    res = getURLTitleByReq(url)
    print res