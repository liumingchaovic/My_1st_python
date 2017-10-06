# -*- coding: cp936 -*-
'''字符排序
编写一个程序，将输入字符串中的字符按如下规则排序。
规则1：英文字母从A到Z排列，不区分大小写。
      如，输入：Type 输出：epTy
规则2：同一个英文字母的大小写同时存在时，按照输入顺序排列。
    如，输入：BabA 输出：aABb
规则3：非英文字母的其它字符保持原来的位置。
    如，输入：By?e 输出：Be?y
样例：
    输入：
   A Famous Saying: Much Ado About Nothing(2012/8).
    输出：
   A  aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
'''
def Sort_String(String_in):
    String_input=list(String_in)
    for i in range(len(String_input)):
        for j in range(len(String_input)-1-i):
            if (String_input[j].upper()<'A' or String_input[j].upper>'Z'):
                continue
            k=j+1
            while k<len(String_input) and (String_input[k].upper()<'A' or String_input[k].upper()>'Z'):
                k=k+1
            if k==len(String_input):
                continue
            if String_input[j].upper()>String_input[k].upper():
                String_input[j],String_input[k]=String_input[k],String_input[j]
    return ''.join(String_input)
s1=raw_input()
String_out=Sort_String(s1)
print String_out
