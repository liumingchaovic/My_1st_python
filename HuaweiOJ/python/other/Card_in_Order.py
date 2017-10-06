# -*- coding: cp936 -*-
'''
图片整理
Lily上课时使用字母数字图片教小朋友们学习英语单词，每次都需要把这些图片按照大小
（ASCII码值从小到大）排列收好。
'''
s=raw_input()
s=list(s)
s.sort()
print ''.join(s)
