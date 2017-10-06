# -*- coding: cp936 -*-
'''
输入整型数组和排序标识，对其元素按照升序或降序进行排序
输入：
1、输入需要输入的整型数个数
2、输入数组组
3、输入排序标识
输出：
输出排好序的数字
最后一个无空格
如下例子

示例输入：
8
1 2 4 9 3 55 64 25
0
示例输出：
1 2 3 4 9 25 55 64
'''
def Int_Sort(s,num):
    if num==0:
        s.sort()
        for i in range(len(s)):
            print s[i],
    if num==1:
        s.sort()
        s=s[::-1]
        for i in range(len(s)):
            print s[i],

Int_Num=input()
s=raw_input().split()
ss=[]
for i in range(len(s)):
    ss.append(int(s[i]))
Flag=input()
Int_Sort(ss,Flag)
    
