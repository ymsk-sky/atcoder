from itertools import product
n,m=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(m)]
k=int(input())
cdl=[list(map(int,input().split())) for _ in range(k)]
ans=0
for prt in product((0,1),repeat=k):  # 全パターン(2^k)試す
    s=set([cd[b] for b,cd in zip(prt,cdl)])  # ボールが乗っている皿
    cnt=0
    for a,b in abl:
        if a in s and b in s:
            cnt+=1
    ans=max(ans,cnt)
print(ans)
