#coding=utf-8
import os

currentPath = os.getcwd()
oct(os.stat(currentPath).st_mode)

octVal = oct(os.stat(currentPath).st_mode)[-3:]
print "octVal:",octVal
