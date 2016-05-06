#coding=utf-8

#coding=utf-8

import urllib
from urllib import quote
import json
import MySQLdb

def getMySQLConn(host='10.150.140.108',usr='root',pwd='mysqlroot',dbname='weblog'):
    
    """
    get and return mysql connection object
    """
    #open db Connection
    conn = MySQLdb.connect(host,usr,pwd,dbname)
    return conn

def closeConn(dbConn):
    """
    close openned mysql connection
    """
    if dbConn:
        try:
            dbConn.close()
        except Exception as e:
            print(e)

def insertIPData(conn,IPStr,getDay):
    """
    test insert record to mysql
    """
    cursor = conn.cursor()
    sql = "INSERT INTO ip_req(hostip,getDay) VALUES ('%s','%s')"%(IPStr,getDay)
    print "==>sql:",sql
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback() 

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

def getReqLoginip():
    """
    get login ip from spark sql
    """
    dayStr = "2016-05-04"
    conn = getMySQLConn(dbname="weblog")
    pageRows = 2000
    page = "pageindex=$i&pagesize=$rows".replace("$rows",str(pageRows))
    url = "http://10.148.16.49:9090/sql/query?dbtype=spark&database=security&project=security&$page&sql=$sql"
    #http://ip.taobao.com/service/getIpInfo.php?ip=~
    
#     sql = "select count(1) from uclogin where logintime>='2016-05-03 00:00:00' and logintime<='2016-05-03 23:59:59'"
    sql = "select count(1) from uclogin where logintime>='$dayStr 00:00:00' and logintime<='$dayStr 23:59:59'".replace("$dayStr", dayStr)
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
        sqlDist = "select distinct loginip from uclogin where logintime>='$dayStr 00:00:00' and logintime<='$dayStr 23:59:59'".replace("$dayStr",dayStr)
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
                loginipStr = one["loginip"]
                print "all rows is ",cntStr,",len of lst:",len(lst),",all pages:",pageCnt
                print "currentPage:",pageNum,"-->one:",loginipStr
                insertIPData(conn,loginipStr,dayStr)
    except Exception as e:
        print(e)
    finally:
        closeConn(conn)

if __name__ == "__main__":
    getReqLoginip()