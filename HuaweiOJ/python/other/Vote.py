# -*- coding: cp936 -*-
'''
计票统计
第一行输入候选人的人数，第二行输入候选人的名字，第三行输入投票人的人数，第四行输入投票
每行输出候选人的名字和得票数量
示例输入：
4
A B C D
8
A B C D E F G H
示例输出：
A : 1
B : 1
C : 1
D : 1
Invalid : 4
'''

Num_Candidate=input()
Candidate=raw_input().split()
#如果有相同名字的只保留最开始一个
#建立Candidate_copy的用处就是不能对Candidate直接进行remove操作，否则会造成i溢出
#这里需要把第一项添加进去，因为第一项不参与查找
Candidate_copy=[]
Candidate_copy.append(Candidate[0])
for i in range(1,len(Candidate)):
    if Candidate[i] in Candidate[0:i]:
        pass
    else:
        Candidate_copy.append(Candidate[i])
vote=[]
for i in range(len(Candidate_copy)):
    vote.append(0)
#建立一个字典
dict_Candidate=dict(zip(Candidate_copy,vote))
Num_Voter=input()
Vote=raw_input().split()
Invalid=0
for c in Vote:
    if c in dict_Candidate:
        dict_Candidate[c]+=1
    else:
        Invalid+=1
for c in Candidate_copy:
    print c+' : '+str(dict_Candidate[c])
print 'Invalid : '+str(Invalid)
