# -*- coding: cp936 -*-
'''
自守数是指一个数的平方的尾数等于该数自身的自然数。
例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n以内的自守数的个数

'''
def ZiShouShu(n):
    count=0
    for i in range(n):
        if i*i%(pow(10,len(str(i))))==i:
            count+=1
    print count
n=input()
ZiShouShu(n)
