# -*- coding: cp936 -*-
'''
求一个int型数据在内存中存储的1的个数
这里需要考虑的情况是负数，负数用补码表示，需要区别对待
其解法可以用原数与num=1(num<<1)进行按位与，然后count统计1的个数
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
