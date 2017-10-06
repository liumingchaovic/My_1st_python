# -*- coding: cp936 -*-
'''
迷宫问题
定义一个二维数组N*M（其中2<=N<=10;2<=M<=10），如5 × 5数组下所示： 
int maze[5][5] = {
        0, 1, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 0,
        0, 0, 0, 1, 0,
};

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的最短路线。入口点为[0,0],既第一空格是可以走的路。
Input
一个N × M的二维数组，表示一个迷宫。数据保证有唯一解,不考虑有多解的情况，即迷宫只有一条通道。
Output
左上角到右下角的最短路径，格式如样例所示。
Sample Input
0 1 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
0 0 0 1 0

Sample Output
(0, 0)
(1, 0)
(2, 0)
(2, 1)
(2, 2)
(2, 3)
(2, 4)
(3, 4)
(4, 4)
'''



def Maze_Path(xi,yi):
    global MinPath
    mz[xi][yi]=-1  #设置标记，避免走回来了
    tempx=[]
    tempy=[]
    tempx.append(xi)
    tempy.append(yi)
    pair=zip(tempx,tempy)
    Path.append(pair[0])
    if xi==x_end and yi==y_end:  #当前位置为出口
        if len(MinPath)==0 or len(Path)<len(MinPath):
            MinPath=Path[:]
        mz[xi][yi]=0
        Path.pop()
        return
    if yi+1<M and mz[xi][yi+1]==0:   #右
        Maze_Path(xi,yi+1)
    if xi-1>=0 and mz[xi-1][yi]==0:  #左
        Maze_Path(xi-1,yi)
    if yi-1>=0 and mz[xi][yi-1]==0:  #上
        Maze_Path(xi,yi-1)
    if xi+1<N and mz[xi+1][yi]==0:   #下
        Maze_Path(xi+1,yi)
    mz[xi][yi]=0   #清除标记
    Path.pop()

MinPath=[] #保存最短路径
Path=[]    #保存当前路径
'''
mz=[[0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0]
    ]
'''
mz=[]
ss=[]
s=raw_input().split()
N=int(s[0])
M=int(s[1])
for i in range(N):
    s=raw_input().split()
    for j in range(M):
        ss.append(int(s[j]))
    mz.append(ss)
    ss=[]
#print mz
x_end=N-1
y_end=M-1
Maze_Path(0,0)
#print MinPath
for i in range(len(MinPath)):
    print '('+str(MinPath[i][0])+','+str(MinPath[i][1])+')'
'''
Pre=item() #保存任意点在路径中的前一步
move=item()
a=[[-1,0],[0,-1],[1,0],[0,1]]
for c in a:
    move.append(c)
print move

def search(x,y,Flag):
    if x==m-1 and y==n-1:
        Flag=1
    else:
        maze[x][y]=1
        if Flag != 1 and y != n-1 and maze[x][y+1]==0:
            search(x,y+1,Flag)
        elif Flag != 1 and x != m-1 and maze[x+1][y]==0:
            search(x+1,y,Flag)
        elif Flag != 1 and y != 0 and maze[x][y-1]==0:
            search(x,y-1,Flag)
        elif Flag != 1 and x != 0 and maze[x-1][y]==0:
            search(x-1,y,Flag)
        else:
            pass
        maze[x][y]=0
        if Flag==1:
            maze[x][y]=5
maze=[[0,1,0,0,0],
      [0,1,0,1,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,0,1,0]
      ]
Flag=0
m=5
n=5
search(0,0,Flag)
for i in range(m):
    for j in range(n):
        print maze[i][j],
    print
'''
