n=int(input())
al=list(map(int,input().split()))
ans=0
l=0
m=float('inf')
for r in range(1,n+1):  # 1<=r<=n
    part=al[l:r]
    min_=min(part)
    len_=r-l
    point=min_*len_
    ans=max(ans,point)
    if m>min_:  # updated min_
        m=min_
        l+=1
print(ans)
