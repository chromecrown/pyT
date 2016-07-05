#coding=utf-8

import paramiko

def sshCon(hostname, port, username, password):
    """
    探测ssh连接是否成功
    返回结果为字典类型
    成功 code 为1
    失败 code 为-1
    """
    retDic = {}
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        retDic["code"] = 1
    except Exception as e:
        print(e)
        retDic["code"] = -1
        pass
    finally:
        return retDic
    
def sshExecCmd(hostname, port, username, password, cmd):
    """
    ssh连接之后执行命令
    返回值为字符串类型
    表示命令执行结果
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        stdin,stdout,stderror = ssh.exec_command(cmd)
        cmdResult = stdout.readlines()
        print cmdResult
    except Exception as e:
        print(e)
        cmdResult = "error"
        pass
    finally:
        return cmdResult

def getFile(hostname,port,username,password):
    """
    从windows端下载linux服务器上的文件
    """
    try:
        t = paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = "/var/log/secure"
        localpath = "D:/data/secure"
        files = sftp.listdir("/root/")
        for f in files:
            print "f-->",f
        sftp.get(remotepath,localpath)
        t.close()
    except Exception as e:
        print(e)
        
def putFile(hostname,port,username,password):
    """
    从windows端上传文件到linux服务器
    """
    try:
        t = paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        remotepath = "/root/me/secure"
        localpath = "D:/data/secure.txt" 
        sftp.put(localpath,remotepath)
        t.close()
    except Exception as e:
        print(e)   
    
if __name__ == "__main__":
    h = "10.75.144.201"
    port = 22
    u = "root"
    p = "000000"
    res = sshCon(h, port, u, p)
    res2 = sshExecCmd(h, port, u, p,"whoami")
    print res,res2
    getFile(h,port,u,p)
    putFile(h,port,u,p)