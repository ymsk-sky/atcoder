from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)

n, x, y = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
q = deque([])
fin = False

def dfs(x, y):
    global fin
    if not fin:
        q.append(x)
    if x == y:
        fin = True
    visited[x] = True
    for z in graph[x]:
        if not visited[z]:
            dfs(z, y)
    if not fin:
        q.pop()

dfs(x, y)
print(*q)