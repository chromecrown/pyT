#coding=utf-8

def nmap_scan(ip_str,args=""):
    """
    用指定的参数扫描指定主机 指定端口
    需要的模块nmap
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
            print "allProtocols:",allProtocols
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
    print "all_hosts:",all_hosts
    return returnVal 

if __name__ == "__main__":
    arg = "10.150.140.110"
    arg = "10.182.200.75"
#     arg = "103.1.40.108"
    r = nmap_scan(arg,args=" -Pn -sV --script=banner -p 80")
    print "==>",r
