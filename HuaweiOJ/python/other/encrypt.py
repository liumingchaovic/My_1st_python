# -*- coding: cp936 -*-
'''
��һ�ּ��ɿ��Զ����ݽ��м��ܣ���ʹ��һ��������Ϊ�����ܳס����������Ĺ���ԭ��
���ȣ�ѡ��һ��������Ϊ�ܳף���TRAILBLAZERS����������а������ظ�����ĸ��ֻ������1����
���༸�����������ڣ��޸Ĺ����Ǹ�����������ĸ������棬������ʾ��

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y

������������ĸ����ʣ�����ĸ����������ڶ���Ϣ���м���ʱ����Ϣ�е�ÿ����ĸ���̶��ڶ������У�
�����������еĶ�Ӧ��ĸһһȡ��ԭ�ĵ���ĸ(��ĸ�ַ��Ĵ�Сд״̬Ӧ�ñ���)����ˣ�ʹ������ܳף�
Attack AT DAWN(����ʱ����)�ͻᱻ����ΪTpptad TP ITVH��

'''
def encrypt(key,data):
    key=list(key)
    #len_key=len(key)
    global len_key
    for i in range(len_key-1):
        for j in range(i+1,len_key):
            if key[j]==key[i]:
                #key[j]=''
                del key[j]
                len_key=len(key)#ȫ�ֱ���δ������
    #key=''.join(key)
    word=['a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z']
    base=list(key)
    for c in word:
        if c in base:
            pass
        else:
            base.append(c)
    
    data_out=''
    for i in range(len(data)):
        if 'A'<=data[i]<='Z':
            data_out+=base[word.index(data[i].lower())].upper()
        elif 'a'<=data[i]<='z':
            data_out+=base[word.index(data[i])]
        else:
            data_out+=data[i]
        
    print data_out
key=raw_input().lower()
data=raw_input()
len_key=len(key)
encrypt(key,data)
