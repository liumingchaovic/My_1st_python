# -*- coding: cp936 -*-
'''
合唱队
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学不交换位置就能排成合唱队形。 
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1, 2, …, K，他们的身高分别为T1, T2, …, TK，
则他们的身高满足T1 < T2 < … < Ti , Ti > Ti+1 > … > TK (1 <= i <= K) 。 
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

输入：
第一行整数 N，表示同学的总数 
第二行整数数组，空格隔开，表示 N 位同学身高

输出：
最少需要几位同学出列

样例输入：
8
186 186 150 200 160 130 197 2001

样例输出：
4
'''
N=input()
s=raw_input().split()
ss=[]
listrise=[]
listdown=[]
max_len=0
for c in s:
    ss.append(int(c))
for i in range(N):
    listrise.append(1)
    listdown.append(1)
#上升子序列
for i in range(1,N):
    for j in range(i):
        if ss[i]>ss[j] and listrise[i]<listrise[j]+1:
            listrise[i]=listrise[j]+1
#下降子序列
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if ss[i]>ss[j] and listdown[i]<listdown[j]+1:
            listdown[i]=listdown[j]+1
for i in range(N):
    if listrise[i]+listdown[i]-1>max_len:
        max_len=listrise[i]+listdown[i]-1
print N-max_len
