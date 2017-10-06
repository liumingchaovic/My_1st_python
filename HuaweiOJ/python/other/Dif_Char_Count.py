# -*- coding: cp936 -*-
'''
字符个数统计：
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。
不在范围内的不作统计。

这里最主要的其实就是区分不同字符，在python中可以使用集合set很方便的实现
'''
s=raw_input()
ss=set(s)
count=0
for c in ss:
    if 0<=ord(c)<=127:
        count+=1
print count
