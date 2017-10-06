# -*- coding: cp936 -*-
'''
��������֮�沨�����ʽʵ��(RPN:Reverse Polish Notation)
1.�沨�����ʽҲ�ƺ�׺���ʽ�����������ڲ�����֮��
2.��ν����ֱ��ʽת��Ϊ�沨�����ʽ
�㷨���£�

��������ջ��һ��������ջ��һ��������顣������ջջ��Ԫ�س�ʼ��Ϊ'/0'��
����������ȼ���Ϊ+-С��*/��
������������������ֱ�Ӵ��������顣
���������������,�����ǰ����������ȼ����ڲ�����ջ������������ȼ���
ֱ�ӽ���ǰ������������ջ�������ǰ����������ȼ�С�ڻ��ߵ��ڲ�����ջ������������ȼ���
��������ջ���������ջ�ٴ��������飬�ٽ���ǰ�������ջ��������ջ��

����������(��ֱ���������ջ��
����������)����������ջ�еķ���ȫ����ջ�ٴ��������飬ֱ������(,����(��ջ��

�����ı��ʽ �沨�����ʽ

a+b ---> a,b,+
a+(b-c) ---> a,b,c,-,+
a+(b-c)*d ---> a,b,c,-,d,*,+
a+d*(b-c)--->a,d,b,c,-,*,+
a=1+3 ---> a=1,3 +


ע�⣺�˳��������ǲ��ϸĽ��ģ����˺ü��Σ�Ŀǰ��֧�ִ����ŵ��������㣬
������֧�ִ���10�������������ݲ�֧�ָ�����
����
15+(2*(-5+8)/3)*10
s_copy=[15, '+', '(', 2, '*', '(', 0, '-', 5, '+', 8, ')', '/', 3, ')', '*', 10]
���Ϊ35
'''

import types
#��������ַ��������������б���ʽ
s=raw_input()
s_copy=[]
i=0
while i<len(s):  #������forѭ���޷��ı�i��ֵ�������while��������ȡ����10������
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

#��s_copyת�����沨�����ʽ
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
priority['(']=-1#(������κ������������ջ

while numbers:
    aChar=numbers.pop(0)
    if type(aChar) == type(1):#�ж����������Ƿ�Ϊint
        RPN.append(aChar)#���ǲ���������ѹ��result��
    elif aChar == '(': #����'('����ֱ��ѹ������б�
        characters.append(aChar)
    elif aChar == ')':#����')'��ȡ��������֪�����������'('Ϊֹ
        bChar=characters.pop()#����ط������ȵ��������жϣ���Ϊ��ʹ����'('ҲҪ��������
        while bChar!='(':
            RPN.append(bChar)
            bChar=characters.pop()
    else:#ʣ�µľ���+-*/��
        topChar=characters[len(characters)-1]#�����ջ�Ĳ�����
        if priority[aChar]>priority[topChar]:#*/ ������ +-
            characters.append(aChar) #���ȼ�������ֱ�Ӵ���
        else:#�������ֻ���ǵ�ǰ���������ȼ�������֮ǰ�Ĳ�����
            while priority[aChar]<=priority[topChar]:
                bChar=characters.pop()
                RPN.append(bChar)
                topChar=characters[len(characters)-1]#����characters�����仯��topChar���»�ȡ
            characters.append(aChar)#֪������ѭ��������ǰ������ѹ��ջ��
            

while characters:
    bChar=characters.pop()
    if bChar != '/0':
        RPN.append(bChar)

        
#�沨�����ʽ����
while len(RPN)>1:
    for c in RPN:
        if c in ['+','-','*','/']:
            i=RPN.index(c)
            a=RPN.pop(i-2)
            b=RPN.pop(i-2)
            operater=RPN.pop(i-2)
            if operater=='+':
                RPN.insert(i-2,a+b)#���ﲻ��ֱ�Ӹ�ֵ����Ѷ�Ӧindex��ֵ���ǵ�����insert
            elif operater=='-':
                RPN.insert(i-2,a-b)
            elif operater=='*':
                RPN.insert(i-2,a*b)
            elif operater=='/':
                RPN.insert(i-2,int(a/b))#������Ҫʹ����������float�������Ϊ������
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
