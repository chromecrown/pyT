#coding=utf-8
import sys,json
import requests as req

reload(sys)
sys.setdefaultencoding("utf-8")

def getOneIPInfo(IPStr,ipUrl):
    """
    获取单个IP信息
    返回值为字典类型
    字典键包含
    ip  IP
    iptype  IP类型
    idcroom  机房
    bussinessname  业务
    phone  负责人电话
    email  邮件
    name 姓名
    modelname  模块
    """
    try:
        dicData = {}
        ipUrl = ipUrl.replace("$ip",IPStr)
        returnPage = req.post(ipUrl,allow_redirects = True,timeout=60)
        page = returnPage.text
        page = str(page)
        d = json.loads(page)
        if d.has_key("result"):
            lstInfo = d["result"]
            if len(lstInfo) > 0:
                dic2 = lstInfo[0]
                iptype = idcroom = bussinessname = phone = email = name = modelname = ""
                if dic2.has_key("machineip"):#机器信息
                    dicMachineip = dic2["machineip"]#type:list
                    if dicMachineip:
                        for oneDicOfMachineip in dicMachineip:
                            if oneDicOfMachineip.has_key("ip"):
                                ipTxt = oneDicOfMachineip["ip"]
                                if ipTxt == IPStr:
                                    if oneDicOfMachineip.has_key("iptype"):
                                        iptype = oneDicOfMachineip["iptype"]
                                        break
                if dic2.has_key("idcroom"):#业务信息
                    idcroomDic = dic2["idcroom"]
                    if idcroomDic.has_key("name"):
                        idcroom = idcroomDic["name"]
                if dic2.has_key("bussinessnameall"):#业务信息
                    bussinessname = dic2["bussinessnameall"]
                if dic2.has_key("owner"):#负责人信息
                    ownerLst = dic2["owner"]
                    if len(ownerLst) > 0:
                        owner = ownerLst[0]#dict类型
                        if owner.has_key("phone"):
                            phone = owner["phone"]
                        if owner.has_key("email"):
                            email = owner["email"]
                        if owner.has_key("name"):
                            name = owner["name"]
                        if owner.has_key("modelname"):
                            modelname = owner["modelname"]
        dicData["ip"] = IPStr
        dicData["iptype"] = str(iptype).strip()
        dicData["idcroom"] = str(idcroom).strip()
        dicData["bussinessname"] = str(bussinessname).strip()
        dicData["phone"] = str(phone).strip()
        dicData["email"] = str(email).strip()
        dicData["name"] = str(name).strip()
        dicData["modelname"] = str(modelname).strip()
#         print "IP=%s,类型=%s,IDC机房=%s,业务名称=%s,电话=%s,电子邮件=%s,姓名=%s,模块名称=%s"%(IPStr,iptype,idcroom,bussinessname,phone,email,name,modelname)
    except Exception as e:
        print(e)
        pass
    return dicData


if __name__ == "__main__":
    ipUrl = "http://lingshu.letv.cn/cmdb/cmdbapi/getmanageperpage?ip_query=$ip&link_token=b3f950ea0a46df02e68062c5f0d950c3"
    ipV = "115.182.92.134"
    retVal = getOneIPInfo(ipV,ipUrl)
    print retVal