# -*- coding: cp936 -*-
'''
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。
许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。
编辑距离的算法是首先由俄国科学家Levenshtein提出的，故又叫Levenshtein Distance。

Ex：

字符串A:abcdefg
字符串B: abcdef

通过增加或是删掉字符”g”的方式达到目的。这两种方案都需要一次操作。
把这个操作所需要的次数定义为两个字符串的距离。

要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。

'''
def strcmp(s, t):
    if len(s) > len(t):
        s, t = t, s
    #第一步
    n = len(s)
    m = len(t)
 
    if not m : return n
    if not n : return m
     
    #第二步
    v0 = [ i for i in range(0, m+1) ]
    v1 = [ 0 ] * (m+1) 
 
    #第三步
    cost = 0
    for i in range(1, n+1):
        v1[0] = i
        for j in range(1, m+1):
            #第四步,五步
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1
 
            #第六步
            a = v0[j] + 1
            b = v1[j-1] + 1
            c = v0[j-1] + cost
            v1[j] = min(a, b, c)
        v0 = v1[:]
    #第七步
    return v1[m]
s=raw_input()
t=raw_input()
print strcmp(s,t)
'''
下面用于计算字符串相似度
ss=''
ss+='1'
ss+='/'
ss+=str(int(strcmp(s,t))+1)
print ss
'''
