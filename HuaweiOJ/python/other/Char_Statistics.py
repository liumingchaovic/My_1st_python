# -*- coding: cp936 -*-
'''
�ַ�ͳ��
����һ���ַ��������ַ��еĸ���Ӣ���ַ������֣��ո����ͳ�ƣ�����ͳ�Ƹ����ɶൽ�����ͳ�ƽ��
���ͳ�Ƶĸ�����ͬ����ASCII����С�������������������ַ��������Щ�ַ����������������
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
    #�������������ͬ��Ĭ�ϰ�ASCII�ŵ�
    lst.sort()
    #���ﷴ��֮�������ͬ������ͷ���
    lst_index=[]
    for c in lst:
        lst_index.append(c[0])
    #��Ҫ��ͳ�Ƹ����Ӵ�С����ͬ�İ�ASCII����
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
