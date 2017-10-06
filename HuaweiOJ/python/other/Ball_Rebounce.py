# -*- coding: cp936 -*-
'''
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下,
求它在第5次落地时，共经历多少米?第5次反弹多高？
'''
height=input()
rebounce=0
sum_height=height
for i in range(5):
    rebounce=height/2.0
    height=rebounce
    if i==4:
        pass
    else:
        sum_height+=2*rebounce
print sum_height
print rebounce
