# -*- coding: cp936 -*-
'''
���ֵ�Ư����
����ÿ��������˵�����ֵ�Ư����=26*��ĸ��������+25*��ĸ������ε�+������
��������NΪN������
�����Ӧ�����ֵ�Ư����
ʾ�����룺
2
zhangsan
lisi
ʾ�������
192
101
'''
def Beauty_Name(s):
    d={}
    for c in s:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    lst=[(d[w],w) for w in d]
    lst.sort()
    lst.reverse()
    score=0
    for i in range(len(lst)):
        score+=(26-i)*lst[i][0]
    print score
N=input()
s=[]
for i in range(N):
    s.append(raw_input())
for i in range(N):
    Beauty_Name(s[i])
