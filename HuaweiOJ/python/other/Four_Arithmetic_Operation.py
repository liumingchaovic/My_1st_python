# -*- coding: cp936 -*-
'''
四则运算之逆波兰表达式实现(RPN:Reverse Polish Notation)
1.逆波兰表达式也称后缀表达式，即操作符在操作数之后。
2.如何将数字表达式转换为逆波兰表达式
算法如下：

设置两个栈，一个操作符栈，一个结果数组。操作符栈栈顶元素初始化为'/0'。
运算符的优先级定为+-小于*/。
如果读入的是运算数，直接存入结果数组。
如果读入的是运算符,如果当前运算符的优先级大于操作符栈顶运算符的优先级，
直接将当前运算符入运算符栈；如果当前运算符的优先级小于或者等于操作符栈顶运算符的优先级，
将操作符栈顶运算符出栈再存入结果数组，再将当前运算符入栈到操作符栈。

如果读入的是(，直接入操作符栈。
如果读入的是)，将操作符栈中的符号全都出栈再存入结果数组，直到遇到(,并将(出栈。

正常的表达式 逆波兰表达式

a+b ---> a,b,+
a+(b-c) ---> a,b,c,-,+
a+(b-c)*d ---> a,b,c,-,d,*,+
a+d*(b-c)--->a,d,b,c,-,*,+
a=1+3 ---> a=1,3 +


注意：此程序由于是不断改进的，分了好几段，目前仅支持带括号的四则运算，
运算数支持大于10的正负整数，暂不支持浮点型
例如
15+(2*(-5+8)/3)*10
s_copy=[15, '+', '(', 2, '*', '(', 0, '-', 5, '+', 8, ')', '/', 3, ')', '*', 10]
输出为35
'''

import types
#将输入的字符串整理成所需的列表形式
s=raw_input()
s_copy=[]
i=0
while i<len(s):  #这里用for循环无法改变i的值，因此用while，方便提取超过10的整数
    if '0'<=s[i]<='9':
        k=i+1
        while k<len(s) and ('0'<=s[k]<='9'):
            k+=1
        s_copy.append(int(s[i:k]))
        i=k
    elif s[i] in ['(','[','{']:
        s_copy.append('(')
        m=i+1
        if m<len(s) and s[m]=='-':
            s_copy.append(0)
            s_copy.append('-')
            i=m+1
        else:
            i+=1
    elif s[i] in [')',']','}']:
        s_copy.append(')')
        i+=1
    elif s[i] in ['+','-','*','/']:
        s_copy.append(s[i])
        i+=1
    else:
        pass
'''
s=list(s)
for i in range(len(s)):
    if s[i] in ['{','[']:
        s[i]='('
    elif s[i] in ['}',']']:
        s[i]=')'
    elif '0'<=s[i]<='9':
        s[i]=int(s[i])
    else:
        pass
'''

#将s_copy转换成逆波兰表达式
numbers=s_copy
#print numbers
#numbers=[1,'+',2,'*','(',3,'+',4,'-',5,')','/',6]
characters=[]
RPN=[]
result=[]
characters.append('/0')
priority={}
priority['/0']=-1
priority['+']=0
priority['-']=0
priority['*']=1
priority['/']=1
priority['(']=-1#(后面的任何运算符都得入栈

while numbers:
    aChar=numbers.pop(0)
    if type(aChar) == type(1):#判断数据类型是否为int
        RPN.append(aChar)#若是操作数，则压入result中
    elif aChar == '(': #若是'('，则直接压入符号列表
        characters.append(aChar)
    elif aChar == ')':#若是')'则取操作符，知道遇到最近的'('为止
        bChar=characters.pop()#这个地方必须先弹出来再判断，因为即使遇到'('也要弹出来的
        while bChar!='(':
            RPN.append(bChar)
            bChar=characters.pop()
    else:#剩下的就是+-*/了
        topChar=characters[len(characters)-1]#最后入栈的操作符
        if priority[aChar]>priority[topChar]:#*/ 优先于 +-
            characters.append(aChar) #优先级更高则直接存入
        else:#这种情况只能是当前操作符优先级不大于之前的操作符
            while priority[aChar]<=priority[topChar]:
                bChar=characters.pop()
                RPN.append(bChar)
                topChar=characters[len(characters)-1]#由于characters发生变化，topChar重新获取
            characters.append(aChar)#知道跳出循环，将当前操作符压入栈中
            

while characters:
    bChar=characters.pop()
    if bChar != '/0':
        RPN.append(bChar)

        
#逆波兰表达式计算
while len(RPN)>1:
    for c in RPN:
        if c in ['+','-','*','/']:
            i=RPN.index(c)
            a=RPN.pop(i-2)
            b=RPN.pop(i-2)
            operater=RPN.pop(i-2)
            if operater=='+':
                RPN.insert(i-2,a+b)#这里不能直接赋值，会把对应index的值覆盖掉，用insert
            elif operater=='-':
                RPN.insert(i-2,a-b)
            elif operater=='*':
                RPN.insert(i-2,a*b)
            elif operater=='/':
                RPN.insert(i-2,int(a/b))#这里若要使浮点数就用float，这里仅为了做题
            else:
                pass
            break
        
print RPN[0]
#print 'true'

'''
def Four_Arithmetic_Operation(s):
    s=list(s)
    for i in range(len(s)):
        if s[i] in ['{','[']:
            s[i]='('
        elif s[i] in ['}',']']:
            s[i]=')'
        else:
            pass
    return 0
s=raw_input()
Four_Arithmetic_Operation(s)
'''
