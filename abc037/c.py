n,k=map(int,input().split())
l=list(map(int,input().split()))
m=sum(l[:k])
a=m
for h,t in zip(l,l[k:]):
    a=a-h+t
    m+=a
print(m)
