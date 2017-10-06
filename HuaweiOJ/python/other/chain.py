# -*- coding: cp936 -*-
'''
输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。
链表结点定义如下：

详细描述：
本题为考察链表的插入和删除知识。
链表的值不能重复
构造过程，例如
(箭头表示在之后插入)
1 -> 2//将数据1插入到2后
3 -> 2//3插到2后
5 -> 1
4 -> 5
7 -> 2
最后的链表的顺序为 2 7 3 1 5 4 
删除 结点 2 
则结果为 7 3 1 5 4

输入：
1输入链表的个数
2输入头节点的值
3按照格式插入各个节点
4输入要删除的节点的值
输出：
输出删除节点后的序列
'''
N=input()
s=[]
s.append(input())
ss=[]
for i in range(N-1):
    ss=raw_input().split()
    if s.index(int(ss[1]))==len(s)-1:
        s.append(int(ss[0]))
    else:
        s.insert(s.index(int(ss[1]))+1,int(ss[0]))
s.remove(input())
for i in range(len(s)):
    print s[i],
