# -*- coding: cp936 -*-
'''
�����ַ������ַ������г��ֵ�����ǰ����Ϸ��š�*���������ַ����ֲ���
ʾ�����룺
Jkdi234klowe90a3
ʾ�������
Jkdi*234*klowe*90*a*3*
'''
s=raw_input()
ss=''
i=0
while i<len(s):
    if '0'<=s[i]<='9':
        ss+='*'
        ss+=s[i]
        i+=1
        if i==len(s):
            ss+='*'
            break
        else:
            while i<len(s) and '0'<=s[i]<='9':
                ss+=s[i]
                i+=1
            ss+='*'
    else:
        ss+=s[i]
        i+=1
print ss
        
