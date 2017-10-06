# -*- coding: cp936 -*-
'''
找出字符串中第一个只出现一次的字符
如果无此字符，请输出'.'
'''
def First_Once_Char(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            print s[i]
            break
        elif i==len(s)-1 and s.count(s[i])!=1:
            print '.'
        else:
            pass
    '''
    此循环不行的原因在于s.index(c)==len(s)-1，我们本意是在判断是否到了最后一个字符
    但是index返回的是第一次找到c的索引值，如果存在两个c的情况则会出错
    for c in s:
        if s.count(c)==1:
            print c
            break
        elif s.index(c)==len(s)-1 and s.count(c)!=1:
            print '.'
        else:
            pass
    '''
s=raw_input()
First_Once_Char(s)
