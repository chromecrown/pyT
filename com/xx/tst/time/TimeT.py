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

if __name__ == "__main__":
    r = getMonthShort()
    print r