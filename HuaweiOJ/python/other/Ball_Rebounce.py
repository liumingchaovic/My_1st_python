# -*- coding: cp936 -*-
'''
����һ���������߶��������£�ÿ����غ�����ԭ�߶ȵ�һ��; ������,
�����ڵ�5�����ʱ��������������?��5�η�����ߣ�
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
