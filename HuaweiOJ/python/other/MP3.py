# -*- coding: cp936 -*-
'''
MP3���
MP3 Player��Ϊ��Ļ��С����ʾ�����б��ʱ��ÿ��ֻ����ʾ���׸�����
�û�Ҫͨ�����¼�����������еĸ�����Ϊ�˼򻯴�������ÿ��ֻ����ʾ4�׸�����
����ʼ��λ��Ϊ��1�׸衣

����Ҫʵ��ͨ�����¼����ƹ���ƶ�����������б������߼����£�
��������<=4��ʱ�򣬲���Ҫ��ҳ��ֻ��Ų�����λ�á�

����ڵ�һ�׸�����ʱ����Up�����Ų�����һ�׸�����
��������һ�׸���ʱ����Down�����Ų����һ�׸�����
����������û���Up�������Ų����һ�׸������û���Down�������Ų����һ�׸�����

������������4��ʱ����һ����10�׸�Ϊ������
���ⷭҳ��
��Ļ��ʾ���ǵ�һҳ������ʾ��1 �C4�ף�ʱ������ڵ�һ�׸����ϣ�
�û���Up������ĻҪ��ʾ���һҳ������ʾ��7-10�׸裩��ͬʱ���ŵ����һ�׸��ϡ�
ͬ���ģ���Ļ��ʾ���һҳʱ����������һ�׸����ϣ��û���Down������ĻҪ��ʾ��һҳ��
���Ų����һ�׸��ϡ�

һ�㷭ҳ����Ļ��ʾ�Ĳ��ǵ�һҳʱ������ڵ�ǰ��Ļ��ʾ�ĵ�һ�׸���ʱ��
�û���Up������Ļ�ӵ�ǰ��������һ�׿�ʼ��ʾ�����ҲŲ����һ�׸�����
��굱ǰ��Ļ�����һ�׸�ʱ��Down������Ҳ���ơ�

������������÷�ҳ��ֻ��Ų�������С�

'''
n=input()
opt=raw_input().strip()
top=1
bottom=0
cur=1
if n<=4:
    bottom=n
    for i in range(len(opt)):
        if opt[i]=='U':
            if cur!=1:
                cur-=1
            else:
                cur=n
        elif opt[i]=='D':
            if cur!=n:
                cur+=1
            else:
                cur=1
        else:
            pass
    for i in range(1,n):
        print i,
    print n
    print cur
elif n>4:
    bottom=4
    for i in range(len(opt)):
        if opt[i]=='U':
            if cur==top:
                if top==1:
                    cur=n
                    bottom=n
                    top=n-3
                else:
                    cur-=1
                    top-=1
                    bottom-=1
            else:
                cur-=1
        elif opt[i]=='D':
            if cur==bottom:
                if bottom==n:
                    cur=1
                    top=1
                    bottom=1
                else:
                    cur+=1
                    bottom+=1
                    top+=1
            else:
                cur+=1
        else:
            pass
    print top,top+1,top+2,top+3
    print cur
else:
    pass
