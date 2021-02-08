X,Y,R=map(float,input().split())
M=10**4
X=int(X*M)
Y=int(Y*M)
R=int(R*M)
ans=0
xmin=(X-R)//M*M
xmax=(X+R)//M*M
if xmin<0:
    xmin+=M
if xmax<0:
    xmax+=M
R2=R**2
for x in range(xmin,xmax+1,10**4):
    y=(R2-(X-x)**2)**(1/2)
    ymin=(Y-y)//M*M
    ymax=(Y+y)//M*M
    if ymin<0:
        ymin+=M
    if ymax<0:
        ymax+=M
    cnt=(ymax-ymin)//M
    ans+=cnt
print(int(ans))


"""
0.2 0.8 1.1
3
"""
