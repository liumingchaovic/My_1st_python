# -*- coding: cp936 -*-
'''
���Һ�����
��Ŀ���������⣨�û����ɼ������У����Ի�óɼ��Ӹߵ��ͻ�ӵ͵��ߵ�����,��ͬ�ɼ�
      ������¼��������ǰ�Ĺ�����
   ��ʾ��
   jack      70
   peter     96
   Tom       70
   smith     67
   
   �Ӹߵ���  �ɼ�            
   peter     96    
   jack      70    
   Tom       70    
   smith     67    

   �ӵ͵���
   smith     67  
   jack      70  
   Tom       70    
   peter     96

ð�ݵĺô�������=�����Ǳ�֤�б���ֵ��ͬ������±���Ԫ���в���
'''

def Grade_Sort(ss):
    if Flag==0:
        for i in range(len(ss)):
            for j in range(len(ss)-i-1):
                if int(ss[j][1])<int(ss[j+1][1]):
                    ss[j],ss[j+1]=ss[j+1],ss[j]
        return ss
    elif Flag==1:
        for i in range(len(ss)):
            for j in range(len(ss)-i-1):
                if int(ss[j][1])>int(ss[j+1][1]):
                    ss[j],ss[j+1]=ss[j+1],ss[j]
        return ss
    else:
        pass

Num=input()
Flag=input()
ss=[]
for i in range(Num):
    s1,s2=raw_input().split()
    s=[s1,s2]
    ss.append(s)
ss_out=Grade_Sort(ss)
for i in range(Num):
    print ' '.join(ss_out[i])
