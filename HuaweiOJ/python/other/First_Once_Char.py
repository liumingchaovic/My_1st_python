# -*- coding: cp936 -*-
'''
�ҳ��ַ����е�һ��ֻ����һ�ε��ַ�
����޴��ַ��������'.'
'''
def First_Once_Char(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            print s[i]
            break
        elif i==len(s)-1 and s.count(s[i])!=1:
            print '.'
        else:
            pass
    '''
    ��ѭ�����е�ԭ������s.index(c)==len(s)-1�����Ǳ��������ж��Ƿ������һ���ַ�
    ����index���ص��ǵ�һ���ҵ�c������ֵ�������������c�����������
    for c in s:
        if s.count(c)==1:
            print c
            break
        elif s.index(c)==len(s)-1 and s.count(c)!=1:
            print '.'
        else:
            pass
    '''
s=raw_input()
First_Once_Char(s)
