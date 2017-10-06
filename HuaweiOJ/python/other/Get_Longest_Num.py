# -*- coding: cp936 -*-
'''
输入一个字符串。

输出字符串中最长的数字字符串和它的长度。

如果数字字符串为空，则只输出0

如 input: dadfsaf  output:0

abcd12345ed125ss123058789
123058789,9

'''
def Get_Longest_Num(s):
    maxlen=0
    index_first=0
    max_len_index=0
    for i in range(len(s)):
        if '0'<=s[i]<='9':
            count=1
            index_first=i
            while i+1<len(s) and '0'<=s[i+1]<='9':
                count+=1
                i+=1
            if count>maxlen:
                maxlen=count
                max_len_index=index_first
    if maxlen!=0:
        print s[max_len_index:max_len_index+maxlen]+','+str(maxlen)
    else:
        print 0
    
s=raw_input()
Get_Longest_Num(s)
