n,m,c=map(int,input().split())
bs=list(map(int,input().split()))
ans=0
for i in range(n):
    as_=list(map(int,input().split()))
    if sum([a*b for a,b in zip(as_,bs)])+c>0:
        ans+=1
print(ans)
