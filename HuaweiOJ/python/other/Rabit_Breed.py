# -*- coding: cp936 -*-
'''
��һ�����ӣ��ӳ������3������ÿ���¶���һ�����ӣ�С���ӳ����������º�ÿ��������һ�����ӣ�
�������Ӷ���������ÿ���µ���������Ϊ���٣�

'''
def Rabit_Breed(month):
    if month==1 or month==2:
        return 1
    else:
        return Rabit_Breed(month-1)+Rabit_Breed(month-2)
month=input()
print Rabit_Breed(month)
