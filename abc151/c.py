n,m=map(int,input().split())
ps=[input().split() for _ in range(m)]
ps=[[int(x), y] for x,y in ps]
wa=0
ac=0
for i,(p,s) in enumerate(ps):
    if s=='WA':
