# -*- coding: cp936 -*-
'''
����n�����������������С��k����
����˵�� 
1 ������������ 
2 ����һ����������
���һ����������

ʾ�����룺
5 2
1 3 5 7 2
ʾ�������
1 2
'''
def Least_k_in_n(s,k):
    s.sort()
    for i in range(k):
        print s[i],

n_k=raw_input().split()
n=int(n_k[0])
k=int(n_k[1])
s=raw_input().split()
for i in range(len(s)):
    s[i]=int(s[i])
Least_k_in_n(s,k)
