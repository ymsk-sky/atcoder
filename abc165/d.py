a,b,n=map(int,input().split())
ans=0
for x in range(1,n+1):
    ans=max(ans,((a*x)//b)-a*(x//b))
print(ans)
