# -*- coding: cp936 -*-
'''
题目描述

1、对输入的字符串进行加解密，并输出。
2加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。


输入：
输入一串要加密的密码
输入一串加过密的密码
输出：
输出加密后的字符
输出解密后的字符

示例输入：
abcdefg
BCDEFGH
示例输出：
BCDEFGH
abcdefg
'''
def encode(string):
    StringList=list(string)
    StringOut=[]
    for i in range(len(StringList)):
        if 'a'<=StringList[i]<='z':
            if StringList[i]=='z':
                StringOut.append('A')
            else:
                StringOut.append((chr(ord(StringList[i])+1)).upper())
        elif 'A'<=StringList[i]<='Z':
            if StringList[i]=='Z':
                StringOut.append('a')
            else:
                StringOut.append((chr(ord(StringList[i])+1)).lower())
        elif '0'<=StringList[i]<='9':
            if StringList[i]=='9':
                StringOut.append('0')
            else:
                StringOut.append(chr(ord(StringList[i])+1))
        else:
            StringOut.append(StringList[i])
    print ''.join(StringOut)
def decode(string):
    StringList=list(string)
    StringOut=[]
    for i in range(len(StringList)):
        if 'a'<=StringList[i]<='z':
            if StringList[i]=='a':
                StringOut.append('Z')
            else:
                StringOut.append((chr(ord(StringList[i])-1)).upper())
        elif 'A'<=StringList[i]<='Z':
            if StringList[i]=='A':
                StringOut.append('z')
            else:
                StringOut.append((chr(ord(StringList[i])-1)).lower())
        elif '0'<=StringList[i]<='9':
            if StringList[i]=='0':
                StringOut.append('9')
            else:
                StringOut.append(chr(ord(StringList[i])-1))
        else:
            StringOut.append(StringList[i])
    print ''.join(StringOut)
str_en=raw_input()
str_de=raw_input()
encode(str_en)
decode(str_de)
