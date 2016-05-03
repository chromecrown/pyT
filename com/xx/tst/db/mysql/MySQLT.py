#coding=utf-8

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


def getMySQLVer():
    """
    get version of mysql
    """
    db = getMySQLConn()
    cursor = db.cursor()
    cursor.execute("select version()")
    versionData = cursor.fetchone()
    
    return versionData 


print "Database version is",getMySQLVer()