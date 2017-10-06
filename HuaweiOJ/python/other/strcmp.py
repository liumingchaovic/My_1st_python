# -*- coding: cp936 -*-
'''
Levenshtein ���룬�ֳƱ༭���룬ָ���������ַ���֮�䣬��һ��ת������һ����������ٱ༭����������
��ɵı༭����������һ���ַ��滻����һ���ַ�������һ���ַ���ɾ��һ���ַ���
�༭������㷨�������ɶ����ѧ��Levenshtein����ģ����ֽ�Levenshtein Distance��

Ex��

�ַ���A:abcdefg
�ַ���B: abcdef

ͨ�����ӻ���ɾ���ַ���g���ķ�ʽ�ﵽĿ�ġ������ַ�������Ҫһ�β�����
�������������Ҫ�Ĵ�������Ϊ�����ַ����ľ��롣

Ҫ��
�������������ַ�����д��һ���㷨�������ǵı༭���롣

'''
def strcmp(s, t):
    if len(s) > len(t):
        s, t = t, s
    #��һ��
    n = len(s)
    m = len(t)
 
    if not m : return n
    if not n : return m
     
    #�ڶ���
    v0 = [ i for i in range(0, m+1) ]
    v1 = [ 0 ] * (m+1) 
 
    #������
    cost = 0
    for i in range(1, n+1):
        v1[0] = i
        for j in range(1, m+1):
            #���Ĳ�,�岽
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1
 
            #������
            a = v0[j] + 1
            b = v1[j-1] + 1
            c = v0[j-1] + cost
            v1[j] = min(a, b, c)
        v0 = v1[:]
    #���߲�
    return v1[m]
s=raw_input()
t=raw_input()
print strcmp(s,t)
'''
�������ڼ����ַ������ƶ�
ss=''
ss+='1'
ss+='/'
ss+=str(int(strcmp(s,t))+1)
print ss
'''
