# -*- coding: cp936 -*-
'''
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）

示例输入：A10;S20;W10;D30;X;A1A;B10A11;;A10;
示例输出： 10,-10 
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
