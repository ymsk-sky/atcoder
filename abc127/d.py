from bisect import bisect_left
n,m=map(int,input().split())
al=sorted(list(map(int,input().split())))
bcs=[list(map(int,input().split())) for _ in range(m)]
bcs.sort(key=lambda x:x[1],reverse=True)
ans=sum(al)
si=0  # 開始インデックス
for b,c in bcs:
    ei=bisect_left(al,c)
    if ei-si<b:
        b=ei-si
    tmp=al[si:si+b]
    if len(tmp)!=0:
        ans-=sum(al[si:si+b])
        ans+=c*b
    si+=b
print(ans)
"""
10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4
al=[1,4,5,5,7,8,13,33,52,100]
bcs=[[4,30],[3,10],[1,4]]
[1,4,5,5] ei=7
[7,8]
[]
"""
