# -*- coding: cp936 -*-
'''
MP3光标
MP3 Player因为屏幕较小，显示歌曲列表的时候每屏只能显示几首歌曲，
用户要通过上下键才能浏览所有的歌曲。为了简化处理，假设每屏只能显示4首歌曲，
光标初始的位置为第1首歌。

现在要实现通过上下键控制光标移动来浏览歌曲列表，控制逻辑如下：
歌曲总数<=4的时候，不需要翻页，只是挪动光标位置。

光标在第一首歌曲上时，按Up键光标挪到最后一首歌曲；
光标在最后一首歌曲时，按Down键光标挪到第一首歌曲。
其他情况下用户按Up键，光标挪到上一首歌曲；用户按Down键，光标挪到下一首歌曲。

歌曲总数大于4的时候（以一共有10首歌为例）：
特殊翻页：
屏幕显示的是第一页（即显示第1 –4首）时，光标在第一首歌曲上，
用户按Up键后，屏幕要显示最后一页（即显示第7-10首歌），同时光标放到最后一首歌上。
同样的，屏幕显示最后一页时，光标在最后一首歌曲上，用户按Down键，屏幕要显示第一页，
光标挪到第一首歌上。

一般翻页：屏幕显示的不是第一页时，光标在当前屏幕显示的第一首歌曲时，
用户按Up键后，屏幕从当前歌曲的上一首开始显示，光标也挪到上一首歌曲。
光标当前屏幕的最后一首歌时的Down键处理也类似。

其他情况，不用翻页，只是挪动光标就行。

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
