# -*- coding: cp936 -*-
'''
24点算法
给出4个1-10的数字，通过，加减乘除，得到数字为24就算胜利
输入：
4个1-10的数字【数字允许重复】
输出：
true or false

【高级版】
计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，本问题中，扑克牌通过如下字符或者字符串表示，其中，小写joker表示小王，大写JOKER表示大王： 

                   3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER

本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。 

详细说明： 

1.运算只考虑加减乘除运算，没有阶乘等特殊运算符号，友情提醒，整数除法要当心； 
2.牌面2~10对应的权值为2~10, J、Q、K、A权值分别为为11、12、13、1； 
3.输入4张牌为字符串形式，以一个空格隔开，首尾无空格；如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算； 
4.输出的算式格式为4张牌通过+-*/四个运算符相连，中间无空格，4张牌出现顺序任意，只要结果正确； 
5.输出算式的运算顺序从左至右，不包含括号，如1+2+3*4的结果为24
6.如果存在多种算式都能计算得出24，只需输出一种即可，如果无法得出24，则输出“NONE”表示无解。
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
华为OJ答案
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
