# -*- coding: cp936 -*-
'''
һ��DNA������A/C/G/T�ĸ���ĸ�����������ɡ�G��C�ı���������ΪGC-Ratio��
��������G��C������ĸ���ܵĳ��ִ��������ܵ���ĸ��Ŀ��Ҳ�������г��ȣ����ڻ��򹤳��У�
��������ǳ���Ҫ����Ϊ�ߵ�GC-Ratio�����ǻ������ʼ�㡣
����һ���ܳ���DNA���У��Լ�Ҫ�����С�����г��ȣ��о���Ա��������Ҫ�������ҳ�GC-Ratio��ߵ������С�

���룺����һ��string�ͻ������У���int���Ӵ��ĳ���
������ҳ�GC������ߵ��ִ�

ʾ�����룺AACTGTGCACGACCTGA
        5
ʾ�������GCACG
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
        
