# -*- coding: cp936 -*-
'''
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C
输入说明：
1、第一个矩阵的行数
2、第一个矩阵的列数和第二个矩阵的行数
3、第二个矩阵的列数
4、第一个矩阵的值
5、第二个矩阵的值
输出两个矩阵相乘的结果
示例输入：
2
2
2
3 8
8 0
9 0
18 9
示例输出：
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
