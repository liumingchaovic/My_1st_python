# -*- coding: cp936 -*-
'''
��һ��int���������ڴ��д洢��1�ĸ���
������Ҫ���ǵ�����Ǹ����������ò����ʾ����Ҫ����Դ�
��ⷨ������ԭ����num=1(num<<1)���а�λ�룬Ȼ��countͳ��1�ĸ���
'''
n=int(raw_input())
n=(n & 0x55555555)+((n>>1) & 0x55555555)
n=(n & 0x33333333)+((n>>2) & 0x33333333)
n=(n & 0x0f0f0f0f)+((n>>4) & 0x0f0f0f0f)
n=(n & 0x00ff00ff)+((n>>8) & 0x00ff00ff)
n=(n & 0x0000ffff)+((n>>16) & 0x0000ffff)
print n
'''
if i>0:
    b=bin(i)
    print b.count('1')
elif i<0:
    i=~i+1
    b=bin(1)
    print b.count('1')
else:
    pass
'''
