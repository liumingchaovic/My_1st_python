# -*- coding: cp936 -*-
'''
素数伴侣
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，
它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的N（N为偶数）个正整数中
挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，
如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，
能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。

输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。

'''
from math import sqrt
import itertools
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True      

def Prime_Paterner(x,y):
    if isPrime(x+y):
        return True
    else:
        return False

N=input()
max=0
s=[]
#if (N%2!=0 or N>100):
#    return -1
a=raw_input().split()
for i in range(N):
    s.append(int(a[i]))
s.sort()
ss=[]
for i in itertools.permutations(s,N):
    ss.append(i)
for c in ss:
    k=0
    for i in range(0,N,2):
        if Prime_Paterner(c[i],c[i+1]):
            k+=1
    if k>max:
        max=k
print max
    
