#coding=utf-8

#coding=utf-8

from urllib import quote
import urllib
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

def execSQL():
    """
    execute sql on mysql
    """
    db = getMySQLConn(dbname="weblog")
    cursor = db.cursor()
    sql = """
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback() 
    finally:
        closeConn(db)

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

def save2DB(IPStr):
    """
    save ip belong information to database
    """
    dicData = getIPBelong(IPStr)
    print "dicData;",dicData

def getSrcIPLstServ():    
    """
    """
    from time import clock
    
    dateLst = []
    #打开数据库连接
    db = getMySQLConn()
    cursor = db.cursor()
    #sql = "select * from ip_req where getDay='$day'".replace("$day",dateStr)
    sqlCnt = "select count(1) from ip_belong where ip=$"
    sqlDateLst = "select distinct getDay from ip_req"
    try:
        #执行sql语句
        cursor.execute(sqlDateLst)
        #获取所有记录列表
        dateStrResults = cursor.fetchall()
        print type(dateStrResults)
        print "len(dateStrResults):",len(dateStrResults)
        indexV = 0
        for row in dateStrResults:
            indexV = indexV + 1
            dateStr = row[0]
            print "indexV:",indexV," ip:",dateStr 
            dateLst.append(dateStr)
        indexIP = 0
        for oneDateStr in dateLst:
#             sqlGetIP = "select hostip from ip_req where getDay='$day'".replace("$day",oneDateStr)
            sqlIP = """
                select hostip from ip_req r
                where r.getDay='$day' 
                and r.hostip not in(select ip from ip_belong)
            """
            sqlGetIP = sqlIP.replace("$day",oneDateStr)
            cursor.execute(sqlGetIP)
            ipResult = cursor.fetchall()
            startTime = clock()#开始计时
            for ipRow in ipResult:
                indexIP = indexIP + 1
                oneIP = ipRow[0]
                print "date is ",oneDateStr,"index is ",indexIP,oneIP
                nowTime = clock()
                internalSec = float((nowTime - startTime)/1000)
                print "(nowTime - startTime):",internalSec
                save2DB(oneIP)
                startTime = clock()
    except Exception as e:
        print(e)
    finally:
        closeConn(db)
    
if __name__ == "__main__":
    ipstr = "1.1.1.7"
    getSrcIPLstServ()