# -*- coding: cp936 -*-
'''
����һ���ַ�����Ȼ������һ���ַ���ͳ���ַ����и��ַ��ĸ���
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
