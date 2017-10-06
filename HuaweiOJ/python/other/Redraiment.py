# -*- coding: cp936 -*-
'''
合唱队
'''
N=input()
s=[]
for i in range(N):
    s.append(input())
ss=[]
listrise=[]
max_len=0
for c in s:
    ss.append(int(c))
for i in range(N):
    listrise.append(1)
#上升子序列
for i in range(1,N):
    for j in range(i):
        if ss[i]>ss[j] and listrise[i]<listrise[j]+1:
            listrise[i]=listrise[j]+1

for i in range(N):
    if listrise[i]>max_len:
        max_len=listrise[i]
print max_len
