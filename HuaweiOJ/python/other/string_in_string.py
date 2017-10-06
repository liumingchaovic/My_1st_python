# -*- coding: cp936 -*-
'''
判断一个短字符串中的字符是否均在长字符串中
若是，返回true
若否，返回false
第一个输入的是短串
第二个输入的是长串
'''
s1=raw_input()
s2=raw_input()
Flag=0
for i in range(len(s1)):
	if s1[i] not in s2:
		Flag=1
		pass
if Flag==0:
	print 'true'
elif Flag==1:
	print 'false'
else:
	pass
