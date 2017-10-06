# -*- coding: cp936 -*-
'''
将两个整型数组按照升序合并，并且过滤掉重复数组元素
输入说明，按下列顺序输入：
1 输入第一个数组的个数
2 输入第一个数组的数值
3 输入第二个数组的个数
4 输入第二个数组的数值

输出合并之后的数组
3
1 2 5
4
-1 0 3 2
-101235
'''
def Int_Union(int1,int2):
    int_Union=list(set(int1) | set(int2))
    int_Union.sort()
    cout=''
    for c in int_Union:
        cout+=str(c)
    print cout
    
Num1=input()
s1=raw_input().split()
int1=[]
for i in range(Num1):
    int1.append(int(s1[i]))

Num2=input()
s2=raw_input().split()
int2=[]
for i in range(Num2):
    int2.append(int(s2[i]))

Int_Union(int1,int2)
