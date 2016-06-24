#coding=utf-8
import urllib2
import base64

def checkGoOn(host,port,user,password,timeout=10):
    """
    判断指定主机 端口 用户名 密码是否可以正确连接
    返回值说明
        字典类型
        host:主机
        port:端口
        user:用户名
        password:密码
        code 200:表示成功,其他表示认证失败
    """
    retDic = {}
    if port=='443':
        url = "https://%s" %(host)
    else:
        url = "http://%s:%d" %(host,int(port))
    login_url = url+'/manager/html'
    code = -1
    try:
        request = urllib2.Request(login_url)
        auth_str_temp = "%s:%s"%(user,password)
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
        retDic["host"] = host
        retDic["port"] = port
        retDic["user"] = user
        retDic["password"] = password
        retDic["code"] = code
        return retDic
    
if __name__ == "__main__":
    host = "localhost"
    port = "8080"
    user = "admin"
    password = "admin"
    code = checkGoOn(host,port,user,password)
    print "code:",code
    #ret = deploy.autoDoploy(host, port, 10, user,password)
    #print "code:",code,"ret:",ret