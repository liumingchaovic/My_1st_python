# -*- coding: cp936 -*-
'''
�ϳ���
Nλͬѧվ��һ�ţ�������ʦҪ�����е�(N-K)λͬѧ���У�ʹ��ʣ�µ�Kλͬѧ������λ�þ����ųɺϳ����Ρ� 
�ϳ�������ָ������һ�ֶ��Σ���Kλͬѧ���������α��Ϊ1, 2, ��, K�����ǵ���߷ֱ�ΪT1, T2, ��, TK��
�����ǵ��������T1 < T2 < �� < Ti , Ti > Ti+1 > �� > TK (1 <= i <= K) �� 
��������ǣ���֪����Nλͬѧ����ߣ�����������Ҫ��λͬѧ���У�����ʹ��ʣ�µ�ͬѧ�ųɺϳ����Ρ�

���룺
��һ������ N����ʾͬѧ������ 
�ڶ����������飬�ո��������ʾ N λͬѧ���

�����
������Ҫ��λͬѧ����

�������룺
8
186 186 150 200 160 130 197 2001

���������
4
'''
N=input()
s=raw_input().split()
ss=[]
listrise=[]
listdown=[]
max_len=0
for c in s:
    ss.append(int(c))
for i in range(N):
    listrise.append(1)
    listdown.append(1)
#����������
for i in range(1,N):
    for j in range(i):
        if ss[i]>ss[j] and listrise[i]<listrise[j]+1:
            listrise[i]=listrise[j]+1
#�½�������
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if ss[i]>ss[j] and listdown[i]<listdown[j]+1:
            listdown[i]=listdown[j]+1
for i in range(N):
    if listrise[i]+listdown[i]-1>max_len:
        max_len=listrise[i]+listdown[i]-1
print N-max_len
