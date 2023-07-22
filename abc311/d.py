from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
sl = [input() for _ in range(n)]

vis = [[0] * m for _ in range(n)]
stp = [[0] * m for _ in range(n)]
vis[1][1] = 1
stp[1][1] = 1

def dfs(i, j, k):
    if k == 0:
        u, v = i + 1, j
    elif k == 1:
        u, v = i - 1, j
    elif k == 2:
        u, v = i, j + 1
    else:
        u, v = i, j - 1
    if sl[u][v] == "#":
        return i, j
    else:
        vis[u][v] = 1
        return dfs(u, v, k)

que = deque([(1, 1)])
while que:
    i, j = que.popleft()
    for k in range(4):
        u, v = dfs(i, j, k)
        if stp[u][v] == 0:
            stp[u][v] = 1
            que.append((u, v))

ans = 0
for i in range(n):
    for j in range(m):
        ans += vis[i][j]
print(ans)

"""
3<=n,m<=200

  1
 3k2
  0
"""
