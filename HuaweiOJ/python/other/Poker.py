# -*- coding: cp936 -*-
'''
�˿�����Ϸ���Ӧ�ö��Ƚ���Ϥ�ˣ�һ������54����ɣ���3~A��2��4�ţ�С��1�ţ�����1�š������С�����������ַ����ַ�����ʾ�����У�Сдjoker��ʾС������дJOKER��ʾ��������
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
���������ƣ�������֮����"-"���ӣ�ÿ���Ƶ�ÿ�����Կո�ָ���"-"����û�пո��磺4 4 4 4-joker JOKER��
��Ƚ������ƴ�С������ϴ���ƣ���������ڱȽϹ�ϵ�����ERROR��
��������
��1������ÿ���ƿ����Ǹ��ӡ����ӡ�˳�ӣ�����5�ţ���������ը�����ĸ����Ͷ����е�һ�֣���������������������뱣֤�����ƶ��ǺϷ��ģ�˳���Ѿ���С�������У�
��2������ը���Ͷ������Ժ������ƱȽ�֮�⣬�������͵���ֻ�ܸ���ͬ���͵Ĵ��ڱȽϹ�ϵ���磬���Ӹ����ӱȽϣ������������Ƚϣ��������ǲ���������磺�����Ӳ�ֳɸ��ӣ���
��3����С��������ƽʱ�˽�ĳ���������ͬ�����ӡ����ӡ������Ƚ������С��˳�ӱȽ���С�ƴ�С��ը������ǰ�����е��ƣ�ը��֮��Ƚ������С�������������ƣ�
��4������������Ʋ��������ȵ������

���룺
���������ƣ�������֮����"-"���ӣ�ÿ���Ƶ�ÿ�����Կո�ָ���"-"����û�пո��� 4 4 4 4-joker JOKER
�����
����������нϴ�����֣��������ӷ����˿���˳�򲻱䣬���Կո��������������ڱȽϹ�ϵ�����ERROR

����ʾ��
1.����ը���Ͷ���֮�⣬��������ͬ���ͱȽ�
2.�����Ѿ���֤�Ϸ��ԣ����ü�������Ƿ��ǺϷ�����
3.�����˳���Ѿ�������С����������˲�����������
'''
s=raw_input().split('-')
first=str(s[0]).split()
second=str(s[1]).split()

Card_Name=['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
Card_Num=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
Card=dict(zip(Card_Name,Card_Num))

n1=len(first)
n2=len(second)
#�Ƚ��鷳����û��switch���
Flag=0
if n1==1:
    if n2==1:
        if Card[first[0]]>Card[second[0]]:
            Flag=1
        else:
            Flag=0
    elif n2==2:
        if Card[second[0]]==16 and Card[second[1]]==17 or Card[second[0]]==17 and Card[second[1]]==16:
            Flag=0
        else:
            Flag=-1
    elif n2==4:
        Flag=0
    else:
        Flag=-1
elif n1==2:
    if Card[first[0]]==16 and Card[first[1]]==17 or Card[first[0]]==17 and Card[first[1]]==16:
        Flag=1
    else:
        if n2==2:
            if Card[first[0]]>Card[second[0]]:
                Flag=1
            else:
                Flag=0
        elif n2==4:
            Flag=0
        else:
            Flag=-1
elif n1==3:
    if n2==2:
        if Card[second[0]]==16 and Card[second[1]]==17 or Card[second[0]]==17 and Card[second[1]]==16:
            Flag=0
        else:
            Flag=-1
    elif n2==3:
        if Card[first[0]]>Card[second[0]]:
            Flag=1
        else:
            Flag=0
    elif n2==4:
        Flag=0
    else:
        Flag=-1
elif n1==4:
    if n2==2:
        if Card[second[0]]==16 and Card[second[1]]==17 or Card[second[0]]==17 and Card[second[1]]==16:
            Flag=0
        else:
            Flag=1
    elif n2==4:
        if Card[first[0]]>Card[second[0]]:
            Flag=1
        else:
            Flag=0
    else:
        Flag=1
elif n1==5:
    if n2==2:
        if Card[second[0]]==16 and Card[second[1]]==17 or Card[second[0]]==17 and Card[second[1]]==16:
            Flag=0
        else:
            Flag=-1
    elif n2==4:
        Flag=0
    elif n2==5:#�Է�˳����A 2 3 4 5�� 2 3 4 5 6�������ж����һλ
        if Card[first[0]]>Card[second[0]]:
            Flag=1
        else:
            Flag=0
    else:
        Flag=-1

#����Flag���ƴ�С�����жϺ����
if Flag==1:
    print s[0]
elif Flag==0:
    print s[1]
else:
    print 'ERROR'
