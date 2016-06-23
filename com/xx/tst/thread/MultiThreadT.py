#coding=utf-8

import threading
import time
from multiprocessing import cpu_count

taskLst = []

def doJob(task):
    """
    the specify process job method
    """
    try:
        print "current thread name is %s"%(threading.current_thread().getName())
        time.sleep(3)
        print "do something,handle current task ",task
    except Exception as e:
        print(e)
        pass

def mainCall(times=5,func=None,taskLst=[]):
    """
    线程调度方法
    """
    cpus = times*cpu_count()#同时开启的最大线程数量
    activeCnt = threading.activeCount()#当前活动的线程数
    taskCnt = len(taskLst)#任务总数
    if taskCnt > 0:
        if taskCnt < cpus:
            for e in taskLst:
                t = threading.Thread(target=func,args=(e,))
                t.start()
        elif taskCnt > cpus:
            while taskCnt > 0:
                needCnt = cpus - threading.activeCount() + activeCnt
                if needCnt == 0:
                    taskCnt = len(taskLst)
                    time.sleep(1)
                elif needCnt > 0:
                    for e in range(0,needCnt):
                        taskCnt = len(taskLst)
                        if taskCnt > 0:
                            t2 = threading.Thread(target=func,args=(taskLst.pop(),))
                            t2.start()
if __name__ == "__main__":
    taskLst = range(1,50)
    mainCall(times=5,func=doJob,taskLst=taskLst)