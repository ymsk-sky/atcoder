import sys
sys.setrecursionlimit(10**6)

n = int(input())
edges = []
for i in range(n):
    c, *pl = list(map(int, input().split()))
    pl = [p - 1 for p in pl]
    edges.append(pl)
ans = []
vis = [0] * n
def dfs(crt):
    for nxt in edges[crt]:
        if vis[nxt]:
            continue
        dfs(nxt)
    vis[crt] = 1
    ans.append(crt + 1)
dfs(0)
print(*ans[:-1])
