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

def createTbl():
    """
    test create table in mysql database
    """
    db = getMySQLConn(dbname="test")
    cursor = db.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    
    sql = """
        CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )
         """
    cursor.execute(sql)
    closeConn(db)

def insertData():
    """
    test insert record to mysql
    """
    db = getMySQLConn(dbname="test")
    cursor = db.cursor()
    sql = """
    INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)
    """
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback() 
    finally:
        closeConn(db)
        
def insertIPData(IPStr,getDay):
    """
    test insert record to mysql
    """
    db = getMySQLConn(dbname="weblog")
    cursor = db.cursor()
    sql = "INSERT INTO ip_req(hostip.getDay) VALUES (%s,%s)"%(IPStr,getDay)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback() 
    finally:
        closeConn(db)