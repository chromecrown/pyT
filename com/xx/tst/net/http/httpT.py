#coding=utf-8

import urllib
from urllib import quote
import json

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

def postHttp(reqUrl,postArgDic={}):
    """
    send http post request
    """
    import urllib,urllib2
    try:
        encodedArg = urllib.urlencode(postArgDic)
        req = urllib2.Request(url=reqUrl,data=encodedArg)
        resObj = urllib2.urlopen(req)
        res = resObj.read()
        return res
    except Exception as e:
        print(e)
        return -1

def postHttp2(url,data={}):
    """
    send http post request
    """
    import urllib,urllib2
    try:
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        #enable cookie
        openner = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = openner.open(req,data)
        return response.read()
    except Exception as e:
        print(e)
        return -1


if __name__ == "__main__":
    pageRows = 1000
    page = "pageindex=$i&pagesize=$rows".replace("$rows",str(pageRows))
    url = "http://10.148.16.49:9090/sql/query?dbtype=spark&database=security&project=security&$page&sql=$sql"
    
#     sql = "select count(1) from uclogin where logintime>='2016-05-03 00:00:00' and logintime<='2016-05-03 23:59:59'"
    sql = "select count(1) from uclogin where logintime>='2016-05-03 00:00:00' and logintime<='2016-05-03 23:59:59'"
    sql = quote(sql)
    urlCnt = url.replace("$sql",sql)
    res  = getHttp(urlCnt)
    print res
    try:
        dicObj = json.loads(res)
        cntStr = dicObj["data"][0]["_c0"]#所有记录数量
        cnt = int(cntStr)
        print cnt,type(cnt)
        pageCnt = cnt/pageRows
        pageMod = cnt%pageRows
        if pageMod != 0:
            pageCnt = pageCnt + 1
        print "page count:",pageCnt
        sqlDist = "select distinct loginip from uclogin where logintime>='2016-05-03 00:00:00' and logintime<='2016-05-03 23:59:59'"
        sqlDist = quote(sqlDist)
        urlPage = url.replace("$sql",sqlDist)
        for pageNum in range(1,pageCnt):
            currentPage = page.replace("$i",str(pageNum))
            currentUrl = urlPage.replace("$page",currentPage)
            print "currentUrl:",currentUrl
            res = getHttp(currentUrl)
            dicObj = json.loads(res)
            lst = dicObj["data"]
            for one in lst:
                print "all rows is ",cntStr,",len of lst:",len(lst),",all pages:",pageCnt
                print "currentPage:",pageNum,"-->one:",one["loginip"]
    except Exception as e:
        print(e)