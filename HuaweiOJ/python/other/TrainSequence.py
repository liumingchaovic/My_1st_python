# -*- coding: cp936 -*-
'''
�𳵽�վ
����һ��������N�����������0<N<10���������������վ�����У�һ��N���𳵣�
ÿ����������1-9��š�Ҫ�����ֵ�����������𳵳�վ�����кš�
��ʵҲ����������п��ܵĳ�ջ���С�

�������룺
3
1 2 3
���������
1 2 3
1 3 2
2 1 3
2 3 1
3 2 1

���

������ʵ���ľ���һ��ջ�����ڵ�K�������ڵ�K������ջ֮ǰ��ǰ��� K-1 ����Ҫôȫ����ȥ�ˣ�
Ҫô����ջ���棬Ҫô������ջ���沿�ֳ�ȥ�ˡ���ô���Լ��룬�ڵ�K������ջ֮ǰ��
���δ�ջ�����ȥ 0����1����2������ջ.size()����Ȼ��ѵ�K����ջ��
�ٶ��� K+1��ͬ��ʵʩ�����ķ�����������Ǹ��ݹ��ˡ�
������ȥ�˵ı�����һ���������棬û��վ�ı�����ջ���棬���һ�����������˵ݹ�����������

'''
def TrainSequence(index,s,v):
	for i in range(len(s),-1,-1):#����ÿ������������֣��ȴ���ջ����ģ��ٴ����������
		#ջ��������ֿ��Գ���[0,all]�������ͷŵ�vTemp��������
		sTemp=s[:]
		vTemp=v[:]
		print sTemp,vTemp
		for j in range(1,i+1):#��ջ�������i������������ȥ
			top=sTemp.pop()
			vTemp.append(top)
			print 'i:'+str(i),'j:'+str(j),'top:'+str(top)
		sTemp.append(Train[index]) #�ŵ�ջ��
		print 'i:'+str(i),'index:'+str(index),sTemp,vTemp
		if n-1==index: #������
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
