# -*- coding: cp936 -*-
'''
������������������ʶ������Ԫ�ذ�����������������
���룺
1��������Ҫ���������������
2������������
3�����������ʶ
�����
����ź��������
���һ���޿ո�
��������

ʾ�����룺
8
1 2 4 9 3 55 64 25
0
ʾ�������
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
    
