n,m=map(int,input().split())
d={k:0 for k in range(1,n+1)}
for _ in range(m):
    a,b=map(int,input().split())
    d[a]+=1
    d[b]+=1
for v in d.values():
    print(v)
