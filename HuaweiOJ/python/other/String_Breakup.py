# -*- coding: cp936 -*-
'''
���������ַ���(�������ΪN,�ַ�������С��100)���밴����Ϊ8���ÿ���ַ�����������µ��ַ������飬
���Ȳ���8���������ַ������ں��油����0�����ַ���������
��������һ��������ΪҪ������ַ���������
���磺
���룺2
      abc
      12345789
�����abc00000
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
        
