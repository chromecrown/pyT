#coding=utf-8

def getStrLength(s):
    """
    get length of string
    """
    return len(s)

def testStr(s,substr):
    """
    """
    #字符串截取
    print s[0:-1]
    print s.find(substr)
    print s.index(substr)
    print s.rfind(substr)
    s.count(substr)#计算substr在字符串中出现的次数
    s.replace("old","new",1)#原来的字符串替换为新的字符串，最后的哦参数指定替换的次数
    #s.strip([chars]),把s中前后chars中所有的字符串全部去掉
    s.strip()
    
    
    #字符串的分割和组合
    s.split(",")
    
    #把指定的序列用给定的字符串连接起来
    lst = ['a','b','c']
    print s.join(lst)
    
    #字符串大小写
    """
    字符串中字符大小写的变换：
    S.lower()   #小写 
    S.upper()   #大写
    S.swapcase()   #大小写互换 
    S.capitalize()   #首字母大写 
    String.capwords(S)  #这是模块中的方法。它把S用split()函数分开，然后用
    capitalize()把首字母变成大写，最后用join()合并到一起
    S.title()    #只有首字母大写，其余为小写，模块中没有这个方法
    """
    
    """
    字符串的测试函数，这一类函数在string模块中没有，这些函数返回的都是bool值：
    S.startwith(prefix[,start[,end]]) #是否以prefix开头 
    S.endwith(suffix[,start[,end]])  #以suffix结尾 
    S.isalnum()  #是否全是字母和数字，并至少有一个字符 
    S.isalpha()  #是否全是字母，并至少有一个字符 
    S.isdigit()  #是否全是数字，并至少有一个字符 
    S.isspace() #是否全是空白字符，并至少有一个字符 
    S.islower() #S中的字母是否全是小写 
    S.isupper() #S中的字母是否便是大写 
    S.istitle() #S是否是首字母大写的
    """
    
    
    return 

if __name__ == "__main__":
    s = "springframework"
    substr = "@"
    arg = getStrLength(s)
    print "arg:",arg
