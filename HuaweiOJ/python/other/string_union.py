# -*- coding: cp936 -*-


def bin(x):
    result=''
    x=int(x)
    while x>0:
        mod=x%2
        x/=2
        result=str(mod)+result
    result='0'*(4-len(result))+result
    return result

s1,s2=raw_input().split()
#s2=raw_input()
s=s1+s2
s_odd=''
s_even=''
#将合并后的字符串按奇偶分别提取出来
for i in range(len(s)):
    if i%2==0:
        s_odd+=s[i]
    elif i%2==1:
        s_even+=s[i]
    else:
        pass
s_odd=list(s_odd)
s_odd.sort()
s_even=list(s_even)
s_even.sort()
s=[]
#排序后重新组合
for i in range(len(s_even)):
    s.append(s_odd[i])
    s.append(s_even[i])
if len(s_odd)>len(s_even):
    s.append(s_odd[-1])
#将每一个字符转换成二进制
out=''
Flag=0
for i in range(len(s)):
    if not('0'<=s[i]<='9' or 'a'<=s[i]<='f' or 'A'<=s[i]<='F'):
        Flag=1
    else:
        r_out=bin(int(s[i],16))
        r_out=list(r_out)
        r_out_reverse=r_out[::-1]
        out+=hex((int("".join(r_out_reverse),2)))[-1].upper()
if Flag==0:
    print out
else:
    pass
