# -*- coding: cp936 -*-
'''
输入一个字符串，然后输入一个字符，统计字符串中该字符的个数
'''
def Char_Statistics_in_String(s,a):
    count=0
    for c in s:
        if c.upper()==a.upper():
            count+=1
    print count
s=raw_input()
a=raw_input()
Char_Statistics_in_String(s,a)
