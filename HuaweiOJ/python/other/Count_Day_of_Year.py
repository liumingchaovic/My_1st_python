# -*- coding: cp936 -*-
'''
根据输入的日期，计算是这一年的第几天。。

详细描述：

输入某年某月某日，判断这一天是这一年的第几天？。

'''
def Count_Day_of_Year(year,month,day):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    run=0
    count=0
    if year%400==0:
        run=1
    elif year%100==0:
        run=0
    elif year%4==0:
        run=1
    else:
        run=0
    for i in range(month-1):
        count+=days[i]
    if run:
        count+=1+day
    else:
        count+=day
    print count
year=input()
month=input()
day=input()
Count_Day_of_Year(year,month,day)
