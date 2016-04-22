#coding=utf-8

def nmap_scan(ip_str,args=" -vvv "):
    """
    用指定的参数扫描指定主机 指定端口
    需要的模块nmap 
    """
    import nmap
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_str,arguments=str(args))
    return nm 

if __name__ == "__main__":
    arg = "le.com"
    r = nmap_scan(arg,"-p 80,8080 -vvv")
    print r
    print r.command_line()
    print r.scaninfo()