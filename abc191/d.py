X,Y,R=map(float,input().split())
ans=0
xl=int(X)
xr=int(X)
R2=R**2
for y in range(int(Y-R),int(Y)+1):
    while 1:
        if (X-xl)**2+(Y-y)**2>R2:
            xl+=1
            break
        else:
            xl-=1
    while 1:
        if (X-xr)**2+(Y-y)**2>R2:
            xr-=1
            break
        else:
            xr+=1
    tmp=xr-xl
    cur=tmp+1 if tmp>0 else 0
    ans+=cur
xl-=1
xr+=1
for y in range(int(Y)+1,int(Y+R)+1):
    while 1:
        if (X-xl)**2+(Y-y)**2>R2:
            break
        else:
            xl+=1
    while 1:
        if (X-xr)**2+(Y-y)**2>R2:
            break
        else:
            xr-=1
    tmp=xr-xl
    cur=tmp+1 if tmp>0 else 0
    ans+=cur
print(ans)
