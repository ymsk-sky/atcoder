from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]  # 有向辺
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)

ans = 0
for i in range(n):
    f = [0] * n  # 到達可能か
    f[i] = 1
    que = deque([i])
    while que:
        crt = que.popleft()
        for nxt in edges[crt]:
            if f[nxt]:
                continue
            f[nxt] = 1
            que.append(nxt)
            ans += 1
print(ans - m)


"""
3<=n<=2000
0<=m<=2000

5 8
1 2
2 1
1 3
3 1
1 4
4 1
1 5
5 1
12
"""
