# -*- coding: cp936 -*-
'''
��������������С������
˼·������������С������=�����˻�/�������Լ��
'''
'''���Լ��Greatest_Common_Divisor'''
def Greatest_Common_Divisor(inta,intb):
    temp=inta%intb
    if temp==0:
        return intb
    else:
        return Greatest_Common_Divisor(intb,temp)
'''��С������Least_Common_Multiple'''
def Least_Common_Multiple(inta,intb):
    return inta*intb/Greatest_Common_Divisor(inta,intb)

inta=input()
intb=input()
print Least_Common_Multiple(inta,intb)
