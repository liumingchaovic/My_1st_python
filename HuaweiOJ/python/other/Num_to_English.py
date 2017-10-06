# -*- coding: cp936 -*-
'''
学英语
'''
def Num_to_English(Num):
    if Num<0:
        s='error'
        return s
    if Num<20:
        if Num==0:
            s='zero'
            return s
        elif Num==1:
            s='one'
            return s
        elif Num==2:
            s='two'
            return s
        elif Num==3:
            s='three'
            return s
        elif Num==4:
            s='four'
            return s
        elif Num==5:
            s='five'
            return s
        elif Num==6:
            s='six'
            return s
        elif Num==7:
            s='seven'
            return s
        elif Num==8:
            s='eight'
            return s
        elif Num==9:
            s='nine'
            return s
        elif Num==10:
            s='ten'
            return s
        elif Num==11:
            s='eleven'
            return s
        elif Num==12:
            s='twelve'
            return s
        elif Num==13:
            s='thirteen'
            return s
        elif Num==14:
            s='fourteen'
            return s
        elif Num==15:
            s='fifteen'
            return s
        elif Num==16:
            s='sixteen'
            return s
        elif Num==17:
            s='seventeen'
            return s
        elif Num==18:
            s='eighteen'
            return s
        elif Num==19:
            s='nineteen'
            return s
        else:
            pass
    elif Num<100:
        if Num%10==0:
            if Num==20:
                s='twenty'
                return s
            elif Num==30:
                s='thirty'
                return s
            elif Num==40:
                s='forty'
                return s
            elif Num==50:
                s='fifty'
                return s
            elif Num==60:
                s='sixty'
                return s
            elif Num==70:
                s='seventy'
                return s
            elif Num==80:
                s='eighty'
                return s
            elif Num==90:
                s='ninety'
                return s
            else:
                pass
        else:
            s=Num_to_English(Num/10*10)+' '+Num_to_English(Num%10)
            return s
    elif Num<1000:
        if Num%100==0:
            s=Num_to_English(Num/100)+' hundred'
            return s
        else:
            s=Num_to_English(Num/100)+' hundred and '+Num_to_English(Num%100)
            return s
    elif Num<1000000:
        if Num%1000==0:
            s=Num_to_English(Num/1000)+' thousand'
            return s
        else:
            s=Num_to_English(Num/1000)+' thousand '+Num_to_English(Num%1000)
            return s
    elif Num<1000000000:
        if Num%1000000==0:
            s=Num_to_English(Num/1000000)+' million'
            return s
        else:
            s=Num_to_English(Num/1000000)+' million '+Num_to_English(Num%1000000)
            return s
    elif Num<10000000000:
        if Num%1000000000==0:
            s=Num_to_English(Num/10000000000)+' billion'
            return s
        else:
            s=Num_to_English(Num/1000000000)+' billion '+Num_to_English(Num%1000000000)
            return s
    else:
        s='error'
        return s

a=input()
s=''
print Num_to_English(a)
