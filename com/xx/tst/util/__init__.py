#coding=utf-8

def ifDictInstance(obj):
    """
    是否字典类型
    """
    isDic = isinstance(obj,dict)
    return isDic

if __name__ == "__main__":
    obj = {}
    print ifDictInstance(obj)