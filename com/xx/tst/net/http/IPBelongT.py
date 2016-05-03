#coding=utf-8

def getNetIPBelongInfo(IPStr,urlIPBelong=""):
    """
    调用网络开放接口查询网络IP的归属地信息
    返回字典类型,如
 {"code":0,"data":{"ip":"210.75.225.254","country":"\u4e2d\u56fd","area":"\u534e\u5317",
    "region":"\u5317\u4eac\u5e02","city":"\u5317\u4eac\u5e02","county":"","isp":"\u7535\u4fe1",
    "country_id":"86","area_id":"100000","region_id":"110000","city_id":"110000",
    "county_id":"-1","isp_id":"100017"}}
    """
    import json,urllib
    urlIPBelong = "http://ip.taobao.com/service/getIpInfo.php?ip=$IP"
    retDic = {}
    if urlIPBelong:
        IPQryService = urlIPBelong.replace("$IP",IPStr)
        try:
            openObj = urllib.urlopen(IPQryService)
            retStr = openObj.read()
            if retStr:
                _dicObj = json.loads(retStr)
                if _dicObj.has_key("code"):
                    #code=0:成功,code=1:失败
                    if _dicObj["code"] == 0:
                        if _dicObj.has_key("data"):
                            dataDic = _dicObj["data"]
                            retDic = dataDic
                    elif _dicObj["code"] == 1:
                        retDic = {}
        except Exception as e:
            print e
    return retDic

if __name__ == "__main__":
    IPVal = "221.239.59.66"
    re = getNetIPBelongInfo(IPVal)
    print type(re)
    print re