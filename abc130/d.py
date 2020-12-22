"""
S(l,r) < S(l,r+1)
S(l,r) > S(l+1,r)
が成り立つのでS(l,r)>=Kならばすべてのx(x>=r)でS(l,x)>=Kが成立
よって最小のrを見つけられれば、左側l固定のときの条件を満たす個数がわかる：(n-r+1)個

これをlを一個ずつずらしながら行なう
"""
n,k=map(int,input().split())
al=list(map(int,input().split()))
ans=0
sum_=0
r=0
for l in range(n):
    while sum_<k:
        if r==n:
            break
        sum_+=al[r]
        r+=1
    if sum_<k:
        break
    ans+=n-r+1
    sum_-=al[l]
print(ans)
