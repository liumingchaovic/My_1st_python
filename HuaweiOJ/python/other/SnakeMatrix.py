# -*- coding: utf-8 -*-
'''
题目说明
蛇形矩阵是由1开始的自然依次排列成的一个矩阵上三角形
样例输入
5
样例输出
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
输入：正整数N（N不大于100）
输出：N行的蛇形矩阵
'''
N=input()
p=1
s=[]
#初始化一个N*N的0矩阵
s=[[0]*N for i in range(N)]
for i in range(N):
    j=i
    k=0
    #模拟for(j=i,k=0;j>=0,k<=i;j--,k++)
    while(j>=0 and k<=i):
        s[j][k]=p
        p+=1
        j-=1
        k+=1
#print s
for i in range(N):
    for j in range(N-i):
        print s[i][j],
    print
