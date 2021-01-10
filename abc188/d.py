n,C=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
imosu=[0]*(n+1)
for a,b,c in l:
    imosu[a-1]+=c
    imosu[b]-=c
for i,v in zip(range(1,n),imosu):
    imosu[i]+=v
imosu=[v if v<C else C for v in imosu][:-1]
print(sum(imosu))
