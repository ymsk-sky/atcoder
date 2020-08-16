n,m=map(int,input().split())
if m<2:
    print(0)
    exit()
if n>m//2:
    print(m//2)
    exit()
c=n%(m//2)
d=m-2*c
c+=d//4
print(c)
