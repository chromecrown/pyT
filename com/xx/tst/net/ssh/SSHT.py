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
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
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
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
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
    