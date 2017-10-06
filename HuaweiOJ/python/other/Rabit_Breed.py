# -*- coding: cp936 -*-
'''
有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？

'''
def Rabit_Breed(month):
    if month==1 or month==2:
        return 1
    else:
        return Rabit_Breed(month-1)+Rabit_Breed(month-2)
month=input()
print Rabit_Breed(month)
