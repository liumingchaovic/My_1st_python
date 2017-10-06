# -*- coding: cp936 -*-
'''
寻找等差数列
在给定的区间范围内找出所有素数能构成的最大的等差数列（即等差数列包含的素数个数最多）。
初级：如果是个数相同的情况下，输出数列最后那个数最大的数列
中级：如果是个数相同的情况下，输出数列首项最小的数列

在区间[0, 10]中，素数构成的最大等差数列为3,5,7
'''
'''
#初级
from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def Arithmetic_Progression_for_Prime(m,n):
    Prime=[]
    #存素数
    for i in range(m,n+1):
        if isPrime(i):
            Prime.append(i)
    #存公差
    #print Prime
    d=[]
    for i in range(len(Prime)):
        for j in range(i+1,len(Prime)):
            d.append(Prime[j]-Prime[i])
    #不重复的公差
    d=set(d)
    d=list(d)
    d.sort()
    #print d
    max_len=1
    index_max_len=0
    diff_max_len=0
    Prime_last=0
    tmp_last=0
    for i in range(len(Prime)):
        for j in range(len(d)):
            tmp=d[j]
            count=1
            while((Prime[i]+tmp) in Prime):
                count+=1
                tmp+=d[j]
            if count>=max_len:
                new_diff_max_len=d[j]
                if count>max_len:
                    max_len=count
                    index_max_len=i
                    diff_max_len=new_diff_max_len
                    #tmp_last用于取最后一个数的值进行比较
                    tmp_last=Prime[i]+(max_len-1)*diff_max_len
                else:
                    #这里的问题就是差值没有更新，所以需要每次进来时更新差值
                    Prime_last=Prime[i]+(max_len-1)*new_diff_max_len
                    if Prime_last>tmp_last:
                        #需要将Prime_last赋值给tmp_last，不然每次进来都是最开始max_len更新的tmp_last
                        tmp_last=Prime_last
                        max_len=count
                        index_max_len=i
                        diff_max_len=new_diff_max_len
    #print max_len,index_max_len,diff_max_len
    for i in range(max_len):
        print Prime[index_max_len]+i*diff_max_len
m=input()
n=input()
Arithmetic_Progression_for_Prime(m,n)
'''
#中级
from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def Arithmetic_Progression_for_Prime(m,n):
    Prime=[]
    #存素数
    if m<=1:
        m=2
    for i in range(m,n+1):
        if isPrime(i):
            Prime.append(i)
    #存公差
    #print Prime
    d=[]
    for i in range(len(Prime)):
        for j in range(i+1,len(Prime)):
            d.append(Prime[j]-Prime[i])
    #不重复的公差
    d=set(d)
    d=list(d)
    d.sort()
    #print d
    max_len=1
    index_max_len=0
    diff_max_len=0
    Prime_first=0
    tmp_first=0
    for i in range(len(Prime)):
        for j in range(len(d)):
            tmp=d[j]
            count=1
            while((Prime[i]+tmp) in Prime):
                count+=1
                tmp+=d[j]
            if count>=max_len:
                new_diff_max_len=d[j]
                if count>max_len:
                    max_len=count
                    index_max_len=i
                    diff_max_len=new_diff_max_len
                    #tmp_last用于取最后一个数的值进行比较
                    tmp_first=Prime[i]
                else:
                    #这里的问题就是差值没有更新，所以需要每次进来时更新差值
                    Prime_first=Prime[i]
                    if Prime_first<tmp_first:
                        #需要将Prime_last赋值给tmp_last，不然每次进来都是最开始max_len更新的tmp_last
                        tmp_first=Prime_first
                        max_len=count
                        index_max_len=i
                        diff_max_len=new_diff_max_len
    #print max_len,index_max_len,diff_max_len
    for i in range(max_len):
        print Prime[index_max_len]+i*diff_max_len,
s=raw_input().split()
Arithmetic_Progression_for_Prime(int(s[0]),int(s[1]))
