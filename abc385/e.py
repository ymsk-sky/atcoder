INF = float("inf")

n = int(input())
edges = [[] for _ in range(n)]
nums = [0] * n  # 辺の数=次数
for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
    nums[u] += 1
    nums[v] += 1

ans = INF
for u in range(n):
    # 頂点uが木の根
    vl = edges[u]
    dl = sorted([nums[v] for v in vl], reverse=True)
    for x in range(1, len(vl) + 1):
        y = dl[x - 1] - 1
        tmp = n - (1 + x + x*y)
        ans = min(ans, tmp)
print(ans)
