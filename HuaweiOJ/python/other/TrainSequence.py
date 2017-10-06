# -*- coding: cp936 -*-
'''
火车进站
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，
每辆火车以数字1-9编号。要求以字典序排序输出火车出站的序列号。
其实也就是输出所有可能的出栈序列。

样例输入：
3
1 2 3
样例输出：
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1

解答：

　　其实核心就是一个栈，对于第K个数，在第K个数进栈之前，前面的 K-1 个数要么全部出去了，
要么都在栈里面，要么部分在栈里面部分出去了。那么可以假想，在第K个数入栈之前，
依次从栈里面出去 0个、1个、2个……栈.size()个，然后把第K个入栈，
再对于 K+1个同样实施这样的方法——这就是个递归了。
　　出去了的保存在一个队列里面，没出站的保存在栈里面，最后一辆车处理完了递归结束并输出。

'''
def TrainSequence(index,s,v):
	for i in range(len(s),-1,-1):#对于每个待处理的数字，先处理栈里面的，再处理这个数字
		#栈里面的数字可以出来[0,all]，出来就放到vTemp里面待输出
		sTemp=s[:]
		vTemp=v[:]
		print sTemp,vTemp
		for j in range(1,i+1):#从栈里面出来i个到队列里面去
			top=sTemp.pop()
			vTemp.append(top)
			print 'i:'+str(i),'j:'+str(j),'top:'+str(top)
		sTemp.append(Train[index]) #放到栈顶
		print 'i:'+str(i),'index:'+str(index),sTemp,vTemp
		if n-1==index: #结果输出
			isFirst=True
			vRes=[]
			if not isFirst:
				print
			for i in range(len(vTemp)):
				vRes.append(vTemp[i])
			while sTemp!=[]:
				top=sTemp.pop()
				vRes.append(top)
			for j in range(len(vRes)-1):
				print vRes[j],
			print vRes[-1]
			isFirst=False
		else:
			TrainSequence(index+1,sTemp,vTemp)
	return 0
n=input()
s=raw_input().split()
Train=[]
for c in s:
	Train.append(int(c))
s=[]
v=[]
TrainSequence(0,s,v)
