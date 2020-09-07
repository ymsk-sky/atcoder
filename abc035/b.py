s=input()
t=int(input())
x=y=m=0
for c in s:
    if c=='L':
        x-=1
    if c=='R':
        x+=1
    if c=='U':
        y+=1
    if c=='D':
        y-=1
    if c=='?':
        m+=1
z=abs(x)+abs(y)
if t==1:
    print(z+m)
else:
    if z>=m:
        print(z-m)
    else:
        d=m-z
        print(d%2)
