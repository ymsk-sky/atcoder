N,D,H=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(N)]
a=float('inf')
for d,h in l:
    tmp=(h-H)/(d-D)
    a=min(a,tmp)
ans=H-a*D
print(ans if ans>0 else 0.0)
