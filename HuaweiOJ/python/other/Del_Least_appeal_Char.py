# -*- coding: cp936 -*-
'''
ɾ���ַ����г��ִ������ٵ��ַ���������ַ����ִ���һ������ɾ�������ɾ����Щ�ַ�����ַ�����
�ַ����������ַ�����ԭ����˳��
�м���������Ҫע��
1��ȫ�ַ���ֻ��һ���ַ�
2������ַ�������ͬ�ĸ���
�ַ��϶��Ǵ�1����ģ���˿��Բ��ϲ��ҵ���i++���ַ���ɾ��
'''
def Del_Least_appeal_Char(s):
    s=list(s)
    d={}
    #�ֵ�ĺô����ǿ��Դ��ֵ��
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
