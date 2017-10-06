# -*- coding: cp936 -*-
'''
题目描述
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
（用K表示）5，1，1和1，5，1 是同一种分法。

输入
每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。<=n<=10<=m<=10
样例输入
7 3
样例输出
8

m个相同的苹果放入n个相同的篮子，篮子可以为空。
下面两种方法求解，动态规划和递归。但都须知：
dp[0][j]=0;含义为:j（j>0）个苹果放入0个篮子，没有地方放，放法为0.
dp[i][0]=1;0个苹果放入i个篮子，每个篮子都为空，放法为1.
dp[0][0]=1;当然，0个苹果放到0个篮子放法为1.即0！=1；
还有 dp[i][j],i>j时，即篮子数大于苹果数是dp[i][j]=dp[j][j],
含义为 把2个苹果放到5个篮子的放法和把2个苹果放到2个篮子放法数相同。
'''
def Apple_in_Basket(m,n):
    if n==0 and m!=0:
        return 0
    elif m==0:
        return 1
    elif m>=n:
        return Apple_in_Basket(m-n,n)+Apple_in_Basket(m,n-1)
    else:
        return Apple_in_Basket(m,m)
Apple,Basket=raw_input().split()
print Apple_in_Basket(int(Apple),int(Basket))
