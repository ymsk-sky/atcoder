n,m=map(int,input().split())
isekis=[list(map(int,input().split())) for _ in range(n)]
ans=0
for gem in range(1,m+1):
    sum_=0
    for l,r,s in isekis:
        if l<=gem<=r:
            pass
        else:
            sum_+=s
    ans=max(ans,sum_)
print(ans)
