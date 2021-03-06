n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
ans=float('inf')
for i in range(n):
    for j in range(n):
        if i==j:
            ans=min(ans,l[i][0]+l[j][1])
        else:
            ans=min(ans,max(l[i][0],l[j][1]))
print(ans)
