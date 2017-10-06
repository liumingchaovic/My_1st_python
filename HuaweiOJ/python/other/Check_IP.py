# -*- coding: cp936 -*-
'''
现在IPV4下用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，
每个部分为8位，表示成一个无符号整数（因此不需要用正号出现），如10.137.17.1，
是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
现在需要你用程序来判断IP是否合法。
输入：一个IP地址
输出：YES or NO
样例输入：10.138.15.1
样例输出：YES
'''
import os,sys 
def check_ip(ipaddr): 
        import sys 
        addr=ipaddr.strip().split('.')  #切割IP地址为一个列表 
        #print addr 
        if len(addr) != 4:  #切割后列表必须有4个参数 
                print "NO"
                sys.exit() 
        for i in range(4): 
                try: 
                        addr[i]=int(addr[i])  #每个参数必须为数字，否则校验失败 
                except: 
                        print "NO"
                        sys.exit() 
                if addr[i]<=255 and addr[i]>=0:    #每个参数值必须在0-255之间 
                        pass
                else: 
                        print "NO"
                        sys.exit() 
                i+=1
        else: 
                print "YES"
ipaddr=raw_input()
check_ip(ipaddr)
'''
if  len(sys.argv)!=2:  #传参加本身长度必须为2 
        print "Example: %s 10.0.0.1 "%sys.argv[0] 
        sys.exit() 
else: 
        check_ip(sys.argv[1])  #满足条件调用校验IP函数
'''
