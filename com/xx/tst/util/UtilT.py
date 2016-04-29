#coding=utf-8

def lst2Tpl(lst):
    """
    transform type of list's argument from list to tuple
    return value:tuple
    """
    return tuple(lst)

def tpl2Lst(tpl):
    """
    transform type of tuple's argument from tuple to list
    return value:list
    """
    return list(tpl)

if __name__ == "__main__":
    l = [1,2,3,4,5]
    tpl = ('a','b','c')
    print lst2Tpl(l)
    print tpl2Lst(tpl)