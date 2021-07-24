from bisect import bisect_left
s=input()
mod=10**9+7
chokudai='chokudai'
d={c:[] for c in chokudai}
d2={c:[] for c in chokudai}
for i,c in enumerate(s):
    if c in d:
        d[c].append(i)
        if c=='i':
            d2[c].append(1)
        else:
            d2[c].append(0)
for k1,k2 in zip(chokudai[::-1][1:],chokudai[::-1]):
    for i,dk1 in enumerate(d[k1]):
        bi=bisect_left(d[k2],dk1)
        for cnt in d2[k2][bi:]:
            d2[k1][i]+=cnt
ans=0
for tmp in d2['c']:
    ans+=tmp
    ans%=mod
print(ans)

"""
chokudaichokudaichokudai
45
c: 0,8,16
h: 1,9,17
o: 2,10,18
k: 3,11,19
u: 4,12,20
d: 5,13,21
a: 6,14,22
i: 7,15,23
"""
