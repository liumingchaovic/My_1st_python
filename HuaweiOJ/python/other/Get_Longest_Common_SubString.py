# -*- coding: utf8 -*-

'''
寻找两个字符串a,b中最长公共字符串
示例：
abcdefghijklmnop
abcsafjklmnopqrstuvw
输出：
jklmnop
'''
def Get_Longest_Common_SubString(s1,s2):
	maxlen=0
	index_first=0
	max_len_index=0
	for i in range(len(s1)):
		for j in range(len(s2)):
			if s1[i]==s2[j]:
				count=1
				index_first=i
				while i<len(s1)-1 and j<len(s2)-1 and s1[i+1]==s2[j+1]:
					count+=1
					i+=1
					j+=1
					
				if count>maxlen:
					maxlen=count
					max_len_index=index_first
					
	print maxlen
	print s1[max_len_index:max_len_index+maxlen]

s1=raw_input()
s2=raw_input()
'''应系统要求，此处要连续输入两个参数，并以空格分开'''
'''s1,s2=raw_input().split(' ')'''
Get_Longest_Common_SubString(s1,s2)

