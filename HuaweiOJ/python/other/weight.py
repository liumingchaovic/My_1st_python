# -*- coding: cp936 -*-
'''
������
��һ�����룬����������ȣ��ֱ�Ϊm1,m2......mn�����ǿ�ȡ����������ֱ�Ϊx1,x2......xn��
����Ҫ����Щ����ȥ����������������ܳƳ������ֲ�ͬ������
ע��
������������0
���룺
n��������������ͬ������
weight:n�����������
num:n��������������
�����
���ø�����������ԳƳ��Ĳ�ͬ��������
ʾ������
2
1
2
2
1
ʾ�����
5
'''
import sys
try:

	N=input()
	if N<=0:
		sys.exit()
	weight=[]
	for i in range(N):
		a=input()
		if a<=0:
			sys.exit()
		else:
			weight.append(a)
	num=[]
	for i in range(N):
		b=input()
		if b<=0:
			sys.exit()
		else:
			num.append(b)
	'''
	ע��������Ҫ�ж�i==0����Ϊ������жϵĻ���������for��ʹset_weight=[0,1]
	Ȼ��j=2��ʱ��ʹ�õ���set_weight=[0,1]ͬʱ����Ҫ��set_weight���б������
	Ȼ��ͻ�����������
	2
	1
	2
	2
	1
	1 1 0 [0, 1]
	1 2 0 [0, 1, 2]
	1 2 1 [0, 1, 2, 3]
	2 1 0 [0, 1, 2, 3, 2]
	2 1 1 [0, 1, 2, 3, 2, 3]
	2 1 2 [0, 1, 2, 3, 2, 3, 4]
	2 1 3 [0, 1, 2, 3, 2, 3, 4, 5]
	'''
	set_weight=[0]
	for i in range(N):
		for j in range(1,num[i]+1):
			if i==0:
				set_weight.append(weight[i]*j)
			else:
				for k in range(len(set_weight)):
					set_weight.append(set_weight[k]+weight[i]*j)
				
	print len(set(set_weight))
except SystemExit:
	pass
