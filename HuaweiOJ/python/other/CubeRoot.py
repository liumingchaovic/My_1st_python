# -*- coding: cp936 -*-
'''
���һ�����������������������ú���
'''
def CubeRoot(N):
    E=0.01
    x0=N
    result=x0-float(x0*x0*x0-N)/(3*x0*x0)
    while not -E<result*result*result-N<E:
        x0=result
        result=x0-float(x0*x0*x0-N)/(3*x0*x0)
    print '%.1f' % result
N=input()
CubeRoot(N)
