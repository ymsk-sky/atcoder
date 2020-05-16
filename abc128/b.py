n=int(input())
sps=dict()
for i in range(n):
    s,p=input().split()
    if not s in sps:
        sps[s]=[]
    sps[s].append([int(p),i+1])
for k in sorted(list(sps.keys())):
    for _,v in sorted(sps[k], reverse=True):
        print(v)
