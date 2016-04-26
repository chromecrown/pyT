#coding=utf-8
from datetime import datetime

def getCurrentTime():
    """
    获取当前时间
    返回当前时间字符串
    格式  
    """
    import time
    timeStr = time.strftime("%Y-%m-%d %H:%M:%S")
    return  timeStr

def getCurrentTimeFmt(fmt="%Y-%m-%d %H:%M:%S"):
    """
    获取当前时间的指定格式
    格式有fmt参数指定  
    """
    import time
    timeStr = ""
    try:
        timeStr = time.strftime(fmt)
    except Exception as e:
        print(e)
        return ""
    return  timeStr

def getCurrentWeekShort():
    """
    获取当前星期英文简写
    """
    weekStr = ""
    import datetime
    try:
        now = datetime.datetime.now()
        weekStr = now.strftime("%a")
    except Exception as e:
        print(e)
        return weekStr
    return weekStr

def getCurrentMonth():
    """
    输出完整的星期几英文名称
    """
    import datetime
    currentAllWeekStr = ""
    now = datetime.datetime.now()
    currentAllWeekStr = now.strftime("%A")
    return currentAllWeekStr

def getMonthShort():
    """
    月份英文简写
    """
    import datetime
    monthShortStr = ""
    now = datetime.datetime.now()
    monthShortStr = now.strftime("%b")
    
    return monthShortStr

def getMonthAll():
    """
    月份英文简写
    """
    import datetime
    monthShortStr = ""
    now = datetime.datetime.now()
    monthShortStr = now.strftime("%B")
    
    return monthShortStr

def getTimestamp(datetimeStr):
    """
    transform datetime formated yyyy-MM-dd HH:mm:ss string to timestamp
    return value of float
    """
    import datetime,time
    longDatetimestamp = 0.0
    try:
        d = datetime.datetime.strptime(datetimeStr,"%Y-%m-%d %H:%M:%S")
        longDatetimestamp = time.mktime(d.timetuple())
        return longDatetimestamp
    except Exception as e:        
        return ""

def getYear(datetimeStr):
    """
    get year value from the given datetime string
    """
    try:
        if datetimeStr:
            yearStr = datetimeStr[0:4]
            return int(yearStr)
    except Exception as e:
        print(e)
        pass
    return 1970

def getMonth(datetimeStr):
    """
    get month value from the given datetime string
    """
    try:
        if datetimeStr:
            d = datetime.datetime.strptime(datetimeStr,"%Y-%m-%d %H:%M:%S")
            monthStr = datetimeStr[5:7]
            return int(monthStr)
    except Exception as e:
        return datetimeStr
    return 12

def getDay(datetimeStr):
    """
    get day value from the given datetime string
    """
    try:
        if datetimeStr:
            d = datetime.datetime.strptime(datetimeStr,"%Y-%m-%d %H:%M:%S")
            dayStr = datetimeStr[8:10]
            return int(dayStr)
    except Exception as e:
        return datetimeStr
    return 28

def getFormatedTime(fmt="%Y%m%d000000"):
    """
    get time formate of yyyyMMdd000000 time string
    """
    import time
    tStr = ""
    try:
        tStr = time.strftime(fmt,time.localtime(time.time()))
    except:
        pass
        return tStr
    return tStr 

if __name__ == "__main__":
    args = "2015-08-05 12:09:12"
    args = "190"
    r = getFormatedTime()
    print r