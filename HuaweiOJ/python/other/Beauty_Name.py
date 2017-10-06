# -*- coding: cp936 -*-
'''
名字的漂亮度
对于每个名字来说，名字的漂亮度=26*字母个数最多的+25*字母个数其次的+。。。
输入整数N为N个姓名
输出相应的名字的漂亮度
示例输入：
2
zhangsan
lisi
示例输出：
192
101
'''
def Beauty_Name(s):
    d={}
    for c in s:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    lst=[(d[w],w) for w in d]
    lst.sort()
    lst.reverse()
    score=0
    for i in range(len(lst)):
        score+=(26-i)*lst[i][0]
    print score
N=input()
s=[]
for i in range(N):
    s.append(raw_input())
for i in range(N):
    Beauty_Name(s[i])
