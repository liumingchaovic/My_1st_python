# -*- coding: cp936 -*-
'''
输入一个单向链表，输出该链表中倒数第K个节点，链表的倒数第0个节点为链表的尾指针
正常返回倒数第K个节点指针，异常返回空指针
输入说明
1输入链表节点个数
2输入链表的值
3输入K的值
输出一个整数
'''
N=input()
s=raw_input().split()
K=input()
if K>=N:
    pass
else:
    print s[N-K-1]
