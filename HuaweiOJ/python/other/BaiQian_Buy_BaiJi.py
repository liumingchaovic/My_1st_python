# -*- coding: cp936 -*-
'''
��Ԫǰ�����ͣ��ҹ��Ŵ���ѧ�������ڡ��㾭��һ��������ˡ��ټ����⡱��
����һֵǮ�壬��ĸһֵǮ����������ֵǮһ����Ǯ��ټ����ʼ��̡���ĸ�����������Σ�
��ϸ������
�ӿ�˵��
ԭ�ͣ�
int GetResult(vector &list)
���������
        ����һ��������ʼ
���������ָ��ָ����ڴ�����֤��Ч����
    list  ���̡���ĸ��������ϵ��б�
����ֵ��
     -1 ʧ��     
     0 �ɹ�
'''
def BaiQian_Buy_BaiJi(cock,hen,chicken):
    cock=int(100/5)
    for i in range(cock):
        hen=int((100-5*i)/3)
        for j in range(hen):
            chicken=100-i-j+1
            for k in range(0,chicken,3):
                if (5*i+3*j+k/3==100 and i+j+k==100):
                    print i,j,k
cock,hen,chicken=0,0,0
if raw_input():
    BaiQian_Buy_BaiJi(cock,hen,chicken)

