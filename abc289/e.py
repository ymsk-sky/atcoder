from collections import deque

INF = float("inf")
t = int(input())  # 1000
for _ in range(t):
    n, m = map(int, input().split())
    cl = list(map(int, input().split()))  # cl[i] = 0:赤 or 1:青
    edges = [[] for _ in range(n)]
    for _ in range(m):  # 2000
        u, v = map(int, input().split())
        u, v = u - 1, v - 1
        edges[u].append(v)
        edges[v].append(u)
    # BFS
    t_dist = [INF] * n  # for takahashi
    a_dist = [INF] * n  # for aoki
    t_dist[0] = a_dist[n - 1] = 0

    que = deque([(0, n - 1)])
    while que:
        t_crt, a_crt = que.popleft()
        for t_nxt in edges[t_crt]:
            if t_dist[t_nxt] <= t_dist[t_crt] + 1:
                continue
            for a_nxt in edges[a_crt]:
                if a_dist[a_nxt] <= a_dist[a_crt] + 1:
                    continue
                if cl[t_nxt] == cl[a_nxt]:
                    continue
                if t_nxt == n - 1 and a_nxt != 0:
                    continue
                if t_nxt != n - 1 and a_nxt == 0:
                    continue
                t_dist[t_nxt] = a_dist[a_nxt] = t_dist[t_crt] + 1
                que.append((t_nxt, a_nxt))
    if t_dist[n - 1] == a_dist[0] and t_dist[n - 1] != INF:
        print(t_dist[n - 1])
    else:
        print(-1)
