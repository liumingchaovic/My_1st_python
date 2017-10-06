# -*- coding: cp936 -*-
'''
删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除，输出删除这些字符后的字符串，
字符串中其它字符保持原来的顺序
有几种特例需要注意
1，全字符串只有一种字符
2，多个字符具有相同的个数
字符肯定是从1算起的，因此可以不断查找等于i++的字符并删除
'''
def Del_Least_appeal_Char(s):
    s=list(s)
    d={}
    #字典的好处就是可以存键值对
    for c in s:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    #print d
    lst=[(d[w],w) for w in d]
    lst.sort()
    k=lst[0][0]
    for i in range(len(lst)):
        if lst[i][0]==k:
            for j in range(k):
                s.remove(lst[i][1])
        else:
            break
    print ''.join(s)
s=raw_input()
Del_Least_appeal_Char(s)
