r1,c1=map(int,input().split())
r2,c2=map(int,input().split())
flag=0
dr=abs(r1-r2)  # x軸の差
dc=abs(c1-c2)  # y軸の差
if dr==0 and dc==0:
    print(0)
    exit()
if dr==0 or dc==0:
    flag+=1
else:  # 近い軸側を基準に同じ値にする
    if dr<dc:
        c1+=(r2-r1)
        r1=r2
    else:
        r1+=(c2-c1)
        c1=c2
s1=r1+c1
s2=r2+c2
s=s2-s1
if s==0:
    flag+=1
elif abs(s)<=3:
    flag+=1
else:
    if s%2==0:
        s//=2
        r1,c1=r1+s,c1+s
    else:
        if s>0:
            s=s//2+1
        else:
            s=s//2-1
        r1,c1=r1+s,c1+s
if r1==r2 and c1==c2:
    flag+=1
print(3-flag)
