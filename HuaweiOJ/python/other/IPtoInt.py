# -*- coding: cp936 -*-
'''
ԭ��ip��ַ��ÿ�ο��Կ�����һ��0-255����������ÿ�β�ֳ�һ����������ʽ���������
Ȼ��������������ת���һ����������
������һ��ip��ַΪ10.0.3.193
ÿ������             ���Ӧ�Ķ�������
10                   00001010
0                    00000000
3                    00000011
193                  11000001
���������Ϊ��00001010 00000000 00000011 11000001,ת��Ϊ10���������ǣ�167773121��
����IP��ַת��������־������ˡ�
'''
def IPtoInt(IP):
    IP=IP.strip().split('.')
    s=''
    for c in IP:
        temp=''
        temp_s=bin(int(c))[2:]
        for i in range(8-len(temp_s)):
            temp+='0'
        s+=temp+temp_s
    print int(s,2)
def InttoIP(d):
    if 0<=d<=4294967295:
        binary=bin(d)[2:]
        b_len=32-len(binary)
        zero=''
        while(b_len>0):
            zero+='0'
            b_len-=1
        binary_full=zero+binary
        IP=''
        for i in range(0,len(binary_full),8):
            temp_str=binary_full[i:i+8]
            IP+=str(int(temp_str,2))+'.'
        print IP[:-1]
IP=raw_input()
d=input()
IPtoInt(IP)
InttoIP(d)
