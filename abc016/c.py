n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
d={i:set() for i in range(1,n+1)}
for a,b in l:
    d[a].add(b)
    d[b].add(a)
for i in range(1,n+1):
    s=set()
    for f in d[i]:
        s|=d[f]
    for j in set([i])|d[i]:
        s.discard(j)
    print(len(s))
