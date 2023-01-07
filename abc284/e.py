import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
M = 10**6
ans = 0
visited = [False] * n
def dfs(crt):
    global ans
    ans += 1
    if ans >= M:
        print(M)
        exit()
    visited[crt] = True
    for nxt in edges[crt]:
        if visited[nxt]:
            continue
        dfs(nxt)
    visited[crt] = False

dfs(0)
print(ans)

"""
1<=n<=2*10**5
0<=m<=min(2*10**5, n(n-1)/2)
各頂点の次数は10以下
"""
