# -*- coding: cp936 -*-
'''
请编写一个函数（允许增加子函数），计算n x m的棋盘格子（n为横向的格子数，m为竖向的格子数）
沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，
不能往左和往上走。

示例输入：
2
2
示例输出：
6
'''
def count(m,n):
    if (m==1 and n==0) or (m==0 and n==1):
        return 1
    if m>0 and n>0:
        return count(m-1,n)+count(m,n-1)
    if m==0:
        return count(m,n-1)
    if n==0:
        return count(m-1,n)
    return 0

m=input()
n=input()
print count(m,n)
