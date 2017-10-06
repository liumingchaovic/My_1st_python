# -*- coding: cp936 -*-
'''
求两个整数的最小公倍数
思路：两个数的最小公倍数=两数乘积/两数最大公约数
'''
'''最大公约数Greatest_Common_Divisor'''
def Greatest_Common_Divisor(inta,intb):
    temp=inta%intb
    if temp==0:
        return intb
    else:
        return Greatest_Common_Divisor(intb,temp)
'''最小公倍数Least_Common_Multiple'''
def Least_Common_Multiple(inta,intb):
    return inta*intb/Greatest_Common_Divisor(inta,intb)

inta=input()
intb=input()
print Least_Common_Multiple(inta,intb)
