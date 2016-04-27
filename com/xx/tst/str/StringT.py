#coding=utf-8

def getStrLength(s):
    """
    get length of string
    """
    return len(s)

def getIndex(s,substr):
    """
    return the index in str if find
    return -1 if not find 
    """
    return s.find(substr)

def replaceStr(s,old,new):
    """
    S.replace(oldstr, newstr, [count])    
    把S中的oldstr替换为newstr，count为替换次数
    """
    return s.replace(old, new)

def toLower(s):
    """
    小写
    """
    return s.lower()

def toUpper(s):
    """
    小写
    """
    return s.upper()

if __name__ == "__main__":
    s = "springframework"
    substr = "@"
    arg = getIndex(s, substr)
    print "arg:",arg
