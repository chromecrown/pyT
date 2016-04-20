#coding=utf-8

import re
import socket
import sys
import time

def getWebClientIP(request):
    """
    获取网络访问客户端IP地址
    """
    ip = '0.0.0.0'
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
        ip =  request.META['HTTP_X_FORWARDED_FOR']  
    else:  
        ip = request.META['REMOTE_ADDR'] 
    return ip

def getLocalIP():
    """
    Returns the actual ip of the local machine.
    This code figures out what source address would be used if some traffic
    were to be sent out to some well known address on the Internet. In this
    case, a Google DNS server is used, but the specific address does not
    matter much.  No traffic is actually sent.
    """
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
        return addr
    except socket.error:
        return "127.0.0.1"
    
def validateDate(dateStr,fmtExp="%Y-%m-%d %H:%M"):
    """
    判断是否是一个有效的日期字符串
    """
    try:
        time.strptime(dateStr, fmtExp)
        return True
    except:
        return False
    
def validateDatetime(dateStr,fmtExp="%Y-%m-%d %H:%M:%S"):
    """
    判断是否是一个有效的日期时间字符串
    """
    try:
        time.strptime(dateStr, fmtExp)
        return True
    except:
        return False

def validateIP(str_m):
    """
    判断给定的字符串是否是合法ip地址
    如果是返回地址 
    否则返回None
    """
    ret_ip = None
    #匹配ip地址的正则表达式 判断是否是ip++
    patternIP = re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    is_match = patternIP.match(str_m)
    
    if is_match:
        #判断是合法ip
        ret_ip = is_match.group()
    return ret_ip

def validateInt(str_m):
    """
    判断给定的字符串是否是数字
    返回值说明
    如果是数字返回True
    不是返回False
    """
    isNum = False
    #匹配ip地址的正则表达式 判断是否是ip++
    patternIP = re.compile('^\d+$')
    is_match = patternIP.match(str_m)
    if is_match:
        #判断是数字
        isNum = True
    return isNum

def validateEmail(email):
    """
    验证给定的字符串是否是合法邮箱
    """
    if len(email) > 1:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False

def validatePhone(phoneStr):
    """
    验证给定的字符串是否是国内合法的手机号码
    """
    isPhone = False
    regex = re.compile(r'^1\d{10}$')
    isMatch = regex.match(phoneStr)
    if isMatch:
        isPhone = True
    return isPhone

def getIPInOut(ipStr):
    """
    获取给定的IP是内网还是外网
    返回值说明，内网返回in，外网返回out
    返回值为字符串类型
    """
    inOut = "in"
    #判断内网ip的正则表达式字符串
    re_inner_ip_str = r"(127[.]0[.]0[.]1)|" +"(localhost)|" + "(10[.]\d{1,3}[.]\d{1,3}[.]\d{1,3})|" + "(172[.]((1[6-9])|(2\d)|(3[01]))[.]\d{1,3}[.]\d{1,3})|" + "(192[.]168[.]\d{1,3}[.]\d{1,3})"
    p_inner_ip = re.compile(re_inner_ip_str)    
    
    #编译匹配内网ip的正则表达式
    m_inner_ip = p_inner_ip.match(ipStr)
    #判断是否是内网ip
    if m_inner_ip:
        inOut = "in"        
    else:
        #不是内网ip判断是外网
        inOut = "out"
    return inOut
    
def validateReg(oriStr,regStr):
    """
    参数说明  
    oriStr  要判断的字符串
    regStr  匹配的正则表达式
    判断给定的字符串是否符合给定的正则表达式
    返回值说明
    如果符合正则表达式返回True
    不是返回False
    """
    isLegal = False
    pattern = re.compile(regStr)
    is_match = pattern.match(oriStr)
    if is_match:
        #判断是否符合正则表达式
        isLegal = True
    return isLegal

def unicode2utf8(str_unicode):
    """
    如果给定字符串是unicode编码的字符串转为utf8编码格式
    """
    ret_str = str_unicode
    if isinstance(ret_str, unicode):
        ret_str = ret_str.encode('utf8')
    return ret_str

def get_cur_info():
    """
    获取当前位置所在的函数名和行号
    """
    fileName = sys._getframe().f_code.co_filename#当前文件名，可以通过__file__获得
    functionName = sys._getframe().f_code.co_name # 当前函数名
    lineNo = sys._getframe().f_lineno # 当前行号
    return (fileName,functionName,lineNo)

def escape(s, quote=None):
    '''
    替换特殊字符"&","<",">"为HTML安全的字符序列
    如果可选标识quote为true,引号字符(")也会被转义
    '''
    s = s.replace("&", "&amp;") # Must be done first!
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    if quote:
        s = s.replace('"', "&quot;")
    return s

if __name__ == "__main__":
    s = "18611127058"
    r = validatePhone(s)
    print r