# -*- coding: cp936 -*-
'''
输入n个整数，输出其中最小的k个。
输入说明 
1 输入两个整数 
2 输入一个整数数组
输出一个整数数组

示例输入：
5 2
1 3 5 7 2
示例输出：
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
