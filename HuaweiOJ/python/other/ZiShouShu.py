# -*- coding: cp936 -*-
'''
��������ָһ������ƽ����β�����ڸ����������Ȼ����
���磺25^2 = 625��76^2 = 5776��9376^2 = 87909376�������n���ڵ��������ĸ���

'''
def ZiShouShu(n):
    count=0
    for i in range(n):
        if i*i%(pow(10,len(str(i))))==i:
            count+=1
    print count
n=input()
ZiShouShu(n)
