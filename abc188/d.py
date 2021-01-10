n,C=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
""""""
F=min([a for a,_,_ in l])  # 最初
L=max([b for _,b,_ in l])  # 最後
print(F,'~',L,L-F,'days')
exit()
""""""
imosu=[0]*(n+1)
for a,b,c in l:
    imosu[a-1]+=c
    imosu[b]-=c
for i,v in zip(range(1,n),imosu):
    imosu[i]+=v
imosu=[v if v<C else C for v in imosu][:-1]
print(sum(imosu))
