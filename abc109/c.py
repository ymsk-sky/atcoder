from math import gcd#fractions
N,X=map(int,input().split())
xs=list(map(int,input().split()))
xs=[abs(x-X) for x in xs]
s=xs[0]
for x in xs[1:]:
    s=gcd(s,x)
print(s)
