# -*- coding: cp936 -*-
'''
���A�Ǹ�x��y�еľ���B�Ǹ�y��z�еľ��󣬰�A��B��ˣ�����������һ��x��z�еľ���C
����˵����
1����һ�����������
2����һ������������͵ڶ������������
3���ڶ������������
4����һ�������ֵ
5���ڶ��������ֵ
�������������˵Ľ��
ʾ�����룺
2
2
2
3 8
8 0
9 0
18 9
ʾ�������
171 72
72 0
'''
def MatrixMul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += int(A[i][k]) * int(B[k][j])
    return res
x=input()
y=input()
z=input()
A=[]
B=[]
for i in range(x):
    s=raw_input()
    A.append(s.split())
for j in range(y):
    t=raw_input()
    B.append(t.split())
res=MatrixMul(A,B)
for i in range(len(res)):
    for j in range(len(res[i])):
        print res[i][j],
    print
