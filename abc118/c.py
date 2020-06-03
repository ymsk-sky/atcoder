from math import gcd  # fractions
n=int(input())
l=list(map(int,input().split()))
s=l[0]
for a in l[1:]:
    s=gcd(s,a)
print(s)
