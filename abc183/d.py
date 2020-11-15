n,w=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
imosu=[0]*(2*10**5+1)
for s,t,p in l:
    imosu[s]+=p
    imosu[t]-=p
for i in range(1,2*10**5+1):
    imosu[i]+=imosu[i-1]
print('No' if max(imosu)>w else 'Yes')
