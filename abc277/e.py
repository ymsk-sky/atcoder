from collections import deque

n, m, k = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, a = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append((v, a))
    edges[v].append((u, a))
sl = [0] * n
tmp = list(map(int, input().split()))
for i in tmp:
    sl[i - 1] = 1

INF = float("inf")
dist = [[INF, INF] for _ in range(n)]
dist[0][1] = 0

q = deque()
q.append((0, 1))

while q:
    crt, on = q.popleft()
    d = dist[crt][on]
    for nxt, a in edges[crt]:
        if a == on and dist[nxt][on] > d + 1:
            dist[nxt][on] = d + 1
            q.append((nxt, on))
        if sl[crt] == 1 and (a == 1 - on) and dist[nxt][1 - on] > d + 1:
            dist[nxt][1 - on] = d + 1
            q.append((nxt, 1 - on))

ans = min(dist[n - 1])
print(-1 if ans == INF else ans)

"""
2<=n<=2*10**5
1<=m<=2*10**5
0<=k<=n
1<=u,v<=n

5 5 2
1 3 0
2 3 1
5 4 1
2 1 1
1 4 0
3 4
"""
