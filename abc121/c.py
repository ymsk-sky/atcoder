n,m=map(int,input().split())
l=sorted([list(map(int,input().split())) for _ in range(n)])
ans=0
for a,b in l:
    if b<m:
        ans+=(a*b)
        m-=b
    else:
        ans+=(a*m)
        break
print(ans)
