from math import gcd
n=int(input())
a=1
for _ in range(n):
    t=int(input())
    a=a*t//gcd(a,t)
print(a)
