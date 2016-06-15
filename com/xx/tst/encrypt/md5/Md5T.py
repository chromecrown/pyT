#coding=utf-8

def getMd5Code(srcStr):
    """
    get md5 code 
    """
    import md5
    mCode = ""
    try:
        m1 = md5.new()
        m1.update(srcStr)
        mCode = m1.hexdigest()
    except Exception as e:
        print(e)
    return mCode

def getMd5Code2(srcStr):
    """
    another method to get md5 code
    """
    import hashlib
    mCode = ""
    try:
        m2 = hashlib.md5()
        m2.update(srcStr)
        mCode = m2.hexdigest()
    except Exception as e:
        print(e)
    return mCode