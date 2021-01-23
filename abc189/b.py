n,x=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
for i,(v,p) in enumerate(l,start=1):
    x-=v*p/100
    if x<0:
        print(i)
        exit()
print(-1)
