#coding=utf-8

import subprocess

cmd = "ping"
p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
p.wait()

print p.stdout.readlines()