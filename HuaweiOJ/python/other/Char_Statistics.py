# -*- coding: cp936 -*-
'''
字符统计
输入一个字符串，对字符中的各个英文字符，数字，空格进行统计，按照统计个数由多到少输出统计结果
如果统计的个数相同，则按ASCII码由小到大输出，如果有其他字符，则对这些字符不做处理（不输出）
'''
def Char_Statistics(s):
    ss=[]
    for c in s:
        if '0'<=c<='9' or 'a'<=c.lower()<='z' or c==' ':
            ss.append(c)
    d={}
    for c in ss:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    lst=[(d[w],w) for w in d]
    #这里排序如果相同则默认按ASCII排的
    lst.sort()
    #这里反向之后个数相同的排序就反了
    lst_index=[]
    for c in lst:
        lst_index.append(c[0])
    #按要求统计个数从大到小，相同的按ASCII升序
    lst_out=[]
    k=lst[-1][0]
    while len(lst_out)<len(lst):
        for i in range(lst_index.index(k),lst_index.index(k)+lst_index.count(k)):
            lst_out.append(lst[i])
        k=lst_index[lst_index.index(k)-1]
    sout=''
    for d in lst_out:
        sout+=d[1]
    print sout
s=raw_input()
Char_Statistics(s)
