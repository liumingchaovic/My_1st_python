# -*- coding: cp936 -*-
'''
假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成
YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼
的地方而不被别人知道真正的密码。
他是这么变换的，大家都知道手机上的字母：
1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,
就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，
声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，
如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
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
