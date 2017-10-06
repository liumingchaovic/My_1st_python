# -*- coding: cp936 -*-
'''
一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）
是序列中G和C两个字母的总的出现次数除以总的字母数目（也就是序列长度）。在基因工程中，
这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。

输入：输入一个string型基因序列，和int型子串的长度
输出：找出GC比例最高的字串

示例输入：AACTGTGCACGACCTGA
        5
示例输出：GCACG
'''

def DNA_GC_Ratio(ss,Num):
    #index_first=0
    max_count=0
    max_index=0
    count=0
    for i in range(len(ss)):
        count=0
        for j in range(Num):
            if (i+Num<len(ss)-1 and ((ss[i+j].upper()=='C') or (ss[i+j].upper()=='G'))):
                count+=1
                j+=1
        if count>max_count:
            max_count=count
            max_index=i
    print max_count
    print ss[max_index:max_index+Num]

ss=raw_input()
Num=input()
DNA_GC_Ratio(ss,Num)
        
