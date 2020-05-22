n,m=map(int,input().split())
f=2**n-1
for _ in range(m):
    l,r=map(int,input().split())
    b=0
    for i in range(l-1,r):
        b=b+(1<<i)
    f=f&b
a=0
while f:
    a+=f&1
    f=f>>1
print(a)
