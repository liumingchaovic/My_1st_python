# -*- coding: cp936 -*-
'''
���дһ�����������������Ӻ�����������n x m�����̸��ӣ�nΪ����ĸ�������mΪ����ĸ�������
���Ÿ��Ա�Ե�ߴ����Ͻ��ߵ����½ǣ��ܹ��ж������߷���Ҫ�����߻�ͷ·������ֻ�����Һ������ߣ�
��������������ߡ�

ʾ�����룺
2
2
ʾ�������
6
'''
def count(m,n):
    if (m==1 and n==0) or (m==0 and n==1):
        return 1
    if m>0 and n>0:
        return count(m-1,n)+count(m,n-1)
    if m==0:
        return count(m,n-1)
    if n==0:
        return count(m-1,n)
    return 0

m=input()
n=input()
print count(m,n)
