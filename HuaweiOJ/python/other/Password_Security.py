# -*- coding: cp936 -*-
'''
���밴���¹�����мƷ֣������ݲ�ͬ�ĵ÷�Ϊ������а�ȫ�ȼ����֡�

       һ�����볤��:
       5 ��: С�ڵ���4 ���ַ�
       10 ��: 5 ��7 �ַ�
       25 ��: ���ڵ���8 ���ַ�

       ������ĸ:
       0 ��: û����ĸ
       10 ��: ȫ����С����д��ĸ
       20 ��: ��Сд�����ĸ

       ��������:
       0 ��: û������
       10 ��: 1 ������
       20 ��: ����1 ������

       �ġ�����:
       0 ��: û�з���
       10 ��: 1 ������
       25 ��: ����1 ������

       �塢����:
       2 ��: ��ĸ������
       3 ��: ��ĸ�����ֺͷ���
       5 ��: ��Сд��ĸ�����ֺͷ���

       �������ֱ�׼:

       >= 90: �ǳ���ȫ
       >= 80: ��ȫ��Secure��
       >= 70: �ǳ�ǿ
       >= 60: ǿ��Strong��
       >= 50: һ�㣨Average��
       >= 25: ����Weak��
       >= 0:  �ǳ���
 

��Ӧ���Ϊ��

  VERY_WEAK,
   WEAK,    
   AVERAGE,    
   STRONG,     
   VERY_STRONG,
   SECURE,     
   VERY_SECURE 

       ���������������ַ��������а�ȫ������

       ע��
       ��ĸ��a-z, A-Z
       ���֣�-9

       ���Ű������£� (ASCII��������UltraEdit�Ĳ˵�view->ASCII Table�鿴)
       !"#$%&'()*+,-./     (ASCII�룺x21~0x2F)
       :;<=>?@             (ASCII<=><=><=><=><=>�룺x3A~0x40)
       [\]^_`              (ASCII�룺x5B~0x60)

  {|}~                (ASCII�룺x7B~0x7E)

'''
def Password_Security(s):
    score=0
    s_len=len(s)
    if s_len<=4:
        score+=5
    elif 5<=s_len<=7:
        score+=10
    elif s_len>=8:
        score+=25
    else:
        pass

    Char_upper_num=0
    Char_lower_num=0
    Num_num=0
    Sig_num=0
    for i in range(len(s)):
        if 'A'<=s[i]<='Z':
            Char_upper_num+=1
        elif 'a'<=s[i]<='z':
            Char_lower_num+=1
        elif '0'<=s[i]<='9':
            Num_num+=1
        else:
            Sig_num+=1
    if Char_upper_num!=0 and Char_lower_num!=0:
        score+=20
    elif Char_upper_num!=0 or Char_lower_num!=0:
        score+=10
    elif Char_upper_num==0 and Char_lower_num==0:
        pass
    else:
        pass

    if Num_num>1:
        score+=20
    elif Num_num==1:
        score+=10
    else:
        pass

    if Sig_num>1:
        score+=25
    elif Sig_num==1:
        score+=10
    else:
        pass

    if Char_upper_num and Char_lower_num and Num_num and Sig_num:
        score+=5
    elif (Char_upper_num or Char_lower_num) and Num_num and Sig_num:
        score+=3
    elif (Char_upper_num or Char_lower_num) and Num_num:
        score+=2
    else:
        pass

    if score>=90:
        print 'VERY_SECURE'
    elif score>=80:
        print 'SECURE'
    elif score>=70:
        print 'VERY_STRONG'
    elif score>=60:
        print 'STRONG'
    elif score>=50:
        print 'AVERAGE'
    elif score>=25:
        print 'WEAK'
    else:
        print 'VERY_WEAK'

s=raw_input()
Password_Security(s)
