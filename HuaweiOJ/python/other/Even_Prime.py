# -*- coding: cp936 -*-
'''
����һ��ż��������2����������2��������ɣ����ż����2�������кܶ��������
����ĿҪ��������ָ��ż��������������ֵ��С��������

ʾ�����룺20
ʾ�������7 13
'''
from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def Even_Prime(m):
    if m<=5 or m>10000 or m%2!=0:
        return 0
    Least_D=m
    Prime1=0
    for i in range(5,m/2):
        if isPrime(i) and isPrime(m-i):
            Difference=m-2*i
            if Difference<Least_D:
                Least_D=Difference
                Prime1=i
    print Prime1
    print m-Prime1

m=input()
Even_Prime(m)
