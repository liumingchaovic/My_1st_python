# -*- coding: cp936 -*-
'''
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数

'''
def EnglishChar(s):
    count=0
    for c in s:
        if 'a'<=c<='z':
            count+=1
    return count
def BlankChar(s):
    count=0
    for c in s:
        if c==' ':
            count+=1
    return count
def NumChar(s):
    count=0
    for c in s:
        if '0'<=c<='9':
            count+=1
    return count
def OtherChar(s):
    count=0
    for c in s:
        if not ('a'<=c<='z' or c==' ' or '0'<=c<='9'):
            count+=1
    return count

s=raw_input()
print EnglishChar(s)
print BlankChar(s)
print NumChar(s)
print OtherChar(s)
