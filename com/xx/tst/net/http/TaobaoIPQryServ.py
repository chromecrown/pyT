#coding=utf-8

from urllib import quote
import urllib
import MySQLdb
import sys,os

reload(sys)
sys.setdefaultencoding('utf8')

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

def execSQL(sql):
    """
    execute sql on mysql
    """
    db = getMySQLConn(dbname="weblog")
    cursor = db.cursor()
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
        if dicData.has_key("code") and dicData["code"] == 0:
            returnVal = dicData["data"]
    except Exception as e:
        print(e)
        return returnVal
    return returnVal

def getCurrentTime():
    """
    获取当前时间
    返回当前时间字符串
    格式  
    """
    import time
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S")
    return  timeStr

def save2DB(IPStr,dateStr):
    """
    save ip belong information to database
    """
    dicData = getIPBelong(IPStr)
    conn = getMySQLConn()
    updatetime = getCurrentTime()#当前时间
    try:
        if dicData.has_key("ip"):
            ipStr = dicData["ip"]
        else:
            ipStr = ""
            
        if dicData.has_key("city"):
            city = dicData["city"]
        else:
            city = ""
            
        if dicData.has_key("area_id"):
            area_id = dicData["area_id"]
        else:
            area_id = ""
            
        if dicData.has_key("region_id"):
            region_id = dicData["region_id"]
        else:
            region_id = ""
            
        if dicData.has_key("area"):
            area = dicData["area"]
        else:
            area = ""
            
        if dicData.has_key("city_id"):
            city_id = dicData["city_id"]
        else:
            city_id = ""
            
        if dicData.has_key("country"):
            country = dicData["country"]
        else:
            country = ""
            
        if dicData.has_key("region"):
            region = dicData["region"]
        else:
            region = ""
            
        if dicData.has_key("country_id"):
            country_id = dicData["country_id"]
        else:
            country_id = ""
            
        if dicData.has_key("county"):
            county = dicData["county"]
        else:
            county = ""
            
        if dicData.has_key("isp_id"):
            isp_id = dicData["isp_id"]
        else:
            isp_id = ""
            
        if dicData.has_key("county_id"):
            county_id = dicData["county_id"]
        else:
            county_id = ""
            
        if dicData.has_key("area"):
            area = dicData["area"]
        else:
            area = ""
        if dicData.has_key("isp"):
            isp = dicData["isp"]
        else:
            isp = ""
            
        cursor = conn.cursor()
        sql = "INSERT INTO ip_belong(ip,country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id,update_time,insert_day)" +\
        " VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(IPStr,country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id,updatetime,dateStr)
        print "method ==>save2DB=>sql->",sql
        cursor.execute(sql)
        conn.commit()
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
            for ipRow in ipResult:
                indexIP = indexIP + 1
                oneIP = ipRow[0]
                save2DB(oneIP,oneDateStr)
    except Exception as e:
        print(e)
    finally:
        closeConn(db)
    
if __name__ == "__main__":
    ipstr = "171.95.208.52"
    getSrcIPLstServ()
#     sql = """
#     INSERT INTO ip_belong(ip,country,country_id,area,area_id,region,region_id,city,city_id,county,county_id,isp,isp_id,update_time,insert_day) VALUES('171.95.208.52','','','','','','','','','','','','','2016-05-10 10:13:24','2016-04-29')
#     """
    #execSQL(sql)
    #ret = getIPBelong(ipstr)