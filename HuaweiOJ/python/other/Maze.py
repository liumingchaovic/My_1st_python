# -*- coding: cp936 -*-
'''
�Թ�����
����һ����ά����N*M������2<=N<=10;2<=M<=10������5 �� 5��������ʾ�� 
int maze[5][5] = {
        0, 1, 0, 0, 0,
        0, 1, 0, 1, 0,
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 0,
        0, 0, 0, 1, 0,
};

����ʾһ���Թ������е�1��ʾǽ�ڣ�0��ʾ�����ߵ�·��ֻ�ܺ����߻������ߣ�����б���ߣ�Ҫ�������ҳ������Ͻǵ����½ǵ����·�ߡ���ڵ�Ϊ[0,0],�ȵ�һ�ո��ǿ����ߵ�·��
Input
һ��N �� M�Ķ�ά���飬��ʾһ���Թ������ݱ�֤��Ψһ��,�������ж�����������Թ�ֻ��һ��ͨ����
Output
���Ͻǵ����½ǵ����·������ʽ��������ʾ��
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
    mz[xi][yi]=-1  #���ñ�ǣ������߻�����
    tempx=[]
    tempy=[]
    tempx.append(xi)
    tempy.append(yi)
    pair=zip(tempx,tempy)
    Path.append(pair[0])
    if xi==x_end and yi==y_end:  #��ǰλ��Ϊ����
        if len(MinPath)==0 or len(Path)<len(MinPath):
            MinPath=Path[:]
        mz[xi][yi]=0
        Path.pop()
        return
    if yi+1<M and mz[xi][yi+1]==0:   #��
        Maze_Path(xi,yi+1)
    if xi-1>=0 and mz[xi-1][yi]==0:  #��
        Maze_Path(xi-1,yi)
    if yi-1>=0 and mz[xi][yi-1]==0:  #��
        Maze_Path(xi,yi-1)
    if xi+1<N and mz[xi+1][yi]==0:   #��
        Maze_Path(xi+1,yi)
    mz[xi][yi]=0   #������
    Path.pop()

MinPath=[] #�������·��
Path=[]    #���浱ǰ·��
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
Pre=item() #�����������·���е�ǰһ��
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
