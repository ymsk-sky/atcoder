import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((c, b))
    edges[b].append((c, a))

ans = 0
vis = set()  # 既
def dfs(crt, s):
    global ans
    vis.add(crt)
    if s > ans:
        ans = s
    for cost, nxt in edges[crt]:
        if nxt in vis:
            continue
        dfs(nxt, s + cost)
    vis.remove(crt)
for i in range(n):
    dfs(i, 0)
print(ans)
