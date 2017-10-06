# -*- coding: cp936 -*-
'''
连续输入字符串(输出次数为N,字符串长度小于100)，请按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
首先输入一个整数，为要输入的字符串个数。
例如：
输入：2
      abc
      12345789
输出：abc00000
      12345678
      90000000
'''
def String_Breakup(s):
    ss=''
    if s.strip()=='':
        return 0
    for i in range(len(s)):
        ss+=s[i]
        if i>0 and i%7==0:
            print ss
            ss=''
    if len(s)%8==0:
        pass
    else:
        for j in range(8-len(ss)):
            ss+='0'
        print ss

Num=input()
s_in=[]
for i in range(Num):
    s=raw_input()
    s_in.append(s)
for i in range(Num):
    String_Breakup(s_in[i])
        
