# -*- coding: cp936 -*-
'''
��������
����һ�������������մ�С�����˳�����������������������
����180����������Ϊ2 2 3 3 5
�˴���ο���ˮ����
https://code.csdn.net/snippets/436936/master/snippet_file_0.txt/raw
�Ҿ����ǽ��������������࣬����صĴ��룬û�о������⴦��ȴ��֤iΪ����
'''
def Prime(N):
    for i in range(2,N+1):
        while(N%i==0 and N!=0):
            print i,
            N=N/i
N=input()
Prime(N)
