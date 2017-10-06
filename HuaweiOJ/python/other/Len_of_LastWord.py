# -*- coding: cp936 -*-
'''
计算字符串最后一个单词的长度，单词以空格隔开
样例输入 hello world
样例输出 5
这里注意字符串最后可能存在空格的情况
'''
def Len_of_LastWord(s):
    print len(s.split()[-1])
s=raw_input()
Len_of_LastWord(s)
