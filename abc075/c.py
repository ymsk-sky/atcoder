n,m=map(int,input().split())
all_bridges=[list(map(int,input().split())) for _ in range(m)]
cnt=0
visited=[0]*n
def dfs(v):
    visited[v]=1
    for u in range(v):
        if visited[u]==1:
            continue
        dfs(u)

for i in range(m):
    bridges=all_bridges[:i]+all_bridges[i+1:]
    visited=[0]*n
    dfs(0)
print(cnt)
