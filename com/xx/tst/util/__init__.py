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

def isBoolInstance(obj):
    """
    是否bool类型
    """
    isBool = isinstance(obj,bool)
    return isBool

if __name__ == "__main__":
    obj = True
    print isBoolInstance(obj)