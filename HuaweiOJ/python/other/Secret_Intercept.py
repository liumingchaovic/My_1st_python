# -*- coding: cp936 -*-
'''
Catcher��MCA�����鱨Ա��������ʱ���ֵй�����һЩ�ԳƵ��������ͨ�ţ�
��������ЩABBA��ABA��A��123321������������ʱ���ڿ�ʼ�����ʱ����һЩ�޹ص��ַ�
�Է�ֹ����ƽ⡣����������б仯 ABBA->12ABBA,ABA->ABAKK,123321->51233214����
��Ϊ�ػ�Ĵ�̫���ˣ����Ҵ��ڶ��ֿ��ܵ������abaaab�ɿ�����aba,��baaab�ļ�����ʽ����
Cathcer�Ĺ�����ʵ����̫���ˣ���ֻ������Ը������������ܰ�Catcher�ҳ������Ч���봮��

��������һ������ط�����Ҳ����֮ǰ�����ַ�����ȡ��󹫹��ַ����ķ�������Ȼ�ǶԳƵģ�
��ô�ߵ�˳�򲢲���ı�ʲô����ȡ�Ĺ����ַ���Ҳ��Ȼ�������������

'''
def Secret_Intercept(ss):
    ss=list(ss)
    ss_reverse=ss[:]
    ss_reverse.reverse()
    max_count=0
    max_index=0
    for i in range(len(ss)):
        for j in range(len(ss_reverse)):
            if ss[i]==ss_reverse[j]:
                count=1
                index_first=i
                while(i+1<len(ss) and j+1<len(ss_reverse) and ss[i+1]==ss_reverse[j+1]):
                    count+=1
                    i+=1
                    j+=1
                if count>max_count:
                    max_count=count
                    max_index=index_first
    print max_count
    print ''.join(ss[max_index:max_index+max_count])
s=raw_input()
Secret_Intercept(s)
