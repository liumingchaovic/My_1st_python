# -*- coding: cp936 -*-
'''
����IPV4����һ��32λ�޷�����������ʾ��һ���õ�ַ�ʽ����ʾ���㽫IP��ַ�ֳ�4�����֣�
ÿ������Ϊ8λ����ʾ��һ���޷�����������˲���Ҫ�����ų��֣�����10.137.17.1��
�����Ƿǳ���Ϥ��IP��ַ��һ��IP��ַ����û�пո���֣���ΪҪ��ʾ��һ��32���֣���
������Ҫ���ó������ж�IP�Ƿ�Ϸ���
���룺һ��IP��ַ
�����YES or NO
�������룺10.138.15.1
���������YES
'''
import os,sys 
def check_ip(ipaddr): 
        import sys 
        addr=ipaddr.strip().split('.')  #�и�IP��ַΪһ���б� 
        #print addr 
        if len(addr) != 4:  #�и���б������4������ 
                print "NO"
                sys.exit() 
        for i in range(4): 
                try: 
                        addr[i]=int(addr[i])  #ÿ����������Ϊ���֣�����У��ʧ�� 
                except: 
                        print "NO"
                        sys.exit() 
                if addr[i]<=255 and addr[i]>=0:    #ÿ������ֵ������0-255֮�� 
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
if  len(sys.argv)!=2:  #���μӱ����ȱ���Ϊ2 
        print "Example: %s 10.0.0.1 "%sys.argv[0] 
        sys.exit() 
else: 
        check_ip(sys.argv[1])  #������������У��IP����
'''
