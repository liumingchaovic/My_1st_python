# -*- coding: cp936 -*-
'''
�������������鰴������ϲ������ҹ��˵��ظ�����Ԫ��
����˵����������˳�����룺
1 �����һ������ĸ���
2 �����һ���������ֵ
3 ����ڶ�������ĸ���
4 ����ڶ����������ֵ

����ϲ�֮�������
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
