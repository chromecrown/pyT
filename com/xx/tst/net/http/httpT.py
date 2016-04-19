#coding=utf-8

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

if __name__ == "__main__":
    url = "http://www.baidu.com"
    res  = getHttp(url)
    print res