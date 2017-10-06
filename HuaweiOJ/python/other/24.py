# -*- coding: cp936 -*-
'''
24���㷨
����4��1-10�����֣�ͨ�����Ӽ��˳����õ�����Ϊ24����ʤ��
���룺
4��1-10�����֡����������ظ���
�����
true or false

���߼��桿
����24����һ���˿���������Ϸ��������4���˿��ƣ�ͨ����(+)����(-)����(*), ��(/)�������㷨�����õ�����24���������У��˿���ͨ�������ַ������ַ�����ʾ�����У�Сдjoker��ʾС������дJOKER��ʾ������ 

                   3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER

������Ҫ��ʵ�֣�����4���ƣ����һ����ʽ����ʽ�Ľ��Ϊ24�㡣 

��ϸ˵���� 

1.����ֻ���ǼӼ��˳����㣬û�н׳˵�����������ţ��������ѣ���������Ҫ���ģ� 
2.����2~10��Ӧ��ȨֵΪ2~10, J��Q��K��AȨֵ�ֱ�ΪΪ11��12��13��1�� 
3.����4����Ϊ�ַ�����ʽ����һ���ո��������β�޿ո���������4�����а�����С����������ַ�����ERROR������ʾ�޷����㣻 
4.�������ʽ��ʽΪ4����ͨ��+-*/�ĸ�������������м��޿ո�4���Ƴ���˳�����⣬ֻҪ�����ȷ�� 
5.�����ʽ������˳��������ң����������ţ���1+2+3*4�Ľ��Ϊ24
6.������ڶ�����ʽ���ܼ���ó�24��ֻ�����һ�ּ��ɣ�����޷��ó�24���������NONE����ʾ�޽⡣
'''
from __future__ import division
import itertools as it

fmtList=["((%d%s%d)%s%d)%s%d","(%d%s%d)%s(%d%s%d)","(%d%s(%d%s%d))%s%d",
         "%d%s((%d%s%d)%s%d)","%d%s(%d%s(%d%s%d))"]
opList=it.product(['+','-','*','/'],repeat=3)

def ok(fmt,nums,ops):
    a,b,c,d=nums
    op1,op2,op3=ops
    expr=fmt%(a,op1,b,op2,c,op3,d)
    try:
        res=eval(expr)
    except ZeroDivisionError:
        return
    if 23.999<res<24.001:
        print expr,'=24'
def calc24(numlist):
    [[ok(fmt,numlist,op) for fmt in fmtList] for op in opList]
calc24([10,11,12,13])

for i in set(it.permutations([3,3,8,8])):
    calc24(i)

'''
��ΪOJ��
from __future__ import division
import itertools as it
import sys
fmtList=["((%d%s%d)%s%d)%s%d","(%d%s%d)%s(%d%s%d)","(%d%s(%d%s%d))%s%d",
         "%d%s((%d%s%d)%s%d)","%d%s(%d%s(%d%s%d))"]
opList=it.product(['+','-','*','/'],repeat=3)

def ok(fmt,nums,ops):
    a,b,c,d=nums
    op1,op2,op3=ops
    expr=fmt%(a,op1,b,op2,c,op3,d)
    Flag=0
    try:
        res=eval(expr)
    except ZeroDivisionError:
        return
    if 23.999<res<24.001:
        Flag=1
    else:
        pass
    return Flag
s=raw_input().split()
numlist=[]
for c in s:
    numlist.append(int(c))
Flag=0
for fmt in fmtList:
    for op in opList:
        if ok(fmt,numlist,op):
            Flag=1
            sys.exit
if Flag:
    print 'true'
else:
    print 'false'
'''
