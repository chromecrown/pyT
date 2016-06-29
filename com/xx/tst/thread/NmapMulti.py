#coding=utf-8

import threading
import time,json
from multiprocessing import cpu_count

def postHttp(url,data={}):
    """
    send http post request
    """
    import urllib,urllib2
    try:
        req = urllib2.Request(url)
        data = urllib.urlencode(data)
        #enable cookie
        openner = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        response = openner.open(req,data)
        return response.read()
    except Exception as e:
        print(e)
        return -1

def mainCall(times=5,func=None,taskLst=[]):
    """
    线程调度方法
    times:cpu核心倍数
    func:多线程将要调度的方法
    taskLst:任务列表
    """
    try:
        cpus = times*cpu_count()#同时开启的最大线程数量
        activeCnt = threading.activeCount()#当前活动的线程数
        taskCnt = len(taskLst)#任务总数
        initTaskCnt = len(taskLst)#任务总数
        print "max thread count:%d,current thread count:%d,initial task count:%d"%(cpus,activeCnt,initTaskCnt)
        if taskCnt > 0:#确保任务总数大于0
            if taskCnt < cpus:#任务总数小于最大线程数量
                print "task count:%d,less than max thread count"%(taskCnt)
                for e in taskLst:
                    t = threading.Thread(target=func,args=(e,))
                    t.start()
            elif taskCnt > cpus:
                print "task count:%d,more than max thread count"%(taskCnt)
                while taskCnt > 0:
                    needCnt = cpus - threading.activeCount() + activeCnt#计算需要启动的线程数量
                    if needCnt == 0:
                        taskCnt = len(taskLst)
                        time.sleep(1)
                        print "need start thread count is %d,all task count is %d,left task count is %s"%(needCnt,initTaskCnt,taskCnt)
                    elif needCnt > 0:
                        for e in range(0,needCnt):
                            taskCnt = len(taskLst)
                            if taskCnt > 0:
                                t2 = threading.Thread(target=func,args=(taskLst.pop(),))
                                t2.start()
    except Exception as e:
        print(e)

def nmapScan(ip_str,args=""):
    """
    用指定的参数扫描指定主机 指定端口
    需要的模块nmap
    参数  -vvv -sV --script=banner
    scan result:
    {
        'host': '10.182.200.75',
        'tcp': {
            80: {
                'product': 'nginx',
                'state': 'open',
                'version': '1.7.12',
                'name': 'http',
                'conf': '10',
                'script': {
                    'http-server-header': 'nginx/1.7.12'
                },
                'extrainfo': '',
                'reason': 'syn-ack',
                'cpe': 'cpe: /a: igor_sysoev: nginx: 1.7.12'
            }
        }
    }
    """
    import nmap
    returnVal = {}
    returnVal["host"] = ip_str
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_str,arguments=str(args))
    all_hosts = nm.all_hosts()#list
    for host in all_hosts:
        nmHostObj = nm[host]
        hostname = nmHostObj.hostname()#hostname
        #get state os host(up|down|unknown|skipped)
        state = nmHostObj.state()
        
        if state == "up":
            #get all scanned protocols['tcp','udp']in(ip|tcp|udp|sctp)
            allProtocols = nmHostObj.all_protocols()#type:list
#             print "allProtocols:",allProtocols
            for protl in allProtocols:
                allPorts = nmHostObj[protl].keys()#get all ports for protl protocol
                print "allPorts:",allPorts
                if protl == "tcp":
                    tcpDicObj = {}
                    for port in allPorts:
                        if nmHostObj.has_tcp(port):#if there  any information for  port/tcp on host
                            tcpPortInfo = nmHostObj['tcp'][port]#type:dic
                            tcpDicObj[port] = tcpPortInfo
#                             print "portInfo and type is:",tcpPortInfo,type(tcpPortInfo)
                    returnVal["tcp"] = tcpDicObj
                elif protl == "udp":
                    udpDicObj = {}
                    for port in allPorts:
                        if nmHostObj.has_tcp(port):#if there  any information for port/tcp on host
                            udpPortInfo = nmHostObj['udp'][port]#type:dic
                            udpDicObj[port] = udpPortInfo
                    returnVal["udp"] = udpDicObj  
#     print "all_hosts:",all_hosts
    return returnVal

def nmapScanServ(ipStr,args="-vvv -sV --script=banner -p1-65535"):
    """
    调用nmap扫描
    """
    try:
        print "now will scan ip is %s"%(ipStr)
        scanRes = nmapScan(ipStr, args)
        url = "http://10.75.139.88:8000/pentest/open/rxInfo"
        data = {}
        data["scanInfo"] = json.dumps(scanRes)
        resp = postHttp(url, data)
        print "response from http:",resp
        print "-->",scanRes
    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    taskLst = []
    with open("ip.txt","r") as fi:
        for e in fi:
            taskLst.append(e.strip())
    mainCall(times=10,func=nmapScanServ,taskLst=taskLst)