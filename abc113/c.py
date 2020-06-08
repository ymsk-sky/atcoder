n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
l2=sorted(l,key=lambda x:x[1])
d=dict()
for p,y in l2:
    if not p in d.keys():
        d[p]=dict()
    d[p][y]=len(d[p])+1
for p,y in l:
    print('{}'.format(p).zfill(6)+'{}'.format(d[p][y]).zfill(6))
