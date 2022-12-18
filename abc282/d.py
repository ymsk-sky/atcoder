import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)

colors = [-1] * n
def dfs(crt, color):
    pair = [0, 0]  # この連結成分内の[0の個数, 1の個数]
    colors[crt] = color
    pair[color] += 1
    for nxt in edges[crt]:
        if colors[nxt] == color:
            # 与えられたグラフ自体が二部グラフでない
            print(0)
            exit()
        if colors[nxt] == -1:
            w, b = dfs(nxt, 1 - color)
            pair[0] += w
            pair[1] += b
    return pair

ans = n*(n - 1)//2 - m
for i in range(n):
    if colors[i] == -1:
        w, b = dfs(i, 0)
        ans -= w*(w - 1)//2
        ans -= b*(b - 1)//2
print(ans)

"""
2<=n<=2*10**5
0<=m<=min(2*10**5, n(n-1)/2)
1<=u,v<=n
グラフは単純
"""
