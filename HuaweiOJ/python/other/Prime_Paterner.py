# -*- coding: cp936 -*-
'''
��������
�������������ĺ�Ϊ����������������������֮Ϊ���������¡�����2��5��6��13��
������Ӧ����ͨ�ż��ܡ���������ѧ���������һ�����򣬴����е�N��NΪż��������������
��ѡ�����ɶ���ɡ��������¡�����ѡ�������ֶ�����������4����������2��5��6��13��
�����5��6��Ϊһ����ֻ�ܵõ�һ�顰�������¡�������2��5��6��13���齫�õ����顰�������¡���
����ɡ��������¡����ķ�����Ϊ����ѷ���������Ȼ����ѧ��ϣ����Ѱ�ҳ�����ѷ�������

����:
��һ����ż��N��N��100������ʾ����ѡ����Ȼ���ĸ��������������������֣���ΧΪ[2,30000]��

���:
���һ������K����ʾ����õġ���ѷ�������ɡ��������¡��Ķ�����

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
    
