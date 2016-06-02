#coding=utf-8

def reqURL(url,user="admin",password="admin",timeout=10):
    """
    请求一个url
    返回值说明
        字典类型
        code  返回状态码  
        page  返回http响应内容
    """
    import urllib2,base64
    dicD = {}
    res_code = res_html = ""
    try:
        request = urllib2.Request(url)
        auth_str_temp = user+':'+password
        auth_str=base64.b64encode(auth_str_temp)
        request.add_header('Authorization', 'Basic '+auth_str)
        res = urllib2.urlopen(request,timeout=timeout)
        res_code = res.code
        res_html = res.read()
    except urllib2.HTTPError,e:
        res_code = e.code
        res_html = e.read()
    except urllib2.URLError,e:
        print(e)
    dicD["code"] = str(res_code)
    dicD["page"] = str(res_html)
    return dicD 