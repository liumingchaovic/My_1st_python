# -*- coding: cp936 -*-
'''
��ȫ��
��ȫ����perfect number�����ֳ����������걸������һЩ�������Ȼ����
�����е������ӣ����������������Լ�����ĺͣ������Ӻ�������ǡ�õ���������
���磺28������Լ��1��2��4��7��14��28����ȥ������28�⣬����5�������1+2+4+7+14=28
����n����n��������ȫ���ĸ��������㷶Χ0<n<=500000
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
