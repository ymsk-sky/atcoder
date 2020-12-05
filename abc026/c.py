n=int(input())
bs=[0]+[int(input()) for _ in range(n-1)]
ps=[0]*n
for i in range(n,0,-1):
    l=[p for b,p in zip(bs,ps) if b==i]
    if len(l)==0:
        ps[i-1]=1
    else:
        ps[i-1]=max(l)+min(l)+1
print(ps[0])
