#coding=utf-8

def isDictInstance(obj):
    """
    是否字典类型
    """
    isDic = isinstance(obj,dict)
    return isDic

def isTupleInstance(obj):
    """
    是否元组类型
    """
    isTuple = isinstance(obj,tuple)
    return isTuple

def isListInstance(obj):
    """
    是否列表类型
    """
    isList = isinstance(obj,list)
    return isList

def isIntInstance(obj):
    """
    是否int类型
    """
    isInt = isinstance(obj,int)
    return isInt

if __name__ == "__main__":
    obj = "12"
    print isIntInstance(obj)