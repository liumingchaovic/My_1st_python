# -*- coding: cp936 -*-
'''
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，
比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符
以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

这里用了一个巧妙地方法，也即是之前两个字符串提取最大公共字符串的方法，既然是对称的，
那么颠倒顺序并不会改变什么，提取的公共字符串也必然是最长密码所在了

'''
def Secret_Intercept(ss):
    ss=list(ss)
    ss_reverse=ss[:]
    ss_reverse.reverse()
    max_count=0
    max_index=0
    for i in range(len(ss)):
        for j in range(len(ss_reverse)):
            if ss[i]==ss_reverse[j]:
                count=1
                index_first=i
                while(i+1<len(ss) and j+1<len(ss_reverse) and ss[i+1]==ss_reverse[j+1]):
                    count+=1
                    i+=1
                    j+=1
                if count>max_count:
                    max_count=count
                    max_index=index_first
    print max_count
    print ''.join(ss[max_index:max_index+max_count])
s=raw_input()
Secret_Intercept(s)
