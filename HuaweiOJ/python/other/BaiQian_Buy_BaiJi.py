# -*- coding: cp936 -*-
'''
公元前五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
详细描述：
接口说明
原型：
int GetResult(vector &list)
输入参数：
        任意一个整数开始
输出参数（指针指向的内存区域保证有效）：
    list  鸡翁、鸡母、鸡雏组合的列表
返回值：
     -1 失败     
     0 成功
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

