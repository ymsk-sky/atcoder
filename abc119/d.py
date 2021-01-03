"""
a 神社
b 寺
s 西からsiの地点の神社
t 西からtiの地点の寺
q個の問い: xi地点スタートで最短の神社と寺を訪れる距離は？(1神社1寺を超えて良い)
"""
from bisect import bisect_right
a,b,q=map(int,input().split())
INF=float('inf')
sl=[-INF]+[int(input()) for _ in range(a)]+[INF]
tl=[-INF]+[int(input()) for _ in range(b)]+[INF]
xl=[int(input()) for _ in range(q)]
for x in xl:
    i_b=bisect_right(sl,x)
    i_d=bisect_right(tl,x)
    r=INF
    for i_s in [sl[i_b], sl[i_b-1]]:
        for i_t in [tl[i_d], tl[i_d-1]]:
            d1=abs(i_s-x)+abs(i_t-i_s)
            d2=abs(i_t-x)+abs(i_s-i_t)
            r=min(r,d1,d2)
    print(r)
