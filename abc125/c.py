"""
- ひとつの数値を置き換える -> ひとつ以外の最大公約数のなかの最大のものを求める
- ユークリッドの互除法を使う
"""
from math import gcd
n=int(input())
al=list(map(int,input().split()))
l=[0]*(n+1)
r=[0]*(n+1)
l[0]=al[0]
r[-1]=al[-1]
ans=1
for i in range(1,n+1):
    l[i]=gcd(l[i-1],al[i-1])
for i in range(1,n+1):
    r[n-i]=gcd(r[n-i+1],al[n-i])
l=l[1:]
r=r[:-1]
for i in range(n):
    if i==0:
        a=r[1]
    elif i==n-1:
        a=l[-2]
    else:
        a=gcd(l[i-1],r[i+1])
    ans=max(ans,a)
print(ans)
