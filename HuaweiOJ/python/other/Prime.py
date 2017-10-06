# -*- coding: cp936 -*-
'''
质数因子
输入一个正整数，按照从小到大的顺序输出它的所有质数的因子
例如180的质数因子为2 2 3 3 5
此代码参考静水深流
https://code.csdn.net/snippets/436936/master/snippet_file_0.txt/raw
我觉得是解这道题见过的最简洁，最奥秘的代码，没有经过特殊处理，却保证i为质数
'''
def Prime(N):
    for i in range(2,N+1):
        while(N%i==0 and N!=0):
            print i,
            N=N/i
N=input()
Prime(N)
