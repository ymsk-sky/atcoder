n,m=map(int,input().split())
l=[list(map(str,input().split())) for _ in range(m)]
ac=0
wa=0
d={} # i番目:WA数
for p,s in l:
    p=int(p)
    if p in d:
        pass
    else:
        d[p]=0
    if s=='AC':
        if d[p]>=0:
            ac+=1
            wa+=d[p]
            d[p]=-1
    else:
        if d[p]>=0:
            d[p]+=1
print(ac,wa)
