n,l=map(int,input().split())
f=1
as_=[]
m=float('inf')
for i in range(n):
    a=l+i
    as_.append(a)
    m=min(m,abs(a))
    if a<0:
        f=-1
    else:
        f=1
print(sum(as_)-f*m)
