n=int(input())
al=list(map(int,input().split()))
d={}
for i,a in enumerate(al,start=1):
    if a in d:
        d[a].append(i)
    else:
        d[a]=[i]
ans=0
for k in d:
    l=len(d[k])
    for i,a in enumerate(d[k],start=1):
        after=n-a  # a以降の数字の個数
        same=l-i  # after内のaと同じ数字の個数
        cnt=after-same  # aと違う数字の個数
        ans+=cnt
print(ans)
"""
20
7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4
173
"""
