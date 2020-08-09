n,k=map(int,input().split())
d={}
for _ in range(n):
    a,b=map(int,input().split())
    if a in d:
        d[a]+=b
    else:
        d[a]=b
s=0
for i in sorted(d):
    s+=d[i]
    if s>=k:
        print(i)
        exit()
