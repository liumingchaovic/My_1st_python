# -*- coding: cp936 -*-
'''
ͳ���ַ����д�д��ĸ�ĸ���
'''
def Num_of_Upper(s):
    Num=0
    for i in range(len(s)):
        if 'A'<=s[i]<='Z':
            Num+=1
    print Num
s=raw_input()
Num_of_Upper(s)
