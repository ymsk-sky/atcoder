from numpy import pi
n=int(input())
l=sorted([int(input()) for _ in range(n)],reverse=True)
s=0
k=1
for r in l:
    s+=k*pi*r**2
    k*=-1
print(s)
