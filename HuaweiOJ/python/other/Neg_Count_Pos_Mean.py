# -*- coding: cp936 -*-
'''
�Ǹ�����
��������Ҫ�������������n��Ȼ������n�����������Ϊn�������и����ĸ�������������������ƽ��ֵ��
ע�⣺������������Ͳ��ñ���һλС��
ʾ�����룺
5
1
2
3
4
5
ʾ�������
0 3
'''
def Neg_Count_Pos_Mean(N,s):
    count=0
    Sum=0
    for c in s:
        if c<0:
            count+=1
        else:
            Sum+=c
    print count,
    if Sum%(len(s)-count)==0:
        print Sum/(len(s)-count)
    else:
        print '%.1f' %(float(Sum)/(len(s)-count))
N=input()
ss=[]
for c in range(N):
    ss.append(input())
Neg_Count_Pos_Mean(N,ss)
