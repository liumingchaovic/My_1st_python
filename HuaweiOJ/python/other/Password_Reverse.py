# -*- coding: cp936 -*-
'''
����Ԩ��ԭ��һ��BBS�ϵ�����Ϊzvbo9441987,Ϊ�˷�����䣬��ͨ��һ���㷨���������任��
YUANzhi1987������������������ֺͳ�����ݣ���ô���������ˣ����ҿ�����Ŀ�ŵ��ط�������
�ĵط�����������֪�����������롣
������ô�任�ģ���Ҷ�֪���ֻ��ϵ���ĸ��
1--1�� abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
����ô�򵥣�Ԩ�Ӱ������г��ֵ�Сд��ĸ����ɶ�Ӧ�����֣����ֺ������ķ��Ŷ������任��
������������û�пո񣬶������г��ֵĴ�д��ĸ����Сд֮��������һλ��
�磺X���ȱ��Сд����������һλ��������y����򵥰ɡ���ס��z��������aŶ��
'''
def Big_To_Small(s):
    small=chr(ord(s)+33)
    return 'a' if ord(small)>=123 else small

def Small_To_Num(s):
    if s in ['a','b','c']:
        return '2'
    elif s in ['d','e','f']:
        return '3'
    elif s in ['g','h','i']:
        return '4'
    elif s in ['j','k','l']:
        return '5'
    elif s in ['m','n','o']:
        return '6'
    elif s in ['p','q','r','s']:
        return '7'
    elif s in ['t','u','v']:
        return '8'
    elif s in ['w','x','y','z']:
        return '9'
    else:
        return '0'

s=raw_input()
s=list(s)
ss=''
for c in s:
    if 'a'<= c <='z':
        ss+=Small_To_Num(c)
    elif 'A'<= c <='Z':
        ss+=Big_To_Small(c)
    elif '0'<= c <='9':
        ss+=c
    else:
        break
print ss
