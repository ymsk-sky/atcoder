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
    # vis[i][j]: Tがi, Aがjに行けるか
    vis = [[0] * n for _ in range(n)]
    vis[0][n - 1] = 1
    que = deque([(0, 0, n - 1)])
    while que:
        cost, crt_t, crt_a = que.popleft()

        if crt_t == n - 1 and crt_a == 0:
            print(cost)
            break
        
        for nxt_t in edges[crt_t]:
            for nxt_a in edges[crt_a]:
                if cl[nxt_t] == cl[nxt_a]:
                    continue
                if vis[nxt_t][nxt_a]:
                    continue
                vis[nxt_t][nxt_a] = 1
                que.append((cost + 1, nxt_t, nxt_a))
    else:
        print(-1)

