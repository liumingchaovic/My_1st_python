# -*- coding: cp936 -*-
'''
�Ȳ�����
����:�Ȳ����� 2��5��8��11��14��������
����:������N >0
���:��Ȳ�����ǰN���
����:ת���ɹ����� 0 ,�Ƿ��������쳣����-1
��͹�ʽsum=n*a1+n(n-1)d/2
'''
def Arithmetic_Progression(n,a1=2,d=3):
    if n<1:
        print -1
    else:
        Sum=n*a1+n*(n-1)*d/2
        print Sum
n=input()
Arithmetic_Progression(n)
