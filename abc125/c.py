"""
- ひとつの数値を置き換える -> ひとつ以外の最大公約数のなかの最大のものを求める
- ユークリッドの互除法を使う
"""
from math import gcd
n=int(input())
al=list(map(int,input().split()))
ans=0
for i in range(n):
    tmp=al[1] if i==0 else al[0]
    for j in range(n):
        if j==i:
            continue
        tmp=gcd(tmp,al[j])
    ans=max(ans,tmp)
print(ans)
