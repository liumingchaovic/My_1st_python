# -*- coding: cp936 -*-
'''
扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A、2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）：
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如：4 4 4 4-joker JOKER。
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR。
基本规则：
（1）输入每手牌可能是个子、对子、顺子（连续5张）、三个、炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）；
（3）大小规则跟大家平时了解的常见规则相同，个子、对子、三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
（4）输入的两手牌不会出现相等的情况。

输入：
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如 4 4 4 4-joker JOKER
输出：
输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR

答案提示：
1.除了炸弹和对王之外，其他必须同类型比较
2.输入已经保证合法性，不用检查输入是否是合法的牌
3.输入的顺子已经经过从小到大排序，因此不用再排序了
'''
s=raw_input().split('-')
first=str(s[0]).split()
second=str(s[1]).split()

Card_Name=['3','4','5','6','7','8','9','10','J','Q','K','A','2','joker','JOKER']
Card_Num=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
Card=dict(zip(Card_Name,Card_Num))

n1=len(first)
n2=len(second)
#比较麻烦的是没有switch语句
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
    elif n2==5:#以防顺子是A 2 3 4 5， 2 3 4 5 6，所以判断最后一位
        if Card[first[0]]>Card[second[0]]:
            Flag=1
        else:
            Flag=0
    else:
        Flag=-1

#根据Flag对牌大小进行判断和输出
if Flag==1:
    print s[0]
elif Flag==0:
    print s[1]
else:
    print 'ERROR'
