# -*- coding: cp936 -*-
'''
����һ��������㹤�ߣ� A��ʾ�����ƶ���D��ʾ�����ƶ���W��ʾ�����ƶ���S��ʾ�����ƶ���
�ӣ�0,0���㿪ʼ�ƶ����������ַ��������ȡһЩ���꣬�����������������������ļ����档

���룺
�Ϸ�����ΪA(����D����W����S) + ���֣���λ���ڣ�
����֮����;�ָ���
�Ƿ��������Ҫ���ж�������AA10;  A1A;  $%$;  YAD; �ȡ�
������һ���򵥵����� �磺
A10;S20;W10;D30;X;A1A;B10A11;;A10;
������̣�
��㣨0,0��
+   A10   =  ��-10,0��
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  ��Ч
+   A1A   =  ��Ч
+   B10A11   =  ��Ч
+  һ���� ��Ӱ��
+   A10  =  (10,-10)
��� ��10�� -10��

ʾ�����룺A10;S20;W10;D30;X;A1A;B10A11;;A10;
ʾ������� 10,-10 
'''
def IsLegal(string):
    if not 2<=len(string)<=3:
        return False
    if string[0] in ['A','D','W','S']:
        for i in range(1,len(string)):
            if not '0'<=string[i]<='9':
                return False
        return True
    return False
def Pos_Calc(s):
    x=0
    y=0
    for i in range(len(s)):
        if IsLegal(s[i]):
            if s[i][0]=='A':
                x-=int(s[i][1:])
            elif s[i][0]=='D':
                x+=int(s[i][1:])
            elif s[i][0]=='W':
                y+=int(s[i][1:])
            elif s[i][0]=='S':
                y-=int(s[i][1:])
            else:
                pass
    print str(x)+','+str(y)

s=raw_input().split(';')
Pos_Calc(s)
