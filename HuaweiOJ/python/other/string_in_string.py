# -*- coding: cp936 -*-
'''
�ж�һ�����ַ����е��ַ��Ƿ���ڳ��ַ�����
���ǣ�����true
���񣬷���false
��һ��������Ƕ̴�
�ڶ���������ǳ���
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
