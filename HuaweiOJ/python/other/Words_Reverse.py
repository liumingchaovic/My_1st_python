# -*- coding: cp936 -*-
'''
题目描述
对字符串中的所有单词进行倒排。
说明：
1、每个单词是以26个大写或小写英文字母构成；
2、非构成单词的字符均视为单词间隔符；
3、要求倒排后的单词间隔符以一个空格表示；如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
4、每个单词最长20个字母；
样例输入
I am a student
样例输入
student a am I

解析思路：
一般都是把空格或已知特定字符作为合并和拆分的基础，这里的非字母字符具有随机性，无法一一捕捉
解决方法为把所有非字母字符全部转换为空格，方便统一处理

示例输入：
I'm a ,good/student
循环后
s=['I', ' ', 'm', ' ', 'a', ' ', ' ', 'g', 'o', 'o', 'd', ' ', 's', 't', 'u', 'd', 'e', 'n', 't']
s1='I m a  good student'  #注意到这个地方有两个空格重叠在一起了
s2=['I', 'm', 'a', 'good', 'student']  #s2再将其分开，这个时候空格就全部消失了
s_Reverse=['student', 'good', 'a', 'm', 'I']  #s3顺便将列表s2里面的元素倒叙一下
s_out='student good a m I'  #最后加入空格

注意程序中列表和元祖（字符串）之间的转换
'''
def Words_Reverse(s):
    s=list(s)
    for i in range(len(s)):
        if not 'A'<=s[i].upper()<='Z':
            s[i]=' '
    s1=''.join(s)
    s2=s1.split()
    s_Reverse=s2[::-1]
    s_out=' '.join(s_Reverse)
    print s_out
s=raw_input()
Words_Reverse(s)
