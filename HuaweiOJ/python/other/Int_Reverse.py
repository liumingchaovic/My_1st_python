# -*- coding: cp936 -*-
'''
����һ��int�����������մ���������Ķ�˳�򣬷���һ�������ظ����ֵ�������
������ص�������0��ͷ��ȥ��0
�����Ǹ���
���磺input:1010 output:1
ʾ�����룺9876673
ʾ�������37689
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
