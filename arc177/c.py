import heapq

n = int(input())
cl = [list(input()) for _ in range(n)]
INF = float("inf")

def dijkstra(si, sj):
    color = cl[si][sj]
    dist = [[INF] * n for _ in range(n)]
    dist[si][sj] = 0
    que = [(0, si, sj)]
    heapq.heapify(que)
    while que:
        cost, i, j = heapq.heappop(que)
        if dist[i][j] < cost:
            continue
        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            u, v = i + p, j + q
            if 0 > u or u >= n or 0 > v or v >= n:
                continue
            if cl[u][v] == color:
                if dist[u][v] <= cost:
                    continue
                dist[u][v] = cost
                heapq.heappush(que, (cost, u, v))
            else:
                if dist[u][v] <= cost + 1:
                    continue
                dist[u][v] = cost + 1
                heapq.heappush(que, (cost + 1, u, v))
    return dist

red = dijkstra(0, 0)
blue = dijkstra(0, n - 1)
ans = red[n - 1][n - 1] + blue[n - 1][0]
print(ans)

"""
3<=n<=500

5
RRRRR
BBBBB
BBBBB
BBBBB
RRRRR
"""