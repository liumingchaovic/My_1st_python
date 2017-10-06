# -*- coding: cp936 -*-
'''
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新整数
如果返回的整数以0开头，去掉0
不考虑负数
例如：input:1010 output:1
示例输入：9876673
示例输出：37689
'''
def Int_Reverse(s):
    s=str(s)
    s=list(s)
    s.reverse()
    ss=''
    for i in range(len(s)):
        if s[0:i].count(s[i])==0:
            ss+=s[i]
    print int(ss)
s=input()
Int_Reverse(s)
