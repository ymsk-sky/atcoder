n,k=map(int,input().split())
al=list(map(int,input().split()))
ans=0
sum_=0
r=0
for l in range(n):
    while sum_<k:
        if r==n:
            break
        sum_+=al[r]
        r+=1
    if sum_<k:
        break
    ans+=n-r+1
    sum_-=al[l]
print(ans)
