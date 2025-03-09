import sys

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append((w, v))
    edges[v].append((w, u))

ans = 1 << 60
vis = [False] * n
def dfs(crt: int, cost: int) -> None:
    if crt == n - 1:
        global ans
        ans = min(ans, cost)
        return
    vis[crt] = True
    for nxt_cost, nxt in edges[crt]:
        if vis[nxt]:
            continue
        dfs(nxt, cost ^ nxt_cost)
    vis[crt] = False

dfs(0, 0)
print(ans)
