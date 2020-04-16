n,k,m=map(int,input().split())
as_=list(map(int,input().split()))
t=m*n-sum(as_)
if t>0:
    if t<=k:
        print(t)
    else:
        print(-1)
else:
    print(0)
