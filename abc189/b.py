n,x=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
s=0
for i,(v,p) in enumerate(l,start=1):
    s+=v*p
    if s>x*100:
        print(i)
        exit()
print(-1)
