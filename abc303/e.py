from collections import deque

n = int(input())
edges = [[] for _ in range(n)]
in_nums = [0] * n  # 次数
for _ in range(n - 1):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
    in_nums[u] += 1
    in_nums[v] += 1

leaf = [i for i in range(n) if in_nums[i] == 1][0]
center = edges[leaf][0]

INF = float("inf")
dist = [INF] * n
dist[center] = 0

que = deque([center])
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if dist[nxt] <= dist[crt] + 1:
            continue
        dist[nxt] = dist[crt] + 1
        que.append(nxt)

ans = []
for i in range(n):
    if dist[i]%3 == 0:
        ans.append(len(edges[i]))
ans.sort()
print(*ans)

"""
3<=n<=2*10**5
"""
