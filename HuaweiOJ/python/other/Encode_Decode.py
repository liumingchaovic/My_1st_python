# -*- coding: cp936 -*-
'''
��Ŀ����

1����������ַ������мӽ��ܣ��������
2���ܷ���Ϊ��
��������Ӣ����ĸʱ���ø�Ӣ����ĸ�ĺ�һ����ĸ�滻��ͬʱ��ĸ�任��Сд,����ĸaʱ���滻ΪB����ĸZʱ���滻Ϊa��
������������ʱ��Ѹ����ּ�1����0�滻1��1�滻2��9�滻0��
�����ַ������仯��
3�����ܷ���Ϊ���ܵ�����̡�


���룺
����һ��Ҫ���ܵ�����
����һ���ӹ��ܵ�����
�����
������ܺ���ַ�
������ܺ���ַ�

ʾ�����룺
abcdefg
BCDEFGH
ʾ�������
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
