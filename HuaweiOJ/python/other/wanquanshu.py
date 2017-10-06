# -*- coding: cp936 -*-
'''
完全数
完全数（perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1，2，4，7，14，28，除去它本身28外，其余5个数相加1+2+4+7+14=28
计算n（含n）以内完全数的个数，计算范围0<n<=500000
'''
def IsWQS(N):
    Sum=0
    for i in range(1,N):
        if N%i==0:
            Sum+=i
    if Sum==N:
        return True
    else:
        return False
def CountWQS(N):
    count=0
    for i in range(2,N):
        if IsWQS(i):
            count+=1
    print count
N=input()
CountWQS(N)
