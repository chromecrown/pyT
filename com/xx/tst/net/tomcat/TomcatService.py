#coding=utf-8
import urllib2,base64

def checkGoOn(host,port,user,password,timeout=10):
    """
    判断是否可以继续
    """
    if port=='443':
        url = "https://%s" %(host)
    else:
        url = "http://%s:%d" %(host,int(port))
    login_url = url+'/manager/html'
    code = -1
    try:
        request = urllib2.Request(login_url)
        auth_str_temp = user+':'+password
        auth_str = base64.b64encode(auth_str_temp)
        request.add_header('Authorization', 'Basic '+auth_str)
        res = urllib2.urlopen(request,timeout=timeout)
        code = int(res.code)
    except urllib2.HTTPError,e:
        code = e.code
    except urllib2.URLError,e:
        code = e.code
    except Exception as e:
        pass
    finally:
        return code