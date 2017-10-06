# -*- coding: cp936 -*-
'''
查找和排序
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
      都按先录入排列在前的规则处理。
   例示：
   jack      70
   peter     96
   Tom       70
   smith     67
   
   从高到低  成绩            
   peter     96    
   jack      70    
   Tom       70    
   smith     67    

   从低到高
   smith     67  
   jack      70  
   Tom       70    
   peter     96

冒泡的好处（不加=）就是保证列表在值相同的情况下保持元序列不变
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
