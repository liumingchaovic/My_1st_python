# -*- coding: cp936 -*-
'''�ַ�����
��дһ�����򣬽������ַ����е��ַ������¹�������
����1��Ӣ����ĸ��A��Z���У������ִ�Сд��
      �磬���룺Type �����epTy
����2��ͬһ��Ӣ����ĸ�Ĵ�Сдͬʱ����ʱ����������˳�����С�
    �磬���룺BabA �����aABb
����3����Ӣ����ĸ�������ַ�����ԭ����λ�á�
    �磬���룺By?e �����Be?y
������
    ���룺
   A Famous Saying: Much Ado About Nothing(2012/8).
    �����
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
