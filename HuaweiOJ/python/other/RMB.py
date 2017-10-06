# -*- coding: cp936 -*-
'''
人民币转换成大写
考试题目和要点：
1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用
壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、整等字样填写。（30分） 

2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，
如￥ 532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。（30分） 

3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，
中文大写金额中间只写一个“零”字，如￥6007.14，应写成“人民币陆仟零柒元壹角肆分“。

注意：这个复制的时候一定要把上面的编码格式复制进去，不然程序运行肯定出错
'''
n=input()
list1='元拾佰仟万拾佰仟亿拾佰仟'
list2='零壹贰叁肆伍陆柒捌玖'
title='人民币'
temp=0
tmp=0
zero=1
Flag=0
if n==0:
    print title+'零元整'
a=int(n)

for i in range(11,-1,-1):
    d=1
    for j in range(i,0,-1):
        d*=10
    if a>d:
        Flag=1
        temp=int(float(a)/d)
        tmp=temp%10
        if tmp!=0:
            if zero==0:
                title+=list2[0:2]
            if (i==1 or i==5 or i==9) and tmp==1:
                title+=list1[2*i:2*(i+1)]
            else:
                title+=list2[2*tmp:2*(tmp+1)]+list1[2*i:2*(i+1)]
        else:
            if i==8 or i==4 or i==0:
                title+=list1[2*i:2*(i+1)]
    #设置此标志位就是因为当a>d不满足时tmp会赋值给zero，这并不是我们想要的
    if Flag:
        zero=tmp
b=int(n*100-a*100)

if a==n:
    title+='整'
else:
    temp=b/10
    tmp=b%10
    if temp!=0:
        title+=list2[2*temp:2*(temp+1)]+'角'
        if tmp!=0:
            title+=list2[2*tmp:2*(tmp+1)]+'分'
    else:
        title+=list2[0:2]+list2[2*tmp:2*(tmp+1)]+'分'
print title
