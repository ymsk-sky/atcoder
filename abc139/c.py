n=int(input())
hs=list(map(int,input().split()))
ans=0
tmp=0
for h,x in zip(hs,hs[1:]+[10**9+1]):
    if h>=x:
        tmp+=1
    elif tmp>ans:
        ans=tmp
        tmp=0
    else:
        tmp=0
print(ans)
