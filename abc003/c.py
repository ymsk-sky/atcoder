n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
c=0
for r in l[n-k:]:
    c=(c+r)/2
print(c)
