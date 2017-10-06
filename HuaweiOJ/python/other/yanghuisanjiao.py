# -*- coding: cp936 -*-
'''
杨辉三角


def printLine(lineList):
    lineList=[str(tmpNum) for tmpNum in lineList]
    print ' '.join(lineList)
    #print("%s%s" %(" "*(N-len(lineList)), " ".join(lineList)))
def yanghuisanjiao(N):
    for i in range(N):
        if i<2:
            yhList=[1]*(i+1)
        else:
            yhList[1:-1]=[(tmpNum+yhList[j]) for j, tmpNum in enumerate(yhList[1:])]
        #printLine(yhList)
    for j in range(len(yhList)):
        if yhList[j]%2==0:
            print j
            break
        
N=input()
yanghuisanjiao(N)
'''
N=input()
if N<=2:
    print -1
elif N%2==1:
    print 2
else:
    print N/2%2+3

