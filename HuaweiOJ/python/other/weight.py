# -*- coding: cp936 -*-
'''
称砝码
有一组砝码，重量互不相等，分别为m1,m2......mn；它们可取的最大数量分别为x1,x2......xn。
现在要用这些砝码去称物体的重量，问能称出多少种不同的重量
注：
称重重量包括0
输入：
n：多少组重量不同的砝码
weight:n组砝码的重量
num:n组砝码的最大数量
输出：
利用给定的砝码可以称出的不同的重量数
示例输入
2
1
2
2
1
示例输出
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
	注意这里需要判断i==0，因为如果不判断的话，最里层的for会使set_weight=[0,1]
	然后j=2的时候使用的是set_weight=[0,1]同时还需要对set_weight进行遍历相加
	然后就会出现如下情况
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
