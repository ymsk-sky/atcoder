import sys
sys.setrecursionlimit(10**6)  # 再帰回数の上限を設定

n,m=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(m)]
d=[[] for _ in range(n)]  # 都市iから直接繋がっている都市リスト
for a,b in abl:
    d[a-1].append(b-1)

def dfs(v):
    if tmp[v]: return
    tmp[v]=True
    for u in d[v]:
        dfs(u)

ans=0
for i in range(n):
    tmp=[False]*n
    dfs(i)
    ans+=sum(tmp)
print(ans)
