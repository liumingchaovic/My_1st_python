# -*- coding: cp936 -*-
'''
Ѱ�ҵȲ�����
�ڸ��������䷶Χ���ҳ����������ܹ��ɵ����ĵȲ����У����Ȳ����а���������������ࣩ��
����������Ǹ�����ͬ������£������������Ǹ�����������
�м�������Ǹ�����ͬ������£��������������С������

������[0, 10]�У��������ɵ����Ȳ�����Ϊ3,5,7
'''
'''
#����
from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def Arithmetic_Progression_for_Prime(m,n):
    Prime=[]
    #������
    for i in range(m,n+1):
        if isPrime(i):
            Prime.append(i)
    #�湫��
    #print Prime
    d=[]
    for i in range(len(Prime)):
        for j in range(i+1,len(Prime)):
            d.append(Prime[j]-Prime[i])
    #���ظ��Ĺ���
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
                    #tmp_last����ȡ���һ������ֵ���бȽ�
                    tmp_last=Prime[i]+(max_len-1)*diff_max_len
                else:
                    #�����������ǲ�ֵû�и��£�������Ҫÿ�ν���ʱ���²�ֵ
                    Prime_last=Prime[i]+(max_len-1)*new_diff_max_len
                    if Prime_last>tmp_last:
                        #��Ҫ��Prime_last��ֵ��tmp_last����Ȼÿ�ν��������ʼmax_len���µ�tmp_last
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
#�м�
from math import sqrt
def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def Arithmetic_Progression_for_Prime(m,n):
    Prime=[]
    #������
    if m<=1:
        m=2
    for i in range(m,n+1):
        if isPrime(i):
            Prime.append(i)
    #�湫��
    #print Prime
    d=[]
    for i in range(len(Prime)):
        for j in range(i+1,len(Prime)):
            d.append(Prime[j]-Prime[i])
    #���ظ��Ĺ���
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
                    #tmp_last����ȡ���һ������ֵ���бȽ�
                    tmp_first=Prime[i]
                else:
                    #�����������ǲ�ֵû�и��£�������Ҫÿ�ν���ʱ���²�ֵ
                    Prime_first=Prime[i]
                    if Prime_first<tmp_first:
                        #��Ҫ��Prime_last��ֵ��tmp_last����Ȼÿ�ν��������ʼmax_len���µ�tmp_last
                        tmp_first=Prime_first
                        max_len=count
                        index_max_len=i
                        diff_max_len=new_diff_max_len
    #print max_len,index_max_len,diff_max_len
    for i in range(max_len):
        print Prime[index_max_len]+i*diff_max_len,
s=raw_input().split()
Arithmetic_Progression_for_Prime(int(s[0]),int(s[1]))
