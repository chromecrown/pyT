#coding=utf-8

#coding=utf8

import os,socket

def bannerTest(ip,port=6379):
    """
    """
    res = -1#返回值
    #创建一个TCP类型的socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #设置超时时间
    s.settimeout(10.0)
    try:
        #尝试连接端口，如果返回值不为0,表示端口没有开放
        connResult = s.connect_ex((ip,port))
        if connResult != 0:
            return res
        #发送PING命令
        s.sendall("PING\r\n")
        #接收返回数据
        msg = s.recv(1024)
        print "msg:",msg
        #如果返回的数据包含PONG,表明是redis且不需要密码
        if msg.find("PONG") != -1:
            res = 1
        #如果返回的数据包中包含NOAUTH,表明是redis但需要密码
        elif msg.find("NOAUTH") != -1:
            res = 0
    except Exception as e:
        print "exception happened ",e
        pass
    finally:
        #关闭socket连接
        s.close()
    return res

if __name__ == "__main__":
    _ip = "10.183.91.21"
    for i in range(9900,9930):
        retCode = bannerTest(_ip,i)
        print 'now will test port is ',i,"result is ",retCode
        if retCode == 0:
            print "port:",i," retCode:",retCode