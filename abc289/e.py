import heapq

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
    # 経路
    dist = [INF] * n
    que = []
    heapq.heapify(que)
    heapq.heappush(que, [0, 0, n - 1])  # 距離, 高橋位置, 青木位置
    while que:
        cost, taka, aoki = heapq.heappop(que)
        if dist[taka] <= cost:
            continue
        dist[taka] = cost
        if taka == n - 1 and aoki == 0:
            print(cost)
            break
        for t_nxt in edges[taka]:
            if dist[t_nxt] <= cost:
                continue
            for a_nxt in edges[aoki]:
                if cl[t_nxt] == cl[a_nxt]:
                    continue
                if t_nxt == n - 1 and a_nxt != 0:
                    continue
                if a_nxt == 0 and t_nxt != n - 1:
                    continue
                heapq.heappush(que, [cost + 1, t_nxt, a_nxt])
    else:
        print(-1)
