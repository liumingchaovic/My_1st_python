# -*- coding: cp936 -*-
'''
��Ʊͳ��
��һ�������ѡ�˵��������ڶ��������ѡ�˵����֣�����������ͶƱ�˵�����������������ͶƱ
ÿ�������ѡ�˵����ֺ͵�Ʊ����
ʾ�����룺
4
A B C D
8
A B C D E F G H
ʾ�������
A : 1
B : 1
C : 1
D : 1
Invalid : 4
'''

Num_Candidate=input()
Candidate=raw_input().split()
#�������ͬ���ֵ�ֻ�����ʼһ��
#����Candidate_copy���ô����ǲ��ܶ�Candidateֱ�ӽ���remove��������������i���
#������Ҫ�ѵ�һ����ӽ�ȥ����Ϊ��һ��������
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
#����һ���ֵ�
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
