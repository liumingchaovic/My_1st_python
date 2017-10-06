# -*- coding: cp936 -*-
'''
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。

       一、密码长度:
       5 分: 小于等于4 个字符
       10 分: 5 到7 字符
       25 分: 大于等于8 个字符

       二、字母:
       0 分: 没有字母
       10 分: 全都是小（大）写字母
       20 分: 大小写混合字母

       三、数字:
       0 分: 没有数字
       10 分: 1 个数字
       20 分: 大于1 个数字

       四、符号:
       0 分: 没有符号
       10 分: 1 个符号
       25 分: 大于1 个符号

       五、奖励:
       2 分: 字母和数字
       3 分: 字母、数字和符号
       5 分: 大小写字母、数字和符号

       最后的评分标准:

       >= 90: 非常安全
       >= 80: 安全（Secure）
       >= 70: 非常强
       >= 60: 强（Strong）
       >= 50: 一般（Average）
       >= 25: 弱（Weak）
       >= 0:  非常弱
 

对应输出为：

  VERY_WEAK,
   WEAK,    
   AVERAGE,    
   STRONG,     
   VERY_STRONG,
   SECURE,     
   VERY_SECURE 

       请根据输入的密码字符串，进行安全评定。

       注：
       字母：a-z, A-Z
       数字：-9

       符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)
       !"#$%&'()*+,-./     (ASCII码：x21~0x2F)
       :;<=>?@             (ASCII<=><=><=><=><=>码：x3A~0x40)
       [\]^_`              (ASCII码：x5B~0x60)

  {|}~                (ASCII码：x7B~0x7E)

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
