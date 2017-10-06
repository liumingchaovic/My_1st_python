# -*- coding: cp936 -*-
'''
记负均正
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值。
注意：如果可以整除就不用保留一位小数
示例输入：
5
1
2
3
4
5
示例输出：
0 3
'''
def Neg_Count_Pos_Mean(N,s):
    count=0
    Sum=0
    for c in s:
        if c<0:
            count+=1
        else:
            Sum+=c
    print count,
    if Sum%(len(s)-count)==0:
        print Sum/(len(s)-count)
    else:
        print '%.1f' %(float(Sum)/(len(s)-count))
N=input()
ss=[]
for c in range(N):
    ss.append(input())
Neg_Count_Pos_Mean(N,ss)
