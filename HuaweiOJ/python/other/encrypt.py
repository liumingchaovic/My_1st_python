# -*- coding: cp936 -*-
'''
有一种技巧可以对数据进行加密，它使用一个单词作为它的密匙。下面是它的工作原理：
首先，选择一个单词作为密匙，如TRAILBLAZERS。如果单词中包含有重复的字母，只保留第1个，
其余几个丢弃。现在，修改过的那个单词死于字母表的下面，如下所示：

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
T R A I L B Z E S C D F G H J K M N O P Q U V W X Y

上面其他用字母表中剩余的字母填充完整。在对信息进行加密时，信息中的每个字母被固定于顶上那行，
并用下面那行的对应字母一一取代原文的字母(字母字符的大小写状态应该保留)。因此，使用这个密匙，
Attack AT DAWN(黎明时攻击)就会被加密为Tpptad TP ITVH。

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
                len_key=len(key)#全局变量未起作用
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
