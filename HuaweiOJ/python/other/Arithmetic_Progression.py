# -*- coding: cp936 -*-
'''
等差数列
功能:等差数列 2，5，8，11，14。。。。
输入:正整数N >0
输出:求等差数列前N项和
返回:转换成功返回 0 ,非法输入与异常返回-1
求和公式sum=n*a1+n(n-1)d/2
'''
def Arithmetic_Progression(n,a1=2,d=3):
    if n<1:
        print -1
    else:
        Sum=n*a1+n*(n-1)*d/2
        print Sum
n=input()
Arithmetic_Progression(n)
