n=int(input())
l=list(map(int,input().split()))
a,b=l[0],sum(l[1:])
m=abs(a-b)
for v in l[1:-1]:
    a+=v
    b-=v
    m=min(m,abs(a-b))
print(m)
