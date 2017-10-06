# -*- coding: cp936 -*-
'''
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，
然后把这个二进制数转变成一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，
即该IP地址转换后的数字就是它了。
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
